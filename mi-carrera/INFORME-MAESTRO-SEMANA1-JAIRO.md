# Informe maestro — Semana 1 · Jairo Saul Salas Quiñones

**Rol:** Analista SEO/GEO · Peru Grand Travel  
**Periodo:** 25 ago – 1 sep 2026 (días 1–6)  
**Audiencia:** Clever · Ricardo · Einel · revisión jefatura (~25 sep)  
**Versión:** 1 sep 2026 · documento vivo — actualizar cada viernes

> **Dos repos, dos frentes:** este informe cubre **PGT** (SEO, datos, migración Drupal, estrategia). El trabajo de **código/POC** (`pgt-web`, Next.js, despliegue) tiene su propio informe paralelo.

---

## Resumen ejecutivo (30 segundos)

En 6 días de onboarding profundo, pasé de cero contexto a **dueño documentado del cutover SEO** de la migración WP → Drupal EN:

- Inventarié **133 URLs** de mi bloque (18 tours + 115 blogs) con línea base GSC, mapa de **454 redirects 301** blog y diagnóstico de canibalización URL.
- Audité staging Drupal (`147.135.114.64`), mapeé el formulario Product real (`anymerce`), generé **pack de migración** (CSV maestro, clipboard SEO, exports WP JSON/MD de los 18 tours).
- Entregué **9 scripts** de automatización, **15 docs Drupal**, **101 capturas** del admin, checklist pre-launch, plan SEO para Clever y estrategia del experimento entre los 4 del cuarteto SEO.
- Apliqué el primer fix visible en producción: optimización CTR del blog P0 **Things to Do in Machu Picchu** (6.115 imp, pos ~6) + solicitud de indexación GSC.
- Estimé tiempos de migración manual: **~49 h** bloque completo (+15 % buffer) — base para planificar sin quemar al equipo.

**Aún no migrado en Drupal:** 0/18 tours y 0/115 blogs del bloque Jairo en staging con paridad WP. El trabajo de la semana fue **preparación, datos y due diligence** — no clicks manuales en Drupal todavía.

---

## Tablero de resultados (números que importan)

| Indicador | Valor | Evidencia |
|---|---:|---|
| Días trabajados | 6 | Bitácora + informes diarios |
| URLs en mi bloque | **133** | `inventario-bloque-jairo.csv` |
| Tours asignados (bloque 3) | 18 | `tours-jairo-2026-08-25.csv` |
| Blogs asignados (bloque 4) | 115 | `blogs-jairo-2026-08-25.csv` |
| Impresiones GSC bloque blogs | ~99.857 | Sheet + análisis 26 ago |
| Impresiones GSC bloque tours | ~19.734 | Sheet + análisis 26 ago |
| Blogs con URL limpia ≠ URL indexada | **115/115** | Riesgo migración documentado |
| Mapa 301 blog (sitio completo) | **454** filas | `redirects-blog-301.csv` |
| Inventario sitemap WP EN | 69 tours · 452 blogs · 62 pages | `inventario-sitemap-2026-08-31/` |
| Export GSC queries+páginas | 15.101 filas | `gsc-export-2026-09-01/` |
| Export GA4 landing + eventos | 174 landings · 8 eventos | `ga4-export-2026-09-01/` |
| Tours exportados WP → JSON/MD | **18/18** OK | `wp-export-tours-jairo/manifest.json` |
| Scripts Python/Bash creados | **9** | `03-seo/scripts/` |
| Docs Drupal (aprendizaje) | **15** | `10-aprendizaje/drupal/` |
| Capturas admin Drupal | **101** | `drupal-capturas-2026-09-01/` |
| Auditorías P0 escritas | 2 | Things MP blog + Salkantay tour |
| Fix producción aplicado | 1 | Rank Math Things MP + indexación GSC |
| POC código desplegado | 1 | `pgt-poc.vercel.app` (informe en pgt-web) |
| Lighthouse tour (POC vs WP) | **99 vs 55** perf mobile | `LIGHTHOUSE-COMPARATIVA.md` |

---

## Línea de tiempo — qué hice cada día

### Día 1 · 25 ago — Onboarding y bloque

| Hecho | Resultado |
|---|---|
| Accesos: marketing@, NAS, Drive, grupo WA | Operativo desde día 1 |
| Reparto cuarteto SEO confirmado | Tours bloque **3** · Blogs bloque **4** |
| Pacto oral Clever | S/ 3.500 · revisión jefatura ~25 sep |
| Contexto equipo | Ricardo, Lizet, Arely; migración Drupal decidida |

**Entregable:** presencia, escucha, claridad de bloque. Sin auditoría aún — correcto para día 1.

---

### Día 2 · 26 ago — Análisis de datos y plan

| Hecho | Resultado |
|---|---|
| Charla Clever: Drupal VPS Ubuntu, plan SEO esperado | Alineación estratégica |
| Exploración wp-admin (Tourmaster, Yoast, ~30 plugins) | Mapa técnico WP |
| Export y análisis bloque 18+115 | `ANALISIS-BLOQUE-JAIRO-2026-08-25.md` |
| Prioridades P0/P1 | `PRIORIDAD-ACCION-JAIRO-2026-08-26.csv` |
| Inventario Drive + GA4 | `DRIVE-INVENTARIO.md`, `GA4-INVENTARIO.md` |
| Sistema HECHOS/DUDAS/INSIGHTS | Base de conocimiento verificable |
| Borrador plan Clever | `PLAN-SEO-PARA-CLEVER-BORRADOR.md` |

**Insight clave:** 10 blogs en top 10 con CTR ~0,07 % sobre ~12k impresiones → ROI inmediato en snippets, no en posts nuevos.

---

### Día 3 · 27 ago — GSC, Einel, documentación

| Hecho | Resultado |
|---|---|
| Nombre jefe interino: **Einel** | HECHOS actualizado |
| Línea base GSC sitio 28d | 643 clics · 116k imp · CTR 0,6 % |
| Informes días 1–3 formalizados | `03-seo/informes/` |
| NAS inventariado (Ryzen 5600GT, 3,58 TiB) | Captura OMV |

---

### Día 4 · 28 ago — Staging Drupal + auditorías P0

| Hecho | Resultado |
|---|---|
| Staging OVH `147.135.114.64` verificado | Drupal 11 + anymerce |
| Auditoría blog Things MP vs staging | WP OK · staging **404** |
| Auditoría tour Salkantay 5D | WP slug ≠ Drupal `/product/9` |
| Mapa 25 URLs prioritarias | `mapa-urls-wp-drupal.csv` |
| Inventario 133 URLs bloque | `inventario-bloque-jairo.csv` |
| Checklist pre-launch | `CHECKLIST-PRE-LAUNCH-DRUPAL.md` |
| Optimización CTR Things MP en WP | Title `12 Things…(2026)` + meta nueva |
| GSC: solicitud indexación Things MP | Cola prioritaria |
| POC Next.js scaffold + deploy Vercel | `pgt-poc.vercel.app` |
| Playbook migración actualizado | `MIGRACION-WP-DRUPAL-PLAYBOOK.md` |

---

### Día 5 · 29 ago — Estrategia y sprint sábado

| Hecho | Resultado |
|---|---|
| Plan 30 días → S/ 5.000 | `PLAN-30-DIAS-5000.md` |
| Decisión página código: Salkantay 5D | `2026-08-29-decision-pagina-codigo.md` |
| Staging delta documentado | `DRUPAL-STAGING-REVISION-2026-08-29.md` |
| Script validador URLs | `check-urls.sh` |
| Reframe Things MP WP = plantilla migración | No trabajo perdido |

---

### Día 6 · 1 sep — Pack migración Drupal (día de arranque)

| Hecho | Resultado |
|---|---|
| Accesos Drupal individuales + assets (Einel) | Listo para migrar |
| Capacitación Drupal → Ricardo | Redundancia equipo |
| Experimento 4 estrategias SEO (Clever) | `EXPERIMENTO-4-ESTRATEGIA-JAIRO.md` + scorecard |
| Inventario sitemap live | 69 tours · 452 blogs · script bash |
| Export Excel keywords → CSV + 454 redirects | `keywords-canibalizacion-2026-08-31/` |
| Sprint pack Drupal | `jairo-migracion-maestro.csv` (133 filas) |
| Mapa formulario Product (4 tabs) | `12-TOUR-PRODUCT-FORM-MAPA-COMPLETO.md` |
| 101 capturas admin Drupal | `drupal-capturas-2026-09-01/` |
| Clipboard SEO 18 tours | `TOURS-SEO-CLIPBOARD.md` |
| Export WP 18 tours JSON+MD | `wp-export-tours-jairo/` — 18/18 OK |
| Guía paso a paso tour piloto Salkantay | `PASO-A-PASO-TOUR-01-SALKANTAY.md` |
| Estimación tiempos migración | `estimacion-tiempos-migracion-jairo.csv` (~49 h) |
| Export GSC + GA4 automatizado | `gsc-export-2026-09-01/`, `ga4-export-2026-09-01/` |
| Guía medición leads WA | `MEDIR-LEADS-WEB-ACTUAL.md` |

**Bloqueadores identificados hoy:**

- Pathauto tours: `/product/N` no `/tour/{slug}/` → pedir Einel
- JSON:API en staging → 404 (no import masivo sin Einel)
- WhatsApp no visible en staging tours
- Body/tabs Tourmaster no en WP REST → semi-manual o scrape HTML

---

## Inventario de entregables (por categoría)

### A. Datos y línea base

| Archivo / carpeta | Qué es | Para qué sirve |
|---|---|---|
| `tours-jairo-2026-08-25.csv` | 18 tours + GSC | Bloque asignado |
| `blogs-jairo-2026-08-25.csv` | 115 blogs + GSC | Bloque asignado |
| `keywords-canibalizacion-2026-08-31/` | 454 blogs + redirects + canibalización | Migración + 301 cutover |
| `inventario-sitemap-2026-08-31/` | 589 URLs live | Cross-check técnico |
| `inventario-bloque-jairo.csv` | 133 URLs unificadas | Tracking migración |
| `jairo-migracion-maestro.csv` | Maestro con estado_drupal | Sprint diario |
| `gsc-export-2026-09-01/` | 15k filas queries×páginas | Análisis profundo |
| `ga4-export-2026-09-01/` | Landings + eventos 28d | Medición leads |
| `estimacion-tiempos-migracion-jairo.csv` | ~49 h bloque | Planificación equipo |

### B. Automatización (scripts)

| Script | Función |
|---|---|
| `analyze-excel-keywords.py` | Excel → CSV + redirects + insights |
| `export-wp-sitemap-inventory.sh` | Sitemaps live → inventario |
| `export-wp-content.py` | Meta HTML público por URL |
| `export-wp-tours-for-drupal.py` | WP REST + HTML → JSON/MD por tour |
| `generate-drupal-sprint-pack.py` | CSV maestro + sprint pack |
| `generate-tour-seo-clipboard.py` | Copy-paste SEO tours → MD |
| `check-urls.sh` | Validador HTTP masivo |

### C. Guías operativas

| Guía | Uso |
|---|---|
| `DRUPAL-SPRINT-JAIRO-HOY.md` | Sprint diario staging |
| `PASO-A-PASO-TOUR-01-SALKANTAY.md` | Piloto tour #1 |
| `MIGRACION-SEO-CAMPO-A-CAMPO.md` | Checklist 10 ítems por URL |
| `MEDIR-LEADS-WEB-ACTUAL.md` | GA4 + GTM + WA |
| `CTR-THINGS-MP-*` (3 archivos) | Fix snippet P0 |
| `GSC-SOLICITAR-INDEXACION.md` | Procedimiento indexación |

### D. Investigación y estrategia

| Doc | Uso |
|---|---|
| `ESQUEMA-MIGRACION-MAESTRO.md` | Biblia migración |
| `MIGRACION-WP-DRUPAL-PLAYBOOK.md` | Cutover SEO dueño |
| `CHECKLIST-PRE-LAUNCH-DRUPAL.md` | Go-live |
| `EXPERIMENTO-4-ESTRATEGIA-JAIRO.md` | Scorecard cuarteto |
| `MIGRACION-AUTOMATIZACION.md` | Qué automatizar vs manual |
| `ANALISIS-BLOQUE-JAIRO-2026-08-25.md` | Prioridades SEO bloque |

### E. Aprendizaje Drupal

| Doc | Uso |
|---|---|
| `12-TOUR-PRODUCT-FORM-MAPA-COMPLETO.md` | Mapa formulario Product |
| `13-INDICE-CAPTURAS-DRUPAL.md` | Índice 101 screenshots |
| `00-LEER-PRIMERO.md` … `11-COMO-PRACTICAR-*` | Currículo autodidacta |

### F. Auditorías P0

| Auditoría | Hallazgo principal |
|---|---|
| `blog-things-to-do-in-machu-picchu.md` | WP completo; staging 404; CTR crítico |
| `tour-the-classic-salkantay-trek-5d.md` | Slug mismatch; sin schema staging |

---

## Hallazgos SEO estratégicos (para la exposición)

### 1. Canibalización URL blog — bomba de migración

**115/115** blogs del bloque tienen dos URLs:

- Limpia: `/blog/{slug}/` (objetivo Drupal)
- Con categoría: `/blog/{categoria}/{slug}/` (lo que Google indexó)

**Acción:** mapa 454 redirects listo. Sin esto, cutover = pérdida de rankings.

### 2. CTR vs ranking — dinero en la mesa

Blogs en top 10 con CTR ~0,07 % (mercado espera 2–5 %). Ejemplo: Things MP — 6.115 imp, 1 clic, pos ~6.

**Acción:** fix aplicado en WP; medir en 2–4 semanas GSC.

### 3. Tours — quick wins en posición 11–30

Salkantay 5d (pos 26,8 · 1.218 imp), Cusco Planetarium (pos 20,6), Machu Picchu Express 3D (pos 29,8).

**Acción:** migrar con paridad + mejorar title/meta en cutover.

### 4. Medición leads rota

GA4 EN: eventos clave = 0. WhatsApp no trackeado como conversión.

**Acción:** guía escrita; pendiente implementar `whatsapp_click` en GTM.

### 5. Staging Drupal — gaps antes de cutover

| Gap | Impacto |
|---|---|
| Blog Things MP → 404 | P0 bloqueado |
| URLs `/product/N` vs `/tour/slug/` | SEO + UX |
| Sin WhatsApp en tours | Conversión |
| Sin JSON-LD en staging | Rich results |
| JSON:API 404 | Sin import automático |

---

## Estimación de esfuerzo migración (bloque Jairo)

| Fase | Cantidad | Min/unidad | Total |
|---|---:|---:|---:|
| Tours (piloto) | 1 | 50 | 50 min |
| Tours (resto) | 17 | 35 | 595 min |
| Blogs | 115 | 20 | 2.300 min |
| **Subtotal** | 133 | — | **~49 h** |
| Buffer +15 % | — | — | ~7 h |
| **Total planificado** | — | — | **~56 h** |

Estrategia: **semi-automático** (exports + clipboard + QA scripts), no migración 100 % manual ni 100 % API.

---

## Experimento 4 personas — propuesta de scorecard

Propuesta para el grupo WA (misma regla para Ricardo, Lizet, Arely, Jairo):

| Métrica | Herramienta | Frecuencia |
|---|---|---|
| URLs migradas sin 404 | `check-urls.sh` | Semanal |
| Checklist SEO 10 ítems | `MIGRACION-SEO-CAMPO-A-CAMPO.md` | Por URL |
| Tiempo por URL | Minutos anotados en CSV maestro | Por URL |
| CTR top 3 URLs | GSC | Semanal |
| Clics → WA | GA4 `whatsapp_click` | Semanal |
| Lighthouse mobile | PageSpeed | Por tour piloto |
| Errores GSC nuevos | Search Console | Semanal |

**Diferenciador Jairo:** datos exportados, scripts, documentación reutilizable por el equipo.

---

## Bloqueos y dependencias (honestos)

| Bloqueo | Owner | Estado |
|---|---|---|
| Pathauto `/tour/{slug}/` | Einel | Pendiente |
| JSON:API / módulos import | Einel | Pendiente |
| WhatsApp block global staging | Einel | Pendiente |
| Pacto WhatsApp por escrito (25 sep) | Jairo → Clever | Pendiente |
| NAS `linux_admin` avisar Ricardo | Jairo | Pendiente |
| Medición WA en GA4 | Jairo + Lizet | Guía lista, tag pendiente |
| Migración manual tour #1 Drupal | Jairo | Pack listo, ejecución pendiente |

---

## Próximos hitos (semana 2)

| Prioridad | Hito | Fecha objetivo |
|---|---|---|
| P0 | Migrar tour piloto Salkantay 5D en Drupal | 2–3 sep |
| P0 | 5 preguntas Einel (slug, SEO, WA, REST, blogs) | 2 sep |
| P1 | Migrar 3 tours piloto (Salkantay, Choquequirao, MP 2D) | 6 sep |
| P1 | Informe externo 1 pág. a Ricardo (mié) | 3 sep |
| P1 | Marcar `estado_drupal` en CSV maestro | Continuo |
| P2 | Script `export-wp-blogs-for-drupal.py` | Post-tours |
| P2 | GEO baseline 10 prompts | Semana 2 |

---

## Frases para la exposición (defendibles)

> "En una semana pasé de onboarding a tener inventario completo de 133 URLs, mapa de 454 redirects blog, exports automatizados de los 18 tours y documentación del formulario Drupal real — no la ruta Commerce que da 404."

> "El mayor ROI inmediato no es escribir posts nuevos: son 10 blogs en página 1 con CTR del 0,07 %. Ya apliqué el fix en el P0 con 6.115 impresiones."

> "Identifiqué que el 100% de mis blogs tienen doble URL — limpia vs categoría indexada. Sin mapa 301, la migración Drupal pierde rankings. Ese mapa ya está exportado."

> "No prometo migrar 133 URLs en una semana sin datos. Sí prometo que cuando migremos, será con checklist, baseline GSC y sin sorpresas de slug."

> "Construí herramientas que Ricardo y el equipo pueden usar — no dependencia de una sola persona."

---

## Índice de evidencias (links rápidos)

| Tipo | Ruta |
|---|---|
| Informes diarios | `03-seo/informes/README.md` |
| Bitácora | `01-situacion/BITACORA.md` |
| Hechos verificados | `01-situacion/HECHOS.md` |
| Entregables checklist | `mi-carrera/ENTREGABLES-CREDITO-JAIRO.md` |
| Qué hacer hoy | `01-situacion/QUE-HACER-AHORA.md` |
| Informe externo 1 pág. | `mi-carrera/INFORME-EXTERNO-SEMANA1-JAIRO.md` |
| Código / POC | Repo `pgt-web` (informe separado) |

---

## Control de versiones

| Fecha | Cambio |
|---|---|
| 1 sep 2026 | v1 — informe maestro semana 1 completo |

**Próxima actualización:** viernes 5 sep 2026 (cierre semana 2 + métricas migración).
