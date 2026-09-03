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

**Workaround DNS (no hace falta cPanel):** WHM → **DNS Zone Manager** (`scripts7/zone_editor`) → zona `perugrandtravel.com` → añadir CNAME `next`.

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

## Implicaciones para pgt-web / cutover EN

1. Banahosting **se mantiene** (16 sitios + mail + DNS) aunque EN vaya a Vercel.
2. DNS de `next.perugrandtravel.com` se hace en **WHM Zone Manager**, no en client area “Dominios”.
3. Load 47 = argumento de negocio: **WP shared saturado**; Next.js en Vercel saca EN de esa caja.
4. Tres `.pe` no-turismo: preguntar a Clever si se quedan o se archivan.

---

## Relacionado

- `pgt-web/docs/HOSTING-DNS-VERCEL-VS-BANAHOSTING.md`
- `pgt-web/docs/PASOS-SOLO-JAIRO.md`
- `02-empresa/INVENTARIO-SISTEMAS.md`
- `02-empresa/GESTION-ACCESOS-DISENO.md`
