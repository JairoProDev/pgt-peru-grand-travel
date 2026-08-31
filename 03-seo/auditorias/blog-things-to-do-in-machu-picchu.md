# Auditoría — Things to Do in Machu Picchu (P0)

**URL:** https://www.perugrandtravel.com/blog/things-to-do-in-machu-picchu/  
**Fecha:** 2026-08-28  
**Auditor:** agente (curl) + pendiente revisión visual Jairo  
**GSC 28d:** 1 clic · 6.115 imp · pos ~5,78 · keyword: Things to Do in Machu Picchu

---

## WordPress (producción)

| Campo | Valor |
|---|---|
| **Title** | Things to Do in Machu Picchu 2026: All The Experiences You Should Know About \| Travel guide |
| **Meta description** | Discover the top things to do in Machu Picchu. From sunrise views to luxury stays, explore our expert guide for an unforgettable Peruvian journey. |
| **Canonical** | https://www.perugrandtravel.com/blog/things-to-do-in-machu-picchu/ |
| **H1** | *(confirmar en browser — pendiente Jairo)* |
| **Schema JSON-LD** | Sí (1 bloque) — validar tipo en Rich Results Test |
| **WhatsApp** | Sí (plugin detectado) |
| **Drupal staging equivalente** | **404** en `http://147.135.114.64/blog/things-to-do-in-machu-picchu/` |

---

## Diagnóstico

| Issue | Severidad | Acción |
|---|---|---|
| **6k imp, 1 clic** = CTR ~0,02% | Alta | Probar title más corto con año + número ("12 Things… 2026") |
| Meta genérica ("unforgettable journey") | Media | Incluir lista concreta: sunrise, Huayna Picchu, tickets |
| No migrado a Drupal | **Crítica migración** | 301 obligatorio a misma slug o 404 en cutover |
| Pos ~6 sin clics | Alta | Revisar snippet en Google (`site:` búsqueda) |

---

## Propuesta title/meta (no aplicar sin OK CM)

**Title propuesto (≤60 chars):**  
`Things to Do in Machu Picchu 2026: Top Experiences & Tips`

**Meta propuesta:**  
`Things to do in Machu Picchu in 2026: sunrise, Huayna Picchu hike, tickets & how to get there. Local tips from Peru Grand Travel.`

*(Incluye focus keyword — Rank Math deja de marcar error rojo.)*

---

## Enlaces internos sugeridos (bloque Jairo)

- `/tour/the-classic-salkantay-trek-5d/`
- `/tour/machu-picchu-express-3d/`
- `/tour/incredible-machu-picchu-2d/`

---

## Checklist migración Drupal

- [ ] Misma URL path en Drupal
- [ ] Title + meta ≥ calidad WP
- [ ] Schema Article/BlogPosting
- [ ] WA visible
- [ ] 301 probado en staging
- [ ] En GSC: inspección URL post-cutover

---

## Pendiente Jairo (5 min en browser)

- [ ] Captura snippet Google
- [ ] Confirmar H1 y enlaces internos actuales
- [ ] PageSpeed mobile (LCP)
