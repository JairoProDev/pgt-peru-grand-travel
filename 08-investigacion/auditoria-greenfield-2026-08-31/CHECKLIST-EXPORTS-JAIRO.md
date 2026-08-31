# Checklist exports Jairo — auditoría greenfield

**Carpeta destino:** `pgt/08-investigacion/auditoria-greenfield-2026-08-31/exports/`

Marca cada ítem al completarlo. El agente no puede autenticarse en estas herramientas sin tu sesión.

## GTM — contenedor `GTM-K8SZBJM5`

- [ ] Abrir [tagmanager.google.com](https://tagmanager.google.com) → contenedor **GTM-K8SZBJM5** (no MJZXPQZR)
- [ ] Exportar o capturar: tags que disparan en clic WhatsApp / `chat:51946622318`
- [ ] Guardar como `exports/gtm-tags-wa.png` o export JSON del workspace

## GA4 — propiedad `368486554` (EN)

- [ ] Admin → Eventos → marcar `chat:51946622318` y futuro `whatsapp_click` como **eventos clave**
- [ ] Admin → Filtros de datos → tráfico interno (IP oficina)
- [ ] Exploraciones → export top páginas WA últimos 28d → `exports/ga4-top-pages-wa.csv`

## GSC — perugrandtravel.com

- [ ] Rendimiento → últimos 28 días → Exportar → `exports/gsc-performance-28d.csv`
- [ ] Páginas → top 100 URLs → `exports/gsc-top-urls.csv`

## Figma (opcional v1)

- [ ] Node tour `485-3513` — captura o export tokens → `exports/figma-tokens.png`

## wp-admin

- [ ] Tour Salkantay 5D — captura campos Tourmaster → `exports/wp-tour-salkantay.png`
- [ ] Blog Things MP — captura Rank Math meta → `exports/wp-blog-things-mp.png`

---

**Estado agente (público, ya hecho):**

- `wp-live-tracking.txt` — GTM-K8SZBJM5, GTM-NNSPKMFM confirmados en HTML live
- `wp-mvp-pages-meta.json` — meta de 4 URLs MVP
- `redirects-mvp.json` — 115 redirects blogs duales
- `poc-vs-wp-diff.md` — comparativa técnica
