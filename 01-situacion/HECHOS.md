# Hechos verificados (solo cosas que viste / te dijeron / exportaste)

Formato: `- AAAA-MM-DD — hecho — fuente`

---

## 2026-08-25 (día 1)

- Setup: laptop propia + monitor TEROS TE-3215G HDMI (Display2 RTX 3060 1080p60); laptop Iris Xe 1080p165 — capturas Windows
- Elegí laptop vs PC oficina: internet más rápido, SSD vs HDD, misma RAM 32 gb — Jairo
- `marketing@` en Chrome + Cursor; Excel Accesos recibido; grupo WA Marketing Sin Jefe — día 1
- NAS `192.168.1.87` (`marketingpgt`) montado; usuario OMV `linux_admin` creado — día 1
- Reparto WA: tours bloque **3**, blogs bloque **4** — grupo 13:08
- Equipo SEO: Ricardo (webmaster/accesos), Lizet (Ads+SEO), Arely (½), Jairo — oficina
- Bloque datos refinados luego: 18 tours + 115 blogs EN — CSV 25–26 ago
- Clever: rol SEO/GEO S/ 3.500; revisión jefatura (plazo ajustado día 2 a ~25 sep) — oral



## 2026-08-26 (día 2)

- Clever: Drupal decidido; VPS Ubuntu interno (no agencia); Jairo entregará plan SEO; mes 1 a 3500 — oral
- WP perugrandtravel.com: Tourmaster, Yoast, ~30+ plugins — wp-admin
- Simplytest Commerce (Belgrade) = demo, no PGT — práctica
- Drive + GA4 inventariados (`DRIVE-INVENTARIO.md`, `GA4-INVENTARIO.md`) — browser Cursor
- GA4 cuenta Peru Grand Travel `47537800`: EN 368486554, PT 375022927, ES 470828894 — selector
- Ads 421-897-0045 sin vincular a GA4 EN — banner Analytics
- Lizet: entró ~17 ago; Lima; Ads mañanas / SEO tardes; vino por SEO — conversación
- Asistencia: equipo marca huella; Jairo aún no registrado — observación
- Quedarse hasta cierre con quien cierre — hábito Jairo



## 2026-08-27 (día 3)

- Jefe de marketing (mañanas) se llama **Einel** — Jairo
- OMV dashboard: Ryzen 5 5600GT, 15 GiB RAM, `/dev/sda1` 3,58 TiB (~24% usado), SMB/NFS/File Browser ON; updates + reinicio pendiente — captura 14:04
- Informes día 1–2–3 creados en `03-seo/informes/` — repo
- **GSC perugrandtravel.com · 28 días:** 643 clics · 116 mil impresiones · CTR 0,6% · posición media 25,6 — Search Console 27 ago
- GSC top página por clics: home (228); Costa Verde 12 clics / 8.740 impresiones — tabla Páginas



## 2026-08-28 (día 4)

- Hosting migración: **OVH VPS** IP `147.135.114.64` (no Banahosting para Drupal) — Einel
- Staging Drupal **11** + Commerce (`anymerce`) + nginx Ubuntu — revisión agente 28 ago
- Solo migrará **inglés** (`perugrandtravel.com`) en primera fase — Einel
- Staging: home visual OK; blog real `/blog/things-to-do-in-machu-picchu/` → **404** — browser
- URLs tours distintas a WP (ej. `/salkantay-trek-5d-4n` vs `/tour/the-classic-salkantay-trek-5d/`) — curl
- Staging: sin WhatsApp visible; botones **Add to cart** — browser
- Staging: home ~437KB HTML; cache `no-cache, private` — curl headers
- Figma tour detail (node 485-3513) abierto en browser — diseño alineado con cards Drupal



## 2026-08-28 (día 4)

- Brief CRM internamente (`08-investigacion/CRM-PGT-Y-VECTORIFY.md`); RD Station y Sheet DAI/Paloma **aún no abiertos** — repo + MAPA-HERRAMIENTAS
- Drupal staging tour Salkantay 5D = **`/product/9`** (title OK); canonical relativo; **Add to cart**; **0 JSON-LD** — curl 28 ago 12:32
- WP blog Things MP: title + meta + schema + WA **OK**; staging mismo path → **404** — curl 28 ago
- Entregables día 4: mapa 25 URLs, inventario 133 URLs, 2 auditorías, checklist pre-launch, plan Clever v1 — repo 28 ago tarde
- **POC Next.js** scaffold en `pgt-poc/`: tour Salkantay + blog Things MP, schema JSON-LD, WA, noindex — build OK 28 ago
- **POC desplegado:** https://pgt-poc.vercel.app · GitHub JairoProDev/pgt-poc · Vercel conectado — 28 ago tarde
- Contenido POC scrapeado de **WP live** (itinerario 5 días, US$ 731, imágenes wp-content, blog 11 secciones) — no Drupal
- GA4 stream POC **`proof of concept`** · Measurement ID **`G-V8FFS0SCXB`** · env Vercel — 28 ago tarde
- POC Lighthouse mobile tour: Perf **99**, SEO **89** (con noindex); comparativa WP 55 / Drupal 13 — capturas Jairo
- POC **indexable** (noindex quitado 28 ago noche) para test SEO Lighthouse — agente
- Blog Things MP optimización CTR iniciada 28 ago tarde: Rank Math title `12 Things to Do in Machu Picchu (2026 Guide)` + meta nueva en post 18674 (`/blog/wp-admin/`) — Jairo
- Things MP: Basic SEO All Good; H1 `12 Things…(2026)`; intro 2026; bloque tours Custom HTML; botón WP = **Save** (no Update) — captura Jairo 28 ago noche
- GSC Inspección URL Things MP: muestra **“La URL no está en Google / Google no reconoce esta URL”** (rastreo N/D) pese a baseline 6.115 imp — captura Jairo; acción: Solicitar indexación + Probar URL publicada
- GSC: **“Se ha solicitado la indexación”** Things MP → cola de rastreo prioritaria — captura 28 ago noche
- `site:` en Bing aún muestra title/meta **viejos** (cache motor) — normal; no repetir solicitud
- Google `site:` Things MP = **0 resultados** (incógnito) — alineado con Inspección “no reconoce”; live OK: 200, `index,follow`, `<title>` nuevo 12 Things… — curl 28 ago 23:51 UTC
- Sáb 29: `site:www.perugrandtravel.com "things to do in machu picchu"` muestra `/blog/things-to-do-in-machu-picchu/` con title **12 Things to Do in Machu Picchu (2026)** + duplicado `/Home/Cusco` title viejo — captura Jairo
- Lunes 1 sep: arranca migración Drupal EN (tours primero, blogs después) — Einel capacita — oral Jairo
- Staging 29 ago: home OK en `147.135.114.64`; tours `/product/N`; Things MP blog **404**; sin WA en tour — curl
- 1 sep: Einel accesos Drupal + assets; capacitación Drupal → Ricardo; experimento 4 estrategias SEO — Jairo
- Inventario sitemap WP EN 1 sep: **69 tours, 452 blogs, 62 pages, 6 tour-categories** — script export-wp-sitemap-inventory.sh

## 2026-09-01 (día 6)

- Admin Drupal products real: `/admin/anymerce/products` (no `/admin/commerce/products` → 404) — browser 1 sep
- Staging: 26 products ya migrados por equipo; bloque Jairo 18 tours sin slug WP 1:1 — revisión 1 sep
- JSON:API staging `/jsonapi` → **404** — curl 1 sep
- Export WP 18 tours bloque Jairo → JSON+MD **18/18 OK** — `wp-export-tours-jairo/manifest.json`
- WP REST tours: title/Yoast OK; body/tabs Tourmaster **no en REST** — script export 1 sep
- CSV maestro migración 133 filas (18 tours + 115 blogs) — `jairo-migracion-maestro.csv`
- Estimación migración bloque: ~49 h (+15 % buffer ~56 h) — `estimacion-tiempos-migracion-jairo.csv`
- Export GSC automatizado: 15.101 filas queries×páginas — `gsc-export-2026-09-01/`
- Export GA4 28d: 174 landing pages, 8 tipos evento — `ga4-export-2026-09-01/`
- 101 capturas admin Drupal indexadas — `drupal-capturas-2026-09-01/`
- Informe maestro semana 1 consolidado — `mi-carrera/INFORME-MAESTRO-SEMANA1-JAIRO.md`
- GCP proyecto `theta-cell-499613-r8` + service account `pgt-cursor-agent@pgt-integrations` — integraciones 1 sep
- GA4 API + GSC EN conectados; verify 5/7 — terminal Jairo 1 sep tarde
- GSC 4 dominios en `.env.mcp`; EN export OK; PT/ES/IT pendiente invitar SA — 1 sep
- GTM cuenta `6371934908` contenedor `261504322` — API OK 1 sep
- Vercel alias **perugrandtravel.vercel.app** → pgt-web prod — CLI 1 sep
- Docs: `pgt-web/docs/REPORTE-AVANCE-JAIRO.md`, `INVENTARIO-PLATAFORMAS.md`, guía Google actualizada — 1 sep
- Sin área IT: Jairo asume dirección técnica; Ricardo webmaster ejecución — oral Jairo 1 sep

