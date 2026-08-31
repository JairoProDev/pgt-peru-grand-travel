# Repo (JSON/git) vs base de datos (Payload) — decisión

> Para el cutover EN 2026 y fase post-cutover.

---

## Pregunta

¿Blogs, tours y páginas deben vivir en el **repo** (`src/content/*.json`) o en una **base de datos** (Payload + PostgreSQL)?

---

## Respuesta corta

| Fase | Tours | Blogs | Páginas estáticas |
|------|-------|-------|-------------------|
| **Cutover EN (ahora)** | Repo JSON | Repo JSON | Repo JSON |
| **Mes 1–2 post-cutover** | Payload (+ sync) | Repo JSON | Repo JSON |
| **Largo plazo** | Payload | Payload o repo | Payload hubs; legal en repo |

**No elimines WordPress hasta 30 días post-cutover** con GSC estable — ver abajo.

---

## Por qué repo ahora (cutover v1)

1. **591 URLs SSG** ya generadas — build predecible, rollback = git revert  
2. **Sin Postgres en prod** — Payload aún stub; no bloquear cutover  
3. **SEO parity** — URLs + contenido versionado en PR  
4. **Coste** — Vercel static = barato vs DB + CMS hosting  
5. **Blogs cambian poco** — 455 posts; scrape batch es suficiente v1  

## Por qué Payload después (tours primero)

1. **Precios cambian** — Ops no debe hacer PR en GitHub  
2. **Includes/itinerario** — correcciones frecuentes en top 20  
3. **Temporada / cupos** — campos dinámicos  
4. **Un tour editado** → rebuild parcial o ISR (Next)  

Blogs pueden quedarse en JSON **6–12 meses** si el calendario editorial es bajo (1–4 posts/mes).

---

## Qué va dónde (regla)

| Dato | pgt (docs) | pgt-web repo | Payload DB | WP (legacy) |
|------|------------|--------------|------------|-------------|
| Estrategia, gaps, comparativas | ✓ | — | — | — |
| Contenido publicado EN | snapshot CSV | ✓ JSON | fase 2 | hasta cutover |
| Precios oficiales | validación | scrape | ✓ edit | fuente hasta swap |
| SEO meta | Sheet export | JSON | ✓ | Yoast |
| Imágenes finales | checklist | `/public/` | media library | wp-content |
| Redirects 301 | CSV ref | `data/redirects.json` | — | Rank Math |

---

## ¿Ya terminamos migración blogs y tours?

### Tours — **sí, estructuralmente; no, en profundidad**

| Aspecto | Estado |
|---------|--------|
| 69/69 URLs con JSON + ruta | ✅ |
| Itinerario | ~94% (65/69) |
| Precio | 55/69 numérico; 14 quote-only |
| Includes/excludes | ❌ 0% (scraper roto → **fix listo, falta re-scrape**) |
| Reseñas | ❌ no migradas |
| Categorías/tags del Sheet | ❌ no en JSON |

### Blogs — **sí, catálogo completo**

| Aspecto | Estado |
|---------|--------|
| 452 inventario + 3 extra | ✅ 455 JSON |
| Contenido por secciones | ✅ ~99% |
| Redirects categoría → flat | ✅ 115 URLs |
| Related tours | ✅ mayoría + fallback |

### Páginas — **sí, con matices**

62/62 JSON; destinos profundos a veces solo `childLinks`.

---

## ¿Puedo eliminar tours/blogs de WordPress ya?

**No todavía.** Hipotéticamente el contenido **textual** está en `pgt-web`, pero:

1. **Imágenes** siguen en `wp-content` (hotlink) — borrar WP = imágenes rotas  
2. **Rollback 30 días** — GSC puede penalizar si algo falla  
3. **ES/PT/IT** siguen en otros dominios/WP  
4. **Tourmaster admin** — precios/cupos pueden no coincidir con scrape  
5. **Formularios, OTAs, plugins** no migrados  

### Cuándo sí apagar contenido EN en WP

Checklist:

- [ ] DNS prod → Vercel 30+ días estable  
- [ ] Imágenes top 50 en `/public/` o CDN propio  
- [ ] `validate-parity-v2` ≥95% en URLs con tráfico  
- [ ] Includes/precios top 20 validados por Ops  
- [ ] Backup WP completo (Ricardo)  
- [ ] Modo mantenimiento o redirect global WP → Vercel  

Entonces: **redirect 301 global** desde WP, no borrar DB hasta 90 días.

---

## Recomendación final

1. **Cutover con JSON en repo** — ya está listo técnicamente  
2. **Payload mes 1** — tours editables; import desde `scripts/import-json-to-payload.ts`  
3. **Blogs en repo** hasta que calendario >4 posts/mes justifique CMS  
4. **pgt/** permanece como mapa de verdad, comparativas y exports Drive — nunca reemplaza el runtime  

Ver también: `docs/PAYLOAD-PHASE2.md` (pgt-web), `08-investigacion/ESQUEMA-MIGRACION-MAESTRO.md`.
