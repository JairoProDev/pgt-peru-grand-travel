# Tutorial: explorar Drupal paso a paso (empaparte)

**Objetivo:** que dejes de oír “Drupal” como caja negra. En 60–90 min en **staging** (o prod solo lectura si te dejan) sabes qué hay y dónde.

**Antes de empezar necesitas:** URL de staging + usuario + contraseña (pídeselos a Ricardo).  
**Si aún no tienes acceso:** lee las secciones 0–2 y haz solo la parte “desde fuera” (§1). El resto espera al login.

**Reglas:** no borres contenido; no instales módulos; no toques producción “para probar”.

---

## 0. Mapa mental (2 min)

```
Login → Admin (oficina)
         ├─ Contenido (nodes: tours, blogs)
         ├─ Estructura (moldes: content types, campos)
         ├─ Configuración (idiomas, Metatag, Redirect…)
         └─ Apariencia (tema Twig)
Visitante → Front (HTML que arma Twig con los datos)
```

---

## 1. Sin login — explorar como Google (15 min)

Abre el sitio **público** (prod o staging si es público):

| Paso | Qué haces | Anota |
|---|---|---|
| 1 | Abre un tour tuyo (ej. Salkantay 5d) | URL exacta |
| 2 | Clic derecho → Ver código fuente | ¿Hay `application/ld+json` (schema)? |
| 3 | Busca en el HTML: `whatsapp`, `wa.me`, precio | ¿CTA claro? |
| 4 | Mira el `<title>` de la pestaña | ¿Coincide con keyword del Sheet? |
| 5 | Prueba la URL del blog con `/blog/cusco/...` y la limpia | ¿Cuál responde? ¿Redirect? |

Esto ya es trabajo útil **aunque Drupal staging no exista aún**.

---

## 2. Primer login (10 min)

1. Ve a `https://STAGING/user/login` (o la URL que te den).  
2. Entra con tu usuario.  
3. Arriba debería aparecer la **barra de administración** (Admin toolbar): negra/azul con “Gestionar”.

Si no ves barra: tu rol es muy limitado → pide “Content editor” o similar.

**Anota:** tu rol (si lo ves en `/user`).

---

## 3. Tour guiado del admin (25 min)

Hazlo en orden. En cada punto escribe 1 línea en bitácora.

### 3.1 Contenido — lista de nodes

1. Menú **Contenido** / **Content** → `/admin/content`  
2. Filtra por tipo si puedes: Tour / Article.  
3. Abre **un** tour que exista (o el que hayan migrado de prueba).

**Pregúntate:** ¿Es el mismo título que en WP? ¿Está en inglés?

### 3.2 Editar un node (sin guardar cambios críticos)

1. Botón **Editar**.  
2. Recorre los campos: Body, precio, imagen, WhatsApp…  
3. Baja a **URL alias** / “Generar alias automático” / Metatag si está en la misma pantalla.  
4. **No guardes** si no estás seguro; o guarda solo si es staging y el equipo dijo “puedes editar”.

**Anota:** lista de campos que viste (nombres).

### 3.3 Content types (moldes)

1. **Estructura → Tipos de contenido** → `/admin/structure/types`  
2. Entra en **Tour** (o como se llame) → **Administrar campos**.  
3. Cuenta cuántos campos hay.

**Pregunta a Ricardo después:** “¿field_X es el precio que usa el Twig?”

### 3.4 Idiomas

1. **Configuración → Regional e idioma → Idiomas**  
2. ¿Están EN, ES, PT, IT?  
3. Si editas un node: ¿hay pestaña “Traducir”?

**Anota:** patrón (traducciones vs Domain).

### 3.5 Metatag (el “Yoast” de Drupal)

1. Busca en admin “Metatag” → suele ser `/admin/config/search/metatag`  
2. Mira plantillas por content type (Tour, Article).

**Anota:** ¿hay template para Tour? ¿Incluye `[node:title]` o similar?

### 3.6 Redirect

1. Busca **Redirect** → `/admin/config/search/redirect`  
2. ¿Hay redirects de prueba? ¿Se pueden importar CSV?

### 3.7 Apariencia / tema

1. **Apariencia** → ¿qué tema default? ¿Hay tema `pgt` custom?  
2. No cambies el tema activo.

### 3.8 Extensiones (módulos) — solo mirar

1. `/admin/modules`  
2. Busca: Metatag, Pathauto, Redirect, Locale, Domain, Migrate.  
3. **No actives/desactives nada.**

---

## 4. Del admin al front (10 min)

1. Con un tour abierto en admin, pulsa **Ver** / Visit.  
2. Compara: lo que editaste en campos vs lo que se ve.  
3. Si cambiaste un texto en staging a propósito: ¿se ve al instante? Si no → alguien hará `drush cr` (caché).

**Idea clave:** campos = nevera; Twig = receta; front = plato.

---

## 5. Mini misión (20 min) — tu aporte real

Elige **1 tour** de tu bloque 3 que exista en staging (o el más parecido).

Llena esta tabla:

| Check | WP (prod) | Drupal staging | ¿Igual? |
|---|---|---|---|
| URL / alias | | | |
| H1 | | | |
| Precio visible | | | |
| Moneda | | | |
| Botón WhatsApp | | | |
| Imagen hero | | | |
| Idioma | | | |
| Title SEO (pestaña) | | | |

Esa tabla se la muestras a Ricardo: **gaps**. Eso es trabajo de analista SEO en migración, no “no sé Drupal”.

---

## 6. Si te pierdes — menú de pánico

| Quiero… | Voy a… |
|---|---|
| Ver todos los tours | Contenido + filtro tipo |
| Ver moldes | Estructura → Tipos de contenido |
| Ver SEO title global | Config → Metatag |
| Ver 301 | Config → Redirect |
| Volver al sitio | Icono “Atrás al sitio” / logo |
| Salir | Usuario → Cerrar sesión |

---

## 7. Después del tutorial — estudio corto

1. `09-TWIG-EXPLICADO.md` (ahora tendrá sentido).  
2. `03-CONTENT-TYPES-Y-CAMPOS.md`  
3. Pedirme: “estos son los campos que vi” → te ayudo a armar gap list vs Tourmaster.

---

## 8. Checklist de “ya me empapé”

- [ ] Sé entrar y salir del admin  
- [ ] Sé qué es un node vs content type (lo expliqué en voz alta)  
- [ ] Vi Metatag o sé que aún no está  
- [ ] Vi Redirect o sé que hay que instalarlo  
- [ ] Completé la tabla WP vs Drupal de 1 tour  
- [ ] Sé que no debo instalar ZIP raros  

Cuando termines, pega en el chat: URL staging (sin password) + foto mental de campos Tour + tabla §5.
