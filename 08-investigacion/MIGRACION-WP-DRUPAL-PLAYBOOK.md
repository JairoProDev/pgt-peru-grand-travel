# Playbook: migración WordPress → Drupal (panorama completo)

**Estado PGT (26 ago 2026):** decisión tomada; trabajo en curso; “estos días”.  
**Tu rol:** dueño **SEO + calidad de cutover** (no pelear el CMS; no fingir ser el arquitecto Drupal senior).  
**Norte Clever:** qualified leads + marca (sin spam, sin perder rankings).

---

## 0. Mentalidad

Una migración **no es** “cambiar de hosting”. Es:

1. Nuevo modelo de datos (Tour, Blog).  
2. Nuevo tema (Figma → Twig).  
3. Nuevo admin.  
4. **Mismo (o redirigido) grafo de URLs** que Google ya conoce.  
5. Paridad: schema, hreflang, WA, pixels, sitemaps.  
6. Vigilancia 30–60 días.

Si fallan los 301, fallan las tablas de keywords y Ads. Te van a mirar a ti si te ofreciste como “el SEO de la migración”.

---

## 1. Preguntas que debes hacer HOY (anota respuestas)

| # | Pregunta | Por qué |
|---|---|---|
| 1 | ¿Drupal **10 o 11**? ¿Quién implementa (agencia / Ricardo / freelance)? | Saber con quién hablar |
| 2 | ¿Staging URL? ¿Ya hay content types? | Empezar a aprender en real |
| 3 | ¿Un sitio multiidioma o **Domain** (4 dominios)? | Arquitectura SEO |
| 4 | ¿Figma cambia **slugs** o solo look? | Dealbreaker |
| 5 | ¿Migran **todos** los dominios o EN primero? | Alcance |
| 6 | ¿Tourmaster se migra con scripts o se recarga a mano? | Tiempo real |
| 7 | ¿Fecha tentativa de cutover producción? | Baseline GSC |
| 8 | ¿Quién hace Redirects? ¿Módulo Redirect? | Dueño |
| 9 | ¿Licencias módulos / tema? (evitar nulled) | Virus 2.0 |
| 10 | ¿Ads landings — lista de Lizet? | Prioridad 301 |

---

## 2. Fases del proyecto (detalle)

### Fase A — Descubrimiento (días 1–5) ← **estás aquí**

| Paso | Qué | Quién | Entregable tuyo |
|---|---|---|---|
| A1 | Inventario dominios vivos vs legacy | Tú + Ricardo | Lista priorizada |
| A2 | Export GSC 28d + 3m (páginas, queries) | Tú | CSV en `03-seo/datos/` |
| A3 | Inventario URLs WP (tours, blogs, pages) | Tú (tu bloque) + equipo | Sheet maestro |
| A4 | Canibalización URL limpia vs categoría (blogs) | Tú | Decisión canónica |
| A5 | Modelo de campos Tour (WP vs Drupal) | Tú + implementador | Gap list |
| A6 | Landings Ads ON | Lizet + tú | URLs prioritarias |
| A7 | Hechos virus/spam residual | Ricardo | Limpieza antes de migrar basura |

### Fase B — Build Drupal (paralelo, 2–8 semanas)

| Paso | Qué | Tu aporte |
|---|---|---|
| B1 | Content types + campos | Revisar obligatoriedad precio/moneda/CTA |
| B2 | Idiomas / Domain | Validar hreflang plan |
| B3 | Tema Twig desde Figma | Revisar H1, CTA, CWV, schema hooks |
| B4 | Metatag / Pathauto / Sitemap / Redirect | Config SEO checklist |
| B5 | Migrate API o import CSV | Validar muestra 10 tours |
| B6 | GA4 / GTM / pixels | Paridad tracking |
| B7 | Roles editor | CM puede publicar sin romper SEO |

### Fase C — Staging QA (1–2 semanas antes de cutover)

| Paso | Checklist |
|---|---|
| C1 | **noindex** staging (robots + metatag + HTTP) |
| C2 | 20 URLs piloto: HTML, schema, WA, idioma |
| C3 | Screaming Frog staging (solo red interna / auth) |
| C4 | Rich Results Test muestra |
| C5 | Comparar title/H1 vs WP |
| C6 | Probar 301 en staging si ya hay mapa |
| C7 | Lizet: preview landings ads |
| C8 | Ventas: ficha se entiende / precio ok |

### Fase D — Cutover (el día)

Orden típico (ajustar con implementador):

1. Congelar WP (solo lectura) o modo mantenimiento corto.  
2. DNS / document root → Drupal (o reverse proxy).  
3. Activar Redirects (mapa completo).  
4. Sitemap nuevo enviado a GSC.  
5. Verificar 10 URLs críticas a mano (home, top tours, top blogs, landings ads).  
6. Monitor 404 (GSC, logs, Screaming Frog prod).  
7. WP viejo: no borrar 2–4 semanas (rollback).

### Fase E — Hipercuidado (días 1–60)

| Día | Acción |
|---|---|
| +1 | Informe 1 pág. a Clever: qué se cortó, riesgos |
| +3 | Lista 404 + softs |
| +7 | GSC rendimiento vs baseline (mismas páginas) |
| +14 | Hreflang sample + schema sample |
| +30 | Informe keywords internas + GSC |
| +60 | Cierre: ¿rollback WP aún necesario? |

---

## 3. Mapa de URLs y 301 (el entregable #1)

### Columnas del Sheet maestro

`url_wp | http_status | tipo (tour/blog/page) | clics_28d | impresiones | destino_drupal | tipo_redirect (301/410) | prioriad (ads/orgánico) | notas`

### Reglas

1. **Misma URL path** si es posible (alias Drupal = permalink WP). Mejor que redirect.  
2. Si cambia path → **301** (no 302).  
3. Cadenas de redirects = mal (A→B→C).  
4. Soft 404 (200 con “no encontrado”) = mal.  
5. Blogs: una sola canónica entre `/blog/slug` y `/blog/cat/slug`.  
6. Landings Ads = prioridad 0.  
7. 410 solo para spam/virus URLs que no deben volver.

### Tu bloque (baseline)

- 18 tours EN — `03-seo/datos/tours-jairo-2026-08-25.csv`  
- 115 blogs — `blogs-jairo-2026-08-25.csv`  
- Análisis: `03-seo/ANALISIS-BLOQUE-JAIRO-2026-08-25.md`

---

## 4. Qué se migra (y qué no)

| Contenido | ¿Automático? | Notas |
|---|---|---|
| Posts blog | A menudo sí (Migrate) | Revisar categorías y URLs |
| Pages | Sí | |
| Media | Parcial | Re-optimizar LCP |
| Tours Tourmaster | **No mágico** | Custom mapping o recarga |
| Goodlayers layout | No | Twig nuevo |
| Usuarios WP | Opcional | |
| Yoast meta | Parcial → Metatag | Re-revisar templates |
| Redirects viejos | Importar al módulo Redirect | |
| Reseñas / widgets | Reimplementar | Trustindex etc. |

---

## 5. Código propio en Drupal — cuándo sí

Ver `10-aprendizaje/drupal/05-TEMAS-TWIG-Y-CODIGO-PROPIO.md`.

**Sí conviene:** tema Twig, módulo `pgt_seo` (schema, helpers), migrate plugins, integraciones.  
**No:** reinventar CMS, ZIP piratas, tocar core.

Yo puedo escribir ese código si me pasas el repo o los archivos (`10-aprendizaje/drupal/08-COMO-ME-AYUDA-EL-AGENTE.md`).

---

## 6. Riesgos (diéctelos en voz alta = talla)

| Riesgo | Mitigación |
|---|---|
| Dip 20–30% tráfico 4–8 semanas | Baseline + 301 1:1 + no cambiar URLs sin necesidad |
| Ads a 404 | Lizet + prioridad 301 |
| Staging indexado | noindex + auth |
| Virus/nulled otra vez | Solo Drupal.org + custom repo |
| CM no sabe publicar | Roles + training 2 h + checklist |
| Tourmaster incompleto | QA muestra 10 tours vs WP |
| Un dominio nuevo sin 301 desde 4 | **No aceptar** sin plan |
| Tú prometes “yo solo Drupal en 1 semana” | No lo hagas |

---

## 7. Cómo te vuelves “clave” en 30 días (para S/ 5.000)

| Semana | Foco | Entregable visible |
|---|---|---|
| 1 | Preguntas A1–A10 + GSC baseline + vocabulario Drupal | CSV + doc gaps |
| 2 | Sheet URLs tu bloque + canónicas blogs + Ads URLs | Mapa 301 v0 |
| 3 | QA staging (schema, metatag, WA) + Twig review | Checklist firmado |
| 4 | Ensayo cutover / soporte D-day + informe +7 | Informe Clever |

Eso **es** trabajo de jefatura técnica de marketing digital, aunque el título aún diga analista.

---

## 8. Qué NO hacer

- Sabotear Drupal (“mejor Next”) en público.  
- Pedir clever@ el día 2.  
- Instalar módulos desde foros.  
- Optimizar keywords del Excel mientras el cutover está ciego.  
- Ausentarte del QA “porque no sé Twig”: pide capturas y las revisamos juntos.

---

## 9. Carpeta de trabajo en el repo

```
03-seo/migracion/
  mapa-urls-MASTER.csv      ← crear cuando tengas datos
  gaps-campos-tour.md
  checklist-cutover.md
  informes/
10-aprendizaje/drupal/       ← estudio
08-investigacion/STACK-IDEAL.md
08-investigacion/VIRUS-Y-STACK-CONVERSACION.md
```

---

## 10. Frase de posicionamiento (1 mes)

> La migración a Drupal ya está decidida; mi foco es que no perdamos el equity SEO ni las landings de Ads: inventario de URLs, redirecciones, baseline Search Console y checklist de schema/hreflang/WhatsApp en staging y el día del corte.
