# Drupal — panorama completo: qué instalar, dónde, por qué

**Para:** Jairo · 26 ago 2026 · Drupal de PGT aún no listo  
**Lee esto ANTES** del tutorial `10-TUTORIAL-EXPLORAR-DRUPAL.md` (ese asume staging de la empresa).

---

## 1. Primer principio: ¿Drupal es un programa de escritorio o una web?

**Drupal no es como Word o Photoshop.**  
No abres “Drupal.exe” y ya.

Drupal es un **sistema web**:

1. Corre en un **servidor** (Linux + PHP + base de datos).  
2. Tú lo usas en el **navegador** (Chrome):  
   - Visitantes: `https://sitio.com/tour/...`  
   - Tú (admin): `https://sitio.com/user/login` → panel `/admin`

| Pregunta | Respuesta |
|---|---|
| ¿Se usa en la web? | **Sí.** El día a día es el navegador. |
| ¿Hay que instalar algo? | Sí, **en un servidor** (o en tu PC simulando un servidor). |
| ¿En Windows nativo? | Posible pero feo. Mejor **WSL (Linux dentro de Windows)**. |
| ¿Necesitas VPS en la laptop? | **No** para empezar. |
| ¿Cuenta en Drupal.org? | Opcional (docs/foro). No es el login del sitio. |

**Analogía:** WordPress/Drupal = el restaurante.  
El **servidor** = el edificio y la cocina.  
El **navegador** = cómo entras a comer o a la oficina del gerente (`/admin`).

---

## 2. Los tres “sitios” donde puede vivir Drupal

| Dónde | Qué es | Para ti ahora |
|---|---|---|
| **A. Staging/prod PGT** | Lo que arma el jefe en la VPS Ubuntu | Aún no existe → no esperes solo esto |
| **B. Local (tu laptop)** | Drupal de práctica en WSL | **Sí, para volverte experto** |
| **C. Demo online** | Sitio de prueba en internet (temporal) | **Sí, hoy mismo, 0 instalación** |

Orden inteligente:

```
Hoy (0–1 h):     C — demo online → tocar el admin sin instalar nada
Esta semana:     B — local en WSL → practicar de verdad
Cuando PGT tenga staging: A — mismo conocimiento, datos reales
En paralelo ligero:       Ubuntu/VPS basics → hablar el idioma del jefe
```

---

## 3. ¿Windows, Linux o WSL?

Tú ya estás en **Windows + WSL2**. Eso es ideal.

| Opción | Veredicto |
|---|---|
| Solo Windows | No recomendado para Drupal moderno (Composer, DDEV, permisos) |
| Linux aparte (dual boot) | Innecesario ahora |
| **WSL2 Ubuntu** | **Sí — aquí instalas la práctica** |
| VPS del jefe | Producción/staging empresa — él administra; tú aprendes a **usar** y más adelante a **entender** |
| “VPS en mi laptop” | Confusión de términos. Una VPS es un servidor en la nube. En la laptop haces **local**, no una VPS de verdad |

**PHP:** lo necesita el **servidor** donde corre Drupal.  
Con la herramienta **DDEV** (recomendado), PHP/MySQL se instalan solos en contenedores. Tú no instalas PHP “a mano” el día 1.

---

## 4. Camino A — HOY, sin instalar nada (empápate del admin)

Objetivo: ver menús, content types, nodos, como en el tutorial, pero en un Drupal público de prueba.

### Opción fácil: Simplytest / demos oficiales

1. Abre en Chrome: busca **“Simplytest.me Drupal”** o ve a la doc de Drupal “Try Drupal”.  
2. Lanza un Drupal 10/11 temporal (vive ~1 h o el tiempo que diga).  
3. Entra al admin (te dan usuario/clave en la misma página).  
4. Sigue solo esto:

| Paso | Dónde | Qué mirar |
|---|---|---|
| 1 | `/admin/content` | Lista de contenido (= nodes) |
| 2 | Crear → Article | Rellenar título, body, guardar |
| 3 | Ver la página en el front | “Así se ve lo que guardé” |
| 4 | `/admin/structure/types` | Content types (moldes) |
| 5 | Extender / Modules | Lista de módulos (no instales 20) |

**Por qué:** separas “aprender el panel” de “aprender a instalar servidores”.  
Si te pierdes en Docker el día 1, igual ya viste el admin.

Cuando el demo expire, no pasa nada: era de práctica.

---

## 5. Camino B — Esta semana: Drupal local en WSL (para ser bueno de verdad)

### ¿Por qué local?

- Puedes romper cosas sin miedo.  
- Ves archivos Twig, `composer`, tema.  
- Es lo más parecido a lo que el jefe monta en Ubuntu, pero en tu máquina.

### ¿Qué vas a instalar? (panorama)

| Pieza | Para qué |
|---|---|
| **WSL2 + Ubuntu** | Linux dentro de Windows (ya lo usas) |
| **Docker Desktop** (Windows) | Motor que DDEV usa |
| **DDEV** | “Botón fácil”: crea PHP + DB + URL local |
| **Composer** (vía DDEV) | Instala Drupal y módulos |
| **Drupal 11** | El CMS en sí |

Tú abres: `https://tuproyecto.ddev.site` en Chrome → admin.  
No es magia distinta: **sigue siendo uso por web**; solo que el servidor está en tu WSL.

### Guía de instalación (orden fijo)

Hazlo un sábado o noche (60–90 min la primera vez).

#### B1. Comprueba WSL

En PowerShell o terminal WSL:

```bash
wsl -l -v
uname -a
```

Debes ver Ubuntu y WSL 2.

#### B2. Instala Docker Desktop en Windows

1. Descarga Docker Desktop para Windows.  
2. En settings: integra con WSL2 / tu distro Ubuntu.  
3. Reinicia si pide.  
4. En Ubuntu WSL: `docker version` debe responder.

#### B3. Instala DDEV dentro de WSL (Ubuntu)

Sigue la doc oficial DDEV para Linux/WSL (comandos `curl` / `apt` según su guía actual).  
Comprueba:

```bash
ddev version
```

#### B4. Crea un proyecto Drupal de práctica

```bash
mkdir -p ~/proyectos/drupal-practica
cd ~/proyectos/drupal-practica
ddev config --project-type=drupal11 --docroot=web
ddev start
ddev composer create drupal/recommended-project:^11
ddev composer require drush/drush
ddev drush site:install -y
ddev launch
```

(Si algún comando falla por versión, pégame el error y lo ajustamos — las flags cambian un poco.)

#### B5. Entra al admin

- URL que DDEV te muestre  
- Usuario `admin` (o el que pidió el instalador)  
- Ahora sí: `10-TUTORIAL-EXPLORAR-DRUPAL.md` §§2–5 **sobre tu práctica local**

#### B6. Cómo “sacarle el máximo provecho”

No solo clicar. Cada día de práctica:

1. Crear content type `tour` con campos precio + WhatsApp.  
2. Crear 2 nodes tour.  
3. Instalar módulos **oficiales**: Metatag, Pathauto, Redirect (`ddev composer require ...` + enable).  
4. Crear un alias igual a una URL tipo PGT.  
5. Crear un 301 de prueba.  
6. Abrir el tema y mirar un `.html.twig` (aunque no lo edites aún).

Eso es exactamente el oficio de la migración PGT, en vacío.

---

## 6. La VPS Ubuntu del jefe — qué es y qué te conviene aprender

### Qué es una VPS

**Virtual Private Server** = un Linux en la nube (DigitalOcean, Hetzner, etc.) con IP pública.  
Ahí instalarán Nginx/Apache + PHP + MariaDB/MySQL + Drupal (o Docker).  
Eso será probablemente el **staging/prod** de PGT.

### Qué solo él sabe (por ahora)

Accesos root, firewall, DNS, SSL, deploy.  
**No digas “yo administro la VPS”** el día 2.

### Qué SÍ te ayuda a dominar (contrarresta falta de experiencia)

Aprende el **idioma** (1 h cada 2 días, sin root de PGT):

| Tema | Por qué |
|---|---|
| SSH `ssh user@ip` | Entrar al servidor |
| `cd`, `ls`, `nano`/`vim` | Moverte |
| `sudo apt update` | Paquetes |
| Nginx/Apache = “quién sirve HTTP” | Conversar cutover |
| SSL / HTTPS | Seguridad |
| `drush` en servidor | Igual que local |
| Logs (`/var/log/...`) | Debug caídas |
| Permisos `www-data` | “Por qué no sube la imagen” |

**Práctica segura:** una VPS barata **tuya** ($5/mes) más adelante — no toques la de ellos sin permiso.  
O solo WSL: 80% del vocabulario Linux es el mismo.

### Frase útil con el jefe

> “Estoy montando Drupal local con DDEV para no frenar mientras termina la VPS. Cuando haya staging, ya conozco el admin, Metatag y Redirect. Si quieres, después me enseñas el esquema de la VPS (Nginx, PHP-FPM, deploy).”

Eso suena a aliado, no a amenaza.

---

## 7. Relación con el tutorial que te confunde

| Archivo | Cuándo usarlo |
|---|---|
| **Este** (`11-COMO-PRACTICAR-SIN-STAGING-PGT.md`) | Ahora — panorama + instalar práctica |
| `10-TUTORIAL-EXPLORAR-DRUPAL.md` | Cuando tengas **cualquier** Drupal abierto (demo, local, o PGT) |
| Playbook migración | Cuando hablemos de URLs PGT |

El tutorial viejo empezaba en “entra al staging de PGT” → por eso te mareó: **ese staging no existe aún**.

---

## 8. Qué NO hacer

- Instalar Drupal a ciegas en la VPS del jefe.  
- Descargar “Drupal nulled” / temas pirata (virus otra vez).  
- Dual boot solo para aprender.  
- Estudiar PHP 8 horas antes de ver el admin 15 minutos.  
- Creer que “cuenta Drupal.org” = acceso al sitio PGT.

---

## 9. Plan concreto (esta semana)

| Día | Qué | Dónde |
|---|---|---|
| Hoy | Camino A: demo online 45 min | Chrome |
| Hoy/mañana | Seguir auditando 1–2 URLs de tu bloque PGT | Chrome prod |
| Noche 1–2 | Docker Desktop + DDEV en WSL | Windows + WSL |
| Noche 3 | `ddev` + Drupal instalado + tutorial §§2–5 | Local |
| Noche 4 | Content type Tour + Metatag + Redirect de prueba | Local |
| Cuando exista staging PGT | Repetir tutorial en **su** URL | Empresa |

---

## 10. Autotest — “¿ya entendí el panorama?”

Responde en voz alta:

1. ¿Drupal se usa en el navegador o como app de escritorio? → **Navegador.**  
2. ¿Dónde corre el PHP? → **En el servidor (VPS o DDEV local).**  
3. ¿Necesito la VPS del jefe para empezar? → **No.**  
4. ¿WSL para qué? → **Practicar Linux + DDEV en tu laptop.**  
5. ¿Qué practico primero sin instalar? → **Admin en un demo online.**

Si alguna falla, relee §1–3.

---

## 11. Cuando te atasques al instalar

Pégame:

- Salida de `wsl -l -v`  
- `docker version`  
- `ddev version`  
- El error completo del comando que falló  

Lo depuramos paso a paso. No hace falta que el jefe termine la VPS para que tú avances.
