# Esquema maestro — migración WP → Drupal (perugrandtravel.com EN)

**Dueño documentación:** Jairo · **Actualizado:** 1 sep 2026  
**Plan acordado:** migrar **~69 tours + ~452 blogs** tal cual (sin optimizar); optimización después.  
**Regla SEO #1:** mantener **URLs indexadas** (misma path o 301 directo).

---

## 1. Inventario real (sitemap WP live)

| Tipo | Cantidad | Sitemap | Prefijo URL |
|---|---:|---|---|
| **Tours** | **69** | `tour-sitemap.xml` | `/tour/{slug}/` |
| **Blogs** | **452** | `blog/post-sitemap.xml` | `/blog/{slug}/` o `/blog/{cat}/{slug}/` |
| **Páginas** | **~60+** | `page-sitemap.xml` | varios (ver §4) |
| **Categorías tour** | 6 | `tour_category-sitemap.xml` | `/tour-category/...` |
| **Travel styles** | (sitemap propio) | `travel-styles-sitemap.xml` | `/travel-styles/...` |

Tu bloque asignado (Sheet): **18 tours + 115 blogs** — subconjunto del total EN.

---

## 2. Arquitectura del sitio (capas)

```
┌─────────────────────────────────────────────────────────────┐
│  HEADER (global) — menú, idioma, teléfono, CTA Book Now     │
├─────────────────────────────────────────────────────────────┤
│  SECCIONES ESTÁTICAS — home, about, contact, legal, hubs    │
├─────────────────────────────────────────────────────────────┤
│  DESTINATIONS (nuevo/ampliado Drupal) — árbol geográfico    │
├─────────────────────────────────────────────────────────────┤
│  TOURS (Tourmaster → Commerce Product Drupal) — 69 URLs     │
├─────────────────────────────────────────────────────────────┤
│  BLOG (WP /blog → Drupal blog) — 452 URLs                   │
├─────────────────────────────────────────────────────────────┤
│  FOOTER — enlaces, pagos, redes, legal                       │
└─────────────────────────────────────────────────────────────┘
```

**Dos WordPress hoy:**

| Instalación | URL admin | Contenido |
|---|---|---|
| Sitio principal | `/wp-admin/` | Tours, pages, destinations |
| Blog | `/blog/wp-admin/` | Posts (452) |

---

## 3. Esquema TOUR (WP Tourmaster → Drupal)

### 3.1 Campos confirmados (Sheet + auditorías)

| Campo | WP / Tourmaster | Drupal staging (Einer) | Obligatorio migración |
|---|---|---|---|
| Título | `post_title` | Product title | ✅ |
| URL slug | `/tour/{slug}/` | Pathauto → **debe ser igual** | ✅ |
| Precio | Tourmaster meta | Commerce price | ✅ |
| Moneda | USD | USD | ✅ |
| Duración | ej. 5D/4N | field duration | ✅ |
| Dificultad | Moderate/Strenuous | field difficulty | ✅ |
| Categoría tour | Taxonomy `tour_category` | taxonomy dest/cat | ✅ |
| Estilo viaje | `travel-styles` | taxonomy | 🟡 |
| Etiquetas | tags | tags | 🟡 |
| Descripción corta | excerpt / TM | body summary | ✅ |
| Itinerario día a día | Tourmaster blocks | paragraphs | ✅ |
| Incluye / No incluye | TM lists | fields | ✅ |
| Galería imágenes | TM gallery + featured | Media | ✅ |
| SEO Title | Yoast (tours main WP) | Metatag title | ✅ |
| Meta description | Yoast | Metatag description | ✅ |
| Canonical | Yoast | Metatag canonical | ✅ |
| Schema Product/Offer | Yoast + TM | Schema.org module | ✅ |
| WhatsApp CTA | Plugin click-to-chat | **Bloque WA** | ✅ negocio |
| Reseñas / rating | Trustindex widget | reimplementar | 🟡 |
| Mapa / ubicación | TM optional | optional | 🟡 |

### 3.2 Taxonomías tour (WP live)

| Taxonomía | Ejemplos | URLs |
|---|---|---|
| **Categoría de tour** | Alternative Inca Trail Treks, Day Tours in Cusco, Tours in Machu Picchu, Tours in Peru, Inca Trail Treks | `/tour-category/...` |
| **Estilo de viaje** | Trekking, Traditional, Adrenaline, Combined Travel, Culture | `/travel-styles/...` |
| **Etiquetas** | Machu Picchu Tours, Cusco, Salkantay Treks, Offers, Luxury Peru Tours, Inca Trail | (no URL propia) |

### 3.3 CSV export tour (columnas objetivo)

Ver plantilla: `03-seo/datos/plantilla-export-tour.csv`

---

## 4. Esquema BLOG (WP Rank Math → Drupal)

### 4.1 Campos confirmados (Sheet blogs jairo)

| Campo | WP | Notas |
|---|---|---|
| Título | post_title | = H1 |
| **URL limpia (canónica)** | `/blog/{slug}/` | **Esta es la que Google debe conservar** |
| URL con categoría | `/blog/{cat}/{slug}/` | 115/115 blogs tienen alternativa — **301 → limpia** |
| Slug | post_name | no cambiar |
| Categoría principal | Rank Math / WP cat | Cusco (70), Perú (27), Lima (6)… |
| Todas las categorías | tags CSV | cusco, peru, lima, puno, ica… |
| Keyword principal | Rank Math | focus keyword |
| Keywords secundarias | Rank Math | |
| SEO Title | Rank Math | ≠ título post a veces |
| Meta description | Rank Math | |
| SEO score | Rank Math | referencia only |
| Contenido | post_content | HTML Gutenberg |
| Imagen destacada | featured_media | |
| Palabras | conteo | |
| Publicado / Modificado | dates | |
| Autor | post_author | |
| Enlaces internos | en body | tours, otros blogs |
| Schema Article | Rank Math | |
| WhatsApp | plugin global | |

### 4.2 Categorías blog (bloque Jairo)

| Categoría | Posts |
|---|---:|
| Cusco | 70 |
| Perú | 27 |
| Lima | 6 |
| Puno | 4 |
| Ica | 3 |
| Luxury | 2 |
| Amazonia | 2 |
| Nazca | 1 |

Tags frecuentes: `cusco`, `peru`, `lima`, `puno`, `ica`, `amazonia`, `salkantay`…

### 4.3 Problema crítico URLs blog

```
URL limpia:     /blog/things-to-do-in-machu-picchu/          ← MANTENER
URL categoría:  /blog/cusco/things-to-do-in-machu-picchu/   ← 301 a limpia
```

**115/115** blogs del bloque Jairo tienen **dos URLs**. En migración Drupal: **una sola canónica** + redirect de la otra.

---

## 5. Tipos de URL del sitio (mapa completo)

| tipo | patrón ejemplo | ¿Migrar fase 1? | Prioridad SEO |
|---|---|---|---|
| `home` | `/` | ✅ | P0 |
| `tour` | `/tour/salkantay-trek-4-days/` | ✅ | P0 |
| `blog` | `/blog/{slug}/` | ✅ | P0 |
| `blog_cat_dup` | `/blog/cusco/{slug}/` | 301 → limpia | P0 |
| `page_about` | `/about-us/` | ✅ | P1 |
| `page_contact` | `/contact-us/` | ✅ | P1 |
| `page_legal` | `/privacy-policy...` | ✅ | P2 |
| `destination_hub` | `/peru/cusco/` | ✅ ampliar | P1 |
| `destination_leaf` | `/peru/lima/museums/...` | ✅ | P1–P2 |
| `tour_category` | `/tour-category/inca-trail-treks/` | ✅ | P1 |
| `package_hub` | `/machu-picchu-packages/` | ✅ | P1 |
| `payments` | `/payments/` | ✅ | P1 ads |
| `blog_index` | `/blogs/` o `/blog/` | ✅ | P1 |
| `offers` | `/offers/` | 🟡 | P2 |
| `social` | `/social-projects/` | 🟡 | P3 |

Lista páginas live: correr `03-seo/scripts/export-wp-sitemap-inventory.sh`

---

## 6. HEADER / menú (WP vs Drupal staging)

### Drupal staging ([147.135.114.64](http://147.135.114.64/)) — referencia Figma

| Elemento | Contenido |
|---|---|
| Top bar | Phone +1 786…, email, 24/7 Support |
| Logo | Peru Grand Travel |
| Menú principal | Destinations ▾ (Peru, Cusco, Lima, Machu Picchu), Home, Packages, Tailor Made, Trek, Experiences ▾, Luxury, About, Blog |
| Idioma | EN / PT-BR / ES (fase 1 solo EN live) |
| CTA | Book Now |
| Footer | Contact, Company links, Packages, Payments icons, redes |

**Migración header:** no es “contenido migrable” — es **bloques Drupal** (Block Content). Einer ya los tiene. Tú validas enlaces rotos post-cutover.

---

## 7. ¿Export WP → import Drupal automático?

### Respuesta honesta

| Contenido | ¿Export/import automático? | Herramienta |
|---|---|---|
| **Blogs (452)** | 🟢 **Sí, parcial–alto** | Drupal Migrate + WP REST API o XML export |
| **Tours (69)** | 🟡 **Parcial** | Tourmaster ≠ estándar — mapping custom |
| **Páginas (~60)** | 🟡 Parcial | Migrate pages + manual layout |
| **Media/imágenes** | 🟡 Parcial | Migrate files + carpeta assets Einer |
| **SEO meta** | 🟡 Parcial | wp_postmeta → Metatag (script) |
| **Menús/header** | 🔴 Manual | Bloques Drupal |
| **Redirects 301** | 🟢 Automatizable | CSV → Redirect module |

**No existe** “un clic” perfecto Tourmaster → Drupal Commerce.  
**Sí existe** pipeline que tú puedes construir:

```
FASE 1 — Inventario (automático)
  sitemap XML → CSV maestro URLs

FASE 2 — Extracción (semi-auto)
  WP REST API / export DB / plugin WP All Export
  → JSON/CSV por tour y blog

FASE 3 — Transform (código — TU APORTE)
  Python: normalizar URLs, canónicas, meta, precios
  → CSV import-ready para Drupal Migrate

FASE 4 — Import (Einer/Ricardo)
  Drupal Migrate / Feeds / manual primera tanda

FASE 5 — QA (automático)
  check-urls.sh + compare-meta + GSC
```

---

## 8. Qué construir en código (Jairo)

| Herramienta | Estado | Prioridad |
|---|---|---|
| `export-wp-sitemap-inventory.sh` | ✅ repo | Hoy |
| `check-urls.sh` | ✅ repo | Hoy |
| `export-wp-content.py` | pendiente | Semana 1 |
| GSC → Sheet sync | pendiente | Semana 2 |
| `compare-meta.sh` WP vs Drupal | pendiente | Semana 1 |

Pedir a Ricardo/Einer: **REST API auth** o **dump SQL read-only** o **WP All Export** — acelera 10×.

---

## 9. Plan “copiar tal cual” (sin optimizar)

### Sí — con 4 condiciones no negociables

1. **Misma URL** (path) que WP canónico  
2. **Mismo title + meta** (copiar de Yoast/Rank Math)  
3. **301** de URLs alternativas (blog con categoría, `/product/N`)  
4. **WhatsApp** visible en tours (no solo cart)

### Orden migración recomendado

```
1. Tours (69) — catálogo + conversión
2. Blogs (452) — tráfico SEO
3. Páginas hub (destinations, packages)
4. Páginas leaf (Lima museums, etc.)
5. Legal / secundarias
```

Optimización (Things MP, Museums MP, Lighthouse) → **después** del parity check.

---

## 10. Sheet maestro — columnas

Usar en Google Sheet compartido con los 4 del cuarteto:

```
tipo | url_wp_canonica | url_alternativa_301 | titulo | seo_title | meta_desc | 
slug | categorias | tags | precio_usd | duracion | dificultad |
drupal_nid | url_drupal | status_migracion | qa_checklist | clics_28d | imp_28d | responsable | notas
```

---

## 11. Cómo liderar la migración (sin ser admin Drupal)

| Rol tuyo | Entregable |
|---|---|
| **Arquitecto datos** | Este doc + plantillas CSV |
| **Dueño URLs** | Mapa 301 + reglas canónicas |
| **QA automatizado** | Scripts + scorecard 4 personas |
| **Especificación SEO** | Things MP como plantilla blog |
| **Informe Clever** | Riesgos + % migrado + GSC |

Einer/Ricardo **implementan** en Drupal. Tú **defines qué debe salir** y **verificas** que no rompió Google.

---

*Relacionado:* `MIGRACION-WP-DRUPAL-PLAYBOOK.md` · `MIGRACION-SEO-CAMPO-A-CAMPO.md` · `MIGRACION-AUTOMATIZACION.md`
