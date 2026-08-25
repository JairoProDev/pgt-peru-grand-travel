# Figma PGT — lectura (25 ago 2026)

Visto en capturas: archivo “Sin título” / borradores. Diseño **modular** (layers: PackagesPage, Pricing, Included, Itinerary, What to Bring, Awards, Footer). Tipografía **Poppins**. Azul marca ~`#193A8A` / `#192A8A`. CTA naranja “Book Now”. Ficha ejemplo: Classic Machu Picchu 5D/4N, precios por categoría de hotel (Economy→Luxury), sidebar “Book this tour” / “Custom Quote”.

## Qué implica para el stack

| Lectura | Implicación |
|---|---|
| Componentes claros (Included, Pricing table…) | Encaja con **content types** (Drupal) **o** bloques/ACF (WordPress) **o** componentes React |
| Misma Poppins que el sitio actual | Continuidad de marca; en performance ya sabes: no cargar 100–900 |
| Checkout en diseño = Book / Quote | Sigue alineado a **lead** (WhatsApp/form), no necesariamente motor de reservas nuevo |
| Modular ≠ “listo para Drupal” | Falta: mapa de campos → Tourmaster / CMS, y **política de URLs** |

## Decisión (sin cambio vs STACK-IDEAL)

1. **90 días:** no migrar. Bajar Figma a **tema hijo WP** o plantilla Tourmaster, **slugs iguales**.
2. **Si ya hay contrato Drupal:** tú dueño SEO del cutover (301, GSC), no el que aprende Drupal contra reloj en 2 semanas.
3. **Código (Next + CMS):** máximo control + tu velocidad; solo si hay admin para que Lizet/Ricardo/Ops editen precios sin ti.

Pregunta mañana a Ricardo: *“El Figma, ¿cambia URLs o solo look? ¿Quién lo baja y a qué plataforma?”*
