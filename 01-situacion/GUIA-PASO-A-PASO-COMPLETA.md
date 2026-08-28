# Guía paso a paso completa — Jairo · PGT · ago–sep 2026

**Objetivo:** Seguir esto al pie de la letra = entregar valor visible, no quedarte en “solo onboarding”, y posicionarte para jefatura (~25 sep).

**Norte Clever:** qualified leads + marca.  
**Tu rol este mes:** Analista SEO/GEO + **dueño SEO del cutover EN** (Drupal).  
**Secreto estratégico:** Track B (POC código) en paralelo, sin pelear Drupal en público.

---

## 0. Cómo leer esta guía


| Símbolo | Significa                                       |
| ------- | ----------------------------------------------- |
| ⏱       | Tiempo estimado                                 |
| ✅       | Entregable concreto (archivo, mensaje, captura) |
| 👤      | Lo haces tú en persona                          |
| 🤖      | Pide al agente Cursor                           |
| 🚫      | No hacer sin OK                                 |
| P0      | Urgente esta semana                             |
| P1      | Importante semana 2                             |


**Regla de oro:** Cada día termina con **3 hechos** en `HECHOS.md` + **1 línea** en `BITACORA.md`.

---



## 1. Rutina diaria (todos los días laborables)



### Mañana — 10 min (antes de abrir 20 pestañas)

1. Abrir `01-situacion/QUE-HACER-AHORA.md`
2. Abrir `01-situacion/registro-diario/` → crear o editar `YYYY-MM-DD.md` (copia estructura de `2026-08-26.md`)
3. Frase del día (memorizar):
  > *Estoy cerrando línea base SEO, apoyando la migración EN a Drupal, y priorizando URLs de mi bloque que generan impresiones pero pocos clics.*



### Tarde — 15 min (cierre)

1. Marcar casillas del día en registro diario
2. Añadir 3 hechos verificables a `HECHOS.md` (formato: `- AAAA-MM-DD — hecho — fuente`)
3. Si aprendiste algo accionable → 1 línea en `INSIGHTS.md`
4. Si quedó duda sin respuesta → `DUDAS.md`
5. Copiar resumen 2–3 líneas a `BITACORA.md`



### Viernes extra — 30 min

- Completar informe interno en `03-seo/informes/YYYY-MM-DD-interno.md`
- Revisar qué falta de la semana vs esta guía § Semana N

---



## 2. Dos carriles (dual track) — no mezclar el discurso



### Track A — Visible (equipo / Clever / Einer)

**Mensaje:** *“Ayudo a que la migración EN no mate Google ni los leads.”*


| Entregable                  | Cuándo                       |
| --------------------------- | ---------------------------- |
| Plan SEO para Clever        | Vie 28 / Lun 31 ago          |
| Mapa URLs WP → Drupal (CSV) | Sem 2                        |
| Checklist pre-launch Drupal | Sem 2                        |
| QA 20 URLs staging          | Cuando Einer tenga contenido |
| Informe semanal 1 página    | Cada viernes                 |




### Track B — Privado / técnico (tú + agente)

**Mensaje (solo si preguntan):** *“Prueba de concepto en 2 páginas para comparar velocidad y SEO con datos.”*


| Entregable                     | Cuándo  |
| ------------------------------ | ------- |
| Repo `pgt-poc` + Vercel        | Sem 1–2 |
| 1 tour Figma + 1 blog P0       | Sem 2–3 |
| Tabla Lighthouse Drupal vs POC | Sem 3   |
| Demo 15 min interna            | Sem 3   |


🚫 Nunca decir: “cancelen Drupal”, “Einer no sirve”, “solo código”.

---



## 3. Semana 1 — Día 4 en adelante (vie 28 ago → lun 31 ago)



### DÍA 4 — Vie 28 ago (HOY) ⏱ ~7 h



#### Bloque 1 — Comunicación (08:00–09:00) P0

**08:00–08:15 👤 Saludo + Einer (si está)**

Si lo ves, 60 segundos:

> Einer, soy Jairo, SEO/GEO. Revisé el staging en la IP de OVH — se ve alineado al Figma. Para la migración EN quiero armar el mapa de URLs y checklist SEO. ¿Las URLs de blog/tour serán iguales o cambian? ¿Seguimos con WhatsApp o será carrito? ¿Me das acceso admin Drupal para QA?

✅ Anotar respuestas en registro diario → luego `HECHOS.md`

**08:15–08:30 👤 WhatsApp Ricardo** (copiar y enviar):

> Ricardo, para el plan SEO quiero un subdominio de prueba `poc.perugrandtravel.com` (2 páginas: 1 blog + 1 tour) para comparar velocidad y snippet sin tocar el sitio vivo. ¿Me ayudas con el DNS o prefieren otro subdominio? También aviso: creé linux_admin en OMV para montar Marketing en mi laptop — ¿está bien o usamos otro usuario?

**08:30–09:00 👤 Cerrar día 3 si quedó a medias**

- Abrir `03-seo/informes/2026-08-27-interno.md` → completar sección «Cierre del día»
- Marcar casillas pendientes



#### Bloque 2 — GSC export completo (09:00–09:45) P0

1. Ir a [Google Search Console](https://search.google.com/search-console)
2. Propiedad: `https://www.perugrandtravel.com/`
3. **Rendimiento → Resultados de búsqueda**
4. Periodo: **28 días**
5. Pestaña **Páginas** → **EXPORTAR** → Hojas de cálculo o CSV
6. Guardar como: `03-seo/datos/gsc-en-paginas-28d-2026-08-28.csv`
7. Repetir pestaña **Consultas** → export → `gsc-en-consultas-28d-2026-08-28.csv`
8. Filtrar en Sheets/Excel solo URLs de tu bloque (115 blogs + 18 tours) → guardar `gsc-bloque-jairo-28d-2026-08-28.csv`

✅ 3 archivos CSV en `03-seo/datos/`  
✅ 1 hecho en HECHOS: totales export confirmados

#### Bloque 3 — Plan Clever (09:45–11:30) P0

Abrir `05-marketing/PLAN-SEO-PARA-CLEVER-BORRADOR.md` y completar:

1. §3 — Añadir cifras GSC reales (643 clics, 116k imp, CTR 0,6%)
2. §4 — Ajustar semanas 2–4 con Drupal staging ya existente
3. §5 — Añadir bullet: revisión staging OVH 28 ago (ver `DRUPAL-STAGING-REVISION-2026-08-28.md`)
4. §6 — Lista “qué necesito”: admin Drupal, mapa URLs, decisión WA vs cart, noindex staging
5. §7 — 3 prioridades P0 con URLs concretas (abajo)

**3 URLs P0 para el plan (ya validadas en CSV):**


| URL                                    | Por qué                                 |
| -------------------------------------- | --------------------------------------- |
| `/blog/things-to-do-in-machu-picchu/`  | ~6k imp, pos ~6, 1 clic                 |
| `/blog/museums-in-machu-picchu/`       | ~2,5k imp, pos ~6                       |
| `/tour/the-classic-salkantay-trek-5d/` | Tour bloque 3, enlazable desde blogs MP |


✅ Plan ≥90% listo para enviar a Clever (PDF o Doc, lun 31)

#### Bloque 4 — Lizet 15 min (11:30–11:45) P0

Preguntas fijas:

1. ¿Qué landings llevan Ads activos esta semana/mes?
2. ¿Eventos clave en GA4 para “lead” (WhatsApp click)?
3. ¿Hay URLs que **no** pueden cambiar de slug?

✅ 5 bullets en registro → pasar a HECHOS las confirmadas

#### Bloque 5 — Auditoría WP en vivo (13:00–14:30) P0

Para **cada** URL P0 (blog Things MP + tour Salkantay 5d):

1. Abrir URL en Chrome incógnito
2. Ver código fuente (Ctrl+U) → anotar:
  - `<title>`
  - `<meta name="description">`
  - ¿Hay JSON-LD? (buscar `application/ld+json`)
  - ¿Botón WhatsApp? ¿URL wa.me?
  - H1 visible
3. Abrir wp-admin → editar post/tour → captura campos Yoast + precio Tourmaster
4. PageSpeed Insights → anotar LCP, CLS, INP (mobile)
5. Crear ficha en `03-seo/auditorias/` (un .md por URL)

Plantilla ficha:

```markdown
# Auditoría — [URL]
Fecha: YYYY-MM-DD
Title: ...
Meta: ...
H1: ...
Schema: sí/no — tipos
WA: sí/no — link
Precio visible: ...
LCP mobile: ...
Notas migración: ...
```

✅ 2 fichas .md  
✅ Capturas en carpeta local (no subir secretos al repo)

#### Bloque 6 — Staging Drupal QA rápido (14:30–15:30) P0

En [http://147.135.114.64/](http://147.135.114.64/):

1. Home: title, meta, tamaño página (DevTools Network)
2. Buscar equivalente Salkantay → anotar slug Drupal
3. Probar `/blog/things-to-do-in-machu-picchu/` → confirmar 404
4. ¿Add to cart vs WhatsApp?
5. Ver `robots.txt` y `sitemap.xml` si existen

✅ Añadir filas al CSV mapa URLs (plantilla §5)  
✅ Enviar resumen a Einer si no respondió mañana (no acusatorio, checklist)

#### Bloque 7 — RD Station 20 min (15:30–15:50) — si hay hueco

Según `QUE-HACER-AHORA.md`: solo mirar, no construir CRM.

1. ¿Login en Accesos.xlsx?
2. ¿Última campaña / último acceso?
3. Anotar en HECHOS: “RD Station: sí/no acceso, último uso …”



#### Bloque 8 — Cierre día 4 (16:00–17:00)

1. Registro diario completo
2. Crear `03-seo/informes/2026-08-28-interno.md` (copiar estructura día 3)
3. BITACORA + HECHOS
4. Preparar envío Plan Clever para lun 31

---



### DÍA 5 — Lun 31 ago ⏱ ~7 h


| Hora        | Tarea                                                      | Entregable                                 |
| ----------- | ---------------------------------------------------------- | ------------------------------------------ |
| 08:00–08:30 | Enviar **Plan SEO** a Clever (email/WA)                    | PDF/Doc enviado                            |
| 08:30–10:00 | Inventario URLs bloque Jairo (18+115) desde Sheet keywords | `03-seo/datos/inventario-bloque-jairo.csv` |
| 10:00–11:00 | Empezar **mapa 301** — 20 URLs prioritarias (P0+P1)        | `03-seo/datos/mapa-urls-wp-drupal.csv`     |
| 11:00–11:30 | Reunión Einer / seguimiento WhatsApp staging               | Respuestas en HECHOS                       |
| 13:00–14:00 | GA4: mirar tráfico orgánico EN 28d (marketing@)            | Notas en `GA4-INVENTARIO.md`               |
| 14:00–15:30 | Auditar 2 blogs P0 más (Museums MP + 1 volumen)            | 2 fichas auditoría                         |
| 15:30–16:30 | Crear cuenta GitHub + Vercel + repo `pgt-poc` privado      | URLs repo anotadas                         |
| 16:30–17:00 | Informe interno lun + cierre semana 1                      | informe 2026-08-31                         |


---



## 4. Semana 2 (1–5 sep) — Medición + mapa migración



### Objetivos de la semana

- [ ] Mapa 301: **50 URLs** mínimo (top GSC + bloque Jairo + landings Lizet)
- [ ] Checklist pre-launch Drupal v1
- [ ] 5 auditorías WP completas
- [ ] POC: scaffold local (🤖 agente) + deploy `*.vercel.app`
- [ ] 1 conversación Clever: “así ayudo en migración”



### Lun 1 sep

- Completar mapa 301 columnas: `url_wp | status | tipo | clics_28d | imp_28d | url_drupal | redirect_301 | prioridad | notas`
- Pedir a Einer: lista slugs Drupal definitivos (aunque sea borrador)



### Mar 2 sep

- Auditar tours P1 (4 tours del CSV prioridad)
- Documentar gap campos: WP Tourmaster vs Drupal Commerce



### Mié 3 sep

- Canibalización blogs: duplicados `/blog/slug` vs `/blog/cat/slug` → columna `url_canonica` en mapa
- 🤖 Agente: checklist SEO pre-launch (`08-investigacion/CHECKLIST-PRE-LAUNCH-DRUPAL.md`)



### Jue 4 sep

- Screaming Frog o agente browser: crawl 50 URLs WP → export títulos/meta
- Cruzar con staging Drupal (donde exista)



### Vie 5 sep

- Informe semanal 1 pág. para Einer/Clever:
  - Avance mapa URLs
  - Riesgos top 3 (URLs distintas, 404 blog P0, WA vs cart)
  - Qué necesitas semana 3
- Demo POC interna 15 min (si hay deploy)

---



## 5. Semana 3 (8–12 sep) — Staging QA + POC



### Objetivos

- [ ] Admin Drupal (si Einer dio acceso): revisar Metatag, Pathauto, Redirect
- [ ] QA 20 URLs piloto en staging
- [ ] POC: tour Salkantay + blog Things MP en Vercel
- [ ] Lighthouse comparativo Drupal IP vs POC
- [ ] Propuesta noindex staging a Einer (texto listo abajo)



### Checklist QA por URL (staging)

Para cada URL piloto:

- [ ] 200 OK (no soft 404)
- [ ] Title único ≠ `\| Peru Grand Travel` solo
- [ ] Meta description > 120 chars, incluye keyword
- [ ] H1 una sola, coherente
- [ ] Precio + moneda visibles
- [ ] CTA WhatsApp (o decisión documentada si es cart)
- [ ] JSON-LD Tour / Article / FAQ si aplica
- [ ] Canonical correcto
- [ ] hreflang EN (otros idiomas: N/A si solo EN)
- [ ] Imágenes con alt
- [ ] Enlaces internos a tours relevantes (blogs)



### Texto noindex para Einer

> Recomendación SEO: mientras el staging esté en IP pública, conviene `noindex` (robots.txt + meta robots + ideally auth). Así Google no indexa contenido duplicado antes del cutover.

---



## 6. Semana 4 (15–19 sep) — Pre-cutover + informe mes



### Objetivos

- [ ] Mapa 301: **133 URLs** de tu bloque (18+115) — aunque Drupal aún no tenga destino, columna `url_drupal` puede ser TBD
- [ ] Informe 30 días para Clever (métricas, riesgos, plan mes 2)
- [ ] Lista 404 esperados vs no esperados
- [ ] Coordinar con Lizet: landings Ads en mapa P0
- [ ] Preparar “día D” checklist (playbook § Fase D)



### Informe mes 1 — estructura

1. Resumen ejecutivo (5 líneas)
2. Línea base GSC (28d ago vs hoy)
3. Trabajo bloque Jairo (auditorías, quick wins aplicados si hubo)
4. Migración: mapa URLs, QA staging, riesgos
5. POC (si aplica): Lighthouse, conclusión neutral
6. Mes 2: prioridades + qué necesitas del equipo

---



## 7. Tu bloque de trabajo (18 tours + 115 blogs)



### Priorización (no optimices 115 a la vez)


| Prioridad | Cantidad            | Criterio                | Acción esta semana |
| --------- | ------------------- | ----------------------- | ------------------ |
| P0        | 6 blogs + 1 tour    | Top CTR malo / pos 5–10 | Auditoría completa |
| P1        | 10 tours + 10 blogs | Volumen impresiones     | Entrar en mapa 301 |
| P2        | Resto               | Mapa solo               | Inventario slug    |


Archivo maestro: `03-seo/datos/PRIORIDAD-ACCION-JAIRO-2026-08-26.csv`

### Acción P0 por blog (template 45 min c/u)

1. GSC: clics, imp, pos, query principal
2. WP: title, meta, H1, intro, enlaces internos, WA
3. ¿Snippet en Google (buscar `site:perugrandtravel.com slug`)?
4. Propuesta **solo** title + meta (no reescribir 3000 palabras mes 1)
5. 2 enlaces contextuales a tours del bloque 3
6. Anotar en ficha auditoría



### Acción P0 por tour (template 45 min c/u)

1. Precio USD visible arriba del fold
2. WA click funciona (mobile)
3. Schema Tour / Product si existe
4. Title incluye duración + keyword (ej. “Salkantay Trek 5 Days”)
5. Fotos LCP — anotar peso hero
6. Ficha auditoría + fila mapa 301

---



## 8. Plantilla mapa URLs (`03-seo/datos/mapa-urls-wp-drupal.csv`)

```csv
url_wp,http_status,tipo,clics_28d,imp_28d,pos_media,url_drupal,redirect, prioridad,canonica_wp,notas
https://www.perugrandtravel.com/tour/the-classic-salkantay-trek-5d/,200,tour,1,1218,26.79,http://147.135.114.64/salkantay-trek-5d-4n,301,P0,,slug distinto — confirmar con Einer
https://www.perugrandtravel.com/blog/things-to-do-in-machu-picchu/,200,blog,1,6115,5.78,,301,P0,,404 en staging 28 ago
```

**Reglas:** Ver `08-investigacion/MIGRACION-WP-DRUPAL-PLAYBOOK.md` §3.

---



## 9. Track B — POC código (paso a paso)



### Fase 1 — Setup (sem 1–2) 👤

1. Cuenta [GitHub](https://github.com) → repo privado `pgt-poc`
2. Cuenta [Vercel](https://vercel.com) → conectar repo
3. Pedir DNS `poc.perugrandtravel.com` a Ricardo (mensaje §3 día 4)
4. OK verbal Einer: *“2 páginas prueba, no producción”*



### Fase 2 — Contenido (sem 2) 👤

1. wp-admin → export texto + URLs imágenes (blog Things MP + tour Salkantay)
2. Figma node 485-3513 → capturas secciones (hero, highlights, related)
3. Pasar al agente: “scaffold POC con este contenido”



### Fase 3 — Build (sem 2–3) 🤖 + 👤

Stack acordado: **Next.js o Astro + Payload CMS** (admin no-dev)

Páginas MVP:

- `/tour/the-classic-salkantay-trek-5d/` (misma slug que WP)
- `/blog/things-to-do-in-machu-picchu/`

Cada página debe tener:

- Title + meta optimizados (de tu auditoría)
- JSON-LD
- WhatsApp CTA (no cart)
- Core Web Vitals verdes en Lighthouse mobile
- Imágenes optimizadas (WebP, lazy)



### Fase 4 — Comparación (sem 3)


| Métrica     | WP prod | Drupal staging | POC |
| ----------- | ------- | -------------- | --- |
| LCP mobile  |         |                |     |
| TBT         |         |                |     |
| HTML weight |         |                |     |
| Schema      |         |                |     |
| WA visible  |         |                |     |


Guardar en `08-investigacion/LIGHTHOUSE-COMPARATIVA.md`

### Fase 5 — Demo (sem 3–4)

15 min con Einer o Clever:

1. Mostrar Figma vs Drupal vs POC
2. Mostrar Lighthouse side by side
3. Mostrar Payload admin (“Lizet puede editar texto sin código”)
4. Cierre: *“Plan A migración Drupal con este checklist SEO; Plan B evolución si queremos más velocidad.”*

---



## 10. Mensajes listos (copiar/pegar)



### Einer — staging SEO

> Einer, revisé 147.135.114.64 — diseño muy avanzado. Para migración EN preparo mapa URLs WP→Drupal y checklist SEO. ¿Confirmas si slugs cambian o podemos mantener los actuales? ¿WhatsApp o carrito en producción? ¿Admin Drupal para QA? ¿Podemos poner noindex en staging hasta cutover?



### Clever — plan mes 1

> Clever, te envío el plan SEO del primer mes: línea base Search Console, prioridades en mi bloque (133 URLs EN), y rol en migración Drupal para no perder rankings ni leads. Revisión ~25 sep según conversamos.



### Lizet — landings

> Lizet, para el mapa de migración necesito las URLs de landings con Ads activos — ¿me pasas lista o 10 min para cruzarlas?



### Ricardo — DNS POC

> (Ver mensaje §3 día 4)

---



## 11. Archivos que debes ir llenando


| Archivo                                         | Frecuencia           |
| ----------------------------------------------- | -------------------- |
| `01-situacion/registro-diario/YYYY-MM-DD.md`    | Diario               |
| `01-situacion/HECHOS.md`                        | Diario (+3 hechos)   |
| `01-situacion/DUDAS.md`                         | Cuando surja         |
| `01-situacion/INSIGHTS.md`                      | 2–3/semana           |
| `01-situacion/BITACORA.md`                      | Diario               |
| `03-seo/informes/YYYY-MM-DD-interno.md`         | Diario laborable     |
| `03-seo/datos/*.csv`                            | Según exports        |
| `03-seo/auditorias/*.md`                        | Por URL auditada     |
| `03-seo/datos/mapa-urls-wp-drupal.csv`          | Semanal              |
| `05-marketing/PLAN-SEO-PARA-CLEVER-BORRADOR.md` | Esta semana → enviar |


---



## 12. Qué NO hacer (mes 1)

- 🚫 Optimizar 115 blogs enteros
- 🚫 Instalar Drupal local obligatorio
- 🚫 Pedir clever@ / DNS raíz sin OK
- 🚫 Cambiar URLs en producción sin OK
- 🚫 Construir CRM / Vectorify
- 🚫 Simplytest / demos Drupal públicas
- 🚫 Anunciar jefatura antes de ~25 sep
- 🚫 Commitear Accesos.xlsx o contraseñas
- 🚫 Reiniciar NAS OMV sin Ricardo
- 🚫 Sabotear Drupal en grupo WA

---



## 13. Cómo demostrar “hice más de lo esperado” (revisión ~25 sep)


| Evidencia                            | Por qué cuenta          |
| ------------------------------------ | ----------------------- |
| Plan SEO entregado sem 1             | Prometiste a Clever     |
| GSC baseline + exports               | Profesional, repetible  |
| Mapa 301 133 URLs                    | Entregable #1 migración |
| QA staging documentado               | Dueño cutover real      |
| 5–10 auditorías P0                   | Trabajo bloque concreto |
| Quick wins title/meta (si CM aplica) | Resultados medibles     |
| POC con Lighthouse                   | Diferenciador técnico   |
| Informes semanales                   | Comunicación jefatura   |
| Relación Einer/Ricardo/Lizet         | No trabajas en silo     |


---



## 14. Si te bloqueas — árbol de decisión

```
¿No sé qué hacer ahora?
  → Abrir QUE-HACER-AHORA.md
  → ¿Es antes de mediodía? → Comunicación + GSC + Plan Clever
  → ¿Es tarde? → Auditoría 1 URL o filas mapa 301
  → ¿Einer no responde? → Sigue mapa URLs con columnas TBD + documenta riesgo
  → ¿Sin wp-admin? → Auditoría solo URL pública + pide acceso Ricardo
  → ¿Abrumado? → 1 URL P0 + 3 hechos + irte a casa (PRIMERA-SEMANA-ONBOARDING.md)
```

---



## 15. Referencias rápidas

- Staging Drupal: [http://147.135.114.64/](http://147.135.114.64/)
- Revisión staging: `08-investigacion/DRUPAL-STAGING-REVISION-2026-08-28.md`
- Playbook migración: `08-investigacion/MIGRACION-WP-DRUPAL-PLAYBOOK.md`
- POC accesos: `08-investigacion/MVP-POC-ACCESOS-Y-TODO.md`
- GSC baseline: `03-seo/datos/GSC-LINEA-BASE-2026-08-27.md`
- Prioridades bloque: `03-seo/datos/PRIORIDAD-ACCION-JAIRO-2026-08-26.csv`
- Tutorial GSC: `10-aprendizaje/GSC-TUTORIAL-DIA-3.md`
- No matar rankings: `10-aprendizaje/COMO-NO-MATAR-RANKINGS-Y-LEADS.md`

---

*Última actualización: 28 ago 2026 — día 4.*