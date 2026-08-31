# GA4 para el POC — guía paso a paso (marketing@)

**Objetivo:** Medir visitas y clics WhatsApp en https://pgt-poc.vercel.app  
**Tiempo:** ~20 minutos  
**Cuenta:** marketing@ (la misma de Search Console)

---

## Qué vas a lograr

1. Un **stream web** separado para el POC (no mezclar con perugrandtravel.com prod)
2. Evento **`whatsapp_click`** cuando alguien pulsa WhatsApp
3. Ver datos en **Informes en tiempo real** en 2 minutos

---

## Parte A — Crear stream GA4 para el POC (10 min)

### Paso 1: Entrar a GA4

1. Abre https://analytics.google.com/
2. Inicia sesión con **marketing@**
3. Arriba izquierda: clic en el nombre de la cuenta → elige **Peru Grand Travel**

### Paso 2: Ir a Admin

1. Abajo izquierda: icono **⚙ Admin**
2. Columna central **Propiedad** → **Flujos de datos** (Data streams)

### Paso 3: ¿Stream nuevo o existente?

**Opción recomendada — stream nuevo solo para POC:**

1. Clic **Agregar flujo** → **Web**
2. Si sale aviso *«¿Seguro que quieres crear otro flujo web?»* → **Sí**
   - Es normal. Google prefiere 1 flujo cuando es el **mismo sitio** y el **mismo recorrido de usuario**.
   - Tu POC está en **otro dominio** (`pgt-poc.vercel.app` ≠ `perugrandtravel.com`) → stream separado es lo correcto.
   - No mezcla tráfico de prueba con prod en informes.
3. URL del sitio web: `https://pgt-poc.vercel.app`
4. Nombre del flujo: `proof of concept` (o `POC Next.js`)
5. **Crear flujo** / **Crear y continuar**

### Paso 4: Copiar el Measurement ID

1. Clic en el flujo **`proof of concept`** (lista de flujos de datos)
2. Arriba verás **ID de medición** (no confundir con ID del flujo `15519868398`)

```
ID de medición: G-XXXXXXXXXX
```

**Copia ese `G-XXXXXXXXXX`** — lo necesitas en Vercel.

---

## Parte B — Conectar GA4 al POC en Vercel (5 min)

### Paso 1: Vercel

1. https://vercel.com/jairoprodevs-projects/pgt-poc
2. **Settings** → **Environment Variables**
3. **Add New:**
   - Name: `NEXT_PUBLIC_GA4_ID`
   - Value: `G-XXXXXXXXXX` (el que copiaste)
   - Environment: **Production** ✓
4. **Save**

### Paso 2: Redeploy

1. Pestaña **Deployments**
2. Último deploy → menú **⋯** → **Redeploy**
3. Espera ~1 min

*(Alternativa: push cualquier cambio a GitHub → auto-deploy)*

### Paso 3: Verificar que carga

1. Abre https://pgt-poc.vercel.app/tour/the-classic-salkantay-trek-5d
2. DevTools (F12) → **Network** → filtra `google`
3. Debes ver petición a `googletagmanager.com/gtag/js?id=G-XXXX`

---

## Parte C — Probar en tiempo real (2 min)

### Importante: ¿estás viendo prod o POC?

En **Tiempo real → Páginas**, si ves rutas como `/packages/` o `/machu-picchu-packages/` → es tráfico de **perugrandtravel.com** (stream principal).

El POC se reconoce por rutas como:
- `/tour/the-classic-salkantay-trek-5d`
- `/blog/things-to-do-in-machu-picchu`

O por hostname `pgt-poc.vercel.app` (si la tarjeta lo muestra).

### Pasos para ver `whatsapp_click`

1. **Abre en otra pestaña** (móvil o incógnito):  
   https://pgt-poc.vercel.app/tour/the-classic-salkantay-trek-5d
2. GA4 → menú izquierdo **Informes** → **Resumen en tiempo real**
3. **Baja** en esa misma pantalla hasta la tarjeta **«Número de eventos por Nombre del evento»**  
   *(GA4 en español; en inglés: Event count by Event name)*
4. Pulsa **Contact on WhatsApp** en el POC
5. En ~10–30 s debe aparecer **`whatsapp_click`** en esa tarjeta

Si no aparece:
- DevTools (F12) → Network → filtra `google` → debe cargar `gtag/js?id=G-V8FFS0SCXB`
- Prueba otro clic (botón sidebar o sticky verde abajo-derecha)

### Ver eventos históricos (no solo tiempo real)

1. Menú izquierdo → **Interacción** (desplegar) → **Eventos**
2. Busca **`whatsapp_click`** en la tabla  
   *(Puede tardar 24 h en aparecer aquí; en tiempo real es inmediato)*

### Marcar como conversión

1. **Admin** (⚙ abajo izquierda) → columna Propiedad → **Eventos**
2. Cuando exista `whatsapp_click` → activar **Marcar como conversión**

---

## Parte C-bis — Los 2 flujos de datos (no se «alternan»)

Tienes **2 streams en la misma propiedad** `perugrandtravel.com - GA4`:

| Stream | URL | ID medición |
|---|---|---|
| `perugrandtravel.com - GA4` | prod | (el de siempre) |
| `proof of concept` | `pgt-poc.vercel.app` | `G-V8FFS0SCXB` |

**No hay botón para «cambiar de stream» en informes.** Los dos vienen a la misma propiedad.

| Qué quieres | Cómo |
|---|---|
| Ver config de un stream | Admin → Flujos de datos → clic en el nombre |
| Ver solo tráfico POC | Informes → filtro **Nombre de host** = `pgt-poc.vercel.app` |
| Ver solo prod | Filtro hostname = `www.perugrandtravel.com` |
| Debug de un stream | Admin → Flujos de datos → clic stream → **Ver detalles de etiquetas** |

En **Tiempo real**, abre el sitio que quieres medir; las páginas que aparecen son las que alguien está visitando ahora (prod o POC).

### Si `whatsapp_click` no aparece

1. **¿Ves `page_view` pero no `whatsapp_click`?** → el clic no llegó a GA4. Tras el fix del 28 ago, recarga con **Ctrl+Shift+R** y prueba de nuevo.
2. **DevTools (F12) → Consola** → pega y Enter:
   ```javascript
   gtag('event', 'whatsapp_click', { utm_content: 'test_manual' })
   ```
   Si aparece en Tiempo real en ~15 s → GA4 OK, el botón era el problema.
3. **DevTools → Network** → filtra `collect` o `google-analytics` → debe haber POST al hacer clic.
4. **Desactiva adblocker** en `pgt-poc.vercel.app` (uBlock, Brave shields, etc.).
5. **No uses el WhatsApp del footer** (sin tracking) — usa el botón verde del sidebar o sticky.

---

Así Lizet/Clever ven “leads” en informes.

1. GA4 → **Admin** → **Eventos** (Events)
2. Espera 24 h o usa **Tiempo real** para que aparezca `whatsapp_click`
3. Cuando exista: toggle **Marcar como conversión** (Mark as conversion)

### Evento personalizado (si no aparece solo)

El POC ya envía:

```javascript
gtag('event', 'whatsapp_click', { utm_content: 'tour_salkantay_5d_sidebar' });
```

Valores `utm_content` útiles:

| Página | utm_content |
|---|---|
| Tour sidebar | `tour_salkantay_5d_sidebar` |
| Tour sticky | `tour_salkantay_5d_sticky` |
| Blog | `blog_things_machu_picchu` |

---

## Parte E — Informe simple para Clever (opcional)

1. GA4 → **Explorar** → **Exploración en blanco**
2. Dimensiones: `Página` + `Nombre del evento`
3. Métricas: `Usuarios` + `Recuento de eventos`
4. Filtro: evento = `whatsapp_click`
5. Exportar captura

---

## Preguntas frecuentes

### ¿El POC aparecerá en GSC?

Solo si Google lo indexa (`pgt-poc.vercel.app` está indexable desde 28 ago). GSC de **prod** no mezcla datos con el POC salvo que añadas la propiedad vercel.app en Search Console (no urgente).

### ¿Mezcla datos con perugrandtravel.com?

**No** si creaste stream separado `POC Next.js`. Propiedad EN (`368486554`) sigue siendo prod; el stream POC es aparte dentro de la misma propiedad o cuenta.

### ¿Puedo usar la misma propiedad EN?

**Sí.** Añade un **segundo stream web** en propiedad `perugrandtravel.com` (368486554) con URL `pgt-poc.vercel.app`. Más limpio que mezclar URLs en un solo stream.

### ¿Qué le digo a Lizet?

> Monté GA4 en el POC interno. Cuando haya tráfico de prueba, el evento whatsapp_click mide clics al botón. ¿Lo cruzamos con Ads landings?

---

## Checklist final

- [x] Stream GA4 creado para `pgt-poc.vercel.app` → **`G-V8FFS0SCXB`**
- [x] `NEXT_PUBLIC_GA4_ID` en Vercel (28 ago tarde)
- [x] Redeploy hecho
- [ ] Tiempo real muestra visita **al POC** (ruta `/tour/...`, no `/packages/`)
- [ ] Click WA genera `whatsapp_click`
- [ ] (Opcional) Marcado como conversión
- [ ] Measurement ID anotado en `HECHOS.md` (sin commitear secretos)

---

## Cuando me des el G-XXXXXXXX

Escríbelo en chat y lo configuro en Vercel por ti + redeploy automático.

---

*Relacionado:* `pgt-poc/MEDIR-RESULTADOS.md` · `02-empresa/GA4-INVENTARIO.md`
