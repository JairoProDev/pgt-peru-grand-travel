# Mapa de trabajo Jairo — registro vivo

**Para qué existe:** un solo hilo numerado de lo que hiciste (antes del empleo y dentro de PGT).  
**Cómo usarlo:** cada actividad nueva = **una fila al final** con el siguiente `JT-nnn`. No reescribas historia; corrige solo si un dato estaba mal.  
**Checklist de “qué falta / qué sigue”:** [`TAREAS-VIVAS.md`](TAREAS-VIVAS.md)  
**CSV / Sheet (3 tracks):** [`tracker/TAREAS-MAESTRO.csv`](tracker/TAREAS-MAESTRO.csv)  
**Narrativa diaria:** [`../01-situacion/BITACORA.md`](../01-situacion/BITACORA.md)  
**Hechos verificados:** [`../01-situacion/HECHOS.md`](../01-situacion/HECHOS.md)

Último ID usado: **JT-078** (3 sep 2026). Siguiente: **JT-079**.

---

## Cómo añadir una fila (copia)

| ID | Fecha | Fase | Título | Qué hiciste | Datos / resultado | Evidencia | Estado |
|----|-------|------|--------|-------------|-------------------|-----------|--------|
| JT-079 | 2026-09-?? | … | … | 1–4 líneas | IDs, URLs, números | path o URL | hecho / parcial / bloqueado |

Fases: `pre-pgt` · `onboarding` · `seo-ops` · `drupal` · `pgt-web` · `hosting-dns` · `carrera` · `equipo`.

---

## Índices que ya existían (no los tires; este archivo los une)

| Archivo | Rol |
|---------|-----|
| `mi-carrera/tracker/TAREAS-MAESTRO.csv` | Tareas machine-readable + sync Sheet |
| `mi-carrera/ENTREGABLES-CREDITO-JAIRO.md` | Qué puedes firmar ante Clever |
| `mi-carrera/CHECKLIST-MAESTRO-JAIRO.md` | Checklist día 2 (desactualizado; no es el vivo) |
| `01-situacion/QUE-HACER-AHORA.md` | Prioridad del día |
| `archivo-original/empleo-seo/` | Auditoría y entregables pre-empleo |
| `conocimiento/articulos-jairosaul/` | Artículos publicados / MDX |
| Landing pública | https://jairosaul.com/peru-grand-travel |

---

## Tabla maestra

| ID | Fecha | Fase | Título | Qué hiciste / explicación | Datos importantes | Evidencia | Estado |
|----|-------|------|--------|---------------------------|-------------------|-----------|--------|
| JT-001 | 2026-08-09 | pre-pgt | Intel corporativa PGT | Investigación RUC, RNP, Camino Inca, modelo de negocio público para la postulación | Empresa Cusco; 4 sitios idioma | `archivo-original/empleo-seo/01-INSIGHTS-Peru-Grand-Travel.md` | hecho |
| JT-002 | 2026-08-09 | pre-pgt | Crawl HTTP 4 dominios | Auditoría técnica preliminar EN/ES/PT/IT (no era “solo 4 URLs”; era 4 **sitios**) | EN, ES, PT, IT | `archivo-original/empleo-seo/02-AUDITORIA-SEO-TECNICA-preliminar.md` | hecho |
| JT-003 | 2026-08-13 | pre-pgt | Auditoría SEO 5 hallazgos | Documento de diagnóstico para entrevista; publicado en portafolio | Hallazgos críticos (hreflang, CWV, schema, indexación, arquitectura) | https://jairosaul.com/peru-grand-travel | hecho |
| JT-004 | 2026-08-15 | pre-pgt | Mapa equivalencias hreflang | ~60 tours cruzados EN\|ES\|PT\|IT | CSV equivalencias + gaps de catálogo | `archivo-original/empleo-seo/equivalencias-hreflang.csv` | hecho |
| JT-005 | 2026-08-15 | pre-pgt | Gaps de catálogo | Qué tours existen en un idioma y no en otro | `gaps-de-catalogo.csv` | mismo folder | hecho |
| JT-006 | 2026-08-18 | pre-pgt | crawler `auditor_seo.py` | Script de crawl automático para repetir la auditoría | Python | `archivo-original/empleo-seo/auditor_seo.py` | hecho |
| JT-007 | 2026-08-18 | pre-pgt | Prototipo hreflang PHP | Plugin/prototipo para 4 WP separados (WPML no aplica) | `hreflang-multidominio.php` | mismo folder | hecho |
| JT-008 | 2026-08-20 | pre-pgt | Generador mapa hreflang | `generar_mapa_hreflang.py` | Python | mismo folder | hecho |
| JT-009 | 2026-08-22 | pre-pgt | Plantillas JSON-LD turismo | Offer, TouristTrip, sin `$0` falso | Markdown plantillas | `archivo-original/empleo-seo/plantillas-jsonld-turismo.md` | hecho |
| JT-010 | 2026-08-22 | pre-pgt | Benchmark competidores Cusco | Posicionamiento vs agencias locales | `08-BENCHMARK-COMPETIDORES-CUSCO.md` | hecho |
| JT-011 | 2026-08-22 | pre-pgt | Playbook 90 días | Plan de aportes post-contratación | `14-PLAYBOOK-APORTES.md` | hecho |
| JT-012 | 2026-08-22 | pre-pgt | Plan editorial EN | Blogs EN vacíos vs ticket alto | `09-PLAN-EDITORIAL-INGLES.md` | hecho |
| JT-013 | 2026-08-22 | pre-pgt | OTAs y competidores | GYG / Viator contexto margen | `11-OTAS-Y-COMPETIDORES.md` | hecho |
| JT-014 | 2026-08-24 | pre-pgt | Landing jairosaul.com | Entregable público de la auditoría | URL canónica de la postulación | https://jairosaul.com/peru-grand-travel | hecho |
| JT-015 | 2026-08-24 | pre-pgt | Correo + CV | Envío postulación con link a landing | `15-CORREO-CV.md` | hecho |
| JT-016 | 2026-08-24 | pre-pgt | Guion video Loom | Recorrido de hallazgos para no leer PDF en pantalla | `10-GUION-VIDEO.md` | hecho |
| JT-017 | 2026-08-24 | pre-pgt | Guiones entrevista / sueldo | Contacto, técnica, KPIs, híbrido | `05-GUIONES-…md`, `13-SUELDO-MAXIMO-Y-REMOTO.md` | hecho |
| JT-018 | 2026-08-24 | pre-pgt | Currículo SEO técnico | Dossiers T00–T06 + D01–D03 (rastreo, index, CWV, schema, WP WAF) | `10-aprendizaje/` + copias en `archivo-original/empleo-seo/` | hecho |
| JT-019 | 2026-08-31 | pre-pgt | 30 artículos MDX jairosaul | Contenido SEO/GEO turismo (hreflang, schema, WA checkout, mercados) | carpeta `conocimiento/articulos-jairosaul/` | hecho |
| JT-020 | 2026-08-25 | onboarding | Día 1 oficina | `marketing@`, NAS `192.168.1.87`, Drive, Excel Accesos, grupo WA “Sin Jefe” | Bloque tours **3** + blogs **4**; S/ 3.500 oral | `01-situacion/BITACORA.md` | hecho |
| JT-021 | 2026-08-25 | onboarding | Usuario NAS `linux_admin` | Creado; Ricardo aún no avisado (sigue pendiente de mensaje) | OMV hostname `marketingpgt` | `02-empresa/NAS-Y-ACCESOS.md` | hecho |
| JT-022 | 2026-08-25 | carrera | Pacto Clever oral | 3500 ahora · revisión ~25 sep → jefe mkt 5000 | Norte: qualified leads + marca | `07-negociacion/WHATSAPP-PACTO-REVISADO.md` | hecho (escrito WA pendiente) |
| JT-023 | 2026-08-26 | seo-ops | Análisis bloque Jairo | 18 tours + 115 blogs EN | CSV prioridades P0/P1 | `03-seo/BLOQUE-JAIRO.md` | hecho |
| JT-024 | 2026-08-26 | seo-ops | Inventario Drive + GA4 | Mapa carpetas Seo / ventas; propiedades GA4 EN/PT/ES | EN `368486554` · GTM `GTM-K8SZBJM5` | `02-empresa/DRIVE-INVENTARIO.md` | hecho |
| JT-025 | 2026-08-26 | seo-ops | Drupal decidido | Clever: VPS Ubuntu interno; mes 1 migración EN; Jairo dueño SEO cutover | Staging **no** Banahosting | oral → `HECHOS.md` | hecho |
| JT-026 | 2026-08-27 | seo-ops | Interino = Einel | Jefe mkt mañanas; GSC propietario `marketing@` | `EinelEH@gmail.com` | bitácora | hecho |
| JT-027 | 2026-08-27 | seo-ops | Baseline GSC EN 28d | Clics / impresiones / CTR / posición | **643 clics · 116k imp · CTR 0,6% · pos 25,6** | informe 27 ago | hecho |
| JT-028 | 2026-08-28 | drupal | Staging vs WP | IP OVH `147.135.114.64`; Drupal 11 + Commerce; Salkantay `/product/9`; Things MP **404**; cart sin WA; 0 JSON-LD | Solo migran EN primero | `03-seo/auditorias/` | hecho |
| JT-029 | 2026-08-28 | seo-ops | Inventario 133 URLs | Bloque Jairo para migración | 18 tours + 115 blogs | `inventario-bloque-jairo.csv` | hecho |
| JT-030 | 2026-08-28 | seo-ops | Mapa 25 URLs WP→Drupal | Prioridad 301 / paridad | `mapa-urls-wp-drupal.csv` | hecho |
| JT-031 | 2026-08-28 | seo-ops | Checklist + playbook Drupal | Pre-launch + playbook WP→Drupal | `CHECKLIST-PRE-LAUNCH-DRUPAL.md` | hecho |
| JT-032 | 2026-08-28 | seo-ops | Fix CTR Things MP | Rank Math title `12 Things to Do in Machu Picchu (2026 Guide)` + indexación GSC | ~6.115 imp baseline | post WP 18674 | hecho |
| JT-033 | 2026-08-28 | pgt-web | POC Next.js | Scaffold tour + blog, schema, WA, Lighthouse | Deploy `pgt-poc.vercel.app` · Lighthouse tour **99** vs WP ~55 vs Drupal ~13 | `pgt-poc` + `LIGHTHOUSE-COMPARATIVA.md` | hecho |
| JT-034 | 2026-08-28 | investigación | CRM mapeado | No hay CRM vivo; WA + sheets + RD Station + Mailchimp | **No construir** mes 1 | `CRM-PGT-Y-VECTORIFY.md` | hecho |
| JT-035 | 2026-08-29 | carrera | Plan 30 días → 5000 | Criterios revisión jefatura | `PLAN-30-DIAS-5000.md` | hecho |
| JT-036 | 2026-08-31 | pgt-web | Empieza `pgt-web` | Next.js EN SSG: scrape tours/blogs/pages | Preview luego `perugrandtravel.vercel.app` | repo `pgt-web` | hecho |
| JT-037 | 2026-09-01 | drupal | Pack migración 18 tours | Export WP JSON+MD 18/18; CSV maestro 133; clipboard SEO; estimación ~56 h | `wp-export-tours-jairo/` | hecho |
| JT-038 | 2026-09-01 | seo-ops | GSC 15k + GA4 174 landings | Exports automatizados | `gsc-export-2026-09-01/` · `ga4-export-2026-09-01/` | hecho |
| JT-039 | 2026-09-01 | seo-ops | 454 redirects blog | Categoría → URL limpia | `redirects-blog-301.csv` | hecho |
| JT-040 | 2026-09-01 | seo-ops | Sitemap live | 69 tours · 452 blogs · 62 pages | `inventario-sitemap-2026-08-31/` | hecho |
| JT-041 | 2026-09-01 | seo-ops | MCP Google + SA | GA4 + GSC EN + Drive; verify | GCP `pgt-cursor-agent` | `GUIA-CONEXION-GOOGLE.md` | hecho |
| JT-042 | 2026-09-01 | drupal | 101 capturas admin | Mapa formulario Product AnyMerce | `10-aprendizaje/drupal/` | hecho |
| JT-043 | 2026-09-01 | carrera | Experimento 4 SEO | Pista A Drupal QA · Pista B Next.js | `EXPERIMENTO-4-ESTRATEGIA-JAIRO.md` | hecho |
| JT-044 | 2026-09-01 | carrera | Informe semana 1 | Maestro + 1 pág. externo | 6/7 entregables semana 1 | `INFORME-EXTERNO-SEMANA1-JAIRO.md` | hecho |
| JT-045 | 2026-09-01 | pgt-web | GTM dataLayer | Evento `whatsapp_click` (tag GA4 **humano** pendiente) | GTM `GTM-K8SZBJM5` | `pgt-web/src/lib/analytics.ts` | parcial |
| JT-046 | 2026-09-01 | pgt-web | Paridad + schema | 117 301 blog; sitemap/robots/llms.txt; JSON-LD sin Offer $0 | checklist 30/30 | `pgt-web` | hecho |
| JT-047 | 2026-09-01 | pgt-web | Imágenes WebP | Pipeline self-hosted ~646 | `public/` | hecho |
| JT-048 | 2026-09-02 | drupal | Piloto Humantay | Tour maestro 5 tabs; no Salkantay primero | `#57` `/tour/humantay-lake-full-day` | guías tour maestro | hecho |
| JT-049 | 2026-09-02 | drupal | Master pack v4 | `drupal-pack.json` + scores; avg 84.2 → 90.5 con Drive | `TOUR-MIGRATION-MASTER-SCHEMA.md` | hecho |
| JT-050 | 2026-09-02 | drupal | Supplement atendimento@ | Tabs vacíos WP ← PPTX Drive | 5 tours score 100 | `modelo-supplement.json` | hecho |
| JT-051 | 2026-09-02 | pgt-web | UX conversión | TrustBar, WA sticky, finder, cards, destinos | reviews `data/reviews.json` (TrustIndex scrape, no API live) | `pgt-web` | hecho |
| JT-052 | 2026-09-02 | pgt-web | Preview sin SSO | `https://perugrandtravel.vercel.app` + `noindex` en vercel.app | proyecto Vercel `prj_PGp7L8czgxfAa841xS55b1oYWlFO` | hecho |
| JT-053 | 2026-09-02 | pgt-web | Blueprint Fase A | Beta `next.` sin tocar www | `BLUEPRINT-FASE-A-BETA-CUTOVER.md` | hecho |
| JT-054 | 2026-09-02 | pgt-web | Precios OTAS | Pipeline merge+apply; tarifario 2026 **no** aplicado hasta Ops | 55 precios scrape / 15 quote-only (como WP) | scripts `pgt-web` | parcial |
| JT-055 | 2026-09-02 | tracker | TAREAS-MAESTRO.csv | 3 tracks + sync Sheet Calendario Diario | ~59+ Drupal + Web | `mi-carrera/tracker/` | hecho |
| JT-056 | 2026-09-03 | drupal | Importer lote | CAPTCHA, flood 300s, pathauto, `--fix-alias` | `import-tour-to-drupal.mjs` | hecho |
| JT-057 | 2026-09-03 | drupal | 18/18 HTTP 200 | URLs `/tour/{slug}` en staging; HTML v7 badges `<ul>/<li>` | OVH `147.135.114.64` | `QUE-HACER-AHORA.md` | hecho |
| JT-058 | 2026-09-03 | drupal | Media pipeline | 6 JPEG/tour + Name/Alt/Title; upload script listo | `optimize-tour-images.mjs` | parcial (subida Media Library) |
| JT-059 | 2026-09-03 | carrera | Presentación 4 sep | Tours SEO/GEO + one-pager Clever + capas SEO | `PRESENTACION-4SEP-*.md` | hecho (presentar) |
| JT-060 | 2026-09-03 | hosting-dns | Login Banahosting Clever | 2FA Gmail; client area; Reseller-1 | servicio `38796` · **$239/año** · vence **15 abr 2027** · PayPal | `HOSTING-BANAHOSTING-INVENTARIO.md` | hecho |
| JT-061 | 2026-09-03 | hosting-dns | “Mis Dominios” vacío | Dominios **no** comprados en Bana; registrador GoDaddy/Registros.com | NS sitios: `ns1/ns2.perutrilhainca.com` | inventario | hecho |
| JT-062 | 2026-09-03 | hosting-dns | 17 cuentas WHM | List Accounts en `priva80.privatednsorg.com:2087` | CloudLinux 8.10 · cPanel 136 · user reseller `hwxniobv` | tabla 17 dominios | hecho |
| JT-063 | 2026-09-03 | hosting-dns | EN = `perugran` | `perugrandtravel.com` IP **50.31.188.120** Plan10Gb desde 2017-05-16 | contacto WHM `marketing@` | inventario | hecho |
| JT-064 | 2026-09-03 | hosting-dns | Satélites + 3 `.pe` | mercadomovil, perubienesraices, tejidosmarangani (¿otro negocio?) | IPs `50.31.188.117–124` | inventario | hecho |
| JT-065 | 2026-09-03 | hosting-dns | cPanel 500 | Clic CP → `/xfercpanel` · Error ID `381fb3f66720c` · `cpsrvd` | Load WHM **47 → 58** (crítico) | capturas WHM | bloqueado cPanel |
| JT-066 | 2026-09-03 | hosting-dns | Zone Manager OK | 17 zonas DNS editables sin cPanel | Incluye `perugrandtravel.com` | WHM `scripts7/zone_editor` | hecho |
| JT-067 | 2026-09-03 | hosting-dns | Modal CNAME 2 campos | WHM no muestra TTL/Target; campos **Nombre** + **CNAME** | Placeholder Nombre = FQDN | ver guía abajo / inventario | en curso |
| JT-068 | 2026-09-03 | hosting-dns | DNS público EN (DoH) | NS perutrilhainca; A `@`/`www` → `.120`; **MX Google Workspace** | `next.` aún **NXDOMAIN** | consulta 3 sep 2026 | hecho |
| JT-069 | 2026-09-03 | pgt-web | Docs hosting | Guía Bana vs Vercel + workaround 5.1.5 | `pgt-web/docs/HOSTING-DNS-VERCEL-VS-BANAHOSTING.md` | hecho |
| JT-070 | 2026-08-25 | seo-ops | Inventario sistemas (Excel) | Más sitios que la auditoría pública de 4 dominios | Explica 4 personas SEO | `INVENTARIO-SISTEMAS.md` | hecho |
| JT-071 | 2026-09-01 | pgt-web | Integraciones Google | Scripts sync GSC/GA4; Ads 421-897-0045 sin vincular GA4 EN | `INTEGRACIONES.md` | parcial (ES GSC SA) |
| JT-072 | 2026-09-02 | producto | Catálogo / fichas | CEREBRO paquetes modelo Drive atendimento@ | `04-producto/` | en curso |
| JT-073 | 2026-09-03 | drupal | Producto basura #68 | `Amazon rainforest express-3d` — pedir borrar | staging | pendiente Einel |
| JT-074 | 2026-09-03 | drupal | CSS theme Einel | `tour-maestro-styles.css` global + sidebar Amazon | mensaje listo | pendiente Einel |
| JT-075 | 2026-08-26 | equipo | Lizet Ads AM / SEO PM | Paid ↔ orgánico aún sin mapa landings | `ADS-GOOGLE-META.md` | pendiente sesión |
| JT-076 | 2026-09-01 | investigación | Vaultwarden diseño | Excel passwords = legacy | `GESTION-ACCESOS-DISENO.md` | diseño (no implantado) |
| JT-077 | 2026-09-03 | pgt-web | Scorecard multimercado | EN cutover vs Drupal; 1 dominio/idioma | `pgt-web/docs/BETA-SCORECARD-Y-MULTIMERCADO.md` | hecho |
| JT-078 | 2026-09-03 | carrera | Este mapa + checklist vivo | Unificar hilación pre-empleo → Banahosting | este archivo + `TAREAS-VIVAS.md` | hecho |

---

## Dominios vistos en WHM (3 sep 2026) — no olvidar

| Dominio | IP A | Rol |
|---------|------|-----|
| perugrandtravel.com | 50.31.188.120 | EN WP prod |
| machupicchupacotes.com | .121 | PT |
| viajesmachupicchutours.com | .124 | ES |
| viaggiomachupicchu.it | .124 | IT |
| luxuryperutour.com | .124 | lujo |
| vinicuncaperu.com | .118 | Vinicunca |
| incatrailbookings.com | .124 | bookings |
| ingressosmachupicchu.com | .118 | ingressos |
| paquetesdeviajesperu.com | .123 | ES legacy |
| machupicchuperu.com.mx | .119 | MX |
| tripstomachupicchu.us | .124 | satélite US |
| perutravelguides.com | .124 | contenido |
| dicasviagem.com | .119 | blog PT |
| perutrilhainca.com | .117 | ancla reseller; 301 → PT trilha |
| mercadomovil.pe | .119 | ¿otro negocio? |
| perubienesraices.pe | .119 | ¿otro negocio? |
| tejidosmarangani.pe | .119 | ¿otro negocio? |

Drupal staging **no** está en esta caja: OVH `147.135.114.64`.
