# Twig explicado despacio (no “Twing”)

Nombre correcto: **Twig**.  
Se pronuncia parecido a “tuig” / “twig” en inglés (ramita).

---

## 1. ¿Qué problema resuelve Twig?

Tienes datos (título del tour, precio, imagen) en la base de datos.  
Necesitas **HTML** para el navegador.

Opciones:

| Enfoque | Ejemplo |
|---|---|
| Mezclar PHP y HTML a mano | `<?php echo $title; ?>` dentro del HTML (temas WP viejos) |
| **Twig** | Plantilla limpia: `{{ label }}` |

Twig = motor de plantillas: archivos `.html.twig` que dicen **dónde** va cada dato.

**No** es un CMS.  
**No** reemplaza Drupal.  
**No** es JavaScript.  
Es la **capa de presentación** del tema Drupal.

---

## 2. Analogía

- **Node / campos** = ingredientes en la nevera (precio, título).  
- **Twig** = la receta escrita: “pon el título en un H1, el precio en un párrafo, el botón aquí”.  
- **CSS** = el emplatado visual (colores, tipografía).  
- **Navegador** = el comensal.

Cuando el jefe de marketing diga “en Figma el precio va a la derecha”, alguien (o tú conmigo) lo baja a **Twig + CSS**, no a “un plugin Yoast”.

---

## 3. Un ejemplo mínimo real

Archivo típico: `node--tour.html.twig`  
(significa: plantilla para nodes del tipo tour)

```twig
{# Esto es un comentario en Twig #}
<article class="tour">
  <h1>{{ label }}</h1>

  {# content.field_price es el campo "precio" renderizado #}
  <div class="price">
    {{ content.field_price }}
  </div>

  <a class="btn-wa" href="{{ content.field_whatsapp.0['#url'] }}">
    WhatsApp
  </a>

  {{ content.body }}
</article>
```

Qué debes entender (no memorizar sintaxis aún):

- `{{ ... }}` = “imprime esto”  
- `{% ... %}` = lógica (if, for)  
- `label` = título del node  
- `content.campo` = el campo tal como Drupal lo preparó para mostrar  

---

## 4. Twig vs “código propio”

| Hacer en Twig | Mejor en módulo PHP |
|---|---|
| Orden de bloques, HTML, clases CSS | Reglas complejas, APIs, Migrate |
| Mostrar u ocultar un bloque simple | Schema JSON-LD muy custom (a veces Twig también) |
| CTA WhatsApp si el link ya es un campo | Calcular descuentos raros |

**Sí puedes poner código propio en Drupal:** tema (Twig/CSS/JS) + módulos PHP. Twig es la parte más visible del “código propio” del diseño.

---

## 5. Qué oirás en la reunión

| Frase | Significado |
|---|---|
| “Hay que ajustar el Twig del tour” | Cambiar la plantilla HTML de la ficha |
| “Eso está hardcodeado en Twig” | Texto fijo en la plantilla (malo si marketing debe editarlo → mejor campo) |
| “Preprocess en el `.theme`” | PHP que prepara variables antes de Twig |
| “Herencia de plantillas” | Un Twig base (`page.html.twig`) y otros que lo extienden |

---

## 6. Qué preguntar tú

> “¿El precio y el WhatsApp salen de campos editables o están fijos en el Twig?”  
> “¿Puedo ver el `node--tour.html.twig` en staging o en el repo?”

Si te muestran el archivo, pégalo en el chat (sin secrets) y lo leemos juntos línea a línea.

---

## 7. Mini práctica (15 min, cuando tengas staging)

1. Abre una ficha tour en el sitio.  
2. Clic derecho → “Ver código fuente”.  
3. Busca el H1 y el precio.  
4. Pregunta a Ricardo: “¿Qué archivo Twig genera este H1?”  

Eso conecta teoría con realidad.

---

## 8. Relación con no matar leads

Twig mal hecho puede:

- Olvidar el botón WhatsApp  
- Poner el precio solo en imagen (Google no lo lee)  
- Cargar 50 JS (lento → rebote)  

Twig bien hecho = ficha clara, rápida, con CTA y schema.  
Por eso te importa aunque no seas “el frontender oficial”.
