# Mensaje DNS — Ricardo (copiar y enviar)

**Subdominio:** `beta.perugrandtravel.com`  
**Destino:** Vercel (staging greenfield EN, noindex)

---

## WhatsApp / correo a Ricardo

> Ricardo, para el rebuild EN en código (staging interno, **no reemplaza Drupal ni WP prod**) necesito un subdominio de prueba:
>
> **`beta.perugrandtravel.com`**
>
> Registro DNS:
> - Tipo: **CNAME**
> - Nombre: **beta**
> - Valor: **cname.vercel-dns.com**
>
> Es solo para demo con el equipo (Clever/Einer). El sitio llevará `noindex` — no compite con Google. ¿Te parece bien o prefieres otro subdominio?
>
> Gracias, Jairo

---

## Después de que Ricardo confirme

1. Deploy en Vercel (repo `pgt-web`)
2. Vercel → Project Settings → Domains → Add `beta.perugrandtravel.com`
3. Si Vercel pide otro CNAME, usar el que muestre el panel (puede variar por proyecto)
4. Env var: `NEXT_PUBLIC_SITE_URL=https://beta.perugrandtravel.com`
5. Verificar: `curl -I https://beta.perugrandtravel.com/`

## Alternativa sin DNS (mientras tanto)

Usar URL `*.vercel.app` del proyecto para demo interna.
