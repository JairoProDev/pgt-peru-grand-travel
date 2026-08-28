# WordPress desde cero (para alguien que no lo ha usado)

Léelo despacio. Cada sección: **qué es → cómo funciona → por qué importa en PGT → qué oirás**.

---

## 1. ¿Qué es WordPress?

WordPress es un **CMS**: Content Management System = sistema para crear y editar un sitio web **sin programar cada página a mano**.

Tú (o Ricardo) entran a un panel, escriben un título, suben una foto, pulsan “Publicar”, y el mundo ve una URL.

Hay dos “WordPress”:

| | WordPress.com | WordPress.org (el de PGT) |
|---|---|---|
| Qué es | Servicio alojado de Automattic | Software **gratis** que instalas en un hosting |
| PGT usa | No | **Sí** — en Banahosting / cPanel |

Cuando digan “el WordPress”, hablan del software en sus servidores.

---

## 2. Las tres capas (memoriza esto)

```
1. CORE (núcleo)     → el motor WordPress
2. TEMA (theme)      → cómo se ve
3. PLUGINS           → qué funciones extras tiene
```

Analogía celular:

1. Android = core  
2. Fondo de pantalla + launcher = tema  
3. Apps = plugins  

En PGT:

- Core = WordPress  
- Tema ≈ Goodlayers TravelTour (con constructor visual)  
- Plugins = Tourmaster (tours), Yoast o Rank Math (SEO), WhatsApp click-to-chat, formularios, etc.

**Importante:** el virus/spam suele entrar por **plugins/temas piratas o desactualizados**, no porque “WordPress sea magia negra”.

---

## 3. ¿Dónde viven las cosas?

| Pieza | Dónde | Qué es |
|---|---|---|
| Panel admin | `tudominio.com/wp-admin` | La “oficina” |
| Archivos | Servidor: carpeta `wp-content/` | Temas, plugins, imágenes subidas |
| Contenido | **Base de datos** MySQL | Títulos, textos, precios (meta) |
| Config | `wp-config.php` | Cómo conectar a la BD (sensible) |

Cuando “editas un tour”, casi nunca editas un archivo HTML: editas un **registro en la base de datos**, y WordPress lo pinta con el tema.

---

## 4. Posts, páginas, CPT — tipos de contenido

### Página (Page)

Contenido estable: Home, Nosotros, Contacto. Pocas.

### Entrada / Post

Blog: artículos con fecha, categorías. En PGT hay cientos.

### Custom Post Type (CPT)

“Tipo de contenido personalizado.” Alguien (un plugin) inventó un tipo nuevo.

En PGT, **Tourmaster** crea el CPT `tour` (y a veces `pacote` en PT).  
Por eso los tours no son “posts de blog”: son otro tipo, con campos raros (itinerario, precio, etc.).

**Por qué importa en la migración:** Drupal no “entiende” Tourmaster. Hay que **recrear** el tipo Tour y copiar/migrar cada ficha.

---

## 5. Permalink, slug, URL (WordPress)

1. Creas un tour con título “Salkantay SKY Trek 4 days”.  
2. WordPress propone un **slug**: `salkantay-sky-trek-4-days`.  
3. La **URL** queda: `https://www.perugrandtravel.com/tour/salkantay-trek-4-days/`  
   (el `/tour/` lo pone el CPT).

Esa URL es el **permalink** (“enlace permanente”).  
Google rankea **URLs**, no “el tour en abstracto”. Si cambias el slug sin 301, el ranking de esa URL se cae.

**Ajustes → Enlaces permanentes** en WP define el patrón global. No lo toques en producción sin plan.

---

## 6. Temas y el constructor (Goodlayers)

El **tema** decide layout: header, footer, tipografía.

Muchos temas de turismo traen un **page builder** (constructor): editas bloques visualmente. Goodlayers es de esa familia.

**Pros:** diseño rápido sin código.  
**Contras:** HTML pesado, muchos CSS/JS, difícil de migrar, peor Core Web Vitals.

En Drupal **no** se lleva el builder: se rehace en **Twig** (plantillas).

---

## 7. Plugins — qué son de verdad

Un plugin = carpeta de PHP que “se engancha” a WordPress en momentos (`hooks`): al pintar el `<head>`, al guardar un post, etc.

### Yoast SEO (te lo oirán mucho)

Plugin que **no posiciona solo**. Te da control de:

- Título que sale en Google (SEO title)  
- Meta description  
- Canonical  
- Sitemap XML (`sitemap_index.xml`)  
- A veces schema (datos estructurados)  
- Semáforos verde/naranja (¡ignóralos como verdad absoluta!)

Si dicen “está en Yoast”, miran la cajita SEO abajo del editor.

**Rank Math** es el competidor; en blogs PGT a veces aparece Rank Math en el Excel de keywords (“SEO score”).

### Tourmaster

El corazón del catálogo: crea tours, precios, a veces reservas.  
Checkout real de PGT ≈ **WhatsApp**, no un carrito Amazon.

### Otros que pueden salir

| Plugin | Para qué |
|---|---|
| Contact Form 7 | Formularios |
| Click to Chat WhatsApp | Botón WA |
| PixelYourSite | Píxeles Meta/GA |
| Trustindex | Reseñas |

---

## 8. Media (imágenes)

Al subir una foto, WordPress la guarda en `wp-content/uploads/año/mes/` y crea tamaños.  
En la ficha solo “elige” la imagen destacada.

En migración: las imágenes hay que copiarlas o re-subirlas a Drupal (`files`).

---

## 9. Usuarios y roles

Admin, Editor, Author…  
En PGT hay riesgo: cuenta `marketing@` compartida en PCs → no se sabe quién cambió qué.

---

## 10. Multisite vs “4 WordPress”

WordPress puede ser **Multisite** (un core, varios sitios).  
PGT en la práctica tiene **varias instalaciones separadas** (EN, PT, ES, IT, satélites). Por eso hreflang es un dolor: no hay un botón “traducir” nativo entre cuatro casas.

Drupal se eligió en parte para **unificar** eso.

---

## 11. Qué es “el código” de WordPress

- PHP en temas/plugins  
- Hooks: `add_action('wp_head', ...)` = “cuando se imprima el head, ejecuta esto” (hreflang, scripts)  
- Plantillas PHP del tema: `single-tour.php`, etc.

No necesitas programar WP este mes; necesitas **entender** que el tour es dato + plantilla + plugins.

---

## 12. Checklist: “ya entiendo WP” si puedes explicar

1. Diferencia core / tema / plugin.  
2. Qué es un CPT y por qué Tourmaster importa.  
3. Qué es un permalink y por qué no se cambia a lo loco.  
4. Qué hace Yoast (y qué no).  
5. Por qué migrar ≠ copiar archivos del tema Goodlayers.

Siguiente: `../drupal/01-QUE-ES-DRUPAL.md` y `../drupal/09-TWIG-EXPLICADO.md`.
