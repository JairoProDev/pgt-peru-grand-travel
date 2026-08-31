# Insights — Keywords, URLs y canibalización (31 ago 2026)

**Periodo GSC:** últimos **16 meses** (no 28 días — cifras más grandes que línea base agosto).

---

## Verdad #1: El blog trae el tráfico, no los tours

| Tipo | URLs | Clics GSC (16m) | % del tráfico contenido |
|---|---:|---:|---:|
| **Blog** | 454 | **20.649** | **~63%** |
| **Páginas** | 69 | **12.256** | **~37%** |
| **Tours** | 73 | **251** | **~0,8%** |

**Implicación greenfield:**
- Priorizar **velocidad + CTA en blogs** (no solo tour pages)
- Tours = conversión directa (ads, hubs) más que SEO orgánico masivo
- Un sitio “solo bonito en tours” **no aprovecha** el 63% del tráfico

---

## Verdad #2: Home y hubs son el dinero orgánico + ads

| Página | Clics (16m) | Impresiones | CTR |
|---|---:|---:|---:|
| **Home** | 6.325 | 158.728 | 4,0% |
| **/machu-picchu-packages/** | 2.361 | 363.994 | 0,65% |
| **/packages/** | 757 | 278.047 | 0,27% |
| Costa Verde (destino) | 451 | 212.839 | 0,21% |

Coincide con GA4 WA: packages + machu-picchu = top conversión.

**Implicación:** MVP greenfield **no puede** ser solo tour — home + packages son P0.

---

## Verdad #3: Things MP es el mayor desperdicio de impresiones

| URL | Clics | Impresiones | CTR | Posición |
|---|---:|---:|---:|---:|
| `/blog/things-to-do-in-machu-picchu/` | **1** | **6.115** | **0,016%** | ~5,8 |

6.115 impresiones casi gratis — **1 clic**. Tu optimización CTR es correcta y urgente.

**Otros blogs alto volumen / bajo CTR** (candidatos optimización):

| Blog | Clics | Impresiones | CTR |
|---|---:|---:|---:|
| animals of peru | 296 | 199.812 | 0,15% |
| Huacachina (canónica) | 111 | 64.276 | 0,17% |
| Virgin Candelaria | 190 | 79.996 | 0,24% |

---

## Verdad #4: Top blogs que SÍ funcionan (modelo a copiar)

| Blog | Clics | CTR | Keyword |
|---|---:|---:|---|
| What to wear Machu Picchu | **3.539** | **2,45%** | what to wear to machu picchu |
| Coca tea | **1.360** | 0,55% | coca tea |
| Day of saints and dead | 873 | 1,20% | day of the saints and dead |
| Hot springs Aguas Calientes | 796 | 0,71% | Aguas Calientes |
| Altitude sickness | 750 | 2,36% | altitude sickness peru |
| Things to do Huaraz | 356 | 0,60% | things to do in huaraz |

**Patrón:** pregunta concreta del viajero + título directo + CTR >0,5%.

---

## Verdad #5: Tours — poco tráfico orgánico individual

| Tour (top) | Clics (16m) |
|---|---:|
| Colonial Lima 9D | 33 |
| Andean Wedding | 24 |
| Belmond Explorer 10D | 23 |
| Condor Canyon | 19 |

Solo **3 tours en top 10 Google**. El catálogo tour es para **cerrar venta**, no para SEO masivo.

---

## Canibalización — 54 grupos, 104 URLs

Criterios: keyword principal idéntica, keywords compartidas, títulos ≥60% términos comunes.

### Top grupos por impacto (impresiones)

| Grupo | Keyword | Canónica | Imp total aprox |
|---|---|---|---|
| 1 | aguas calientes | hot-springs-in-aguas-calientes | ~114k |
| 2 | virgin of candelaria | virgin-of-candelaria-2026 | ~98k |
| 3 | huacachina | legend-of-huacachina-ica | ~85k |
| 4 | things to do in huaraz | the-best-things-to-do-in-huaraz | ~61k |
| 5 | things to do in machu picchu | things-to-do-in-machu-picchu | canibaliza con `/Home/Cusco` |

**Acción greenfield:** implementar `redirects-blog-301.csv` (454 reglas) + fusionar canónicas del Excel.

---

## Spam — 24 URLs excluidas

Inyección portugués en `/vip/` y `/apps/` (apuestas). **24 clics residuales.**  
**Acción:** 410/301 a home + bloqueo en GSC + WAF. No migrar.

---

## URLs sin ficha — 40 indexadas

Mezcla de:
- URLs categoría blog sin post (`/blog/peru/where-to-buy-peruvian-pisco-2026` sin slash)
- Taxonomías (`/tour-category/`, `/travel-styles/`)
- Índice `/blog`

**Acción:** revisar `urls-sin-ficha.csv` — cada una necesita 301 o página real en greenfield.

---

## Mapa redirect blog (crítico para pgt-web)

- **454 filas** en `redirects-blog-301.csv`
- Formato: `URL con categoría` → `URL limpia`
- **93%** de categorías validadas contra GSC (0 discrepancias Rank Math vs URL indexada)

```csv
from,to,clics
https://www.perugrandtravel.com/blog/cusco/things-to-do-in-machu-picchu/,https://www.perugrandtravel.com/blog/things-to-do-in-machu-picchu/,...
```

---

## Estrategia greenfield actualizada (prioridades)

| Prioridad | Qué | Por qué |
|---|---|---|
| **P0** | Home + `/packages/` + `/machu-picchu-packages/` | Clics + ads + WA |
| **P0** | `redirects-blog-301.csv` en `next.config` | 454 URLs duales |
| **P1** | Top 20 blogs por clics | 63% del tráfico |
| **P1** | Things MP + blogs alto imp/bajo CTR | Quick wins CTR |
| **P1** | 54 grupos canibalización | Consolidar autoridad |
| **P2** | 73 tours (catálogo completo) | Conversión, no volumen SEO |
| **P2** | Árbol `/peru/lima/...` | Destinos con impresiones |
| **P3** | Spam cleanup | Higiene |

---

## Contradicción resuelta: GSC 28d vs Excel 16m

| Fuente | Periodo | Clics sitio |
|---|---|---:|
| Línea base ago (`GSC-LINEA-BASE`) | 28 días | 643 |
| Este Excel (Resumen) | 16 meses | blog 20k + pages 12k + tours 251 |

No se contradicen — periodos distintos. **Usar Excel para priorizar URLs; usar GSC 28d para tendencia semanal.**

---

## Qué copiar a pgt-web (otro chat)

```
@/home/jairoprodev/proyectos/pgt/03-seo/datos/keywords-canibalizacion-2026-08-31/README.md
@/home/jairoprodev/proyectos/pgt/03-seo/datos/keywords-canibalizacion-2026-08-31/INSIGHTS.md
@/home/jairoprodev/proyectos/pgt/03-seo/datos/keywords-canibalizacion-2026-08-31/redirects-blog-301.csv
@/home/jairoprodev/proyectos/pgt/03-seo/datos/keywords-canibalizacion-2026-08-31/tours.csv
@/home/jairoprodev/proyectos/pgt/03-seo/datos/keywords-canibalizacion-2026-08-31/blogs.csv
@/home/jairoprodev/proyectos/pgt/03-seo/datos/keywords-canibalizacion-2026-08-31/paginas.csv
```

---

*Generado automáticamente desde Excel 31 ago 2026*
