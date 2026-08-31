# Cómo medir si la web trae leads (WhatsApp + conversión)

**Fecha:** 1 sep 2026 · **Dominio EN:** perugrandtravel.com  
**Pregunta:** ¿La web actual convierte? ¿Cuántos clics WhatsApp hay?

---

## Hallazgos GA4 EN (1 sep 2026 — capturas Jairo)

| Evento | Eventos / 28d | Usuarios | Eventos/usuario | Lectura |
|---|---:|---:|---:|---|
| `whatsapp_click` | 12 | 3 | **4,0** | Pico solo **29 ago** · todo **Perú** → **casi seguro equipo probando** |
| `chat:51946622318` | 93 | 89 | **1,04** | Repartido en el mes · ~1 clic/usuario → **proxy real de intención WA** |
| `session_start` | 2.800 | 2.215 | — | Base tráfico 28d |
| Eventos clave | 0 | — | — | Nadie marcó conversión |

**Tasa intención (chat):** 89 usuarios chat / 2.218 usuarios totales ≈ **4,0%**  
**Tasa intención (sesiones):** 93 / 2.800 sesiones ≈ **3,3%**

`51946622318` ≈ teléfono ventas (+51 946 622 318) — evento del plugin Click to Chat, no del POC.

### Export `ga4-chat-eventos-2026-08-03-30.xlsx` (1 sep)

**Evento:** `chat:51946622318` · Click to Chat for WhatsApp · 93 eventos / 89 usuarios

| Insight | Dato |
|---|---|
| Promedio | **3,3 clics/día** |
| Pico | 25 ago: **11** clics |
| Fuera de Perú | **79/93 (85%)** — sí es tráfico turista |
| Top países | BR 26%, US 23%, PE 15%, GB 10%, CA 8% |
| Top páginas | `/package` 28% · home 19% · `/machu-picchu-packa…` 18% |
| Por tipo | Packages/hubs **46%** · Home **29%** · Tours **17%** · Blog **2%** |

**No viene en el export:** tiempo hasta clic → ver sección “Tiempo hasta clic” abajo.


### Cómo saber si no fuimos nosotros

1. **`whatsapp_click` (12/3/4,0)** → descartar como baseline; es test del 29 ago.
2. **`chat:51946622318` (93/89)** → usar este hasta que `whatsapp_click` tenga 28d limpios.
3. **GA4 → Admin → Filtros de datos → Tráfico interno** → IP oficina + marcar equipo.
4. **Excluir Perú** en exploración solo para estimar mercado EN (US/CA/UK/AU) — no borrar Perú en prod.
5. **Cruzar con ventas** — única prueba de lead real.

### Cruce ventas + GA4 + Ads (1 sep 2026)

**Ventas (Paloma):** últimos leads EN = **18 ago** y **22 ago** (1/día).  
**GA4 chat (3–30 ago):** **93 clics WA** / 89 usuarios (~3,3/día).  
**Google Ads EN** (`USA-CAN/SEARCH/28AGO-2026`): **61 clics** en 7d, pico **28–30 ago** · S/153.

| Capa | Agosto EN | Lectura |
|---|---|---|
| Clics WA (GA4) | ~93 | Intención de contacto |
| Leads ventas | **2** (18 y 22) | Lo que ventas cuenta como lead |
| Ads EN clics | 61 (casi todo fin de mes) | Campaña nueva ~28 ago |
| Conversión WA → lead ventas | **~2%** (2/93) | Embudo se rompe después del clic |

**Ads Lizet — URL final vs ruta visible (corregido 1 sep tarde):**

En Google Ads hay **dos cosas distintas**:

| Campo en Ads | Ejemplo | Qué es |
|---|---|---|
| **URL final** | `…/packages/` · `…/machu-picchu-packages/` | Donde **aterriza** el usuario al clicar — **ambas 200 OK** |
| **Ruta del anuncio** (display path) | `peru-packages` · `machu-picchu` | Texto **decorativo** en el anuncio; no es la URL real |

Lo que se ve en el preview (`www.perugrandtravel.com/peru-packages`) **no tiene que existir** como página. Google lo permite para URLs más cortas/legibles en el snippet del anuncio.

**No es un bug de Lizet** si la URL final está bien. Revisar igual: ¿la ruta visible coincide con el contenido? ¿genera confianza?


**BR vs EN:** GA4 chat por país — BR 26%, US 23%, PE 15%. Más campañas BR en Ads; EN recién despegó fin de agosto.

**Implicación:** La web **sí genera clics WA**; ventas reporta **casi cero leads EN**. Causas probables: (1) definición distinta de “lead”, (2) muchos chats no calificados / no respondidos, (3) ads EN muy nuevos para explicar ago 18/22 (probable orgánico), (4) mezcla BR+EN en un solo WhatsApp.



**Hoy no hay en el repo un número verificado de “leads cerrados desde web EN”.**  
Lo que sí sabemos:

| Métrica | Valor | Fuente |
|---|---:|---|
| Clics Google / 28d (todo el sitio EN) | **643** | GSC 27 ago |
| Usuarios GA4 / 7d | **~606** | GA4 inventario 26 ago |
| **Conversiones marcadas en GA4** | **0** | Eventos clave = 0 |
| Plugin WA en WP | Click to Chat (`ht_ctc`) | curl prod |
| GTM en **vivo** (HTML) | `GTM-K8SZBJM5` + `GTM-NNSPKMFM` | curl 1 sep |
| GTM que abriste tú | `GTM-MJZXPQZR` (workspace “PGT WhatsApp Tracking”) | **no está en el HTML** — puede ser borrador |
| GA4 en vivo (vía GTM) | `G-NTXD373H4Q` | DevTools → `collect?v=2&tid=` |
| Tracking | GTM + UA legacy + Google Ads + **RD Station** | curl + Network |
| CRM leads real | Sheet **DAI / Paloma** (ventas) | Drive — **no abierto aún** |

**Conclusión:** puedes medir **tráfico** (GSC/GA4). Para **leads reales** necesitas cruzar GA4 eventos + ventas. Sin eso, no decidas “tirar Drupal” solo por intuición.

---

## Tres capas de medición (el embudo real)

```
Capa 1 — DEMANDA          Capa 2 — INTENCIÓN         Capa 3 — NEGOCIO
────────────────          ────────────────         ─────────────────
GSC clics / imp           Clic WhatsApp / form      Venta cerrada
GA4 sesiones              (evento medible)          (Sheet ventas / WA Business)
Posición Google           tawk.to chats             WeTravel / pagos
```

**Solo la capa 3 es dinero.** Capa 2 es tu mejor proxy **hoy** si ventas no comparte datos.

---

## Paso a paso — HOY (45 min con marketing@)

### A. GA4 — ¿hay eventos WhatsApp?

1. https://analytics.google.com → cuenta **Peru Grand Travel**
2. Propiedad **perugrandtravel.com** (ID `368486554`)
3. **Informes → Tiempo real** → abre la web en incógnito → clic botón WA verde
4. ¿Aparece algún evento? Busca nombres como:
   - `click`
   - `whatsapp`
   - `ht_ctc_chat`
   - `contact`
   - `generate_lead`

5. **Informes → Interacción → Eventos** → últimos **28 días**
6. Ordena por recuento → anota top 10 eventos

7. **Admin → Eventos → Eventos clave**
   - Si hay evento WA → **Marcar como conversión**
   - Si Eventos clave = 0 → **ahí está el hueco** (Lizet nunca lo configuró)

### B. GTM — confusión habitual (léelo)

**GTM no muestra cuántos clics hubo.** Solo configura etiquetas. Los números están en **GA4 → Eventos**.

Lo que ves en **Resumen** (flecha Contenedor → “Untitled tag” → `AW-708879898`) es **Google Ads** (conversiones de campañas), **no** clics WhatsApp en la web.

| Dónde estás | Qué es |
|---|---|
| Tag `AW-708879898` | Google Ads — redes / remarketing |
| Contenedor `GTM-MJZXPQZR` | Workspace “PGT WhatsApp Tracking” — **puede no estar publicado en prod** |
| Contenedores **en vivo** | `GTM-K8SZBJM5` y `GTM-NNSPKMFM` (curl homepage) |

**Primero:** arriba en GTM, selector de contenedor → busca **`GTM-K8SZBJM5`** (no solo MJZXPQZR).

#### Navegación GTM (5 clics)

1. **tagmanager.google.com** → cuenta Peru Grand Travel
2. Contenedor **`GTM-K8SZBJM5`** (el del HTML)
3. Menú izquierdo → **Etiquetas** (Tags)
   - ¿Hay alguna con nombre WhatsApp / GA4 / `G-NTXD373H4Q`?
4. Menú → **Activadores** (Triggers)
   - ¿Hay “Click” en enlace que contenga `wa.me` o `whatsapp`?
5. Botón **Vista previa** (arriba derecha)
   - Pega `https://www.perugrandtravel.com`
   - En la web: clic botón WA verde
   - Panel GTM: ¿alguna etiqueta pasó a **Tags Fired**?

Si en Etiquetas **no hay nada de WhatsApp** → hoy **no se mide** el clic (o solo lo mide el plugin/RD Station por otro canal).

#### Dónde ver los números (GA4, no GTM)

1. **analytics.google.com** → propiedad `perugrandtravel.com` (`368486554`)
2. **Informes → Tiempo real → Evento por nombre de evento** → clic WA en otra pestaña
3. **Informes → Interacción → Eventos** → últimos 28 días → busca `click`, `whatsapp`, `contact`, `generate_lead`

Measurement ID que viste en Network: **`G-NTXD373H4Q`** (stream web EN dentro de esa propiedad).

### C. Tiempo hasta clic + página (Exploración GA4)

El informe **Eventos** no trae “cuántos segundos tardaron”. Hay que usar **Explorar**:

#### Páginas de origen (ya lo tienes en el export)

En Eventos → clic en `chat:51946622318` → scroll a **Event Label** (título + URL de la página donde clickearon).

O exportar de nuevo con dimensión **Página de destino** / **Título de página**.

#### Tiempo hasta clic WhatsApp

1. GA4 → **Explorar** → plantilla **Embudo de exploración**
2. Pasos:
   - Paso 1: `session_start`
   - Paso 2: `chat:51946622318` (o el nombre exacto del evento)
3. Opciones del embudo → activar **Tiempo entre pasos** (median/average)
4. Segmento opcional: excluir Perú o tráfico interno

Alternativa rápida:

1. **Exploración libre**
2. Filtro: nombre evento = `chat:51946622318`
3. Dimensión: **Ruta de página** (o Event Label)
4. Métrica: **Duración media de la sesión** (proxy burdo — no es tiempo exacto al clic)

Para tiempo exacto sin BigQuery: solo el **embudo con tiempo entre pasos**.


### C. Google Ads — conversiones

Sitio tiene `AW-708879898` y `AW-16457731278`.

1. ads.google.com → conversiones
2. ¿Hay conversión “WhatsApp” o “Click to call”?
3. Ads **no estaba vinculado** a GA4 EN (26 ago) — puede haber datos solo en Ads

### D. Ventas — fuente de verdad (15 min, imprescindible)

Pregunta a **Paloma / Daidys / ventas@**:

> ¿Cuántos chats WhatsApp EN llegaron la última semana?  
> ¿De esos, cuántos venían de la web (vs referido, OTA, Instagram)?  
> ¿Usan el Sheet “seguimiento leads DAI/PALOMA”?

Si el Sheet existe → **esa** es la cifra que Clever respeta.

### E. Formularios + tawk.to

- Contact Form 7 → ¿emails a ventas@? ¿contados?
- tawk.to → panel de chats (Accesos.xlsx)

---

## Qué puedes calcular con datos actuales (sin ventas)

| Ratio | Fórmula | Para qué |
|---|---|---|
| CTR Google | GSC clics / imp | ¿Snippet funciona? (Things MP 0,02%) |
| Clics/día | 643 / 28 ≈ **23** | Demanda orgánica EN |
| Usuarios/día | 606 / 7 ≈ **87** | Tráfico total (todas fuentes) |
| WA clics / sesión | eventos WA / sesiones | **Efectividad web** (necesitas evento) |
| WA → venta | ventas / WA clics | **Solo ventas puede decirlo** |

---

## ¿La web es “efectiva”? Criterios

| Señal | Web SÍ funciona | Web NO convierte (problema landing) |
|---|---|---|
| GSC clics | Suben o estables | Caen sin posición peor |
| WA clics / 100 sesiones | >3–5 (turismo) | <1 |
| Ventas confirman leads web | Sí, recurrentes | “Casi nada del .com” |
| Ads ROAS | Positivo (Lizet) | Queman budget |

**Tráfico sin WA clics** = problema UX/velocidad/CTA (tu POC tiene sentido).  
**WA clics sin ventas** = problema ventas/precio/seguimiento (no es solo SEO).  
**Poco tráfico** = problema SEO/Ads (Things MP, migración URLs).

---

## Migración vs experimento código — marco de decisión

### Costo migración (solo copiar, sin optimizar)

| Contenido | Cantidad | Tiempo/unidad | Horas totales |
|---|---:|---:|---:|
| Tours | 69 | 30–35 min | **~35–40 h** |
| Blogs | 452 | ~15–25 min? | **~110–190 h** |
| **Total equipo** | | | **~150–230 h** |

Una semana full-time = ~40 h → **tours solos ≈ 1 semana** (coincide con lo que dijiste).  
**Blogs = semanas adicionales** para todo el equipo.

### Cuándo migrar igual (aunque la web no convierta)

- Clever ya decidió Drupal
- Riesgo SEO si no hay 301
- Equipo de 4 ya empezó

### Cuándo tiene sentido tu experimento código

- WA clics **existen** pero conversión mala → **landing/CWV** (POC)
- Tráfico alto, CTR bajo → **snippet** (WP/Drupal igual)
- Ventas dice “web no manda nada” pero GSC 643 clics → **medición rota** (arreglar GA4 primero)
- Drupal staging sin WA → **migración empeora** conversión

**No saltes a “rearmar todo en código”** hasta tener **7–28 días** de evento WA en GA4 o datos del Sheet ventas.

---

## Plan recomendado (esta semana)

| Día | Acción |
|---|---|
| **Hoy** | GA4 eventos 28d + test Tiempo real WA |
| **Hoy** | WhatsApp a ventas: “¿cuántos leads web EN/semana?” |
| **Mañana** | GTM preview + marcar conversión WA |
| **Esta semana** | UTMs en enlaces WA (`utm_source=web&utm_medium=whatsapp`) |
| **Paralelo** | Migración tours (mandato equipo) — tú QA SEO |
| **Mes 2** | POC subdominio vs prod con **mismo** evento WA medible |

---

## Script rápido — probar WA en vivo (tú)

1. Incógnito → https://www.perugrandtravel.com/tour/the-classic-salkantay-trek-5d/
2. F12 → **Network** → filtro `google-analytics` o `collect`
3. Clic botón WhatsApp verde
4. ¿Sale petición analytics? → captura para Lizet

---

## Qué decirle a Clever (cuando tengas números)

> “Tenemos ~643 clics Google/mes en EN y ~600 usuarios/semana en GA4. Estoy cruzando clics WhatsApp (GA4/GTM) con ventas (Sheet DAI/Paloma) para saber cuántos leads cierra la web antes de decidir si el cuello de botella es tráfico, landing o ventas. En paralelo, la migración copia catálogo; la optimización CTR y velocidad van en fase 2 medible.”

---

*Relacionado:* `02-empresa/GA4-INVENTARIO.md` · `08-investigacion/CRM-PGT-Y-VECTORIFY.md` · `10-aprendizaje/GA4-POC-GUIA-PASO-A-PASO.md`
