# Admin Drupal — día a día (para no romper nada)

## Reglas de supervivencia

1. **Staging primero.** Si no sabes si es staging, pregunta.
2. No borres contenido “para probar”. Duplica o usa entorno local.
3. Después de cambiar config: alguien debe **exportar config** (YAML) al repo — si trabajan con Composer/Git.
4. Cache: si no ves cambios → `drush cr` o “Clear all caches” en admin.
5. Nunca instalar módulo desde ZIP desconocido (virus 2.0).

## Rutas admin típicas

| Qué | Ruta aprox. |
|---|---|
| Lista contenido | `/admin/content` |
| Content types | `/admin/structure/types` |
| Campos de Tour | `/admin/structure/types/manage/tour/fields` |
| Menús | `/admin/structure/menu` |
| Idiomas | `/admin/config/regional/language` |
| Metatag | `/admin/config/search/metatag` |
| Pathauto | `/admin/config/search/path` |
| Redirects | `/admin/config/search/redirect` |
| Extensiones (módulos) | `/admin/modules` |
| Reportes | `/admin/reports` |

## Publicar un tour (checklist editorial)

1. Idioma correcto.
2. Alias = URL acordada (o dejar Pathauto + Redirect).
3. Precio + moneda.
4. Imagen con alt.
5. CTA WhatsApp.
6. Metatag revisado (no genérico).
7. Traducciones enlazadas.
8. Vista previa.
9. Publicar.
10. Verificar en front + Rich Results Test / view-source schema.

## Qué pedir el día 1 en Drupal

- Usuario con rol **Content editor** o similar (no hace falta admin total al inicio).
- URL staging.
- Quién es el **implementador** (agencia / Ricardo / freelance).
- Acceso al repo Git del tema (ideal) o ZIP del theme.

Siguiente: `08-COMO-ME-AYUDA-EL-AGENTE.md`.
