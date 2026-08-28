# Yoast, staging, Drush, permalink, node — cada uno a fondo

Pediste no solo “mencionarlos”. Aquí van **uno por uno**, lentos.

---

## A) ¿Qué es Yoast?

**Yoast SEO** es un **plugin de WordPress** (se instala en WP, no en Drupal).

### Para qué sirve

Cuando editas una página/tour/post, Yoast añade una caja donde controlas:

1. **SEO title** — el título azul que suele mostrar Google.  
2. **Meta description** — el texto gris debajo en Google.  
3. **Slug** — parte de la URL.  
4. **Canonical** — URL “oficial” si hay dudas de duplicados.  
5. **Sitemap** — lista de URLs que WordPress ofrece a Google.  
6. **Schema** — datos estructurados (a veces incompletos o mal en temas raros).  
7. Semáforos — heurística del plugin; **no** son la verdad de Google.

### Qué NO hace

No “posiciona automático”. No reemplaza buen contenido ni buena URL.  
No migra a Drupal: en Drupal usarás **Metatag** y amigos.

### Por qué te importa ahora

En WP, los titles/metas de tus 18 tours / 115 blogs viven (muchas veces) en Yoast o Rank Math.  
Al migrar, hay que **recrear** esa info en Drupal o se pierden snippets → baja CTR → parecen “peores rankings”.

**Pregunta:** “¿Los SEO title de Yoast se van a importar a Metatag o se reescriben?”

---

## B) ¿Qué es staging?

**Staging** = entorno de **ensayo**.

| Entorno | Público | Uso |
|---|---|---|
| Producción | Sí | Clientes reales, Ads, Google |
| Staging | No (o poco) | Probar Drupal, diseño, migración |
| Local | Solo tú | Laptop (opcional) |

Ejemplo PGT: `demo.perugrandtravel.com` (si sigue activo).

### Reglas

1. Romper en staging está bien.  
2. Staging debe decirle a Google **noindex** (no me muestres).  
3. Contraseñas distintas a producción si se puede.  
4. Nunca “subir a prod” sin checklist.

**Pregunta hoy:** “¿Cuál es la URL de staging de Drupal y me crean usuario?”

---

## C) ¿Qué es Drush?

**Drush** = **Dr**upal Shell.  
Programa de **línea de comandos** (terminal negra) para administrar Drupal sin hacer clic en todo.

Analogía: control remoto de técnico.

Ejemplos que oirás:

| Comando | En cristiano |
|---|---|
| `drush cr` | “Limpia la caché” — para ver cambios de Twig/config |
| `drush status` | “¿El sitio está bien conectado a la BD?” |
| `drush cex` / `cim` | Exportar / importar configuración |

Tú al inicio: **entiende la frase**. No necesitas ejecutarlo hoy.  
Si alguien dice “haz drush cr”, pide que lo hagan ellos o te digan exactamente dónde.

---

## D) ¿Qué es un permalink?

Palabra de **WordPress** (en Drupal se dice más **alias** / **URL alias**).

**Permalink** = “enlace permanente” = la URL estable de un contenido.

Ejemplo:

`https://www.perugrandtravel.com/tour/humantay-lake-full-day/`

Esa cadena es un activo SEO. Tiene impresiones y clics en GSC.

Si mañana Drupal solo tiene `/node/88` o `/experience/humantay`, Google ve otra cosa → hace falta **misma URL** o **301**.

**Slug** = trozo final: `humantay-lake-full-day`.

---

## E) ¿Qué es un node?

Palabra de **Drupal**.

**Node** = una pieza de contenido creada a partir de un content type.

| Content type (molde) | Node (ejemplares) |
|---|---|
| Tour | Salkantay 4d, Humantay, Maras… |
| Article | Cada post del blog |

Analogía: content type = “formulario de inscripción”; node = “una ficha llena”.

ID interno: `node/145`.  
URL pública: alias `/tour/...`.

**No confundir con Node.js** (runtime JavaScript). Son homónimos infelices.

---

## F) Relación entre todos (una historia)

1. En **WordPress**, editas un tour; **Yoast** guarda el SEO title; el **permalink** ya rankea.  
2. Montan **Drupal** en **staging**.  
3. Crean content type Tour; importan un **node** Salkantay.  
4. El **Twig** pinta la ficha.  
5. Alguien corre **Drush** para limpiar caché.  
6. Configuran Metatag (reemplazo de Yoast).  
7. Arman **301** si el alias no coincide con el permalink.  
8. El día del **cutover**, producción apunta a Drupal; GSC se vigila.

Tu hilo conductor: **permalink/alias + 301 + GSC + ficha con WhatsApp**.

---

## G) Autotest (responde en bitácora)

1. ¿Yoast se instala en Drupal?  
2. ¿Staging debe salir en Google?  
3. ¿`drush cr` borra tours?  
4. ¿Permalink y alias son primos?  
5. ¿Un blog post en Drupal es un node?

Respuestas: 1) No 2) No 3) No, limpia caché 4) Sí 5) Sí
