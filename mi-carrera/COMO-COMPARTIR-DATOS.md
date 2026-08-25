# Cómo pasarme tablas Excel / Sheets (formato)

Para que yo analice tus bloques (`tours jairo`, `blogs jairo`) sin perder columnas ni romper seguridad.

---

## Ranking (mejor → peor)

| # | Formato | Cuándo usarlo | Por qué |
|---|---------|---------------|---------|
| 1 | **CSV UTF-8** | Siempre que puedas | Lo leo directo, ordeno, sumo, comparo versiones. Sin macros ni sorpresas. Git-friendly en `inbox/` o `03-seo/datos/` |
| 2 | **Archivo en `inbox/`** (CSV o XLSX de **solo tu hoja**) | Export desde Excel/Sheets | Ruta local en WSL; no pegas datos sensibles en chat |
| 3 | **Link Google Sheet** (pestaña concreta + permiso lectura) | Datos vivos que cambian a diario | Útil referencia; **yo a veces no puedo abrir** si pide login corporativo |
| 4 | **XLSX** (.xlsx) | Si CSV pierde formato raro | OK en `inbox/`; más pesado; evita si tiene macros o varias hojas gigantes |
| 5 | **Pegar en chat** | ≤30 filas, 5–8 columnas | Rápido para una duda puntual; malo para bloque completo |
| 6 | **TSV** | CSV falla con comas en celdas | Mismo rol que CSV, separador tab |
| 7 | **ODS** | Solo si no tienes otra opción | Menos estándar; convierte a CSV |
| 8 | **HTML** (export web) | Evitar | Tags basura, difícil de parsear |
| 9 | **PDF** | Solo para **mostrar a Clever** | **Peor para mí:** no calculo, no filtro, no diff |

---

## Procedimiento recomendado (2 minutos)

### Desde Google Sheets (tu caso)

| Acción | Resultado |
|--------|-----------|
| Descargar **CSV** | **Solo la pestaña activa** (nombre incluye la hoja) |
| Descargar **XLSX** (.xlsx) | **Todo el libro** (todas las pestañas) |
| Descargar **una hoja** como XLSX desde el menú de la pestaña | Solo esa hoja |

Si CSV y XLSX **pesan igual**, casi seguro exportaste **la misma hoja** en dos formatos — no el archivo completo.

**Para el agente:** CSV por hoja en `03-seo/datos/`. **Respaldo:** un XLSX completo en `inbox/PGT-completo-AAAA-MM-DD.xlsx`.

Pasos CSV (por hoja):

1. Abre pestaña `tours jairo` o `blogs jairo`.
2. **Archivo → Descargar → Valores separados por comas (.csv)**.
3. Guarda en `03-seo/datos/` o `inbox/` con nombre `{tours|blogs}-jairo-AAAA-MM-DD.csv`.
4. En el chat: *"Exporté tours y blogs en datos con fecha …"* — no pegues 500 filas.

### Desde Excel desktop

1. **Guardar como → CSV UTF-8 (delimitado por comas)**.
2. Misma carpeta `inbox/`.
3. Si Excel te advierte “solo hoja activa”: **acepta** (quiero una hoja por archivo).

### Nombres de archivo

```
{tours|blogs}-jairo-AAAA-MM-DD.csv
gsc-bloque-jairo-AAAA-MM-DD.csv   ← export Search Console aparte
```

Así comparo día a día.

---

## Qué NO compartir

- `Accesos*.xlsx` (contraseñas, TOTP).
- Todo el Drive en ZIP.
- Login + 2FA de marketing@ en browser del agente.
- CSV con columnas de credenciales.

---

## Link vs archivo

| | Link Sheet | CSV en inbox |
|---|------------|--------------|
| Datos actualizados | Sí | Snapshot del momento |
| Yo puedo analizar sin ti | A veces no (login) | **Sí siempre** |
| Diff semana a semana | Manual | **Fácil** |
| Para informe Clever | Vista bonita | Export + PDF hecho por ti |

**Ideal:** link para **ti** en el día a día + **CSV semanal** (viernes) para mí y para adjuntar evidencia.

---

## Columnas mínimas (no borres al exportar)

**Tours:** `URL`, `Keyword principal`, `Clicks`, `Impresiones`, `CTR`, `Posición`, `SEO score`, `Modificado`

**Blogs:** `URL limpia` (o URL), `Keyword principal`, `Clics`, `Impresiones`, `CTR`, `Posición`, `SEO score`, `Palabras`

Si exportas “solo columnas visibles”, asegúrate de incluir URL + métricas GSC.

---

## Capturas (como las de hoy)

Útiles para **contexto rápido** (“¿ves mi hoja?”). **No sustituyen CSV** para sumar clics o priorizar 40 URLs.

Orden: captura → confirmación visual · CSV → trabajo serio.

---

Ver también: `COMO-COMPARTIR-DRIVE.md`.
