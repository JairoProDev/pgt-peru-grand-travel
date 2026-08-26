# Content types y campos (el corazón)

## Idea

En WP un “tour” es un CPT + meta sueltos del plugin.  
En Drupal defines: **Content type `Tour`** + lista de **campos** con tipo (texto, número, entity reference, etc.).

Eso es bueno para PGT: un modelo = imposible “olvidar” precio en PT si el campo es obligatorio.

## Campos típicos que debes pedir en el modelo Tour

| Campo | Tipo sugerido | Por qué SEO/leads |
|---|---|---|
| Título | Title | H1 / title |
| Body / itinerario | Text (formatted) | Contenido |
| Duración (días) | Integer / List | Snippets, GEO |
| Precio desde | Decimal | Offer schema |
| Moneda | List (USD/PEN/…) | `priceCurrency` — problema histórico PGT |
| Incluye / No incluye | Text list / Paragraphs | Claridad lead |
| Destino | Taxonomy | Arquitectura |
| CTA WhatsApp | Link + UTM params | Conversión |
| Imagen hero | Media image | LCP |
| FAQ | Paragraphs Q&A | FAQ schema / GEO |
| ID legado WP | Text (hidden) | Migración / 301 |
| Traducciones | Content Translation | EN/ES/PT/IT |

## Blog

Content type `Article` o `Blog`: title, body, categoría, hero, Metatag.  
Cuidado PGT: URLs `/blog/cusco/slug` vs `/blog/slug` — decidir **una** canónica antes de migrar (ver playbook).

## Paragraphs (módulo)

Bloques reutilizables (hero, pricing, included) — encaja con Figma modular. Pregunta si lo usan.

## Tu trabajo en el mes 1

1. Pedir **export o pantallazo** del content type Tour en staging.
2. Comparar con 5 fichas WP de tu bloque: ¿falta algún dato que ventas usa?
3. Documentar gaps: “en WP hay X; en Drupal no está el campo”.
4. Eso es aporte de **jefe de producto digital**, no de “quien no sabe Drupal”.

Siguiente: `04-MULTIIDIOMA-Y-DOMAIN.md`.
