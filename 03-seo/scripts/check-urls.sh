#!/usr/bin/env bash
# Valida URLs WP vs staging Drupal — uso: ./check-urls.sh [mapa.csv]
# Requiere: curl

MAP="${1:-$(dirname "$0")/../datos/mapa-urls-wp-drupal.csv}"
STAGING="${STAGING:-http://147.135.114.64}"

echo "=== PGT URL check — $(date -Iseconds) ==="
echo "Staging: $STAGING"
echo ""

while IFS=',' read -r tipo url_wp url_drupal _rest; do
  [[ "$tipo" == "tipo" || -z "$url_wp" ]] && continue
  wp_code=$(curl -s -o /dev/null -w "%{http_code}" -L "$url_wp" 2>/dev/null || echo "ERR")
  drupal_path="${url_drupal:-}"
  if [[ -z "$drupal_path" || "$drupal_path" == "url_drupal_prevista" ]]; then
    drupal_path=$(echo "$url_wp" | sed 's|https://www.perugrandtravel.com||')
  fi
  st_code=$(curl -s -o /dev/null -w "%{http_code}" -L "${STAGING}${drupal_path}" 2>/dev/null || echo "ERR")
  status="OK"
  [[ "$st_code" != "200" ]] && status="MISSING"
  printf "%-6s WP:%s ST:%s %s\n" "$status" "$wp_code" "$st_code" "$url_wp"
done < "$MAP"

echo ""
echo "Done. MISSING = staging no tiene 200 — revisar antes de cutover."
