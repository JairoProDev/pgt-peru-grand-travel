# Drupal sprint — Jairo (hoy)

**Staging:** [http://147.135.114.64/](http://147.135.114.64/)  
**Mi bloque:** 18 tours + 115 blogs  
**Pack generado:** `03-seo/datos/drupal-sprint-jairo-2026-09-01/`

---

## División de roles (no te quemes)


| Tú (Jairo)                    | Equipo / Einel                       |
| ----------------------------- | ------------------------------------ |
| Pegar meta SEO (title, desc)  | Contenido body, itinerario, imágenes |
| Verificar URL `/tour/{slug}/` | Pathauto, redirects 301              |
| QA checklist 5 min por URL    | Precio, campos tour                  |
| Marcar `estado_drupal` en CSV | WA block global (pedir a Einel)      |


**Tu ventaja:** optimizas mientras migran — no copies sin mejorar meta donde GSC lo pide.

---



## Rutas Drupal (verificadas 1 sep)


| Qué              | URL                                                                                                                    |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Lista products   | [http://147.135.114.64/admin/anymerce/products](http://147.135.114.64/admin/anymerce/products)                         |
| Crear tour       | [http://147.135.114.64/admin/anymerce/products/add/default](http://147.135.114.64/admin/anymerce/products/add/default) |
| Admin content    | [http://147.135.114.64/admin/content](http://147.135.114.64/admin/content) → tab **Products**                          |
| Media            | [http://147.135.114.64/admin/content/media](http://147.135.114.64/admin/content/media)                                 |
| Bloques globales | [http://147.135.114.64/admin/content/block](http://147.135.114.64/admin/content/block)                                 |
| **NO usar**      | `/admin/commerce/products` → 404                                                                                       |


**Estado staging:** 26 products migrados (equipo). Tus 18 tours del bloque Jairo aún no tienen slug WP 1:1.

## Dónde pegar SEO (exacto)

Sidebar derecho del formulario Product → **Meta tags** → **Basic tags**:

- **Page title** ← `seo_title` del CSV (reemplazar token `[anymerce_product:title] | [site:name]`)
- **Description** ← `meta` del CSV (reemplazar token)

Clipboard listo: `03-seo/datos/drupal-tour-seo-clipboard/TOURS-SEO-CLIPBOARD.md`

---



## Flujo rápido por TOUR (30–35 min manual equipo)

1. Abre **WP** tour en una pestaña: `perugrandtravel.com/tour/{slug}/`
2. Abre **Drupal** Product → Edit (o crear si no existe)
3. **Copiar** de `jairo-migracion-maestro.csv`: seo_title, meta, keyword
4. **Pegar** en campos Metatag / SEO de Drupal (pregunta a Einel nombre exacto)
5. **URL alias:** `/tour/{slug}/` — si solo sale `/product/N`, anotar en CSV → Einel
6. Checklist 5 min → marcar `hecho` en CSV



## Flujo rápido por BLOG (15–25 min)

1. WP: `/blog/{slug}/` (o editar en `/blog/wp-admin/`)
2. Drupal: Add content → Blog
3. Pegar título, body, meta (Things MP = plantilla)
4. **Bloque tours** al final (3 enlaces) — obligatorio para conversión
5. Alias `/blog/{slug}/`
6. Anotar 301: `url_categoria_301` → Einel/Ricardo

---



## Orden HOY (prioridad SEO)



### P0 — Tours piloto (aprende el flujo)


| Slug                            | Por qué                       |
| ------------------------------- | ----------------------------- |
| `the-classic-salkantay-trek-5d` | Ads 8.100/mes salkantay + POC |
| `choquequirao-trek-5d`          | Keyword Ads in account        |
| `incredible-machu-picchu-2d`    | Machu picchu tours            |




### P0 — Blog


| Slug                           | Por qué                                 |
| ------------------------------ | --------------------------------------- |
| `things-to-do-in-machu-picchu` | 6.115 imp, CTR 0,02% — ya optimizado WP |




### P1 — Top blogs tu bloque (impresiones)

1. `is-it-safe-to-go-to-peru` — 9.102 imp
2. `huayna-picchu` — 2.854 imp
3. `the-top-3-hikes-in-cusco` — 2.254 imp
4. `best-things-to-do-in-cusco` — 1.205 imp
5. `ceviche-peru-in-10-days` — 985 imp

(Lista completa en `SPRINT-HOY.md`)

---



## Archivos que debes tener abiertos

```
03-seo/datos/drupal-sprint-jairo-2026-09-01/jairo-migracion-maestro.csv  ← marcar estado
03-seo/datos/drupal-sprint-jairo-2026-09-01/SPRINT-HOY.md                 ← fichas por URL
03-seo/guias/MIGRACION-SEO-CAMPO-A-CAMPO.md                               ← checklist
03-seo/guias/CTR-THINGS-MP-WP-PASO-A-PASO.md                              ← spec Things MP
```

---



## Lo que necesito de ti (para ir más rápido)


| #   | Qué                                                                                                                                            | Para qué                     |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| 1   | **Carpeta assets Einel** (ruta o zip) está en descargas traela de windows a linux si es que es mejor apra acceder y tenerlo en el repo de pgt. | No buscar imágenes una a una |
| 2   | **1 captura** del formulario Edit Product (campos SEO)                                                                                         | Guía campo a campo exacta    |
| 3   | **Confirmar** si puedes editar Products o solo Blogs                                                                                           | Ajustar plan                 |
| 4   | Marcar en CSV `estado_drupal` cuando termines cada URL                                                                                         | Yo hago diff WP vs staging   |


---



## Preguntas urgentes para Einel (WhatsApp)

1. ¿Dónde está el campo **SEO title / meta** en Product y Blog?
2. ¿Pathauto para `/tour/{slug}/` está configurado o seguimos en `/product/N`?
3. ¿Cuándo activan **botón WhatsApp** en tours?
4. ¿Import masivo CSV o solo manual esta semana?

---



## Automatización ya lista

```bash
# Pack sprint (fichas + CSV maestro)
python3 03-seo/scripts/generate-drupal-sprint-pack.py

# Clipboard SEO por tour (title + meta listos para pegar)
python3 03-seo/scripts/generate-tour-seo-clipboard.py

# Validar URLs WP vs staging
bash 03-seo/scripts/check-urls.sh
```

---

*Actualizado 1 sep 2026 mañana*