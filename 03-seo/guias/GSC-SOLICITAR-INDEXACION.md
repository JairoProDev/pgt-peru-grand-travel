# GSC — Solicitar indexación (Things MP)

**URL a pegar:**
```
https://www.perugrandtravel.com/blog/things-to-do-in-machu-picchu/
```

---

## Por qué (fundamento)

Google ya tiene la URL indexada (por eso hay 6k impresiones). **Solicitar indexación** no “reinicia” el ranking: pide al crawler que **vuelva pronto** a leer title/meta/H1 nuevos. Sin esto, a veces tarda semanas; con esto, suele ser días.

No cambia posición por sí solo. Solo acelera que el **snippet nuevo** aparezca en resultados.

---

## Paso a paso

1. Abre una pestaña nueva → ve a:
   ```
   https://search.google.com/search-console
   ```
2. Elige la propiedad **perugrandtravel.com** (la misma donde viste clics/impresiones).
3. Arriba, en la **barra de búsqueda** (dice “Inspecciona cualquier URL…” / “Inspect any URL”), pega:
   ```
   https://www.perugrandtravel.com/blog/things-to-do-in-machu-picchu/
   ```
4. Pulsa **Enter**.
5. Espera 5–15 s a que cargue el informe.
6. Verás algo como:
   - “La URL está en Google” / “URL is on Google”, **o**
   - “La URL no está en Google”
7. Clic en el botón azul:
   - **Solicitar indexación** / **Request indexing**
8. Espera (puede tardar 1–2 min). Cuando termine: “Indexación solicitada” / “Indexing requested”.

**Límite:** ~10–20 solicitudes/día por propiedad. Una sola para este post basta.

---

## Si dice “La URL no está en Google” / “Google no reconoce esta URL”

**No entres en pánico.** Suele pasar aunque la página **sí** tenga impresiones en Rendimiento.

| Señal | Qué significa |
|---|---|
| Inspección: “no reconoce esta URL” + rastreo N/D | El informe de índice **de esta vista** no tiene ficha fresca de la URL |
| Rendimiento (xlsx): 6.115 imp / pos ~5,8 | Google **sí** la mostró en resultados (estaba indexada) |
| Sitemap / página de referencia “ninguna” | Datos de descubrimiento vacíos en esta ficha — no prueba que no exista |

**Qué hacer (orden):**

1. Clic **PROBAR URL PUBLICADA** → espera → confirma que se puede rastrear (sin noindex / 404).
2. Clic **SOLICITAR INDEXACIÓN** → espera “Indexación solicitada”.
3. Comprueba en Google (incógnito):  
   `site:perugrandtravel.com/blog/things-to-do-in-machu-picchu`  
   Si sale el resultado → **está en Google**; el inspector iba retrasado.
4. En 2–7 días vuelve a Inspección; a menudo pasa a “La URL está en Google”.

**No** reescribas title/meta otra vez por este mensaje.

---

## Después

- No hace falta refrescar cada hora.
- En **7–14 días**: Google incógnito → `site:perugrandtravel.com things to do machu picchu` → mira si el title muestra `12 Things... (2026 Guide)`.
- Cada lunes: GSC → Rendimiento → filtro página exacta → anotar CTR.
