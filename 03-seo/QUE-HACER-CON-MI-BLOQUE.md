# Qué hacer con TU bloque (tours 3 + blogs 4)

**Fecha:** 26 ago 2026  
**Datos:** ya analizados en `ANALISIS-BLOQUE-JAIRO-2026-08-25.md`  
**CSV:** `datos/tours-jairo-2026-08-25.csv` (18) · `datos/blogs-jairo-2026-08-25.csv` (115)

---

## 1. La confusión (y la respuesta)

| Pensabas | Realidad |
|---|---|
| “Tengo que optimizar 115 blogs ya” | No. Tienes que **ser dueño** de esas URLs |
| “La tabla es para editar keywords todo el día” | La tabla es **inventario + prioridades + input del mapa 301** |
| “Si no toco WordPress no aporto” | En migración, el aporte #1 es **no perder URLs/Ads/GSC** |
| “El agente lo hace todo” | Yo priorizo, redacto, armo sheets; **tú** abres páginas, GSC, staging, hablas con el equipo |

---

## 2. ¿Qué puedo hacer YO (agente) por ti?

| Ya hice / puedo hacer | Necesito de ti |
|---|---|
| Sumar clics/impresiones, priorizar ROI | — (CSV ya está) |
| Lista ordenada “haz esto primero” | — |
| Borrador titles/metas para top URLs | Que confirmes si puedes editar Yoast/Rank Math o solo proponer |
| Plantilla mapa `url_wp → url_drupal → 301` | URL staging + si aliases serán iguales |
| Revisar Twig/schema cuando pegues código | Archivos o capturas |
| Informes diarios | Tus tiempos + hechos |

**No puedo** (sin acceso peligroso): entrar yo solo a wp-admin/Drupal prod, aplicar 301 en servidor, hablar con Lizet.

---

## 3. Qué haces TÚ esta semana (checklist con ⏱)

### Día 2–3 (26–27 ago)

| ☐ | ⏱ | Tarea | Hecho cuando |
|---|---|---|---|
| [ ] | 20 | Abrir GSC → export Páginas 28 días | CSV en `03-seo/datos/gsc-pages-2026-08-26.csv` |
| [ ] | 15 | Pedir staging Drupal + usuario | URL anotada en bitácora |
| [ ] | 15 | Lizet: 5–20 landings Ads | Lista en Sheet o chat |
| [ ] | 45 | **Auditar en navegador** blog #1: [Things to Do in Machu Picchu](https://www.perugrandtravel.com/blog/things-to-do-in-machu-picchu/) | Notas: title, H1, WA links a tours, schema (view-source) |
| [ ] | 30 | Igual blog #2: Museums in Machu Picchu | Idem |
| [ ] | 30 | Tour #1: Salkantay 5d | Precio, moneda, WA, title |

### Día 4–5

| ☐ | ⏱ | Tarea |
|---|---|---|
| [ ] | 60 | Empezar Sheet **mapa URLs** (columnas abajo) — pegar las 18 tours + top 30 blogs por impresiones |
| [ ] | 40 | Tutorial Drupal en staging: `10-aprendizaje/drupal/10-TUTORIAL-EXPLORAR-DRUPAL.md` |
| [ ] | 20 | Anotar: URL limpia vs URL con categoría (¿cuál abre? ¿cuál indexa GSC?) |

### No esta semana

- Reescribir 20 posts  
- Cambiar slugs en producción  
- Prometer “yo migro Drupal”

---

## 4. Columnas del Sheet mapa (cópialas)

```
tipo | titulo | url_wp | url_alternativa_gsc | clics | impresiones | posicion | url_drupal_prevista | accion (igual|301|410) | prioridad (P0 ads|P1 top clicks|P2 resto) | notas_auditoria
```

- **P0:** landings Ads (Lizet)  
- **P1:** blogs top 10 + tours quick win  
- **P2:** resto de tu bloque  

Si me pegas “aliases serán iguales a WP”, yo te genero el CSV borrador de las 18+115 con `accion=igual` y prioridades ya marcadas.

---

## 5. Prioridad concreta (no inventes otra lista)

### Hoy / mañana — solo estas 3 URLs

1. **Blog** Things to Do in Machu Picchu — pos ~5.8 · 6.115 imp · 1 clic → **CTR**  
2. **Blog** Museums in Machu Picchu — pos ~6.3 · 2.494 · 1 clic → **CTR**  
3. **Tour** Salkantay SKY Trek 5 days — pos ~26.8 · 1.218 imp → **acercar a top 10**

Para cada una anota en un doc o Sheet:

- Title actual (pestaña del navegador / Yoast)  
- Meta description  
- ¿Hay botón WhatsApp visible sin scroll eterno?  
- ¿Enlaces a fichas tour relacionadas?  
- ¿URL con `/blog/cusco/...` redirige a la limpia?

Eso **es** trabajo de tu bloque. No hace falta tocar las otras 112 todavía.

---

## 6. Cómo se conecta con Drupal

| Tu bloque en WP | En migración |
|---|---|
| 18 tours | 18 nodes Tour (o los que existan) — mismos aliases o 301 |
| 115 blogs | 115 nodes Article — **decidir canónica** limpia vs categoría |
| Keywords del Sheet | Sirven para Metatag title, no para “rellenar densidades” |

Cuando exista staging: busca **un** tour tuyo y compara campo a campo con WP (precio, body, WA). Anota gaps → eso es oro para la reunión.

---

## 7. Si te preguntan “¿qué avanzaste?”

> Tengo 18 tours y 115 blogs asignados. Baseline del Sheet: ~20k imp tours, ~100k blogs, CTR roto en top 10. Audité [N] URLs prioritarias y armé el mapa de redirecciones de mi bloque para Drupal. Export GSC con fecha [X].

---

## 8. Siguiente paso inmediato (ahora mismo)

1. Si tienes 45 min: audita URL #1 (Things to Do in Machu Picchu) con la lista del §5.  
2. Pégame tus notas (o capturas de title/meta) → te devuelvo title + meta + enlaces internos sugeridos.  
3. Si ya hay staging: abre `10-TUTORIAL-EXPLORAR-DRUPAL.md` y sigue los pasos.
