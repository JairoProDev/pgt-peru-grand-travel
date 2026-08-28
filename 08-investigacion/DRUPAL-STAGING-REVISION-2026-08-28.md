# Revisión staging Drupal — OVH · 28 ago 2026

**URL:** [http://147.135.114.64/](http://147.135.114.64/)  
**Hosting:** OVH VPS (IP pública) · nginx/1.28.3 · Ubuntu  
**Stack:** **Drupal 11** + módulo **Commerce** (`anymerce_*`)  
**Alcance acordado:** solo **inglés** (`perugrandtravel.com`) por ahora  
**Responsable build:** Einer (jefe mkt mañanas)

---

## Estado general (una frase)

**Shell visual avanzado (home + tours demo + Figma aplicado), pero aún NO es migración SEO-ready:** contenido real no importado, URLs distintas a WordPress, sin WhatsApp, SEO técnico débil, rendimiento pesado.

---

## Lo que SÍ está hecho

| Área | Evidencia |
|---|---|
| Home EN | Hero, stats, tours grid, FAQ, partners, footer |
| Diseño | Alineado con Figma (menú, cards, badges Best Seller) |
| Tours demo | ~6 productos (Inca Trail, Salkantay 5D, Lares, etc.) |
| Estructura nueva | `/packages`, `/trek`, `/experiences`, `/about-us` |
| Blog shell | 3 posts **placeholder** (Lima restaurants, Titicaca, Vinicunca) |
| i18n UI | Switcher EN / PT-BR / ES (contenido real solo EN planificado) |
| Drupal 11 | Header `X-Generator: Drupal 11` |

---

## Problemas críticos (SEO / negocio)

| # | Problema | Riesgo |
|---|---|---|
| 1 | **URLs ≠ WordPress** — WP: `/tour/the-classic-salkantay-trek-5d/` · Drupal: `/salkantay-trek-5d-4n` | **301 masivo** obligatorio; si falla = pierden rankings |
| 2 | **Blog real no existe** — `/blog/things-to-do-in-machu-picchu/` → **404** | Tu bloque P0 (6k imp) no migrado |
| 3 | **Title roto** — `\| Peru Grand Travel` (falta título página) | CTR bajo en SERPs |
| 4 | **Meta description** genérica — `"Peru Grand Travel"` | CTR bajo |
| 5 | **0 JSON-LD** detectado en home | Pierden rich snippets tours |
| 6 | **0 enlaces WhatsApp** — hay **"Add to cart"** (Commerce) | **Modelo de conversión distinto** — Clever mide WA/leads |
| 7 | **HTML home ~437 KB** | LCP / CWV malos |
| 8 | **Cache: `no-cache, private` · Max-Age: 0** | Cada visita golpea PHP; lento bajo tráfico |
| 9 | **HTTP sin HTTPS** en IP | No listo producción |
| 10 | **robots.txt permite indexar** — sin `Disallow: /` global | Google **puede indexar staging** si descubre la IP |
| 11 | **Contenido demo** — fechas "Aug 2026", textos genéricos | No es el catálogo real |

---

## Figma vs Drupal

Figma abierto (`node-id=485-3513`): página **detalle tour** — Tour Highlights, aviso Machu Picchu tickets, "You Might Also Like".

Drupal home ya refleja cards similares (badges, precio USD, rating). **El diseño va bien; falta capa SEO + contenido real + paridad conversión.**

---

## Qué implica "esperar a que termine Einer"

| Puedes esperar | No debes esperar |
|---|---|
| Shell visual completo | Baseline GSC / mapa URLs |
| Más tours en Drupal | Checklist SEO pre-cutover |
| Admin Drupal usable | Preguntar: ¿WhatsApp o cart? |
| | **noindex** en staging |
| | Tu POC código (paralelo, no bloqueante) |

---

## Estrategia recomendada (dual track)

### Track A — Aliado de migración Drupal (política)

Tu rol visible: **dueño SEO del cutover EN**.

Entregables:
1. Mapa URL WP → Drupal (CSV)
2. Checklist pre-launch (title, meta, schema, WA, 301, noindex staging)
3. 20 URLs piloto QA
4. Informe semanal a Einer/Clever

### Track B — POC código (privado / staging propio)

**No cancelar Drupal.** Demostrar:

> "Mismo diseño Figma + mismo contenido + **mismas URLs** → más rápido + mejor SEO + admin para no-dev (Payload)."

**MVP óptimo ahora:**
- 1 página Figma = **tour detail** (Salkantay 5D)
- 1 blog P0 = Things Machu Picchu
- Deploy: Vercel + Payload (tu cuenta)
- Comparar: Lighthouse Drupal IP vs tu POC

Cuando tengas números → conversación con Einer: *¿front headless encima del contenido Drupal?* o *¿POC como plan B si cutover falla?*

---

## Accesos — actualizado

| Recurso | Estado | Pedir a |
|---|---|---|
| Staging IP 147.135.114.64 | **Ver (público)** | — |
| Drupal admin staging | **Falta** | Einer |
| Figma diseño | **Sí** (browser) | — |
| GSC / GA4 marketing@ | **Sí** | — |
| wp-admin EN / cPanel | **Probable** (viste cPanel tab) | Ricardo |
| DNS producción | **No** | Einer/Clever cuando toque |
| OVH panel | **No** | Einer |

---

## Mensaje modelo para Einer (WhatsApp)

> Einer, revisé el staging en 147.135.114.64 — el diseño se ve bien y alineado al Figma. Para cuando migremos EN, me gustaría armar el mapa de URLs viejas → nuevas y un checklist SEO (titles, schema, WhatsApp, noindex en staging). ¿Tendremos las mismas URLs de blog/tour o cambian? ¿El checkout sigue siendo WhatsApp o será carrito? ¿Me das acceso admin Drupal para QA?

---

## Próximos pasos

Ver `08-investigacion/MVP-POC-ACCESOS-Y-TODO.md` (actualizar Track B con Figma tour page).
