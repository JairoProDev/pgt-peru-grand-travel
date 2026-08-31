# Plan SEO — para Clever (v1 · 28 ago 2026)

**De:** Jairo Saul Salas Quiñones · Analista SEO/GEO  
**Para:** Clever  
**Estado:** Listo para enviar (ajusta solo si Einel respondió algo hoy)

---

## 1. Qué entendí del norte del negocio

Perú Grand Travel busca:

1. Más **leads calificados** (WhatsApp / formularios que ventas cierra).  
2. **Fortalecer la marca** (confianza, sin spam ni sitios hackeados).

El SEO/GEO conecta demanda (Google, IA) con la ficha correcta en el idioma correcto.

---

## 2. Cómo está organizado el trabajo SEO

- Equipo: Ricardo, Lizet (Ads), Arely (½), yo.  
- **Mi bloque EN:** 18 tours + 115 blogs (`perugrandtravel.com`).  
- Medición: Sheet keywords + Search Console + GA4.

---

## 3. Línea base (datos reales · 27–28 ago)

### Sitio EN completo (GSC · 28 días)

| Métrica | Valor |
|---|---|
| Clics | **643** |
| Impresiones | **116.000** |
| CTR medio | **0,6 %** |
| Posición media | **25,6** |

### Mi bloque (Sheet keywords · 25 ago)

| | Tours (18) | Blogs (115) |
|---|---|---|
| Impresiones | ~19.700 | ~99.900 |
| Clics | ~18 | ~32 |
| Top 10 Google | 0 | ~10 |

**Lectura:** Hay blogs con **miles de impresiones y casi cero clics** — oportunidad de mejorar títulos/descripciones sin reescribir todo el contenido.

### 3 URLs prioritarias (esta semana)

| URL | Impresiones | Posición | Oportunidad |
|---|---:|---:|---|
| `/blog/things-to-do-in-machu-picchu/` | ~6.115 | ~6 | CTR muy bajo — quick win |
| `/blog/museums-in-machu-picchu/` | ~2.494 | ~6 | Igual |
| `/tour/the-classic-salkantay-trek-5d/` | ~1.218 | ~27 | Enlazar desde blogs MP |

---

## 4. Migración Drupal (lo que ya revisé)

**Staging OVH:** http://147.135.114.64/ · Drupal 11 · solo EN primero.

| ✅ Bien | ⚠️ Riesgo |
|---|---|
| Diseño alineado Figma | URLs distintas a WordPress (`/product/9` vs `/tour/...`) |
| Tours demo visibles | Blog P0 Things Machu Picchu → **404** |
| | Botones "Add to cart" vs WhatsApp actual |
| | Sin schema JSON-LD detectado |
| | Staging indexable (sin noindex) |

**Mi rol:** dueño SEO del cutover — mapa 301, checklist pre-launch, QA 20 URLs, baseline GSC antes/después.

Entregables ya iniciados: inventario 133 URLs, mapa migración 25 URLs top, checklist SEO (`CHECKLIST-PRE-LAUNCH-DRUPAL.md`).

---

## 5. Plan 30 días

### Semana 1 (ahora)
- ✅ Línea base GSC  
- ✅ Inventario bloque Jairo (133 URLs)  
- ✅ Auditorías P0 + checklist Drupal  
- ⬜ Plan enviado a Clever  
- ⬜ Alineación landings Ads (Lizet)

### Semana 2
- Mapa 301 ampliado (50+ URLs)  
- 5 auditorías completas  
- Confirmar slugs finales con Einel  
- Evento GA4 WhatsApp click

### Semana 3
- QA 20 URLs en staging Drupal  
- Quick wins title/meta P0 (con OK CM)  
- Prueba técnica 2 páginas (velocidad/SEO) en subdominio staging

### Semana 4
- Informe mes 1: GSC vs baseline, avance migración, riesgos, mes 2

---

## 6. Qué necesito del equipo

| De quién | Qué | Para cuándo |
|---|---|---|
| **Einel** | Slugs finales WP vs Drupal, WA vs cart, admin Drupal, noindex staging | Esta semana |
| **Ricardo** | DNS subdominio POC (opcional), confirmación NAS linux_admin | Esta semana |
| **Lizet** | URLs landings Ads activas | Esta semana |
| **Clever** | OK prioridades: ¿migración segura primero o quick wins CTR en WP? | Al recibir este plan |

---

## 7. Cierre

Llevo 4 días de onboarding con entregables concretos: baseline Search Console, inventario de mi bloque, revisión del staging Drupal, y prioridades accionables.  
El próximo paso es cerrar el mapa de URLs con Einel y empezar QA antes del cutover EN — para no perder rankings ni leads.

Quedo atento a tu feedback sobre prioridades.

— Jairo

---

*Anexos internos (no enviar a Clever si no pide detalle):*  
`03-seo/datos/mapa-urls-wp-drupal.csv` · `08-investigacion/CHECKLIST-PRE-LAUNCH-DRUPAL.md` · `08-investigacion/DRUPAL-STAGING-REVISION-2026-08-28.md`
