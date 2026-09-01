#!/usr/bin/env python3
"""Genera hojas copy-paste SEO por tour para Drupal Metatag sidebar."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATOS = ROOT / "03-seo" / "datos"
TOURS_CSV = DATOS / "tours-jairo-2026-08-25.csv"
OUT = DATOS / "drupal-tour-seo-clipboard"


def tour_block(row: dict) -> str:
    slug = row["Slug"]
    return f"""---
## {row['Título']}
**Slug:** `{slug}`
**WP:** {row['URL']}
**Drupal alias objetivo:** `/tour/{slug}/`

### Pegar en Metatag → Basic tags

**Page title** (copiar todo):
```
{row.get('Título SEO', '').strip()}
```

**Description** (copiar todo):
```
{row.get('Meta description', '').strip()}
```

### QA 30 seg
- [ ] Pestaña navegador = title de arriba
- [ ] View source → meta description
- [ ] URL = /tour/{slug}/ (o anotar /product/N)
- [ ] CSV estado_drupal = seo_ok

"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    tours = list(csv.DictReader(open(TOURS_CSV, encoding="utf-8")))
    # Orden: pilotos primero, luego por impresiones
    pilots = {
        "the-classic-salkantay-trek-5d",
        "choquequirao-trek-5d",
        "incredible-machu-picchu-2d",
    }

    def imp(r):
        try:
            return int(str(r.get("Impresiones", "0")).replace(",", ""))
        except ValueError:
            return 0

    ordered = sorted(tours, key=lambda r: (0 if r["Slug"] in pilots else 1, -imp(r)))

    md = [
        "# Tours Jairo — clipboard SEO para Drupal",
        "",
        "Abre un tour en WP + Edit en Drupal. Sidebar → **Meta tags** → Basic tags.",
        "",
        f"Total: **{len(tours)} tours**",
        "",
    ]
    for row in ordered:
        md.append(tour_block(row))

    (OUT / "TOURS-SEO-CLIPBOARD.md").write_text("\n".join(md), encoding="utf-8")

    # TSV para doble pantalla
    with open(OUT / "tours-seo.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["slug", "seo_title", "meta_description", "alias", "wp_url"])
        for row in ordered:
            w.writerow([
                row["Slug"],
                row.get("Título SEO", ""),
                row.get("Meta description", ""),
                f"/tour/{row['Slug']}/",
                row["URL"],
            ])

    print(f"OK → {OUT} ({len(tours)} tours)")


if __name__ == "__main__":
    main()
