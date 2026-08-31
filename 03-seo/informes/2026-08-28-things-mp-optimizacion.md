# Informe — Optimización CTR Things MP (WP blog)

**Fecha:** 28 ago 2026 · tarde  
**Autor:** Jairo (con guía agente)  
**URL:** https://www.perugrandtravel.com/blog/things-to-do-in-machu-picchu/  
**Post ID:** 18674  
**Editor:** `/blog/wp-admin/` (WordPress blog separado del sitio principal)

---

## Baseline (antes)

| Métrica GSC 28d | Valor |
|---|---:|
| Impresiones | 6.115 |
| Clics | 1 |
| CTR | ~0,02 % |
| Posición media | ~5,8 |

**Title SEO (Rank Math template):** `%title% %page% | Travel guide` → ~91 chars, truncado en Google  
**Meta:** genérica (“unforgettable Peruvian journey”)  
**H1:** título largo igual al post title antiguo

---

## Cambios aplicados (28 ago)

### Rank Math — Preview Snippet Editor

| Campo Rank Math | Valor nuevo | Chars |
|---|---|---:|
| **Title** (SEO title) | `12 Things to Do in Machu Picchu (2026 Guide)` | 44/60 ✅ |
| **Description** (meta) | `Sunrise at the citadel, Huayna Picchu hike, Machu Picchu Mountain, tickets & how to get there — local tips for 2026. Plan with Peru Grand Travel.` | 145/160 ✅ |
| **Permalink** | `things-to-do-in-machu-picchu` | sin cambio ✅ |
| **Focus keyword** | `Things to Do in Machu Picchu` | ya existía |

### Completado tarde 28 ago

- [x] Meta v2 con focus keyword — Basic SEO **All Good** ✅
- [x] Rank Math score **86–87/100**
- [x] Post title (H1): `12 Things to Do in Machu Picchu (2026)`
- [x] Primer párrafo hook 2026 (`Planning your 2026 trip?...`)
- [x] Focus keyword en primeros 10% del contenido ✅

### Rank Math — qué ignorar (28 ago)

| Checklist | Estado | Acción |
|---|---|---|
| **Basic SEO** | All Good | Nada — es lo que importa |
| Additional: keyword en subheading | 1 error | Opcional: renombrar un H2 (bajo ROI) |
| Title Readability: sentiment / power word | 2 “errors” | **Ignorar** — plantilla Rank Math, no ranking |
| Link Suggestions | No visible | Enlazar a mano (tours) — no bloquear Update |

### Pendiente

- [x] Bloque tours Custom HTML (Recommended Machu Picchu Tours…) — visible en editor
- [x] **Save** en WP (= Update)
- [x] GSC **Solicitar indexación** — cola prioritaria OK (captura 28 ago noche)
- [ ] Lun+ : snippet Google muestra `12 Things… (2026 Guide)` (7–14 días)
- [ ] Seguimiento CTR lunes en GSC

---

## Hallazgos técnicos

- **Blog ≠ sitio principal:** posts en `perugrandtravel.com/blog/wp-admin/`, no en `/wp-admin/` (0 posts ahí)
- **Plugin SEO:** Rank Math (no Yoast). Title = SEO title; Description = meta description
- **Canibalización:** `/blog/cusco/things-to-do-in-machu-picchu/` → **301** a URL principal ✅

---

## URLs tours (enlaces internos — verificadas 200)

| Tour | URL |
|---|---|
| Classic Machu Picchu 5D | https://www.perugrandtravel.com/tour/classic-machu-picchu-5d/ |
| Salkantay SKY 5D | https://www.perugrandtravel.com/tour/the-classic-salkantay-trek-5d/ |
| Machu Picchu Express 3D | https://www.perugrandtravel.com/tour/machu-picchu-express-3d/ |
| Incredible Machu Picchu 2D | https://www.perugrandtravel.com/tour/incredible-machu-picchu-2d/ |

---

## Meta v2 recomendada (incluye focus keyword)

```
Things to do in Machu Picchu in 2026: sunrise, Huayna Picchu hike, tickets & how to get there. Local tips from Peru Grand Travel.
```

(~130 chars — deja espacio; Rank Math verde + keyword en meta)

---

## Seguimiento (cada lunes)

GSC → Rendimiento → filtro página exacta → anotar clics/CTR vs baseline.

| Fecha | Imp | Clics | CTR | Notas |
|---|---:|---:|---:|---|
| 27 ago baseline | 6.115 | 1 | 0,02 % | xlsx en datos/ |
| | | | | |

---

## Plantilla reutilizable (otros blogs P0)

1. Abrir `/blog/wp-admin/` → post correcto
2. Rank Math → Title **sin** `%variables%` — texto plano ≤60 chars
3. Description con keyword + lista concreta ≤160 chars
4. H1 alineado al title
5. Bloque tours + internal links
6. Update + GSC indexación

**Próximo candidato:** Museums in Machu Picchu (~2.494 imp)
