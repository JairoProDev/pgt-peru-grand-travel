# Inventario de sistemas (sanitizado)

Fuente: Excel `Accesos PGT -2026 Actuales.xlsx` (Ricardo), leído 25 ago 2026.  
**Este archivo NO contiene contraseñas ni secretos 2FA.** Esos viven solo en el Excel de ellos / tu copia local fuera de git.

Actualizado: agosto 2026 (según el propio Excel).

## Hallazgo clave

La auditoría pública de agosto hablaba de **4 dominios**. El Excel lista **muchos más sitios WordPress y blogs satélite**. El trabajo SEO real es más grande de lo que el aviso sugería — y explica que sean **4 personas en SEO**.

## WordPress / webs (wp-admin o cPanel listados)

| Sitio | Notas del Excel |
|---|---|
| perugrandtravel.com | US / EN + `/payments/` + blog |
| machupicchupacotes.com | PT + blog |
| viajesmachupicchutours.com | ES + blog |
| viaggiomachupicchu.it | IT |
| paquetesdeviajesperu.com | ES legacy |
| vinicuncaperu.com | ES |
| luxuryperutour.com | (+ staging) |
| incatrailbookings.com | US |
| tripstomachupicchu.us | US |
| machupicchuperu.com.mx | ES / MX |
| dicasviagem.com | Blog PT satélite |
| perutravelguides.com | Blog / marca contenido |
| clever.pe | Página personal Clever (también en Drive) |

Blogs con usuarios `seo3@` / `copywriter` / `ClairePGT` en varios `/blog/wp-admin`.

## Hosting y DNS

- **Banahosting** — usuario raíz típico `clever@perugrandtravel.com`
- **Registros.com** — dominios
- **GoDaddy** — dominios
- **cPanel** por cada sitio (usuarios distintos por dominio)

Sin `clever@` (2FA en su celular) no tocas DNS/hosting de raíz. Motivo válido más adelante: ticket concreto (SSL, redirect, verificación GSC DNS).

## OTAs y reservas

- GetYourGuide (supplier) — marketing@
- Viator (supplier) — josimar1@
- TourRadar (operators) — josimar1@ (nota: “no accedí”)
- WeTravel — ventas@
- Peru Rail agencias — CPONCE5001
- Camino Inca sistema (negtu.com)
- TuBoleto cultura (disponibilidad)

## Marketing / analítica / stack creativo

RD Station · Hotjar · Mailchimp · Serprobot · UptimeRobot · Trustindex · Canva · CapCut · TikTok Ads · Mail/SMS (Twilio, Sonetel, MyTelfon) · tawk.to · AnswerThePublic · Growwer / link tools · ChatGPT (cuenta marketing, nota de rotación sept) · ElevenLabs · DJI · Shutterstock / iStock

## Redes (páginas, no solo un IG)

Facebook: `.en` / `.br` / `.esp` (+ cuentas “falsas” de mercado — riesgo ético/ToS: no las uses sin criterio del jefe de mkt).  
Instagram: @perugrandtravel, dicasviagem, perutravelguides.  
TikTok varios · YouTube · Vimeo · LinkedIn · X · Pinterest · Flickr · Medium · Spotify · Linktree.

## Correos relevantes al rol

| Correo | Rol aparente |
|---|---|
| marketing@ | Operativo diario SEO/mkt (celular 908882425) |
| clever@ | Google Admin / raíz |
| seo@ / seo1@ / seo2@ / seo3@ | Equipo SEO (seo@ pide celular) |
| rrss1@ | Redes y diseño |
| copywriter@ | Contenido |
| ventas@ / vendas@ / atendimento@ | Ventas EN/PT |
| rrhh@ | Computrabajo empresa |
| otas@ | OTAs (notas de cambio a marketing) |

## Oficina / NAS

Open Media Vault ya figura en el Excel. Host real visto el día 1: **192.168.1.87**, hostname `marketingpgt`. Detalle: `NAS-Y-ACCESOS.md`.

## Implicaciones para el trabajo

1. Antes de “arreglar hreflang en 4 sitios”, confirma con Ricardo **qué dominios están vivos, indexables y son prioridad** vs marcas satélite / legacy.
2. Las tablas de keywords por idioma probablemente cruzan varios de estos dominios — pide el archivo canónico (`PGT_URLs_keywords…` / estudios en Drive Ricardo).
3. Viator + GYG + TourRadar refuerzan el argumento de margen, pero el mix hay que medirlo, no inventarlo.
4. RD Station = CRM/automatización (fuerte en BR). Pregunta quién lo vive: ventas o mkt.
