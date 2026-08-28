# Cómo funciona el sitio PGT (panorama) + por qué migrar es difícil

**26 ago 2026.** Tras ver tu `wp-admin` de perugrandtravel.com.

---

## 1. Lo que estás viendo ahora

| Pantalla | Qué es |
|---|---|
| Barra negra arriba en perugrandtravel.com | Estás **logueado en WordPress** |
| `/wp-admin/` | Panel de administración (oficina) |
| Menú **Tour** | Plugin **Tourmaster** (los paquetes) |
| **Yoast SEO** | Títulos/metas/sitemaps para Google |
| **Plugins** | “Apps” instaladas (WhatsApp, Rocket, Redirection…) |
| Simplytest Belgrade (antes) | Drupal de **juguete** — otra cosa, temporal |

Hoy practicaste el **origen**. Drupal será el **destino**.

---

## 2. ¿En qué lenguajes está?

No es “un solo lenguaje”. Es un sándwich:

```
NAVEGADOR (visitante)
  ← recibe HTML + CSS + JavaScript
SERVIDOR (Banahosting / luego VPS)
  ← ejecuta PHP (WordPress, temas, plugins)
  ← lee/escribe MySQL (textos, tours, precios, users)
ARCHIVOS EN DISCO
  ← wp-admin/, wp-includes/, wp-content/themes/, wp-content/plugins/
```

| Capa | Lenguaje | ¿Lo editas tú a diario? |
|---|---|---|
| Contenido (tours, blogs) | Datos en **MySQL** | Sí, desde wp-admin |
| Lógica CMS + Tourmaster + Yoast | **PHP** | Casi no (plugins ya hechos) |
| Diseño / constructor Goodlayers | PHP + HTML + mucho CSS/JS | A veces |
| Lo que ve Google/usuario | **HTML** generado | Indirectamente |

**Twig** aún no está aquí. Twig aparece en **Drupal**.  
WordPress de PGT = sobre todo **PHP + MySQL + HTML/CSS/JS**.

---

## 3. ¿Se puede “descargar toda la página / todo el código”?

### Lo que NO sirve

- Clic derecho → “Guardar como…” → solo una foto HTML muerta, sin panel, sin tours editables.
- Extensiones “download website” → igual: cáscara, no el sistema.

### Lo que SÍ es “todo el sitio” (2 piezas)

| Pieza | Qué contiene | Cómo se saca (con permiso) |
|---|---|---|
| **1. Archivos** | Core WP + tema Goodlayers + child theme + plugins (Tourmaster, Yoast…) | cPanel File Manager, FTP/SFTP, o backup del hosting |
| **2. Base de datos** | Todos los textos, tours, precios, users, opciones Yoast | Export `.sql` (phpMyAdmin / backup) |

Sin las **dos**, no “tienes el sitio”.  
Eso lo suele hacer **Ricardo / hosting / clever@**, no un “Download” del navegador.

### ¿Debes descargarlo tú hoy?

**No**, salvo que Ricardo te pida un backup.  
Para aprender y para SEO de migración **no necesitas** el ZIP completo. Necesitas:

- Entender el panel (ya entraste)  
- Inventario de URLs  
- Qué plugins hacen qué  

⚠️ **No pegues en el chat** capturas del Excel de Accesos con contraseñas. Borra esas imágenes del hilo si puedes. Riesgo de seguridad.

---

## 4. Cómo funciona, en una historia

1. Alguien visita `/tour/salkantay-trek-4-days/`.  
2. El servidor ejecuta **PHP** (WordPress).  
3. WordPress pregunta a **MySQL**: “dame el tour con ese slug”.  
4. **Tourmaster** aporta campos (precio, itinerario…).  
5. El **tema / Goodlayers** arma el HTML.  
6. **Yoast** inyecta title/meta/schema en el `<head>`.  
7. **Click to Chat** pone el botón WhatsApp.  
8. **WP Rocket** puede servir una copia rápida en caché.  
9. El navegador muestra la página.

Tú en wp-admin no “escribes HTML del tour”: editas **datos**; PHP los pinta.

---

## 5. Dónde está la complejidad de migrar (Drupal o código puro)

La complejidad **no** es “copiar la home bonita”.  
Es **todo esto a la vez**:

### A) Muchos sitios, no uno

El Excel lista **varios WordPress** (EN, PT, ES, IT, luxury, vinicunca, etc.).  
Migrar “PGT” puede ser migrar **una red**, no una página.

### B) Tours ≠ posts de blog

Los tours viven en **Tourmaster** (tablas/meta propias).  
Un migrador genérico WP→Drupal trae posts/páginas.  
**No** entiende Tourmaster solo. Hay que mapear campo a campo o recrear.

### C) Diseño Goodlayers

El layout está en el constructor, no en HTML limpio.  
En Drupal/código se **redibuja** con Twig/React desde Figma. No se “exporta el builder”.

### D) SEO guardado en Yoast (+ URLs)

Titles, metas, a veces redirects.  
Si no se migran → Google muestra basura → CTR cae (“matamos rankings”).  
Plugins **Redirection** = reglas 301 que también hay que llevar.

### E) Plugins = funciones que hay que reemplazar

Cada plugin activo es una promesa:

| Plugin (vimos en tu pantalla) | En destino hay que… |
|---|---|
| Tourmaster | Content type Tour + campos |
| Yoast | Metatag (Drupal) o capa SEO en código |
| Click to Chat | Campo/botón WA |
| WP Rocket | Caché Drupal/servidor |
| Redirection | Módulo Redirect / nginx |
| PixelYourSite / GTM | Volver a poner tags |
| QuadMenu | Menú en tema nuevo |
| Trustindex / Tripadvisor widgets | Re-integrar |
| RD Station | Reconectar forms |

### F) URLs y Google

Miles de URLs ya indexadas.  
Misma ruta o **301**. Fallar aquí = matar rankings y Ads.

### G) Idiomas

4+ frentes. Unificar en Drupal es la promesa; el trabajo es el mapa hreflang + no dejar huecos.

### H) “Código puro” no elimina B–G

Aún debes: modelo Tour, admin para marketing, migrar datos, 301, schema, WA, tags, menús.  
Ganas control; **no** te saltas la migración de contenido ni el SEO.

```
Fácil (apariencia):     Figma → HTML bonito
Difícil (negocio):      70 tours × campos × idiomas + 400 blogs + Yoast + 301 + Ads + WA
```

---

## 6. Mapa mental final (guárdalo)

```
HOY (origen)
  WordPress × varios dominios
  + Tourmaster (tours)
  + Goodlayers (diseño)
  + Yoast (SEO)
  + otros plugins
  + MySQL (datos)
  + archivos PHP en hosting

MAÑANA (destino Drupal)
  Un Drupal (o Domain)
  + content types / Twig
  + Metatag / Redirect
  + mismos datos migrados
  + mismas URLs o 301
  + VPS Ubuntu (lo que arma el jefe)

O destino código
  Next/PHP propio + CMS admin
  + MISMAS dificultades de datos/URLs/SEO
```

---

## 7. Qué hacer TÚ con este panorama (hoy)

No descargues el sitio entero.

1. En wp-admin: **Tour** → mira cómo se edita un tour (campos).  
2. **Posts** → un blog tuyo.  
3. **Yoast** en esa ficha → title/meta.  
4. **Plugins** → ya viste la lista; no desactives nada.  
5. Anota: “Tourmaster + Yoast + Click to Chat + Redirection + Rocket = piezas críticas.”

Eso conecta con: *la migración es difícil porque hay que recrear esas piezas y no perder URLs/datos.*

Drupal demo (Simplytest) = otra pestaña, otra hora. No mezcles con wp-admin de PGT en la misma cabeza el mismo minuto.
