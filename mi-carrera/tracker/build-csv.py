#!/usr/bin/env python3
"""Regenerate TAREAS-MAESTRO.csv — run manually when restructuring."""
import csv
from pathlib import Path

OUT = Path(__file__).parent / "TAREAS-MAESTRO.csv"
FIELDS = [
    "id", "epica_id", "tipo", "track", "fecha_inicio", "fecha_fin", "dia_pgt",
    "categoria", "tarea", "prioridad", "estado", "fecha_entrega", "link",
    "evidencia", "metrica", "notas",
]
rows: list[dict] = []


def add(**kw):
    rows.append({k: kw.get(k, "") for k in FIELDS})


# ═══════════════════════════════════════════════════════════════
# TRACK: drupal — 1 épica + subtareas
# ═══════════════════════════════════════════════════════════════
add(
    id="EPIC-DRUPAL", epica_id="EPIC-DRUPAL", tipo="epica", track="drupal",
    fecha_inicio="2026-09-01", dia_pgt="D6", categoria="migración",
    tarea="Migrar 18 tours bloque 3 WP → Drupal staging (paridad SEO)",
    prioridad="P0", estado="en_progreso", fecha_entrega="2026-09-20",
    link="03-seo/guias/MIGRACION-TOURS-DRUPAL-PASO-A-PASO.md",
    evidencia="03-seo/datos/wp-export-tours-jairo/", metrica="0/18 en Drupal",
    notas="Asignación bloque 3 — cutover global es Einel/Ricardo",
)

drupal = [
    ("D-01", "Prep: export WP 18/18 JSON+MD", "2026-09-01", "hecho", "18/18", "03-seo/datos/wp-export-tours-jairo/manifest.json", ""),
    ("D-02", "Prep: clipboard SEO title/meta", "2026-09-01", "hecho", "18 tours", "03-seo/datos/drupal-tour-seo-clipboard/TOURS-SEO-CLIPBOARD.md", ""),
    ("D-03", "Prep: drupal-paste HTML por tour", "2026-09-01", "hecho", "18 carpetas", "03-seo/datos/wp-export-tours-jairo/", ""),
    ("D-04", "Prep: guía tour piloto Salkantay", "2026-09-01", "hecho", "", "03-seo/guias/PASO-A-PASO-TOUR-01-SALKANTAY.md", ""),
    ("D-05", "Prep: CSV maestro migración", "2026-09-01", "hecho", "133 filas", "03-seo/datos/drupal-sprint-jairo-2026-09-01/jairo-migracion-maestro.csv", ""),
    ("D-06", "Prep: estimación tiempos bloque", "2026-09-01", "hecho", "~56h buffer", "03-seo/datos/estimacion-tiempos-migracion-jairo.csv", ""),
    ("D-07", "Prep: mapa formulario Product", "2026-09-01", "hecho", "4 tabs", "10-aprendizaje/drupal/12-TOUR-PRODUCT-FORM-MAPA-COMPLETO.md", ""),
    ("D-08", "Ejecutar: tour #1 Salkantay 5D", "2026-09-02", "pendiente", "0/1", "03-seo/guias/PASO-A-PASO-TOUR-01-SALKANTAY.md", "Pack listo"),
    ("D-09", "Ejecutar: tours #2–18", "", "pendiente", "0/17", "03-seo/datos/wp-export-tours-jairo/", "~35 min/tour"),
    ("D-10", "QA checklist SEO por tour", "", "pendiente", "", "03-seo/guias/MIGRACION-SEO-CAMPO-A-CAMPO.md", ""),
    ("D-11", "Bloqueo Pathauto /tour/{slug}/", "2026-09-01", "bloqueado", "", "", "Einel"),
    ("D-12", "Bloqueo JSON:API staging", "2026-09-01", "bloqueado", "", "", "Einel"),
    ("D-13", "Bloqueo WhatsApp en staging", "2026-09-01", "bloqueado", "", "", "Einel/dev"),
]
for sid, t, fd, st, met, ev, note in drupal:
    add(
        id=f"DRUPAL-{sid}", epica_id="EPIC-DRUPAL", tipo="subtarea", track="drupal",
        fecha_inicio=fd, dia_pgt="D6" if fd == "2026-09-01" else ("D7" if fd else ""),
        categoria="migración", tarea=t, prioridad="P0", estado=st, evidencia=ev,
        metrica=met, notas=note,
    )

# ═══════════════════════════════════════════════════════════════
# TRACK: codigo-web — 1 épica + subtareas (pgt-web)
# ═══════════════════════════════════════════════════════════════
add(
    id="EPIC-WEB", epica_id="EPIC-WEB", tipo="epica", track="codigo-web",
    fecha_inicio="2026-08-31", dia_pgt="D4", categoria="producto",
    tarea="Construir sitio Next.js EN (pgt-web) — reemplazo WordPress + cutover",
    prioridad="P0", estado="en_progreso", fecha_entrega="2026-09-16",
    link="https://perugrandtravel.vercel.app",
    evidencia="../pgt-web/docs/ESTADO-PROYECTO.md", metrica="591 rutas SSG",
    notas="Pista B experimento 4 · separada de migración Drupal manual",
)

web = [
    ("W-01", "Scaffold Next.js + MVP home/packages/tour/blog", "2026-08-31", "hecho", "", "../pgt-web/"),
    ("W-02", "Scrape SSG 69 tours + 452 blogs + 62 pages", "2026-08-31", "hecho", "591 rutas", "../pgt-web/src/content/"),
    ("W-03", "GTM + dataLayer whatsapp_click", "2026-08-31", "hecho", "", "../pgt-web/src/lib/analytics.ts"),
    ("W-04", "Pipeline WebP self-hosted imágenes", "2026-09-01", "hecho", "~646 img", "../pgt-web/"),
    ("W-05", "TrustBar + WA sticky + BlogLeadCTA + hubs dual CTA", "2026-09-01", "hecho", "", "../pgt-web/"),
    ("W-06", "PackageGrid + tour cards v2 conversión", "2026-09-01", "hecho", "", "../pgt-web/"),
    ("W-07", "Trip finder + búsqueda global + heroes conversión", "2026-09-01", "hecho", "", "../pgt-web/"),
    ("W-08", "Destinos dropdown + páginas región Perú", "2026-09-01", "hecho", "", "../pgt-web/"),
    ("W-09", "117 redirects blog dual URL", "2026-09-01", "hecho", "117", "../pgt-web/data/redirects.json"),
    ("W-10", "sitemap + robots + llms.txt + JSON-LD", "2026-09-01", "hecho", "", "../pgt-web/"),
    ("W-11", "Scripts parity + pre-cutover-checklist", "2026-09-01", "hecho", "30/30", "../pgt-web/scripts/pre-cutover-checklist.sh"),
    ("W-12", "Integraciones Google scripts + verify 7/7", "2026-09-01", "hecho", "7/7", "../pgt-web/docs/GUIA-CONEXION-GOOGLE.md"),
    ("W-13", "Pipeline precios OTAS merge+apply (código)", "2026-09-01", "en_progreso", "", "../pgt-web/scripts/"),
    ("W-14", "Fix duración tours + itinerarios day-tours", "2026-09-02", "hecho", "67/70 itin", "../pgt-web/"),
    ("W-15", "Preview perugrandtravel.vercel.app sin SSO", "2026-09-02", "hecho", "", "https://perugrandtravel.vercel.app"),
    ("W-16", "noindex en vercel.app + NEXT_PUBLIC_SITE_URL", "2026-09-02", "hecho", "", "../pgt-web/"),
    ("W-17", "Blueprint Fase A beta + guía DNS", "2026-09-02", "hecho", "", "../pgt-web/docs/BLUEPRINT-FASE-A-BETA-CUTOVER.md"),
    ("W-18", "Tag GTM whatsapp_click → GA4 conversión", "2026-09-02", "pendiente", "", "../pgt-web/docs/CUTOVER.md", "30 min UI"),
    ("W-19", "QA manual preview 10 puntos", "2026-09-02", "pendiente", "", "../pgt-web/docs/REPORTE-AVANCE-JAIRO.md"),
    ("W-20", "CSV tarifario 2026 + precios:apply", "", "pendiente", "", "../pgt-web/", "Validar con Ricardo"),
    ("W-21", "DNS beta beta.perugrandtravel.com", "", "pendiente", "", "../pgt-web/docs/GUIA-DNS-JAIRO.md"),
    ("W-22", "Cutover DNS prod", "", "pendiente", "", "../pgt-web/docs/BLUEPRINT-FASE-A-BETA-CUTOVER.md"),
]
for sid, t, fd, st, met, ev, *rest in web:
    note = rest[0] if rest else ""
    add(
        id=f"WEB-{sid}", epica_id="EPIC-WEB", tipo="subtarea", track="codigo-web",
        fecha_inicio=fd, categoria="producto", tarea=t, prioridad="P0", estado=st,
        evidencia=ev, metrica=met, notas=note,
    )

# ═══════════════════════════════════════════════════════════════
# TRACK: seo-operaciones — todo lo demás (pre-PGT + mes 1)
# ═══════════════════════════════════════════════════════════════

# Pre-PGT portafolio
pre = [
    ("PRE-01", "investigación", "Intel corporativa PGT (RUC RNP Camino Inca)", "2026-08-09", "hecho", "archivo-original/empleo-seo/01-INSIGHTS-Peru-Grand-Travel.md"),
    ("PRE-02", "auditoría", "Crawl HTTP 4 dominios EN/ES/PT/IT", "2026-08-09", "hecho", "archivo-original/empleo-seo/02-AUDITORIA-SEO-TECNICA-preliminar.md"),
    ("PRE-03", "auditoría", "Documento auditoría SEO 5 hallazgos críticos", "2026-08-13", "hecho", "https://jairosaul.com/peru-grand-travel"),
    ("PRE-04", "hreflang", "Mapa equivalencias ~60 tours EN|ES|PT|IT", "2026-08-15", "hecho", "archivo-original/empleo-seo/equivalencias-hreflang.csv"),
    ("PRE-05", "hreflang", "Análisis gaps catálogo entre dominios", "2026-08-15", "hecho", "archivo-original/empleo-seo/gaps-de-catalogo.csv"),
    ("PRE-06", "código", "auditor_seo.py crawl automático", "2026-08-18", "hecho", "archivo-original/empleo-seo/auditor_seo.py"),
    ("PRE-07", "código", "Prototipo hreflang-multidominio.php", "2026-08-18", "hecho", "archivo-original/empleo-seo/hreflang-multidominio.php"),
    ("PRE-08", "código", "generar_mapa_hreflang.py", "2026-08-20", "hecho", "archivo-original/empleo-seo/generar_mapa_hreflang.py"),
    ("PRE-09", "contenido", "Plantillas JSON-LD turismo", "2026-08-22", "hecho", "archivo-original/empleo-seo/plantillas-jsonld-turismo.md"),
    ("PRE-10", "estrategia", "Benchmark competidores Cusco", "2026-08-22", "hecho", "archivo-original/empleo-seo/08-BENCHMARK-COMPETIDORES-CUSCO.md"),
    ("PRE-11", "estrategia", "Playbook aportes 90 días", "2026-08-22", "hecho", "archivo-original/empleo-seo/14-PLAYBOOK-APORTES.md"),
    ("PRE-12", "portafolio", "Página jairosaul.com/peru-grand-travel", "2026-08-24", "hecho", "https://jairosaul.com/peru-grand-travel"),
    ("PRE-13", "portafolio", "Correo + CV postulación", "2026-08-24", "hecho", "archivo-original/empleo-seo/15-CORREO-CV.md"),
    ("PRE-14", "contenido", "Guion video auditoría Loom", "2026-08-24", "hecho", "archivo-original/empleo-seo/10-GUION-VIDEO.md"),
    ("PRE-15", "contenido", "30 artículos SEO/GEO MDX", "2026-08-31", "hecho", "conocimiento/articulos-jairosaul/"),
    ("PRE-16", "negociación", "Guiones entrevista + KPIs sueldo", "2026-08-24", "hecho", "archivo-original/empleo-seo/05-GUIONES-contacto-entrevista-negociacion.md"),
]
for pid, cat, t, fd, st, ev in pre:
    add(id=pid, epica_id="", tipo="tarea", track="seo-operaciones", fecha_inicio=fd,
        categoria=f"pre-pgt/{cat}", tarea=t, prioridad="P1" if "PRE-0" in pid and int(pid.split("-")[1]) > 3 else "P0",
        estado=st, evidencia=ev, link=ev if ev.startswith("http") else "")

# PGT mes 1 — operaciones SEO (no Drupal manual, no pgt-web)
def op(pid, cat, t, fd, dia, st, ev, pri="P1", met="", note=""):
    add(
        id=pid, epica_id="", tipo="tarea", track="seo-operaciones",
        fecha_inicio=fd, dia_pgt=dia, categoria=cat, tarea=t,
        prioridad=pri, estado=st, evidencia=ev, metrica=met, notas=note,
    )

op("OPS-01", "onboarding", "Setup accesos marketing@ NAS Drive WA", "2026-08-25", "D1", "hecho", "01-situacion/BITACORA.md", "P0")
op("OPS-02", "onboarding", "Confirmación bloques tours 3 + blogs 4", "2026-08-25", "D1", "hecho", "03-seo/BLOQUE-JAIRO.md", "P0")
op("OPS-03", "negociación", "Pacto oral Clever S/3500 → ~25 sep S/5000", "2026-08-25", "D1", "hecho", "07-negociacion/WHATSAPP-PACTO-REVISADO.md", "P0")
op("OPS-04", "negociación", "WhatsApp pacto 25 sep por escrito", "", "", "pendiente", "07-negociacion/WHATSAPP-PACTO-REVISADO.md", "P0")
op("OPS-05", "datos", "Análisis bloque 18 tours + 115 blogs", "2026-08-26", "D2", "hecho", "03-seo/ANALISIS-BLOQUE-JAIRO-2026-08-25.md", "P0")
op("OPS-06", "datos", "CSV prioridades P0/P1 bloque", "2026-08-26", "D2", "hecho", "03-seo/datos/PRIORIDAD-ACCION-JAIRO-2026-08-26.csv", "P0")
op("OPS-07", "datos", "Inventario Drive + mapa GA4", "2026-08-26", "D2", "hecho", "02-empresa/DRIVE-INVENTARIO.md", "P1")
op("OPS-08", "estrategia", "Borrador plan SEO Clever v1", "2026-08-26", "D2", "hecho", "03-seo/PLAN-SEO-PARA-CLEVER-BORRADOR.md", "P1")
op("OPS-09", "datos", "Línea base GSC sitio 28d", "2026-08-27", "D3", "hecho", "03-seo/informes/2026-08-27-interno.md", "P0", "643 clics")
op("OPS-10", "equipo", "Identificar interino Einel", "2026-08-27", "D3", "hecho", "01-situacion/BITACORA.md", "P1")
op("OPS-11", "informes", "Informes internos días 1–6", "2026-09-01", "D6", "hecho", "03-seo/informes/", "P1")
op("OPS-12", "auditoría", "Staging Drupal vs WP Things MP + Salkantay", "2026-08-28", "D4", "hecho", "03-seo/auditorias/", "P0", "2 auditorías P0")
op("OPS-13", "datos", "Inventario 133 URLs bloque", "2026-08-28", "D4", "hecho", "03-seo/datos/inventario-bloque-jairo.csv", "P0", "133")
op("OPS-14", "migración", "Mapa 25 URLs prioritarias WP→Drupal", "2026-08-28", "D4", "hecho", "03-seo/datos/mapa-urls-wp-drupal.csv", "P0")
op("OPS-15", "migración", "Checklist pre-launch Drupal", "2026-08-28", "D4", "hecho", "03-seo/migracion/CHECKLIST-PRE-LAUNCH-DRUPAL.md", "P0")
op("OPS-16", "migración", "Playbook migración WP→Drupal", "2026-08-28", "D4", "hecho", "08-investigacion/MIGRACION-WP-DRUPAL-PLAYBOOK.md", "P1")
op("OPS-17", "migración", "Esquema migración maestro", "2026-08-28", "D4", "hecho", "08-investigacion/ESQUEMA-MIGRACION-MAESTRO.md", "P1")
op("OPS-18", "prod", "Fix CTR blog Things MP Rank Math", "2026-08-28", "D4", "hecho", "03-seo/informes/2026-08-28-things-mp-optimizacion.md", "P0", "6115 imp")
op("OPS-19", "prod", "Indexación GSC Things MP", "2026-08-28", "D4", "hecho", "03-seo/guias/GSC-SOLICITAR-INDEXACION.md", "P1")
op("OPS-20", "carrera", "Plan 30 días → S/5000", "2026-08-29", "D5", "hecho", "mi-carrera/PLAN-30-DIAS-5000.md", "P1")
op("OPS-21", "auditoría", "Revisión staging delta 29 ago", "2026-08-29", "D5", "hecho", "08-investigacion/DRUPAL-STAGING-REVISION-2026-08-29.md", "P1")
op("OPS-22", "carrera", "Estrategia experimento 4 personas", "2026-09-01", "D6", "hecho", "mi-carrera/EXPERIMENTO-4-ESTRATEGIA-JAIRO.md", "P1")
op("OPS-23", "informes", "Informe maestro + externo semana 1", "2026-09-01", "D6", "hecho", "mi-carrera/INFORME-EXTERNO-SEMANA1-JAIRO.md", "P0", "6/7 entregables")
op("OPS-24", "datos", "Mapa 454 redirects blog categoría→limpia", "2026-09-01", "D6", "hecho", "03-seo/datos/keywords-canibalizacion-2026-08-31/redirects-blog-301.csv", "P0", "454")
op("OPS-25", "datos", "Inventario sitemap live", "2026-09-01", "D6", "hecho", "03-seo/datos/inventario-sitemap-2026-08-31/", "P1", "69+452+62")
op("OPS-26", "datos", "Export GSC 15k filas automatizado", "2026-09-01", "D6", "hecho", "03-seo/datos/gsc-export-2026-09-01/", "P0", "15101")
op("OPS-27", "datos", "Export GA4 landings + eventos", "2026-09-01", "D6", "hecho", "03-seo/datos/ga4-export-2026-09-01/", "P1", "174 landings")
op("OPS-28", "automation", "9 scripts Python/Bash SEO migración", "2026-09-01", "D6", "hecho", "03-seo/scripts/", "P1", "9 scripts")
op("OPS-29", "aprendizaje", "15 docs currículo Drupal", "2026-09-01", "D6", "hecho", "10-aprendizaje/drupal/", "P2", "15 docs")
op("OPS-30", "aprendizaje", "101 capturas admin Drupal", "2026-09-01", "D6", "hecho", "10-aprendizaje/drupal/13-INDICE-CAPTURAS-DRUPAL.md", "P2", "101")
op("OPS-31", "investigación", "CRM PGT mapeo (no construir)", "2026-08-28", "D4", "hecho", "08-investigacion/CRM-PGT-Y-VECTORIFY.md", "P2")
op("OPS-32", "investigación", "Lighthouse comparativa POC vs WP", "2026-08-28", "D4", "hecho", "08-investigacion/LIGHTHOUSE-COMPARATIVA.md", "P2", "99 vs 55")
op("OPS-33", "investigación", "Greenfield plan maestro", "2026-08-31", "D5", "hecho", "08-investigacion/GREENFIELD-PGT-PLAN-MAESTRO.md", "P2")
op("OPS-34", "investigación", "Diseño gestión accesos Vaultwarden", "2026-09-01", "D6", "hecho", "02-empresa/GESTION-ACCESOS-DISENO.md", "P2")
op("OPS-35", "guías", "Guías CTR Things MP", "2026-08-28", "D4", "hecho", "03-seo/guias/CTR-THINGS-MP-WP-PASO-A-PASO.md", "P1")
op("OPS-36", "guías", "Medición leads WA web actual", "2026-09-01", "D6", "hecho", "03-seo/guias/MEDIR-LEADS-WEB-ACTUAL.md", "P1")
op("OPS-37", "guías", "Drupal sprint diario", "2026-09-01", "D6", "hecho", "03-seo/guias/DRUPAL-SPRINT-JAIRO-HOY.md", "P1")
op("OPS-38", "integraciones", "MCP Google GA4+GSC+Drive OAuth", "2026-09-01", "D6", "hecho", ".cursor/mcp.json", "P1", "verify 7/7")
op("OPS-39", "integraciones", "GSC SA propiedad ES (403)", "", "", "pendiente", "../pgt-web/docs/INVENTARIO-PLATAFORMAS.md", "P2")
op("OPS-40", "geo", "GEO baseline 10 prompts", "", "", "pendiente", "04-geo/BASELINE-PLANTILLA.md", "P2")
op("OPS-41", "equipo", "Mapa paid↔orgánico con Lizet", "", "", "pendiente", "05-marketing/ADS-GOOGLE-META.md", "P2")
op("OPS-42", "equipo", "Avisar NAS linux_admin a Ricardo", "", "", "pendiente", "01-situacion/BITACORA.md", "P2")
op("OPS-43", "blogs", "Migrar 115 blogs bloque 4 (post-tours)", "", "", "pendiente", "03-seo/datos/blogs-jairo-2026-08-25.csv", "P1", "0/115")
op("OPS-44", "tracker", "Sistema tracker 3 tracks + sync Sheet", "2026-09-02", "D7", "hecho", "mi-carrera/tracker/TAREAS-MAESTRO.csv", "P2")

with OUT.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=FIELDS)
    w.writeheader()
    w.writerows(rows)

from collections import Counter
c = Counter(r["track"] for r in rows)
s = Counter(r["estado"] for r in rows)
print(f"Wrote {len(rows)} rows to {OUT}")
print("Por track:", dict(c))
print("Por estado:", dict(s))
