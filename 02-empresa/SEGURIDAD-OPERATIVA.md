# Seguridad operativa — día 1 en adelante

Reglas para no quemarte ni quemar a la empresa. Sin alarmismo; con criterio.

## Nunca en git / GitHub / chats de IA

- El Excel `Accesos PGT -2026 Actuales.xlsx`
- Contraseñas, PIN Banahosting, códigos de recuperación Facebook, secretos TOTP
- Capturas donde se lea una clave

Este repo está en `.gitignore` para `*Accesos*`, `*.xlsx`, carpetas `secretos/`.

Si Gemini u otra IA ya vio un secreto: asume que puede haber quedado en historial. No lo reenvíes. Si es crítico (Google Admin), que Ricardo rote cuando toque — no lo rotes tú solo.

## Cuenta marketing@ compartida

Todas las PCs usan la misma sesión. **No hay auditoría** de quién borró un anuncio o quién aceptó un permiso. En tu laptop, con tu perfil, al menos hay rastro de dispositivo. No “arregles” la seguridad de Google Admin sin clever@. Documenta el problema para la jefatura.

## clever@ y 2FA en su celular

Motivos legítimos más adelante (uno a la vez, con ticket):

- Verificar dominio en GSC por DNS
- Cambiar registro en Banahosting / Registros.com
- Revisar usuarios en Google Workspace

El día 2–14: **no**. Trabaja con marketing@ + lo que Ricardo ya te dio.

## NAS `linux_admin` + sudo

Créalo para montar el share está bien si Ricardo lo sabe. Tener **sudo** sin anunciarlo es el punto fino. Frase:

> Para no depender de la sesión Marketing compartida, creé un usuario en el OMV solo para mi laptop. Si quieren, lo dejamos solo en el grupo users sin sudo.

## Cuentas Facebook “falsas” (BR/ES/US)

Están en el Excel. Son un riesgo de ToS y de reputación. No las uses. Si el jefe de mkt las pide, que quede por escrito.

## WiFi vs Ethernet

Tu laptop en WiFi va más rápido que la PC cableada. Puede ser driver, proxy, antivirus o disco de la PC. No lo conviertas en “sistemas no sabe”. Si quieres aportar: medir speedtest en ambos y pasárselo a Ricardo como dato, no como juicio.
