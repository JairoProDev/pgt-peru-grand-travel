# Decisión — qué página llevar con código (análisis 29 ago 2026)

**Pregunta:** ¿Cuál URL, dominio y mercado conviene reconstruir en código para demostrar mejoras radicales y más leads?

**Respuesta corta:**  
**Dominio** `perugrandtravel.com` (EN) · **Mercado** US/UK/CA/AU · **Página** `/tour/the-classic-salkantay-trek-5d/` (Salkantay 5D).  
**Blogs CTR** (Things MP, Museums MP) → seguir en **WordPress** (Rank Math), no duplicar en código.

---

## Fuentes usadas

| Fuente | Qué aporta |
|---|---|
| `PRIORIDAD-ACCION-JAIRO-2026-08-26.csv` | 133 URLs bloque Jairo: imp, clics, posición |
| `GSC-LINEA-BASE-2026-08-27.md` | Sitio EN: 643 clics / 116k imp / CTR 0,6% |
| `tours-jairo-2026-08-25.csv` | 18 tours asignados |
| `GA4-INVENTARIO.md` | EN ~606 usuarios/7d; **eventos clave = 0** (WA no marcado) |
| `LIGHTHOUSE-COMPARATIVA.md` | Salkantay: WP 55 vs POC **100** perf |
| HECHOS | Migración solo inglés; Clever = leads WA |

---

## Marco: dos tipos de “win” (no mezclar)

| Tipo | Motor | Métrica | Herramienta | Ejemplo |
|---|---|---|---|---|
| **A — CTR snippet** | Ya en página 1, nadie hace clic | Impresiones × CTR | WP + Rank Math | Things MP (6k imp, 0,02% CTR) |
| **B — Página comercial** | Posición media + velocidad + conversión | Clics → `whatsapp_click` | Código (Next.js POC) | Tour Salkantay 5D |

**Error común:** reconstruir en código un blog que solo necesita title/meta (win barato en WP).  
**Error común:** optimizar snippet de un tour en posición 50 (necesita meses de autoridad).

---

## Ranking por potencial (datos reales 28d GSC)

### Blogs — volumen vs posición

| URL / keyword | Imp | Clics | Pos | CTR | Veredicto |
|---|---:|---:|---:|---:|---|
| best time to travel to peru | 10.711 | 0 | 80,9 | 0% | Volumen enorme, **página 8** — proyecto editorial, no weekend |
| is it safe to go to peru | 9.102 | 1 | 40,6 | 0,01% | Info; baja intención compra |
| **Things to Do in Machu Picchu** | **6.115** | 1 | **5,8** | 0,02% | **Mejor CTR quick win** — ya en WP ✅ |
| climate in Peru | 6.674 | 0 | 49,4 | 0% | Mismo problema posición |
| **Museums in Machu Picchu** | **2.494** | 1 | **6,3** | 0,04% | **Siguiente CTR WP** (lun) |
| peru one week itinerary | 4.637 | 0 | 59,9 | 0% | Planificación; leads indirectos |

### Tours — intención comercial (tu bloque)

| Tour | Imp | Clics | Pos | Por qué importa |
|---|---:|---:|---:|---|
| Salkantay 4D | 3.259 | 1 | 51,5 | Más imp, peor pos — largo plazo |
| Maras Moray day | 2.816 | 1 | 46,9 | Day tour, pos lejana |
| **Salkantay 5D** | **1.218** | 1 | **26,8** | **Producto estrella + POC listo** |
| Machu Picchu Challenge 8D | 589 | 1 | **10,1** | Mejor posición tour; menos volumen |
| Machu Picchu Express 3D | 528 | 1 | 29,8 | MP express — buen 2º candidato código |
| Machu Picchu Challenge 8D | 589 | 1 | 10,1 | Quick win ranking si solo snippet |

### Sitio completo (fuera bloque Jairo)

| URL | Imp | Clics | Nota |
|---|---:|---:|---|
| Home | 3.525 | 228 | 35% clics sitio — no tocar sin Clever |
| Costa Verde Lima | 8.740 | 12 | CTR roto pero **no es tu mercado core** (Lima day trip) |

---

## ¿Qué dominio y mercado?

| Opción | Estado migración | GA4 / GSC | Recomendación |
|---|---|---|---|
| **perugrandtravel.com (EN)** | Fase 1 decidida | Tu bloque, tu GSC | **Sí — único foco** |
| viajesmachupicchutours.com (ES) | Después | Otra propiedad | No ahora |
| machupicchupacotes.com (PT) | Después | Más tráfico GA4 que EN | No ahora — equipo Brasil |

**Mercado:** viajeros **angloparlantes** (US, UK, CA, AU) buscando treks/MP. Es quien usa EN y quien Clever quiere como lead calificado.

---

## Recomendación: Salkantay 5D en código

**URL:** `https://www.perugrandtravel.com/tour/the-classic-salkantay-trek-5d/`  
**POC:** https://pgt-poc.vercel.app/tour/the-classic-salkantay-trek-5d

### Por qué gana sobre otras opciones

| Criterio | Salkantay 5D | Things MP (código) | Best time Peru (código) | MP Express 3D |
|---|---|---|---|---|
| Intención compra | Alta (trek $731) | Media (info → tour) | Baja (planificación) | Alta |
| Mejora técnica demostrable | **LCP 6,8s → 1,4s** | Blog ya pesado WP | Contenido largo | Similar a Salkantay |
| POC ya hecho | ✅ | Parcial (blog) | No | No |
| Plantilla migración Drupal | Tour = sí | Blog = otro equipo | N/A | Sí, pero menos datos |
| Medición leads | `whatsapp_click` | Indirecto | Muy indirecto | Sí |
| Datos GSC | 1.218 imp | 6.115 imp (WP CTR mejor) | 10.711 imp pos 81 | 528 imp |

### Qué demuestras a Clever (narrativa)

1. **Velocidad:** Lighthouse 55 → 100 (captura ya en repo).
2. **GEO:** FAQ + TouristTrip JSON-LD (citaciones IA).
3. **Conversión:** WA sticky + evento GA4 medible (vs cart Drupal).
4. **Migración:** Misma URL, mismo contenido, stack moderno — patrón para 18 tours.

### Qué NO prometer

- “Duplicar clics de Things MP en 48 h” en el tour — pos 26 necesita tiempo + enlaces internos.
- Reemplazar prod sin Ricardo/Clever — POC en subdominio o Vercel con canonical a prod.

---

## Plan dual (lo correcto)

```
Track A — WP (CTR, esta semana)     Track B — Código (demo + migración)
─────────────────────────────────   ────────────────────────────────────
Things MP ✅ hecho                   Salkantay 5D POC → siguiente nivel
Museums MP (lun, 45 min)             Schema + CWV + WA conversion
No código                            Informe Clever con antes/después
```

---

## Sábado 29 — acciones concretas

1. **10 min** — GSC baseline Things MP (imp/clics/CTR hoy).
2. **Opcional 2h** — POC Salkantay: re-test Lighthouse, FAQ schema, sticky WA, UTM `?utm_source=organic`.
3. **5 min** — GA4 EN: `whatsapp_click` → conversión.
4. **Anotar** canibalización `/Home/Cusco` vs `/blog/things-to-do-in-machu-picchu/` para Ricardo.

---

## Siguiente blog WP (no código)

**Museums in Machu Picchu** — 2.494 imp, pos 6,3, mismo playbook Things MP.
