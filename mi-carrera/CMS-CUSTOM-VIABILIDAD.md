# CMS custom (código + admin) — ¿viable para PGT?

**Respuesta corta:** Sí es viable **para ti** a medio plazo. **No** es lo recomendable como primera propuesta en la semana 1. La jugada que te posiciona mejor: **win SEO en WordPress → tema hijo o headless POC → propuesta escrita**.

Tu intuición es correcta: control del código, IA, admin a medida para Lizet/Ricardo/CM. El riesgo no es técnico — es **político, operativo y SEO**.

---

## Por qué te conviene (steelman)

| Ventaja | En PGT |
|---|---|
| CWV y schema como código | Goodlayers hoy penaliza LCP y rompe Offer |
| Un `Tour` = 4 idiomas, cero huecos PT | Problema #1 del negocio |
| Admin personalizado | Lizet ve landings; Ricardo ve redirects; CM ve blog sin romper SEO |
| Automatización + IA | Bulk meta, hreflang, checks pre-publicar |
| Te diferencia vs "solo SEO" | Jefe que entiende producto digital, no solo keywords |
| Figma → React | Encaja con diseño modular del PDF |

---

## Por qué NO empezar por ahí (semana 1–4)

| Riesgo | Qué pasa en la práctica |
|---|---|
| Ricardo es el hub técnico | "Jairo quiere tirar WordPress" = amenaza, aunque tengas razón |
| Clever mide keywords mensuales | Cualquier cutover = dip 4–8 semanas |
| 73 tours + 454 blogs | No es un landing; son meses de modelo + migración |
| Equipo no técnico | Sin admin usable, cada precio = ticket a ti → te quemas |
| Drupal ya en conversación | Tres frentes (WP, Drupal, custom) = parálisis |
| Tu meta es jefatura en 14 días | Necesitas **resultados medibles**, no repo en GitHub |

---

## Stack recomendado si lo haces en serio

No "HTML a mano". La forma profesional:

```
Next.js (front, SEO, i18n, schema)
    ↕ API
Payload CMS o Sanity (admin para no-devs)
    ↕
PostgreSQL / Mongo
    ↕
Media (S3 o NAS para assets pesados)
```

Alternativa intermedia (menor drama):

```
WordPress headless (solo backend + Tourmaster migrado gradualmente)
    ↕ REST/GraphQL
Next.js front
```

**Evitar:** admin 100% custom desde cero sin framework CMS — reinventas usuarios, roles, media, revisiones, preview.

---

## Alcance realista por fases

### Fase 0 — Ahora → 2 semanas (obligatorio antes de hablar de custom)

- Línea base GSC de tu bloque
- 1 win en WordPress (tema hijo **una** plantilla tour, **mismas URLs**)
- Preguntas: ¿Drupal tiene vendor? ¿Figma cambia slugs?

### Fase 1 — Mes 1–2 (credibilidad)

- Tema hijo WP completo desde Figma en **staging** (`demo.perugrandtravel.com`)
- Mapa 1:1 URLs actuales → nuevas plantillas
- Documento "por qué no cambiamos slugs"

### Fase 2 — Mes 2–4 (POC headless)

- 1 tour + 1 blog en Next + Payload en subdominio staging
- Paridad: schema, hreflang, WA, pixel
- Demo interna a Ricardo + Clever (**no producción**)

### Fase 3 — Mes 4–8 (decisión)

- Cutover por dominio (PT primero o el que acuerden)
- 301 masivo verificado
- 60 días vigilancia GSC + tablas keywords

**Duración honesta full custom 4 sitios:** 4–8 meses **contigo a tiempo parcial**, 2–4 meses con otro dev.

---

## Qué debe tener el admin (checklist producto)

Para que marketing no dependa de ti:

| Módulo | Usuario | Must have |
|---|---|---|
| Tour | SEO, ops | Precio por mercado, idiomas, includes, CTA WA, slug bloqueado |
| Blog | CM | Editor rich, categorías, preview, SEO fields (title, meta, canonical) |
| Media | Diseño | NAS/cloud, alt text obligatorio |
| Redirects | Ricardo | 301 manager |
| Roles | Todos | CM no toca schema; SEO no toca DNS |
| Publicación | Todos | Checklist pre-publish (hreflang, precio, imagen LCP) |
| i18n | SEO | Un tour, N traducciones, no duplicar catálogo |

---

## Costos ocultos

- Hosting (Vercel + DB + CDN vs Banahosting flat)
- Backups, WAF, uptime — hoy lo lleva WP/hosting
- **Tu tiempo** — si eres jefe, no puedes ser único dev
- Deuda si te vas — documentación y handoff
- Temporada alta — no migrar jun–ago

---

## Cómo proponerlo sin sonar a capricho

**Mal (semana 1):**

> "Tiro WordPress y lo hago en Next yo solo."

**Bien (después de 1–2 wins):**

> "Medimos que el cuello es plantilla + catálogo en 4 sitios. Propongo fase 1: mismo WordPress, tema hijo, URLs congeladas. Fase 2: un tour en staging headless para comparar velocidad y workflow. Decisión con datos, no con opinión."

Eso es **jefe + técnico**, no fanático.

---

## Comparación rápida

| Criterio | WP tema hijo | Drupal | Next + Payload |
|---|---|---|---|
| Time to first win | Días–semanas | Meses | Semanas (POC) |
| Riesgo keywords | Bajo si mismas URLs | Alto | Medio |
| Admin para CM | Conocido | Curva alta | Bueno si diseñas UX |
| Tu velocidad con IA | Alta | Media-baja | Muy alta |
| Si te vas | Ricardo sigue | Huérfano probable | Huérfano si no hay doc |
| Encaje revisión 2 sem | ★★★★★ | ★ | ★★ |

---

## Decisión para ti

1. **Sí, persigue custom** como visión 12–18 meses y como diferenciador de jefatura.
2. **No, no lo lideres** como proyecto día 1–14.
3. **Sí, usa código** ya en: snippets, scripts, tema hijo, informes, automatización GEO.
4. **POC Payload** solo después de línea base GSC + Ricardo te respete en lo operativo.

Lectura relacionada: `08-investigacion/STACK-IDEAL.md`, `08-investigacion/FIGMA-LECTURA.md`.
