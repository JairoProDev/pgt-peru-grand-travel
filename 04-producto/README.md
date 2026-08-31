# Producto PGT — catálogo y datos

Centro de verdad **humana + analítica** para tours, paquetes, destinos y precios. La web (`pgt-web`) consume datos; este repo define qué debe existir y de dónde sale.

| Documento | Para qué |
|-----------|----------|
| [CATALOGO-MAESTRO.md](./CATALOGO-MAESTRO.md) | 73 fichas Sheet, 69 sitemap, taxonomías, gaps |
| [FUENTES-DATOS.md](./FUENTES-DATOS.md) | Matriz Drive / Sheet / WP / web / mente vendedores |
| [RECONCILIACION-INVENTARIO.md](./RECONCILIACION-INVENTARIO.md) | **73 tours / 454 blogs** — Sheet vs sitemap vs web |
| [REPO-VS-CMS.md](./REPO-VS-CMS.md) | Qué vive en git vs Payload vs Drive |
| [datos/catalogo-maestro-2026-08-31/](./datos/catalogo-maestro-2026-08-31/) | CSV exportado (regenerar con script) |

## Regenerar catálogo

Desde `pgt-web`:

```bash
python3 scripts/build-catalogo-maestro.py
# Opcional: re-scrape tours antes
npm run scrape:tours
```

## Norte

Un viajero debe poder comparar tours (duración, precio, incluye/no incluye, estilo) **sin preguntar al vendedor** — y aun así escribir por WhatsApp con confianza.
