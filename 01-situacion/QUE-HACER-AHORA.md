# Qué hacer ahora — 3 sep 2026

**Hilación de trabajo:** `mi-carrera/MAPA-TRABAJO-JAIRO.md` · checks: `mi-carrera/TAREAS-VIVAS.md`

**DNS beta (ahora):** WHM CNAME — campo **Nombre** = `next` (o FQDN con punto); campo **CNAME** = `cname.vercel-dns.com.` · Mail EN = Google Workspace, no cPanel. Detalle: `02-empresa/HOSTING-BANAHOSTING-INVENTARIO.md`.

**Drupal:** 18/18 tours HTTP 200. HTML **v7** (badges OK). Imágenes: 6/tour listas en `assets/ready` + `media-ready.json` (Name/Alt/Title). Subida Media Library pendiente (`upload-tour-media-to-drupal.mjs`). Presentación: `mi-carrera/PRESENTACION-4SEP-TOURS-SEO-GEO.md` + one-pager Clever + `CHECKLIST-SEO-CAPAS.md`. Logs: `tail -f /tmp/batch-v7b-update.log`.

## Estilo (decisión GEO/SEO)

- Sin emojis decorativos; listas con • ✓ ✕ por CSS.
- Badges = `<ul class="pgt-badges"><li class="pgt-badge">…` (CKEditor 5 no debe fusionarlos).
- Humantay: Duration corregida (`Full Day (~13h)`; antes leak CSS `19px ;" >`).

## P0 — migración tours

1. **Re-import v7** — batch en `/tmp/batch-v7-update.log` (flood 300s/tour).
2. **Aliases `/tour/{slug}`** — pathauto widget sigue peleando; URLs canónicas ya responden 200.
3. **Einel** — CSS global `tour-maestro-styles.css`.
4. Galerías media + Corpus Christi precio (Drive).
5. Producto basura #68 `Amazon rainforest express-3d` — pedir borrar.

### URLs (staging) — lote completo

| # | Tour | URL preferida | Nota |
|---|------|---------------|------|
| 57 | Humantay | http://147.135.114.64/tour/humantay-lake-full-day | 200 — Duration fix v7 |
| 58 | South Valley | http://147.135.114.64/tour/tour-south-valley-cusco | 200 |
| 59 | Q'eswachaka | http://147.135.114.64/tour/qeswachaka-bridge-full-day | 200 |
| 60 | Planetarium | http://147.135.114.64/tour/cusco-planetarium | 200 |
| 61 | Wonder 13D | http://147.135.114.64/tour/wonder-of-peru-coast-andes-and-rainforest-13d | 200 |
| 62 | Salkantay 4D | http://147.135.114.64/tour/salkantay-trek-4-days | 200 |
| 9 | Salkantay 5D | http://147.135.114.64/tour/the-classic-salkantay-trek-5d | 200 |
| 63 | Choquequirao | http://147.135.114.64/tour/choquequirao-trek-5d | 200 |
| 64 | Maras | http://147.135.114.64/tour/maras-moray-and-the-salineras-full-day | 200 |
| 65 | Sacred Valley + Short IT | http://147.135.114.64/tour/sacred-valley-short-inca-trail-3d | 200 |
| 66 | Incredible MP 2D | http://147.135.114.64/tour/incredible-machu-picchu-2d | 200 |
| 67 | MP Express 3D | http://147.135.114.64/tour/machu-picchu-express-3d | 200 |
| 69 | MP Moderate 4D | http://147.135.114.64/tour/machu-picchu-moderate-4d | 200 |
| 76 | MP Challenge 8D | http://147.135.114.64/tour/machu-picchu-challenge-8d | 200 — badges v7 |
| 71 | Spectacular Cusco 7D | http://147.135.114.64/tour/spectacular-cusco-7-days | 200 |
| 72 | Grand Deluxe Casa Andina | http://147.135.114.64/tour/grand-deluxe-cusco-machu-picchu-by-casa-andina-hotels-5-days | 200 |
| 73 | Grand Deluxe Inkaterra | http://147.135.114.64/tour/grand-deluxe-cusco-machu-picchu-by-inkaterra-hotels-5-days | 200 |
| 74 | Corpus Christi | http://147.135.114.64/tour/cusco-corpus-christi | 200 |

```bash
export DRUPAL_USER='Jairo saul' DRUPAL_PASS='...'
# Seguimiento live
tail -f /tmp/batch-v7-update.log
# Alias puntual
node 03-seo/scripts/import-tour-to-drupal.mjs --fix-alias --slug=choquequirao-trek-5d
# Regenerar HTML local
python3 03-seo/scripts/build-tour-clean-html.py --force
```

## P1 — sitio web / cutover

1. **Cruces tours** Drive ↔ slugs web
2. **GTM tag** `whatsapp_click` → GA4 — 10 min UI marketing@
3. **Validar precios** con Ricardo — sheet OTAS
4. **DNS beta** con Ricardo → QA 7 días

## P1 — cuando haya tiempo

| Tarea | Quién |
|-------|-------|
| GSC ES: invitar SA a `viajesmachupicchutours.com` | Jairo |
| Filtro tráfico interno GA4 | Jairo |
| `npm run precios:apply` tras mapeo + validación Ops | Jairo |
| Cutover prod DNS | Jairo + Ricardo |

## Referencia Google (mantenimiento)

`pgt-web/docs/GUIA-CONEXION-GOOGLE.md` — sección **INTEGRACIONES CERRADAS**

```bash
cd ~/proyectos/pgt-web && npm run verify:google && npm run sync:ga4 && npm run sync:gsc
```

## URLs

| Uso | URL |
|-----|-----|
| Demo pgt-web | https://perugrandtravel.vercel.app |
| Drupal staging | http://147.135.114.64 |
