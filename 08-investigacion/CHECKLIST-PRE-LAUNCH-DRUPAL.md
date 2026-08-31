# Checklist pre-launch Drupal — EN cutover

**Dueño QA SEO:** Jairo  
**Actualizado:** 28 ago 2026  
**Staging:** http://147.135.114.64/

Marcar cada ítem antes de cutover producción. **No lanzar** si hay 🔴 sin resolver.

---

## A. Staging / infraestructura

| # | Check | Estado 28 ago | Responsable |
|---|---|---|---|
| A1 | **noindex** en staging (robots + meta + idealmente auth) | 🔴 robots.txt permite indexar | Einel |
| A2 | HTTPS en producción (certificado válido) | 🔴 solo HTTP en IP | Einel |
| A3 | DNS apunta a servidor final (no IP cruda) | ⬜ | Einel/Ricardo |
| A4 | Cache habilitado (no `no-cache, private` en home) | 🔴 Max-Age 0 | Einel |
| A5 | Backups DB + rollback plan documentado | ⬜ | Einel |

---

## B. URLs y redirects

| # | Check | Estado 28 ago |
|---|---|---|
| B1 | Mapa 301 WP → Drupal completo (133 bloque Jairo mínimo) | 🟡 CSV 25 URLs iniciado |
| B2 | **Misma slug** que WP donde sea posible | 🔴 `/product/9` vs `/tour/the-classic-salkantay-trek-5d/` |
| B3 | Blogs P0 existen (no 404) | 🔴 Things MP → 404 |
| B4 | Cero cadenas redirect (A→B→C) | ⬜ probar en staging |
| B5 | Módulo Redirect o nginx map cargado | ⬜ |
| B6 | Soft 404 audit (200 con "not found") | ⬜ |
| B7 | Canonical absoluto (no relativo `/product/9`) | 🔴 canonical relativo en product/9 |

---

## C. SEO on-page (muestra 20 URLs)

Por cada URL piloto:

- [ ] Title único (no `\| Peru Grand Travel` solo)
- [ ] Meta description 120–155 chars
- [ ] H1 una sola
- [ ] Canonical correcto https://www.perugrandtravel.com/...
- [ ] Precio + moneda visible
- [ ] Imágenes con alt
- [ ] Enlaces internos (blogs → tours)

**URLs piloto mínimas:**

1. Home  
2. `/blog/things-to-do-in-machu-picchu/`  
3. `/blog/museums-in-machu-picchu/`  
4. `/tour/the-classic-salkantay-trek-5d/`  
5. `/tour/salkantay-trek-4-days/`  
6. `/tour/machu-picchu-express-3d/`  
7. `/tour/maras-moray-and-the-salineras-full-day/`  
8. `/blog/what-is-the-best-time-to-travel-to-peru-machu-picchu/`  
9. `/packages`  
10. `/trek`  
11–20. *(completar con landings Lizet)*

---

## D. Schema / rich results

| # | Check | Estado 28 ago |
|---|---|---|
| D1 | JSON-LD en home (`TravelAgency`) | 🔴 0 detectado |
| D2 | JSON-LD en tours (`TouristTrip`/`Product` + `Offer`) | 🔴 0 en product/9 |
| D3 | JSON-LD en blogs (`Article`) | ⬜ |
| D4 | FAQ schema donde hay FAQ | ⬜ |
| D5 | Rich Results Test sin errores críticos | ⬜ |

---

## E. Conversión / negocio

| # | Check | Estado 28 ago |
|---|---|---|
| E1 | **WhatsApp** visible en tour (si negocio sigue WA) | 🔴 Add to cart |
| E2 | UTM en links WA | ⬜ |
| E3 | GA4 evento `whatsapp_click` | ⬜ confirmar Lizet |
| E4 | GTM/pixels paridad con WP | ⬜ |
| E5 | Formularios contacto funcionan | ⬜ |

---

## F. Internacional (fase EN primero)

| # | Check | Notas |
|---|---|---|
| F1 | Solo EN en cutover 1 | Acordado con Einel |
| F2 | hreflang preparado para fase 2 | ⬜ |
| F3 | Switcher PT/ES no publica contenido vacío | 🟡 UI visible, contenido demo |

---

## G. Post-cutover (día D + 60 días)

| Día | Acción |
|---|---|
| D0 | Verificar 10 URLs críticas manualmente |
| D0 | Enviar sitemap a GSC |
| D+1 | Informe 1 pág. Clever |
| D+3 | Lista 404 GSC |
| D+7 | GSC rendimiento vs baseline (`GSC-LINEA-BASE-2026-08-27.md`) |
| D+30 | Informe keywords + clics bloque Jairo |
| D+60 | Cierre migración EN |

---

## Resumen ejecutivo staging (28 ago)

| Área | Semáforo |
|---|---|
| Diseño visual | 🟢 |
| Contenido real | 🔴 |
| URLs / 301 | 🔴 |
| SEO técnico | 🔴 |
| Performance | 🔴 |
| Conversión (WA) | 🔴 |
| Seguridad staging | 🔴 |

**Veredicto:** No listo para cutover. Listo para QA colaborativo con Einel.
