# Reconciliación de inventarios — tours y blogs

> Fuente canónica SEO: **Sheet/Excel** `PGT_URLs_keywords_canibalizacion_2`  
> Export: `03-seo/datos/keywords-canibalizacion-2026-08-31/` (actualizado 2026-08-31 con `(3).xlsx`)

---

## Números oficiales (equipo SEO)

| Tipo | Sheet Excel | Sitemap WP (31-ago) | Web Next.js |
|------|-------------|---------------------|-------------|
| **Tours** | **73 fichas** | **69** URLs públicas | **70** JSON (69 sitemap + 1 extra) |
| **Blogs** | **454 artículos** | **452** (snapshot anterior) | **456** JSON (ver abajo) |
| **Páginas** | **69** | **62** | **62** |

El README del repo (`~73 tours + ~454 blogs`) es correcto. El sitemap de cutover EN usa **69 tours publicados** + **454 blogs** del Sheet como referencia editorial.

---

## Tours: por qué 73 ≠ 69

**73 en Sheet** = 69 tours en sitemap WP + **4 filas adicionales**:

| Slug | Estado Sheet | En sitemap | En web | Notas |
|------|--------------|------------|--------|-------|
| `challenge-of-the-incas-15d` | **private** | ❌ | ✅ (añadido 2026-08-31) | URL live 200 — ficha SEO válida, 15D package |
| `incredible-experience-machu-picchu-7-days` | **draft** | ❌ | ❌ (alias) | Slug obsoleto; canónico web: `incredible-experience-machu-picchu-7d` |
| `peru-private-romance` | **draft** | ❌ | ❌ | URL 404 — borrador |
| `peru-private-romance-copy` | **draft** | ❌ | ❌ | URL 404 — duplicado borrador |

**Regla:** contar **69** para paridad URL/cutover; contar **73** para trabajo SEO/fichas; incluir `challenge-of-the-incas-15d` en web si la ficha sigue indexada o enlazada desde blogs.

---

## Blogs: por qué 454 ≠ 452 ≠ 456

**454 en Sheet** = lista canónica de artículos publicados para SEO.

| Slug | Sheet | Sitemap | Web | Notas |
|------|-------|---------|-----|-------|
| `temples-in-peru-2026` | ✅ | ❌ | ✅ (añadido 2026-08-31) | Reemplazo/canónica 2026 del post antiguo |
| `temples-in-peru` | ❌ (reemplazado) | ✅ | ✅ | URL legacy aún live — considerar 301 → `-2026` |
| `where-to-buy-peruvian-pisco-2027` | ✅ | ❌ | ✅ | Versión 2027 en Sheet |
| `where-to-buy-peruvian-pisco` | ❌ | ✅ | ✅ | Versión anterior aún live |
| `luxury-travel-peru` | ✅ | ❌ | ✅ | Nuevo vs snapshot sitemap |
| `tourist-packages-to-enjoy-with-children-for-a-trip-to-peru-machu-picchu` | ✅ | ❌ | ✅ | Nuevo vs snapshot sitemap |

**Regla cutover:** objetivo **454 rutas** alineadas al Sheet; resolver duplicados (`temples-in-peru`, `pisco`) con **301** hacia la URL canónica del Sheet.

---

## Acciones abiertas

- [x] Re-export Excel `(3).xlsx` → CSV en `keywords-canibalizacion-2026-08-31/`
- [x] Scrape tour `challenge-of-the-incas-15d`
- [x] Scrape blog `temples-in-peru-2026`
- [ ] Redirect 301: `/blog/temples-in-peru/` → `/blog/temples-in-peru-2026/` (si Sheet confirma canónica)
- [ ] Redirect 301: `/blog/where-to-buy-peruvian-pisco/` → `-2027` (si aplica)
- [ ] Actualizar `inventario-sitemap` post-cutover desde WP live
- [ ] Marcar drafts Sheet (`peru-private-romance*`) como `archived` en catálogo — no migrar

---

## Comandos

```bash
# Re-exportar Sheet desde Downloads
cd pgt && python3 03-seo/scripts/analyze-excel-keywords.py \
  "/mnt/c/Users/jairo/Downloads/PGT_URLs_keywords_canibalizacion_2 (3).xlsx" \
  --out 03-seo/datos/keywords-canibalizacion-2026-08-31

# Regenerar catálogo merge
cd pgt-web && python3 scripts/build-catalogo-maestro.py
```
