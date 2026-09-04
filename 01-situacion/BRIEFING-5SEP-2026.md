# Briefing — viernes 5 sep 2026

**Para:** Areli, Lizet, Ricardo, Einel, Jairo  
**Sitio de trabajo:** https://next.perugrandtravel.com (noindex) · CMS: https://next.perugrandtravel.com/admin/  
**No tocar:** DNS `www` / `@` — WordPress sigue siendo el canónico público.

---

## Qué hay vivo ahora (Next)

- Catálogo **EN / ES / PT** real (no clon EN→ES).
- ES **no** tiene `/peru/`. Destinos: `/es/destinos/`, `/es/tours-lima/`, `/es/camino-inca/`, etc.
- PT **sí** tiene `/pt/peru/cusco/` etc.
- Footer, header, búsqueda ⌘K, CTA de blog y 404 en el idioma de la URL.
- CMS Payload en Neon free: pestaña Contenido / SEO / HTML, Live Preview, “mi parte”.
- Vista previa de `heroImage` pegando URL (sin Blob de pago).

## Quién entra al CMS

| Persona | Email | Rol |
|---------|-------|-----|
| Jairo | cms@perugrandtravel.com | admin |
| Areli | areli@perugrandtravel.com | editor |
| Lizet | lizet@perugrandtravel.com | editor |
| Ricardo | ricardo@perugrandtravel.com | editor |

Filtro: en cada colección, columna **assignee** = tu nombre. El banner “mi parte” está arriba de la tabla.

**Reparto:** mismos tipos de contenido a partes iguales. Lizet no es “solo tours”. Ricardo **no** aprueba precios.

## QA de 25 minutos (hacer hoy)

1. Entrar a `/admin/`, filtrar assignee = tú, abrir 1 tour, 1 blog, 1 página.
2. Cambiar **un** H1 o meta description, Save, Live Preview: ¿se ve en next.?
3. En el sitio: `/es/` footer → un destino → 200. ⌘K “Salkantay” en `/es/` → tours en español.
4. Un clic WhatsApp desde un tour ES: ¿sale el mensaje en español?
5. No editar slugs ni market. Sí puedes tocar HTML (SEO/cuerpo).

## Lo que NO es tu trabajo hoy

- Precios OTAS / `precios:apply` — espera tarifario Ricardo.
- Cutover `www` → Vercel.
- Inventar páginas ES copiando inglés.
- Pedir Vercel Blob / Neon pago.

## Mensaje corto para Einel (mañanas)

next. ya sirve ES/PT con navegación real. El KPI sigue siendo `whatsapp_click` en GA4 (stream EN `G-NTXD373H4Q`). No hace falta un carrito. Sí hace falta que el equipo **entre al CMS** y deje un H1 más vendible en su parte.

## Riesgos visibles

- Algunos tours ES tienen HTML sucio de WP (incluye/no incluye duplicados). Eso se limpia en Payload pestaña HTML, no en un scrape nuevo.
- `next.` sigue noindex. Google no debe tratarlo como canónico.
- Lang switch ahora intenta quedarse en el mismo tipo de página (tour↔tour). Si el slug no existe en el otro idioma, cae a home — no es un 404 inventado.

## Después de este briefing

Ver `pgt-web/docs/PENDIENTES-BETA-5SEP.md` y `08-investigacion/COMPETENCIA-ACCION-SEMANA.md`.
