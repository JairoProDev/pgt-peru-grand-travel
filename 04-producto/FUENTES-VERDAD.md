# Fuentes de verdad — producto & precios PGT

Actualizado: 2026-09-01

## Resumen ejecutivo

| Dato | Fuente canónica | Copia en repo | Vista web |
|------|-----------------|---------------|-----------|
| **Inventario SEO (73 fichas)** | Sheet `PGT_URLs_keywords_canibalizacion` | `pgt/03-seo/datos/.../tours.csv` | — |
| **Contenido público tours** | `pgt-web/src/content/tours/*.json` | Git | `/tour/{slug}/` |
| **Precios ventas 2026** | Drive **atendimento@** → `TARIFARIO GENERAL 2026 PGT` / `OTAS reservas · Precios de productos` | Export CSV → `pgt/04-producto/datos/precios-otas/` | Tras `npm run precios:apply` |
| **Paquetes modelo (Slides)** | Drive `PAQUETES MODELO 2026 - COTI`, `Unbranded 2026` | No descargar todo — export bajo demanda | Hubs + tours (copy manual o futuro CMS) |
| **Catálogo cruzado** | Script merge | `pgt/04-producto/datos/catalogo-maestro-*/` + `pgt-web/data/` | `/catalog/` (noindex, interno) |

**No clonar Drive completo al repo.** Es ineficiente, se desactualiza en días y mezcla PII/contratos. El flujo óptimo es **export periódico CSV/JSON de las hojas clave** + scripts de merge.

---

## Cuentas Google Drive

### marketing@perugrandtravel.com
- SEO, ads, calendarios, keywords, backlinks.
- Inventario: `02-empresa/DRIVE-INVENTARIO.md`
- Sheet útil: `OTAS reservas · Precios de productos` (copia o espejo de ventas)

### atendimento@perugrandtravel.com (ventas)
- **Fuente operativa** de tours, tarifarios y decks comerciales.
- Carpetas vistas en "Compartidos conmigo" (sep 2026):

| Carpeta | Uso |
|---------|-----|
| `TARIFARIO GENERAL 2026 PGT` | Precios públicos / cotización |
| `TARIFARIO NETOS - HOTELES` | Costos hoteleros |
| `TARIFAS RESTAURANTE` / `TRANSPORTES` / `PROVEDORES` | Costeo interno |
| `PAQUETES MODELO 2026 - COTI` | Plantillas cotización |
| `Unbranded 2026` | Decks sin marca (B2B) |
| `PROGRAMAS` | Itinerarios por producto |
| `AGENCIAS` | Material agencias |
| Decks `Peru Private Escape`, `Peru Private Circle` | Luxury / private |

**Acceso desde consola/terminal:** no hay API configurada en el repo. Opciones:
1. **Manual (recomendado ahora):** Descargar CSV desde Sheets → carpeta `precios-otas/`
2. **rclone / Google Drive API:** solo si se automatiza semanalmente (service account + carpeta compartida)
3. **No** scrapear Slides/Docs — el contenido no es estable para CI

---

## Pipeline de precios (cuando hay export Drive)

```bash
cd pgt-web

# 1. Snapshot precios actuales web (baseline)
npm run precios:snapshot

# 2. Colocar export en:
#    ../pgt/04-producto/datos/precios-otas/precios-otas-YYYY-MM-DD.csv

# 3. Merge con catálogo + snapshot
python3 scripts/merge-precios-otas.py ../pgt/04-producto/datos/precios-otas/precios-otas-YYYY-MM-DD.csv

# 4. Aplicar a JSON (solo filas validado_ops=yes)
npm run precios:apply

# 5. Rebuild catálogo + sitio
npm run catalog:build
npm run build
```

Mientras no hay export OTAS: los precios en web vienen del **scrape WP/JSON-LD** (`precios-web-snapshot-latest.csv`), no del tarifario 2026 de ventas.

---

## Pipeline catálogo maestro

```bash
cd pgt-web && npm run catalog:build
```

Genera:
- `pgt/04-producto/datos/catalogo-maestro-2026-08-31/catalogo-tours.csv`
- `pgt-web/data/catalogo-tours.{csv,json}`

Vista interna: `https://pgt-web-theta.vercel.app/catalog/` (robots: noindex)

---

## ¿Tenemos paquetes 2026 reales con precios actualizados?

| Qué | Estado hoy |
|-----|------------|
| Listado 73 productos SEO | ✅ Catálogo maestro |
| Páginas tour en web | ✅ ~70 live JSON |
| Precios alineados a tarifario ventas 2026 | ❌ **Pendiente export Drive** |
| Decks Slides por paquete | ❌ Solo en Drive (no en web) |
| Hubs 2026 (copy SEO) | ✅ Títulos/grid actualizados |

**Próximo paso humano (5 min):** desde atendimento@, abrir `OTAS reservas` o `TARIFARIO GENERAL 2026`, exportar CSV, guardar en `precios-otas/`, avisar para correr merge + apply.

---

## SEO técnico (pgt-web)

| Recurso | Ruta | Estado |
|---------|------|--------|
| Sitemap | `/sitemap.xml` | ✅ |
| Robots | `/robots.txt` | ✅ (noindex en beta) |
| llms.txt | `/llms.txt` | ✅ |
| JSON-LD org + rating | Solo home | ✅ (footer sin rating) |
| FAQ schema | Hubs principales | ✅ |
| 404 útil | `not-found.tsx` | ✅ |

Ver también: `pgt-web/docs/INTEGRACIONES.md` (MCP + APIs GA4/GSC/Drive).
