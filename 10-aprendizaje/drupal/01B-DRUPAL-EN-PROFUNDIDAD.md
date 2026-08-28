# Drupal desde cero — explicado con detenimiento

Si `01-QUE-ES-DRUPAL.md` se te hizo corto, **este** es el que debes leer.  
Complementa: `09-TWIG-EXPLICADO.md`, `../wordpress/00-WORDPRESS-DESDE-CERO.md`, `../HABLAR-EL-IDIOMA-EQUIPO.md`.

---

## 1. ¿Qué es Drupal, sin humo?

Drupal es un **CMS en PHP**, como WordPress: guarda contenido en una base de datos y lo muestra en páginas web.

La diferencia de “personalidad”:

| | WordPress (PGT hoy) | Drupal (destino) |
|---|---|---|
| Filosofía | Fácil de empezar, muchos plugins, builders | Modelo de datos estricto, permisos finos, enterprise |
| Tours | Plugin Tourmaster (caja negra comercial) | Ustedes definen el molde Tour |
| Idiomas | 4 instalaciones sueltas | Pensado para traducir en un sistema |
| Diseño | Goodlayers (clics visuales) | Tema + **Twig** (plantillas) |
| Extensiones | Plugins | **Módulos** |

Clever eligió Drupal: unificar catálogo/idiomas y salir del caos de plugins/builders (y del riesgo de pirata).  
Tu trabajo no es “gustarte Drupal”: es **que el cambio no borre Google ni WhatsApp**.

---

## 2. De cero: qué ve el visitante vs qué ves tú

### Visitante

Abre `https://www.perugrandtravel.com/tour/salkantay-trek-4-days/`  
Ve HTML: título, fotos, precio, botón WhatsApp.

### Tú en el admin

Entras a `/admin` (o `/user/login`), editas campos, guardas.  
Drupal guarda en BD y, al visitar la URL, **renderiza** (arma) el HTML con el tema Twig.

**Staging** = misma idea, pero en una URL de prueba para no romper el sitio real.

---

## 3. Node — la palabra que más te va a confundir

En Drupal, casi todo contenido “de página” es una **entidad**.  
El tipo más común de contenido de página se llama **node**.

**Node = una unidad de contenido publicada (o borrador).**

Ejemplos:

- El tour Salkantay 4 días → **1 node**  
- El blog “Things to Do in Machu Picchu” → **1 node**  
- La página “About us” → **1 node**  

No significa “nodo de red” ni “Node.js” (eso es otro mundo JavaScript).  
En reuniones, “crear el node” = “crear esa ficha/página en Drupal”.

Cada node tiene un ID interno (`/node/123`) y un **alias** bonito (`/tour/salkantay…`).  
Google debe ver el alias; el `/node/123` es feo (a veces se redirige).

---

## 4. Content type — el molde

Antes de crear nodes, defines el **content type** (tipo de contenido):

- Content type `tour` → todos los tours  
- Content type `article` → blogs  

Es como elegir “¿voy a crear un tour o un artículo?” en el admin.

**Campos:** trozos de información del molde.

Ejemplo molde Tour:

| Campo | Ejemplo de dato |
|---|---|
| Título | Salkantay SKY Trek 4 days |
| Body | Descripción larga |
| field_price | 450 |
| field_currency | USD |
| field_whatsapp | https://wa.me/51… |
| field_hero | imagen |

Cuando migren, alguien debe haber creado estos campos.  
Tu pregunta inteligente: “¿Qué campos tiene el Tour? ¿Precio y WhatsApp son obligatorios?”

---

## 5. Tema, Twig, módulo — otra vez, más claro

```
[Base de datos: nodes y campos]
        ↓
[Drupal core + módulos]  ← reglas, SEO, redirects, migrate
        ↓
[Tema: archivos Twig + CSS + JS]  ← cómo se ve
        ↓
[HTML al navegador]
```

- **Módulo Redirect:** sabe hacer 301.  
- **Módulo Metatag:** sabe title/description.  
- **Tema Twig:** coloca el precio en la columna derecha.

Si el precio no aparece, puede ser: campo vacío **o** Twig que no lo imprime. Por eso preguntar “¿dato o plantilla?”.

---

## 6. Staging, Drush, Composer — operaciones

### Staging

Copia de trabajo. URL distinta. Debe tener **noindex**.  
Ahí prueban migración y diseño.  
Producción = clientes reales.

### Composer

Instala Drupal y módulos con versiones controladas (profesional).  
Evita ZIP raros (virus).

### Drush

Programa de terminal. Ejemplos:

- `drush cr` — limpia caché (cambiaste Twig y no se ve → suelen hacer esto)  
- `drush status` — ¿está sano el sitio?  

Tú al inicio **no** tienes que manejar Drush; sí saber qué significa cuando Ricardo lo diga.

---

## 7. SEO en Drupal (equivalentes mentales)

| Querías en WP | En Drupal sueles usar |
|---|---|
| Yoast title/meta | Módulo **Metatag** |
| Permalinks automáticos | **Pathauto** (patrones de alias) |
| Plugin Redirection | Módulo **Redirect** |
| Sitemap Yoast | **Simple XML Sitemap** (o similar) |
| Schema Yoast | Schema Metatag / custom |

Nadie “instala Yoast en Drupal”. Se arma el stack de módulos.

---

## 8. Idiomas (por qué les importa)

Drupal puede tener el mismo tour en EN y PT como **traducciones** del mismo contenido, o varios dominios con el módulo Domain.

Pregunta de oro:

> “¿Un solo Drupal con idiomas, o Domain con perugrandtravel + machupicchupacotes + …?”

De eso depende el plan hreflang y los 301.

---

## 9. ¿Puedes poner código propio? ¿Conviene?

**Sí.** Carpetas típicas:

- `themes/custom/nombre_tema/` → Twig, CSS, JS  
- `modules/custom/nombre_modulo/` → PHP propio  

**Conviene** para diseño Figma, schema fino, scripts de migración.  
**No conviene** descargar módulos pirateados.

Yo puedo escribir Twig/PHP contigo si me pasas archivos del repo (sin contraseñas). Ver `08-COMO-ME-AYUDA-EL-AGENTE.md`.

---

## 10. Qué debes lograr entender esta semana (prueba)

Explica en voz alta a un amigo imaginario:

1. Qué es un node vs un content type.  
2. Qué es Twig (y que no es “Twing”).  
3. Qué es staging vs producción.  
4. Qué es un 301 y por qué salva rankings.  
5. Qué hace Metatag (parecido a Yoast).  

Si puedes, ya hablas el idioma del equipo lo suficiente para el mes 1.

Siguiente lectura práctica: `../COMO-NO-MATAR-RANKINGS-Y-LEADS.md`.
