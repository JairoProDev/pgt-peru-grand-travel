# Vocabulario: WordPress ↔ Drupal

Memoriza esta tabla. En reuniones traduce en tu cabeza.

| WordPress | Drupal | Nota PGT |
|---|---|---|
| Post / Page | **Node** (de un Content type) | Tour = content type `tour` |
| Custom Post Type (CPT) | **Content type** | Tourmaster `tour` → hay que **recrear** campos |
| Custom field / ACF / postmeta | **Field** (Field API) | Precio, duración, incluye… |
| Taxonomy / category / tag | **Taxonomy** + terms | Categoría de tour, destino |
| Media library | **Media** entities | Imágenes LCP, alt text |
| Theme + page builder | **Theme** + Twig (+ Layout Builder) | Figma → Twig, no Goodlayers |
| Plugin | **Module** | Solo de Drupal.org o custom; **nunca nulled** |
| `functions.php` / mu-plugin | **Custom module** o `.theme` | Hooks / event subscribers |
| Hook `wp_head` | `html_head` / preprocess / attachments | Schema, hreflang |
| Permalink / slug | **Alias** (Path / Pathauto) | Congelar URLs = aliases 1:1 |
| Redirect plugin | Módulo **Redirect** | 301 masivos |
| Yoast title/meta | Módulo **Metatag** | Plantillas por content type |
| Yoast schema | Schema.org Metatag / custom | Offer, Product, TouristTrip |
| `robots.txt` | Core + Metatag / robotstxt | |
| XML sitemap | Módulo **Simple XML Sitemap** (o core en D10+) | Verificar post-cutover |
| Multisite / 4 WP | **Content Translation** + Language (+ **Domain**) | Decisión de arquitectura |
| WP-CLI | **Drush** | `drush cr` = clear cache |
| `wp-content/uploads` | `sites/default/files` | |
| User roles | Roles + **permissions** granulares | |
| Transient / object cache | Cache bins / Redis | CWV y admin |

## Frases útiles en mesa

- “Ese CPT de Tourmaster hay que mapearlo a un content type con campos X, Y, Z.”
- “Los aliases tienen que coincidir con los permalinks actuales o va Redirect.”
- “El schema no lo inventa el tema: lo configuramos en Metatag o en un custom.”
- “`drush cr` después de cambiar config en staging.”

## Lo que NO existe 1:1

| WP | Realidad Drupal |
|---|---|
| Tourmaster checkout | No hay equivalente mágico; ustedes cierran por **WhatsApp** → campo CTA + tracking |
| Goodlayers sections | Se rehacen en Twig / Paragraphs / Layout Builder |
| Rank Math score | No hay “semáforo” igual; ignora vanidad |

Siguiente: `03-CONTENT-TYPES-Y-CAMPOS.md`.
