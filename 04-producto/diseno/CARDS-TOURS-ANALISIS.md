# Análisis: cards de tours — PGT web vs Drupal staging

> Norte: **leads calificados por WhatsApp**, no clics a “Explore more”.  
> Fecha: 2026-08-31

---

## Comparativa rápida

| Criterio | **Drupal (referencia)** | **PGT anterior** | **PGT v2 (implementado)** |
|----------|-------------------------|------------------|---------------------------|
| CTA principal | “Explore more” → ficha | 2 botones iguales (itinerario + WA) | **1 CTA WA ancho** + link texto itinerario |
| Precio visible | ✅ From $X /person | ✅ From US$ | ✅ + microcopy confianza |
| Meta scannable | ✅ duración, dificultad, rating | ⚠️ solo duración duplicada en título | ✅ duración · estilo · dificultad |
| Descripción | ✅ 2 líneas hook | ❌ bullets crudos del scrape | ✅ summary + chips |
| Destinos | ✅ breadcrumb visual | ❌ | ✅ overlay en imagen |
| Badge | “Best Seller” | ❌ | ✅ solo lista curada (honesto) |
| Rating ★ 4.9 | ✅ | ❌ | ❌ **no fake** — pendiente TripAdvisor real |
| Imagen | ✅ hero grande | ✅ | ✅ next/image + hover |
| Confianza WA | ❌ | ⚠️ implícita | ✅ “No booking fee to ask” |

---

## Drupal — qué hace bien

1. **Jerarquía visual clara** — imagen → meta → título → hook → precio → CTA.
2. **Metadata en fila** — duración, dificultad, rating: el usuario escanea en 2 s.
3. **Descripción comercial** — 2 líneas orientadas a beneficio, no lista técnica.
4. **Precio anclado** — “From $X /person” antes del botón.
5. **Badge Best Seller** — ancla atención (si es verdad).

## Drupal — qué hace mal (para nuestro norte)

1. **“Explore more” no convierte a WA** — envía a otra página; fricción extra; no mide lead directo.
2. **Rating 4.9 (312) probablemente placeholder** — mismo número en 3 cards distintas en captura = **mala práctica** / riesgo legal.
3. **Imágenes incorrectas** — card Inca Trail con foto de ciudad europea; card “Premium” con costa genérica → destruye confianza.
4. **Inconsistencia título vs meta** — “8D/7N” en título pero “5 Days / 4 Nights” en meta.
5. **Destinos genéricos repetidos** — “Peru, Cusco, Machu Picchu, Sacred Valley” en todos igual.
6. **CTA naranja compite con marca WA** — usuario acostumbrado a verde WhatsApp en PGT.

---

## PGT anterior — qué hacía bien

1. **Dual intención reconocida** — algunos quieren leer, otros cotizar.
2. **WhatsApp visible** — verde, icono, tracking `card_{slug}`.
3. **`isTrustedPrice`** — no muestra $16 en tour 10D.
4. **Precio naranja/azul** según confianza del dato.

## PGT anterior — qué hacía mal

1. **Dos botones mismo peso** — “Full itinerary” compite con “Get quote”; en mobile el verde no domina.
2. **Highlights = scrape crudo** — “Day 1: Snack every day…” ilegible en card.
3. **Título + duración duplicados** — “7D/6N” dos veces.
4. **Sin hook emocional** — no summary, no destinos, no estilo (trek vs package).
5. **Sin badge** para best sellers reales.
6. **`background-image`** — peor LCP que `next/image`.

---

## Diseño superior PGT v2 — principios

1. **Una acción primaria por card:** `Get quote on WhatsApp` a ancho completo.
2. **Itinerario = link secundario** — para investigadores, no compite visualmente.
3. **3 segundos de valor:** destinos en foto + meta row + precio.
4. **Confianza sin mentir:** no rating hasta tener número TripAdvisor verificado por Ops.
5. **Best seller solo en slugs curados** (`tour-card.ts` → GSC/hub).
6. **Chips derivados de includes reales** — “Lodging included”, “Machu Picchu”, etc.
7. **Microcopy anti-fricción:** “English support · No booking fee to ask”.

Implementación: `TourPackageCard.tsx`, `src/lib/tour-card.ts`.

---

## Malas prácticas a evitar siempre

- ★ rating inventado o copiado de otra ficha  
- Dos CTAs primarios del mismo tamaño  
- “Explore more” / “Learn more” sin camino a WA  
- Precio sin moneda o sin “from”  
- Imagen que no corresponde al producto  
- Texto largo del scrape en la card  
- Pop-ups o badges falsos de “Limited spots”  

---

## Métricas a medir post-deploy

| Evento | Dónde |
|--------|-------|
| `whatsapp_click` utm `card_{slug}` | GTM → GA4 |
| CTR card → `/tour/` (link itinerario) | GA4 path |
| Scroll depth hub `/packages/` | GA4 |
| WA users/mes hub vs home | baseline 28% packages |

**Hipótesis:** subir WA/card 15–30% vs dual-button al eliminar competencia visual.

---

## Pendiente (fase 2)

- [ ] Rating real TripAdvisor cuando Ops confirme número  
- [ ] A/B label WA: “Get quote” vs “Check dates & price”  
- [ ] Imágenes locales `/public/` (no hotlink WP)  
- [ ] Card compacta en RelatedTours (misma jerarquía)
