# Greenfield PGT — Plan maestro (rebuild en código)

**Para:** Jairo · **Fecha:** 1 sep 2026  
**Objetivo:** Reconstruir `perugrandtravel.com` EN en código puro — más rápido, más claro, más convertible — **sin tirar el SEO acumulado**.  
**Handoff prompt:** `08-investigacion/PROMPT-INICIO-CHAT-GREENFIELD.md`

---

## 1. Norte (una frase)

> **Mismo catálogo, mismas URLs que Google ya conoce, experiencia 10× más clara y rápida, cada clic medido hasta WhatsApp.**

No es “otra agencia con plantilla Tourmaster”. Es **un embudo de ventas** disfrazado de sitio web.

---

## 2. Qué NO empezar de cero (activos existentes)

### 2.1 SEO / demanda (lo más valioso)

| Activo | Valor | Dónde está |
|---|---|---|
| **643 clics Google / 28d** | Tráfico orgánico real | `03-seo/datos/GSC-LINEA-BASE-2026-08-27.md` |
| **116k impresiones** | Posicionamiento acumulado | GSC |
| **589 URLs indexables** | Mapa de lo que hay que servir o redirigir | `03-seo/datos/inventario-sitemap-2026-08-31/` |
| **69 tours** `/tour/{slug}/` | Money pages | `tours.txt` |
| **452 blogs** `/blog/{slug}/` | Top of funnel + long-tail | `blogs.txt` |
| **62 páginas** hubs/destinos/legal | Arquitectura de información | `pages.txt` |
| **115 URLs duales blog** | `/blog/cat/slug` → 301 a `/blog/slug` | `blogs-jairo-2026-08-25.csv` |
| Meta title/desc por URL | Copiar verbatim en v1 | `export-wp-content.py` + Sheet keywords |
| Things MP optimizado | Template CTR para blogs | WP post 18674 |

**Regla:** Cambiar slug = perder ranking. **Congelar paths.**

### 2.2 Conversión (lo que ya funciona)

| Activo | Dato | Implicación diseño |
|---|---|---|
| Clics WA / mes | **~89 usuarios** (`chat:51946622318`) | Botón WA sticky en **todas** las páginas |
| Top páginas conversión | `/packages/` 28%, home 19%, `/machu-picchu-packages/` 18% | Priorizar hubs en diseño, no solo tours |
| Blog → WA | **2%** de clics chat | Blogs necesitan **bloque tours + CTA** visible |
| Ventas leads EN | 2 en ago (18, 22) | Embudo post-clic roto — UX + seguimiento, no solo tráfico |
| Checkout real | WhatsApp (+51 946 622 318) | **No** carrito como CTA principal |

### 2.3 Contenido y media

| Fuente | Qué extraer |
|---|---|
| WP live (HTML público) | Título, meta, H1, precio, itinerario, galería |
| Carpeta assets Einer | Imágenes ordenadas por tour |
| Tourmaster fields | Precio USD, duración, includes, dificultad |
| Rank Math (blog) | Focus keyword, meta, canonical |
| Figma | Layout modular, tokens | `08-investigacion/FIGMA-LECTURA.md` |
| Figma URL | https://www.figma.com/design/jhLCgtdkX4AtItlUD5ooBf/ — node tour `485-3513` |

### 2.4 Medición (conectar, no reinventar)

| Herramienta | ID / nota |
|---|---|
| GA4 propiedad EN | `368486554` · measurement `G-NTXD373H4Q` |
| GTM prod | `GTM-K8SZBJM5` + `GTM-NNSPKMFM` |
| Evento WA prod | `chat:51946622318` (plugin) — replicar o unificar |
| Evento WA POC | `whatsapp_click` en `G-V8FFS0SCXB` |
| Google Ads | `421-897-0045` · landings `/packages/`, `/machu-picchu-packages/` |
| GSC | `https://www.perugrandtravel.com/` |
| RD Station | Scripts en prod — mantener si activo |

### 2.5 POC probado (no reinventar la rueda)

| Item | Valor |
|---|---|
| Repo | `github.com/JairoProDev/pgt-poc` (externo) |
| URL | https://pgt-poc.vercel.app |
| Stack | Next.js + Vercel |
| Lighthouse mobile | **100** vs WP **55** |
| LCP | **1,4s** vs **6,8s** |
| JSON-LD | TouristTrip + Product + FAQ |
| Tour piloto | `/tour/the-classic-salkantay-trek-5d` |

**Acción:** Clonar/extender `pgt-poc`, no empezar repo vacío.

### 2.6 Diseño (Figma → código)

| Token | Valor |
|---|---|
| Font | **Poppins** (subset 400/600/700 — no cargar 100–900) |
| Azul marca | `#193A8A` / `#192A8A` |
| CTA primario | Naranja "Book Now" + **WhatsApp verde** |
| Módulos tour | Pricing, Included, Itinerary, What to Bring, Awards, Footer |
| Principio | **Menos menú, más decisión** — ver §6 UX |

---

## 3. Qué SÍ construir nuevo (diferenciadores)

| Hoy (WP/plantilla) | Greenfield |
|---|---|
| 30+ plugins, 7,5 MB payload | HTML estático + islands mínimos |
| Menú mega-confuso | Navegación 3 clics máx a WA |
| Blog sin CTA comercial | Bloque "Tours relacionados" + WA en cada post |
| Cart + WA compitiendo | **Un CTA:** WhatsApp con UTM + mensaje prefill |
| Schema parcial | JSON-LD completo por tipo de página |
| Sin conversión GA4 | `whatsapp_click` como evento clave día 1 |
| Mobile afterthought | **Mobile first** — 70%+ tráfico travel |
| GEO ignorado | FAQ schema, entidades claras, contenido citabile por IA |
| 4 sitios WP desconectados | Arquitectura preparada para i18n fase 2 |

---

## 4. Stack recomendado (magnitud PGT)

### Decisión: Next.js 15 + TypeScript + Tailwind

| Capa | Tecnología | Por qué |
|---|---|---|
| **Framework** | Next.js 15 App Router | POC probado, SSG/ISR, SEO, Vercel |
| **Lenguaje** | TypeScript | Catálogo tipado, menos roturas |
| **Estilos** | Tailwind + CSS variables (tokens Figma) | Velocidad diseño, CWV |
| **Contenido v1 (tarde)** | JSON/MDX generado por scripts desde WP | Ship hoy sin CMS |
| **Contenido v2 (semana 2+)** | Payload CMS 3.x + PostgreSQL | Admin para Lizet/Ricardo |
| **Imágenes** | `next/image` + CDN Vercel; URLs WP como fallback | No re-hostear 10k imgs día 1 |
| **Deploy** | Vercel | Ya funciona POC |
| **Analytics** | GTM container único + dataLayer events | No hardcodear 5 pixels |
| **Forms** | WA primario; Contact → ventas@ opcional | Alineado negocio |
| **i18n** | Preparar rutas; **solo EN en v1** | PT/ES/IT fase 2 mismo monorepo |
| **Redirects** | `next.config.js` redirects + CSV 301 masivo | Paridad SEO |
| **Search** | Opcional fase 2 | No bloquea MVP |

### No usar (para este proyecto)

- WordPress headless (sigue arrastrando Tourmaster)
- Drupal front (equipo ya migra backend — tu front es **alternativa**, no bloqueante)
- Admin 100% custom sin CMS
- SPA pura sin SSR/SSG
- shadcn por defecto sin personalizar (se ve genérico)

---

## 5. Arquitectura de información (URLs sagradas)

### Patrones obligatorios (paridad WP)

```
/                                    home
/tour/{slug}/                        69 tours
/blog/{slug}/                        452 blogs (canónica)
/blog/{category}/{slug}/             → 301 a /blog/{slug}/
/tour-category/{slug}/               6 categorías
/packages/                           hub ads + conversión
/machu-picchu-packages/              hub ads + conversión
/peru/{region}/...                   árbol destinos (~40 URLs)
/about-us/, /contact-us/, /faq/       corporativo
/travel-styles/{slug}/               taxonomía
/blogs/                              índice blog (existe en WP)
```

### Inventario URLs + keywords (31 ago — NUEVO)

**Carpeta:** `03-seo/datos/keywords-canibalizacion-2026-08-31/`  
**Insights:** `INSIGHTS.md` — blog = 63% tráfico, tours = 0,8%, 454 redirects, 54 grupos canibalización

| Activo | Valor |
|---|---|
| URLs totales | **596** (454 blog + 73 tour + 69 pages) |
| Redirects blog 301 | **454** en `redirects-blog-301.csv` |
| Canibalización | **54 grupos** / 104 URLs |
| Spam excluido | **24** URLs `/vip/` `/apps/` |

```
03-seo/datos/inventario-sitemap-2026-08-31/inventario-urls.csv  (589 filas)
03-seo/datos/keywords-canibalizacion-2026-08-31/  (keywords + GSC 16m + redirects)
03-seo/datos/inventario-sitemap-2026-08-31/blogs.txt
03-seo/datos/inventario-sitemap-2026-08-31/pages.txt
```

### Sitemap + robots

- `/sitemap.xml` index → tours, blogs, pages, hubs
- Generar estáticamente desde inventario CSV
- `robots.txt` → sitemap + disallow staging

---

## 6. UX — por qué las agencias confunden (y cómo no)

### Problemas del sitio actual (y plantillas competencia)

1. **Demasiadas opciones** — 69 tours sin jerarquía clara
2. **Dos CTAs** — Book / Cart / WA compiten
3. **Blog aislado** — lee, se va, no convierte
4. **Hubs débiles** — packages deberían ser landing de ads
5. **Lento en mobile** — 6,8s LCP = abandono antes del WA

### Principios diseño greenfield

| Principio | Implementación |
|---|---|
| **Un objetivo por página** | Tour = "preguntar por este tour"; Blog = "ver tours relacionados + WA" |
| **WA siempre visible** | Sticky bottom-right mobile; header desktop |
| **3 segundos a valor** | Hero: destino + precio desde + duración |
| **Confianza arriba** | Trustpilot, años operando, WhatsApp humano |
| **Sin laberinto** | Nav: Packages · Tours · Destinations · Blog · Contact |
| **Prefill WA inteligente** | `"Hi, I'm interested in [Tour Name] from perugrandtravel.com"` |
| **UTM en cada enlace WA** | `utm_source=web&utm_medium=whatsapp&utm_content={slug}` |

### Jerarquía de plantillas (solo 6)

1. `HomePage`
2. `HubPage` (packages, machu-picchu-packages, destination)
3. `TourPage` ← dinero
4. `BlogPostPage`
5. `BlogIndexPage`
6. `StaticPage` (about, contact, legal)

---

## 7. Embudo completo (SERP → lead)

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐    ┌──────────┐
│ 1. IMPRESIÓN│ →  │ 2. CLIC SERP │ →  │ 3. LANDING  │ →  │ 4. WA    │
│ title/meta  │    │ CTR snippet  │    │ CWV + CTA   │    │ clic     │
│ schema      │    │ posición     │    │ confianza   │    │          │
└─────────────┘    └──────────────┘    └─────────────┘    └──────────┘
     SEO/GEO              SEO               UX/Perf           Medición
```

| Etapa | Métrica | Objetivo greenfield |
|---|---|---|
| Impresión | GSC impressions | Mantener/subir (mismas URLs) |
| Clic SERP | CTR | Titles optimizados (Things MP template) |
| Landing | LCP < 2,5s | Lighthouse 95+ mobile |
| Engagement | Scroll a pricing/itinerary | Diseño Figma modular |
| Intención | `whatsapp_click` / sesión | >4% (hoy ~3,3% chat) |
| Negocio | Leads ventas | Cruzar con Sheet DAI/Paloma |

---

## 8. Modelo de contenido (TypeScript)

```typescript
// Tour — campos mínimos v1
interface Tour {
  slug: string;                    // URL path sin /tour/
  title: string;
  seo: { title: string; description: string; canonical: string };
  priceFrom: number;               // USD
  currency: 'USD';
  duration: string;                // "5D/4N"
  difficulty?: string;
  categories: string[];
  heroImage: string;
  gallery: string[];
  summary: string;
  itinerary: { day: number; title: string; body: string }[];
  included: string[];
  excluded: string[];
  faq?: { q: string; a: string }[];
  relatedTourSlugs?: string[];
}

// Blog
interface BlogPost {
  slug: string;
  title: string;
  seo: { title: string; description: string };
  publishedAt: string;
  body: string;                    // MDX o HTML sanitizado
  relatedTourSlugs: string[];    // obligatorio en rebuild
  category?: string;               // solo para breadcrumb, no URL
}

// Page (estática/hub)
interface Page {
  slug: string;
  title: string;
  seo: SeoFields;
  sections: Section[];           // bloques modulares
}
```

---

## 9. SEO + GEO checklist (cada URL)

### On-page (todas)

- [ ] `<title>` y meta description = WP actual (v1) o mejorado (v2)
- [ ] Canonical self-referencing
- [ ] Un solo H1
- [ ] `alt` en todas las imágenes LCP
- [ ] Internal links a hubs + tours relacionados
- [ ] Breadcrumb visible + `BreadcrumbList` JSON-LD

### Tours

- [ ] `TouristTrip` + `Product` + `Offer` JSON-LD
- [ ] Precio visible en HTML (no solo JS)
- [ ] FAQ schema si hay preguntas
- [ ] Open Graph + Twitter cards

### Blogs

- [ ] `Article` JSON-LD
- [ ] Bloque "Related tours" (mín. 3)
- [ ] CTA WA al final
- [ ] Fecha actualizada visible (GEO freshness)

### GEO (IA / citaciones)

- [ ] Respuestas directas en primer párrafo (definición clara)
- [ ] Listas y tablas donde aplique
- [ ] Entidades: Machu Picchu, Cusco, PGT como `TravelAgency`
- [ ] `sameAs` redes sociales en Organization schema
- [ ] Contenido factual verificable (precios, duraciones)

### Técnico

- [ ] Sitemap XML automático
- [ ] `hreflang` preparado (fase 2)
- [ ] 301 map para URLs duales blog
- [ ] Trailing slash consistente con WP
- [ ] Core Web Vitals green

---

## 10. Integraciones (día 1)

```tsx
// GTM en layout.tsx
<Script id="gtm" strategy="afterInteractive">{`
  (function(w,d,s,l,i){...})(window,document,'script','dataLayer','GTM-K8SZBJM5');
`}</Script>

// WA click — dataLayer
const onWhatsAppClick = (context: string) => {
  window.dataLayer?.push({
    event: 'whatsapp_click',
    page_path: pathname,
    content_type: 'tour' | 'blog' | 'hub',
    content_slug: slug,
  });
};
```

| Integración | Acción |
|---|---|
| GTM | Un container; eventos `whatsapp_click`, `page_view` |
| GA4 | Marcar `whatsapp_click` como conversión |
| Google Ads | Mantener URLs finales actuales |
| GSC | Verificar propiedad post-cutover |
| Meta Pixel | Si Lizet usa — vía GTM, no hardcode |
| RD Station | Evaluar si sigue activo; si sí, GTM |

---

## 11. Pipeline de contenido (WP → código)

### Scripts existentes

```bash
# Inventario URLs
bash 03-seo/scripts/export-wp-sitemap-inventory.sh

# Meta básica (HTML público)
python3 03-seo/scripts/export-wp-content.py --type tour --limit 69
python3 03-seo/scripts/export-wp-content.py --type blog --limit 452
```

### Scripts a crear (nuevo chat)

| Script | Output |
|---|---|
| `scrape-tour-full.py` | JSON por tour: itinerario, precio, galería, includes |
| `scrape-blog-full.py` | MDX/HTML + imágenes |
| `generate-redirects.ts` | `redirects.json` desde blogs duales CSV |
| `generate-sitemap.ts` | sitemap desde inventario |
| `validate-parity.sh` | diff title/meta WP vs nuevo sitio |

### Estrategia imágenes v1

- **Hotlink** desde `perugrandtravel.com/wp-content/uploads/...` con `next.config.js` `remotePatterns`
- v2: descargar a Vercel Blob / S3

---

## 12. Fases de entrega (realista)

### Fase 0 — Esta tarde (MVP demostrable)

**Meta:** Sitio navegable que **se siente** PGT nuevo, mide WA, 3 URLs reales.

| Entregable | Detalle |
|---|---|
| Repo | Fork/extend `pgt-poc` → `pgt-web` |
| Design system | Tokens Figma + componentes base |
| Páginas | Home, `/packages/`, 1 tour (Salkantay), 1 blog (Things MP) |
| Global | Header, footer, WA sticky, GTM |
| SEO | meta, JSON-LD, sitemap parcial |
| Perf | Lighthouse 95+ en tour |

### Fase 1 — Semana 1 (hubs + bloque SEO)

- `/machu-picchu-packages/`, `/contact-us/`, `/about-us/`
- 18 tours bloque Jairo + 10 blogs top GSC
- Redirects duales blog
- GA4 conversión configurada

### Fase 2 — Semana 2–4 (catálogo)

- 69 tours completos (script scrape)
- 452 blogs (batch; priorizar top 50 GSC primero)
- 62 páginas estáticas/hubs
- Payload CMS admin básico

### Fase 3 — Cutover

- Subdominio `beta.perugrandtravel.com` o reemplazo directo
- 301 solo si cambia algo (ideal: cero)
- Monitoreo GSC 30 días
- A/B WA copy si ventas coopera

**Política interna:** Drupal sigue en paralelo (Pista A). Greenfield = **Pista B** con datos, no guerra.

---

## 13. Decisiones que deben estar cerradas ANTES de codear

| # | Decisión | Recomendación | Estado |
|---|---|---|---|
| 1 | ¿Fork `pgt-poc` o repo nuevo? | **Repo nuevo `pgt-web`** (copiar patrones del POC) | ✅ 1 sep |
| 2 | ¿Subdominio staging? | **`beta.perugrandtravel.com`** para demo | ✅ 1 sep |
| 3 | ¿Trailing slash? | **Sí** (paridad WP) | ✅ |
| 4 | ¿Cambiar slugs? | **No** | ✅ |
| 5 | ¿Cart/checkout? | **Ocultar** — solo WA v1 | ✅ 1 sep |
| 6 | ¿Hotlink imágenes WP? | Sí v1 | ✅ |
| 7 | ¿Qué número WA? | +51 946 622 318 (ventas EN) | ✅ |
| 8 | ¿Payload cuándo? | Después MVP tarde | ✅ |
| 9 | ¿Drupal en paralelo? | **Sí** — no bloquear ni sabotear | ✅ 1 sep |
| 10 | ¿Quién edita contenido post-launch? | Lizet/Ricardo — Payload semana 2 | ⬜ |

---

## 14. Archivos clave del repo (leer en orden)

1. `08-investigacion/PROMPT-INICIO-CHAT-GREENFIELD.md` ← pegar en nuevo chat
2. `08-investigacion/GREENFIELD-PGT-PLAN-MAESTRO.md` ← este doc
3. `08-investigacion/FIGMA-LECTURA.md`
4. `08-investigacion/LIGHTHOUSE-COMPARATIVA.md`
5. `08-investigacion/ESQUEMA-MIGRACION-MAESTRO.md`
6. `03-seo/guias/MEDIR-LEADS-WEB-ACTUAL.md`
7. `03-seo/datos/inventario-sitemap-2026-08-31/`
8. `03-seo/datos/GSC-LINEA-BASE-2026-08-27.md`
9. `mi-carrera/CMS-CUSTOM-VIABILIDAD.md`
10. `08-investigacion/NORTE-IDEAL-ARQUITECTURA-Y-CRECIMIENTO.md`

---

## 15. Riesgos

| Riesgo | Mitigación |
|---|---|
| Perder rankings al cutover | Mismas URLs, 301 map, staging con noindex |
| Equipo ve como amenaza a Drupal | Subdominio demo; scorecard datos |
| 452 blogs manual | Scrape batch + priorizar top GSC |
| Sin CMS = Jairo es cuello de botella | Payload semana 2 |
| Imágenes rotas si WP cae | Descargar assets críticos semana 1 |
| Ventas no cierra leads | Proceso aparte; web optimiza intención |

---

## 16. Métricas de éxito (30 días post-beta)

| Métrica | Baseline | Target |
|---|---:|---:|
| Lighthouse mobile (tour) | 55 (WP) | **95+** |
| LCP | 6,8s | **<2,5s** |
| WA clics / sesión | 3,3% | **5%+** |
| CTR Things MP | 0,02% | **2%+** |
| Leads ventas EN | 2/mes | **8+/mes** (con ventas) |
| GSC clics | 643/28d | Mantener o subir |

---

*Última actualización: 1 sep 2026 tarde · dueño: Jairo*
