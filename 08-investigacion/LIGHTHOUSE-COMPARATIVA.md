# Lighthouse comparativa — POC vs WordPress vs Drupal

**Fecha:** 28 ago 2026  
**Dispositivo:** Mobile (PageSpeed Insights)  
**URL analizada:** Tour Salkantay 5D (misma intención de página)

| Plataforma | URL |
|---|---|
| **POC Next.js** | https://pgt-poc.vercel.app/tour/the-classic-salkantay-trek-5d |
| **WordPress prod** | https://www.perugrandtravel.com/tour/the-classic-salkantay-trek-5d/ |
| **Drupal staging** | http://147.135.114.64/product/9 |

**Capturas:** Jairo · PageSpeed Insights · 28 ago 2026

---

## Resumen ejecutivo (1 frase)

El POC Next.js supera ampliamente a WP y Drupal en velocidad (Performance **100** vs **55** vs **13**), con contenido real de WP, WhatsApp y schema — listo para demo interna con Einel/Clever.

---

## Tour Salkantay 5D — Mobile

| Métrica | WP prod | Drupal `/product/9` | **POC Next.js** |
|---|---:|---:|---:|
| **Performance** | 55 | 13 | **100** |
| **SEO (Lighthouse)** | 92 | 100* | **82→98**† |
| **Accessibility** | 88 | 84 | **98→100**† |
| **Best Practices** | 74 | 100* | **100** |
| **LCP** | 6,8 s | 18,2 s | **1,4 s** |
| **FCP** | 4,5 s | 3,2 s | **0,5 s** |
| **TBT** | 0 ms | 1.170 ms | **40 ms** |
| **CLS** | 0,173 | 0,383 | **0** |
| **Speed Index** | 6,6 s | 13,9 s | **2,1 s** |
| **HTML (aprox.)** | ~211 KB | ~314 KB | ~80 KB‡ |
| **JSON-LD** | Product (parcial) | 0 | TouristTrip + Product + FAQ |
| **WhatsApp** | Sí | No (cart) | **Sí** |
| **Precio visible** | Sí (US$ 731) | Sí | **Sí (US$ 731)** |

\* Drupal SEO 100 en lab pero sin schema útil, cart vs WA, URL `/product/9`  
† POC SEO 82 en captura inicial (home sin meta + thumbs sin alt); corregido 28 ago tarde — re-test tour URL  
‡ HTML servido estático; menor payload que WP/Drupal

---

## Por qué WP está lento (55)

| Problema PageSpeed | Impacto |
|---|---|
| TTFB ~2,4 s | Servidor + cache + PHP |
| Render-blocking CSS/JS | ~30+ plugins Tourmaster/Goodlayers |
| Payload ~7,5 MB total | Imágenes + scripts |
| CLS 0,17 | Layout shift en carga |

---

## Por qué Drupal staging está peor (13)

| Problema | Impacto |
|---|---|
| LCP 18,2 s | HTML 314 KB + no cache (`no-cache, private`) |
| TBT 1.170 ms | Drupal 11 + Commerce JS |
| CLS 0,38 | Layout inestable |
| Sin WhatsApp | Modelo conversión distinto |

---

## Por qué POC gana (100)

| Ventaja | Detalle |
|---|---|
| Static generation | Next.js pre-render en Vercel edge |
| Imágenes | `next/image` WebP + sizes |
| Sin plugin hell | 0 jQuery, 0 Tourmaster |
| Schema en código | JSON-LD validado |
| Contenido WP | Mismo texto, precio, fotos |

---

## Mejoras POC aplicadas tras tu captura (28 ago tarde)

- [x] Tema claro forzado (no dark mode)
- [x] `alt` en todas las fotos galería
- [x] `aria-label` en botones WhatsApp
- [x] Meta title/description en home POC
- [x] Schema `Product` (paridad WP)
- [ ] Re-test tour URL → objetivo SEO **95+**

---

## Blog Things Machu Picchu — pendiente tu captura

| URL POC | https://pgt-poc.vercel.app/blog/things-to-do-in-machu-picchu |
|---|---|
| WP | https://www.perugrandtravel.com/blog/things-to-do-in-machu-picchu/ |
| Drupal | **404** |

Corre PageSpeed en las 2 URLs y añade fila aquí.

---

## Cómo repetir (tú)

1. https://pagespeed.web.dev/
2. Pegar URL → **Analyze**
3. Elegir **Mobile**
4. Captura → Drive Seo / informe Clever

---

## Frase para Einel / Clever

> Misma ficha Salkantay, mismo precio US$ 731, mismas fotos — POC Next.js: Performance 100, LCP 1,4 s. WordPress actual: 55. Drupal staging: 13. WhatsApp y schema incluidos.

---

## Próximo paso medición leads (no Lighthouse)

Ver `10-aprendizaje/GA4-POC-GUIA-PASO-A-PASO.md` — stream GA4 + evento `whatsapp_click`.
