# Multidioma y Domain (4 sitios PGT)

## El problema que tienen hoy

4 WordPress ≈ 4 catálogos. Hreflang a mano o inexistente. Gaps PT. Lujo solo EN.

## Cómo lo resuelve Drupal (2 patrones)

### A) Un sitio, varios idiomas (Content Translation)

- Un node Tour con traducciones `en`, `es`, `pt-br`, `it`.
- URLs: prefijo `/en/…`, dominio único, o path prefix.
- Hreflang lo generan módulos de idioma si se configura bien.

### B) Varios dominios, un backend (módulo Domain / Domain Access)

- `perugrandtravel.com`, `machupicchupacotes.com`, etc. apuntan al mismo Drupal.
- Contenido asignado a dominios.
- Más cercano a “seguir con 4 marcas/URLs”.

**Pregunta crítica al equipo (hoy/mañana):**

> ¿Drupal será un solo dominio con idiomas, o Domain con los 4 dominios actuales?

Si cambian a un solo dominio sin 301 desde los 4 → **catástrofe SEO**.

## Hreflang

En migración debes exigir:

1. Mapa de equivalencias (ya tienes CSV en `09-herramientas/equivalencias-hreflang.csv`).
2. Que cada traducción enlace a las otras.
3. Validación post-cutover: Screaming Frog / site: / GSC Internacional.

## Pathauto por idioma

Aliases pueden diferir por idioma (`/tour/salkantay…` vs `/pacote/…`).  
**Regla de oro:** el alias publicado = URL que ya rankea, o Redirect 301 desde la vieja.

Siguiente: `05-TEMAS-TWIG-Y-CODIGO-PROPIO.md`.
