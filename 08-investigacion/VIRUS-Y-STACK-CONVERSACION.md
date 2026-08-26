# Virus, spam y stack — conversación con el equipo

**Para:** Jairo · preparación de reunión (no leer en voz alta entero)  
**Norte de Clever:** más **qualified leads** + **fortalecer la marca**  
**Actualizado:** 26 ago 2026

---

## 1. El incidente (qué significa de verdad)

Dijeron: entró “virus”, hubo páginas spam, reclamaron al hosting (Banahosting / Core), y el hosting dijo **culpa del equipo**.

Eso es **plausible y frecuente** en WordPress. No implica que “WordPress sea basura”. Implica que **alguien instaló o no auditó código de riesgo**.

### Causas típicas (orden de probabilidad en agencias de turismo en LatAm)

| Causa | Qué pasa | Encaje con “el hosting dice que es culpa de ustedes” |
|---|---|---|
| **Plugins/temas nulled (piratas)** | El ZIP trae backdoor. Al activar, inyecta spam SEO (pharma, casino) que **solo ve Googlebot**. El dueño no ve nada en el navegador. | Sí: el malware llega por archivo subido por el equipo, no por fallo del servidor |
| **Plugin abandonado / desactualizado** | Exploit conocido → inyección | Sí, parcialmente (mantenimiento) |
| **Credenciales compartidas** | `marketing@` en todas las PCs, Excel con claves en claro, misma sesión Chrome | Sí: vector humano |
| **Supply chain oficial** | Plugin legítimo comprometido en update (casos 2025–2026 documentados) | Hosting también puede decir “su app”, aunque no sea nulled |
| **Fallo del hosting** | Aislamiento débil, vecinos en shared | Menos frecuente; ellos casi nunca lo admiten |

**Plugins nulled = vector clásico.** Campañas tipo WP-VCD: el webmaster infecta su propio sitio al instalar “premium gratis”. El malware se copia a temas, `wp-includes`, BD; **borrar el plugin no limpia**. Spam SEO → Google degrada o lista negra → **mata leads y marca**.

Tu sospecha (plugins no oficiales) es **hipótesis #1 sólida**. Hay que **verificar** con Ricardo, no acusar en reunión.

### Qué preguntar (sin culpar)

1. ¿Qué páginas spam eran? ¿URLs? ¿`site:perugrandtravel.com` mostraba pharma/casino?
2. ¿Quién instaló plugins en los últimos 6–12 meses? ¿Hay lista de plugins activos?
3. ¿Algún tema/plugin “premium” sin licencia / descargado de sitios raros?
4. ¿Se limpió solo (Wordfence/Sucuri) o formatearon y reinstalaron?
5. ¿Quedó malware en `wp-config.php` / usuarios admin desconocidos?
6. ¿Google Search Console mostró “Hackeo” / seguridad?

Si no hay respuesta clara → **riesgo activo** aunque “ya no se vea spam”.

---

## 2. ¿Código propio es “más seguro”?

**A medias.**

| Afirmación | Verdad |
|---|---|
| “Con código propio no hay virus de plugins” | **Cierto en parte:** eliminas el vector #1 (nulled WP). |
| “Código propio = seguro automáticamente” | **Falso.** Auth débil, secretos en repo, dependencias npm vulnerables, panel admin sin 2FA, S3 abierto = mismo drama. |
| “Drupal no se hackea” | **Falso.** Menos superficie de plugins basura; más curva; si mal configurado, igual. |
| “WordPress oficial + licencias + WAF + updates = suficiente para muchos” | **Cierto** para miles de operadores turismo. El problema de PGT no es “usar WP”; es **higiene + arquitectura multi-sitio**. |

**Seguridad = proceso, no marca de CMS:**

- Solo código con licencia / fuente conocida  
- Menos plugins (cada uno = superficie)  
- Updates + backups + WAF (Cloudflare / Sucuri)  
- Usuarios con roles; **no** Excel de contraseñas compartido  
- Staging ≠ producción  
- Monitoreo `site:dominio` y GSC seguridad  

Código propio **bien hecho** reduce superficie. Código propio **a prisa sin ops** es otro vector.

---

## 3. ¿Qué le conviene al **negocio** (no a tu ego de stack)?

Clever midió: **leads calificados** + **marca**.

| Lo que mueve leads | ¿Lo resuelve cambiar CMS? |
|---|---|
| Ficha rápida, precio claro, CTA WhatsApp, idioma correcto | Parcial (plantilla), no “Drupal” |
| Catálogo unificado (un tour = 4 idiomas) | **Sí arquitectura**; WP×4 o Drupal o headless |
| Ads + orgánico aterrizan en URL correcta + UTM | No |
| Confianza (reseñas, E-E-A-T, sin spam en Google) | **Sí higiene seguridad** |
| Velocidad (CWV) | Tema/constructor; headless ayuda |
| Tablas keywords estables | Migración **las empeora** 4–8 semanas |

**Diagnóstico PGT (verificable):**

1. **Seguridad / reputación** — virus spam = amenaza directa a marca y rankings.  
2. **Arquitectura** — 4+ WordPress + Tourmaster + Goodlayers + blogs satélite.  
3. **Medición** — clics ≠ WhatsApp; blogs con CTR ~0% en top 10.  
4. **Migración Drupal** — posible solución a (2), **no** a (3); riesgo SEO alto; Tourmaster no migra solo.  
5. **Código puro sin admin** — te convierte en cuello de botella de precios y copy.

### Lo ideal para PGT (orden de negocio)

```
A. Higiene ahora (esta semana–mes)
   → inventariar plugins, eliminar nulled, limpiar residual, WAF, 2FA, menos usuarios admin

B. Leads 90 días (WordPress vivo)
   → mismas URLs, CWV/plantilla, schema, hreflang, CTR blogs, UTMs → WhatsApp

C. Arquitectura 6–18 meses (una decisión, no tres)
   → Un catálogo + admin para no-devs + front rápido + URLs congeladas
```

**Candidatos serios para C:**

| Opción | Seguridad | Velocidad tuyas | Admin equipo | Riesgo keywords | Encaje Cusco |
|---|---|---|---|---|---|
| WP limpio + tema hijo custom + plugins licenciados | Buena si higiene | Alta | Ya lo saben | Bajo | ★★★★★ |
| Drupal 11 + vendor | Buena | Baja (tú) | Curva | Alto cutover | ★★ si hay agencia |
| **Next + Payload/Sanity** | Excelente si ops | Muy alta (tú+Cursor) | Hay que diseñarlo | Alto cutover | ★★★★ si tú te quedas |
| HTML a mano / sin CMS | Mala ops | Alta al inicio | **Mata el negocio** | Alto | ★ |

**Recomendación firme:**

- **No** propongas “tiramos WordPress mañana y lo rehago yo en Cursor”.  
- **Sí** propón: *higiene + medición + arquitectura en fases*, y que el techo técnico sea **front en código + CMS headless con admin**, no “páginas sueltas”.  
- Si Drupal ya tiene **contrato y pago**, no pelees el CMS: pelea **SEO del cutover + no usar nulled + un catálogo**.

---

## 4. El mito “con Cursor hago en días lo de meses”

| Lo que Cursor acelera | Lo que **no** acelera |
|---|---|
| UI de una ficha tour, schema, layout Figma | Migrar 70 tours × 4 idiomas + metadatos Tourmaster |
| CRUD admin básico con Payload | Roles, permisos, preview, media library, backups |
| Landing de ads | 301 de ~600 URLs + vigilancia GSC 60 días |
| Scripts SEO / hreflang | Confianza del equipo, capacitación CM, Ricardo |
| Prototipo staging en 1–2 semanas | Producción multi-dominio sin downtime ni spam |

**Frase honesta (úsalá):**

> Con IA puedo prototipar el front y el admin en semanas. Lo que no se comprime es: migrar contenido bien, no romper rankings, y que Lizet cambie un precio sin mí. Si saltamos eso, el “rápido” se vuelve lento en ventas.

Si dices “en días tengo el sitio nuevo”, el equipo te oirá como **amenaza o ingenuo**. Si dices “en 2 semanas staging de 1 tour + admin; en 3–4 meses cutover con mapa 301”, te oirán como **alguien que ha hecho cutovers**.

---

## 5. Argumentos reales a favor de código propio (cuándo sí)

Úsalos **solo** si ya hay higiene WP y un win SEO, o si preguntan “¿y si no Drupal?”.

1. **Superficie de ataque:** menos plugins PHP aleatorios = menos vector nulled (el que probablemente los quemó).  
2. **CWV y schema:** HTML controlado > Goodlayers + 70 JS.  
3. **Un modelo Tour:** TypeScript/Payload = un tour, N idiomas; imposible “olvidar” PT.  
4. **GEO / IA:** `llms.txt`, facts extractables, APIs — más natural en app moderna.  
5. **Figma → React:** diseño modular ya existe.  
6. **Tú + IA:** velocidad de implementación real en **ese** stack (no en Drupal Twig).  
7. **Marca:** sitio limpio, rápido, sin historial de spam = confianza.

## Argumentos reales **en contra** de “código puro ya” (diéctelos tú, ganas credibilidad)

1. **Sin admin usable, marketing no publica** → leads mueren en temporada.  
2. **Cutover = dip keywords** → Clever odia eso.  
3. **Si te vas, el sitio queda huérfano** salvo documentación + contrato de mantenimiento.  
4. **Ricardo opera WP hoy** → aliarlo, no reemplazarlo en público.  
5. **Drupal puede ser decisión política/contrato** → pelear stack = pelear ego.  
6. **El virus no se cura migrando a ciegas:** se cura limpiando + higiene; migrar basura infectada o sin 301 es peor.

---

## 6. Guion de reunión (orden político)

### A. Empieza por el dolor compartido (virus + leads)

> Entiendo el tema del spam/virus. En WordPress el vector más común es plugin o tema no oficial: el hosting suele tener razón al decir que entró por la aplicación. Eso pega directo a **marca** y a Google. Antes de hablar de Drupal o de sitio nuevo, conviene inventario de plugins, limpiezas residuales y que no quede backdoor.

### B. Une a las dos agujas de Clever

> El norte es leads calificados y marca. Plataforma nueva solo ayuda si: (1) no nos banean otra vez, (2) marketing edita sin ticket, (3) no rompemos las URLs que ya rankean.

### C. Ofrece tres caminos (no uno “mío”)

| Camino | 90 días | 12 meses |
|---|---|---|
| **1. WP endurecido + tema Figma mismas URLs** | Leads ya | Base sólida |
| **2. Drupal** (si hay vendor pagado) | Casi 0 (migración) | Catálogo unificado |
| **3. Front código + CMS admin (Payload/Sanity)** | POC staging | Techo técnico + seguridad |

> Yo recomiendo **1 ahora**. **3 como visión** si quieren control y menos dependencia de plugins raros. **2 solo con agencia Drupal y mapa 301**. No recomiendo HTML sin panel: cada precio pasaría por un developer.

### D. Cómo te posicionas tú

> Puedo liderar el checklist SEO de cualquier cutover (URLs, 301, GSC, schema) y un prototipo en staging. No voy a fingir que Drupal se hace en dos sábados ni que “Cursor borra el riesgo de migración”.

### E. Lo que **no** digas

- “WordPress es una porquería / Ricardo lo hizo mal.”  
- “Yo solo, en código, en una semana.”  
- “Drupal es estúpido.”  
- “Plugins pirata” como acusación sin evidencia.  
- “Soy el jefe de tecnología” (aún no).

---

## 7. Checklist de preparación (antes de proponer algo radical)

| ☐ | Qué | Por qué |
|---|---|---|
| [ ] | Confirmar con Ricardo hechos del virus (URLs, fecha, limpieza) | Datos > opinión |
| [ ] | Lista plugins activos (export o captura) | Detectar nulled / abandonados |
| [ ] | ¿Hay licencia Goodlayers / Tourmaster / Yoast? | Presupuesto higiene |
| [ ] | ¿Drupal: vendor, cotización, fecha? | Evitar pelear fantasmas |
| [ ] | ¿Figma cambia slugs? | Dealbreaker SEO |
| [ ] | 1 win SEO visible esta semana (CTR o fix) | Autoridad antes de arquitectura |
| [ ] | POC mental: 1 tour en staging, no 4 sitios | Alcance creíble |
| [ ] | Quién edita precios hoy si no eres tú | Requisito admin |

---

## 8. Respuesta corta si te preguntan “¿qué harías tú?”

> Primero: cerrar el agujero de seguridad (plugins, limpio, WAF, accesos). Segundo: no parar leads — WordPress con diseño nuevo y **mismas URLs**. Tercero: si quieren salir del riesgo de plugins y unificar idiomas, yo apostaría a **front en código + CMS con panel para el equipo**, en fases, con mapa 301. Drupal solo si ya hay quien lo implemente de verdad. El CMS no trae leads solo; la ficha, el idioma, WhatsApp y no tener spam en Google sí.

---

## Lecturas en el repo

- `08-investigacion/STACK-IDEAL.md`  
- `mi-carrera/CMS-CUSTOM-VIABILIDAD.md`  
- `00-manana/SI-SALE-DRUPAL.md`  
- `10-aprendizaje/D03-STACK-WORDPRESS-WAF-USERAGENTS.md`  

**Veredicto final:** código propio **sí puede ser lo mejor a 12–18 meses** para PGT **si** incluye CMS admin y cutover disciplinado. **No** es lo mejor como respuesta inmediata al virus ni como propuesta día 2. El virus pide **higiene**; los leads piden **medir y optimizar WP**; la arquitectura pide **una decisión en frío con Ricardo y Clever a favor**, no una revolucionar.
