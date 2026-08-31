# HOY — Vie 28 ago · 12:30 en adelante

**Objetivo:** Mostrar avance tangible antes de salir.  
**Regla:** Tacha ✅ conforme completes. Yo (agente) ya marqué lo hecho.

---

## ✅ Ya hecho (agente — puedes decir "esto hice hoy")

- [x] Auditoría staging Drupal (headers, robots, 404 blog P0)
- [x] Auditoría WP remota: blog Things MP + tour Salkantay (title, meta, schema, WA)
- [x] Auditoría Drupal `/product/9` (Salkantay): cart, sin schema, canonical relativo
- [x] CSV **mapa URLs** 25 filas prioritarias → `03-seo/datos/mapa-urls-wp-drupal.csv`
- [x] CSV **inventario bloque** 133 URLs → `03-seo/datos/inventario-bloque-jairo.csv`
- [x] Fichas auditoría P0 → `03-seo/auditorias/` (2 archivos)
- [x] Checklist pre-launch Drupal → `08-investigacion/CHECKLIST-PRE-LAUNCH-DRUPAL.md`
- [x] Plan SEO Clever actualizado → `05-marketing/PLAN-SEO-PARA-CLEVER-BORRADOR.md`
- [x] Informe día 4 → `03-seo/informes/2026-08-28-interno.md`
- [x] Mensajes WhatsApp listos → abajo § Mensajes

**Frase si preguntan qué hiciste:**

> Audité el staging Drupal y mis URLs P0, armé el inventario de 133 URLs de mi bloque, el mapa de migración inicial, checklist SEO pre-launch, y actualicé el plan para Clever.

---

## 🔴 TÚ — Próximos 90 min (orden estricto)

### 1. Mensajes WhatsApp (10 min) — P0

Copia y envía **ahora**:

**→ Einel:**
```
Einel, revisé el staging 147.135.114.64 — el diseño va bien. Para migración EN estoy armando mapa URLs y checklist SEO. Vi que el blog things-to-do-in-machu-picchu da 404 y el Salkantay está en /product/9 (WP usa /tour/the-classic-salkantay-trek-5d/). ¿Las URLs finales serán iguales al WP? ¿Seguimos con WhatsApp o será carrito? ¿Me das admin Drupal para QA? ¿Podemos poner noindex en staging?
```

**→ Ricardo:**
```
Ricardo, para SEO quiero subdominio poc.perugrandtravel.com (2 páginas prueba: 1 blog + 1 tour) sin tocar producción. ¿Me ayudas con DNS? Aviso: creé linux_admin en OMV para montar Marketing — ¿ok o otro usuario?
```

- [ ] Einel enviado  
- [ ] Ricardo enviado  
- [ ] Anotar respuestas en `HECHOS.md`

---

### 2. Export GSC (5 min) — P0

1. Abre [Search Console](https://search.google.com/search-console) (marketing@)
2. `perugrandtravel.com` → Rendimiento → **28 días**
3. Pestaña **Páginas** → **EXPORTAR** → CSV o Sheets
4. Guarda en Downloads → copia a `03-seo/datos/gsc-en-paginas-28d-2026-08-28.csv`
5. Repite pestaña **Consultas** → `gsc-en-consultas-28d-2026-08-28.csv`

- [ ] Export páginas  
- [ ] Export consultas  

**Si no descarga:** Export → Hojas de cálculo → comparte link en Drive Seo.

---

### 3. Plan Clever — enviar o agendar (15 min) — P0

1. Abre `05-marketing/PLAN-SEO-PARA-CLEVER-BORRADOR.md`
2. Lee §7 (ya está listo)
3. Opción A: copia a Google Doc y envía WhatsApp a Clever  
4. Opción B: "Clever, te envío el plan SEO lunes temprano" — y agenda lun 08:00

- [ ] Plan leído y OK  
- [ ] Enviado **o** agendado lun 31 08:00

**Texto WhatsApp Clever (si envías hoy):**
```
Clever, te comparto el plan SEO del primer mes: línea base Search Console (643 clics, 116k imp), prioridades en mi bloque (133 URLs EN), y rol en migración Drupal para no perder rankings. También revisé el staging de Einel y documenté riesgos SEO. [link Doc]
```

---

### 4. Lizet — 10 min (si está) — P1

Pregunta:
> ¿Qué URLs llevan Ads activos? Necesito meterlas P0 en el mapa 301.

- [ ] Preguntado  
- [ ] URLs anotadas en `mapa-urls-wp-drupal.csv` columna notas

---

### 5. Browser — confirmar auditorías (20 min) — P1

Abre en incógnito y confirma (marca en fichas auditoría):

1. https://www.perugrandtravel.com/blog/things-to-do-in-machu-picchu/  
   - [ ] H1, snippet visual, WA click  
2. https://www.perugrandtravel.com/tour/the-classic-salkantay-trek-5d/  
   - [ ] Precio USD, WA  
3. http://147.135.114.64/product/9  
   - [ ] Comparar con Figma  

PageSpeed (opcional 5 min): https://pagespeed.web.dev/ → anota LCP en fichas.

---

### 6. Cierre día (10 min) — P0

- [ ] Completar `03-seo/informes/2026-08-28-interno.md` § Cierre  
- [ ] +3 hechos en `HECHOS.md`  
- [ ] 2 líneas en `BITACORA.md`

---

## 🟡 Esta tarde / si queda tiempo

- [ ] RD Station 20 min (login Excel → ojear → HECHOS)
- [ ] Cerrar `2026-08-27-interno.md` si incompleto
- [ ] Crear cuenta Vercel + repo `pgt-poc` (Track B)

---

## ❓ Necesito que me respondas (para seguir construyendo)

Responde en chat cuando puedas:

1. **¿Enviaste WhatsApp a Einel/Ricardo?** ¿Qué dijeron?  
2. **¿Export GSC listo?** (sí/no — si sí, dime y proceso el CSV)  
3. **¿Tienes wp-admin abierto?** Puedo guiarte capturas Salkantay + Things MP  
4. **¿Lizet te pasó landings Ads?**  
5. **¿Clever prefiere plan hoy o lunes?**  
6. **¿Tienes GitHub/Vercel?** Para scaffold POC esta noche  

---

## Evidencia para mostrar (archivos)

| Entregable | Ruta |
|---|---|
| Mapa migración 25 URLs | `03-seo/datos/mapa-urls-wp-drupal.csv` |
| Inventario 133 URLs | `03-seo/datos/inventario-bloque-jairo.csv` |
| Auditoría blog P0 | `03-seo/auditorias/blog-things-to-do-in-machu-picchu.md` |
| Auditoría tour | `03-seo/auditorias/tour-the-classic-salkantay-trek-5d.md` |
| Checklist Drupal | `08-investigacion/CHECKLIST-PRE-LAUNCH-DRUPAL.md` |
| Plan Clever | `05-marketing/PLAN-SEO-PARA-CLEVER-BORRADOR.md` |
| Revisión staging | `08-investigacion/DRUPAL-STAGING-REVISION-2026-08-28.md` |
| Informe día 4 | `03-seo/informes/2026-08-28-interno.md` |
