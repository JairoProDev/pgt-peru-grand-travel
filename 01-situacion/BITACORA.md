# Bitácora

No escribas contraseñas.

## 25 ago 2026 — día 1

**Equipo SEO**

- Ricardo — accesos, reparte carga, líder no oficial
- Lizet — SEO + Google Ads + Meta Ads
- Arely — medio tiempo, mañanas
- Jairo — entrante SEO/GEO
- Carga: ~73 tours + ~454 blogs, 4 bloques
- **Reparto (grupo WA 13:08–13:09):**
  - Tours: Arely 1 · Lizet 2 · **Jairo 3** · Ricardo 4
  - Blogs: Ricardo 1 · Lizet 2 · Arely 3 · **Jairo 4**
- Mi bloque exacto (URLs): hojas `tours jairo` y `blogs jairo` en Sheet `PGT_URLs_keywords_canibalizacion_2` — ver `03-seo/BLOQUE-JAIRO.md`
- Grupo WA: **"Peru Grand Travel Marketing - Sin Jefe"** (9 miembros)
- Links grupo: [Sheet keywords](https://docs.google.com/spreadsheets/d/1VAaeEpG_hW8DOMbdqbidQhc2aNjhV8qDJQZ0nWcGMQU/edit) · [Drive marketing](https://drive.google.com/drive/folders/1-1wEMq2qox3D0jrs4uY1XQz-3sqbTW9z) · [Figma](https://www.figma.com/design/jhLCgtdkX4AtItlUD5ooBf/Sin-t%C3%ADtulo?node-id=485-3479) · PDF "Nuevo Diseño de sitio web PGT" (137 MB, Ricardo 12:50)

**Jefe marketing interino**

- Nombre: **Einel** (solo mañanas) — confirmado 27 ago
- Email: 	EinelEH@gmail.com
- tiene permisos completos en GSC, supongo que él lo creo.
- marketing@perugrandtravel.com tiene permisos de propietario verificado en GSC

**Pacto Clever**

- 3500 ahora · **revisión ~1 mes (~25 sep)** → jefe mkt 5000 (ya no 2 semanas) · oral · WhatsApp (`WHATSAPP-PACTO-REVISADO.md` / `REVISION-1-MES.md`)
- Norte: qualified leads + marca
- No firmé nada

**Accesos**

- marketing@, NAS, Drive Ricardo, Accesos.xlsx
- linux_admin: Ricardo aún no sabe → avisarle

**Figma / Drupal**

- Figma modular (Paquetes, Pricing, Included…)
- Migración Drupal **decidida** (26 ago) — Jairo = dueño SEO cutover
- Playbook: `08-investigacion/MIGRACION-WP-DRUPAL-PLAYBOOK.md`

**Qué dije de mí**

- SEO/GEO, WP, Drupal (recalibrar), fullstack, GA, GSC, Semrush, Hotjar…

## 26 ago 2026 — día 2

**Hechos nuevos**

- Clever: Drupal va (VPS Ubuntu interno); mes 1 migración + plan SEO; jefatura ~25 sep
- Análisis bloque 18 tours / 115 blogs + prioridades CSV
- Drive + GA4 mapeados; HECHOS/DUDAS/INSIGHTS; borrador plan Clever
- Simplytest = no PGT
- Lizet: Ads AM / SEO PM

**Pendientes que pasaron a día 3**

- [ ] Respuestas A1–A10 playbook
- [ ] Staging Drupal URL: ____
- [ ] WhatsApp pacto 25 sep enviado: ____
- [ ] Avisar NAS `linux_admin` a Ricardo
- [ ] GSC línea base export
- [x] Nombre del interino → **Einel**

## 27 ago 2026 — día 3

**Plan:** `03-seo/informes/2026-08-27-interno.md`

- [ ] GSC export bloque
- [ ] Saludo Einel (si está)
- [ ] Ricardo: NAS + staging + huella
- [ ] Lizet 15 min Ads
- [ ] Plan Clever ≥80%
- [ ] Cierre informe noche

## 28 ago 2026 — día 4

**CRM (menciones de Clever, no encargo)**

- Brief: `08-investigacion/CRM-PGT-Y-VECTORIFY.md`
- Inventario: no hay CRM vivo verificado. Hay WA (checkout) + Sheet DAI/Paloma + RD Station (Josimar) + Mailchimp + tawk + WeTravel + OTAs
- Postura: mapear, no construirlo. No mezclar con el plan SEO de esta semana ni con Vectorify
- RD Station sigue **sin ojear** (`MAPA-HERRAMIENTAS.md`)

## 28 ago — tarde (día 4)

- Agente: mapa 25 URLs migración, inventario 133 URLs bloque, auditorías P0 (Things MP + Salkantay), checklist pre-launch Drupal, plan Clever v1
- Hallazgo: Drupal `/product/9` = Salkantay; blog Things MP 404 en staging; cart sin WA
- Pendiente humano: WhatsApp Einel/Ricardo, export GSC, enviar plan Clever

## 29 ago 2026 — día 5 (sáb)

**Contexto:** Lunes arranca migración Drupal EN; Einel capacita tours → blogs.

- Plan personal 30 días → S/ 5.000: `mi-carrera/PLAN-30-DIAS-5000.md`
- Sprint sáb 9–12: `01-situacion/SABADO-29-SPRINT.md`
- Staging delta 29 ago: home OK; tours `/product/N`; blog Things MP **404**; blogs demo nuevos slugs — `DRUPAL-STAGING-REVISION-2026-08-29.md`
- Reframe: trabajo Things MP WP = **plantilla SEO migración**, no trabajo perdido
- Script validador URLs: `03-seo/scripts/check-urls.sh`
- CRM: no construir mes 1; medición WA primero (`CRM-PGT-Y-VECTORIFY.md`)

## 1 sep 2026 — día 6 (lun) · migración arranca

- Einel da accesos Drupal individuales + carpeta assets ordenada — oral Jairo
- Capacitación Drupal → **Ricardo** (admin futuro), no solo Jairo
- Clever/experimento: **4 personas** aplican su estrategia; comparar resultados
- Estrategia Jairo: Pista A Drupal QA + Pista B POC código — `mi-carrera/EXPERIMENTO-4-ESTRATEGIA-JAIRO.md`
- Automatización: QA/scripts, no migración manual completa — `MIGRACION-AUTOMATIZACION.md`

**Accesos (diseño, sin implementar)**

- Excel/Sheet de contraseñas = legacy; no es buena práctica como fuente de secretos
- Diseño: proceso (menos cuentas compartidas + offboarding) + Vaultwarden $0 → `02-empresa/GESTION-ACCESOS-DISENO.md`
- Owner rotación hoy: Ricardo; ~20 personas; pitch pendiente a Ricardo/Clever
- No construir app interna de passwords; no pegar secretos en chat/repo

**Pack migración generado (agente + Jairo)**

- CSV maestro 133 URLs: `drupal-sprint-jairo-2026-09-01/jairo-migracion-maestro.csv`
- Export WP 18/18 tours JSON+MD: `wp-export-tours-jairo/manifest.json`
- Clipboard SEO tours: `drupal-tour-seo-clipboard/TOURS-SEO-CLIPBOARD.md`
- Mapa formulario Product + 101 capturas Drupal
- Estimación tiempos: ~49 h bloque (+15 % buffer → ~56 h)
- Exports GSC (15k filas) + GA4 (174 landings): `gsc-export-2026-09-01/`, `ga4-export-2026-09-01/`
- Informe maestro semana 1: `mi-carrera/INFORME-MAESTRO-SEMANA1-JAIRO.md`

**Pendiente humano día 6**

- [ ] Migrar tour piloto Salkantay 5D en Drupal
- [ ] 5 preguntas Einel (Pathauto, JSON:API, WA, blogs cuándo)
- [ ] Marcar `estado_drupal` en CSV maestro

## 2 sep 2026 — piloto Humantay (tour maestro)

- Piloto oro: **Humantay** `#57` → http://147.135.114.64/tour/humantay-lake-full-day (no Salkantay primero)
- 5 tabs: Overview · Itinerary · Included · Pricing · What to Bring
- Precio US$ 90 · SEO title/meta · trip details · galería **5** webp
- Plantilla: `03-seo/guias/TOUR-MAESTRO-ESTRUCTURA.md` + CSS `wp-export-tours-jairo/_shared/tour-maestro-styles.css`
- Decisión: **hacer bien de una** (no migrar feo → optimizar luego)
- Playwright MCP: opcional; script local `import-tour-to-drupal.mjs` es el camino
- Pendiente Einel: CSS theme + fix sidebar overlap (Amazon) — `guias/MENSAJE-EINEL-CSS-SIDEBAR.md`
- Siguiente: QA Humantay vs compañeros → clonar plantilla a los otros 17

## 2 sep 2026 (tarde) — capa maestra migración 18 tours

- Script `build-tour-migration-master.py` v4: merge WP + CSV SEO + tabs + catálogo + modelos Drive
- Por tour: `drupal-pack.json` (meta GEO/robots, commerce, taxonomías, media alt/title, modelo) + `MIGRATION-README.md` + `assets/`
- Inventario: `MIGRATION-MASTER-INVENTORY.csv` — avg score **84.2**, 10/18 con modelo Drive
- Esquema documentado: `03-seo/guias/TOUR-MIGRATION-MASTER-SCHEMA.md`
- Gaps globales: 17 sin HTML v2 clean; 4 tours tabs vacíos WP; 3 deluxe sin modelo; Corpus Christi precio sin verificar
- Treks Salkantay/Choquequirao: modelo PPTX only (sin xlsx precios/itinerario en CSV Drive)

## 2 sep 2026 (noche) — supplement atendimento@ Drive

- `modelo_drive_content.py`: tabs vacíos WP → datos oficiales Drive (PPTX Single tours Cusco, Wonder 13D)
- Q'eswachaka, Planetarium, Wonder 13D, South Valley, Humantay, Maras: `modelo-supplement.json`
- Inventario avg **90.5** — 5 tours score 100
- Corpus Christi (74): sin deck Drive; supplement ops-standard; precio pendiente cotizador

## 3 sep 2026 — lote Drupal 7 tours

- Login CAPTCHA + Category required + flood 300s manejados en `import-tour-to-drupal.mjs`
- Creados: South Valley #58, Q'eswachaka #59, Planetarium #60, Wonder 13D #61, Salkantay 4D #62
- Actualizados: Humantay #57, Salkantay 5D #9
- Alias forzados `/tour/{slug}` (pathauto off)
- Pendiente: 11 tours + CSS Einel + media upload

## 3 sep 2026 (mañana) — lote 11 + HTML v5 híbrido

- Batch: Choquequirao #63, Maras #64, Sacred Valley #65, Incredible MP #66, Express #67, Moderate #69, Spectacular #71, Casa Andina #72, Inkaterra #73, Corpus #74, Challenge **#76** (no tocar #1 de compañeros)
- Fallos alias: widget pathauto se re-marca solo; Path UI = Access denied; varios live en URL pathauto (sin `/tour/`)
- Basura parcial #68 `Amazon rainforest express-3d` — pedir borrado
- Estilo: v4 emoji-dense se lee IA; v5 híbrido (checks/puntitos/✕ + badges + GEO) regenerado local 18/18; piloto Q’eswachaka
- Bug fix importer: `--create` ya no fuzzy-match; checkbox pathauto boolean; `--fix-alias`

## 3 sep 2026 (tarde+) — imágenes + presentación 4 sep

- **18/18** HTTP 200 (0 Page not found); badges Challenge corregidos (v7 `<ul>/<li>`)
- Media Drupal: `field_anymerce_media` (hero) + `field_prod_slid_med` (slider) + `field_prod_broch_med`; por archivo: **Name / Alt / Title**
- `optimize-tour-images.mjs`: 6 JPEG/tour ≤1600px q82 + `media-ready.json`; `upload-tour-media-to-drupal.mjs` listo
- Presentación mañana: `mi-carrera/PRESENTACION-4SEP-TOURS-SEO-GEO.md`, one-pager Clever, `CHECKLIST-SEO-CAPAS.md` (mapa capas + techo Drupal/WP + CMS propio sin nombrar vendor)

## 3 sep 2026 (tarde) — `next.` vivo

- CNAME WHM OK · Vercel domain OK · env `SITE_URL` + `ENV=next` · redeploy
- URL: https://next.perugrandtravel.com (200, noindex, canonical next)
- Snapshot zona + guía: `pgt-web/docs/GUIA-VIVA-BETA-NEXT.md`
- Siguiente humano: QA manual + GTM whatsapp_click → GA4

## 3 sep 2026 (tarde) — mapa de trabajo + correo EN

- Registro vivo numerado: `mi-carrera/MAPA-TRABAJO-JAIRO.md` (JT-001…JT-078, incluye pre-empleo / jairosaul.com)
- Checklist siguiente paso: `mi-carrera/TAREAS-VIVAS.md`
- DNS público: MX EN → **Google** (`aspmx.l.google.com`); SPF RD Station + SendGrid (sin `_spf.google.com`); `next.` aún NXDOMAIN
- Modal CNAME WHM: solo **Nombre** + **CNAME** (no TTL/Target)

## 3 sep 2026 (tarde) — Banahosting / WHM (cuenta Clever)

- Login `clever@` + 2FA OK · Reseller-1 `perutrilhainca.com` · **$239/año** hasta abr 2027
- **17 cPanels** en WHM (no 1 dominio). Inventario: `02-empresa/HOSTING-BANAHOSTING-INVENTARIO.md`
- “Mis Dominios” vacío = comprados en GoDaddy/Registros.com, DNS en Banahosting
- **Load ~47–48** → clic CP de `perugrandtravel.com` = **500** `xfercpanel` Error ID `381fb3f66720c`
- Workaround: **WHM → DNS Zone Manager** (17 zonas, incluye perugrandtravel.com) — no hace falta cPanel
- Tres `.pe` no-turismo: mercadomovil, perubienesraices, tejidosmarangani — preguntar Clever
- Drupal staging sigue en OVH, no en este reseller

## 3 sep 2026 (tarde) — batch v6 + fix badges v7

- Batch v6: **18/18 saved** + HTTP **200** en las 18 URLs `/tour/{slug}` (0 Page not found)
- Bug badges: CKEditor 5 fusionaba `<span class="pgt-badge">` adyacentes → un solo pill (Challenge overview)
- Fix v7: badges = `<ul class="pgt-badges"><li class="pgt-badge">…`; sanitize Duration rechaza leaks CSS (`19px ;" >` en Humantay)
- Re-import v7 en curso: `tail -f /tmp/batch-v7-update.log`

## 3 sep 2026 (media mañana) — HTML v6 sin emojis

- Decisión: cero emojis decorativos (riesgo “parece IA” para LLMs/GEO + coherencia con compañeros)
- Markers solo CSS: • highlights, ✓ included/bring, ✕ not included; badges texto; GEO callout texto
- Local 18/18 regenerado; **Q’eswachaka #59** ya re-importado v6 en staging
- Importer: expandir tabs colapsadas antes de fill (Add more con count=0 rompía Save)

## 2 sep 2026 (noche) — HTML v4 + importer v2

- `build-tour-clean-html.py`: 18/18 tours con diseño premium (badges 🕐🥾, emojis, GEO callout 📍, acordeones, price hero)
- CSS v2: `_shared/tour-maestro-styles.css` — pedir a Einel en theme global
- Inventario avg **89.1** (Humantay + South Valley 100/100)
- `import-tour-to-drupal.mjs` v2: lee `drupal-pack.json` + meta GEO/robots + 5 tabs clean
- Fix duración corrupta catálogo (CSS leak → parse desde slug/título)