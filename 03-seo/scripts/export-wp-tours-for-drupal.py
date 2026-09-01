#!/usr/bin/env python3
"""
Exporta tours del bloque Jairo desde WP → packs listos para pegar en Drupal.

Fuentes:
  - REST /wp-json/wp/v2/tour?slug=...  → título, slug, Yoast title/meta, imagen
  - HTML público del tour              → precios, días itinerario (texto)

NO escribe en Drupal (staging sin JSON:API). Genera JSON + MD por tour.

Uso:
  python3 03-seo/scripts/export-wp-tours-for-drupal.py
  python3 03-seo/scripts/export-wp-tours-for-drupal.py --slug the-classic-salkantay-trek-5d
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import date
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOURS_CSV = ROOT / "03-seo/datos/tours-jairo-2026-08-25.csv"
OUT = ROOT / "03-seo/datos/wp-export-tours-jairo"
BASE = "https://www.perugrandtravel.com"
UA = "PGT-Migration-Export/1.0"


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", errors="replace")


def fetch_json(url: str) -> dict | list:
    return json.loads(fetch(url))


def strip_html(html: str) -> str:
    text = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.S | re.I)
    text = re.sub(r"<style[^>]*>.*?</style>", "", text, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    return unescape(re.sub(r"\s+", " ", text)).strip()


def parse_html_tour(html: str) -> dict:
    days = re.findall(r"(Day \d+:[^<]{15,200})", html, re.I)
    days = list(dict.fromkeys(d.strip() for d in days))
    prices = list(dict.fromkeys(re.findall(r"US\$\s*([\d,]+)", html)))
    images = list(
        dict.fromkeys(
            re.findall(
                r"https://www\.perugrandtravel\.com/wp-content/uploads/[^\"'\s>]+\.(?:webp|jpg|jpeg|png)",
                html,
                re.I,
            )
        )
    )
    h1_m = re.search(r"<h1[^>]*>([^<]+)</h1>", html, re.I)
    return {
        "h1": h1_m.group(1).strip() if h1_m else "",
        "itinerary_days": days,
        "prices_usd": prices,
        "image_urls": images[:12],
    }


def export_tour(slug: str, row: dict | None = None) -> dict:
    api_url = f"{BASE}/wp-json/wp/v2/tour?slug={slug}"
    items = fetch_json(api_url)
    if not items:
        raise ValueError(f"Tour no encontrado en REST: {slug}")
    api = items[0]
    page_url = api.get("link") or f"{BASE}/tour/{slug}/"
    html = fetch(page_url)
    parsed = parse_html_tour(html)
    yoast = api.get("yoast_head_json") or {}

    featured_url = ""
    fm = api.get("featured_media")
    if fm:
        try:
            media = fetch_json(f"{BASE}/wp-json/wp/v2/media/{fm}")
            featured_url = media.get("source_url", "")
        except (urllib.error.HTTPError, json.JSONDecodeError):
            pass

    price_from = parsed["prices_usd"][-1] if parsed["prices_usd"] else ""

    pack = {
        "slug": slug,
        "url_wp": page_url,
        "drupal_alias": f"/tour/{slug}/",
        "title": api.get("title", {}).get("rendered", ""),
        "h1": parsed["h1"] or api.get("title", {}).get("rendered", ""),
        "seo_title": yoast.get("title", row.get("Título SEO", "") if row else ""),
        "meta_description": yoast.get(
            "description", row.get("Meta description", "") if row else ""
        ),
        "keyword": row.get("Keyword principal", "") if row else "",
        "price_from_usd": price_from,
        "featured_image": featured_url,
        "gallery_images": parsed["image_urls"],
        "itinerary_days": parsed["itinerary_days"],
        "tour_category_ids": api.get("tour_category", []),
        "tour_tag_ids": api.get("tour_tag", []),
        "note": (
            "Tabs Overview/Included/Pricing/What to Bring: copiar desde wp-admin "
            "→ Tour → Edit (Tourmaster no expone body en REST)."
        ),
    }
    return pack


def md_pack(p: dict) -> str:
    days = "\n".join(f"- {d}" for d in p["itinerary_days"]) or "- (copiar de wp-admin)"
    imgs = "\n".join(f"- {u}" for u in p["gallery_images"][:8]) or "- (descargar de WP)"
    return f"""# {p['title']}

| Campo Drupal | Valor (copiar tal cual) |
|---|---|
| **Product title** | {p['h1']} |
| **URL alias** | `{p['drupal_alias']}` |
| **Page title (Metatag)** | {p['seo_title']} |
| **Meta description** | {p['meta_description']} |
| **Price (USD)** | {p['price_from_usd'] or 'VER WP'} |
| **SKU** | `{p['slug']}` |

**WP:** {p['url_wp']}

## Itinerario (texto extraído — completar tabs en wp-admin)

{days}

## Imágenes detectadas

{imgs}

## Tabs que debes copiar manualmente desde wp-admin

1. Tour → Edit → cada sección Tourmaster → pestañas:
   - Overview
   - Itinerary (HTML completo)
   - Included / Not included
   - Pricing
   - What to Bring

> {p['note']}
"""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", help="Un solo tour")
    ap.add_argument("--out", type=Path, default=OUT)
    args = ap.parse_args()

    rows = list(csv.DictReader(open(TOURS_CSV, encoding="utf-8")))
    by_slug = {r["Slug"]: r for r in rows}
    slugs = [args.slug] if args.slug else [r["Slug"] for r in rows]

    args.out.mkdir(parents=True, exist_ok=True)
    manifest = []
    errors = []

    for slug in slugs:
        print(f"Exportando {slug}...", file=sys.stderr)
        try:
            pack = export_tour(slug, by_slug.get(slug))
            (args.out / f"{slug}.json").write_text(
                json.dumps(pack, indent=2, ensure_ascii=False), encoding="utf-8"
            )
            (args.out / f"{slug}.md").write_text(md_pack(pack), encoding="utf-8")
            manifest.append({"slug": slug, "ok": True, "title": pack["title"]})
        except Exception as e:
            errors.append({"slug": slug, "error": str(e)})
            print(f"  ERROR: {e}", file=sys.stderr)

    (args.out / "manifest.json").write_text(
        json.dumps({"date": date.today().isoformat(), "tours": manifest, "errors": errors}, indent=2),
        encoding="utf-8",
    )
    print(f"OK → {args.out} ({len(manifest)} tours, {len(errors)} errores)", file=sys.stderr)


if __name__ == "__main__":
    main()
