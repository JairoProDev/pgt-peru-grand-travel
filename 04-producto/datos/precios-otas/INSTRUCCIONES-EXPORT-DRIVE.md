# Export OTAS · Precios de productos (Drive)

> Archivo en Drive marketing@: **OTAS reservas · Precios de productos**  
> Inventariado en `02-empresa/DRIVE-INVENTARIO.md` (carpeta Ventas & Pauta / Ads)

---

## Pasos (Jairo u Ops)

1. Abrir [Drive marketing](https://drive.google.com/drive/folders/1-1wEMq2qox3D0jrs4uY1XQz-3sqbTW9z)
2. Localizar **OTAS reservas · Precios de productos** (Google Sheet o Excel)
3. **Archivo → Descargar → CSV** (una pestaña) o **.xlsx** (libro completo)
4. Guardar como:
   ```
   pgt/04-producto/datos/precios-otas/precios-otas-YYYY-MM-DD.csv
   ```
5. Si las columnas no coinciden con la plantilla, renombrar o copiar a `PLANTILLA-EXPORT-OTAS.csv`
6. Ejecutar merge:
   ```bash
   cd pgt-web
   python3 scripts/build-precios-snapshot.py
   python3 scripts/merge-precios-otas.py ../pgt/04-producto/datos/precios-otas/precios-otas-YYYY-MM-DD.csv
   ```

---

## Columnas mínimas esperadas

| Columna | Obligatorio | Ejemplo |
|---------|-------------|---------|
| `slug` o URL tour | ✅ | `the-classic-salkantay-trek-5d` |
| `precio_otas_interno_usd` | ✅ | `650` (neto agencia / base ventas) |
| `precio_gyg_usd` | opcional | precio público GetYourGuide |
| `precio_viator_usd` | opcional | precio público Viator |
| `notas_ops` | opcional | temporada, mínimo pax, hotel 3*/4* |

---

## Mientras no hay export OTAS

Usar **`precios-web-snapshot-latest.csv`** — precios scrapeados de la web (JSON-LD / `#prices`).  
No sustituye el sheet interno: ventas conoce márgenes y tiers que el scrape no ve.

```bash
cd pgt-web && python3 scripts/build-precios-snapshot.py
```

---

## Cruce con catálogo

Después del merge, revisar tours con `delta_web_vs_otas` > US$20 o `quote_only=yes` en web — prioridad validación Ops.

Ver también: `04-producto/CATALOGO-MAESTRO.md` (14 tours quote only).
