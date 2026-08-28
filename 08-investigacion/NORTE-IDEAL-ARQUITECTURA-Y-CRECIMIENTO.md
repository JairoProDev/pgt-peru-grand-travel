# Norte ideal — arquitectura, tecnología, SEO/GEO y crecimiento PGT

**Para quién:** Jairo (y quien tenga poder de decisión técnica + marketing)  
**Fecha:** 28 ago 2026  
**Premisa:** *Si tuvieras poder total* para diseñar cómo debería estar todo — sin restricciones políticas del día 1, pero con la realidad del negocio (operador de tours, WhatsApp como checkout, 4 mercados lingüísticos, ~73 tours, ~454 blogs).

**Relacionado (más pragmático / política interna):** `STACK-IDEAL.md`, `mi-carrera/CMS-CUSTOM-VIABILIDAD.md`, `MIGRACION-WP-DRUPAL-PLAYBOOK.md`

---

## 1. Una frase de norte

> **Un catálogo único de verdad, cuatro experiencias web por idioma, HTML ultrarrápido con SEO/GEO impecable, y cada visita medida hasta el WhatsApp que ventas cierra.**

Todo lo demás — servidores, CMS, dominios — existe para servir esa frase.

---

## 2. Qué estamos optimizando (jerarquía de métricas)

Clever mide **leads calificados + marca**. La tecnología debe mover esto, en orden:

| Nivel | Métrica | Por qué importa |
|---|---|---|
| 1 | **Conversaciones WhatsApp calificadas** (por idioma/mercado) | Es el checkout real de PGT |
| 2 | **Leads con UTM trazables** (orgánico vs paid vs IA) | Saber qué canal paga |
| 3 | **Clics orgánicos en URLs de intención comercial** | Tours + landings BOFU |
| 4 | **CTR en SERPs** (title/meta/schema) | Impresiones que ya tienes pero no convierten en clics |
| 5 | **Impresiones / posición** (tablas keywords) | Diagnóstico, no objetivo final |
| 6 | **Core Web Vitals** | Google + conversión (travel: ~+10% conv por 0,1 s LCP en estudios sector) |
| 7 | **Citaciones en IA** (GEO) | Nuevo canal de demanda 2025–2027 |

**Regla:** Una keyword que sube sin WhatsApp es vanidad. Una ficha lenta con buen ranking es dinero quemado.

---

## 3. Arquitectura ideal (diagrama mental)

```
                    ┌─────────────────────────────────────┐
                    │     FUENTE ÚNICA DE VERDAD (CMS)     │
                    │  Tour · Blog · Page · Landing · FAQ  │
                    │  1 ID estable · 4 traducciones       │
                    └─────────────────┬───────────────────┘
                                      │ API (GraphQL/REST)
          ┌───────────────────────────┼───────────────────────────┐
          ▼                           ▼                           ▼
   ┌──────────────┐            ┌──────────────┐            ┌──────────────┐
   │  Front EN    │            │  Front PT    │            │  Front ES/IT │
   │  Next.js     │            │  Next.js     │            │  Next.js     │
   │  Edge CDN    │            │  Edge CDN    │            │  Edge CDN    │
   └──────┬───────┘            └──────┬───────┘            └──────┬───────┘
          │                           │                           │
          ▼                           ▼                           ▼
 perugrandtravel.com      machupicchupacotes.com    viajes… / viaggio…
          │                           │                           │
          └───────────────────────────┴───────────────────────────┘
                                      │
                    hreflang · canonical · schema · sitemap por dominio
                                      │
                                      ▼
                         Google · Bing · IA (GEO) · Ads landings
                                      │
                                      ▼
                    WhatsApp (UTM) · Form · WeTravel · OTAs
                                      │
                                      ▼
                              Ventas → Ops → Reseña → loop
```

**Principio clave:** Separar **contenido** (una vez) de **presentación** (por idioma/mercado) de **medición** (por canal).

---

## 4. Dominios: ¿uno o cuatro?

### Situación actual PGT

| Idioma | Dominio | Rol |
|---|---|---|
| EN | perugrandtravel.com | Mercado USA/UK/AU — ticket alto |
| PT | machupicchupacotes.com | Brasil — volumen |
| ES | viajesmachupicchutours.com | Hispanoamérica + España |
| IT | viaggiomachupicchu.it | Italia — nicho fuerte |
| + | luxuryperutour.com, satélites | Lujo / long-tail |

### Escenario ideal (recomendado)

**Mantener los 4 dominios principales** — ya tienen historial, backlinks y branding por mercado. **No unificar en un solo dominio** salvo greenfield.

**Pero cambiar la lógica:**

| Hoy (mal) | Ideal (bien) |
|---|---|
| 4 WordPress independientes | 1 backend de contenido |
| Catálogo duplicado / huecos (19 tours faltan en PT) | 1 registro `Tour` con traducciones obligatorias |
| 0 hreflang | `hreflang` + `x-default` en cada par de URLs |
| 4 admins distintos | 1 panel con roles por idioma |
| 4 plugins distintos | 0 plugins de terceros en front |

**Alternativa válida (solo si empezaran de cero):**  
`perugrandtravel.com/en/`, `/pt/`, `/es/`, `/it/` con subdirectorios + hreflang.  
**Para PGT no conviene** migrar dominios históricos a subcarpetas — el costo SEO/político supera el beneficio.

### Reglas de dominio

1. **Cada URL tiene exactamente una versión canónica** por idioma.
2. **hreflang** bidireccional entre las 4 versiones de cada tour/blog.
3. **`x-default`** → EN (`perugrandtravel.com`) — mercado global + IA en inglés.
4. **Satélites** (luxury, vinicunca): o se integran al catálogo con 301, o quedan como landings con `noindex` si duplican.
5. **Staging:** subdominios `staging.perugrandtravel.com` con **noindex** + auth — nunca IP pública indexable.
6. **POC/pruebas:** `poc.perugrandtravel.com` — noindex hasta decisión.

---

## 5. ¿Un sitio web o varios?

### Respuesta ideal

**Varios dominios, una plataforma.**

| Capa | Cantidad | Tecnología ideal |
|---|---|---|
| **Frontends públicos** | 4 (EN/PT/ES/IT) | 1 codebase Next.js con i18n routing por host |
| **CMS / admin** | 1 | Payload CMS o Sanity |
| **Base de datos** | 1 primaria | PostgreSQL |
| **Media** | 1 bucket + CDN | Cloudflare R2 o S3 + img proxy |
| **Analytics** | 1 propiedad GA4 + 4 data streams | Por dominio/idioma |
| **GSC** | 4 propiedades (o 1 dominio raíz si unifican) | Una por dominio vivo |

**No ideal:** 4 repos, 4 CMS, 4 equipos publicando catálogos distintos.

---

## 6. Stack tecnológico ideal (capa por capa)

### 6.1 Frontend (lo que ve Google y el viajero)

| Componente | Tecnología ideal | Por qué |
|---|---|---|
| Framework | **Next.js 15+** (App Router) | SSR/SSG/ISR, SEO, React, ecosistema |
| Alternativa ligera | **Astro** (solo blogs/landings estáticas) | Aún más rápido; menos dinámico para tours |
| Estilos | **Tailwind CSS** + tokens Figma | Consistencia diseño, bundle pequeño |
| i18n | **next-intl** o routing por `host` | 4 dominios → locale automático |
| Imágenes | **next/image** + CDN (Cloudinary/imgix) | WebP/AVIF, LCP |
| Fuentes | **next/font** (self-hosted) | Sin FOIT, sin Google Fonts bloqueante |

**Objetivo CWV mobile:** LCP < 2,0 s · INP < 200 ms · CLS < 0,1 en fichas tour.

### 6.2 CMS (capa para no-programadores)

| Componente | Tecnología ideal | Por qué |
|---|---|---|
| CMS headless | **Payload CMS 3.x** | TypeScript, self-host, campos SEO custom, roles |
| Alternativa SaaS | **Sanity** | Menos ops, más coste mensual |
| **Evitar como único CMS** | Drupal / WordPress monolito | Más lento front, más plugins, peor CWV |
| **Evitar** | Admin 100% custom desde cero | Reinventas usuarios, media, revisiones, preview |

**Módulos obligatorios en admin:**

| Módulo | Usuarios | Campos críticos |
|---|---|---|
| **Tour** | SEO, ops, CM | slug (bloqueado post-publish), precio+moneda por mercado, duración, dificultad, includes, CTA WA por idioma, galería, schema flags |
| **Blog** | CM, SEO | editor rich, categoría, autor, fecha, SEO fields, enlaces internos sugeridos |
| **Page** | CM | home, about, legal |
| **Landing Ads** | Lizet | template sin menú, UTM preset, noindex opcional |
| **FAQ** | CM / SEO | reutilizable en tours + schema FAQPage |
| **Redirect** | Ricardo / SEO | 301 manager con regex |
| **Media** | Diseño | alt obligatorio, compresión automática |
| **Review snippet** | SEO | agregación TripAdvisor/Google (manual o API) |

**Workflow pre-publicar (automático):**  
Checklist: ¿title? ¿meta? ¿precio? ¿WA? ¿hreflang completo? ¿imagen hero < 200 KB? → si falla, no publica.

### 6.3 Backend / API

| Componente | Ideal |
|---|---|
| API | GraphQL (Payload nativo) o REST |
| Auth admin | Payload users + 2FA |
| Preview | Draft mode Next.js + token |
| Webhooks | Revalidate ISR al publicar |
| Search interno | Algolia o Meilisearch (opcional, mes 6+) |

### 6.4 Base de datos

| Uso | Tecnología |
|---|---|
| Contenido + usuarios | **PostgreSQL 16** (Neon, Supabase, o RDS) |
| Cache / sesiones | **Redis** (Upstash serverless) |
| Logs analytics propios | ClickHouse o BigQuery (fase 2) |

**No ideal:** MySQL en VPS sin réplicas, sin backups automáticos.

### 6.5 Infraestructura y hosting

| Capa | Ideal | Alternativa aceptable |
|---|---|---|
| **Front + SSR** | **Vercel** (edge, ISR, preview deploys) | Cloudflare Pages |
| **CMS** | Payload en **Railway / Fly.io / VPS OVH** con Docker | Mismo Vercel si Payload 3 serverless |
| **CDN** | **Cloudflare** (DNS + WAF + cache + bot fight) | Incluido en Vercel |
| **Media** | **Cloudflare R2** o S3 + CDN | NAS OMV para archivo maestro, CDN para web |
| **Email transaccional** | Resend / Postmark | — |
| **Backups DB** | Diario automático + retención 30 d | — |

**Por qué no un solo VPS OVH para todo (como staging Drupal actual):**

- Sin edge = LCP malo para USA/Europa
- Un servidor = SPOF (single point of failure)
- Cache `no-cache, private` en Drupal staging = señal de config mala
- Tú ops 24/7 — no escala

**Arquitectura híbrida realista para PGT:**

```
Viajero USA → Cloudflare edge (Miami) → Vercel SSR (Next) → API CMS
Viajero BR  → Cloudflare edge (SP)     → misma app, locale PT, dominio machupicchu…
Admin CM    → admin.pgt.internal o Payload en subdominio auth
Archivo RAW → NAS OMV (fotos originales) → sync a R2
```

### 6.6 Lo que NO va en el stack ideal

- 30+ plugins WordPress (Tourmaster, Goodlayers, PixelYourSite…)
- Constructor visual en producción (Elementor-style)
- jQuery + 40 JS en ficha tour
- Checkout e-commerce pesado si el cierre es WhatsApp (Commerce cart en Drupal staging = desalineación negocio)
- Staging indexable en IP pública
- CRM custom como proyecto SEO mes 1

---

## 7. SEO técnico ideal

### 7.1 URLs

| Regla | Detalle |
|---|---|
| Slugs estables | `/tour/the-classic-salkantay-trek-5d/` — no cambiar por Figma |
| Trailing slash | Política única (con o sin `/`) — 301 la variante mala |
| Blogs | Una canónica: preferir `/blog/slug/` sin categoría en URL |
| Parámetros | `?utm_*` ok; no indexar filtros (`?sort=`, `?page=2` con rel prev/next) |
| Migración | Mapa 301 1:1 — **cero cadenas** A→B→C |

### 7.2 On-page (cada tour)

```
<title> — keyword + duración + marca (≤60 chars)
<meta description> — beneficio + CTA implícito (120–155 chars)
<link rel="canonical">
<link rel="alternate" hreflang="en|pt|es|it|x-default">
<h1> — una sola, distinta de title
Precio visible above the fold + moneda (Offer schema)
CTA WhatsApp con data-attribute para GA4 event
Imágenes: alt descriptivo, width/height, lazy below fold
Enlaces internos: 3–5 tours relacionados + 1 blog relevante
```

### 7.3 Schema JSON-LD (obligatorio por tipo)

| Tipo página | Schema |
|---|---|
| Home | `TravelAgency` + `WebSite` + `SearchAction` |
| Tour | `TouristTrip` o `Product` + `Offer` + `AggregateRating` + `FAQPage` (si hay FAQ) |
| Blog | `Article` o `BlogPosting` + `BreadcrumbList` |
| FAQ | `FAQPage` |
| Breadcrumb | `BreadcrumbList` en todas |

**Generación:** código TypeScript en Next — no depender de plugin que outputea JSON inválido.

### 7.4 Sitemaps

- `/sitemap.xml` índice por dominio
- Sub-sitemaps: tours, blogs, pages, images
- `lastmod` real desde CMS
- Enviado a GSC por propiedad
- **No** incluir URLs noindex, staging, parámetros

### 7.5 robots.txt

```
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /api/
Disallow: /preview/
Sitemap: https://www.perugrandtravel.com/sitemap.xml
```

Staging:

```
User-agent: *
Disallow: /
```

### 7.6 Indexación internacional

```html
<link rel="alternate" hreflang="en" href="https://www.perugrandtravel.com/tour/..." />
<link rel="alternate" hreflang="pt-BR" href="https://www.machupicchupacotes.com/tour/..." />
<link rel="alternate" hreflang="es" href="https://www.viajesmachupicchutours.com/tour/..." />
<link rel="alternate" hreflang="it" href="https://www.viaggiomachupicchu.it/tour/..." />
<link rel="alternate" hreflang="x-default" href="https://www.perugrandtravel.com/tour/..." />
```

**Validación mensual:** GSC → Internacional → errores hreflang.

### 7.7 Contenido duplicado

- Blog EN duplicado con/sin categoría → 301 a canónica
- Satélites que repiten tour → 301 o canonical al dominio principal del idioma
- PDFs indexables → noindex o canonical

---

## 8. GEO — Generative Engine Optimization (2026+)

Las IAs (ChatGPT, Perplexity, Google AI Overviews) citan fuentes **estructuradas, claras, autoritativas**.

### 8.1 Qué implementar

| Pieza | Acción |
|---|---|
| **Contenido citables** | FAQs con respuestas directas (40–80 palabras), listas, tablas comparativas |
| **E-E-A-T** | Autor con bio, fecha actualizada, “Reviewed by” guía local |
| **Schema rico** | FAQ, HowTo (itinerarios), TouristTrip |
| **llms.txt** | `/llms.txt` — mapa de URLs importantes para crawlers IA |
| **Datos factuales** | Precios, duraciones, permisos Inca Trail — sin marketing fluff |
| **Entidades** | Machu Picchu, Cusco, Salkantay — enlazadas con contexto |
| **Reseñas** | AggregateRating real (TripAdvisor, Google) |
| **Freshness** | `dateModified` visible en blogs estacionales |

### 8.2 Tipos de contenido que ganan en IA

1. “Best time to visit Machu Picchu” — tabla por mes  
2. “Inca Trail permits 2026” — datos actualizados  
3. “Salkantay vs Inca Trail” — comparativa honesta  
4. “How to get from Cusco to Machu Picchu” — pasos numerados  

**Tu bloque EN** ya tiene blogs con impresiones altas en estas intenciones — hoy con CTR bajo. GEO + title/meta = palanca doble.

### 8.3 Qué evitar

- Contenido genérico AI-spam (Google Helpful Content penaliza)  
- Páginas sin autor ni fecha  
- Contradicciones de precio entre idiomas  

---

## 9. Herramientas ideales (stack de medición y operación)

### 9.1 SEO / orgánico

| Tool | Uso | Prioridad |
|---|---|---|
| **Google Search Console** | 4 propiedades, export mensual | P0 |
| **GA4** | 4 data streams, eventos WA | P0 |
| **Looker Studio** | Dashboard leads por idioma/canal | P1 |
| **Screaming Frog** | Crawl pre/post migración | P1 |
| **Ahrefs o Semrush** | Keywords, backlinks, gap (1 licencia equipo) | P1 |
| **PageSpeed / CrUX** | CWV field data | P0 |
| **Rich Results Test** | Validar schema | P0 |
| **Sheet keywords** | Mantener hasta BI real | P0 (transición) |

### 9.2 Paid / atribución

| Tool | Uso |
|---|---|
| **Google Ads** | Search + PMax con landings dedicadas |
| **Meta Ads** | Lizet — creativos → URL específica |
| **GTM** | Un contenedor, tags centralizados (no PixelYourSite × 4) |
| **UTM builder** | Plantilla equipo — `utm_source`, `utm_campaign`, `utm_content` hasta WA |

### 9.3 Contenido / diseño

| Tool | Uso |
|---|---|
| **Figma** | Diseño — export a componentes React |
| **Payload admin** | Publicación tours/blogs |
| **Canva** | Social — no para web producción |
| **NAS OMV** | Archivo fotos RAW — no servir directo al público |

### 9.4 CRM / leads (ideal, fase 2 — no construir custom mes 1)

| Tool | Rol ideal |
|---|---|
| **WhatsApp Business API** + inbox (Respond.io, Trengo, o RD Station inbox) | Cola por idioma, UTM visible, asignación ventas |
| **RD Station** o **HubSpot** | Pipeline, scoring, email nurture |
| **Sheet DAI/Paloma** | Migrar a CRM — no duplicar eternamente |
| **WeTravel** | Pagos — integrar link en ficha post-WA |

**No ideal:** CRM custom desde cero mientras migras 600 URLs.

### 9.5 DevOps

| Tool | Uso |
|---|---|
| **GitHub** | Mono-repo `pgt-platform` |
| **Vercel** | Deploy front + preview por PR |
| **GitHub Actions** | CI: lint, typecheck, Lighthouse CI |
| **Sentry** | Errores producción |
| **UptimeRobot / Better Stack** | Alertas caída |

---

## 10. Flujo de contenido ideal

```
Ops confirma producto operable
        ↓
SEO/CM crea tour en CMS (EN master)
        ↓
Traducción PT/ES/IT (humana o asistida IA + revisión nativa)
        ↓
Checklist automático (SEO fields, precio, WA, imágenes)
        ↓
Preview en staging → QA SEO (tú o checklist bot)
        ↓
Publish → ISR revalidate → sitemap update → ping GSC
        ↓
Monitoreo 7d: GSC impresiones, GA4 WA clicks
        ↓
Iteración title/meta si CTR bajo
```

**Roles:**

| Rol | Responsabilidad |
|---|---|
| **Jefe SEO/GEO (tú)** | Arquitectura, schema, hreflang, migración, priorización |
| **CM / redactor** | Blogs, copy tour, traducciones |
| **Lizet** | Landings Ads, UTM, alineación paid-orgánico |
| **Ricardo / dev** | Infra, DNS, redirects, deploys |
| **Ops / ventas** | Verdad operativa (precios, cupos, qué se vende) |
| **Clever** | Norte, presupuesto, no microgestionar stack |

---

## 11. Crecimiento: de tecnología a clientes (playbook)

### Fase A — Arreglar la tubería (mes 1–2)

**Objetivo:** No perder lo que ya tienes.

1. Línea base GSC + GA4 por dominio  
2. hreflang en 4 dominios (aunque sea WP actual)  
3. Arreglar titles/metas P0 (blogs 5k+ imp, CTR < 1%)  
4. WhatsApp con UTM en los 4 sitios  
5. Evento GA4 `whatsapp_click`  
6. noindex staging  
7. Mapa 301 listo **antes** de cutover  

**Resultado esperado:** +10–30% clics sin subir posiciones (solo CTR).

### Fase B — Velocidad + confianza (mes 2–4)

**Objetivo:** Más conversión por visita.

1. Front Next.js en fichas tour (POC → producción gradual)  
2. LCP < 2,5 s mobile en top 20 URLs  
3. Schema completo tours + FAQ  
4. Reseñas visibles (TripAdvisor widget o estático)  
5. Landings Ads → URL dedicada, no home  

**Resultado esperado:** +5–15% WA clicks por misma sesión orgánica.

### Fase C — Contenido que captura demanda (mes 3–6)

**Objetivo:** Más impresiones en intención alta.

1. Publicar huecos catálogo PT (19 tours) — **solo si Ops confirma**  
2. Clusters GEO: Machu Picchu, Inca Trail, Salkantay, “best time”  
3. Enlazar blogs → tours (internal linking programático)  
4. Actualizar fechas/permissos 2026/2027 en posts estacionales  
5. IT blog TOFU (hoy casi solo BOFU)  

**Resultado esperado:** impresiones +20–40% en bloques trabajados (6–12 meses).

### Fase D — Escala internacional (mes 6–12)

1. Un CMS, cero huecos de catálogo  
2. Campañas paid por mercado con landings nativas  
3. Email nurture post-WA (RD Station)  
4. Programa reseñas post-viaje  
5. GEO: monitor citaciones en Perplexity/ChatGPT búsquedas test  

**Resultado esperado:** leads calificados +30–50% año 1 (rangos amplios — depende de Ops y ventas).

### Palancas por tipo de página

| Tipo | Palanca #1 | Palanca #2 |
|---|---|---|
| Tour BOFU | Precio claro + WA above fold | Schema + reviews |
| Blog TOFU | Title/meta CTR | Enlaces a 3 tours |
| Home | Trust signals + top tours | LCP hero |
| Landing Ads | Message match + sin menú | Velocidad |
| PT/IT | Catálogo completo | hreflang + copy nativo |

---

## 12. Seguridad ideal

| Capa | Medida |
|---|---|
| DNS | Cloudflare proxy ON |
| WAF | Cloudflare OWASP + rate limit |
| CMS admin | VPN o IP allowlist + 2FA |
| Dependencias | Dependabot / Renovate |
| WordPress legacy | Modo lectura post-migración; desactivar plugins |
| Backups | DB diario + media semanal |
| Secretos | Vault / 1Password equipo — nunca Excel en repo |
| Staging | noindex + auth básica |

**Lección virus 2026:** plugins nulled = vector. En stack ideal **no hay plugins en front**.

---

## 13. Comparativa: hoy vs ideal

| Dimensión | Hoy (WP × 4) | Drupal (en curso) | **Ideal (headless)** |
|---|---|---|---|
| Catálogo | 4 silos, huecos | 1 Drupal (EN primero) | 1 CMS, 4 fronts |
| Front CWV | Malo (Goodlayers) | Medio-pesado | Excelente (edge) |
| Admin CM | Conocido | Curva alta | Payload intuitivo |
| SEO schema | Roto/incompleto | Depende config | Código, testeado |
| hreflang | 0 | Posible | Obligatorio day 1 |
| Conversión | WA (bien) | Cart (mal alineado) | WA + UTM |
| Migración riesgo | — | Alto (URLs nuevas) | Medio (controlado) |
| Coste mensual | ~$100–200 hosting | VPS OVH + tiempo | ~$100–300 Vercel+DB+CF |
| Talento Cusco | Ricardo WP | Pocos Drupal | Tú + 1 dev JS |
| IA/GEO | No preparado | No nativo | llms.txt + schema |

---

## 14. Roadmap ideal (12 meses) — si tuvieras poder total

### Q1 (mes 1–3): Fundamentos

- [ ] Baseline + dashboards GA4/GSC  
- [ ] hreflang 4 dominios (WP o nuevo)  
- [ ] Mapa 301 completo ~600 URLs  
- [ ] POC Next + Payload: 2 páginas EN  
- [ ] Decisión: ¿cutover EN a headless o arreglar Drupal?  
- [ ] Quick wins CTR (10 URLs P0)  

### Q2 (mes 4–6): Migración EN

- [ ] Cutover `perugrandtravel.com` a Next + Payload  
- [ ] 301 verificados  
- [ ] 60 días vigilancia GSC  
- [ ] Landings Ads Lizet en nuevo stack  
- [ ] Eventos WA + Looker dashboard  

### Q3 (mes 7–9): PT + ES

- [ ] Migrar machupicchu… y viajes…  
- [ ] Completar catálogo PT (traducciones)  
- [ ] Clusters GEO Machu Picchu  

### Q4 (mes 10–12): IT + optimización

- [ ] viaggiomachupicchu.it  
- [ ] Retirar WordPress a modo archivo  
- [ ] CRM inbox unificado WA  
- [ ] Informe anual: tráfico, leads, CWV, citaciones IA  

---

## 15. Equipo mínimo ideal

| Rol | Dedicación | Notas |
|---|---|---|
| Jefe SEO/GEO + producto digital (tú) | Full | Arquitectura, priorización, QA |
| Dev frontend (Next) | 0,5 FTE | Contigo o freelance Lima/remoto |
| CM / traducción | 1 FTE | Blogs + copy 4 idiomas |
| Ricardo | 0,25 FTE | DNS, infra, no CMS day-to-day |
| Lizet | Ads + landings | Alineación orgánico |
| Ventas | Feedback leads | Qué califica / qué no |

**No necesitas:** 4 admins WordPress, agencia Drupal externa, CRM custom dev.

---

## 16. Presupuesto orientativo (ideal, mensual)

| Ítem | USD/mes aprox. |
|---|---|
| Vercel Pro | 20–150 |
| Neon/Supabase Postgres | 0–25 |
| Cloudflare Pro | 20–200 |
| R2/S3 media | 10–50 |
| Payload hosting | 0–30 |
| Ahrefs/Semrush (1 seat) | 100–200 |
| Sentry, uptime | 0–30 |
| **Total** | **~150–500** |

Comparado con: dip SEO por migración mal hecha = **miles en ads para compensar**.

---

## 17. Decisiones que tomaría el primer día con poder total

1. **Congelar slugs** — Figma no toca URLs.  
2. **Un catálogo** — tour ID `PGT-0042`, no “otro post en WP PT”.  
3. **WhatsApp sigue siendo checkout** — no cart e-commerce.  
4. **Next + Payload** como stack objetivo 12 meses.  
5. **Drupal actual** → usar solo si acelera EN **con mismas URLs**; si no, POC headless y decidir con Lighthouse.  
6. **hreflang esta semana** — no “después del sitio nuevo”.  
7. **Medir WA click** — sin eso, SEO es teatro.  
8. **noindex staging** — hoy.  
9. **No CRM custom** — RD Station + WA API primero.  
10. **Publicar solo lo operable** — Ops veto catálogo.

---

## 18. Cómo usar este documento en la vida real (semana 1)

No puedes implementar todo. **Sí puedes alinear decisiones:**

| Este doc dice | Tu acción visible ahora |
|---|---|
| Un catálogo | Pedir a Einel mapa tour IDs WP → Drupal |
| hreflang | Incluir en checklist migración |
| WA > cart | Preguntar decisión a Clever/Einel |
| Next + Payload | Track B POC privado |
| Medir WA | Pedir a Lizet evento GA4 |
| Slugs congelados | Entregable mapa 301 |
| GEO | Mejorar FAQs + schema en auditorías P0 |

**Frase para Clever (cuando toque):**

> El norte no es “Drupal o WordPress”. Es un catálogo único, cuatro webs rápidas por idioma, y medir hasta WhatsApp. Propongo fases: primero no perder Google en la migración EN, luego evolucionar a front moderno con admin para el equipo. Tengo baseline y prioridades.

---

## 19. Referencias internas

- Pragmatismo político: `STACK-IDEAL.md`  
- Viabilidad custom: `mi-carrera/CMS-CUSTOM-VIABILIDAD.md`  
- Migración: `MIGRACION-WP-DRUPAL-PLAYBOOK.md`  
- Staging actual: `DRUPAL-STAGING-REVISION-2026-08-28.md`  
- Modelo negocio: `02-empresa/MODELO-NEGOCIO.md`  
- Herramientas: `02-empresa/MAPA-HERRAMIENTAS.md`  
- CRM (no mezclar): `CRM-PGT-Y-VECTORIFY.md`  
- Tu guía operativa: `01-situacion/GUIA-PASO-A-PASO-COMPLETA.md`

---

*Documento vivo. Actualizar cuando cambie decisión de stack (Drupal vs headless) o dominios activos.*
