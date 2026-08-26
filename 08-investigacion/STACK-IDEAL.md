# Stack ideal para Peru Grand Travel

**Dos agujas de Clever (25 ago 2026):** (1) más **qualified leads** (2) **fortalecer la marca**.

**Pregunta de plataforma:** ¿qué stack mueve esas agujas sin tumbar las tablas de keywords ni parar al cuarteto SEO (73 tours + 454 blogs)?

**Respuesta corta:** los próximos 90 días / las 2 semanas de prueba, **WordPress** + bajar Figma a plantilla/tema **sin cambiar URLs**. Una migración a Drupal **no es cambiar de servidor** ni es automática para Tourmaster. Código (Next + CMS) es el techo si tú implementas a largo plazo y hay admin para no-técnicos. Drupal modela bien “un tour, cuatro idiomas”, pero es donde **tú más lento vas** y donde hay menos talento en Cusco. Ver también `FIGMA-LECTURA.md`.

**Virus / spam / plugins piratas:** ver `VIRUS-Y-STACK-CONVERSACION.md`. El hosting que dice “culpa del equipo” suele tener razón cuando el vector es nulled plugin — eso **no** demuestra que “código propio mañana” sea la respuesta; demuestra que hace falta **higiene** + arquitectura en fases.

El CMS no posiciona palabras. Posicionan URLs estables, contenido en la intención del mercado, velocidad, idioma correcto y una ficha que ventas puede cerrar.

---

## 1. Qué tienen hoy (el dato que manda)

No es “un WordPress”. Es **cuatro WordPress** + tema comercial Goodlayers TravelTour + **Tourmaster** (CPT `tour` / `pacote`) + Yoast + WhatsApp como checkout + constructor que dispara 23–31 CSS y 35–72 JS.

Implicaciones:

- El catálogo **no es un blog**. Vive en metadatos de plugin. Los migradores WP→Drupal importan posts/páginas/usuarios. **No importan Tourmaster.**
- El cierre no es un motor de reservas tipo FareHarbor. Es **WhatsApp**. El CMS gana si la ficha es rápida, clara y en el idioma del viajero. No si tiene un checkout de hotel.
- El problema de negocio #1 ya diagnosticado no es el CMS: es **cuatro catálogos desconectados** (19 huecos en PT, lujo solo EN, 0 hreflang) + EN sin blog + schema roto.

Migrar de plataforma **sin unificar el catálogo** es cambiar el capó y dejar el mismo motor partido en cuatro.

---

## 2. Las tablas de keywords (lo que les importa)

Actualizar cada mes posición por idioma/mercado es un **tablero de diagnóstico**, no el objetivo. Un lead calificado es: país correcto + idioma correcto + producto que Ops puede operar + conversación que ventas cierra.

| Si la keyword sube y… | Qué pasó |
|---|---|
| No suben clics en GSC | Vanidad. Featured snippet / IA / CTR |
| Suben clics y no WhatsApp | Landing mala, idioma, precio, o ads al home |
| Sube “Machu Picchu tour” genérico | Caro, OTA, poco calificado |
| Sube “Short Inca Trail 2 days permits” y hay ficha + WA | Eso sí es el oficio |

**Una migración es el evento #1 que rompe esas tablas.** Google recrawlea, las URLs cambian o redirigen mal, hay un dip de 20–30% que puede durar semanas; si el mapa 301 está mal, meses. Si a quien le importan esas tablas no oye esto **antes** de firmar Drupal, te van a culpar a ti cuando el Excel se ponga rojo.

Cómo hablarlo:

> Las tablas sirven. El norte es conversaciones de WhatsApp por mercado. Si cambiamos de CMS, esas posiciones van a temblar sí o sí. O lo hacemos cuando el orgánico ya está medido en GSC y el mapa de URLs es 1:1, o estamos eligiendo un rediseño contra el propio KPI que ustedes cuidan.

---

## 3. WordPress vs Drupal vs código — para ESTA agencia

### WordPress (lo que ya corre)

**A favor**
- Ricardo y sistemas ya lo operan. Lidia/CM ya publican.
- Tourmaster ya tiene los 74 productos. El checkout (WA) ya está.
- Tus quick wins (hreflang, Offer, robots, tema hijo) viven **aquí**, en semanas.
- Ecosistema turismo (WP Travel Engine 20k+ installs; ellos ya tienen Tourmaster).
- Figma se puede bajar a un **tema hijo custom** sin cambiar URLs.

**En contra**
- Goodlayers es lento y el schema sale mal de la plantilla. Eso se arregla cambiando **tema/plantilla**, no necesariamente de CMS.
- Multidioma nativo no existe: WPML no aplica a 4 instalaciones. El hueco es arquitectónico, no “WordPress es malo”.
- Plugin hell a 5 años si siguen apilando.

**Cuándo es lo más efectivo para leads:** ahora, y mientras el diseño nuevo se pueda hacer **sin tocar slugs**.

### Drupal 10/11

**A favor (el steelman honesto)**
- Multidioma **en el core** (Content Translation, 4 módulos). Un tipo de contenido `Tour` con traducciones EN/ES/PT/IT: el hueco de 19 productos en PT **deja de ser posible por olvido de cuatro bases**.
- Modelado de datos (precio por mercado, incluye, idioma del guía, licencia Camino Inca) de primera.
- Un solo backoffice para cuatro dominios (módulo Domain) o un sitio con hreflang limpio.
- Workflow de traducción (el blog EN/IT podría nacer ligado al ES/PT sin copy-paste).
- Coste de mantenimiento a 5 años más predecible *si* hay un Drupalista de verdad.

**En contra, en Cusco, en 2026, con este equipo**
- No hay Tourmaster. El módulo `tour` de Drupal.org es un **walkthrough del admin**, no un catálogo de Machu Picchu. Booking en Drupal (Yoyaku, etc.) está en alpha o es otro oficio. Ustedes cierran por WhatsApp: igual hay que **reconstruir el tipo Tour**.
- La “migración automática” (Migrate API, `wordpress_migrate_sql`, `wp_drupal_migrate`) cubre **posts, páginas, taxonomías, media, usuarios**. No cubre CPT + `postmeta` serializado de Goodlayers/Tourmaster. Eso es **código de mapeo a medida**, ficha a ficha, campo a campo.
- El tema no viaja. Figma → tema Twig **desde cero**.
- Curva: 2–3 meses para desarrollo competente; 20+ h para que marketing publique solo (cifras típicas de comparativas 2026). CM/diseño van a odiar el admin si nadie diseña la UX editorial.
- Talento: pocos Drupal en Cusco; más caros. Si te vas, el sitio se queda huérfano.
- **Tu flujo con IA:** Drupal es YAML + config + hooks + Twig. Hay menos ejemplos que de Next o WP. Vas más lento, no más rápido. Eso no es prejuicio: es el mercado de código y de modelos.
- SEO: 4 sitios × ~150–225 URLs = cutover de ~600 URLs. Quien vive de tablas mensuales va a ver sangre si fallan 301s.

**Cuándo sí valdría Drupal:** si ya hay **agencia Drupal contratada y pagada**, o van a contratar un Drupal senior, y el horizonte es 18–36 meses de **un** catálogo. No si la idea es “Jairo lo arma en las noches”.

### Código real (Next.js / app + CMS)

**A favor**
- Techo de CWV, schema, GEO, hreflang como código. El 10.1% de conversión por 0,1 s en travel (Deloitte/Google, citado en guías 2026) vive aquí más que en un constructor.
- Tú + este repo: máxima velocidad de implementación.
- Un modelo `Tour` en TypeScript = una fuente de verdad, cuatro dominios, gaps imposibles de “olvidar”.
- Figma encaja natural (React).
- Escala a app, landings de ads, `llms.txt`, APIs.

**En contra**
- Sin CMS, **cada cambio de precio** pasa por un developer. Ops y marketing no van a esperar. Eso mata leads en temporada.
- Hay que construir: admin de tours, blog, media, roles, preview, i18n. Eso no es “un landing”. Son 3–6 meses con alcance cerrado, no dos sábados.
- Misma sangre SEO en el cutover que Drupal si cambian URLs.
- Hosting, auth, backups, WAF: hoy lo resuelve el stack WP. En custom lo operas tú o un PaaS (Vercel, etc.).

**La versión que sí es seria:** no “HTML a mano”. **Front en Next (o similar) + CMS headless** (Payload, Sanity, o WordPress headless). Los no técnicos editan. Tú controlas HTML/SEO. Ese es el stack que las guías de travel 2026 reservan a operadores con 50+ tours / multi-destino. PGT está en esa liga de catálogo (50–70 tours × 4 idiomas).

---

## 4. La migración WP → Drupal, sin mito

| Creencia | Realidad |
|---|---|
| “Es cambiar de servidor y todo sigue” | Falso. Otro PHP, otra DB, otro admin, otro tema, otras URLs posibles |
| “Se migra automático” | Automático: posts/páginas/media *si* el modelo es blog. Manual/código: tours Tourmaster, builder, reservas, widgets de reseñas, CF7, PixelYourSite |
| “Se crea de cero” | El **front** (Figma) sí. El **contenido** se importa a trozos. Los **tours** se rehacen o se mapean a mano |
| “Drupal se hace todo a mano, WordPress no” | Al revés para un developer: Drupal es más código (Composer, Drush, config). Para un CM, Drupal se siente más “formularios de gobierno” y menos Canva |
| “Así posicionamos más keywords” | El CMS no rankea. Una migración mal hecha **destruye** las keywords que ya tienen |

Proceso real, 4 sitios:

1. Inventario de URLs (ya tienes sitemaps y el CSV hreflang).
2. Modelo de contenido Drupal (`Tour`, `Post`, `Page`, traducciones).
3. Scripts Migrate para posts/páginas; **scripts custom** para tours.
4. Tema Twig desde Figma.
5. Mapa 301 1:1. Si una ficha cambia de `/tour/x/` a `/node/123`, se perdieron años.
6. Paridad: schema, hreflang, WA, pixel, GSC, sitemaps.
7. Staging. Cutover por dominio (PT primero, que cachea, o EN que es ticket — decisión de negocio).
8. 60 días de vigilancia GSC + las tablas de keywords.

Duración honesta: **4–8 meses** para cuatro idiomas si hay un Drupalista. No “el mes que viene”.

---

## 5. Figma

Figma no elige CMS. Es la piel.

| Destino de Figma | Riesgo SEO | Quién lo baja más rápido aquí |
|---|---|---|
| Tema hijo WP, **mismas URLs** | Bajo | Tú + Ricardo (PHP/Twig-ish PHP) |
| Tema Drupal Twig, mismas URLs | Medio (cutover igual) | Agencia Drupal, no tú el mes 1 |
| Next.js, mismas URLs | Medio (hosting/SSR) | Tú, alto apalancamiento |
| Cualquiera con **URLs nuevas** | Alto / catastrófico para las tablas | Nadie debería firmarlo |

La jugada inteligente: **nuevo diseño en WordPress, slugs congelados**. Si en 12 meses el constructor sigue asfixiando LCP, entonces headless. No al revés.

---

## 6. Recomendación para PGT (lo que yo firmaría)

### Horizonte 90 días — leads

1. Quedarse en WordPress.
2. P0 de la auditoría (hreflang, moneda, robots, Offer PT, caché real).
3. Publicar en PT/IT lo que Ops ya opera.
4. UTM hasta WhatsApp. Eso es “leads calificados”, no un CMS nuevo.
5. Si Figma está listo: prototipo de **una** plantilla de tour en tema hijo, no un replatform.

### Horizonte 12–18 meses — arquitectura

El stack ideal no es una marca. Es esta forma:

```
Una fuente de verdad de tours (id estable, 4 traducciones)
        ↓
4 dominios (URLs actuales, 301 = identidad)
        ↓
HTML rápido + schema + hreflang + cápsula GEO
        ↓
WhatsApp / form con UTM
        ↓
Ventas
```

Cómo se implementa, en orden de encaje con **este** equipo y **tú**:

1. **Mejor ROI / menor drama:** WordPress unificado o 4 WP + mapa de IDs (el CSV que ya existe) + tema custom. Sigue el talento local.
2. **Mejor techo si tú eres el implementador largo plazo:** Next.js + CMS (Payload o WP headless). Código de verdad, editores con admin, IA a tu favor.
3. **Mejor techo si ellos ya compraron Drupal y hay vendor:** Drupal 11 + Domain + traducciones, **tú dueño de SEO del cutover** (URLs, 301, GSC, schema), no el que aprende Drupal contra el reloj.

**No recomiendo Drupal como primera opción tuya.** No porque Drupal sea malo. Porque el cuello de PGT es catálogo + idioma + medición, y Drupal añade una curva que ni el equipo ni tú tienen, en una ciudad sin banco de Drupalistas, mientras las tablas de keywords son el totem interno.

### Qué no hacer

- Migrar en temporada alta (jun–ago) ni en el trimestre en que “empezamos a medir SEO en serio”.
- Elegir Drupal “porque es más enterprise” o código “porque Jairo es rápido”.
- Cambiar URLs para que queden “bonitas en Figma”.
- Pausar hreflang “hasta el sitio nuevo”. El sitio nuevo puede no existir en 2026.

---

## 7. Cómo te posicionas tú (sin guerra con sistemas)

Si Ricardo o una agencia ya empujaron Drupal, no llegues mañana con “Drupal es estúpido”. Llega con criterios:

> Si el objetivo es leads este trimestre, no migraría. Si el objetivo es un catálogo único a 18 meses, Drupal o un headless sirven; WordPress también, unificando. Lo que no es negociable: mismas URLs, mapa 301, GSC de los cuatro, y que marketing pueda editar un tour sin ticket a sistemas. Yo puedo bajar Figma a WordPress rápido. Drupal lo haría bien una agencia que ya lo viva; yo no voy a fingir 5 años de Drupal.

Eso es talla. “Hagámoslo en Next que yo vuelo” se oye a capricho de stack, aunque sea cierto para ti.

---

## 8. Preguntas que tienes que hacer (sin eso, no hay decisión)

1. ¿Quién decidió Drupal? ¿Hay proveedor, cotización, fecha, contrato?
2. Figma: ¿cambia la arquitectura de URLs o solo el look?
3. ¿Siguen queriendo **cuatro dominios** o unificar en uno?
4. ¿Tourmaster se usa para pagar/cupos o solo ficha + WhatsApp?
5. ¿Quién publicará tours el año que viene si el CMS es Drupal: marketing o solo sistemas?
6. ¿Aceptan un dip de 4–8 semanas en las tablas de keywords como costo del proyecto?
7. ¿El presupuesto es “tema nuevo” o “plataforma nueva”? (un cero de diferencia)

Hasta que no tengas 1, 2 y 6, cualquier stack es opinión.

---

## Lecturas (para ti, no para recitar)

- CMS travel 2026: booking engine primero, i18n como filtro, 50+ tours → headless/custom. [AtlasPerk](https://atlasperk.com/guides/technology-for-travel/website-cms/)
- WP→Drupal Migrate API importa blog, no plugins de tours. [wordpress_migrate_sql](https://www.drupal.org/project/wordpress_migrate_sql) · [wp_drupal_migrate](https://www.drupal.org/project/wp_drupal_migrate) (el segundo, sin security advisory al consultar)
- Migraciones y SEO: el dip es los 301, no el CMS. Playbooks 2026 de cutover (el sentido vale en ambos sentidos WP↔Drupal)
