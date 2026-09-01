# Migración SEO — campo a campo (WP → Drupal)

**Para:** capacitación Einel + tu QA por URL  
**Dueño:** Jairo (especificación) · Einel (implementación Drupal)

---

## Por qué existe este doc

Lo que optimizaste en Things MP **no se pierde** — es la **receta** que cada URL migrada debe cumplir en Drupal.

---

## Blog (ejemplo Things MP)

| Elemento | WordPress (Rank Math) | Drupal (preguntar a Einel) | Valor objetivo |
|---|---|---|---|
| URL | `/blog/things-to-do-in-machu-picchu/` | Pathauto / alias | **Igual** |
| SEO Title | `12 Things to Do in Machu Picchu (2026 Guide)` | Campo meta title | 44 chars |
| Meta description | `Things to do in Machu Picchu in 2026: sunrise…` | Campo meta desc | ≤160 chars |
| H1 | `12 Things to Do in Machu Picchu (2026)` | Título nodo | Alineado al title |
| Focus keyword | Things to Do in Machu Picchu | (opcional módulo SEO) | Coherencia |
| Intro | Párrafo `Planning your 2026 trip?...` | Body primer párrafo | Keyword + año |
| Tours block | HTML lista 4 tours | Bloque CTA o paragraph | Enlaces a `/tour/...` |
| Canonical | self | Metatag | Absoluto https |
| Schema | Article (Rank Math) | Metatag / custom | Article + FAQ si aplica |
| WA | Plugin click-to-chat | Bloque / field | Visible |

---

## Tour (ejemplo Salkantay 5D)

| Elemento | WordPress | Drupal staging hoy | Objetivo |
|---|---|---|---|
| URL | `/tour/the-classic-salkantay-trek-5d/` | `/product/9` 🔴 | **Slug WP** |
| Title | `5-Day Salkantay Sky Camp Trek…` | `Salkantay Trek 5D/4N \| PGT` | OK similar |
| Precio | US$ 731 | $590 en card 🔴 | Una fuente |
| Schema | Product JSON-LD | 0 🔴 | Product + Offer |
| CTA | WhatsApp | Add to cart 🔴 | WA |
| Itinerario | Tourmaster días | Fields Drupal | Paridad contenido |

---

## QA por URL migrada (5 min)

```
[ ] URL idéntica a WP (o 301 documentado)
[ ] Title ≤ 60 chars
[ ] Meta 120–160 chars
[ ] H1 único
[ ] Canonical absoluto prod
[ ] Precio + moneda
[ ] WA visible
[ ] JSON-LD valida (search.google.com/test/rich-results)
[ ] 200 (no 404)
[ ] Enlaces internos a 2+ tours/blogs
```

---

## Plantilla reutilizable

Al migrar cada tour/blog, copia fila a `03-seo/datos/mapa-urls-wp-drupal.csv` columna `notas_auditoria`.
