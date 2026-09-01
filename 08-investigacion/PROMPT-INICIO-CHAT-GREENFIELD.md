# Prompt para nuevo chat Cursor — Greenfield PGT

**Copia todo el bloque entre `---INICIO---` y `---FIN---` en un chat nuevo.**

---

---INICIO---

## Contexto

Soy Jairo, analista SEO en **Peru Grand Travel (PGT)**. Quiero **reconstruir perugrandtravel.com (EN) desde cero en código puro** — no WordPress, no Drupal en el front. Objetivo: **más leads por WhatsApp**, mejor CTR, mejor velocidad, UX clara (las agencias de tours suelen confundir), SEO/GEO impecable.

**Repo de contexto/planning:** `/home/jairoprodev/proyectos/pgt/`  
**Plan maestro:** lee `08-investigacion/GREENFIELD-PGT-PLAN-MAESTRO.md` PRIMERO.

**POC de referencia (no fork — copiar patrones):**
- GitHub: `JairoProDev/pgt-poc` (leer código, no clonar como base)
- Live: https://pgt-poc.vercel.app
- Nuevo repo: **`pgt-web`** en `/home/jairoprodev/proyectos/pgt-web/`

## Lo que NO se puede perder (SEO)

- **589 URLs** en inventario: 69 tours, 452 blogs, 62 páginas
- Inventario: `03-seo/datos/inventario-sitemap-2026-08-31/inventario-urls.csv`
- Patrones URL sagrados:
  - `/tour/{slug}/`
  - `/blog/{slug}/` (canónica)
  - `/blog/{cat}/{slug}/` → 301 a limpia
  - `/packages/`, `/machu-picchu-packages/` (hubs ads + top conversión)
- GSC baseline: **643 clics / 116k imp / 28d** — `03-seo/datos/GSC-LINEA-BASE-2026-08-27.md`
- Meta title/desc: copiar de WP en v1 (`03-seo/scripts/export-wp-content.py`)

## Negocio

- Checkout = **WhatsApp** (+51 946 622 318), no carrito
- ~89 clics WA/mes (GA4 `chat:51946622318`); ventas reporta ~2 leads EN/mes → optimizar embudo
- Top páginas conversión: `/packages/` (28%), home (19%), `/machu-picchu-packages/` (18%)
- Google Ads EN apunta a esas landings (URL final correcta; display path decorativo)

## Diseño

- Figma: https://www.figma.com/design/jhLCgtdkX4AtItlUD5ooBf/ (node tour `485-3513`)
- Lectura: `08-investigacion/FIGMA-LECTURA.md`
- Poppins, azul `#193A8A`, CTA naranja + WA verde
- **Mejorar UX** respecto a WP: menos menú, WA sticky, un CTA por página, blogs con tours relacionados

## Stack decidido

- **Repo nuevo:** `pgt-web` (patrones de `pgt-poc`, no fork del repo)
- **Next.js 15** App Router + TypeScript + Tailwind
- **Subdominio demo:** `beta.perugrandtravel.com`
- **Carrito:** oculto — solo WhatsApp
- **Drupal:** avanza en paralelo (Pista A) — no tocar ni mencionar en código
- Contenido v1: JSON/MDX desde scrape WP (sin CMS hoy)
- Contenido v2: Payload CMS (semana 2)
- Deploy: Vercel
- Imágenes v1: hotlink `perugrandtravel.com/wp-content/uploads/` via `next/image`
- GTM: `GTM-K8SZBJM5` + evento `whatsapp_click` en dataLayer
- GA4: propiedad `368486554`, measurement `G-NTXD373H4Q`

## Performance target (vs WP actual)

| Métrica | WP | Target |
|---|---:|---:|
| Lighthouse mobile | 55 | 95+ |
| LCP | 6,8s | <2,5s |

Ver: `08-investigacion/LIGHTHOUSE-COMPARATIVA.md`

## Embudo a optimizar

SERP (title/meta/schema) → clic → landing rápida → CTA claro → WhatsApp medido → ventas cierra

## Plantillas necesarias (solo 6)

1. Home
2. Hub (packages, machu-picchu-packages, destinations)
3. Tour (money page)
4. Blog post
5. Blog index
6. Static (about, contact, legal)

## Modelo Tour (campos mínimos)

slug, title, seo{title,description,canonical}, priceFrom USD, duration, difficulty, categories, heroImage, gallery[], summary, itinerary[{day,title,body}], included[], excluded[], faq[], relatedTourSlugs[]

JSON-LD: TouristTrip + Product + Offer + FAQ

## Tu tarea en este chat

### Fase 1 — Planificar (hazlo primero, no codees aún)

1. Lee `GREENFIELD-PGT-PLAN-MAESTRO.md` y confirma stack/estructura
2. Propón estructura de carpetas del repo (`pgt-web` o extend `pgt-poc`)
3. Lista componentes React a crear (design system)
4. Define orden de implementación para **MVP esta tarde**:
   - Home + `/packages/` + tour Salkantay + blog Things MP
   - Header/footer/WA sticky/GTM
   - SEO + JSON-LD + sitemap parcial
5. Identifica qué scripts de scrape necesitas crear
6. Lista redirects 301 necesarios (blogs duales)

### Fase 2 — Construir MVP (después de aprobar plan)

1. Inicializar/extender proyecto Next.js
2. Design tokens Figma → Tailwind config
3. Implementar las 4 páginas MVP con contenido real scrapeado de WP live
4. WhatsApp con UTM + prefill + dataLayer event
5. GTM snippet en layout
6. `next.config.js`: trailing slashes, image domains, redirects básicos
7. Verificar Lighthouse en tour page

### Reglas estrictas

- **Repo nuevo** `pgt-web` — no modificar `pgt-poc` ni `/home/jairoprodev/proyectos/pgt/` (solo docs)
- **Subdominio target:** `beta.perugrandtravel.com` (configurar en Vercel al deploy)
- **Sin carrito** — ningún botón Add to Cart; solo WhatsApp
- **Drupal en paralelo** — no mencionar ni integrar; esto es Pista B independiente
- **NO cambiar slugs/URLs** respecto a WP
- **Trailing slash** como WP (`/tour/slug/`)
- **Mobile first**
- No over-engineer: sin CMS hoy, sin i18n hoy
- Minimizar scope: MVP demostrable > catálogo completo hoy
- Reutilizar lógica del POC si existe en `pgt-poc`
- No tocar repo `/home/jairoprodev/proyectos/pgt/` salvo docs/datos — código nuevo en repo separado

### Archivos de referencia en pgt/

```
08-investigacion/GREENFIELD-PGT-PLAN-MAESTRO.md
03-seo/datos/README.md                                          ← índice todos los datasets
03-seo/datos/keywords-canibalizacion-2026-08-31/INSIGHTS.md   ← LEER PRIMERO
03-seo/datos/keyword-stats-2026-08-26/INSIGHTS.md               ← volumen Google Ads
03-seo/datos/keywords-canibalizacion-2026-08-31/redirects-blog-301.csv
03-seo/datos/keywords-canibalizacion-2026-08-31/{tours,blogs,paginas}.csv
08-investigacion/FIGMA-LECTURA.md
08-investigacion/LIGHTHOUSE-COMPARATIVA.md
08-investigacion/ESQUEMA-MIGRACION-MAESTRO.md
03-seo/guias/MEDIR-LEADS-WEB-ACTUAL.md
03-seo/datos/inventario-sitemap-2026-08-31/
03-seo/datos/GSC-LINEA-BASE-2026-08-27.md
03-seo/scripts/export-wp-content.py
03-seo/scripts/export-wp-sitemap-inventory.sh
```

### URLs MVP para scrapear contenido real

- Home: https://www.perugrandtravel.com/
- Packages: https://www.perugrandtravel.com/packages/
- Tour: https://www.perugrandtravel.com/tour/the-classic-salkantay-trek-5d/
- Blog: https://www.perugrandtravel.com/blog/things-to-do-in-machu-picchu/
- POC referencia: https://pgt-poc.vercel.app/tour/the-classic-salkantay-trek-5d

### Pregunta inicial para ti

Empieza leyendo el plan maestro, luego preséntame:
1. Arquitectura de carpetas propuesta
2. Lista de componentes
3. Plan de implementación por pasos (esta tarde)
4. Qué decisiones necesitas que confirme antes de codear

No empieces a codear hasta que apruebe el plan.

---FIN---

---

## Notas para Jairo (no pegar en el chat)

- Si `pgt-poc` no está clonado localmente, el nuevo chat debe clonarlo primero o crear `pgt-web` adyacente
- Figma no está en repo — usar `FIGMA-LECTURA.md` + capturas si las tienes
- Drupal sigue en paralelo — esto es Pista B, no reemplazo político inmediato
- Después del MVP: subdominio `beta.perugrandtravel.com` para demo Clever
