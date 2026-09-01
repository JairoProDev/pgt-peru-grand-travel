# Sprint sábado 29 ago — 9:00 a 12:00 (3 h)

**Objetivo:** Salir con baseline documentado + mensaje lunes para Einel + 1 pieza demo código.

---

## 9:00–9:45 · Medición (no negociable)

### GSC (15 min)

1. search.google.com/search-console → `perugrandtravel.com`
2. Rendimiento → 28 días → Páginas
3. Filtrar URL Things MP → anotar imp / clics / CTR
4. **EXPORTAR** CSV → guardar como `03-seo/datos/gsc-en-paginas-28d-2026-08-29.csv`

### Things MP status (10 min)

- Incógnito: `site:www.perugrandtravel.com "things to do in machu picchu"`
- ¿Sale `/blog/things-to-do-in-machu-picchu/` con title `12 Things…`?
- ¿Sigue duplicado `/Home/Cusco`? → anotar en `HECHOS.md`

### GA4 (10 min)

1. analytics.google.com → propiedad EN `368486554`
2. Admin → Eventos → `whatsapp_click` → marcar **conversión**
3. Si no existe evento: anotar “pendiente POC o plugin WP”

### Anotar baseline (10 min)

Copiar a `03-seo/datos/CTR-THINGS-MP-seguimiento.csv` (crear si no existe):

```csv
fecha,imp,clics,ctr,pos,notas
2026-08-27,6115,1,0.02,5.8,baseline xlsx
2026-08-29,,,,,post-optimización día 1
```

---

## 9:45–10:45 · Drupal staging delta (Einel)

**URL:** http://147.135.114.64/

| Check | Cómo | Resultado 29 ago |
|---|---|---|
| Home carga | Browser | ✅ 200, diseño nuevo |
| Tour Salkantay | `/product/9` | ✅ title OK; 🔴 canonical relativo; 🔴 sin WA |
| Blog Things MP | `/blog/things-to-do-in-machu-picchu/` | 🔴 **404** |
| Blogs nuevos | `/blog/limas-best-restaurants-2025-...` | ✅ existen; slugs distintos a WP |
| URLs tours | View source home | 🔴 `/product/1`, `/product/9`… no `/tour/...` |
| JSON-LD | curl \| rg ld+json | 🔴 0 en product/9 (28 ago) |

**Entregable:** actualizar `08-investigacion/DRUPAL-STAGING-REVISION-2026-08-29.md`

**Mensaje WhatsApp Einel (borrador, enviar lunes AM):**

> Einel, buenos días. Para alinear SEO en la migración: ¿los tours quedarán en `/tour/slug-wp/` o en `/product/N`? El blog Things MP hoy da 404 en staging — necesitamos la misma URL que WP para no perder posición. ¿Cuándo capacitación tours? Traigo checklist y mapa URLs. Gracias.

---

## 10:45–11:45 · Código (1 mejora visible)

**No construir CRM. No rehacer Things MP en Next.**

Elegir **una**:

### Opción A — Informe Clever (recomendada si poco tiempo)

Completar/enviar `05-marketing/PLAN-SEO-PARA-CLEVER-BORRADOR.md` con:
- Línea base GSC
- Things MP optimizado + baseline
- Riesgos Drupal (404 blog, /product/N, cart vs WA)
- POC Lighthouse 55→100

### Opción B — POC Salkantay polish

En `pgt-poc/`:
1. Re-test Lighthouse tour URL
2. Añadir UTM al link WA: `?utm_source=organic&utm_medium=tour&utm_campaign=salkantay-5d`
3. Captura antes/después para carpeta `08-investigacion/`

### Opción C — Script validador (tu diferenciador)

Crear `03-seo/scripts/check-urls.sh` que lea `mapa-urls-wp-drupal.csv` y haga HEAD a WP vs staging.

---

## 11:45–12:00 · Cierre

- [ ] `BITACORA.md` — 3 líneas del día
- [ ] `QUE-HACER-AHORA.md` — prioridad lunes
- [ ] Respirar — no abrir CRM, no pelear con Einel, no prometer ranking en 48 h

---

## Lo que NO hacer hoy

- Re-editar Things MP en WP
- Construir CRM
- Decirle a Clever que Drupal es mala idea
- Trabajar PT/ES (solo EN fase 1)
- Perseguir Rank Math 100/100
