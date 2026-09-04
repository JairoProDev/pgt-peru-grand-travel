# Competencia — acciones de esta semana (no un PDF de Lighthouse)

**Fecha:** 5 sep 2026  
**Norte:** más leads WhatsApp calificados. No “ganar TTFB”.  
**Canónico público:** WordPress `www`. Lo que sigue se practica en [next.](https://next.perugrandtravel.com) y se copia a WP solo si Einel lo pide.

Lectura previa: [`BRIEF-COMPETITIVO-PGT-2026-09-04.md`](BRIEF-COMPETITIVO-PGT-2026-09-04.md) (citas Alpaca/GYG/SAS, 4 sep), [`COMPETIDORES.md`](COMPETIDORES.md), [`TURISMO-PERU-2026.md`](TURISMO-PERU-2026.md).

**Norte de esa ficha:** no perseguir el volumen de reviews de Alpaca ni el checkout de GetYourGuide. Ganar como **operador licenciado en Cusco que responde WhatsApp con RUC, permisos reales y tres productos claros**. No copiar “#1 on TripAdvisor” (Alpaca se anuncia #1 y su listing estaba ~#226).

`whatsapp_click` → GA4 **ya está** (GTM). Esta semana: bloquecito de permisos + tabla Classic vs Short vs Salkantay en next.; Einel trae licencia/RUC 2026 (no un PDF de 2022); Lizet arma saludos WA. Ricardo confirma hechos de ops, no aprueba precios.

## Cómo nos ven (honesto)

PGT es operador licenciado en Cusco (RUC 20603059302), tres marcas (EN / ES / PT), conversión por WhatsApp. No competimos en “checkout GYG”. Competimos en: **confianza local + respuesta rápida + itinerario a medida**.

Los jugadores que duelen:

| Tipo | Quién | Qué copiar | Qué ignorar |
|------|-------|------------|-------------|
| Inca Trail USA | [Alpaca Expeditions](https://www.alpacaexpeditions.com/) | Permisos, tamaño de grupo, “sold out” honesto | Página de 8 MB |
| Schema / EN serio | Valencia Travel (ficha en repo 9 ago) | `TravelAgency` + estrellas si son reales | Headcount de marketing |
| hreflang simple | TreXperience | Un hreflang de verdad | Arquitectura WP extra |
| Default del viajero indeciso | [GetYourGuide](https://www.getyourguide.com/), [Viator](https://www.viator.com/) | Precio visible + fechas | Comisión y review farming |
| ES/PT | Civitatis / locales Lima | Copy nativo, no Google Translate | Landings Ads genéricas |

No decir en sala “Valencia es mejor”. Sí: *ellos ya emiten entidad; nosotros tenemos tres idiomas y un operador en Cusco — el premio es más grande si el H1 y el WhatsApp coinciden*.

## 10 acciones esta semana (next. + CMS)

1. **Areli / Lizet / Ricardo:** 1 H1 + 1 meta description en *su* parte. El CMS ya tiene contador SEO.
2. **5 tours ES** con incluye/excluye duplicado: limpiar pestaña HTML. El scrape no lo va a arreglar.
3. **Precio:** no inventar. Si el JSON no es de fiar, dejar “Solicitar cotización”. Tarifario Ricardo antes de `precios:apply`.
4. **Inca Trail / Salkantay:** una frase de escasez verdadera (permisos, temporada) en el H1 o el primer párrafo — no “¡oferta!” falso.
5. **WhatsApp:** mensaje prellenado ya sale en ES/PT. No cambiar el número. Medir `whatsapp_click` 7 días.
6. **Blog → tour:** un post ES debe mostrar 2–4 tours *del catálogo ES*. Código listo; revisar slugs basura.
7. **Trust:** RUC, dirección El Sol, “desde 2012” ya están en footer. No añadir sellos inventados.
8. **hreflang:** emitido en tours/blogs/homes de next. No sirve a Google hasta cutover. No perder el tiempo “indexando next.”.
9. **Comparar 4 fichas** (Inca 4D, MP full day, Salkantay, Rainbow) vs Alpaca / un OTA: precio visible, grupo, incluye. Una tabla, no un informe de 20 páginas.
10. **Ads Lizet:** no mandar tráfico de Ads a next. (noindex). Landings siguen en WP hasta cutover.

## GEO / IA (lo mínimo útil)

Cuando un modelo cite operador en Cusco, `llms.txt` ya dice: canónico `www`, WhatsApp para cotizar, no inventar precios. Preview next. está marcado noindex.

Prompt de prueba (hacer 1 vez, anotar): *“best licensed Cusco operator for Salkantay 4 days WhatsApp quote”* — ¿aparece PGT o Alpaca/GYG?

## Hacks que sí (operador licenciado)

- Responder en <2 h en horario Cusco; el copy ya promete “unas horas”. Cumplir.
- Pedir fechas + pax en el primer mensaje (el CTA ya lo pide).
- Mandar 2–3 opciones, no un PDF de 40 tours.
- Nombrar el tour en el wa.me (utm_content ya va en dataLayer).

## Hacks que no

- Fake scarcity (“solo 2 cupos”) si no es verdad.
- Clonar EN a ES para “tener /peru/”.
- Comprar reviews.
- Source maps en producción “para debug LCP”.

## Fuentes

- Alpaca: https://www.alpacaexpeditions.com/
- GYG Perú: https://www.getyourguide.com/peru-l315/
- Viator Machu Picchu: https://www.viator.com/Cusco-tours/Machu-Picchu/d445-g12-c92
- next. CMS: https://next.perugrandtravel.com/admin/
