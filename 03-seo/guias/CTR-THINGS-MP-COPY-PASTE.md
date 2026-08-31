# Things MP — copy/paste (Rank Math + bloques)

**Post ID:** 18674  
**Editor:** https://www.perugrandtravel.com/blog/wp-admin/post.php?post=18674&action=edit  
**Plugin SEO:** Rank Math (no Yoast)

---

## 1. Rank Math — pegar tal cual

Clic en **Rank Math** (arriba derecha, 87/100) → pestaña **General** o **Edit snippet**:

**Focus Keyword:**
```
things to do in machu picchu
```

**SEO Title:**
```
12 Things to Do in Machu Picchu (2026 Guide)
```

**Meta description:**
```
Things to do in Machu Picchu in 2026: sunrise, Huayna Picchu hike, tickets & how to get there. Local tips from Peru Grand Travel.
```

---

## 2. Título del post (arriba del editor = H1)

Reemplaza el título largo por:

```
12 Things to Do in Machu Picchu (2026)
```

*(No cambies el slug `things-to-do-in-machu-picchu`)*

---

## 3. Primer párrafo — reemplazar texto

Busca el párrafo que empieza con *"The silence at Machu Picchu..."* y **añade al inicio** (o reemplaza el primer párrafo por):

```
Planning your 2026 trip? Here are the best things to do in Machu Picchu — from sunrise at the Sun Gate to Huayna Picchu, Machu Picchu Mountain, and how to buy tickets before they sell out.

The silence at Machu Picchu is not empty; it is full of history...
```

*(Mantén el resto del párrafo si quieres — lo importante es la primera línea con keyword + 2026.)*

---

## 4. Bloque nuevo — tours (antes de "More information")

**Opción A — Visual:** `+` → bloque **Heading** + **List**  
**Opción B — Code editor:** pega esto **antes** del bloque `More information:`

```html
<!-- wp:heading -->
<h2 class="wp-block-heading">Recommended Machu Picchu Tours from Cusco</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Ready to plan your trip? Our Cusco team helps with trains, tickets, and guided visits — chat on WhatsApp anytime.</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li><a href="https://www.perugrandtravel.com/tour/classic-machu-picchu-5d/">Classic Machu Picchu 5 Days</a> — popular multi-day route to the citadel</li>
<li><a href="https://www.perugrandtravel.com/tour/the-classic-salkantay-trek-5d/">Salkantay SKY Trek 5 Days</a> — trek the Andes to Machu Picchu</li>
<li><a href="https://www.perugrandtravel.com/tour/machu-picchu-express-3d/">Machu Picchu Express 3D/2N</a> — ideal if you are short on time</li>
<li><a href="https://www.perugrandtravel.com/tour/incredible-machu-picchu-2d/">Incredible Machu Picchu 2D/1N</a> — Sacred Valley + Machu Picchu by train</li>
</ul>
<!-- /wp:list -->
```

---

## 5. Rank Math — enlaces internos (sidebar)

En **Link Suggestions**, enlaza desde este post hacia (elige 2–3):

- 7 Travel Planning Tips for Machu Picchu 2026
- Machu Picchu Tours from Cusco: Best Routes
- The ultimate Inca Trail to Machu Picchu Guide 2026

Anchor natural en una frase del artículo (no "click here").

---

## 6. Publicar

1. **Update** (arriba derecha)
2. GSC → Inspección URL → solicitar indexación
3. Anotar en HECHOS: fecha del cambio

---

## Canibalización — ya resuelta ✅

`/blog/cusco/things-to-do-in-machu-picchu/` → **301** a `/blog/things-to-do-in-machu-picchu/`  
No hagas nada extra ahí.
