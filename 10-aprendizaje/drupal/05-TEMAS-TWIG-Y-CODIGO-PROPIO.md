# Temas Twig y código propio — ¿puedo? ¿conviene?

## Respuesta corta

**Sí, en Drupal se pone código propio.** Es normal y profesional.  
**Conviene** para tema (Figma), schema fino, integraciones WhatsApp/UTM, migraciones.  
**No conviene** reescribir el core ni “plugins piratas portados”.

## Dónde vive tu código

| Lugar | Qué pones | Riesgo |
|---|---|---|
| **Tema custom** (`themes/custom/pgt_theme`) | Twig, CSS, JS, `*.theme` preprocess | Bajo si no tocas core |
| **Módulo custom** (`modules/custom/pgt_seo`) | Schema, hreflang helpers, hooks | Bajo–medio |
| **Módulo contribute** (Drupal.org) | Metatag, Redirect, Pathauto… | Bajo si oficiales + updates |
| Parches al core | Casi nunca | Alto |
| “Nulled” / ZIP raros | Nunca | Virus otra vez |

## Twig (lo mínimo que debes leer)

Twig = plantillas HTML con lógica limitada.

```twig
{# node--tour.html.twig #}
<article>
  <h1>{{ label }}</h1>
  <p class="price">{{ content.field_price }}</p>
  <a href="{{ content.field_whatsapp }}">WhatsApp</a>
  {{ content.body }}
</article>
```

Variables vienen de preprocess en PHP (`.theme` o módulo).

## ¿Conviene código propio vs solo módulos?

| Necesidad | Mejor enfoque |
|---|---|
| Title/meta básicos | Metatag (módulo) |
| 301 masivos | Redirect (módulo) + CSV |
| Product/Offer schema exacto | Metatag Schema **o** módulo custom pequeño |
| Diseño Figma | Tema Twig custom |
| Importar tours desde WP | Migrate API + **custom migrate plugins** |
| CTA WA + UTM | Campo + Twig (simple) |

## Cursor + Drupal

Yo puedo:

- Escribir Twig, CSS, módulo custom PHP, YAML de config.
- Revisar PRs / diffs.
- Armar scripts de mapa 301, validadores schema.
- Documentar content types.

Yo **no** debería:

- Que pegues TOTP/claves en el chat.
- Entrar yo solo a producción Banahosting con tu sesión.

Cómo: `08-COMO-ME-AYUDA-EL-AGENTE.md`.

Siguiente: `06-MODULOS-SEO.md`.
