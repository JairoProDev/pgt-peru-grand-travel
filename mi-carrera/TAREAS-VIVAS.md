# Tareas vivas — check diario

Marca `[x]` al terminar. **Añade** filas abajo; no borres historia.  
Mapa narrado: [`MAPA-TRABAJO-JAIRO.md`](MAPA-TRABAJO-JAIRO.md)  
Guía beta EN (paso a paso): `../pgt-web/docs/GUIA-VIVA-BETA-NEXT.md`

**Hoy:** 3 sep 2026.

---

## Ahora mismo (orden)

| ☐ | # | Tarea | Por qué | Hecho cuando |
|---|---|-------|---------|--------------|
| [x] | N1 | CNAME `next` en WHM | Beta sin tocar www | Zona: `next` → `cname.vercel-dns.com` TTL 14400 |
| [x] | N2 | Vercel domain + env + redeploy | SSL + canonical `next.` | Domains add + SITE_URL + ENV=next · 200/noindex |
| [ ] | N3 | **QA manual** en https://next.perugrandtravel.com | Confiar ante Clever | Tabla FASE 1 en `PASOS-SOLO-JAIRO.md` |
| [x] | N4 | **GTM:** `whatsapp_click` → GA4 (`G-NTXD373H4Q`) | Tag fired en Tag Assistant 3 sep | Versión 2 publicada |
| [x] | N4b | GA4: `whatsapp_click` = **evento clave** (estrella) | KPI Clever | Nombre OK; flujo UI puede decir “proof of concept” hasta que lleguen hits del stream EN |
| [ ] | N4c | Confirmar en DebugView / Tiempo real desde `next.` | Que el flujo activo sea perugrandtravel.com-GA4 | Admin → DebugView |
| [ ] | N3 | **QA manual** en https://next.perugrandtravel.com | Confiar ante Clever | Tabla FASE 1 en `PASOS-SOLO-JAIRO.md` |
| [ ] | N5 | Ticket Banahosting (opcional) load 47–58 | cPanel 500 | Error ID `381fb3f66720c` |
| [ ] | N6 | Presentación 4 sep / plan SEO Clever | Capas SEO + next. + scorecard | `PRESENTACION-4SEP-*.md` + `GUIA-VIVA-BETA-NEXT.md` |
| [ ] | N7 | WhatsApp pacto ~25 sep | Congelar S/ 5.000 | captura (no Git) |

---

## Pendiente humano / equipo

| ☐ | Quién | Tarea |
|---|-------|-------|
| [ ] | Jairo | QA + GTM conversión |
| [ ] | Jairo | WhatsApp pacto 25 sep |
| [ ] | Jairo | Avisar NAS `linux_admin` a Ricardo |
| [ ] | Einel | CSS tour maestro + product #68 |
| [ ] | Ricardo | Tarifario 2026 antes de `precios:apply` |
| [ ] | Lizet | Landings Ads ON |
| [ ] | Clever | 3 `.pe` + OK cutover www (después) |
| [ ] | Jairo | Team Vercel PGT + Pro **antes** de www |

---

## Cutover EN — no hacer todavía

| ☐ | Ítem |
|---|------|
| [ ] | Cambiar A/`www` a Vercel |
| [ ] | Apagar WP EN / Banahosting |

---

## Hecho reciente

| ☐ | Ítem |
|---|------|
| [x] | Zona DNS leída completa: MX Google, SPF RD+SendGrid, next CNAME |
| [x] | https://next.perugrandtravel.com vivo (SSL, noindex, canonical) |
| [x] | Snapshot rollback documentado en `GUIA-VIVA-BETA-NEXT.md` |
