# Gestión de accesos PGT — diseño (proceso + Vaultwarden)

**Fecha:** 28 ago 2026  
**Estado:** borrador aprobado en chat (Jairo) — pendiente pitch a Ricardo / Clever  
**Secretos:** **nunca** en este archivo ni en el repo. Contraseñas solo en el cofre (Vaultwarden) o en el Excel local hasta migrar.

**Relacionado:** `02-empresa/MAPA-HERRAMIENTAS.md` (mapa sin secretos, uso diario SEO).

---

## 1. Problema

Hoy los accesos viven en un Excel/Sheet (`Accesos PGT -2026 Actuales`): sitio, URL, usuario, contraseña, notas en una sola tabla plana.

Eso genera:

| Dolor | Por qué pasa |
|---|---|
| Ricardo rota muchas claves al salir alguien | Cuentas **compartidas** (mismo user/pass para varios) |
| Difícil saber quién debe ver qué | Una sola hoja; sin roles |
| Riesgo alto | Sheet compartido = filtración; historial de versiones; copia a Drive |
| Caos visual | Categorías mezcladas, filas vacías, notas sueltas, cuentas eliminadas mezcladas |
| Onboarding lento | “Pídele la clave a Ricardo / mira el Excel” |

**Conclusión:** Excel sirve como **inventario temporal**, no como gestor de secretos.

---

## 2. Principios (acordados)

1. **Separar inventario vs secretos**  
   - Inventario (este repo / mapa): qué existe, URL, owner, colección, riesgo.  
   - Secretos: solo en password manager.
2. **Menos cuentas compartidas**  
   Invitar usuario personal o Google SSO cuando la tool lo permita. Compartido solo si no hay alternativa.
3. **Colecciones por rol**, no una lista infinita  
   Al salir alguien: quitar del grupo → pierde acceso a la colección. Rotar solo lo que era cuenta compartida.
4. **Owners claros**  
   Ricardo = admin del cofre + infra crítica. Clever = owner raíz (Google, dominio, hosting). Resto = membresía por colección.
5. **No construir app interna de contraseñas**  
   Mantener Vaultwarden cuesta; reinventar Bitwarden es peor (seguridad, 2FA, sync, auditoría).
6. **Costo $0 al inicio**  
   Vaultwarden (compatible Bitwarden) self-hosted en VPS o NAS ya existentes.

---

## 3. Solución: proceso + Vaultwarden

### 3.1 Qué es Vaultwarden

Servidor compatible con clientes **Bitwarden** (browser, móvil, desktop), self-hosted, sin licencia por usuario.

Cada persona:

- Tiene su bóveda personal.
- Entra a **colecciones** de la organización PGT según su rol.
- Autocompleta login en el navegador.
- Ricardo (admin) **revoca** al usuario en minutos.

### 3.2 Dónde hospedarlo (elegir una)

| Opción | Pros | Contras |
|---|---|---|
| **A. VPS Drupal / Ubuntu** (recomendado si ya hay Docker) | Acceso remoto seguro (HTTPS); mismo stack ops | Hay que exponer con reverse proxy + backup |
| **B. NAS OMV** (red local / VPN) | Cerca del archivo actual de “accesos” | Fuera de oficina más fricción; VPN obligatoria |
| **C. Solo LAN + Tailscale/VPN** | $0 y menos superficie pública | Setup VPN para ~20 personas |

**Recomendación:** Docker en VPS con HTTPS + backups diarios del volumen; acceso solo por org PGT. Si el VPS aún no está listo, NAS + Tailscale como fase 0.

### 3.3 Roles en el cofre

| Rol Vaultwarden | Personas (aprox.) | Puede |
|---|---|---|
| Owner | Clever (+ esposa/coordinación si aplica) | Todo + política |
| Admin | Ricardo | Users, colecciones, rotar críticos |
| Manager (opcional) | 1 marketing / 1 ops | Gestionar ítems de su colección |
| User | Resto (~15–18) | Usar lo de sus colecciones |

### 3.4 Colecciones (taxonomía)

Nombres cortos. Cada ítem del Excel migra a **una** colección + tags opcionales (`idioma:en`, `estado:eliminada`, `riesgo:alto`).

| Colección | Qué entra (del Excel actual) | Quién suele verlo |
|---|---|---|
| `00-critico-owners` | Banahosting, GoDaddy, Registros.com, Google Admin, dominio raíz | Clever, Ricardo |
| `10-web-wp-admin` | WP admin de sitios tour (PGT, pacotes, viajes, IT, luxury, etc.) | SEO + Ricardo + quien edite web |
| `11-web-cpanel` | cPanels de los mismos dominios | Ricardo + quien toque hosting |
| `12-web-blog` | Blogs WP + blogs satélite (dicas, perutravelguides) | SEO / content |
| `20-rrss` | Facebook, IG, LinkedIn, X, Flickr, TikTok, YouTube, Vimeo, Linktree | RRSS / marketing |
| `21-rrss-sensibles` | Cuentas falsas FB, recovery, celulares de 2FA | Solo Ricardo + owner RRSS |
| `30-ads-analytics` | TikTok Ads, Hotjar, Serprobot, AnswerThePublic, Growwer, etc. | Ads + SEO |
| `40-crm-email` | Mailchimp, RD Station, tawk.to | Marketing / ventas según uso |
| `50-otas-reservas` | WeTravel, PeruRail, Ministerio, Camino Inca, GYG, Viator, TourRadar, TrustIndex, TripAdvisor/Trustpilot | Reservas + ops + marketing puntuales |
| `60-diseno-ia` | Canva, CapCut, Shutterstock/iStock, ChatGPT, ElevenLabs, Suno, D-ID, Medium, Spotify | Diseño / content |
| `70-voip-telefonos` | Twilio, Sonetel, MyTelfon, Toll Free Forwarding, iPhone | Quien opere líneas |
| `80-rrhh-corp` | Computrabajo, correos PGT (inventario de casillas), USIL si aplica | RRHH / admin |
| `90-infra-local` | NAS, Open Media Vault, TpLink, staging clever, WiFi oficina | Ricardo + Clever |
| `99-archivo` | Cuentas eliminadas / “sin acceso” / “ya no existe” | Solo admin (historial) |

**Regla:** si un ítem no encaja, va a la colección del **owner** que más lo usa, no a “varios”.

### 3.5 Campos por ítem (en el cofre)

- Nombre: `Sitio — propósito` (ej. `WP — perugrandtravel.com`)
- URI (URL de login)
- Usuario / email
- Contraseña (generada fuerte)
- Notas: 2FA dónde vive, PIN recovery, “cuenta eliminada”, idioma (US/ES/BR), owner humano
- Custom: `Owner`, `Tipo` (`personal` \| `compartida` \| `sso-google`), `Rotar-si-sale`

---

## 4. Inventario organizado (sin secretos)

Lista canónica de **SITIO / APP** agrupada. URLs de login van en el cofre; aquí solo el mapa.

### 4.1 Infra y dominios → `00-critico-owners`

- HOSTING DE BANAHOSTING → manage.banahosting.com  
- DOMINIOS DE GODADDY → godaddy.com  
- DOMINIOS DE REGISTROS.COM → registros.com  

### 4.2 Web WordPress / cPanel / blogs → `10` / `11` / `12`

**WP admin (tour):**  
perugrandtravel.com, payments, machupicchupacotes, viajesmachupicchutours, paquetesdeviajesperu, vinicuncaperu, incatrailbookings, tripstomachupicchu.us, luxuryperutour, viaggiomachupicchu.it, machupicchuperu.com.mx, machupicchupacotes LP, ikimei.org, staging.luxuryperutour.com, clever staging si aplica.

**Blogs:** viajes…/blog, perugrandtravel.com/blog, machupicchupacotes/blog, luxury…/blog, dicasviagem, perutravelguides, mywpgt.

**cPanel:** mismos dominios principales (+ dicas / perutravelguides).

**Linktree:** perugrandtravel, .us, avaliacoes, opiniones, reviews.

### 4.3 Operaciones / OTAs / reviews → `50-otas-reservas`

- WeTravel, PeruRail, Conjunta, Ministerio (tuboleto), Camino Inca (negtu)  
- GetYourGuide, Viator, TourRadar  
- UptimeRobot, TripAdvisor, Trustpilot, TrustIndex, Google (reviews)  

### 4.4 Redes → `20-rrss` (+ `21` si sensible)

- Facebook (EN/BR/ES + cuentas falsas aparte)  
- Instagram (PGT, dicas, perutravelguides)  
- LinkedIn (2 company pages), X, Flickr  
- YouTube, Vimeo, TikTok (varias + Ads Manager)  

### 4.5 Marketing tools → `30` / `40` / `60`

- Serprobot, Mailchimp, Hotjar, RD Station, Medium, tawk.to, Spotify  
- Backlinks (Growwer, LinkAtomic, eReferer)  
- Canva, CapCut, Suno, ChatGPT, ElevenLabs, AnswerThePublic, D-ID  
- Platzi, ThemeForest, Fotos Premium (Shutterstock/iStock)  

### 4.6 Telecom / oficina → `70` / `90` / `80`

- Toll Free Forwarding, Twilio, MyTelfon, Sonetel, iPhone  
- PromPerú (registro / TurismoIn), DJI, imágenes  
- TpLink, Reddit, Pinterest, Open Media Vault / NAS  
- Computrabajo + inventario de correos `@perugrandtravel.com`  

### 4.7 Correos pivote (referencia; no es el cofre)

Ver también `MAPA-HERRAMIENTAS.md`:

| Correo | Uso típico |
|---|---|
| clever@ | Raíz / hosting / admin |
| marketing@ | Día a día tools SEO/ads |
| ventas@ / reservations@ / reservaciones@ | Comercial / OTAs |
| seo3@ / seo@ / seo1@ / seo2@ | SEO / blogs |
| rrss1@ / josimar1@ | Redes / propiedad social |
| rrhh@ / contabilidad@ / etc. | Oficinas |

**Acción de proceso:** mantener un Sheet **solo de directorio de casillas** (quién usa qué correo) **sin contraseñas**. Las contraseñas de Gmail/Workspace van en Vaultwarden o se evitan con sesión Google del usuario.

---

## 5. Proceso que alivia a Ricardo

### 5.1 Offboarding (checklist, 15–30 min)

Cuando alguien se va:

1. Desactivar usuario en **Vaultwarden** (pierde todas las colecciones).  
2. Desactivar usuario en **Google Workspace** (si aplica).  
3. Lista corta “cuentas compartidas tocadas por ese rol” → **rotar solo esas**.  
4. Quitar de Meta Business / TikTok Ads / RD Station / WP users **como usuario**, no cambiando el pass master si no hacía falta.  
5. Marcar en `99-archivo` si se cierra una cuenta.

**Meta:** dejar de “cambiar 80 contraseñas del Excel” y pasar a “revocar 1 usuario + rotar 3–8 compartidas”.

### 5.2 Onboarding

1. Crear user Vaultwarden + asignar colecciones del cargo.  
2. Invitar a tools con SSO/Google cuando exista.  
3. Entregar solo lo de su rol; nada del Excel completo.

### 5.3 Reducir contraseñas variadas (sí, es ideal)

| Preferencia | Ejemplo |
|---|---|
| Mejor | Login con Google / “invitar miembro” |
| Aceptable | 1 cuenta compartida por tool en colección + pass fuerte + 2FA en celular de la empresa |
| Evitar | Misma pass débil en 10 sitios; pass en Sheet; 2FA en celular personal de un empleado |

No hace falta “una contraseña distinta por gusto”: hace falta **una fuerte por cuenta** generada por el manager, y **menos cuentas compartidas**.

### 5.4 2FA

- Preferir app TOTP en cuenta **de rol** (ej. celular marketing documentado) o Bitwarden TOTP donde la política lo permita.  
- Documentar en notas del ítem: “2FA en cel XXX / dueño Y”.  
- Códigos de recuperación: solo en `00-critico` o `21-rrss-sensibles`, nunca en Sheet.

---

## 6. Migración desde el Excel (fases)

| Fase | Qué | Quién | Hecho cuando |
|---|---|---|---|
| **0** | Congelar Sheet como “legacy”; avisar: no añadir secretos nuevos ahí | Ricardo | Mensaje al equipo |
| **1** | Instalar Vaultwarden + HTTPS + backup; Ricardo + Clever como owners | Ricardo (+ Jairo apoyo doc) | Login OK en 2 dispositivos |
| **2** | Migrar `00-critico` + `10-web-wp` + `11-cpanel` | Ricardo | Esos ítems viven en cofre |
| **3** | Migrar RRSS, ads, CRM, OTAs por bloques | Ricardo + owners | Colecciones llenas |
| **4** | Sheet → solo inventario (sitio, URL, owner, colección) **sin columna contraseña** o archivar | Ricardo | Excel deja de ser fuente de secretos |
| **5** | Checklist offboarding usado 1 vez real | Ricardo | Tiempo medido < 30 min |

**No migrar de golpe las 200 filas:** críticos primero.

---

## 7. Qué NO hacer

- App interna custom “para administrar contraseñas” (salvo UI de inventario sin secretos).  
- Seguir pidiendo el Excel completo por WhatsApp/Drive.  
- Pegar contraseñas en chats de IA, Notion público o este repo.  
- Una sola colección “todo PGT” para 20 personas.

---

## 8. Pitch corto para Ricardo / Clever

> El Excel nos sirve de inventario, pero cada salida de personal obliga a rotar demasiadas claves porque todo es compartido y visible.  
> Propuesta $0: Vaultwarden en nuestro servidor + clientes Bitwarden.  
> Accesos por rol; al salir alguien se le quita el usuario y solo se rotan las pocas cuentas compartidas.  
> El Sheet queda sin contraseñas.  
> Empezamos por hosting, dominios y WordPress.

---

## 9. Riesgo inmediato (seguridad)

En la conversación del 28 ago se pegaron usuarios/contraseñas/notas del Sheet (y hay captura visible). Tratar esas credenciales como **potencialmente expuestas**.

**Acción recomendada (Ricardo):** rotar al menos `00-critico-owners` y WP/cPanel principales cuando se active el cofre; no reutilizar las claves del Sheet.

---

## 10. Próximos pasos concretos

1. Jairo: este doc + actualizar `MAPA-HERRAMIENTAS.md` (enlace).  
2. Jairo ↔ Ricardo: 20 min — enseñar mock de colecciones + offboarding.  
3. Decidir host: VPS vs NAS.  
4. Fase 1 técnica (Docker Vaultwarden) — **solo con OK de Ricardo/Clever**.  
5. Actualizar inventario vivo en `MAPA-HERRAMIENTAS.md` cuando cambien tools SEO; no duplicar el Excel entero aquí.

---

## Apéndice A — Mapeo rápido Excel → colección

| Bloque Excel | Colección |
|---|---|
| HOSTING / GODADDY / REGISTROS | `00-critico-owners` |
| PAGINAS WEBS (WORDPRESS) | `10-web-wp-admin` |
| PAGINAS WEBS (CPANEL) | `11-web-cpanel` |
| Blog / BLOGS PGT | `12-web-blog` |
| Linktree + FACEBOOK…TIKTOK | `20-rrss` |
| CUENTAS FALSAS (FACEBOOK) | `21-rrss-sensibles` |
| serprobot, ads, hotjar, answer the public, backlinks | `30-ads-analytics` |
| Mailchimp, RD STATION, tawk | `40-crm-email` |
| WETRAVEL…CAMINO INCA, OTAs, REVIEWS | `50-otas-reservas` |
| CANVA, IA, CAPCUT, SUNO, PLATZI, FOTOS… | `60-diseno-ia` |
| TOLL FREE…Sonetel, IPHONE | `70-voip-telefonos` |
| COMPUTRABAJO, CORREOS PGT, PromPerú | `80-rrhh-corp` |
| TpLink, NAS/OMV, staging clever, WiFi | `90-infra-local` |
| cuenta eliminada / no existe / sin acceso | `99-archivo` |
