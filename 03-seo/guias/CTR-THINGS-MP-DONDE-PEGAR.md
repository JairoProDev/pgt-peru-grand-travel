# Things MP — DÓNDE pegar cada cosa (mapa de pantalla)

**URL editor:** https://www.perugrandtravel.com/blog/wp-admin/post.php?post=18674&action=edit

---

## Ya hecho ✅ (no tocar)

| Qué | Dónde en pantalla |
|---|---|
| SEO Title | Barra derecha → Rank Math → preview → ya dice `12 Things to Do...` |
| Meta description | Igual — ya verde |
| Focus keyword | Barra derecha → Rank Math → tag verde |
| Permalink / slug | Rank Math o Permalink debajo del título — `things-to-do-in-machu-picchu` |

---

## Lo que falta — 3 zonas del editor

```
┌─────────────────────────────────────────────────────────────────┐
│  [Edit with Elementor]  [Save]  [Rank Math 86]     [Update]    │
├──────────────────────────────────────┬──────────────────────────┤
│  ZONA A — Título del post (H1)       │  Rank Math (ya listo)   │
│  "Things to Do in Machu Picchu 2026…"│                          │
├──────────────────────────────────────┤                          │
│  ZONA B — Primer párrafo             │                          │
│  "The silence at Machu Picchu..."    │                          │
│  ...resto del artículo...            │                          │
│                                      │                          │
│  ZONA C — Antes de "More information"│                          │
│  (pegar bloque tours aquí)           │                          │
└──────────────────────────────────────┴──────────────────────────┘
```

---

## PASO 1 — ZONA A: Título del post (arriba, letras grandes)

**Dónde:** La caja de texto **más arriba** del artículo (no Rank Math, no Elementor).

**Borra** el título largo y **pega:**

```
12 Things to Do in Machu Picchu (2026)
```

**Por qué:** Ese texto es el **H1** que ve el usuario y Google en la página. Rank Math ya tiene otro title para Google (`...2026 Guide)`); está bien que sean casi iguales.

---

## PASO 2 — ZONA B: Primer párrafo ✅ (ya hecho si ves "Planning your 2026 trip?")

El párrafo original **no** dice "The silence at Machu Picchu". Dice:

> *There is a specific kind of silence that only exists at 2,430 meters...*

Si ya pegaste el párrafo `Planning your 2026 trip?...` **encima** de ese texto → **listo, salta al paso 3**.

---

## PASO 3 — ZONA C: Bloque tours (solo si quieres — el post ya tiene sección "Experiences" al final)

**"More information:"** está al **final del artículo**, después de FAQ y "The Sanctuary Awaits". En el editor: **Ctrl+F** (o Cmd+F) → busca `More information`.

### Método FÁCIL — sin Custom HTML

1. **Ctrl+F** → escribe `The Sanctuary Awaits` → Enter (te lleva casi al final)
2. Clic en el párrafo **justo encima** de ese heading
3. Pulsa **Enter** para línea nueva
4. Clic en **+** (cuadrado azul arriba izquierda, o entre bloques)
5. Busca **Heading** → escribe: `Recommended Machu Picchu Tours from Cusco`
6. **+** otra vez → **Paragraph** → pega:
   `Ready to plan your trip? Our Cusco team helps with trains, tickets, and guided visits — chat on WhatsApp anytime.`
7. **+** otra vez → **List** → añade 4 ítems (cada uno: texto + enlace con el icono 🔗):

| Texto del enlace | URL |
|---|---|
| Classic Machu Picchu 5 Days | `https://www.perugrandtravel.com/tour/classic-machu-picchu-5d/` |
| Salkantay SKY Trek 5 Days | `https://www.perugrandtravel.com/tour/the-classic-salkantay-trek-5d/` |
| Machu Picchu Express 3D/2N | `https://www.perugrandtravel.com/tour/machu-picchu-express-3d/` |
| Incredible Machu Picchu 2D/1N | `https://www.perugrandtravel.com/tour/incredible-machu-picchu-2d/` |

### ¿No encuentras Custom HTML?

Normal en algunos WP. **No lo necesitas** — usa Heading + Paragraph + List como arriba.

### ¿Atascado? Opción mínima

El post **ya** tiene tours al final ("Experiences"). Si estás perdido: **salta el paso 3**, pulsa **Update**, y pide indexación en GSC. Title + meta + H1 + intro ya son el 90 % del win.

---

## PASO 4 — Enlaces internos (sin Link Suggestions)

**Link Suggestions** a veces no aparece (versión Free, otra pestaña, o UI distinta). **No lo busques más.**

### Método manual (2 min) — mejor que el plugin

1. En el editor, **Ctrl+F** → busca: `Classic Machu Picchu 5D` (o `Classic Machu Picchu 5 Days`)
2. Selecciona esas palabras → icono **enlace** (🔗) en la barra del bloque
3. Pega URL: `https://www.perugrandtravel.com/tour/classic-machu-picchu-5d/` → Enter
4. Repite con otra frase, p. ej. cerca de Huayna Picchu / tours:
   - `https://www.perugrandtravel.com/tour/the-classic-salkantay-trek-5d/`
   - `https://www.perugrandtravel.com/tour/machu-picchu-express-3d/`

**Por qué:** Google valora enlaces a páginas de conversión (tours). Rank Math “Link Suggestions” solo automatiza; el resultado es el mismo.

**Si el post ya tiene “Classic Machu Picchu 5D” enlazado** (en tu captura lo está) → **1 enlace interno ya cuenta**. Puedes Update sin más.

---

## PASO 5 — Guardar

**Dónde:** Botón azul **Update** arriba a la derecha (junto a Rank Math 86).

Luego GSC → Inspección URL → Solicitar indexación.

---

## ¿Por qué NO te doy todo el HTML del post?

El artículo tiene ~2.000 palabras, imágenes y bloques de Elementor/Gutenberg. Pegar **todo** el HTML de golpe:

- Rompe bloques existentes
- Pierdes formato e imágenes
- Riesgo alto, beneficio cero

Solo necesitas **3 ediciones quirúrgicas** (título + 1 párrafo + 1 bloque al final). El 95 % del post **no se toca**.
