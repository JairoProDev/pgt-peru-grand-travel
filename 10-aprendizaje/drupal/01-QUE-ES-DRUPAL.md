# Qué es Drupal (desde cero)

## En una frase

**Drupal** es un CMS (como WordPress): base de datos + panel de admin + temas + módulos. La diferencia: modela contenido con **tipos de contenido y campos** de forma más rígida y potente; el multidioma y los permisos son de primer nivel; el front se construye con **Twig** (plantillas), no con un page builder típico tipo Elementor/Goodlayers.

## Analogía


|              | WordPress (PGT hoy)            | Drupal (destino)                                     |
| ------------ | ------------------------------ | ---------------------------------------------------- |
| Sistema      | WordPress core                 | Drupal core (10 u 11)                                |
| “Apps”       | Plugins                        | **Módulos**                                          |
| Apariencia   | Tema + constructor             | **Tema Twig** (+ a veces Layout Builder)             |
| Tours        | Plugin Tourmaster (CPT `tour`) | **Content type** `tour` + campos                     |
| SEO plugin   | Yoast / Rank Math              | Metatag + Pathauto + Redirect + Schema.org (módulos) |
| Traducciones | 4 instalaciones distintas      | Traducciones en **un** sitio (o Domain)              |




## Qué problemas de PGT resuelve Drupal (por eso lo eligieron)

1. **Un tour, varios idiomas** sin copiar 4 WordPress.
2. Campos estructurados (precio, incluye, duración) sin pelear con `postmeta` serializado de Tourmaster.
3. Workflows y roles más finos (quién publica, quién traduce).
4. Menos dependencia de “plugin comercial + constructor” (menos superficie si no instalan basura).



## Qué NO resuelve solo

- Leads de WhatsApp (sigue siendo proceso comercial).
- Ads / Semrush / contenido bueno.
- Una migración mal hecha (301 rotos = muerte SEO).
- Spam si suben módulos piratas (mismo riesgo de higiene).



## Piezas que oirás todo el día


| Pieza                 | Qué es                                                            |
| --------------------- | ----------------------------------------------------------------- |
| **Core**              | Drupal en sí (`/core`)                                            |
| **Contribute module** | Módulo de Drupal.org (como plugin del repo oficial)               |
| **Custom module**     | Código PHP propio del proyecto                                    |
| **Theme**             | Capas Twig + CSS/JS                                               |
| **Entity**            | Unidad de datos (nodo, usuario, media, párrafo…)                  |
| **Node**              | Contenido publicado de un content type (una ficha tour = un node) |
| **Config**            | Configuración exportable (YAML) — “Infrastructure as code” light  |
| **Composer**          | Cómo se instalan Drupal y módulos (`composer require …`)          |
| **Drush**             | CLI de Drupal (como WP-CLI)                                       |
| **Staging**           | Entorno de prueba (ej. `demo.perugrandtravel.com`)                |




## Versiones

Pregunta ya: **¿Drupal 10 o 11?** No estudies Drupal 7 (obsoleto). En 2026 lo normal es **10 LTS o 11**.

## Cómo se “siente” el admin

Más formularios, menos Canva. CM suele odiarlo al principio. Tu valor: **diseñar campos y checklist de publicación** para que no sufran — y schema/hreflang correctos.

## Práctica mínima (esta semana)

1. Pedir acceso **solo lectura** al staging Drupal (si existe).
2. Crear (o ver) un content type de prueba: título + body + un campo precio.
3. Ver una página en el front y preguntar: ¿qué Twig la renderiza?

Siguiente: `02-VOCABULARIO-WP-VS-DRUPAL.md`.