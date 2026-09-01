# Experimento 4 personas + migración Drupal — estrategia Jairo

**Fecha:** lun 1 sep 2026  
**Contexto nuevo:** Einel da accesos Drupal con autoría individual; carpeta assets ordenada; capacitación Drupal → **Ricardo** (no Jairo); Clever quiere ver qué estrategia funciona mejor entre los 4 del cuarteto SEO.

---

## Lo que cambió (y qué NO significa)

| Hecho | Lo que NO es | Lo que SÍ es |
|---|---|---|
| Ricardo será admin Drupal | Que Ricardo sea jefe de marketing | Que Clever quiere **redundancia** (no depender de una persona) |
| Migración manual con assets | Que tu código no sirve | Fase 1 inevitable; automatizas **QA y medición**, no cada clic |
| Experimento entre 4 | Guerra interna | **Oportunidad** si defines métricas iguales para todos |
| Tu stack / servidor propio | Reemplazar Drupal mañana | **Pista B** en paralelo — demo medible |

**Miedo de Clever:** “¿Y si Jairo se va y nadie puede tocar las páginas?”  
**Respuesta ganadora:** no “yo controlo todo”, sino **“construyo sistema + documentación + herramientas que Ricardo/Lizet/Arely también usan”**.

---

## Dos pistas — corre las dos

```
PISTA A (obligatoria)              PISTA B (tu diferenciador)
─────────────────────              ───────────────────────────
Migrar bloque 3 tours + 4 blogs    1 URL en tu stack (POC)
en Drupal con Einel/Ricardo        Salkantay 5D · subdominio
Manual contenido + assets          Automatización + métricas
Dueño: SEO QA + especificaciones   Dueño: velocidad + schema + WA
```

**Ganas el experimento** si en la tabla comparativa de Clever apareces con:
- Mismas URLs / menos errores SEO
- Mejor Lighthouse (pista B)
- Medición clara (GSC + GA4 WA)
- Menos tiempo de QA (scripts)

---

## Scorecard — proponer al cuarteto (misma regla para los 4)

| Métrica | Cómo medir | Frecuencia |
|---|---|---|
| URLs migradas sin 404 | `check-urls.sh` | Semanal |
| Checklist SEO (10 ítems) | `MIGRACION-SEO-CAMPO-A-CAMPO.md` | Por URL |
| Tiempo migración por URL | Minutos anotados | Por URL |
| CTR top 3 URLs bloque | GSC | Semanal |
| Clics → WA | GA4 `whatsapp_click` | Semanal |
| Lighthouse mobile perf | PageSpeed | 1× por tour piloto |
| Errores GSC nuevos | Search Console | Semanal |

**Propón esto en el grupo WA** — quien define las reglas del juego tiene ventaja.

---

## ¿Qué tan automatizable es la migración?

### Manual (no pelees — 60–70% del trabajo)

- Primera carga de contenido en Drupal (textos, párrafos, itinerarios)
- Subir assets desde carpeta de Einel (imágenes, PDFs)
- Decisiones editoriales (qué bloque va dónde)
- Ajustes visuales finos en Drupal

### Semi-automatizable (tu aporte visible — 20–30%)

| Tarea | Herramienta | Quién |
|---|---|---|
| Lista meta title/desc por URL | CSV desde Sheet keywords | Jairo export → todos importan |
| Validar URL WP = Drupal | `03-seo/scripts/check-urls.sh` | Jairo / cualquiera |
| Renombrar assets si hay convención | Script bash + regex slug | Jairo una vez, doc para Ricardo |
| Checklist post-migración | Agente + checklist markdown | Jairo |
| Mapa 301 masivo | CSV → módulo Redirect Drupal | Ricardo implementa, Jairo especifica |

### Automatizable (10% — alto impacto)

| Tarea | Cómo |
|---|---|
| Diff title/meta WP vs Drupal | Script curl + comparar |
| Schema validation | rich-results test batch |
| Lighthouse regression | CI en POC / script semanal |
| GSC → Sheet sync | Apps Script (tu idea en DUDAS.md) — **gran aporte** |
| Alertas 404 post-cutover | GSC API o crawl semanal |

**Frase para Einel:** “La migración de contenido es manual; yo automatizo que **no se rompa SEO** al migrar.”

---

## Ricardo — aliado, no rival

Ricardo admin Drupal **reduce tu carga**, no te quita el puesto.

| Ricardo hace bien | Tú haces mejor |
|---|---|
| Accesos, cPanel, NAS, redirects nginx | Medición GSC/GA4, schema, CTR |
| Operaciones día a día | POC velocidad, scripts, agents |
| Relación con Clever histórica | Informes con datos + riesgo migración |

**Hoy dile algo así:**

> Ricardo, en mi bloque llevo checklist SEO por URL. Cuando migres o valides en Drupal, yo paso QA en 5 min con script — te mando reporte, no te bloqueo. Si quieres, documentamos juntos dónde van title/meta en Drupal.

**No digas:** “Yo haría todo en código y no necesitaríamos Drupal.”

---

## Pista B — tu stack (1 página, dominio controlado)

**URL objetivo:** Tour Salkantay 5D  
**WP prod:** `/tour/the-classic-salkantay-trek-5d/`  
**POC ya existe:** https://pgt-poc.vercel.app/tour/the-classic-salkantay-trek-5d

### Dónde hostear (responde al miedo “una sola persona”)

| Opción | Bus factor | Recomendación |
|---|---|---|
| Tu laptop solo | 🔴 Peor | No |
| Vercel + GitHub (ya tienes) | 🟢 Cualquiera con acceso repo despliega | **Sí ahora** |
| `poc.perugrandtravel.com` | 🟢 DNS en empresa, código en GitHub | Pedir Ricardo esta semana |
| Servidor propio random | 🔴 Clever no controla | No sin OK |

**No pidas “servidor propio mío”** — pide **subdominio empresa + repo compartido**. Mismo poder técnico, cero miedo de dependencia.

### Qué demostrar en 2 semanas (Pista B)

1. Lighthouse mobile **≥95** vs WP **55**
2. JSON-LD TouristTrip + Product + FAQ
3. `whatsapp_click` con UTM en GA4
4. Mismo contenido/precio que WP
5. README: “cómo desplegar sin Jairo” (3 comandos)

---

## HOY lunes 1 sep — checklist

### Mañana (con Einel / accesos)

- [ ] Entrar Drupal con tu usuario; confirmar rol (¿puedes editar tours y blogs?)
- [ ] Ubicación carpeta assets; convención nombres
- [ ] Preguntar: slug final tours (`/tour/...` vs `/product/N`)
- [ ] Preguntar: campos SEO (title, meta) en Drupal
- [ ] Preguntar: WA o cart en prod
- [ ] Anotar quién migra qué URL primero (piloto)

### Tarde (solo tuyo — 2 h)

- [ ] Export GSC bloque → `03-seo/datos/`
- [ ] Baseline 1 URL piloto (WP curl: title, meta, schema)
- [ ] Correr `check-urls.sh` contra staging
- [ ] Elegir **1 tour** pista A (Salkantay) + confirmar POC pista B
- [ ] Mensaje grupo: proponer scorecard (5 métricas)

### No hacer hoy

- Construir CRM
- Prometer reemplazar Drupal
- Competir abiertamente con Ricardo
- Migrar 10 URLs sin checklist

---

## De aquí al 25 sep (ajustado)

| Semana | Pista A (Drupal) | Pista B (código) | Política |
|---|---|---|---|
| 1 (sep 1–7) | 1 tour + 1 blog piloto QA | POC Salkantay + README deploy | Alianza Ricardo |
| 2 | 5 tours bloque 3 | Subdominio poc.* si Ricardo OK | Scorecard semanal |
| 3 | Blogs P0 (Things MP spec) | GSC sync Sheet (automatización) | Informe Clever |
| 4 | Mapa 301 completo | Informe A vs B Lighthouse + leads | Pedir S/ 5.000 |

---

## Frase para Clever (experimento 4)

> “Mi estrategia: migración Drupal sin perder URLs, con checklist automatizado, y en paralelo una pista técnica en subdominio que demuestra el techo de velocidad y medición WA. Todo documentado para que no dependa de una sola persona.”

---

*Relacionado:* `mi-carrera/PLAN-30-DIAS-5000.md` · `02-empresa/EQUIPO-SEO.md` · `mi-carrera/CMS-CUSTOM-VIABILIDAD.md`
