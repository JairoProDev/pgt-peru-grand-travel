# Keywords, URLs y canibalización — PGT EN

**Fuente:** `PGT_URLs_keywords_canibalizacion_2 (2).xlsx` (actualizado ~31 ago 2026)  
**Copia en repo:** `PGT_URLs_keywords_canibalizacion_2026-08-31.xlsx`  
**Insights:** `INSIGHTS.md`  
**Uso:** `pgt/` (estrategia SEO) + `pgt-web/` (redirects, meta, priorización)

## Hojas exportadas → CSV

| Archivo | Filas | Contenido |
|---|---:|---|
| `tours.csv` | 73 | Tours + GSC 16m + keywords Rank Math |
| `blogs.csv` | 454 | Blogs + URL limpia + URL categoría + GSC |
| `paginas.csv` | 69 | Páginas/hubs/destinos + GSC |
| `canibalizacion.csv` | 54 grupos | URLs que compiten entre sí + acción |
| `redirects-blog-301.csv` | **454** | Mapa `from` (cat URL) → `to` (limpia) |
| `spam-urls.csv` | 24 | Inyección /vip/ /apps/ — excluir |
| `urls-sin-ficha.csv` | 40 | Indexadas sin post WP |
| `consultas-sitio-top1000.csv` | 1000 | Queries GSC sitio |
| `consultas-blog-top1000.csv` | 1000 | Queries GSC /blog/ |
| `resumen.txt` | — | Totales del Excel |
| `insights.json` | — | Top URLs machine-readable |

## Campos clave por tipo

### Tours (`tours.csv`)
`Título`, `URL`, `Slug`, `Keyword principal`, `Título SEO`, `Meta description`, `Clics`, `Impresiones`, `CTR`, `Posición`

### Blogs (`blogs.csv`)
`URL actual (limpia)`, `URL con categoría (antigua / indexada)`, `Keyword principal`, `Clics`, `Impresiones`, `CTR`, `Título SEO`

### Canibalización (`canibalizacion.csv`)
`#` (grupo), `Prioridad`, `URL actual`, `Acción sugerida` (CANÓNICA / 301)

## Para pgt-web

```bash
# Redirects masivos blog
cp redirects-blog-301.csv ../../../pgt-web/data/   # cuando exista

# Meta por URL
# tours.csv + blogs.csv + paginas.csv → content/*.json en build
```

## Fuentes cruzadas en el Excel

- WordPress export 24-08-2026
- GSC sitio completo 25-08-2026 (tours, páginas) — 16 meses
- GSC /blog/ 24-08-2026 — 16 meses (más profundo en cola larga)
