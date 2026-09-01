#!/usr/bin/env python3
"""Genera pack de migración Drupal para bloque Jairo."""

from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATOS = ROOT / "03-seo" / "datos"
OUT = DATOS / "drupal-sprint-jairo-2026-09-01"

PILOT_TOURS = [
    "the-classic-salkantay-trek-5d",
    "choquequirao-trek-5d",
    "incredible-machu-picchu-2d",
]


def imp(row: dict, key: str = "Impresiones") -> int:
    v = str(row.get(key, "0")).replace(",", "")
    try:
        return int(float(v))
    except ValueError:
        return 0


def card_tour(t: dict) -> str:
    slug = t["Slug"]
    return f"""## TOUR: {t['Título'][:60]}

| Campo | Valor WP (copiar) |
|---|---|
| **URL objetivo** | `/tour/{slug}/` |
| **SEO Title** | {t.get('Título SEO', '')} |
| **Meta** | {t.get('Meta description', '')} |
| **Keyword** | {t.get('Keyword principal', '')} |
| **GSC** | {t.get('Clics', '0')} clics · {t.get('Impresiones', '0')} imp · pos {t.get('Posición', '')} |

**WP live:** {t['URL']}

### Checklist Drupal (5 min QA)
- [ ] Pathauto = `/tour/{slug}/`
- [ ] Meta title + description pegados
- [ ] Precio USD correcto
- [ ] WhatsApp visible (no solo cart)
- [ ] 200 OK en preview
"""


def card_blog(b: dict) -> str:
    slug = b["Slug"]
    clean = b.get("URL actual (limpia)", "")
    cat = b.get("URL con categoría (antigua / indexada)", "")
    return f"""## BLOG: {b['Título'][:55]}

| Campo | Valor WP (copiar) |
|---|---|
| **URL objetivo** | `/blog/{slug}/` |
| **301 desde** | `{cat}` |
| **Keyword** | {b.get('Keyword principal', '')} |
| **GSC** | {b.get('Clics', '0')} clics · {b.get('Impresiones', '0')} imp |

**WP live:** {clean}

### Checklist Drupal
- [ ] Alias `/blog/{slug}/`
- [ ] Bloque 3 tours relacionados + WA
- [ ] Canonical self
"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    tours = list(csv.DictReader(open(DATOS / "tours-jairo-2026-08-25.csv", encoding="utf-8")))
    blogs = list(csv.DictReader(open(DATOS / "blogs-jairo-2026-08-25.csv", encoding="utf-8")))
    blogs_sorted = sorted(blogs, key=imp, reverse=True)
    tour_by_slug = {t["Slug"]: t for t in tours}
    pilot_tour_rows = [tour_by_slug[s] for s in PILOT_TOURS if s in tour_by_slug]
    things = [b for b in blogs if "things-to-do-in-machu-picchu" in b.get("URL actual (limpia)", "")]

    lines = [
        "# Sprint Drupal Jairo — pack migración",
        "",
        "## Tu bloque: **18 tours + 115 blogs**",
        "",
        "### Orden HOY",
        "",
        "1. **3 tours piloto** (abajo) — aprende el flujo",
        "2. **Things MP** — ya optimizado en WP, copiar spec",
        "3. **Top 15 blogs** por impresiones en tu bloque",
        "4. Resto tours → resto blogs",
        "",
    ]
    lines.append("## Fase A — Tours piloto\n")
    for t in pilot_tour_rows:
        lines.append(card_tour(t))
    lines.append("## Fase B — Things MP\n")
    if things:
        lines.append(card_blog(things[0]))
    lines.append("## Fase C — Top 15 blogs (impresiones)\n")
    for b in blogs_sorted[:15]:
        lines.append(card_blog(b))

    (OUT / "SPRINT-HOY.md").write_text("\n".join(lines), encoding="utf-8")

    with open(OUT / "jairo-migracion-maestro.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "tipo",
                "prioridad",
                "titulo",
                "url_wp",
                "slug",
                "seo_title",
                "meta",
                "keyword",
                "clics",
                "impresiones",
                "url_categoria_301",
                "estado_drupal",
                "notas",
            ]
        )
        for t in tours:
            pri = "P0" if t["Slug"] in PILOT_TOURS else "P1"
            w.writerow(
                [
                    "tour",
                    pri,
                    t["Título"],
                    t["URL"],
                    t["Slug"],
                    t.get("Título SEO", ""),
                    t.get("Meta description", ""),
                    t.get("Keyword principal", ""),
                    t.get("Clics", ""),
                    t.get("Impresiones", ""),
                    "",
                    "pendiente",
                    "",
                ]
            )
        for i, b in enumerate(blogs_sorted):
            clean = b.get("URL actual (limpia)", "")
            pri = (
                "P0"
                if "things-to-do-in-machu-picchu" in clean
                else ("P1" if i < 20 else "P2")
            )
            w.writerow(
                [
                    "blog",
                    pri,
                    b["Título"],
                    clean,
                    b["Slug"],
                    "",
                    "",
                    b.get("Keyword principal", ""),
                    b.get("Clics", ""),
                    b.get("Impresiones", ""),
                    b.get("URL con categoría (antigua / indexada)", ""),
                    "pendiente",
                    "",
                ]
            )

    manifest = {
        "tours": len(tours),
        "blogs": len(blogs),
        "pilot_tours": PILOT_TOURS,
        "drupal_base": "http://147.135.114.64",
        "wp_base": "https://www.perugrandtravel.com",
        "admin_products": "http://147.135.114.64/admin/content → tab Products",
        "admin_blogs": "http://147.135.114.64/admin/content → filter Blog",
    }
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"OK → {OUT} ({len(tours)} tours, {len(blogs)} blogs)")


if __name__ == "__main__":
    main()
