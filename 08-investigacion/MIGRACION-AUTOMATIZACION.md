# Automatización migración — qué sí, qué no

**Para:** Einer, Ricardo, cuarteto SEO  
**Dueño propuesta:** Jairo

---

## Resumen

| Capa | % esfuerzo | Automatizable |
|---|---:|---|
| Contenido + assets primera vez | 60–70% | 🔴 Manual |
| SEO fields (title, meta, URL) | 15% | 🟡 CSV / copy spec |
| QA post-migración | 10% | 🟢 Scripts |
| Medición + alertas | 5% | 🟢 GSC/GA4 |
| Redirects 301 | 10% | 🟡 CSV → Redirect module |

---

## Flujo recomendado por URL

```
1. SPEC (Jairo)     → title, meta, URL, H1 desde WP o Things MP template
2. MIGRATE (human)  → Drupal + assets carpeta Einer
3. QA (script)      → ./03-seo/scripts/check-urls.sh
4. FIX (human)      → solo lo que el script marque MISSING
5. LOG (sheet)      → fecha, minutos, responsable, score checklist
```

---

## Scripts en repo

| Script | Uso |
|---|---|
| `03-seo/scripts/check-urls.sh` | WP 200 vs staging 200 |
| *(pendiente)* `compare-meta.sh` | curl title/meta WP vs Drupal |
| *(pendiente)* GSC → Sheet | Apps Script semanal |

---

## Carpeta assets Einer — semi-automatizar

Si los archivos siguen patrón `slug-tour-day1.jpg`:

```bash
# Ejemplo: listar assets por slug (adaptar ruta real)
ls /ruta/assets/ | rg "salkantay"
```

Documentar convención en `02-empresa/ASSETS-MIGRACION.md` cuando la veas hoy.

---

## Regla

**Automatiza verificación, no creatividad.**  
El equipo migra; Jairo garantiza que no se rompa Google.
