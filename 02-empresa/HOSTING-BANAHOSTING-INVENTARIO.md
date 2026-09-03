# Inventario Banahosting / WHM — PGT

> **Fecha inspección:** 3 sep 2026  
> **Quién:** Jairo (cuenta Clever + 2FA)  
> **Panel:** WHM `priva80.privatednsorg.com:2087` · Reseller `hwxniobv` · CloudLinux 8.10 · cPanel 136.0.38  
> **Client area:** manage.banahosting.com servicio id `38796` · Bana Reseller-1 · **$239 USD/año** · vence **15 abr 2027** · PayPal  
> **Sin contraseñas en este archivo.**

---

## Hallazgo 3 sep — cPanel 500 / servidor saturado

| Dato | Valor |
|------|--------|
| Load averages (WHM header) | **~47–48** (crítico; normal < 4–8 en este tipo de caja) |
| Error al clic “CP” | `500 Internal Server Error` |
| URL que falla | `https://priva80.privatednsorg.com:2087/xfercpanel` |
| Error ID | `381fb3f66720c` |
| Daemon | `cpsrvd` |
| Cuentas suspendidas | **0** |

**Causa más probable:** el servidor no puede abrir sesión cPanel (`xfercpanel`) porque está **sobrecargado**, no porque falte permiso.

**Workaround DNS (no hace falta cPanel):** WHM → **DNS Zone Manager** (`scripts7/zone_editor`) → zona `perugrandtravel.com` → **CNAME Record**.

Load visto el mismo día: **47–48** (List Accounts) y **58.33 / 48.94** (Zone Manager). Sigue crítico.

### Modal CNAME real (WHM 136, español) — solo 2 campos

No hay TTL ni etiqueta “Target”. Equivalencia:

| Campo en pantalla | Significado | Valor |
|-------------------|-------------|--------|
| **Nombre** | Host nuevo | `next` **o** `next.perugrandtravel.com.` (con **punto final** si usas FQDN) |
| **CNAME** | Destino (Target) | `cname.vercel-dns.com.` (punto final recomendado) |

El placeholder `example.perugrandtravel.com.` **no** significa que debas copiar `example`. Significa “FQDN de este dominio”. Si escribes `next.perugrandtravel.com` **sin** punto, cPanel a veces concatena el dominio otra vez.

TTL: default de zona (típicamente 14400). No aparece en el modal.

**Aún no creado (DoH 3 sep 2026):** `next.perugrandtravel.com` → NXDOMAIN.

**Ticket Banahosting (si persiste):** load 47+, Error ID `381fb3f66720c`, no se puede entrar a cPanel de `perugrandtravel.com`.

---

## Plan de facturación (client area)

| Campo | Valor |
|-------|--------|
| Producto | Bana Reseller-1 |
| Dominio etiqueta | `perutrilhainca.com` (ancla reseller, **no** el único sitio) |
| “Mis Dominios” | Vacío = **no compraron dominios en Bana**; están en GoDaddy/Registros.com |
| NS del plan (ficha) | `ns1.privatednsorg.com` (50.31.188.115) · `ns2.privatednsorg.com` (50.31.188.116) |
| NS que usan los sitios PGT | `ns1.perutrilhainca.com` · `ns2.perutrilhainca.com` (mismo stack) |
| Usuario reseller | `hwxniobv` |

**Costo:** ~$239/año para **17 cPanels** ≈ $14/sitio/año. **No es caro.** Lo caro es duplicar EN (WP + Drupal OVH + Vercel).

---

## 17 cuentas cPanel (WHM List Accounts)

Contacto casi todo `marketing@perugrandtravel.com`. Solo perutrilhainca: `clever@`.

| Dominio | IP | Usuario cPanel | Paquete | Alta (WHM) | Rol |
|---------|-----|----------------|---------|------------|-----|
| perugrandtravel.com | 50.31.188.120 | `perugran` | Plan10Gb-Principal | 2017-05-16 | **EN WP prod** |
| machupicchupacotes.com | 50.31.188.121 | — | Plan10Gb-Principal | — | **PT** |
| viajesmachupicchutours.com | 50.31.188.124 | `viajesmachupicch` | Plan10Gb-Principal | — | **ES** |
| viaggiomachupicchu.it | 50.31.188.124 | `viaggiomachupicc` | Pack2Gb | — | **IT** |
| luxuryperutour.com | 50.31.188.124 | — | Pack2Gb | — | Lujo |
| vinicuncaperu.com | 50.31.188.118 | `vinicuncaperu` | Pack5Gb | — | Vinicunca |
| incatrailbookings.com | 50.31.188.124 | — | Pack5Gb | — | Bookings |
| ingressosmachupicchu.com | 50.31.188.118 | — | Pack2Gb | — | Ingressos |
| paquetesdeviajesperu.com | 50.31.188.123 | `paquetes` | Plan10Gb-Principal | — | ES legacy |
| machupicchuperu.com.mx | 50.31.188.119 | `machupicchuperuc` | Pack2Gb | — | MX |
| tripstomachupicchu.us | 50.31.188.124 | `tripstomachu` | Pack2Gb | — | Satélite US |
| perutravelguides.com | 50.31.188.124 | `perutravelguides` | Pack5Gb | — | Contenido |
| dicasviagem.com | 50.31.188.119 | — | Pack2Gb | — | Blog PT |
| perutrilhainca.com | 50.31.188.117 | `hwxniobv` | Pack2Gb | 2017-05-15 | Ancla reseller; 301 → pacotes/trilha-inca |
| mercadomovil.pe | 50.31.188.119 | `mercadomovil` | Pack2Gb | — | **¿otro negocio?** |
| perubienesraices.pe | 50.31.188.119 | `perubienesraices` | Pack2Gb | — | **¿otro negocio?** |
| tejidosmarangani.pe | 50.31.188.119 | `tejidosmarangani` | Pack2Gb | — | **¿otro negocio?** |

Drupal staging **no** está aquí: OVH `147.135.114.64`.

---

## Análisis del servidor `priva80` (3 sep 2026)

### Qué es

Caja **shared/reseller CloudLinux 8.10** de Banahosting (`priva80.privatednsorg.com`). Un reseller (`hwxniobv`) con **17 cPanels** WordPress (varios desde 2017). No es un VPS exclusivo de PGT: el load altísimo encaja con **muchos sitios + PHP viejo + crawlers + cron** en la misma máquina (posiblemente también vecinos de otros clientes del nodo).

### Uso real (lo que sí está aquí)

| Función | ¿En `priva80`? | Evidencia |
|---------|----------------|-----------|
| WordPress EN/PT/ES/IT + satélites | **Sí** | 17 cuentas WHM; A de `perugrandtravel.com` = `50.31.188.120` |
| DNS autoritativo de esos dominios | **Sí** | NS `ns1/ns2.perutrilhainca.com` |
| Drupal staging | **No** | OVH `147.135.114.64` |
| Next.js pgt-web | **No** | Vercel |
| Compra de dominios | **No** | Client area “Mis Dominios” vacío; GoDaddy/Registros.com |
| **Correo `@perugrandtravel.com`** | **No en cPanel como buzón principal** | ver sección siguiente |
| `webmail.` / `cpanel.` EN | Hostname A apunta a `.120` | leftover de cPanel; no prueba que el mail viva ahí |
| PHP | WHM avisó **PHP desactualizado** | riesgo WP, no Vercel |

### Load ~47–58

Load average ≈ procesos a la espera de CPU. En un shared de 8–16 cores, **> 8–12** ya duele; **47–58** es saturación: timeouts, 500 de `cpsrvd`, Zone Editor lento. **Causa del 500 al entrar a cPanel**, no un permiso faltante.

Implicación de negocio: sacar **solo EN** a Vercel reduce tráfico PHP de `perugran`, pero los otros 16 sitios siguen machacando el nodo. Banahosting **no se apaga**.

### Costo vs uso

~$239/año ≈ **$14/sitio/año** por 17 cPanels + DNS. Barato. Lo caro es triplicar EN (WP + Drupal OVH + Vercel) y un servidor que **no aguanta abrir cPanel**.

---

## Dónde está el correo `@perugrandtravel.com` (DNS público, 3 sep 2026)

Consulta DoH (Google DNS). **Sin entrar a cPanel.**

### EN — Google Workspace (Gmail), no buzones cPanel

| Tipo | Valor |
|------|--------|
| NS | `ns1.perutrilhainca.com` · `ns2.perutrilhainca.com` |
| A `@` / `www` | `50.31.188.120` (WordPress Banahosting) |
| **MX** | `1 aspmx.l.google.com` + `alt1–alt4.aspmx.l.google.com` (**Google**) |
| DKIM | `google._domainkey` presente (firma Google) + `default._domainkey` (otro firmante, típico cPanel/mail mixto) |
| DMARC | `p=none` · rua `dmarc@perugrandtravel.com` |
| SPF | `v=spf1 include:_spf.rdstation.com.br include:sendgrid.net ~all` — **no** incluye `_spf.google.com` (hueco: envíos desde Gmail pueden fallar SPF) |
| SOA email | `clever.perugrandtravel.com` (contacto zona) |

Conclusión: **`marketing@`, `clever@`, `seo@`, etc. se reciben en Google Workspace**. Por eso usas Gmail + 2FA, no Roundcube de Banahosting, como correo diario.

`mail.perugrandtravel.com` y `webmail.perugrandtravel.com` **sí** resuelven a `50.31.188.120` (nombres típicos de cPanel). Eso es **hostname residual**, no el MX. No borres esos A “por limpieza” sin Ricardo: alguien podría usar webmail viejo o autodiscover raro.

### Otros idiomas (contraste)

| Dominio | MX (DoH) | Lectura |
|---------|----------|---------|
| machupicchupacotes.com | `0 machupicchupacotes.com` | correo **local cPanel** (o al menos MX al propio host) |
| viajesmachupicchutours.com | `0 viajesmachupicchutours.com` | igual |
| viaggiomachupicchu.it | `0 viaggiomachupicchu.it` | igual |
| luxuryperutour.com | `0 luxuryperutour.com` | igual |
| perutrilhainca.com | `0 perutrilhainca.com` | igual |

O sea: **el mail corporativo de marca EN está en Google**; varios satélites/PT/ES/IT todavía delegan MX al mismo servidor Banahosting. Cortar Banahosting rompería esos MX, no el Gmail de `@perugrandtravel.com`.

### Qué no tocar al crear `next`

MX Google, TXT SPF/DKIM/DMARC, A de `@`/`www`. Solo un CNAME nuevo.

---

## Implicaciones para pgt-web / cutover EN

1. Banahosting **se mantiene** (16 sitios + DNS + MX locales PT/ES; mail EN = Google).
2. DNS beta: **hecho** 3 sep — `next` → Vercel. Edit en WHM Zone Manager.
3. Load alto = argumento de negocio; cPanel puede seguir en 500.
4. Tres `.pe` no-turismo: preguntar a Clever.

---

## Relacionado

- `pgt-web/docs/HOSTING-DNS-VERCEL-VS-BANAHOSTING.md`
- `mi-carrera/MAPA-TRABAJO-JAIRO.md` · `mi-carrera/TAREAS-VIVAS.md`
- `pgt-web/docs/PASOS-SOLO-JAIRO.md`
- `02-empresa/INVENTARIO-SISTEMAS.md`
- `02-empresa/GESTION-ACCESOS-DISENO.md`
