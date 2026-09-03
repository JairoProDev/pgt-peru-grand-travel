# Tracker Jairo — 3 tracks

**Hilación humana (cientos de ítems, append-only):** `mi-carrera/MAPA-TRABAJO-JAIRO.md` + checks `mi-carrera/TAREAS-VIVAS.md`.

**Fuente de verdad CSV / Sheet:** `TAREAS-MAESTRO.csv` en este folder.  
**Espejo:** pestaña **Jairo** en [Calendario Diario - Marketing](https://docs.google.com/spreadsheets/d/1XEeKQGmlTIYmpxJhGceMIgF_Vsn5fLp-kM5UpxXxEPc/edit?gid=10640812).

## Los 3 tracks (no mezclar)

| Track | Qué es | Épica |
|---|---|---|
| **`seo-operaciones`** | Pre-PGT + mes 1: auditorías, datos, guías, scripts repo `pgt`, equipo, informes, prod WP, aprendizaje | Sin épica — muchas tareas sueltas |
| **`drupal`** | **Una sola misión:** pegar tus 18 tours en Drupal staging | `EPIC-DRUPAL` + subtareas D-01…D-13 |
| **`codigo-web`** | **Una sola misión:** construir `pgt-web` (Next.js cutover EN) | `EPIC-WEB` + subtareas W-01…W-22 |

Drupal ≠ código web. El equipo migra a Drupal; tú además construiste el sitio Next.js en paralelo (experimento 4).

## Columnas

`id` · `epica_id` · `tipo` (epica|subtarea|tarea) · `track` · fechas · `dia_pgt` · `categoria` · `tarea` · `prioridad` · `estado` · `fecha_entrega` · `link` · `evidencia` · `metrica` · `notas`

## Rutina diaria

1. Actualiza `TAREAS-MAESTRO.csv` (o corre `build-csv.py` si reestructuras).
2. Sync Sheet: `uv run --with gspread --with google-auth python mi-carrera/tracker/sync-to-sheets.py`
3. Bitácora narrativa: `01-situacion/BITACORA.md`

## MCP Google en Cursor

Config: `.cursor/mcp.json` — debe usar `scripts/mcp/run-gdrive-mcp.sh` (carga OAuth de `pgt-web/.env.mcp`).

Si no aparecen en el chat: **Settings → MCP → Reload** (o reinicia Cursor). Los MCP solo se listan si el servidor arranca sin error.

Troubleshooting: `pgt-web/docs/GUIA-CONEXION-GOOGLE.md` § "Si algo se rompe".

## Resumen rápido (filtrar por Track en Sheet)

- **seo-operaciones** → ~59 tareas (pre-trabajo + operación)
- **drupal** → 1 épica + 13 subtareas (7 prep hechas, 0 tours migrados)
- **codigo-web** → 1 épica + 22 subtareas (~90% técnico hecho)
