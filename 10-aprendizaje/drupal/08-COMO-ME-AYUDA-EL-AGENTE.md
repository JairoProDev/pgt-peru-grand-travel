# Cómo te ayudo yo con Drupal (sin login peligroso)

## Respuesta directa

**Sí puedo trabajar en lo que te toque de Drupal** (Twig, CSS, módulos custom, scripts de migración, checklists, 301, schema).  
**No** necesitas (ni debes) iniciar sesión de producción en “el browser del agente” con 2FA pegado en el chat.

## Cómo trabajamos (mejor → peor)

| # | Método | Cómo |
|---|---|---|
| 1 | **Repo Git del tema/módulos** clonado en `/home/jairoprodev/proyectos/pgt/` o carpeta hermana | Yo edito archivos; tú subes PR o despliegas con Ricardo |
| 2 | **Export** Twig/PHP/YAML a `inbox/` o `03-seo/migracion/` | Yo propongo diffs; tú pegas en staging |
| 3 | **Capturas + copy del admin** (content type fields, Metatag) | Yo te digo qué cambiar clic a clic |
| 4 | Staging con usuario editor **tuyas** en tu Chrome | Tú operas; yo guío |
| 5 | Login del agente en cuenta corporativa | **Evitar** (2FA, secretos, ToS, auditoría) |

## Qué pegar / no pegar en el chat

| Sí | No |
|---|---|
| Código Twig/PHP (sin secrets) | Contraseñas, TOTP, cookies de sesión |
| CSV de URLs / 301 | Accesos.xlsx |
| Screenshots de config | “Entra tú a Banahosting” |
| Link staging (si es público o te logueas tú) | Claves de DB en claro |

Ver `mi-carrera/COMO-COMPARTIR-DRIVE.md` y `COMO-COMPARTIR-DATOS.md`.

## Qué pedirme cuando empiece el trabajo real

1. “Aquí está `node--tour.html.twig`” → optimizo schema + WA + CWV.  
2. “CSV de 500 URLs WP” → genero mapa 301 Drupal.  
3. “Export config Metatag” → reviso templates.  
4. “Error en Migrate” → debug del plugin de migración (código).  
5. “Checklist cutover dominio EN” → playbook ejecutable.

## Local Drupal (opcional, más adelante)

Si quieres ambiente local: DDEV o Lando + Composer. Eso es un fin de semana, no día 1. Prioridad mes 1 = **playbook SEO + staging del equipo**, no instalar Drupal en tu laptop sí o sí.

## Límites honestos

- Sin acceso al código/config, solo puedo enseñar y revisar capturas.  
- No reemplazo a la agencia Drupal si ya está contratada: **me sumo como SEO + front/tema**.  
- Producción: cambios solo con OK de Ricardo / implementador.
