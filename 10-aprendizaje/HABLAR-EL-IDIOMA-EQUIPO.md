# Hablar el idioma del equipo (migración) — 26 ago ~9:30

**Quiénes son 5:** tú + Ricardo + Lizet + Arely + jefe de marketing.  
**Objetivo en mesa:** entender lo que digan, hacer 1–2 preguntas inteligentes, no fingir maestría en Drupal.

Si una palabra te suena a chino, di:

> “Para asegurarme: ¿con eso te refieres a [repite en tus palabras]? ¿Y eso afecta las URLs que ya están en Google?”

Eso suena a profesional, no a perdido.

---

## 1. Mapa mental en 60 segundos

Imagina el sitio web como un **restaurante**:

| Parte | Analogía | En PGT hoy (WordPress) | En destino (Drupal) |
|---|---|---|---|
| Cocina / datos | Ingredientes y recetas | Base de datos + Tourmaster | Content types + campos |
| Mesero / panel | Quién anota el pedido | `wp-admin` | Admin Drupal `/admin` |
| Plato servido | Lo que ve el cliente | Página HTML del tour | Misma idea, otro motor |
| Carta / menú | URLs y nombres de platos | Permalinks | Aliases |
| Traductor | Idiomas | 4 WordPress distintos | Traducciones / Domain |
| Google | Crítico gastronómico | Ya conoce las URLs viejas | Debe encontrar las nuevas sin 404 |

**Matar rankings** = Google llega al local y el plato ya no está (404) o está en otra dirección sin aviso (sin 301).  
**Matar leads** = el viajero no encuentra WhatsApp, el precio, o Ads aterriza en error.

---

## 2. Diccionario para la reunión (explicado de verdad)

### URL / permalink / alias / slug

- **URL:** la dirección completa. Ejemplo: `https://www.perugrandtravel.com/tour/salkantay-trek-4-days/`
- **Slug:** la última parte bonita: `salkantay-trek-4-days`
- **Permalink (WordPress):** “enlace permanente” = esa URL estable. Si la cambias, Google se pierde salvo que redirijas.
- **Alias (Drupal):** lo mismo: el nombre legible de la página (no el número interno `node/123`).

**Pregunta útil:**  
> “¿Los aliases de Drupal van a ser iguales a los permalinks actuales, o vamos a redirigir?”

### Redirect / 301 / 302 / 404

- **404:** “no existe”. Malo si era una URL con clics.
- **301:** “se mudó para siempre a esta otra URL”. Google transfiere (casi) el historial. **Es lo que quieres en migración.**
- **302:** “mudanza temporal”. Google duda; **no uses 302 para migración permanente.**
- **Redirect:** la regla automática que hace ese 301.

**Pregunta útil:**  
> “¿Quién carga el mapa de 301? ¿Módulo Redirect? ¿Tenemos CSV de origen→destino?”

### Staging / producción / local

- **Producción (prod):** el sitio real que ve el mundo. `perugrandtravel.com`
- **Staging (demo/preprod):** copia de prueba. Ahí se rompe sin quemar clientes. Ej. `demo.perugrandtravel.com`
- **Local:** en tu laptop (más adelante).

**Regla de oro:** nunca “probar” borrando cosas en producción.  
**Pregunta útil:**  
> “¿La URL de staging ya está en noindex para que Google no la indexe?”

### noindex

Instrucción: “Google, no muestres esta página en resultados.”  
Staging **debe** llevar noindex. Producción de tours **no**.

### Node / content type / campo (Drupal)

- **Content type:** el “molde”. Ej. molde `Tour`, molde `Article` (blog).
- **Node:** **una** pieza hecha con ese molde. El Salkantay 4 días = **un node** de tipo Tour. El blog de Humantay = **un node** de tipo Article.
- **Campo (field):** un dato del molde: precio, duración, imagen, WhatsApp.

En WordPress, “Custom Post Type `tour`” ≈ content type. Cada tour publicado ≈ node.

### Twig (no “Twing”)

**Twig** es el lenguaje de **plantillas** de Drupal (y de Symfony).  
No es la base de datos. Es el archivo que dice: “pon el título aquí, el precio allá, el botón de WhatsApp acá”.

Analogía: el **diseño del plato** (cómo se presenta). Los ingredientes son los campos del node.

Ejemplo mental:

```twig
<h1>{{ label }}</h1>   {# título del tour #}
<p>{{ content.field_price }}</p>
```

Cuando digan “hay que tocar el Twig del tour”, significa: **editar la plantilla visual de la ficha**, no el precio en sí (el precio está en el campo del node).

### Tema (theme) vs módulo (module)

- **Tema:** ropa / diseño (HTML, CSS, Twig, JS de presentación).
- **Módulo:** función (redirects, SEO metatags, migrar datos). Como un “plugin” de WordPress.

### Plugin (WordPress) / módulo (Drupal)

Paquete de código que añade funciones.  
**Yoast** = plugin SEO de WordPress (títulos, meta, sitemaps, algo de schema).  
En Drupal lo equivalente se arma con módulos: **Metatag**, **Pathauto**, **Redirect**, etc.

### Tourmaster / Goodlayers (su WP actual)

- **Tourmaster:** el plugin que crea los tours (no son “posts de blog” normales).
- **Goodlayers:** el constructor visual del diseño (muchas cajas, CSS/JS pesado).

Por eso migrar no es “copiar y pegar”: hay que **recrear** tours en Drupal.

### Composer / Drush

- **Composer:** instalador de dependencias PHP (como npm en JS). Con él se instala Drupal y módulos oficiales.
- **Drush:** terminal de Drupal. Comandos tipo “limpia caché”, “importa config”. Como WP-CLI en WordPress.

Si dicen `drush cr` = “clear cache / rebuild” = refrescar para ver cambios.

### Schema / Offer / priceCurrency

**Schema** = datos estructurados (JSON-LD) para que Google entienda “esto es un producto/tour, cuesta X, moneda USD”.  
Si está mal, no “rompe” el sitio, pero pierdes rich results y claridad.  
`priceCurrency` = moneda del precio (problema histórico en PGT).

### Hreflang

Señal: “esta página en inglés tiene su hermana en portugués aquí”.  
Sin eso, Google muestra el idioma equivocado → **leads mal calificados**.

### GSC (Google Search Console)

Panel de Google: qué URLs tienen clics/impresiones, errores, sitemaps.  
**Tu arma** para demostrar que la migración no mató tráfico.

### CTA / WhatsApp

**CTA** = call to action = el botón/enlace que quieres que pulsen (WhatsApp).  
Si en Drupal la ficha queda bonita pero sin WA claro → **matas leads** aunque rankees.

### Cutover

El momento del cambio: apagas (o dejas de servir) WordPress y enciendes Drupal para el mundo.  
Día D.

---

## 3. Frases que oirás y qué significan

| Dicen | Traducción |
|---|---|
| “Hay que mapear los CPT” | Pasar tours de Tourmaster a content type Tour |
| “Pathauto genera el alias” | Drupal inventa la URL según un patrón |
| “Metatag por bundle” | Título SEO según tipo de contenido |
| “Exportar config” | Guardar ajustes en archivos YAML (para no perderlos) |
| “Migrate plugin” | Script que importa datos WP → Drupal |
| “Paragraphs” | Bloques reutilizables (hero, precio, incluye) — encaja con Figma |
| “Domain module” | Un Drupal sirve varios dominios |
| “Hardcodear en Twig” | Poner texto fijo en la plantilla (a veces mal: mejor campo editable) |

---

## 4. Qué preguntar TÚ (guion de 10 min)

Orden sugerido en la mesa de 5:

1. **Staging:** “¿Cuál es la URL de prueba y tengo usuario?”  
2. **URLs:** “¿Vamos a conservar las mismas rutas o hay lista de 301?”  
3. **Alcance:** “¿Qué dominio corta primero?”  
4. **Ads (a Lizet):** “¿Me pasas las landings que están pagando? Esas van primero en redirects.”  
5. **Contenido:** “¿Los tours se importan con Migrate o se cargan a mano?”  
6. **SEO:** “¿Quién configura Metatag / sitemap / noindex del staging?”  
7. **Roles:** “¿Arely y yo editamos en staging ya?”  
8. **Fecha:** “¿Hay fecha tentativa de cutover?”  

Tu frase de posicionamiento:

> “Yo me encargo de que el mapa de URLs y Search Console queden listos para no perder clics ni landings de Ads en el corte.”

---

## 5. Cómo NO matar rankings ni leads (versión mesa)

Detalle largo: `COMO-NO-MATAR-RANKINGS-Y-LEADS.md`.

**En una frase:** mismas URLs o 301; staging invisible a Google; WhatsApp y precio visibles; Ads redirigidas; medir antes y después con GSC.

---

## 6. Estudio hoy (26 ago, desde 9:30)

No leas 10 archivos a la vez. Orden:

| ⏱ | Qué |
|---|---|
| 25 min | Este archivo (releer §2) |
| 40 min | `wordpress/00-WORDPRESS-DESDE-CERO.md` |
| 40 min | `drupal/01-QUE-ES-DRUPAL.md` + `09-TWIG-EXPLICADO.md` |
| 30 min | `COMO-NO-MATAR-RANKINGS-Y-LEADS.md` |
| Noche | Empieza `php/00-PHP-DESDE-CERO.md` (no todo) |

Mientras tanto en oficina: anota respuestas a las 8 preguntas del §4.
