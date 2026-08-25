# NAS OpenMediaVault + accesos de oficina

Verificado el 25 ago 2026 desde pantallas de Jairo. Sin contraseñas en este archivo.

## Qué es

**OpenMediaVault (OMV)** — NAS (almacenamiento en red) sobre Linux/Debian. No es “la nube”: es un PC/servidor en la oficina que comparte carpetas por **SMB/CIFS** (lo que Windows monta como `Z:`).

| Dato | Valor |
|---|---|
| IP | 192.168.1.87 |
| Hostname | marketingpgt |
| OMV | 6.5.6-1 (Synchrony) |
| Kernel | Linux 7.0.10+deb13-amd64 |
| CPU | AMD Ryzen 5 5600GT |
| RAM | ~15 GiB (uso bajo el día 1) |
| Disco | /dev/sda1 ~2.74 TiB, ~860 GiB usados |
| Uptime visto | ~10 días |
| Servicios | SMB/CIFS, SSH, File Browser |
| Alertas | Updates disponibles + **restart required** |

Panel web: `http://192.168.1.87` (HTTP, “Not secure” — normal en LAN).

## Carpetas que viste

En el share `Marketing`: anuncios, videos por mes 2026, Corpus/Inti Raymi drone, fotos web, “FOTOS PARA Q EDITE LIDIA”, landing producto, contenido bajo estrategia, mapas de circuitos, etc. Es el **DAM informal** del equipo creativo.

También existe share/usuario `linux_admin` en el árbol del explorador.

## Usuarios OMV (panel Users)

| Usuario | Grupos | Lectura |
|---|---|---|
| Marketing | users | Cuenta compartida del equipo para el share |
| linux_admin | _ssh, adm, **sudo**, users | Cuenta que creaste; privilegios de administración del Linux |

El login web que viste con usuario `admin` es el **admin de OMV**, distinto de estos dos.

## Contraste con el informe de Gemini

| Afirmación Gemini | Veredicto |
|---|---|
| Panel en 192.168.x.x, OMV | Correcto (87) |
| marketing@ + 2FA celular 908882425 | Coherente con Excel/notas |
| Device registrado en Google | Plausible; no lo re-verificamos aquí |
| DNS/Banahosting/Google Admin en clever@ | Correcto según Excel |
| TOTP / secretos en el cuadro de accesos | **Sí están en el Excel — no los copies a Git ni a chats** |
| “Control sobre el panel OMV” como logro | Matiz: entraste; crear `linux_admin` con **sudo** es privilegio alto |

## Cómo usarlo bien (y cómo no)

**Sí**
- Montar `Marketing` en la laptop para videos/fotos pesados sin saturar Drive.
- Trabajar assets del mes (agosto videos, landings).
- Avisar a Ricardo: *“monté el share en mi laptop con un usuario propio para no usar la sesión de todos”*.

**No**
- Guardar el Excel de Accesos dentro del NAS y además en un repo git.
- Usar sudo en el NAS “para experimentar”.
- Reiniciar el servidor aunque OMV pida restart — eso lo decide quien opera la oficina.
- Asumir que WiFi rápido en tu laptop es “mejor infraestructura”: la PC cableada puede estar mal configurada; no lo digas como ataque a sistemas.

## Relación con el rol

El NAS explica el volumen creativo (Lidia, video, drone, Corpus). Un jefe de marketing digital ordena **prioridad y URL de destino**, no archiva carpetas. El SEO técnico casi no necesita sudo en OMV; necesita GSC y WP.
