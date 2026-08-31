# CTR quick win — Things to Do in Machu Picchu (WP prod)

**URL:** https://www.perugrandtravel.com/blog/things-to-do-in-machu-picchu/  
**Fecha guía:** 28 ago 2026  
**Objetivo:** subir CTR desde ~0,02 % hacia **1–2 %** (sin cambiar URL)

---

## La matemática (para que no te engañes ni te desanimes)

| Escenario | CTR | Clics / 28 días (6.115 imp) | vs hoy (1 clic) |
|---|---:|---:|---:|
| **Hoy** | 0,02 % | ~1 | — |
| Realista mes 1 | 0,3–0,5 % | 18–31 | **18–30×** |
| Buen resultado | 1 % | ~61 | **~60×** |
| Stretch (pos ~6) | 2 % | ~122 | **~100×** ✅ |

**Sí: 2 % sería ~100× más clics** que hoy. Es posible en teoría (posición media ~6), pero **no lo prometas en 48 h**. Google tarda **2–4 semanas** en re-rastrear y mostrar el nuevo snippet.

**Meta sensata:** apuntar a **0,5 % en 30 días** (≈30 clics/mes) y revisar. Si llegas a 1 %, ya es un win enorme para Clever.

---

## Por qué hoy casi nadie hace clic

1. **Title demasiado largo** — Google lo corta y pierde el gancho  
   Actual (~85 caracteres):  
   `Things to Do in Machu Picchu 2026: All The Experiences You Should Know About | Travel guide`

2. **Meta genérica** — “unforgettable journey” no dice *qué* van a ver

3. **Posible canibalización** — existe también  
   `/blog/cusco/things-to-do-in-machu-picchu/` (misma intención, otra URL)

---

## Paso a paso en WordPress (30–45 min)

### 1. Entrar a editar el post

1. **https://www.perugrandtravel.com/blog/wp-admin/** (no el `/wp-admin/` principal — ahí hay 0 posts)
2. **Posts** → buscar **“Things to Do in Machu Picchu”**  
   O enlace directo: `.../blog/wp-admin/post.php?post=18674&action=edit`
3. Slug: `things-to-do-in-machu-picchu`

### 2. Rank Math SEO — pegar title y meta (no Yoast)

Clic en **Rank Math** (score arriba derecha) → **Edit Snippet**:

Copy/paste completo: `03-seo/guias/CTR-THINGS-MP-COPY-PASTE.md`

| Campo | Valor a pegar | Chars |
|---|---|---:|
| **SEO title** | `12 Things to Do in Machu Picchu (2026 Guide)` | ~43 |
| **Meta description** | `Sunrise at the citadel, Huayna Picchu hike, Machu Picchu Mountain, tickets & how to get there — local tips for 2026. Plan with Peru Grand Travel.` | ~155 |

**Alternativa title** (si prefieres keyword exacta primero):  
`Things to Do in Machu Picchu 2026: 12 Best Experiences` (~52 chars)

Yoast semáforo: busca **verde** en title y meta. Si title sale naranja por “keyword al inicio”, está bien — prioriza legibilidad en SERP.

### 3. H1 del artículo (en el contenido, no solo Yoast)

El **H1 visible** debe coincidir o ser muy parecido al title. Sugerido:

```text
12 Things to Do in Machu Picchu (2026)
```

No dejes un H1 larguísimo distinto del title.

### 4. Primer párrafo (2 min)

Añade o ajusta las **primeras 2 líneas** para que incluyan:

- “things to do in Machu Picchu”
- año 2026
- 1 beneficio concreto (ej. “sunrise”, “Huayna Picchu tickets”)

Ejemplo:

> Planning your visit in 2026? Here are the **12 best things to do in Machu Picchu** — from sunrise at the Sun Gate to Huayna Picchu and the best time to buy tickets.

### 5. Enlaces internos (10 min) — sube CTR *y* conversión

Al final del post (o en un bloque “Recommended tours”), añade **3 enlaces** con texto descriptivo:

| Anchor (texto del enlace) | URL |
|---|---|
| Salkantay Trek 5 Days to Machu Picchu | `/tour/the-classic-salkantay-trek-5d/` |
| Machu Picchu Express 3D/2N | `/tour/machu-picchu-express-3d/` *(confirmar slug en WP)* |
| Incredible Machu Picchu 2D/1N | `/tour/incredible-machu-picchu-2d/` *(confirmar slug)* |

**No uses** “click here”. Usa el nombre del tour.

### 6. WhatsApp / CTA

Confirma que el botón **click-to-chat** sigue visible (ya estaba en auditoría). No lo quites.

### 7. Publicar

- **Actualizar** el post (no hace falta cambiar fecha si WP lo permite sin “republicar”)
- Si Yoast pregunta “¿reindexar?” → sí / guardar

### 8. Pedir re-rastreo en GSC (2 min)

1. Search Console → **Inspección de URLs**
2. Pegar: `https://www.perugrandtravel.com/blog/things-to-do-in-machu-picchu/`
3. **Solicitar indexación**

---

## Ver el snippet antes/después (5 min)

1. Google en incógnito: `site:perugrandtravel.com things to do machu picchu`
2. Captura cómo se ve el resultado **antes** del cambio (si aún no cambiaste)
3. Repite en **7–14 días** después del cambio

Opcional: https://search.google.com/test/rich-results → pegar URL → validar Article schema.

---

## Canibalización — ✅ ya resuelta (28 ago)

`/blog/cusco/things-to-do-in-machu-picchu/` redirige **301** a la URL principal. No requiere acción.

---

## Cómo medir éxito (cada lunes)

GSC → Rendimiento → **28 días** → filtro **Página exacta**:

`https://www.perugrandtravel.com/blog/things-to-do-in-machu-picchu/`

| Semana | Impresiones | Clics | CTR | Nota |
|---|---:|---:|---:|---|
| Baseline 27 ago | 6.115 | 1 | 0,02 % | xlsx guardado |
| +1 sem | | | | |
| +2 sem | | | | |
| +4 sem | | | | meta 0,5 %+ |

Copia fila a `03-seo/datos/CTR-THINGS-MP-seguimiento.csv` (crear si quieres).

---

## Checklist rápido

- [ ] Title Yoast ≤ 60 caracteres
- [ ] Meta 150–160 caracteres, con lista concreta
- [ ] H1 alineado al title
- [ ] 3 enlaces internos a tours
- [ ] WA visible
- [ ] Actualizar post
- [ ] GSC solicitar indexación
- [ ] Revisar URL duplicada `/blog/cusco/...`
- [ ] Captura snippet Google (antes)
- [ ] Anotar en `HECHOS.md` fecha del cambio

---

## Qué decirle a Clever (una línea)

> Optimicé title/meta del blog Things MP (6k imp/mes, CTR 0,02 %). Objetivo 0,5–1 % en 30 días = decenas de clics extra sin Ads.

---

*Relacionado:* `03-seo/auditorias/blog-things-to-do-in-machu-picchu.md` · inventario P0 en `03-seo/datos/`
