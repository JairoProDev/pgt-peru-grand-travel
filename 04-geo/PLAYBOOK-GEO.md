# GEO — Generative Engine Optimization para PGT

GEO no es un rebranding de SEO. SEO te pone en diez enlaces. GEO te pone **dentro de la respuesta** de ChatGPT, Gemini, Perplexity y los AI Overviews de Google.

El aviso dice SEO/GEO. Mañana puedes ser la única persona en esa oficina que distingue los dos sin humo.

## Por qué le importa a un operador de Cusco

Más del 40% de viajeros (Phocuswright 2025, citado en literatura de tours 2026) **empieza** a planear con IA. AI Overviews aparecen en ~30% de queries de travel (cifras de mercado 2026: úsalas como orden de magnitud, no como KPI interno).

Si alguien pregunta *“best Inca Trail operator from Cusco that is licensed”* y la IA cita Viator o Valencia, PGT no existe. La comisión de GYG se vuelve el default.

Mismo argumento de siempre: **canal propio, margen**. Solo cambia la puerta de entrada.

## Qué hace que una IA cite a un operador

1. **Hechos extraíbles** al inicio de la ficha, no prosa de “unforgettable”.
2. **Schema** de turismo: `TravelAgency`, `TouristTrip` / Product+Offer con moneda, FAQPage, AggregateRating **por tour**.
3. **Corroboración externa**: Tripadvisor, Google Business, lista SERNANP, PromPerú, prensa. Las IAs confían más en reseñas y listados que en el copy de la home.
4. **Consistencia de entidad**: mismo nombre, dirección, teléfono, en web, GBP, GYG, TA.
5. **Crawlers de IA no bloqueados** (WAF + robots). PGT ya da 406 a UA raros: hay que **medir** si GPTBot entra, no asumir.
6. **Contenido fresco** con números (precio, cupos, circuitos 2026). Contenido de hace un año se cita menos.

## Qué no es GEO

- “Escribir para ChatGPT” con tono robot.
- Pagar un saaaS milagroso de “AI rank” el mes 1.
- Bloquear GPTBot “por seguridad” y luego quejarse de que no te mencionan.
- Copiar la ficha de Viator: la IA citará Viator.

## Auditoría GEO de línea base (semana 1–2)

Elige 15 prompts, 3 motores (ChatGPT, Gemini/Google AIO, Perplexity). Tabla:

| Prompt | ¿Sale PGT? | ¿Quién sale? | Fuente citada | Idioma de la respuesta |
|---|---|---|---|---|
| best licensed Inca Trail operator Cusco | | | | |
| Inca Trail vs Salkantay which to book | | | | |
| Machu Picchu full day from Cusco price | | | | |
| pacote Machu Picchu 5 dias Brasil | | | | |
| tour Machu Picchu 1 giorno da Cusco | | | | |
| Rainbow Mountain tour altitude | | | | |
| Salkantay trek 5 days licensed | | | | |
| luxury Machu Picchu tour Peru | | | | |
| Short Inca Trail 2 days permits | | | | |
| melhor agência Machu Picchu Cusco | | | | |
| Valencia Travel vs Peru Grand Travel | | | | |
| GetYourGuide Machu Picchu Cusco | | | | |
| Camino Inca operadores autorizados | | | | |
| mal de altura Cusco primer día | | | | |
| Palccoyo vs Vinicunca | | | | |

No hace falta tool de pago el día 1. Capturas + hoja. Eso **es** el entregable GEO del mes 1. Nadie del equipo lo tiene.

Repite a 30 y 90 días. KPI: *share of mention*, no posición Google.

## Quick wins GEO que no pisan al equipo

| Win | Quién | Esfuerzo |
|---|---|---|
| Capsula factual al tope de 10 fichas estrella (duración, precio, idioma guía, grupo máx, punto de encuentro) | Tú + Mkt | M |
| `TravelAgency` + dirección + sameAs (TA, GBP, IG, Facebook BR) | Tú | S |
| FAQ real por tour (3–5 preguntas de viajero) + FAQPage | Mkt redacta, tú marcas | M |
| Página de licencia Camino Inca con enlace a lista oficial | Ops valida, Mkt, tú | M |
| Revisar robots/WAF para GPTBot, PerplexityBot, Google-Extended | Sis + tú | M |
| `llms.txt` en los 4 dominios (qué son, destinos, booking directo) | Tú, Sis sube | S |
| No copiar AggregateRating de empresa en cada ficha | Tú | — (prohibición) |

## Copy que sí extrae una IA vs el que no

No: *Welcome to our amazing adventure. Our passionate team…*

Sí: *Classic Inca Trail 4 days is operated by Peru Grand Travel Group S.A.C., an authorized Inca Trail operator. Daily hiking 6–12 km, max altitude 4,215 m (Dead Woman’s Pass), small groups with English- or Spanish-speaking guide. Permits sell out months ahead for June–August. Direct booking on this page; WhatsApp for custom dates.*

Eso lo puede citar un modelo. Lo otro, no.

## Relación con ads y CM

GEO no sustituye Meta. El viajero de Meta a menudo ya decidió destino. El de ChatGPT está 2–6 meses antes. Contenido EN/IT + schema + reseñas es la misma guerra en dos frentes. Dilo así al equipo: *ustedes ya consiguen reseñas; GEO es cobrarlas también frente a la IA, no solo en el widget.*

## Lecturas

- [GEO for tour operators, 2026](https://hamzaliaqat.com/blog/geo-strategy-2026)
- [GEO travel/hospitality playbook](https://astral3.io/blog/geo-for-travel/)
- [Sojern GEO for destinations](https://www.sojern.com/blog/a-complete-guide-to-generative-engine-optimization-for-dmos)

No las imprimas para Clever. Ejecuta la tabla de 15 prompts.
