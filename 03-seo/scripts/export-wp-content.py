#!/usr/bin/env python3
"""
Export WP content structure → JSON/CSV for Drupal migration prep.
Phase 1: public data only (no auth) — title from HTML, sitemap URLs.

Usage:
  python3 export-wp-content.py --type tour --limit 5
  python3 export-wp-content.py --type blog --limit 10
  python3 export-wp-content.py --inventory  # all URLs from latest sitemap export

Requires: curl, rg (or extend to use requests)
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

REPO = Path(__file__).resolve().parents[1]
DATOS = REPO / "datos"


def curl(url: str) -> str:
    r = subprocess.run(
        ["curl", "-sL", "-A", "PGT-Migration-Bot/1.0", url],
        capture_output=True,
        text=True,
        timeout=60,
    )
    return r.stdout if r.returncode == 0 else ""


def extract_meta(html: str) -> dict:
    def one(pattern: str, flags=re.I | re.S) -> str:
        m = re.search(pattern, html)
        return m.group(1).strip() if m else ""

    return {
        "title": one(r"<title[^>]*>([^<]+)</title>"),
        "meta_description": one(r'name="description"\s+content="([^"]*)"'),
        "canonical": one(r'rel="canonical"\s+href="([^"]*)"'),
        "og_title": one(r'property="og:title"\s+content="([^"]*)"'),
        "h1": one(r"<h1[^>]*>([^<]+)</h1>"),
        "robots": one(r'name="robots"\s+content="([^"]*)"'),
    }


def slug_from_url(url: str) -> str:
    path = urlparse(url).path.strip("/")
    return path.split("/")[-1] if path else ""


def load_urls(kind: str) -> list[str]:
    inv_dir = sorted(DATOS.glob("inventario-sitemap-*"))
    if inv_dir:
        f = inv_dir[-1] / f"{kind}s.txt"
        if f.exists():
            return [ln.strip() for ln in f.read_text().splitlines() if ln.strip()]
    # fallback sitemap
    sm = {
        "tour": "https://www.perugrandtravel.com/tour-sitemap.xml",
        "blog": "https://www.perugrandtravel.com/blog/post-sitemap.xml",
    }[kind]
    xml = curl(sm)
    return re.findall(r"<loc>([^<]+)</loc>", xml)


def export_urls(urls: list[str], out: Path) -> None:
    rows = []
    for i, url in enumerate(urls):
        print(f"[{i+1}/{len(urls)}] {url}", file=sys.stderr)
        html = curl(url)
        meta = extract_meta(html)
        rows.append({
            "url": url,
            "slug": slug_from_url(url),
            "tipo": "tour" if "/tour/" in url else "blog",
            **meta,
            "http_ok": bool(html and "<title" in html.lower()),
        })
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(rows, indent=2, ensure_ascii=False))
    csv_path = out.with_suffix(".csv")
    if rows:
        with csv_path.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=rows[0].keys())
            w.writeheader()
            w.writerows(rows)
    print(f"Wrote {out} and {csv_path}", file=sys.stderr)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--type", choices=["tour", "blog"], default="tour")
    p.add_argument("--limit", type=int, default=0)
    p.add_argument("--inventory", action="store_true")
    args = p.parse_args()

    urls = load_urls(args.type)
    if args.limit:
        urls = urls[: args.limit]

    stamp = __import__("datetime").date.today().isoformat()
    out = DATOS / f"export-wp-{args.type}-{stamp}.json"
    export_urls(urls, out)


if __name__ == "__main__":
    main()
