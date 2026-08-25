# Análisis bloque Jairo — baseline 25 ago 2026

Fuente: export CSV pestañas `tours jairo` y `blogs jairo` del Sheet `PGT_URLs_keywords_canibalizacion_2`.  
Archivos canónicos: `03-seo/datos/tours-jairo-2026-08-25.csv` · `blogs-jairo-2026-08-25.csv`

---

## Resumen ejecutivo (para informe externo)

| | Tours (bloque 3) | Blogs (bloque 4) |
|---|---|---|
| **URLs** | 18 | 115 |
| **Clics GSC (periodo del sheet)** | 18 | 32 |
| **Impresiones** | 19.734 | 99.857 |
| **URLs con ≥1 clic** | 18 (100%) | 32 (28%) |
| **URLs sin clics** | 0 | **83 (72%)** |
| **Posición media** | 39,2 | 32,8 |
| **En top 10 Google** | 0 | 10 |

**Lectura:** el bloque de **blogs** concentra el volumen y la oportunidad. Muchas URLs rankean bien (posición) pero **no convierten impresiones en clics** — problema de título/meta/SERP, no solo de ranking. Tours: todas tienen 1 clic simbólico; ninguna en página 1; quick wins en posición 11–30.

---

## Tours — prioridades (esta semana)

### Quick wins (posición 11–30 + impresiones altas)

| Prioridad | Tour | Keyword | Pos | Imp | Acción sugerida |
|---|---|---|---:|---:|---|
| 1 | Salkantay SKY Trek 5 days | salkantay trek 5 days | 26,8 | 1.218 | Revisar title/meta vs SERP; schema Offer; CTA WA |
| 2 | Cusco Planetarium | Cusco Planetarium | 20,6 | 784 | Contenido único; no compite con OTA genérico |
| 3 | Machu Picchu Express 3D | machu picchu 3 days | 29,8 | 528 | Intención BOFU — precio claro, WhatsApp arriba |
| 4 | Spectacular Cusco 7 days | cusco tour | 24,9 | 556 | Keyword genérica — acotar long-tail en H2 |

### Observaciones técnicas tours

- **Palabras = 0** en las 18 filas → el export no trae conteo de contenido (plugin/Yoast); verificar en WP, no confiar en la columna.
- **Modificado 2026-06-04** en casi todas → batch reciente del equipo; cuidado al tocar sin avisar a Ricardo.
- **Dominio:** 100% `perugrandtravel.com` (EN).
- **Mejor CTR relativo:** Choquequirao (0,36%), South Valley (0,27%) — volúmenes bajos pero señal de intención específica.
- **Peor posición con volumen:** Humantay Lake (67,8 pos, 1.107 imp) — prioridad media.

---

## Blogs — prioridades

### Ya en página 1 (proteger + optimizar CTR)

Estas rankean top 10 pero casi todas tienen **1 solo clic** con miles de impresiones:

| Blog | Keyword | Pos | Imp | Clics | Acción |
|---|---|---:|---:|---:|---|
| Things to Do in Machu Picchu | Things to Do in Machu Picchu | 5,8 | 6.115 | 1 | **#1 prioridad:** title/meta, FAQ schema, enlaces a tours |
| Museums in Machu Picchu | Museums in Machu Picchu | 6,3 | 2.494 | 1 | Igual — BOFU a fichas tour |
| Ceviche Peru | Ceviche Peru | 8,0 | 985 | 1 | Mantener; enlazar paquetes 10 días |
| Valentine's / Holy Week / Puno churches | varios | 7–10 | 200–900 | 0–1 | Estacional — no gastar junio |

**Insight clave:** tienes **10 URLs en top 10** con **~12.000+ impresiones** y **~8 clics totales**. Eso es CTR ~0,07% donde el mercado espera 2–5% en posiciones 5–8. **El mayor ROI esta semana está en SERP snippets, no en escribir posts nuevos.**

### Cero clics, muchas impresiones (urgente)

| Blog | Keyword | Imp | Pos | Problema probable |
|---|---|---:|---:|---|
| What is the best time to travel to Peru - Machu Picchu? | best time to travel to peru | 10.711 | 80,9 | Título largo; posición mala; canibaliza con otros "best time" |
| Climate in Peru | climate in Peru | 6.674 | 49,4 | 0 clics — snippet aburrido o competencia IA |
| Visits to Peru one week itinerary | peru one week itinerary | 4.637 | 59,9 | |
| 2 Weeks in Peru | 2 weeks in Peru | 4.233 | 61,1 | |
| Luxury Peru Vacations | luxury peru vacations | 3.811 | 58,4 | Marca luxury — alinear con `luxuryperutours` si existe |
| Where is Machu Picchu | where is machu picchu | 3.122 | 50,8 | Intent informacional — enlazar tours |
| Museums in Cusco | Museums in Cusco | 1.811 | 22,4 | **Quick win:** pos 22, muchas imp, 0 clics |

### Canibalización URL (115/115 blogs)

Todas tienen **URL limpia** ≠ **URL indexada (con categoría)**.  
Ejemplo: `/blog/the-top-3-hikes-in-cusco/` vs `/blog/cusco/the-top-3-hikes-in-cusco/`

Esto es **bomba para migración Drupal** (y para cualquier replatform). Antes de migrar hay que decidir canonical único + 301 de la indexada → limpia (o al revés, según GSC).

### Otros

- **1 draft:** Luxury Travel Peru — no indexar hasta publicar.
- **Varias filas sin Clics/Impresiones/Posición** (Rank Math reciente, sin datos GSC aún) — normal en posts nuevos 2026.

---

## Plan de acción sugerido (mañana → semana 1)

| ⏱ | Día | Acción |
|---|-----|--------|
| 30 min | Mañana | Confirmar periodo GSC de las columnas (¿28 d? ¿3 m?) |
| 45 min | Mañana | Auditar **Things to Do in Machu Picchu** + **Museums in Machu Picchu** (title, meta, H1, schema, links a tours) |
| 30 min | Día 2 | **Museums in Cusco** (pos 22, 0 clics, 1.811 imp) |
| 30 min | Día 2 | Tour **Salkantay 5d** (quick win) |
| 20 min | Día 3 | Documento canibalización URL (5 ejemplos) → ticket Ricardo |
| 15 min | Viernes | Informe externo 1 pág. con tabla resumen de arriba |

---

## Si mañana hablan de migración Drupal

**No digas no en la cara.** Di esto:

> Antes de cutover necesitamos: inventario URL 1:1, mapa 301 de las URLs con categoría vs limpias en blogs (tengo 115 casos solo en mi bloque), baseline GSC por URL, y congelar slugs. Si arrancamos migración sin eso, las tablas de keywords se van a poner rojas. Yo puedo liderar el checklist SEO del cutover; la implementación Drupal necesita vendor o scope claro.

Preguntas que hacer mañana:

1. ¿Migración = **diseño nuevo en WP** o **Drupal ya contratado**?
2. ¿Empiezan **staging** o **producción**?
3. ¿Quién hace 301s — Ricardo, agencia?
4. ¿Aceptan **dip 4–8 semanas** en posiciones?

Ver `08-investigacion/STACK-IDEAL.md` y `00-manana/SI-SALE-DRUPAL.md`.

**Tu mejor jugada:** ofrecerte a **due diligence SEO** (URLs, 301, GSC), no a ser el implementador Drupal del día 1.

---

## Formato de archivo — qué recibí

| Archivo | Estado |
|---------|--------|
| CSV tours | ✓ analizado → `03-seo/datos/tours-jairo-2026-08-25.csv` |
| CSV blogs | ✓ analizado → `03-seo/datos/blogs-jairo-2026-08-25.csv` |
| XLSX | **No llegó a `inbox/`** — solo CSV en WSL |

**Sobre “¿descargó todo o solo la hoja abierta?”**

- **CSV desde Google Sheets:** siempre **solo la pestaña activa**. Tus nombres confirman eso (`… - tours jairo …csv`).
- **XLSX desde Google Sheets:** descarga **todas las pestañas** en un solo libro.
- Pesaban igual porque exportaste **dos veces la misma pestaña** (una como CSV, una como XLSX de una hoja), no el libro completo.

**Para tener todo el archivo maestro:** una vez descarga **XLSX completo** (Archivo → Descargar → Microsoft Excel) y suéltalo en `inbox/PGT-completo-2026-08-25.xlsx`. Pestañas útiles: `Canibalizacion`, `Consultas sitio`, `URLs sin ficha`.

**Formato ganador para trabajar:** CSV por hoja en `03-seo/datos/` (como ya hicimos). XLSX completo solo como respaldo.
