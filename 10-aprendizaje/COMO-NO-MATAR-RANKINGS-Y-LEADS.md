# Cómo NO matar rankings ni leads (en cristiano)

**Ranking** = aparecer en Google.  
**Lead** = alguien que escribe por WhatsApp / form y puede comprar.

La migración puede romper los dos. Tú existes para que no pase — o para detectarlo en 24 h.

---

## Parte A — Cómo se mata un ranking (y cómo evitarlo)

### 1) Cambiar la URL sin avisar a Google

**Qué pasa:**  
Google tiene guardado `/tour/salkantay-trek-4-days/`. Si en Drupal queda `/tours/salkantay` y no hay redirect → **404**. Pierdes clics, posiciones y tiempo.

**Evitar:**  
- Misma ruta (ideal), o  
- **301** de la vieja → la nueva (siempre 301, no 302).

**Tu trabajo:** Sheet `url_antigua → url_nueva → 301`.

### 2) Staging indexado

**Qué pasa:** Google indexa `demo.…` y compite contigo mismo (contenido duplicado) o muestra “sitio de prueba”.

**Evitar:** noindex + a veces login en staging. Verificar con “Inspección de URL” en GSC.

### 3) Sitemap / robots mal

**Qué pasa:** Google no descubre las URLs nuevas, o se le bloquea el crawl.

**Evitar:** sitemap nuevo en GSC el día del cutover; `robots.txt` no debe bloquear `/tour/` en prod.

### 4) Canonical raro

**Canonical** = “la URL oficial de esta página”.  
Si todas apuntan al home, Google ignora tus fichas.

**Evitar:** cada tour canonical a sí mismo (o a la URL canónica acordada en blogs con/sin categoría).

### 5) Hreflang roto o ausente

**Qué pasa:** al brasileño le muestras inglés → rebote → peor conversión; Google confunde idiomas.

**Evitar:** plan de equivalencias EN↔ES↔PT↔IT antes del corte.

### 6) Contenido vacío o thin al migrar

**Qué pasa:** el node existe pero body/precio/itinerario no vinieron del import.

**Evitar:** QA de muestra (10 tours): comparar WP vs Drupal lado a lado.

### 7) Spam / malware residual

**Qué pasa:** Google marca hackeo; rankings caen en bloque.

**Evitar:** no migrar basura; limpiar WP; solo módulos oficiales en Drupal.

---

## Parte B — Cómo se mata un lead (y cómo evitarlo)

### 1) Ficha sin WhatsApp claro

Bonita pero sin CTA → el viajero se va a GetYourGuide.

### 2) Precio / moneda confusos o ausentes

Desconfianza → no escribe.

### 3) Ads pagan a una URL que ahora es 404

Lizet quema plata. Prioridad **máxima** en el mapa 301.

### 4) Idioma equivocado en la landing

Misma lógica que hreflang: lead no calificado.

### 5) Form/WA sin UTM (menos visible)

No “mata” el lead, pero **mata tu capacidad de demostrar** que el orgánico/ads funcionan → peor para jefatura.

### 6) Site lento (CWV)

En móvil, abandono. Twig limpio ayuda; no es el único factor.

---

## Parte C — Ritual anti-muerte (tu checklist corto)

### Antes del cutover

1. Export GSC (páginas + clics) con fecha.  
2. Lista top 50 URLs por clics + todas las landings Ads.  
3. Mapa 301 completo para esas.  
4. Staging: noindex; 10 fichas con precio + WA + schema.  
5. Lizet valida destinos ads en staging (si apunta a prod paths, simular).

### Día D

1. Redirects ON.  
2. Abrir 10 URLs críticas en el celular.  
3. Enviar sitemap a GSC.  
4. Anotar hora del corte.

### Día +1 a +7

1. Buscar 404 (GSC, logs, crawler).  
2. Comparar clics de top URLs vs baseline (tendencia, no histérico día 1).  
3. Informe de 1 página a Clever / jefe mkt.

---

## Parte D — Qué decir en la mesa de 5

> “El riesgo número uno de esta migración no es Drupal en sí: es mover URLs sin 301, indexar staging, o dejar landings de Ads rotas. Yo propongo dueño de mapa de URLs + baseline Search Console + checklist de ficha (precio, WhatsApp, idioma) antes del corte.”

Si alguien dice “después vemos los redirects”:

> “Si los redirects van después, Google y Ads fallan el día D. Mejor mapa listo antes; el corte solo enciende lo ya probado.”
