# Google Search Console — lo que debes dominar este mes

## Para qué en la migración

GSC es tu **caja negra de evidencia**: qué URLs tenían clics/impresiones **antes** del cutover y qué pasa **después**. Sin baseline, nadie te cree si “Drupal bajó el tráfico”.

## Qué hacer YA (bloque Jairo)

1. Propiedad del dominio o URL prefix de `perugrandtravel.com` (y las que te toquen).
2. Rendimiento → último **28 días** y **3 meses** → exportar **Páginas** y **Consultas** (CSV) → `03-seo/datos/`.
3. Filtrar / etiquetar tus 18 tours + 115 blogs.
4. Cobertura / Indexación: errores, excluidas, detectada no indexada.
5. Experiencia / CWV si está.
6. Removals: no usar salvo spam residual del virus.

## Durante migración

| Momento | Acción GSC |
|---|---|
| Pre | Baseline CSV con fecha en nombre |
| Staging | **noindex** staging; no verificar staging como prod |
| Cutover | Inspección URL de 20 URLs piloto; enviar sitemap nuevo |
| +7 / +30 días | Comparar páginas vs baseline; listar 404 y soft 404 |
| Siempre | Anotar cambios de dominio/HTTPS |

## Informes que impresionan a Clever

- “Top 20 URLs por clics pre-migración”  
- “Estado post-día-7: X recuperadas, Y en 404, Z en Redirect”  
- No: “subimos 50 posiciones” sin export.

## Atajos

- Inspección de URL → HTML indexado vs vivo.  
- `site:dominio/ruta` en Google (complemento, no reemplazo).
