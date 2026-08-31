# MVP / POC — accesos, certezas y TODO (Jairo + agente)

Actualizado: 28 ago 2026.

**Estado POC:** scaffold Next.js en `pgt/pgt-poc/` — build OK. Pendiente: push GitHub + deploy Vercel (`pgt-poc/DEPLOY.md`).

## ¿Qué es POC?

**POC** = *Proof of Concept* (prueba de concepto).

No es el sitio final. Es un **experimento pequeño** para demostrar que la nueva arquitectura funciona mejor **antes** de migrar todo.

**Por qué POC y no “proyecto completo”:**

- Menos riesgo político (no cancelas Drupal en voz alta)
- Menos riesgo SEO (1–2 URLs, no 600)
- Resultados medibles en 2–4 semanas
- Si falla, pierdes poco tiempo

**MVP del POC:** 1 blog + 1 tour EN en `poc.perugrandtravel.com` → luego 1 URL en producción (misma slug).

---

## ¿Deberías probar? **Sí**

Condiciones:

1. Avisar a **Einer o Ricardo** (1 frase, no drama): *“Quiero un subdominio de prueba para comparar velocidad y SEO en 2 páginas.”*
2. **Staging primero** (`poc.` o `demo.`) — no tocar producción sin OK.
3. No anunciar “tiro Drupal” — anunciar “prueba con datos”.

---

## Accesos: ¿tienes todo?

| Necesitas | ¿Lo tienes? | Para qué |
|---|---|---|
| marketing@ (GSC, GA4, Drive) | **Sí** | Baseline, medir después |
| wp-admin perugrandtravel.com | **Probable sí** (Excel) | Copiar contenido tour/blog |
| Repo local `/pgt` + tu laptop | **Sí** | Código y docs |
| Cuenta GitHub/Git (personal o empresa) | **Sí** | Deploy Vercel — push pendiente |
| DNS subdominio `poc.` | **No confirmado** | Staging público — pedir Ricardo |
| cPanel/FTP EN | **Preguntar Ricardo** | Assets reales wp-admin |
| clever@ / DNS raíz | **No** (y no pedir aún) | Solo si routing en prod |
| Vercel / Railway / CF | **Sí** | Import repo → deploy |
| Aprobación escrita POC | **Falta** | Einer/Clever 1 OK |

**Conclusión:** puedes **empezar a construir en local y en tu Vercel personal** hoy. Para **staging con dominio PGT** y **swap de 1 URL prod** necesitas 2–3 accesos más + un “sí” del jefe.

---

## De qué estamos seguros

- Bloque tuyo: tours 3 + blogs 4 (EN).
- GSC EN 28d: 643 clics, 116k imp, CTR 0,6%.
- Blog P0: Things Machu Picchu — ~6k imp, pos ~6, 1 clic → oportunidad CTR.
- Tour enlace: Salkantay 5d en tu bloque.
- WP hoy = Tourmaster + Yoast + muchos plugins.
- Migración Drupal decidida pero **no** imposible reconsiderar con **datos**.
- Einer = jefe mkt mañanas; Ricardo = accesos técnicos.

## Qué nos falta

- [ ] OK verbal/escrito para POC staging
- [ ] Subdominio `poc.perugrandtravel.com` (DNS)
- [ ] Confirmar wp-admin EN (usuario en Excel)
- [ ] Export GSC completo (CSV/Sheets) — tú 1 clic EXPORTAR
- [ ] Texto/imágenes actuales de las 2 URLs (scrape o wp-admin)
- [ ] ¿Quién aprueba cambiar 1 URL en producción?
- [ ] GTM/pixel IDs para paridad tracking (Lizet/Ricardo)

---

## TODO — Jairo (tú)

### Esta semana (obligatorio)

- [ ] Mensaje WhatsApp **Ricardo** (copiar abajo)
- [ ] Mensaje corto **Einer** si está: permiso POC 2 páginas
- [ ] GSC → EXPORTAR → guardar en `03-seo/datos/`
- [ ] Abrir en wp-admin: blog Things Machu Picchu + tour Salkantay 5d → capturas o export
- [ ] Crear cuenta **Vercel** (si no tienes) con GitHub
- [ ] Crear repo `pgt-poc` (privado) en tu GitHub

### Semana 2

- [ ] Pedir DNS `poc.perugrandtravel.com` → Vercel (cuando Ricardo responda)
- [ ] Demo interna 15 min (Lighthouse antes/después)
- [ ] Anotar baseline URL en HECHOS (clics/imp hoy)

### No hacer sin OK

- [ ] Cambiar URL en producción
- [ ] Pedir clever@ / DNS raíz
- [ ] Publicar “cancelamos Drupal”

### Mensaje modelo Ricardo

> Ricardo, para el plan SEO quiero un subdominio de prueba `poc.perugrandtravel.com` (2 páginas: 1 blog + 1 tour) para comparar velocidad y snippet sin tocar el sitio vivo. ¿Me ayudas con el DNS o prefieren otro subdominio? También aviso: creé linux_admin en OMV para montar Marketing en mi laptop — ¿está bien o usamos otro usuario?

---

## TODO — Agente (yo)

- [ ] Spec técnico MVP (`MVP-POC-STACK.md`) — stack, páginas, métricas
- [ ] Scaffold proyecto Next/Astro + estructura contenido
- [ ] Checklist SEO por página (schema, meta, WA, canonical)
- [ ] Script o guía: extraer contenido WP de las 2 URLs
- [ ] Tabla comparación Lighthouse (plantilla)
- [ ] Borrador 1 página para Clever/Einer (“prueba de concepto, no reemplazo aún”)
- [ ] Actualizar HECHOS/DUDAS cuando completes accesos
- [ ] Revisar tu browser (GSC, wp-admin) si dejas sesión abierta

---

## Orden de trabajo (resumen)

```
Día 1–2:  mensajes + export GSC + wp-admin capturas
Día 3–7:  código POC local (agente + tú)
Día 8–10: deploy Vercel (*.vercel.app) — sin DNS aún
Día 11–14: DNS poc. + demo equipo
Mes 2:    si OK → 1 URL producción misma slug
```
