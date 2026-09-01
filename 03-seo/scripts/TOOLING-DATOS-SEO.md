# Herramientas — análisis datos SEO (pgt)

**Actualizado:** 31 ago 2026

## Instalación (una vez)

WSL sin `sudo` — pip en usuario:

```bash
python3 /tmp/get-pip.py --user --break-system-packages   # si no tienes pip
python3 -m pip install --user --break-system-packages -r 03-seo/scripts/requirements-seo-data.txt
```

Verificar:

```bash
python3 -c "import pandas, openpyxl; print('OK', pandas.__version__)"
```

**Con sudo (preferido en máquina propia):**

```bash
sudo apt install python3-pip python3-venv
cd /home/jairoprodev/proyectos/pgt
python3 -m venv .venv
source .venv/bin/activate
pip install -r 03-seo/scripts/requirements-seo-data.txt
```

## Script principal

```bash
# URLs + keywords + canibalización (Excel Claude)
python3 03-seo/scripts/analyze-excel-keywords.py \
  "/mnt/c/Users/jairo/Downloads/PGT_URLs_keywords_canibalizacion_2 (2).xlsx" \
  --out 03-seo/datos/keywords-canibalizacion-2026-08-31 \
  --type canibalizacion

# Google Ads Keyword Planner export
python3 03-seo/scripts/analyze-excel-keywords.py \
  "/mnt/c/Users/jairo/Downloads/Keyword Stats 2026-08-26 at 14_06_41.xlsx" \
  --out 03-seo/datos/keyword-stats-2026-08-26 \
  --type keyword-stats
```

Salida: CSV por hoja + `insights.json` + `INSIGHTS.md` + copia del `.xlsx`

## Índice de datos

Ver `03-seo/datos/README.md`

## Otros scripts

| Script | Uso |
|---|---|
| `export-wp-sitemap-inventory.sh` | URLs desde sitemaps live |
| `export-wp-content.py` | Meta HTML público WP |
| `check-urls.sh` | WP vs Drupal staging |
| `analyze-excel-keywords.py` | Excel → CSV + insights |
