# Catálogo maestro de tours (EN)

> Actualizado: 2026-08-31  
> Snapshot CSV: `datos/catalogo-maestro-2026-08-31/catalogo-tours.csv`

---

## Resumen ejecutivo

| Dimensión | Valor | Fuente |
|-----------|-------|--------|
| **Tours publicados EN** | **69** | WP sitemap + `pgt-web/src/content/tours/` |
| **Categorías WP** | 6 | `03-seo/datos/inventario-sitemap-2026-08-31/tour-categories.txt` |
| **Estilos de viaje** | 5 | Sheet keywords (`Trekking`, `Traditional`, `Adrenaline`, `Combined Travel`, `Culture`) |
| **Hub principal** | 39 tours en `/packages/` | `packages.json` → `tourSlugs` |
| **Con precio en web** | ~55 | Scrape JSON-LD + tabla `#prices` |
| **Quote only** | 14 | Belmond, Amazon, eventos, algunos day tours |
| **Itinerario scrapeado** | ~65/69 | Sección `#itinerary` WP |
| **Includes/excludes** | Re-scrape 2026-08-31 | Scraper icon-list → **69/69 includes** |
| **Reseñas / rating** | **0 migradas** | Solo en WP widgets / TripAdvisor externo |

---

## Taxonomía (cómo se organizan)

### Categorías Tourmaster (6)

1. **Best Selling Packages in Peru** — paquetes multi-día Lima+Cusco+…  
2. **Tours in Peru** — circuitos nacionales  
3. **Tours in Machu Picchu** — paquetes MP-focused  
4. **Inca Trail Treks** — Camino Inca y variantes  
5. **Alternative Inca Trail Treks** — Salkantay, Lares, Choquequirao, Jungle  
6. **Day Tours in Cusco** — full day desde Cusco  

### Estilos de viaje (`travel-styles`)

| Estilo | Ejemplos |
|--------|----------|
| Trekking | Salkantay, Inca Trail, Lares |
| Traditional | Paquetes culturales 7–12D |
| Adrenaline | Jungle, rafting, ATV |
| Combined Travel | Lima + Cusco + Amazon |
| Culture | Day tours, Inti Raymi, weddings |

### Hubs web (conversión WA)

| Hub | Rol | % clics WA (baseline) |
|-----|-----|------------------------|
| `/packages/` | Catálogo general | ~28% |
| `/machu-picchu-packages/` | MP packages | ~18% |
| `/inca-trail-tours/` | Treks regulados | — |
| `/salkantay-treks/` | Alternativas | — |
| `/day-tours-in-cusco/` | Day trips | — |
| `/luxury-tours/` | Belmond / 5* | — |

---

## Campos por tour (esquema objetivo)

| Campo | pgt (verdad editorial) | pgt-web (runtime) | WP hoy | Drive / ventas |
|-------|--------------------------|-------------------|--------|----------------|
| slug, URL | Sheet + sitemap | JSON | ✓ | — |
| título, H1, SEO | Sheet | JSON | ✓ | — |
| categoría, tags, estilo | Sheet | **falta en JSON** | ✓ | — |
| precio USD desde | **OTAS sheet** + validación | `priceFrom` | JSON-LD | **OTAS reservas · Precios** |
| duración | Sheet plantilla | `duration` | título + widget | vendedores |
| dificultad | Ops | `difficulty` | parcial | vendedores |
| itinerario día a día | Ops / PDF | `itinerary[]` | ✓ HTML | PDFs ventas |
| incluye / no incluye | Ops | `included[]` / `excluded[]` | ✓ icon-list | contratos |
| opcionales | Ops | **falta campo** | ✓ WP | cotizaciones |
| qué llevar | Ops | **falta campo** | ✓ WP | — |
| hoteles por día | Ventas | **falta** | texto WP | Excel OTAs |
| reseñas, rating | TripAdvisor/GYG | **falta** | widgets | OTAs |
| diferenciador vs similar | **solo vendedores** | — | — | — |
| temporada / cupos Inca Trail | Ops | **falta** | parcial | calendario ventas |

---

## 14 tours “quote only” (precio no público o no scrapeado)

| Slug | Motivo probable |
|------|-----------------|
| `grand-deluxe-cusco-machu-picchu-by-belmond-5-days` | Luxury — cotización |
| `peru-grand-deluxe-by-belmond-andean-explorer-10-days` | Tren Belmond |
| `peru-grand-deluxe-lima-cusco-machu-picchu-7days` | Deluxe bundle |
| `peru-amazon-rainforest-9d` | Amazon seasonal |
| `amazon-rainforest-express-3d` | Amazon |
| `amazon-rainforest-4d` | Amazon |
| `cusco-corpus-christi` | Evento estacional |
| `holy-week-in-cusco` | Evento estacional |
| `condor-canyon-cusco-full-day` | Precio en tabla HTML |
| `sacred-valley-machu-picchu-2d` | Revisar WP |
| `inca-jungle-combined-7d` | Combo |
| `moche-route-chiclayo-and-trujillo-5d` | Norte Perú |
| `dome-piuray-lagoon` | Experiencia nicho |
| `cusco-rafting-and-zipline` | Actividad |

**Acción:** exportar **OTAS reservas · Precios de productos** (Drive) y cruzar con esta lista.

---

## Discrepancias conocidas

1. **Precio Salkantay:** WP $731 vs Drupal staging $590 — documentado en `03-seo/guias/MIGRACION-SEO-CAMPO-A-CAMPO.md`. Web scrape: **$731**.
2. **Sheet 73 filas vs sitemap 69 tours** — 4 filas extra (revisar duplicados o drafts).
3. **Categorías/tags en JSON web vacías** — existen en Sheet, no en scrape.
4. **Imágenes** — 100% hotlink WP; cutover requiere `npm run backup:images`.
5. **3 blogs extra** en web no en inventario sitemap (stubs débiles).

---

## Responsables sugeridos

| Tarea | Quién |
|-------|-------|
| Validar precios top 20 GSC | Lizet/Ops + Jairo |
| Export OTAS precios → CSV en `04-producto/datos/` | Jairo |
| Completar includes + optional en top 20 | Ops |
| Diferenciadores (“Salkantay vs 4D vs Classic 5D”) | Ventas → doc en `04-producto/fichas/` |
| Reseñas agregadas (TripAdvisor count) | Ops verifica # oficial |

---

## Próximo paso

1. Re-scrape tours: `npm run scrape:tours` (includes fix)  
2. Regenerar CSV: `python3 scripts/build-catalogo-maestro.py`  
3. Export Drive **OTAS precios** → `04-producto/datos/precios-otas-YYYY-MM-DD.csv`  
4. Crear `04-producto/fichas/{slug}.md` solo para top 20 GSC (no las 69)
