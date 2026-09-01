# Datos SEO — índice maestro

Carpeta central para **pgt** (estrategia) y **pgt-web** (build). Siempre preferir CSV/JSON aquí sobre re-leer Excel en Downloads.

## Datasets

| Carpeta | Fuente | Uso principal |
|---|---|---|
| [`keywords-canibalizacion-2026-08-31/`](keywords-canibalizacion-2026-08-31/) | Excel URLs/keywords/GSC 16m | Redirects 301, meta, priorización URLs |
| [`keyword-stats-2026-08-26/`](keyword-stats-2026-08-26/) | Google Ads Keyword Planner | Volumen búsqueda, alinear Ads + SEO |
| [`inventario-sitemap-2026-08-31/`](inventario-sitemap-2026-08-31/) | Sitemaps WP live | Lista URLs técnicas (589) |
| [`GSC-LINEA-BASE-2026-08-27.md`](GSC-LINEA-BASE-2026-08-27.md) | GSC 28 días | Tendencia reciente |

## Archivos críticos para pgt-web

```
keywords-canibalizacion-2026-08-31/redirects-blog-301.csv    # 454 redirects
keywords-canibalizacion-2026-08-31/blogs.csv                 # meta + GSC blogs
keywords-canibalizacion-2026-08-31/paginas.csv               # hubs + home
keywords-canibalizacion-2026-08-31/tours.csv                 # catálogo tours
keyword-stats-2026-08-26/keywords-google-ads.csv             # volumen Ads
```

## Leer primero (insights)

1. `keywords-canibalizacion-2026-08-31/INSIGHTS.md`
2. `keyword-stats-2026-08-26/INSIGHTS.md`

## Re-procesar Excel nuevo

```bash
python3 03-seo/scripts/analyze-excel-keywords.py RUTA.xlsx --out 03-seo/datos/NOMBRE-FECHA --type auto
```

Instalación: `03-seo/scripts/TOOLING-DATOS-SEO.md`
