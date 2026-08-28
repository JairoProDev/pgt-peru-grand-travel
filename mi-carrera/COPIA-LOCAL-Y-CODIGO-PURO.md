# Copia local del sitio + opinión código puro (26 ago)

## Secretos — regla

**No pegar en Cursor chat:** contraseñas, TOTP, cookies de sesión, dumps con users.  
**Sí:** archivos ya en tu disco (`inbox/`, fuera de git) o repo privado; tú te logueas en cPanel/FTP en **tu** navegador.

`.gitignore` ya bloquea `*.xlsx`, `inbox/`, secretos.

---

## 1. Opinión directa (lo que preguntas)

### Simplytest te abrumó — normal y engañoso

Ese sandbox era **Commerce Kickstart** (tienda Belgrade), no un Drupal limpio de tours PGT.  
Mala primera impresión ≠ “Drupal es absurdo”. Fue como juzgar WordPress entrando a WooCommerce con 50 plugins de demo.

Igual: Drupal **sí** se siente más burocrático que WP o que un admin que tú diseñas. Esa intuición es válida.

### ¿Migración grupal a Drupal vs tú en código puro?

| | Drupal (decisión Clever) | Código puro + admin (tu visión) |
|---|---|---|
| Política ahora | **Ya decidido** | Chocar con el dueño = mal mes 1 |
| Automatizable | Migrate + scripts (sí se automatiza datos) | Muy automatizable con Cursor |
| Admin para Lizet/CM | Hay que configurarlo bien | Tú lo diseñas a medida — **tu mejor argumento** |
| SEO cutover | Mismo problema 301/URLs | **Idéntico** problema |
| Riesgo si te vas | Agencia/Ricardo | Huérfano si no documentas |
| Tiempo realista | Meses (equipo) | Meses (tú + Cursor); no “esta semana” |
| Virus/nulled | Menos plugins basura si higiene | Superficie distinta; ops tuya |

**Cómo lo veo:**

1. **Tu idea de código + paneles admin** es sólida a 6–18 meses y te posiciona.  
2. **Ahora** pelear “tiramos Drupal” te quema con Clever/Ricardo.  
3. Lo trabajoso repetitivo de la migración grupal (mapear tours, 301, QA) **existe igual** en código puro: son los **datos y URLs**, no el CMS. Cursor acelera HTML/admin; no elimina 70 tours × idiomas × Yoast.  
4. Movida inteligente: **cumplir Drupal como empleado** + en paralelo POC local de “tour + admin” en código para **demostrar** después, con datos, no con odio a Simplytest.

Frase para ti (no para la mesa aún):

> Drupal corporativo puede ser el tren que ya salió. Yo me subo al SEO del cutover. El techo técnico que prefiero es front en código + CMS admin; lo prototipo en local y lo presento cuando haya un win, no el día 2.

---

## 2. Qué significa “tener todo en local”

Necesitas **dos** cosas (como el doc de migración):

| Pieza | Contenido |
|---|---|
| A. Archivos | `wp-content/` (tema child, plugins), idealmente core |
| B. Base de datos | Export `.sql` de esa instalación |

Una sola web (empieza por **perugrandtravel.com EN**). No las 10 del Excel el mismo día.

---

## 3. Cómo pedirlo / hacerlo sin pegar secretos aquí

### Opción recomendada (con Ricardo, 15 min)

Mensaje:

> Ricardo, para practicar migración y no tocar prod: ¿me pasas un **backup** de solo perugrandtravel.com (archivos + DB) o me das 20 min en cPanel para bajarlo yo a mi laptop? Lo uso en local WSL, sin subir a ningún lado.

Él puede:

- Generar backup en Banahosting/cPanel → te pasa el ZIP por NAS/Drive interno  
- O darte FTP **solo lectura** / usuario limitado  

Tú descargas a:

```
C:\Users\jairo\Downloads\pgt-wp-backup\   (Windows)
o
/home/jairoprodev/proyectos/pgt/inbox/wp-perugrandtravel-YYYY-MM-DD/
```

Luego me dices: *“el backup está en inbox/…”* **sin** contraseña. Yo te guío para levantarlo con **LocalWP** o **DDEV**.

### Opción B — tú en cPanel (si ya tienes acceso)

En **tu** Chrome (no en el chat):

1. cPanel → Softaculous/Backup o File Manager + phpMyAdmin  
2. Comprimir `public_html` (o la carpeta de esa web)  
3. Export DB `.sql`  
4. Guardar en `inbox/`  

Si te falta usuario cPanel: **no uses clever@** sin permiso. Pide a Ricardo.

### Opción C — solo archivos tema/plugins (menos completo)

FTP → bajar `wp-content/themes` + `wp-content/plugins`.  
Sin DB no tienes tours reales. Sirve para leer PHP; no para “sitio completo”.

---

## 4. Cómo lo levantas en la laptop (después del ZIP)

Camino simple para ti (Windows):

1. Instalar **Local WP** (localwp.com) o DDEV en WSL.  
2. “Import site” / crear sitio vacío e importar SQL + poner `wp-content`.  
3. Ajustar URLs (`wp search-replace` prod → `http://pgt.local`).  
4. Abrir `http://pgt.local/wp-admin` en Chrome.

Ahí sí puedes explorar Tourmaster sin miedo.  
**Producción no se toca.**

---

## 5. Si igual quieres “código puro” con Cursor

Alcance honesto de un POC (no “migración completa”):

| Fase | Entregable |
|---|---|
| 1 | 1 tour hardcodeado en Next (o PHP) desde Figma |
| 2 | Admin mínimo (Payload): editar precio + WA |
| 3 | Import CSV de tus 18 tours |
| 4 | Demo interna a Clever: “así editaría Lizet” |

Eso **sí** lo podemos hacer con archivos locales y sin pelear el tren Drupal.  
La migración total de 4 idiomas + 400 blogs + Ads = proyecto de meses con checklist SEO igual que Drupal.

---

## 6. Qué te pido yo (sin secretos en el mensaje)

Responde solo con **sí/no** o rutas:

1. ¿Ricardo puede darte backup de **solo** perugrandtravel.com?  
2. ¿Tienes cPanel propio o solo wp-admin?  
3. ¿Prefieres Local WP (más fácil) o DDEV en WSL?  
4. ¿El POC código lo quieres en paralelo (noches) sin anunciarlo aún?

Cuando el ZIP/SQL esté en `inbox/` (sin subir a git), escribe:  
`backup listo en inbox/wp-pgt-en/`  
y seguimos instalación local paso a paso.
