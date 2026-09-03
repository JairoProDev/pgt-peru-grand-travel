# Tareas vivas — check diario

Marca `[x]` al terminar. **Añade** filas abajo; no borres historia.  
Mapa narrado: [`MAPA-TRABAJO-JAIRO.md`](MAPA-TRABAJO-JAIRO.md)  
CSV: [`tracker/TAREAS-MAESTRO.csv`](tracker/TAREAS-MAESTRO.csv) (algunas filas Drupal D-08/D-09 pueden estar **desfasadas**: los 18 tours ya dan HTTP 200).

**Hoy (actualiza la fecha):** 3 sep 2026.

---

## Ahora mismo (orden)

| ☐ | # | Tarea | Por qué | Hecho cuando |
|---|---|-------|---------|--------------|
| [ ] | N1 | **CNAME `next` en WHM** (2 campos, ver abajo) | Beta Next.js sin tocar www | `dig`/`nslookup` `next.perugrandtravel.com` → `cname.vercel-dns.com` |
| [ ] | N2 | En Vercel: añadir dominio `next.perugrandtravel.com` (si no está) | El CNAME solo no sirve si Vercel no tiene el host | SSL verde en el subdominio |
| [ ] | N3 | Abrir `https://next.perugrandtravel.com` · confirmar `noindex` | QA beta | Home + 1 tour + WA |
| [ ] | N4 | **GTM:** tag `whatsapp_click` → GA4 conversión (property `368486554`) | Único KPI de lead que pide Clever | Evento en DebugView |
| [ ] | N5 | Ticket Banahosting (opcional): load 47–58 + Error ID `381fb3f66720c` | cPanel inutilizable; 17 WP en shared | Respuesta soporte |
| [ ] | N6 | Presentación 4 sep (si es mañana) | Capas SEO + 18 tours staging | `PRESENTACION-4SEP-*.md` |
| [ ] | N7 | WhatsApp pacto ~25 sep por escrito | Congelar S/ 5.000 | captura (no Git) |

---

## CNAME WHM — exactamente 2 campos (3 sep 2026)

El modal **“Añadir Un CNAME Registro”** **no tiene TTL ni “Target”**. Equivalencia:

| Lo que ves | Qué es | Qué escribir |
|------------|--------|----------------|
| **Nombre** | El host que creas (lado izquierdo del CNAME) | Preferido: `next` · Si el UI lo rechaza o el placeholder es FQDN: `next.perugrandtravel.com.` (**punto final**) |
| **CNAME** | El destino (lo que yo llamé Target) | `cname.vercel-dns.com.` (**punto final** recomendado) |

**Peligro cPanel:** si pones `next.perugrandtravel.com` **sin** el punto final, a veces crea `next.perugrandtravel.com.perugrandtravel.com`. Evita eso con `next` solo **o** FQDN **con** punto.

TTL: WHM usa el default de la zona (suele ser 14400). No hace falta campo.

**No toques** registros A de `@`/`www`, ni MX, ni TXT.

Hasta que exista el registro, `next.perugrandtravel.com` es **NXDOMAIN**. Las demos siguen en https://perugrandtravel.vercel.app

---

## Pendiente humano / equipo

| ☐ | Quién | Tarea |
|---|-------|-------|
| [ ] | Jairo | GTM → GA4 `whatsapp_click` |
| [ ] | Jairo | CNAME `next` + Vercel domain |
| [ ] | Jairo | WhatsApp pacto 25 sep |
| [ ] | Jairo | Avisar a Ricardo usuario NAS `linux_admin` |
| [ ] | Einel | CSS `tour-maestro-styles.css` + overlap sidebar |
| [ ] | Einel | Borrar product #68 Amazon rainforest express |
| [ ] | Einel | Subida media / theme (si no lo hace Jairo con script) |
| [ ] | Ricardo | Validar tarifario 2026 antes de `precios:apply` |
| [ ] | Lizet | 20 min landings Ads ON (mapa paid↔orgánico) |
| [ ] | Clever | ¿los 3 `.pe` (mercadomovil, bienes raíces, tejidos) se quedan? |
| [ ] | Clever / Ricardo | Cutover **www** — **no** hoy (GTM + QA + OK dueño) |
| [ ] | Jairo | Invitar SA a GSC ES `viajesmachupicchutours.com` |
| [ ] | Jairo | GEO baseline 10 prompts |
| [ ] | Jairo | Migrar 115 blogs Drupal (después de tours/media) |

---

## Cutover EN — no hacer todavía

| ☐ | Ítem | Bloqueo |
|---|------|---------|
| [ ] | Cambiar A/CNAME de `www` / `@` a Vercel | GTM conversión + Clever OK + Team Vercel PGT + Pro comercial |
| [ ] | Apagar WordPress EN | 30 días de WP vivo post-cutover |
| [ ] | Apagar Banahosting | PT/ES/IT + DNS + leftovers `webmail.` siguen ahí |

---

## Hecho reciente (referencia rápida)

| ☐ | Ítem |
|---|------|
| [x] | Auditoría pre-empleo + jairosaul.com/peru-grand-travel |
| [x] | Día 1–6 onboarding, bloque 18+115, GSC/GA4 exports |
| [x] | POC + pgt-web ~591 rutas, preview vercel.app |
| [x] | Drupal staging 18/18 `/tour/{slug}` HTTP 200 |
| [x] | WHM: 17 cuentas, Zone Manager, load crítico, cPanel 500 |
| [x] | Confirmado por DNS: mail EN = **Google Workspace**, no cPanel |

---

## Próximas IDs al cerrar N1–N3

Al guardar el CNAME, añade en `MAPA-TRABAJO-JAIRO.md`:

- **JT-079** — CNAME `next` creado (fecha, TTL observado)
- **JT-080** — Vercel domain + SSL
- **JT-081** — QA beta URL
