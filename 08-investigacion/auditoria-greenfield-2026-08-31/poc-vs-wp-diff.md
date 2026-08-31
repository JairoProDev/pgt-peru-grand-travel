# POC vs WordPress — diferencias clave (MVP)

**Fecha:** 2026-08-31  
**URLs comparadas:** Tour Salkantay 5D, Blog Things MP

## Resumen

| Dimensión | WordPress prod | POC Next.js | Greenfield target |
|---|---|---|---|
| Lighthouse mobile | 55 | 100 | 95+ |
| LCP | 6,8s | 1,4s | <2,5s |
| HTML payload | ~211 KB | ~80 KB | <100 KB |
| JSON-LD | Product parcial | TouristTrip + Product + FAQ | Completo por tipo |
| CTA principal | Cart + WA compiten | Solo WA | Solo WA + sticky |
| Nav items | 30+ (mega-menú) | 5 links | 5 links |
| Analytics | GTM-K8SZBJM5 (plugin chat) | GA4 directo POC | GTM prod + dataLayer |
| Trailing slash | Sí | No (bug POC) | Sí (paridad WP) |
| Font | Poppins 100–900 | system-ui | Poppins 400/600/700 |
| Blog → tours | No | Link interno 1 | Bloque RelatedTours min 3 |

## Qué portar del POC

- Patrones JSON-LD (`TouristTrip`, `Product`, `Offer`, `FAQPage`, `BlogPosting`)
- UTM + prefill WA (`utm_source=web`, no `poc_web`)
- `remotePatterns` para imágenes WP en `next.config.ts`
- Contenido JSON scrapeado (Salkantay, Things MP)

## Qué NO portar del POC

- Rutas estáticas por carpeta (usar `[slug]` dinámico)
- GA4 hardcodeado sin GTM
- `robots` allow index (beta = noindex)
- Fuente system-ui
- Label "POC" en metadata

## Ventaja greenfield vs WP (embudo)

1. **Un CTA** — elimina fricción cart vs WhatsApp
2. **Hubs prioritarios** — packages/machu-picchu-packages como landings de ads
3. **Blog comercial** — tours relacionados + CTA visible (WP: 2% WA en blogs)
4. **Medición unificada** — `whatsapp_click` en dataLayer comparable a `chat:51946622318`
5. **Velocidad** — 70%+ tráfico mobile; LCP <2,5s = menos abandono pre-WA
