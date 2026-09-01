# Mapa completo — formulario Product (tour) en Drupal PGT

**Staging:** http://147.135.114.64/  
**Admin products:** http://147.135.114.64/admin/anymerce/products  
**Crear tour:** http://147.135.114.64/admin/anymerce/products/add/default  
**Capturas:** `03-seo/datos/drupal-capturas-2026-09-01/`  
**Actualizado:** 1 sep 2026

---

## 1. Qué es un "Product" en PGT Drupal

| WP (hoy) | Drupal (staging) |
|---|---|
| CPT `tour` (Tourmaster) | **Product** (módulo `anymerce`) |
| URL `/tour/{slug}/` | Pathauto → objetivo `/tour/{slug}/` (hoy muchos en `/product/N`) |
| Yoast SEO title/meta | **Metatag** en sidebar derecho |
| Itinerario en tabs WP | **Tabs** (paragraphs) en tab Content |
| Precio en Tourmaster | **Price and sales** tab |
| Categorías tour | **Classification and details** (taxonomías) |

**Estado equipo (1 sep):** 26 products en staging. Ninguno de tus 18 tours del bloque Jairo aparece con slug WP exacto aún.

---

## 2. Navegación admin (memoriza)

```
Login → Content (menú arriba)
         └─ tab Products  →  lista tours
         └─ Add product   →  formulario 4 tabs

Atajos:
  /admin/anymerce/products          ← lista products (USAR ESTE)
  /admin/content → tab Products     ← mismo lugar
  /admin/content/media              ← biblioteca imágenes
  /admin/content/block              ← bloques globales (WA, footer, hero)
```

**No usar:** `/admin/commerce/products` → 404

---

## 3. Las 4 tabs del formulario Product

### Tab 1 — Content (contenido principal)

| Campo Drupal | Qué pegar desde WP | Quién | Notas |
|---|---|---|---|
| **Product title** | Título del tour WP | Equipo / tú | H1 visible |
| **Description** | Resumen corto / excerpt | Equipo | Aparece en cards |
| **Tabs** (repetible) | Itinerario, Included, Pricing, What to bring | Equipo | Cada tab = label + body HTML |
| Tab labels típicos | Overview · Itinerary · Included · Pricing · What to Bring | — | Igual que Figma |

**Tabs — estructura:**
- `Tab label` (texto) → ej. "Itinerary"
- `Tab content` (CKEditor Full HTML) → copiar HTML de WP
- Botón **Add Tour — tab to Tabs** para cada sección

**Tu rol SEO aquí:** revisar que el H1 del title no duplique keyword stuffing; no reescribir body salvo optimización acordada.

---

### Tab 2 — Price and sales

| Campo | WP equivalente | Notas |
|---|---|---|
| **Price** | Precio "from" USD | Un precio base; tabla multi-hotel va en tab Pricing |
| **Compare-at price** | Precio tachado (si hay) | Opcional |
| **Currency code** | USD | Siempre USD en EN |
| **SKU** | ID interno | Puede quedar vacío o slug |
| **Stores** | — | Dejar default |
| **Inventory policy** | — | Tours = no inventario real |
| **Requires shipping** | No | Desmarcar si aplica |
| **Price note** | Texto bajo precio | ej. "per person" |

---

### Tab 3 — Classification and details

| Campo | WP equivalente | SEO |
|---|---|---|
| **Taxonomías destino** | Categoría tour | Peru > Cusco > Machu Picchu… |
| **Trek / Packages / Day Tours** | Etiquetas WP | Arquitectura interna |
| **Best Seller / Featured / New** | Flags WP | Conversión, no SEO directo |
| **Rating / Reviews count** | TripAdvisor widget | Schema futuro |
| **Trip details** (Detail + Value) | Duración, dificultad, grupo | GEO / snippets |

Taxonomías visibles en staging: Peru, Cusco, Machu Picchu, Salkantay, Choquequirao, Inca Trail, Packages, Trek, Adventure, Luxury, Day Tours, etc.

---

### Tab 4 — Media and links

| Campo | WP equivalente |
|---|---|
| **Product images** | Galería hero + thumbs |
| **Map** (URL + link text) | Embed mapa si hay |
| **Brochure** | PDF descargable |

Subir vía **Add media** o reutilizar de `/admin/content/media`.

---

## 4. Sidebar derecho (SIEMPRE revisar antes de Save)

### Meta tags ← **TU CAMPO PRINCIPAL**

Expandir **Meta tags → Basic tags**:

| Campo Metatag | Valor para migración | De dónde (CSV) |
|---|---|---|
| **Page title** | Reemplazar token por texto literal | `seo_title` en `jairo-migracion-maestro.csv` |
| **Description** | Reemplazar token por meta literal | columna `meta` |
| **Keywords** | Opcional (Google ignora) | `keyword` |
| **Canonical URL** | Dejar `[anymerce_product:url]` hasta que alias sea `/tour/slug/` | — |

**Default actual (NO dejar en producción):**
```
Page title:    [anymerce_product:title] | [site:name]
Description:   [anymerce_product:field_anymerce_description]
Canonical:     [anymerce_product:url]
```

**Para SEO real:** sobrescribir Page title y Description con los valores WP optimizados.

### URL alias

| Control | Acción |
|---|---|
| **Generate automatic URL alias** | Dejar ✓ si Pathauto configurado |
| **URL alias** | Debe quedar `/tour/{slug}/` — si sale `/product/9`, anotar en CSV → Einel |

### Sale settings

- **Active product** ✓ = publicado

### Authoring information

- Fecha autoría — no crítico para SEO

---

## 5. Flujo migración tour — 15 min (solo SEO, tú)

Para cada tour de `jairo-migracion-maestro.csv`:

1. Abre WP: `perugrandtravel.com/tour/{slug}/`
2. Busca en Drupal: http://147.135.114.64/admin/anymerce/products → filter por título
3. Si no existe → equipo crea; tú esperas o creas shell y ellos llenan body
4. **Edit** → sidebar **Meta tags**:
   - Page title = `seo_title` del CSV
   - Description = `meta` del CSV
5. **URL alias** → verificar `/tour/{slug}/`
6. **View** (preview) → 200 OK, title correcto en pestaña
7. CSV → `estado_drupal` = `seo_ok` o `pendiente_alias`

---

## 6. Primer tour piloto — Salkantay 5D

| | |
|---|---|
| **Slug WP** | `the-classic-salkantay-trek-5d` |
| **WP** | https://www.perugrandtravel.com/tour/the-classic-salkantay-trek-5d/ |
| **SEO Title** | 5-Day Salkantay Sky Camp Trek to Machu Picchu |
| **Meta** | Hike the Salkantay Trek to Machu Picchu in 5 days with Sky Camp accommodation, breathtaking scenery, and unforgettable adventure experiences. |
| **Drupal similar** | "Salkantay Trek 5D/4N" (product #9) — **no es el mismo slug** |

**Acción:** o editas product #9 y corriges alias, o creas product nuevo con slug correcto. Pregunta a Einel cuál es el plan.

---

## 7. Qué NO tocar

- Bloques globales (`/admin/content/block`) — Footer, Header CTA, Payment methods
- Structure / Taxonomy — solo marcar categorías, no crear términos nuevos
- Theme / Twig — Einel
- Pathauto patterns globales — Einel
- Módulos / updates

---

## 8. Automatización disponible

```bash
# Pack sprint con fichas por URL
python3 03-seo/scripts/generate-drupal-sprint-pack.py

# Hoja copy-paste SEO por tour (nuevo)
python3 03-seo/scripts/generate-tour-seo-clipboard.py

# Validar URLs WP responden 200
bash 03-seo/scripts/check-urls.sh
```

---

## 9. Preguntas para Einel (WhatsApp)

1. ¿Pathauto `/tour/[product:field_slug]/` ya está o seguimos en `/product/N`?
2. ¿Edito products existentes o creo nuevos por slug WP?
3. ¿Cuándo activan botón WhatsApp en ficha tour?
4. ¿Hay import CSV o solo manual esta semana?

---

Siguiente: `13-INDICE-CAPTURAS-DRUPAL.md` · Guía operativa: `03-seo/guias/DRUPAL-SPRINT-JAIRO-HOY.md`
