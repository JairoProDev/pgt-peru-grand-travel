#!/usr/bin/env bash
# Inventario URLs desde sitemaps WP perugrandtravel.com
# Uso: ./export-wp-sitemap-inventory.sh
# Salida: 03-seo/datos/inventario-sitemap-YYYY-MM-DD/

set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/datos/inventario-sitemap-$(date +%Y-%m-%d)"
mkdir -p "$OUT"

fetch_locs() {
  local url="$1"
  curl -sL "$url" | rg -o '<loc>[^<]+</loc>' | sed 's|<loc>||;s|</loc>||'
}

echo "=== Export sitemap inventory ==="
echo "Output: $OUT"

# Tours
fetch_locs "https://www.perugrandtravel.com/tour-sitemap.xml" > "$OUT/tours.txt"
echo "Tours: $(wc -l < "$OUT/tours.txt")"

# Blogs
fetch_locs "https://www.perugrandtravel.com/blog/post-sitemap.xml" > "$OUT/blogs.txt"
echo "Blogs: $(wc -l < "$OUT/blogs.txt")"

# Pages
fetch_locs "https://www.perugrandtravel.com/page-sitemap.xml" > "$OUT/pages.txt"
echo "Pages: $(wc -l < "$OUT/pages.txt")"

# Tour categories
fetch_locs "https://www.perugrandtravel.com/tour_category-sitemap.xml" > "$OUT/tour-categories.txt"
echo "Tour categories: $(wc -l < "$OUT/tour-categories.txt")"

# CSV maestro mínimo
{
  echo "tipo,url"
  while read -r u; do echo "tour,$u"; done < "$OUT/tours.txt"
  while read -r u; do echo "blog,$u"; done < "$OUT/blogs.txt"
  while read -r u; do echo "page,$u"; done < "$OUT/pages.txt"
  while read -r u; do echo "tour_category,$u"; done < "$OUT/tour-categories.txt"
} > "$OUT/inventario-urls.csv"

echo "CSV: $OUT/inventario-urls.csv"
echo "Done."
