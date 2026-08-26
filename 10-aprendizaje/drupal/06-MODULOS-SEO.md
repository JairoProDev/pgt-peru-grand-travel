# Módulos SEO esenciales (Drupal)

Lista para pedir / verificar en el proyecto PGT. Nombres pueden variar por versión; confirma en staging.

| Necesidad | Módulo típico | Equivalente WP |
|---|---|---|
| Title, description, OG | **Metatag** (+ Metatag Open Graph) | Yoast |
| Schema.org | **Schema.org Metatag** o custom | Yoast graph |
| URLs bonitas / patrones | **Pathauto** + Token | Permalinks + Yoast |
| 301 / 302 | **Redirect** | Redirection / Yoast Premium |
| Sitemap XML | **Simple XML Sitemap** | Yoast sitemap |
| Canonical | Metatag / core | Yoast |
| Hreflang | Language + Metatag / contrib | Manual / WPML |
| robots.txt | Core + ajustes | Yoast |
| Breadcrumbs | Easy Breadcrumb / tema | Yoast |
| Redirect tras cambio de alias | Pathauto + Redirect | — |

## Checklist que TÚ validas (tu valor)

Para cada content type Tour y Article:

- [ ] Metatag title template con keyword principal (sin keyword stuffing)
- [ ] Meta description editable
- [ ] Canonical correcta (no a home)
- [ ] OG image = hero
- [ ] Schema: Organization/TravelAgency en sitio; Product/Offer o TouristTrip en ficha
- [ ] `priceCurrency` correcto
- [ ] Sitemap incluye tours publicados, no drafts
- [ ] noindex en staging (crítico)
- [ ] WhatsApp link con UTM opcionales

## Drush útil (pide que te lo muestren)

```bash
drush cr                    # rebuild cache
drush config:export -y      # exportar config
drush xmlsitemap:regenerate # si aplica
drush status
```

No ejecutes en producción sin Ricardo / devops.

Siguiente: `07-ADMIN-DIA-A-DIA.md`.
