#!/usr/bin/env python3
"""Exporta hojas Excel PGT a CSV + genera insights.json y INSIGHTS.md."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from datetime import date
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DATOS = ROOT / "03-seo" / "datos"


def slugify_name(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def find_header_row(df: pd.DataFrame, markers: list[str], max_rows: int = 15) -> int:
    for i in range(min(max_rows, len(df))):
        row = " ".join(str(x).lower() for x in df.iloc[i].tolist() if pd.notna(x))
        if any(m in row for m in markers):
            return i
    return 0


# Hojas conocidas → fila header (0-indexed)
CANIB_SHEETS = {
    "Tours": 2,
    "Blogs": 2,
    "Paginas": 2,
    "Canibalizacion": 2,
    "Spam": 2,
    "URLs sin ficha": 2,
    "Consultas sitio": 2,
    "Consultas blog": 2,
}


def sheet_to_df(raw: pd.DataFrame, markers: list[str]) -> pd.DataFrame:
    hi = find_header_row(raw, markers)
    return sheet_to_df_fixed(raw, hi)


def sheet_to_df_fixed(raw: pd.DataFrame, header_row: int) -> pd.DataFrame:
    header = [str(c).strip() if pd.notna(c) else f"col_{j}" for j, c in enumerate(raw.iloc[header_row])]
    body = raw.iloc[header_row + 1 :].copy()
    n = min(len(header), body.shape[1])
    body = body.iloc[:, :n]
    body.columns = header[:n]
    return body.dropna(how="all")


def export_workbook(xlsx: Path, out_dir: Path, copy_xlsx: bool = True) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    xl = pd.ExcelFile(xlsx)
    manifest = {"source": str(xlsx), "sheets": {}, "exported": date.today().isoformat()}

    for sheet in xl.sheet_names:
        raw = pd.read_excel(xlsx, sheet_name=sheet, header=None)
        if raw.dropna(how="all").empty:
            continue

        if sheet == "Resumen":
            text = "\n".join(
                " | ".join(str(c) for c in row if pd.notna(c) and str(c).strip())
                for _, row in raw.iterrows()
                if any(pd.notna(c) and str(c).strip() for c in row)
            )
            (out_dir / "resumen.txt").write_text(text, encoding="utf-8")
            manifest["sheets"][sheet] = {"file": "resumen.txt", "rows": len(raw)}
            continue

        if sheet in CANIB_SHEETS:
            df = sheet_to_df_fixed(raw, CANIB_SHEETS[sheet])
        else:
            markers = ["url", "clics", "keyword", "consulta"]
            df = sheet_to_df(raw, markers)

        fname = f"{slugify_name(sheet)}.csv"
        out_path = out_dir / fname
        df.to_csv(out_path, index=False, encoding="utf-8")
        manifest["sheets"][sheet] = {"file": fname, "rows": len(df), "columns": list(df.columns)}

    if copy_xlsx:
        dest = out_dir / re.sub(r"\s+", "-", xlsx.name)
        shutil.copy2(xlsx, dest)

    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    return manifest


def analyze_canibalizacion(out_dir: Path) -> dict:
    path = out_dir / "canibalizacion.csv"
    if not path.exists():
        return {}
    df = pd.read_csv(path)
    col_grp = "#"
    if col_grp not in df.columns:
        return {}
    df[col_grp] = df[col_grp].ffill()
    url_col = "URL actual"
    imp_col = "Impresiones"
    clics_col = "Clics"
    groups = []
    for gid, g in df.groupby(col_grp):
        if pd.isna(gid):
            continue
        imp = pd.to_numeric(g[imp_col], errors="coerce").sum()
        clics = pd.to_numeric(g[clics_col], errors="coerce").sum()
        canon = g.iloc[0]
        groups.append(
            {
                "grupo": int(float(gid)) if str(gid).replace(".", "").isdigit() else gid,
                "urls": len(g),
                "impresiones": int(imp),
                "clics": int(clics),
                "canonica": str(canon.get(url_col, "")),
                "keyword": str(canon.get("Keyword / términos en común", canon.get("Keyword principal", ""))),
            }
        )
    groups.sort(key=lambda x: -x["impresiones"])
    return {"grupos": len(groups), "top10": groups[:10]}


def analyze_traffic_csv(out_dir: Path, fname: str, url_col_name: str) -> list[dict]:
    path = out_dir / fname
    if not path.exists():
        return []
    df = pd.read_csv(path)
    if url_col_name not in df.columns:
        return []
    clics_col, imp_col, ctr_col = "Clics", "Impresiones", "CTR"
    df = df[df[url_col_name].astype(str).str.startswith("http", na=False)].copy()
    df[clics_col] = pd.to_numeric(df[clics_col], errors="coerce").fillna(0)
    df[imp_col] = pd.to_numeric(df[imp_col], errors="coerce").fillna(0)
    top = df.nlargest(10, clics_col)
    rows = []
    for _, r in top.iterrows():
        rows.append(
            {
                "url": str(r[url_col_name]),
                "clics": float(r[clics_col]),
                "impresiones": float(r[imp_col]),
                "ctr": float(r[ctr_col]) if ctr_col in df.columns and pd.notna(r.get(ctr_col)) else None,
            }
        )
    return rows


def build_blog_redirects(out_dir: Path) -> int:
    path = out_dir / "blogs.csv"
    if not path.exists():
        return 0
    df = pd.read_csv(path)
    from_col = "URL con categoría (antigua / indexada)"
    to_col = "URL actual (limpia)"
    clics_col = "Clics"
    if from_col not in df.columns or to_col not in df.columns:
        return 0
    out = df[[from_col, to_col, clics_col]].copy()
    out.columns = ["from", "to", "clics"]
    out = out[out["from"].notna() & out["to"].notna()]
    out = out[out["from"] != out["to"]]
    out.to_csv(out_dir / "redirects-blog-301.csv", index=False, encoding="utf-8")
    return len(out)


def write_insights_md(out_dir: Path, insights: dict, title: str) -> None:
    lines = [
        f"# Insights — {title}",
        "",
        f"**Generado:** {date.today().isoformat()} · **Herramienta:** pandas + openpyxl",
        "",
    ]
    if "totals" in insights:
        lines.append("## Totales\n")
        for k, v in insights["totals"].items():
            lines.append(f"- **{k}:** {v}")
        lines.append("")
    for section in ("top_blogs", "top_tours", "top_pages", "top_queries", "low_ctr_high_imp"):
        if section in insights and insights[section]:
            lines.append(f"## {section.replace('_', ' ').title()}\n")
            lines.append("| URL / Query | Clics | Imp | CTR |")
            lines.append("|---|---:|---:|---:|")
            for row in insights[section][:15]:
                url = row.get("url") or row.get("query") or row.get("keyword", "")
                clics = row.get("clics", "")
                imp = row.get("impresiones", row.get("imp", ""))
                ctr = row.get("ctr", "")
                if ctr and isinstance(ctr, float):
                    ctr = f"{ctr*100:.2f}%"
                lines.append(f"| {url[:80]} | {clics} | {imp} | {ctr} |")
            lines.append("")
    if "canibalizacion" in insights:
        c = insights["canibalizacion"]
        lines.append(f"## Canibalización\n\n- **Grupos:** {c.get('grupos', 0)}\n")
        if c.get("top10"):
            lines.append("| Grupo | Imp | Canónica |")
            lines.append("|---:|---|---|")
            for g in c["top10"]:
                lines.append(f"| {g.get('keyword','')[:40]} | {g.get('impresiones',0)} | {g.get('canonica','')[:60]} |")
            lines.append("")
    (out_dir / "INSIGHTS.md").write_text("\n".join(lines), encoding="utf-8")


def analyze_keyword_stats(xlsx: Path, out_dir: Path) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    raw = pd.read_excel(xlsx, sheet_name=0, header=None)
    # Row 2 = headers (Keyword, Avg. monthly searches, ...)
    df = sheet_to_df_fixed(raw, 2)
    df = df[df["Keyword"].notna() & (df["Keyword"] != "Keyword")]
    df.to_csv(out_dir / "keywords-google-ads.csv", index=False, encoding="utf-8")
    shutil.copy2(xlsx, out_dir / "Keyword-Stats-2026-08-26.xlsx")

    vol_col = "Avg. monthly searches"
    df[vol_col] = pd.to_numeric(df[vol_col], errors="coerce")
    in_account = df[df["In Account"].astype(str).str.upper() == "Y"] if "In Account" in df.columns else pd.DataFrame()

    insights: dict = {
        "source": "google-ads-keyword-planner",
        "period": str(raw.iloc[1, 0]) if len(raw) > 1 else "",
        "total_keywords": len(df),
        "in_account_count": len(in_account),
        "top_volume": [
            {"keyword": str(r["Keyword"]), "volume": int(r[vol_col]) if pd.notna(r[vol_col]) else 0,
             "competition": str(r.get("Competition", "")), "in_account": str(r.get("In Account", ""))}
            for _, r in df.nlargest(15, vol_col).iterrows()
        ],
        "in_account_keywords": [
            {"keyword": str(r["Keyword"]), "volume": int(r[vol_col]) if pd.notna(r[vol_col]) else 0}
            for _, r in in_account.sort_values(vol_col, ascending=False).iterrows()
        ],
        "ad_groups_empty": [
            str(r["Keyword"]) for _, r in df.iterrows()
            if pd.isna(r.get(vol_col)) or r.get(vol_col) == 0
        ],
    }

    (out_dir / "insights.json").write_text(json.dumps(insights, indent=2, ensure_ascii=False), encoding="utf-8")
    write_keyword_stats_md(out_dir, insights, df)
    return insights


def write_keyword_stats_md(out_dir: Path, insights: dict, df: pd.DataFrame) -> None:
    lines = [
        "# Insights — Google Ads Keyword Stats (26 ago 2026)",
        "",
        f"**Periodo:** {insights.get('period', '')}",
        f"**Keywords en export:** {insights.get('total_keywords', 0)}",
        f"**Marcadas In Account (campaña activa):** {insights.get('in_account_count', 0)}",
        "",
        "## Top volumen búsqueda (EE.UU./target Ads)",
        "",
        "| Keyword | Vol/mes | Competencia | En cuenta |",
        "|---|---:|---|---|",
    ]
    for row in insights.get("top_volume", []):
        lines.append(f"| {row['keyword']} | {row['volume']:,} | {row.get('competition','')} | {row.get('in_account','')} |")

    lines += ["", "## Keywords en cuenta (Lizet) — prioridad SEO/landing", ""]
    for row in insights.get("in_account_keywords", []):
        lines.append(f"- **{row['keyword']}** — {row['volume']:,}/mes")

    empty = insights.get("ad_groups_empty", [])
    if empty:
        lines += ["", "## Grupos de anuncio sin volumen (solo estructura)", ""]
        for g in empty[:20]:
            lines.append(f"- {g}")

  # Cruzar con GSC
    lines += [
        "",
        "## Implicaciones PGT",
        "",
        "1. **salkantay trek** (8.100/mes) — keyword masiva; tour Salkantay debe ser landing P0.",
        "2. **inca trail** (2.900/mes) — hub Inca Trail + tours individuales.",
        "3. **machu picchu tours** (1.000/mes) — alinea con `/machu-picchu-packages/`.",
        "4. Grupos vacíos (atv & bike tours, cultural packages…) — nombres de ad group sin keyword con volumen; revisar estructura campaña.",
        "5. Keywords **In Account** = las que Lizet ya usa en Ads → títulos H1/meta deben hablar el mismo idioma.",
        "",
        "**Archivo datos:** `keywords-google-ads.csv`",
    ]
    (out_dir / "INSIGHTS.md").write_text("\n".join(lines), encoding="utf-8")


def analyze_canibalizacion_workbook(xlsx: Path, out_dir: Path) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    export_workbook(xlsx, out_dir, copy_xlsx=True)
    n_redirects = build_blog_redirects(out_dir)

    blogs_path = out_dir / "blogs.csv"
    tours_path = out_dir / "tours.csv"
    pages_path = out_dir / "paginas.csv"

    insights = {
        "redirects_blog": n_redirects,
        "canibalizacion": analyze_canibalizacion(out_dir),
        "top_blogs": analyze_traffic_csv(out_dir, "blogs.csv", "URL actual (limpia)"),
        "top_tours": analyze_traffic_csv(out_dir, "tours.csv", "URL"),
        "top_pages": analyze_traffic_csv(out_dir, "paginas.csv", "URL"),
    }

    # low CTR high impressions blogs
    if blogs_path.exists():
        df = pd.read_csv(blogs_path)
        imp_col, ctr_col, url_col, clics_col = "Impresiones", "CTR", "URL actual (limpia)", "Clics"
        if imp_col in df.columns:
            df[imp_col] = pd.to_numeric(df[imp_col], errors="coerce")
            df[ctr_col] = pd.to_numeric(df[ctr_col], errors="coerce")
            df[clics_col] = pd.to_numeric(df[clics_col], errors="coerce")
            low = df[(df[imp_col] > 5000) & (df[ctr_col] < 0.005)].nlargest(15, imp_col)
            insights["low_ctr_high_imp"] = [
                {
                    "url": str(r[url_col]),
                    "clics": float(r[clics_col]),
                    "impresiones": float(r[imp_col]),
                    "ctr": float(r[ctr_col]),
                }
                for _, r in low.iterrows()
            ]

    # totals from resumen
    resumen = out_dir / "resumen.txt"
    if resumen.exists():
        text = resumen.read_text(encoding="utf-8")
        totals = {}
        for line in text.splitlines():
            if "|" in line and any(x in line for x in ("Blogs", "Tours", "Páginas", "Clics")):
                parts = [p.strip() for p in line.split("|") if p.strip()]
                if len(parts) >= 2 and parts[1].replace(".", "").isdigit():
                    totals[parts[0]] = parts[1]
        insights["totals"] = totals

    (out_dir / "insights.json").write_text(json.dumps(insights, indent=2, ensure_ascii=False), encoding="utf-8")
    write_insights_md(out_dir, insights, "URLs Keywords Canibalización")
    return insights


def main():
    p = argparse.ArgumentParser(description="Analiza Excel PGT → CSV + insights")
    p.add_argument("xlsx", type=Path, help="Ruta al .xlsx")
    p.add_argument("--out", type=Path, required=True, help="Carpeta salida en 03-seo/datos/")
    p.add_argument("--type", choices=["canibalizacion", "keyword-stats", "auto"], default="auto")
    args = p.parse_args()

    name = args.xlsx.name.lower()
    kind = args.type
    if kind == "auto":
        kind = "keyword-stats" if "keyword" in name else "canibalizacion"

    if kind == "keyword-stats":
        analyze_keyword_stats(args.xlsx, args.out)
    else:
        analyze_canibalizacion_workbook(args.xlsx, args.out)

    print(f"OK → {args.out}")


if __name__ == "__main__":
    main()
