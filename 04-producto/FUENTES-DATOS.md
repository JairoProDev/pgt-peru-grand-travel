# Fuentes de datos — tours, paquetes, destinos

> Mapa de dónde vive cada dato y qué falta exportar.

---

## Matriz de fuentes

| Fuente | Ubicación | Qué tiene | Acceso | En repo |
|--------|-----------|-----------|--------|---------|
| **Sheet keywords** | [PGT_URLs_keywords_canibalizacion_2](https://docs.google.com/spreadsheets/d/1VAaeEpG_hW8DOMbdqbidQhc2aNjhV8qDJQZ0nWcGMQU/edit) | 69+ tours: SEO, categoría, estilo, tags, GSC 16m | marketing@ | `03-seo/datos/keywords-canibalizacion-2026-08-31/tours.csv` |
| **WP live EN** | perugrandtravel.com | HTML tours, blogs, pages, precios, itinerarios | público | Scrape → `pgt-web/src/content/` |
| **pgt-web JSON** | GitHub pgt-web | Runtime SSG: 69+455+62 archivos | dev | Sí |
| **Drive marketing** | [Carpeta Drive](https://drive.google.com/drive/folders/1-1wEMq2qox3D0jrs4uY1XQz-3sqbTW9z) | Calendarios, keywords, OTAs, leads | marketing@ | Parcial — ver `02-empresa/DRIVE-INVENTARIO.md` |
| **OTAS · Precios productos** | Drive (Ventas) | Precios reales, márgenes, OTAs | Lizet/Ops | **NO exportado — P0** |
| **Informe palabras claves 2026** | Drive | Keywords anual | SEO | No |
| **Estudio intención búsqueda tours** | Drive | Competencia + intención | SEO | No |
| **GSC / GA4** | Google | Tráfico, consultas, WA users | Jairo | CSVs en `03-seo/datos/` |
| **TripAdvisor / GYG / Viator** | OTAs | Reseñas, rating, precio público | Ops | Solo menciones en IDENTIDAD |
| **Mente vendedores** | — | Diferencias entre tours similares, hoteles, upsells | WhatsApp | **No documentado — hueco crítico** |
| **RD Station** | Drive carpeta | Leads, embudo | Marketing | No |
| **Accesos PGT xlsx** | Drive local | Credenciales | Jairo | **Nunca al repo** |

---

## Qué debe vivir en `pgt/` (centro de trabajo)

| Tipo | Carpeta | Ejemplos |
|------|---------|----------|
| Inventarios y exports | `03-seo/datos/` | sitemap, keywords, GSC |
| Catálogo producto | `04-producto/` | este doc, CSV maestro, fichas top 20 |
| Esquemas migración | `08-investigacion/` | ESQUEMA-MIGRACION-MAESTRO |
| Identidad / NAP | `02-empresa/` | IDENTIDAD.md |
| Plantillas SEO/JSON-LD | `09-herramientas/` | plantillas-jsonld-turismo.md |
| Decisiones pendientes Drive | `02-empresa/DRIVE-INVENTARIO.md` | marcar export hecho |

## Qué debe vivir en `pgt-web/` (sitio)

| Tipo | Ubicura | Motivo |
|------|---------|--------|
| JSON tours/blogs/pages | `src/content/` | Build SSG, versionado, PR review |
| Redirects | `data/redirects.json` | next.config |
| FAQ hubs estables | `data/packages-faq.json` | Editable sin scrape |
| Scripts scrape/build | `scripts/` | Reproducible |
| Payload CMS (fase 2) | `cms/` + Postgres | Edición no-dev |

---

## Información inaccesible hoy (sin acción humana)

1. **Precios OTAS internos** — requiere export Drive  
2. **Diferenciadores comerciales** — entrevista 30 min ventas → fichas markdown  
3. **Reseñas agregadas** — API TripAdvisor o scrape manual + número oficial Ops  
4. **Carpeta Drive `Seo/` subcarpetas** — inventario incompleto (`DRIVE-INVENTARIO.md`)  
5. **Cupos Inca Trail por mes** — calendario ventas (¿Sheet? ¿Tourmaster admin?)  
6. **Hoteles asignados por categoría** (3* vs 4*) — cotizador interno  

---

## Acciones P0 (esta semana)

- [ ] Jairo: export **OTAS reservas · Precios de productos** → `04-producto/datos/precios-otas.csv`  
- [ ] Jairo: completar inventario carpeta **Seo/** en Drive  
- [ ] Ops: tabla “Salkantay 4D vs 5D vs Classic MP 5D” → `04-producto/fichas/comparativa-salkantay-machu-picchu.md`  
- [ ] Dev: re-scrape tours post-fix includes + merge categorías desde Sheet al JSON  

---

## Flujo recomendado

```
Drive/Sheet (precios, SEO meta)
        ↓ export CSV
     pgt/04-producto/  ← verdad editorial + gaps
        ↓ script merge / CMS import
     pgt-web/src/content/  ← build → Vercel
        ↓ post-cutover
     Payload CMS  ← edición Ops sin PR
```
