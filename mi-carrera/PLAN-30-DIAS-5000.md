# Plan personal — 30 días hacia S/ 5.000 (jefatura mkt + tecnología)

**Inicio:** 29 ago 2026 · **Revisión oral:** ~25 sep 2026  
**Sueldo hoy:** S/ 3.500 · **Meta:** S/ 5.000 + rol jefatura  
**Contexto nuevo:** Lunes arranca migración Drupal EN; Einel capacita tours → blogs.

---

## La verdad que necesitas oír

### Tu trabajo en Things MP **sí sirve** — no es basura por la migración

| Lo que hiciste en WP | Lo que se convierte en la migración |
|---|---|
| Title/meta optimizados | **Especificación** para replicar en Drupal (campos SEO del tour/blog) |
| H1 + intro + bloque tours | **Plantilla de contenido** que Einel/Ricardo copian al migrar |
| GSC indexación + baseline | **Línea base pre-cutover** — sin esto no puedes probar que no perdiste tráfico |
| Rank Math checklist | **Checklist QA** por URL migrada (mismo criterio, otro CMS) |

**Sin tu trabajo de ayer:** migrarían el blog con el title largo viejo y perderían el win de CTR.  
**Con tu trabajo:** eres quien dice *“esta URL debe quedar así en Drupal”*.

La migración no invalida SEO — **multiplica** tu valor si eres dueño del cutover.

### Por qué te sientes insignificante (y cómo voltearlo)

| Sensación | Realidad | Acción |
|---|---|---|
| “Copy-paste en CMS” | Mes 1 = migración; copy es inevitable **una vez** | Automatiza QA con scripts/agents, no el copy |
| “Einel hace el sitio” | Einel hace **Drupal + CRM template**; tú haces **no perder Google + medir leads** | Roles complementarios, no competencia pública |
| “Código es mejor” | Sí para velocidad, schema, medición — **no** para reemplazar Drupal que ya decidieron | Código = capa de demostración + herramientas internas |
| “CRM lo haré mejor” | Probablemente sí a largo plazo — **ahora** te quemarías | Fase 2: diseño + integración; no construir en agosto |

---

## Tu propuesta de valor (lo que Clever paga S/ 5.000)

No vendas “sé SEO”. Vende **tres cosas medibles**:

```
┌─────────────────────────────────────────────────────────────┐
│  1. CUTOVER SIN PERDER TRÁFICO (dueño SEO migración)        │
│     Mapa 301 · URLs iguales · schema · GSC · staging QA     │
├─────────────────────────────────────────────────────────────┤
│  2. MÁS LEADS POR VISITA (CTR + conversión WA)              │
│     Things MP + Museums MP · GA4 whatsapp_click · UTMs      │
├─────────────────────────────────────────────────────────────┤
│  3. CAPA TÉCNICA (código donde CMS es lento)                │
│     POC Lighthouse · validadores · agents · informes auto   │
└─────────────────────────────────────────────────────────────┘
```

**Jefe de marketing + tecnología** = quien une Lizet (ads), Einel (web), Ricardo (infra) y **datos** — no quien pelea por el teclado de Drupal.

---

## Semana a semana (29 ago → 25 sep)

### Semana 1 (29 ago – 4 sep) — Migración arranca

| Día | Entregable | Para quién |
|---|---|---|
| Sáb 29 | Baseline GSC export + checklist staging delta | Tú |
| Lun | Reunión Einel: preguntas SEO (abajo) + pedir slug WP = Drupal | Einel |
| Mar–vie | **1 tour piloto** migrado con tu QA (Salkantay 5D) | Einel + tú |
| Vie | Informe 1 pág: estado migración SEO | Clever |

**Preguntas para Einel (lunes):**

1. ¿Pathauto dejará `/tour/the-classic-salkantay-trek-5d/` o `/product/9`?
2. ¿Dónde van title SEO y meta en Drupal? (módulo, campos)
3. ¿WhatsApp o cart en producción? Clever mide WA.
4. ¿Cuándo blogs? ¿Misma URL `/blog/things-to-do-in-machu-picchu/`?
5. ¿Puedo tener export de 1 tour para validar schema?

### Semana 2 (5–11 sep) — Tours bloque Jairo

- Migrar/validar **5 tours P1** con checklist (`CHECKLIST-PRE-LAUNCH-DRUPAL.md`)
- POC Salkantay: informe antes/después Lighthouse para Clever
- GA4: `whatsapp_click` conversión + 1 dashboard Looker (opcional)
- CTR WP: **Museums MP** (si blogs aún en WP)

### Semana 3 (12–18 sep) — Blogs + 301 masivo

- Mapa 301 completo 133 URLs bloque
- Blogs P0 en Drupal sin 404
- Replicar plantilla Things MP en 2–3 blogs migrados
- Script/agent: validar redirects (curl batch)

### Semana 4 (19–25 sep) — Cierre revisión

- GSC comparativa pre/post (aunque cutover sea parcial)
- 1 página Clever: riesgos + lo hecho + próximo trimestre
- WhatsApp pacto S/ 5.000 (`REVISION-1-MES.md`)
- CRM: **solo** brief 1 pág “fase 2” si Clever pregunta — no demo

---

## Sábado 29 (9:00–12:00) — sprint 3 horas

Ver `01-situacion/SABADO-29-SPRINT.md`.

---

## Código vs CMS — regla de oro

| Hazlo en código | Hazlo en CMS (Drupal/WP) |
|---|---|
| Validadores (301, schema, lighthouse) | Contenido y campos SEO por URL |
| POC demo velocidad | Producción que Clever ya aprobó |
| Agents que auditan 133 URLs | Migración que hace Einel |
| GA4/GSC automatización | Title/meta que tú **especificas** |
| Informes para Clever | No reescribir 2000 palabras |

**Tu ventaja:** un agente que revise 18 tours en 5 minutos > 3 horas de clics manuales.

---

## CRM — postura inteligente (no te quemes)

Einel probablemente use plantilla (RD Station, HubSpot, o custom Drupal). **No digas “lo haré 100x mejor” en público.**

| Ahora (sep) | Después (oct+) |
|---|---|
| Mapear flujo WA → ventas (brief ya en repo) | Proponer **capa de atribución**: UTM + GA4 + evento WA |
| Preguntar: ¿Sheet DAI/Paloma sigue activo? | Integración sitio → CRM vía webhook (tu código) |
| Medir `whatsapp_click` en GA4 | Dashboard leads por URL/idioma |

Ver `08-investigacion/CRM-PGT-Y-VECTORIFY.md` — no construir CRM mes 1.

---

## Criterios S/ 5.000 (propón tú el 25 sep)

1. ✅ Mapa URL + 301 bloque Jairo validado  
2. ✅ Checklist SEO ejecutado en ≥10 URLs migradas  
3. ✅ GSC baseline + seguimiento documentado  
4. ✅ 1 win CTR medible (Things MP o Museums MP)  
5. ✅ POC técnico + informe Lighthouse entregado a Clever  
6. ✅ GA4 conversión WA configurada  
7. ✅ Sin guerra con Einel — coordinación visible  

---

## Una frase para Clever (practica)

> “Migré el SEO sin perder URLs: baseline GSC, checklist por tour, y el blog Things MP ya optimizado para cuando entre a Drupal. El POC demuestra que podemos tener páginas 2× más rápidas con el mismo contenido. Siguiente: medir WhatsApp como conversión y cerrar el mapa 301 del bloque inglés.”

---

*Relacionado:* `07-negociacion/REVISION-1-MES.md` · `08-investigacion/MIGRACION-WP-DRUPAL-PLAYBOOK.md` · `03-seo/informes/2026-08-29-decision-pagina-codigo.md`
