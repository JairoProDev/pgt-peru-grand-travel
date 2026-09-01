# CRM en PGT y Vectorify — briefing 28 ago 2026

**Qué es esto:** mapa de lo verificable sobre cómo PGT cierra hoy, qué implica “hacer nuestro CRM”, y cómo no mezclar eso con Vectorify.

**Qué no es:** un sí a construirlo. Drupal sigue siendo el foco del mes 1. Este documento existe para que, si Clever lo vuelve a mencionar, tengas criterio y no voluntariado.

**Fuentes:** `MAPA-HERRAMIENTAS.md`, `INVENTARIO-SISTEMAS.md`, `DRIVE-INVENTARIO.md`, `MODELO-NEGOCIO.md`, `CLEVER-PONCE.md`, `TITULO-DEL-PUESTO.md`, `STACK-IDEAL.md`, insights públicos 09 ago, Excel Accesos (solo nombres de tools, 25 ago). Nada de esto es una entrevista a ventas: varias piezas **aún no las abriste**.

Canvas al lado del chat: `crm-pgt-vectorify.canvas.tsx` en el directorio de canvases del workspace.

---

## 1. Veredicto (solo lo que se puede afirmar)

1. **No hay un CRM vivo como sistema de verdad.** Hay un *Frankenstein*: WhatsApp (checkout real) + formularios WP + hoja “seguimiento leads DAI / PALOMA” + RD Station (cuenta existe) + Mailchimp + tawk.to + WeTravel + OTAs. La carpeta Drive de RD Station está bajo **trabajo de Josimar** (extrabajador). Pregunta abierta desde el día 1: si RD Station lo usa alguien o está instalado y olvidado.
2. **Clever no te pidió (aún) que lo construyas.** Lo mencionó dos veces. Eso puede ser: frustración de dueño, idea de IKIMEI TECH, deseo de dejar de pagar SaaS, o confusión CMS/CRM. Hasta que no sepas *en qué frase y con quién*, no te ofrezcas.
3. **El producto que imaginan suele ser cinco productos.** Inbox, CRM de contactos, cotizador, motor de reservas, ops (tren/cupos). Quien promete “el CRM” sin separar eso se quema.
4. **Tú puedes ser el más capacitado para *entenderlo y diseñarlo*.** No eres, en agosto 2026, el más capacitado para *entregarlo solo* mientras eres SEO del cutover Drupal y apuntas a jefatura ~25 sep.
5. **Vectorify y el CRM de PGT son empresas distintas.** El primero es plataforma para cualquier empresa. El segundo es un operador de turismo con WhatsApp como POS. Usar PGT como primer cliente de Vectorify, sin contrato, es conflicto de interés y riesgo de IP.

---

## 2. Qué usan hoy

### Verificado (en Excel Accesos, Drive, o wp-admin)

| Pieza | Qué es en la práctica | Oficio |
|---|---|---|
| **WhatsApp** + plugin Click to Chat | Checkout. El viajero escribe; ventas cotiza y cierra. | Ventas |
| **Contact Form 7** | Formularios en las webs | Mkt / web |
| **tawk.to** | Chat en sitio | Atención |
| **RD Station** | CRM + automatización (fuerte en BR / LGPD). Carpeta Drive en trabajos de Josimar. Checklist tuya: aún **sin ojear**. | ¿Ventas o mkt? **No confirmado** |
| **Mailchimp** | Email masivo. Puede solaparse con RD Station. | Mkt |
| **Plantilla seguimiento leads DAI / PALOMA** | Excel/Sheet. Si esto está activo, *eso* es el CRM de verdad. DAI ≈ Daidys (sales); Paloma = customer service. | Ventas / CS |
| **WeTravel** | Pagos / grupos (`ventas@`) | Ventas |
| **`/payments/`** en perugrandtravel.com | Pago web EN | Ventas |
| **PixelYourSite** | Tags Meta/GA en WP | Ads / mkt |
| **GA4** | Tráfico. Ads EN **sin vincular** a GA4 (visto 26 ago). No hay evento WA documentado. | Mkt |
| **Twilio / Sonetel / MyTelfon** | Voz/SMS. No sabemos si se usan. | ¿Ventas? |
| **OTAs** | GYG, Viator, TourRadar — otro “CRM” por portal | Josimar1@ / marketing@ |
| **Peru Rail, TuBoleto, Camino Inca (negtu)** | Ops, no CRM | Reservas (Bertha) |
| **Correos** | `ventas@` / `vendas@` / `atendimento@` | Ventas EN/PT |

### No verificado (no lo trates como hecho)

- Si RD Station tiene pipeline, scoring, o solo un form colgado.
- Si Mailchimp está vivo o es lista zombie.
- Cuántos números de WhatsApp hay y si hay cola por idioma.
- Si Tourmaster cobra o solo ficha + WA (`STACK-IDEAL.md` pregunta 4).
- Mix real web / WA / GYG.
- Si Clever piensa el CRM en **PGT**, en **IKIMEI**, o “cuando acabemos Drupal”.

### El flujo que sí es el negocio

```
Demanda (Google, IA, Meta, OTAs, referidos)
        ↓
Idioma correcto + ficha
        ↓
WhatsApp / form / OTA
        ↓
Ventas cotiza y cierra          ← aquí no hay sistema de verdad
        ↓
Ops: tren, entradas, guía, bus
        ↓
Experiencia → reseña
```

Un CRM bueno vive en la línea “ventas cotiza”. Un CRM *excelente* en turismo también habla con ops y con atribución (para que SEO/ads no reporten vanidad). Eso ya no es un CRM: es el **sistema operativo del operador**.

---

## 3. Las cinco cosas que la gente llama “CRM”

Cuando Clever dice “nuestro CRM”, puede estar pidiendo cualquiera. **Separarlas es tu valor.**

| # | Nombre honesto | Qué resuelve | Quién lo sufre hoy | ¿Custom? |
|---|---|---|---|---|
| 1 | **Inbox** | Un lugar para WA + IG + FB + tawk + forms, por idioma | Paloma, Ubaldina, asesores | Casi nunca. Chatwoot, WA Business, Kommo |
| 2 | **CRM (contactos + pipeline)** | Quién es el viajero, en qué etapa, quién lo atiende, que no se pierda | DAI / Paloma en Sheet | A veces. Pipedrive, HubSpot, RD Station, Attio |
| 3 | **Cotizador** | PDF/WA con tour, fechas, pax, precio por mercado | Ventas (copia/pega) | A menudo sí, porque el catálogo es de ellos |
| 4 | **Booking / pagos** | Seña, saldo, WeTravel, `/payments/` | Ventas + contabilidad | Peligroso reinventar. WeTravel, Stripe, Culqi |
| 5 | **Ops / reservas** | Cupos Inca, tren, hoteles | Bertha | **No es CRM.** Es otro producto |

El error clásico del fundador: pedir 1–5 en un solo “CRM propio” porque RD Station “no se adapta” y el Excel duele.

**Cómo hablarlo:**

> Lo que duele no es “no tener CRM”. Es que el viajero escribe al WhatsApp y la memoria queda en el celular del asesor. Podemos ordenar el inbox y el seguimiento en semanas con herramientas que ya existen. Un sistema propio tiene sentido cuando ya sabemos el proceso y lo que no cubre ninguna tool. Drupal y el CRM no son el mismo proyecto.

---

## 4. Requisitos reales de un CRM para *esta* agencia

No los inventes en una demo. Valídalos sentándote con ventas. Esta lista es la hipótesis a partir del modelo PGT, no un backlog prometido.

### Must have (si no están, ventas no lo usa)

- **WhatsApp como superficie principal**, no un módulo. El asesor no va a abrir “el CRM” y el chat aparte.
- **Idioma del viajero** (EN/ES/PT/IT) y **cola o plantillas** por idioma. Ficha PT + primer mensaje en castellano mata el lead.
- **Ficha de conversación:** país, fechas, pax, tour de interés, presupuesto, origen (dominio / UTM / ads / referido).
- **Dueño del lead** (asesor) y **que no se duplique** entre Paloma y ventas.
- **Etapas que coincidan con ellos**, no con Salesforce: p.ej. nuevo → cotizado → seña → confirmado → viajado → reseña. *Confirmar nombres reales con ellos.*
- **Catálogo de tours** (aunque sea lista) para no escribir el nombre mal.
- **Móvil.** Cierran en el teléfono.
- **Que no pidan doble carga.** Si hay que copiar el chat al CRM, el CRM muere en 14 días.

### Should have (jefe de mkt / Clever)

- UTM hasta el chat (orgánico vs Meta vs Google vs ficha).
- Tiempo de primera respuesta (contra Instant Booking de GYG).
- Motivo de pérdida (precio, fecha, OTA, no responde).
- LGPD (Brasil) + datos de pasaporte/fecha de viaje con cuidado.
- Vista para Clever: conversaciones y cierre por mercado, no “sesiones”.

### No en v1

- Motor de cupos Camino Inca.
- Reemplazar WeTravel.
- App del guía.
- IA que cotiza sola sin humano.
- Multi-empresa (eso es Vectorify, no PGT).

### Implicaciones que hay que decir en voz alta

| Tema | Implicación |
|---|---|
| **Adopción** | El CRM lo mata ventas, no el código. Si Paloma sigue el Excel, el Excel gana. |
| **WhatsApp API** | Cloud API de Meta: Business Manager, número verificado, plantillas preaprobadas, política de 24 h, coste por conversación. No es el plugin Click to Chat. |
| **Datos en celulares** | Migrar historial es feo; a menudo se empieza en “leads nuevos”. |
| **Comisiones** | Si el sueldo de ventas es variable, el CRM toca dinero. Resistencia. |
| **Temporada** | No roll out jun–ago. |
| **Drupal en paralelo** | Dos transformaciones digitales a la vez = ninguna termina. |
| **Si te vas** | Custom huérfano. Igual que el CMS custom (`CMS-CUSTOM-VIABILIDAD.md`). |
| **IKIMEI** | Segunda empresa *tech* de Clever. Si el CRM es “su juguete”, competir por construirlo es error de poder (`TITULO-DEL-PUESTO.md`). |
| **Tu rol** | SEO/GEO → jefatura mkt. Construirlo tú solo te convierte en único developer y te saca del norte (leads + marca + cutover). |

---

## 5. Tres caminos (PGT)

### A — Mapa + comprar (recomendado ahora)

2–4 semanas: ojear RD Station, sentarte con Paloma/un asesor, dibujar el proceso real, memo de 2 páginas *comprar vs construir vs ordenar lo que hay*.

- **A favor:** encaja con jefatura 25 sep; no pisa a Ricardo ni a Drupal; te vuelve la persona que *entiende el cierre*.
- **En contra:** no hay “app” que mostrar. Clever a veces solo se enamora de demos.
- **Stack típico si compran:** inbox (Chatwoot o WA Business) + CRM ligero WhatsApp-first (Kommo, HubSpot con inbox, o RD Station bien configurado) + UTM en wa.me.

### B — Integrar, no autoría (si insisten en “hacer algo”)

No escribís un CRM. Pegás piezas: **Chatwoot** (inbox) + CRM (Kommo/Pipedrive/Twenty) + **n8n** + Cloud API. Cotizador = plantillas + catálogo en Sheet/DB.

- **A favor:** semanas, no meses; vendible internamente; aprendes el dominio para Vectorify sin robar código de PGT.
- **En contra:** Clever puede decir “eso no es *nuestro*”; hay licencias; sigue haciendo falta dueño de proceso.

### C — Sistema propio (solo con presupuesto, alcance y que no seas el único dev)

Next.js + Postgres + Cloud API + autenticación + roles. 6–18 meses a tiempo parcial; 3–6 con otro dev. Compite con Drupal por tu tiempo.

- **A favor:** control, catálogo PGT, historia para Vectorify.
- **En contra:** cementerio de “CRM de la agencia”. Política (IKIMEI, sistemas). Oportunidad de la revisión de sueldo.

**Recomendación:** A ahora. B si Clever asigna presupuesto y un dueño de ventas. C no en 2026 salvo que lo fondeen como proyecto *aparte* del puesto SEO.

---

## 6. Cómo se ve “realmente bueno” (no un Salesforce feo)

Los CRM que ventas usa tienen una regla: **el trabajo diario no cambia; la memoria sí**.

1. **El chat es la UI.** El CRM se actualiza desde el hilo (humano o extracción asistida). Nadie “entra al CRM a trabajar”.
2. **Una verdad.** Un viajero, un dueño, un idioma. Paloma no reasigna a ciegas.
3. **Velocidad contra la OTA.** SLA de primera respuesta. Eso es margen, no vanidad.
4. **Idioma y mercado como campos de primer nivel**, no etiquetas opcionales.
5. **Origen del lead.** Sin esto, SEO y Lizet no pueden defender presupuesto. Es tu palanca de jefatura, no un extra.
6. **Handoff a ops explícito.** “Cerrado” ≠ “ya compramos el tren”.
7. **Clever ve una página:** conversaciones, cierre, mercado, tiempo de respuesta. No 40 dashboards.
8. **Empieza en un idioma y un equipo.** PT + un asesor. No cuatro dominios el día 1.

Eso es producto. El stack es secundario.

### Tecnologías (si algún día hay C)

| Capa | Opciones serias | Evitar |
|---|---|---|
| Inbox | Chatwoot, WA Cloud API directa | Otro plugin WP de chat |
| CRM base | Twenty (OSS), Attio, Espo, o modelo propio estrecho | Clonar HubSpot |
| App | TypeScript, Next.js, Postgres | PHP a mano “porque WP” |
| Automatización | n8n (self-host) o jobs en el backend | Zapier eterno sin dueño |
| Auth | Un login (Google Workspace de PGT) | Usuarios a mano |
| Hosting | VPS Ubuntu que ya van a tener + backups, o Cloud con costo claro | “Lo subo yo en mi laptop” |

No hace falta decidir stack hasta que el proceso esté dibujado. Decidir Next vs Laravel ahora es evasión.

---

## 7. Política — cómo no perder la jefatura

| Movida | Lectura en la oficina |
|---|---|
| “Yo se los armo en un mes” | Amenaza a sistemas + promesa impagable + te sales de SEO |
| “Es fácil, es un CRUD” | No has visto a ventas |
| Ofrecerlo en el plan SEO de esta semana | Mezclas oficios; Einel/Ricardo se tensan |
| Sentarte con Paloma “para entender cómo no se pierde el brasileño” | Oficio de cierre; norte de Clever |
| Memo comprar vs construir después de mapear | Jefe |
| Mencionar IKIMEI o Vectorify en la mesa | Fuera de lugar (`CLEVER-PONCE.md`) |

**Frase si lo vuelve a sacar:**

> Me interesa porque hoy el lead se cae entre la web y el chat. Antes de construir nada, necesito ver cómo cotizan Paloma y ventas un día normal, y si RD Station todavía vive. En dos semanas les digo qué se puede ordenar sin parar Drupal, y qué sí pediría sistema propio.

Luego **cúmplelo**. No improvises demo.

---

## 8. Vectorify — otro producto

En este repo **no hay código ni spec de Vectorify**. No aparece en el disco de trabajo PGT. Hay un [vectorify.ai](https://vectorify.ai/) ajeno (conector AI para Laravel). El tuyo, aquí, es tesis.

### Lo que describiste

CRM para cualquier empresa, personalizable al máximo, construible sin saber tecnología, que se adapte al contexto.

Eso no es un CRM. Es **una plataforma para generar CRMs** (Airtable + Salesforce + un analista funcional, reemplazados por software). El cementerio está lleno: “no-code CRM”, “Salesforce para pymes”, “Airtable con pipeline”.

### Por qué es tan difícil

| Promesa | Dificultad real |
|---|---|
| Cualquier empresa | Cada vertical tiene objetos distintos (tour vs póliza vs lote). El 80 % del valor está en el modelo, no en el kanban. |
| Sin saber tecnología | El usuario *sí* tiene que saber su proceso. Si no lo tiene, la tool no lo inventa bien. La IA puede *entrevistar* y proponer esquema; no puede adivinar comisiones. |
| Personalizable al máximo | Personalización infinita = Salesforce: poderosa e inusable. Hay que acotar. |
| Se adapta al contexto | El moat 2026–27: **entrevista → esquema → CRM**, no más campos custom. |

### Tres formas de Vectorify

1. **Horizontal (schema engine).** “Descríbeme cómo vendes” → objetos, etapas, campos, permisos. Muy grande. Competidores: Attio, Notion, Airtable, Fillout, emergentes AI-CRM.
2. **Vertical (recomendado como cuña).** Operadores de turismo LatAm, WhatsApp-first, multi-idioma, cotización + inbox. PGT te enseña el dominio. El producto no lleva datos de PGT.
3. **Plantillas + IA.** No “cualquier CRM desde cero”: 5 verticales (turismo, clínica, inmobiliaria, academia, ferretería) + un motor de campos. Lo que Salesforce hizo con Industry Cloud, más chico.

**Recomendación Vectorify:** motor genérico de esquema (2) *por dentro*, cuña turismo WhatsApp *por fuera*. No empieces por el constructor universal.

### Qué sería “bueno” en Vectorify (producto)

- Onboarding = conversación (y/o importar el Excel que ya usan — en PGT eso sería la plantilla DAI/Paloma).
- WhatsApp Cloud API como primer canal, no email.
- Multi-tenant de verdad (datos de empresa A no existen para B).
- Permisos por rol (dueño, asesor, mkt, solo lectura).
- Exportar (o te odian cuando se quieren ir).
- Local: español, PT-BR, LGPD, precios en PEN/USD/BRL.
- El “sin código” es **cambiar etapas y campos**, no un IDE.

### Stack razonable (cuando construyas Vectorify, no PGT)

- App: TypeScript + Postgres + RLS por tenant.
- Inbox: Cloud API; no dependas de un solo BSP sin plan B.
- AI: extrae entidades del chat y propone el esquema inicial; el humano confirma.
- No reinventes billing, auth, email transaccional.

### PGT vs Vectorify — muro ético

| OK | No OK |
|---|---|
| Aprender cómo cotiza un operador | Copiar plantillas, precios, listas de clientes |
| Anotar *tipos* de etapa (cotizado, seña) | Subir el Sheet de Paloma a tu SaaS |
| Inbox de prueba con datos dummy | Usar números WA de PGT en tu producto |
| Ofrecer Vectorify a PGT *después*, con contrato y precio | “Mientras tanto lo hago yo y ya queda en mi startup” |

Si algún día PGT es cliente de Vectorify: contrato, quién es dueño del código, qué pasa si te vas. No lo mezcles con el sueldo de SEO.

---

## 9. Qué tienes que empaparte (orden)

No es un bootcamp de Next. Es **dominio + proceso + una tool de inbox**.

### Semana (encajar en huecos, no parar Drupal/GSC)

1. Abrir **RD Station** y **Mailchimp**. ¿Login? ¿últimos envíos? ¿forms de las webs conectados? Anotar en `HECHOS.md`.
2. Abrir la **plantilla DAI/Paloma**. Columnas = el modelo de datos real.
3. Pedir a un asesor **15 minutos**: “cuando llega un brasileño por WhatsApp, ¿qué haces hasta la seña?”. No grabes sin permiso; dibuja el flujo a mano.
4. Contar **números WA** y si hay split PT/EN.
5. Ver **WeTravel** por encima (qué entra ahí vs `/payments/`).

### Conceptos a estudiar (noches, Vectorify)

- Pipeline, etapa, actividad, SLA, scoring — vocabulario, no certifícate.
- **WhatsApp Cloud API:** ventana 24 h, plantillas, BSP vs API directa, WABA.
- LGPD básico (Brasil es el mercado caliente).
- Chatwoot o Kommo: una cuenta demo, no código.
- Diferencia CRM vs ESP (Mailchimp) vs CDP vs booking engine.
- Twenty CRM o Attio: qué es “flexible” de verdad.

### Lo que no estudies aún

- Microservicios, Kafka, “arquitectura Salesforce”.
- Motor de reservas (Bokun, Rezdy) salvo para saber que *existen* y no reinventarlos.
- Drupal Commerce como CRM. No lo es.

---

## 10. Preguntas que faltan (no las dispares todas)

A **ventas / Paloma** (una, cuando haya confianza):

> Cuando te escribe alguien del sitio, ¿dónde queda anotado para que no se pierda si tú no estás?

A **Clever**, solo si él lo saca:

> Cuando dices CRM, ¿es el WhatsApp ordenado, o también cotizar y cobrar? Lo pregunto porque son tiempos distintos.

A **ti**, antes de mezclar Vectorify:

> ¿Vectorify es el producto que quieres construir los próximos 2 años, o es el nombre que le pones a “sistemas a medida”?

---

## 11. Relación con el resto del repo

- Norte leads: `MODELO-NEGOCIO.md`, `STACK-IDEAL.md`
- No colgarte “tech”: `TITULO-DEL-PUESTO.md`
- CMS custom ≠ CRM: `mi-carrera/CMS-CUSTOM-VIABILIDAD.md`
- WA como POS: `conocimiento/articulos-jairosaul/turismo/whatsapp-es-el-checkout.mdx`
- Tools: `MAPA-HERRAMIENTAS.md` (RD Station sigue sin ojear)

**No entra en el plan SEO de esta semana** (`PLAN-SEO-PARA-CLEVER-BORRADOR.md`). Si acaso, una línea interna: “mapear destino del lead (WA / form / RD) para atribución”. Eso sí es marketing. Construir CRM no.
