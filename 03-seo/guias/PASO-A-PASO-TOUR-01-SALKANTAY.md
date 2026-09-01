# Paso a paso — Tour #1 Salkantay 5D (piloto con cronómetro)

**Objetivo:** migración COMPLETA (body + tabs + precio + taxonomías + imágenes + SEO).  
**Drupal:** editar product existente #9 (no crear desde cero).  
**Tiempo meta 1er tour:** 55–70 min · **tours 2–3:** ~40 min · **tours 4+:** ~30 min.

---

## Antes de empezar — abre 3 pestañas

| # | URL | Para qué |
|---|---|---|
| A | https://www.perugrandtravel.com/tour/the-classic-salkantay-trek-5d/ | Copiar contenido visible |
| B | https://www.perugrandtravel.com/wp-admin/ → Tour → buscar "Salkantay SKY Trek 5 days" → Edit | Copiar HTML limpio (si tienes login) |
| C | http://147.135.114.64/admin/anymerce/products/9/edit | Drupal — formulario |

**Cronómetro:** pon uno en el móvil. Anota al final de cada fase.

---

## FASE 0 — Setup (⏱ 3 min)

- [ ] Pestaña C abierta en **Edit Salkantay Trek 5D/4N**
- [ ] Arriba del formulario: tab **Content** activa (azul)
- [ ] Sidebar derecho visible (Meta tags, URL alias, Save)
- [ ] `03-seo/datos/drupal-tour-seo-clipboard/TOURS-SEO-CLIPBOARD.md` abierto en otra ventana

**Anota hora inicio:** ___________

---

## FASE 1 — Recolectar contenido en WP (⏱ 8–12 min)

### Si tienes wp-admin (más rápido — 8 min)

1. Pestaña B → menú izquierdo **Tour** → All Tours
2. Busca **Salkantay SKY Trek 5 days** → **Edit**
3. En un Doc/Notepad temporal, copia sección por sección:
   - Título del tour
   - Texto intro / descripción corta (arriba del itinerario)
   - Cada tab: Overview, Itinerary, Included, Pricing, What to Bring
   - Precio "From" en USD
   - Trip details: Duration, Difficulty, Group size, Max altitude (si aparecen)
4. **Imágenes:** en la galería del tour WP, clic derecho → "Abrir imagen en pestaña nueva" → guarda 1 hero + 3–5 galería en `Descargas/salkantay/`

### Si NO tienes wp-admin (12 min)

1. Pestaña A → recorre cada tab del tour en el front
2. Selecciona texto de cada tab → Ctrl+C → pega en Notepad con etiqueta:
   ```
   === OVERVIEW ===
   (texto)
   === ITINERARY ===
   (texto)
   ...
   ```
3. Imágenes: clic derecho en hero y thumbs → Guardar imagen como

**⏱ Anota:** Fase 1 = _____ min

---

## FASE 2 — Tab Content: título + descripción (⏱ 5 min)

En Drupal pestaña C, tab **Content**:

### 2.1 Product title
- Borra `Salkantay Trek 5D/4N`
- Pega: **`Salkantay SKY Trek 5 days`** (igual que WP H1)

### 2.2 Description (editor debajo del título)
- Borra el texto placeholder actual
- Pega el **párrafo intro** de WP (2–4 oraciones que aparecen bajo el título en la ficha)
- Si no hay intro claro, usa la primera parte del tab Overview (máx. 2 párrafos)
- **Text format:** cambia a **Full HTML** si vas a pegar con formato

**⏱ Anota:** Fase 2 = _____ min

---

## FASE 3 — Tabs del tour (⏱ 20–25 min) ← la más larga

Scroll hasta la sección **Tabs**. Por cada sección de WP, repite:

### Tab 1 — Overview (⏱ 4 min)
1. Clic **Add Tour — tab to Tabs**
2. **Tab label:** `Overview`
3. **Tab content:** pega contenido Overview de WP
4. Si el formato se rompe: botón **Source** en el editor → pega HTML → volver a visual
5. **Text format:** Full HTML

### Tab 2 — Itinerary (⏱ 8 min)
1. **Add Tour — tab to Tabs**
2. **Tab label:** `Itinerary`
3. Pega Day 1, Day 2, Day 3, Day 4, Day 5 con sus títulos
4. Mantén `<h3>` o listas si puedes; si no, texto plano con "Day 1:", "Day 2:" en negrita

### Tab 3 — Included (⏱ 4 min)
1. **Tab label:** `Included`
2. Pega lista Included + Not included de WP (o dos subsecciones con H3)

### Tab 4 — Pricing (⏱ 5 min)
1. **Tab label:** `Pricing`
2. Pega tabla de precios WP (categorías hotel si las hay)
3. Si no hay tabla en WP, escribe:
   ```
   From US$ 699 per person.
   All prices in USD. Contact us for private tour rates.
   ```
   *(Confirma precio en WP antes de guardar)*

### Tab 5 — What to Bring (⏱ 3 min)
1. **Tab label:** `What to Bring`
2. Pega lista de equipaje WP

**⏱ Anota:** Fase 3 = _____ min

---

## FASE 4 — Price and sales (⏱ 3 min)

1. Clic tab **Price and sales** (arriba del formulario)
2. **Price:** `699` *(verifica en WP el "From" correcto)*
3. **Currency code:** `USD`
4. **Currency symbol:** `$`
5. **Price note:** `per person` o `From USD per person`
6. **Requires shipping:** desmarcado
7. **SKU:** `the-classic-salkantay-trek-5d` (opcional pero útil)

**⏱ Anota:** Fase 4 = _____ min

---

## FASE 5 — Classification and details (⏱ 5 min)

1. Clic tab **Classification and details**

### Taxonomías — marca estas casillas:
- [ ] **Peru**
- [ ] **Cusco**
- [ ] **Machu Picchu**
- [ ] **Trek** (carpeta)
  - [ ] **Salkantay**
- [ ] **Adventure**
- [ ] **Machu Picchu Tours** (si aplica en WP)

### Trip details (tabla Detail / Value)
Rellena filas vacías con datos de WP:

| Detail | Value (ejemplo — confirma en WP) |
|---|---|
| Duration | 5 days / 4 nights |
| Difficulty | Moderate |
| Group size | Small groups |
| Max altitude | 4,650 m / 15,255 ft |
| Best season | April – October |

**⏱ Anota:** Fase 5 = _____ min

---

## FASE 6 — Media and links (⏱ 10–15 min)

1. Clic tab **Media and links**

### Product images
1. **Add media** → **Upload** o **Library**
2. Sube hero + 3–5 fotos de `Descargas/salkantay/`
3. La **primera imagen** = hero (portada)
4. Ordena arrastrando si el CMS lo permite

### Map / Brochure
- Dejar vacío si WP no los tiene

**⏱ Anota:** Fase 6 = _____ min

---

## FASE 7 — SEO sidebar (⏱ 3 min)

Scroll sidebar derecho → expandir **Meta tags** → **Basic tags**

### Page title
Borra el token. Pega exacto:
```
5-Day Salkantay Sky Camp Trek to Machu Picchu
```

### Description
Borra el token. Pega exacto:
```
Hike the Salkantay Trek to Machu Picchu in 5 days with Sky Camp accommodation, breathtaking scenery, and unforgettable adventure experiences.
```

### Keywords (opcional)
```
salkantay trek 5 days
```

**⏱ Anota:** Fase 7 = _____ min

---

## FASE 8 — URL alias (⏱ 2 min)

Sidebar → expandir **URL alias**

1. **Desmarca** "Generate automatic URL alias"
2. En **URL alias** escribe manualmente:
   ```
   /tour/the-classic-salkantay-trek-5d
   ```
3. Si el campo sigue bloqueado → déjalo y anota en CSV `pendiente_alias` para Einel

**⏱ Anota:** Fase 8 = _____ min

---

## FASE 9 — Guardar + QA (⏱ 5 min)

1. Clic **Save** (abajo)
2. Clic **View** (barra negra arriba) o abre la URL del product
3. Checklist visual:

| ✓ | Qué verificar |
|---|---|
| [ ] | H1 = "Salkantay SKY Trek 5 days" |
| [ ] | Aparecen 5 tabs clicables |
| [ ] | Precio visible (From $699 o similar) |
| [ ] | Galería con imágenes |
| [ ] | Pestaña navegador = SEO title (no "Salkantay Trek 5D/4N \| Peru Grand Travel") |
| [ ] | URL contiene `the-classic-salkantay-trek-5d` o anotaste pendiente |
| [ ] | Teléfono / contacto visible en página |

4. En `jairo-migracion-maestro.csv` → fila Salkantay → `estado_drupal` = `hecho` o `seo_ok` + nota si alias pendiente

**⏱ Anota:** Fase 9 = _____ min

---

## RESUMEN CRONÓMETRO

| Fase | Min estimado | Tu tiempo real |
|---|---|---|
| 0 Setup | 3 | |
| 1 WP gather | 8–12 | |
| 2 Title + desc | 5 | |
| 3 Tabs (5) | 20–25 | |
| 4 Price | 3 | |
| 5 Classification | 5 | |
| 6 Media | 10–15 | |
| 7 SEO | 3 | |
| 8 URL alias | 2 | |
| 9 QA | 5 | |
| **TOTAL** | **64–78 min** | **_____ min** |

---

## Si te atascas

| Problema | Solución rápida |
|---|---|
| Formato feo al pegar | Editor → **Source** → pegar HTML → Full HTML |
| No encuentras tour en wp-admin | Menú **Tour** (no Posts) |
| Alias no deja editar | Anota en CSV, sigue con el resto |
| Imágenes pesadas | Comprime en squoosh.com antes de subir |
| Save da error | Revisa campos obligatorios con asterisco rojo |

---

## Después del #1

Tour #2 (Choquequirao) y #3 (Machu Picchu 2D) siguen el mismo orden.  
Copia este archivo, cambia slug y datos del clipboard.
