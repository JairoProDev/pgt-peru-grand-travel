# Analytics — notas consolidadas (agente + docs pgt)

**GTM live (curl WP):** `GTM-K8SZBJM5`, `GTM-NNSPKMFM`  
**GA4 EN:** propiedad `368486554`, measurement `G-NTXD373H4Q`  
**Evento WA baseline:** `chat:51946622318` — 89 usuarios / 28d (~3,3% sesiones)  
**Evento greenfield:** `whatsapp_click` via dataLayer → configurar tag en GTM-K8SZBJM5

## Implementación pgt-web

1. GTM container `GTM-K8SZBJM5` en layout
2. `dataLayer.push({ event: 'whatsapp_click', page_path, content_type, content_slug, utm_content, environment })`
3. UTM WA: `utm_source=web&utm_medium=whatsapp&utm_content={slug}`
4. Beta: `environment: 'beta'` para filtrar en GA4

## Pendiente Jairo (requiere login GTM admin)

Ver `CHECKLIST-EXPORTS-JAIRO.md` para screenshots/exports manuales.
