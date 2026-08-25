# SEO — índice operativo

La auditoría completa, los 23 problemas, el playbook de 90 días y el mapa hreflang están en `archivo-original/empleo-seo/`. Aquí va lo que necesitas **activo**.

## Hallazgos que todavía puedes afirmar (24 ago 2026)

| # | Hallazgo | Estado vivo |
|---|---|---|
| 1 | Cero hreflang en 4 dominios | **Sí. grep = 0 en las 4 homes** |
| 2 | Offer sin priceCurrency / PT sin Offer | No re-rastreé fichas hoy. Re-verificar día 1 con 1 URL por dominio |
| 3 | Cero aggregateRating en schema | Re-verificar |
| 4 | Blog EN 0, IT ~2 | Re-verificar sitemaps semana 1 |
| 5 | no-store en EN | **Cuidado.** Hoy EN y PT responden `public, max-age=0`. No recites no-store |
| — | robots EN con Disallow absoluto y `*/page/*` | **Sí, intacto** |

## Orden de implementación (no cambia)

Semana 1: accesos, línea base, cero producción de diseño.
P0: moneda Offer, Offer en PT, hreflang piloto, robots, caché real (max-age > 0, no solo public).
No: Next.js, matar GYG, posiciones, pegar 4.9 de la empresa en 69 tours.

Detalle: `archivo-original/empleo-seo/14-PLAYBOOK-APORTES.md`.

## Relación con GEO

Schema, fichas con hechos (precio, duración, idioma del guía, punto de encuentro), `TravelAgency`, licencia Camino Inca, permitir GPTBot/PerplexityBot si el WAF no los mata, `llms.txt` cuando sistemas acepte. Ver `04-geo/`.

## Relación con la jefatura

El SEO técnico alimenta al equipo: URLs, intención por mercado, UTM, lo que no se traduce ES→EN. No les quites el calendario el día 1. Dales **un** clúster (Inca Trail EN) cuando haya arquitectura.

## Documentos fuente

- Insights: `archivo-original/empleo-seo/01-INSIGHTS-Peru-Grand-Travel.md`
- Auditoría: `02-AUDITORIA-SEO-TECNICA-preliminar.md`
- 23 problemas: `D02-LOS-23-PROBLEMAS-EXPLICADOS.md`
- Equivalencias: `09-herramientas/equivalencias-hreflang.csv`
- Gaps catálogo: `09-herramientas/gaps-de-catalogo.csv`
- Editorial EN: `archivo-original/empleo-seo/09-PLAN-EDITORIAL-INGLES.md`
