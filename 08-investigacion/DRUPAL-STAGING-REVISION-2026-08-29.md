# Drupal staging — revisión 29 ago 2026

**URL:** http://147.135.114.64/  
**Contexto:** Einel sigue desarrollando; lunes arranca migración formal (tours primero, blogs después).

---

## Resumen ejecutivo

| Área | Estado | Riesgo SEO / negocio |
|---|---|---|
| **Home** | ✅ Visual moderna, tours listados | Medio — URLs `/product/N`, HTML ~409 KB |
| **Tours** | 🟡 Contenido existe | **Alto** — slug no coincide WP; canonical relativo |
| **Blogs WP reales** | 🔴 Things MP → 404 | **Crítico** — 6k imp GSC en riesgo |
| **Blogs demo** | ✅ Nuevos slugs en `/blog/...` | Medio — no son las URLs con tráfico |
| **Conversión** | 🔴 Add to cart, sin WA visible | **Crítico** — modelo Clever es WA |
| **Schema** | 🔴 0 JSON-LD en tour piloto | Alto — rich results / GEO |
| **Performance** | 🔴 cache private, HTML pesado | Alto — CWV (GSC ya alerta 100% LCP lento) |
| **Indexación staging** | 🔴 robots permite indexar IP | Medio — canibalización si Google rastrea IP |

---

## Hallazgos técnicos (curl 29 ago)

### Home

- HTTP 200, `Content-Length: ~409 KB`
- `Cache-Control: must-revalidate, no-cache, private`
- Canonical: `http://147.135.114.64/` (IP, no dominio)
- Tours enlazan a `/product/1`, `/product/7`, `/product/8`, `/product/9`, `/product/10`, `/product/11`

### Tour Salkantay (`/product/9`)

- Title: `Salkantay Trek 5D/4N | Peru Grand Travel` ✅
- Canonical: `href="/product/9"` 🔴 (relativo, no absoluto, no slug WP)
- WP equivalente: `/tour/the-classic-salkantay-trek-5d/`
- Precio staging home card: **$590** vs WP **$731** — verificar fuente de verdad

### Blog Things MP

- `GET /blog/things-to-do-in-machu-picchu/` → **404**
- Blogs visibles en home (demo):
  - `/blog/limas-best-restaurants-2025-street-ceviche-fine-dining`
  - `/blog/lake-titicaca-complete-visitors-guide-2025`
  - `/blog/rainbow-mountain-vinicunca-everything-you-need-know-you-go`

### Comparativa WP prod (Things MP optimizado 28 ago)

- Title: `12 Things to Do in Machu Picchu (2026 Guide)` ✅
- `robots: index, follow` ✅
- Indexado en Google (site: confirma 29 ago) ✅

**Implicación:** El trabajo SEO de Jairo en WP es la **especificación** que Drupal debe replicar al migrar ese blog.

---

## Acciones dueño SEO (Jairo) — antes de cutover

| # | Acción | Prioridad |
|---|---|---|
| 1 | Exigir slug WP = Drupal para top 20 URLs GSC | P0 |
| 2 | Mapa 301 `/product/N` → `/tour/...` si no hay paridad | P0 |
| 3 | Blog Things MP no puede lanzarse en 404 | P0 |
| 4 | WhatsApp sticky en tour (o decisión escrita cart) | P0 |
| 5 | JSON-LD Product/TouristTrip en tour piloto | P1 |
| 6 | Canonical absoluto https://www.perugrandtravel.com/... | P1 |
| 7 | noindex staging hasta DNS final | P1 |

---

## Para reunión lunes con Einel

Traer impreso o en pantalla:

1. `03-seo/datos/mapa-urls-wp-drupal.csv`
2. `08-investigacion/CHECKLIST-PRE-LAUNCH-DRUPAL.md`
3. Captura Things MP optimizado (title/meta Rank Math)
4. Esta revisión

**Mensaje:** No bloqueo la migración — evito que mate 116k impresiones/mes.

---

*Anterior:* `DRUPAL-STAGING-REVISION-2026-08-28.md`
