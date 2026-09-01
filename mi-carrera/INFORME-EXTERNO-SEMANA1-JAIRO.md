# Avance SEO — Jairo · Semana 1 (25 ago – 1 sep 2026)

**Para:** Clever · Ricardo · Einel  
**Formato:** 1 página · hechos y números

---

## Resumen (3 líneas)

- Bloque asignado: **tours bloque 3** (18 URLs) · **blogs bloque 4** (115 URLs) · dominio EN `perugrandtravel.com`.
- Semana 1: línea base GSC, inventario completo, auditoría staging Drupal, mapa 301 blog (454 URLs), exports automatizados de 18 tours, optimización CTR blog P0, documentación migración y estimación de tiempos (~49 h bloque).
- Semana 2: migración piloto tours en Drupal (Salkantay 5D primero), medición WhatsApp en GA4, informe semanal clics→leads.

---

## Resultados medibles

| Indicador | Valor |
|---|---:|
| URLs inventariadas (mi bloque) | 133 |
| Mapa redirects blog listo | 454 |
| Tours exportados WP (JSON listo para Drupal) | 18/18 |
| Export GSC (queries × páginas) | 15.101 filas |
| Blogs con doble URL (riesgo migración) | 115/115 |
| Fix producción aplicado | Things MP (title/meta 2026 + indexación GSC) |
| Scripts automatización creados | 9 |
| Documentación Drupal + migración | 30+ archivos |

---

## Entregables visibles

- [x] Análisis bloque + prioridades P0/P1 (CSV + informe)
- [x] Línea base GSC sitio (643 clics / 116k imp / 28d)
- [x] Inventario sitemap WP (69 tours · 452 blogs)
- [x] Auditorías staging vs WP (blog Things MP + tour Salkantay)
- [x] Checklist pre-launch Drupal
- [x] Mapa 301 blog categoría → limpia
- [x] Pack migración: CSV maestro + clipboard SEO + exports WP
- [x] Estimación tiempos migración bloque Jairo
- [x] 1 optimización CTR en producción (blog P0)
- [ ] Migración primera URL en Drupal — **pendiente semana 2**
- [ ] Pacto revisión 25 sep por WhatsApp — **pendiente**

---

## Hallazgo crítico para la migración

Todos los blogs del sitio tienen **dos URLs** (limpia `/blog/slug/` vs indexada `/blog/categoria/slug/`). Sin redirects 301 en el cutover, Google pierde la señal acumulada. El mapa ya está preparado; falta implementación en Drupal/nginx al go-live.

---

## Dependencias (si algo no avanzó)

| Tema | Necesito de |
|---|---|
| URLs tours `/tour/slug/` en staging | Einel (Pathauto) |
| WhatsApp visible en fichas tour | Einel / equipo dev |
| Import masivo contenido | Einel (JSON:API o proceso acordado) |

---

## Próximo hito

**Migrar tour piloto Salkantay 5D** en staging con paridad SEO (title, meta, alias, checklist) — objetivo 2–3 sep.

---

*Detalle técnico completo:* `mi-carrera/INFORME-MAESTRO-SEMANA1-JAIRO.md`
