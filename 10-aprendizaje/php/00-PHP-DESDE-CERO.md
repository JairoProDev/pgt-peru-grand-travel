# PHP desde cero → útil para WordPress y Drupal

**Meta:** entender y leer PHP lo suficiente para no volar en reuniones y para trabajar temas/módulos conmigo.  
**No es:** un máster universitario en una noche. Vas por capas.

PHP = lenguaje del **servidor**. WordPress y Drupal están escritos en PHP. El navegador recibe HTML; PHP se ejecutó **antes**, en el hosting.

---

## Capa 0 — Idea (10 min)

| Lenguaje | Dónde corre | Ejemplo |
|---|---|---|
| HTML/CSS | Navegador | Estructura y estilo |
| JavaScript | Navegador (a veces también servidor) | Menús, clicks |
| **PHP** | **Servidor** | “Busca el tour en la BD y arma el HTML” |

Flujo:

1. Visitas `/tour/salkantay…`  
2. El servidor ejecuta PHP (WordPress o Drupal)  
3. PHP consulta MySQL  
4. PHP (o Twig generado desde PHP) devuelve HTML  
5. Tú ves la página  

---

## Capa 1 — Sintaxis mínima (leer en voz alta)

```php
<?php
// Comentario de una línea

$nombre = "Salkantay";           // variable (siempre con $)
$precio = 450;                   // número
$activo = true;                  // booleano

echo $nombre;                    // imprime
echo "Tour: " . $nombre;         // . concatena strings

if ($precio > 400) {
  echo "Premium";
} else {
  echo "Estandar";
}

$includes = ["Guía", "Tren"];    // array
foreach ($includes as $item) {
  echo $item;
}

function formatear_precio($n) {
  return "$" . $n . " USD";
}
echo formatear_precio($precio);
```

**Qué memorizar:**

- Empieza con `<?php`  
- Variables: `$algo`  
- `echo` imprime  
- `if` / `foreach` / `function`  
- Arrays con `[]`  

---

## Capa 2 — Cómo “se siente” en WordPress

```php
// En un tema, single-tour.php (simplificado)
get_header();
the_title('<h1>', '</h1>');
the_content();
get_footer();
```

O con hooks:

```php
add_action('wp_head', function () {
  echo '<link rel="alternate" hreflang="en" href="https://..." />';
});
```

Traducción: “cuando WordPress imprima el `<head>`, añade esta etiqueta.”

---

## Capa 3 — Cómo se siente en Drupal

Menos “archivos sueltos”, más **clases y servicios**. Ejemplo conceptual de un módulo custom:

```php
<?php

namespace Drupal\pgt_seo;

/**
 * Ayuda SEO (ejemplo didáctico).
 */
class WhatsappLink {
  public function build($phone, $text) {
    $q = rawurlencode($text);
    return "https://wa.me/{$phone}?text={$q}";
  }
}
```

Y Twig llama datos que PHP preparó.

**Drush** (CLI) también es PHP por debajo: comandos para limpiar caché, etc.

---

## Capa 4 — Conceptos que sí o sí

### 1) Request / Response

Una visita = petición HTTP → PHP arma respuesta.

### 2) Base de datos

PHP no “guarda tours en el archivo Twig”. Usa SQL (MySQL/MariaDB/PostgreSQL).  
Tú casi no escribirás SQL al inicio; el CMS lo hace.

### 3) Composer

Herramienta para instalar librerías PHP:

```bash
composer require drupal/redirect
```

Como `npm install` pero del mundo PHP.

### 4) Autoload / namespaces

Organizan código (`Drupal\pgt_seo\...`) para no pelear nombres.

### 5) Seguridad básica

- Nunca confíes en lo que manda el usuario sin validar  
- No pegues contraseñas en código  
- Updates = parches de seguridad  

El malware de plugins nulled **es PHP malicioso** inyectado.

---

## Capa 5 — Plan de dominio (4 semanas, realista)

| Semana | Enfoque | Práctica |
|---|---|---|
| 1 | Sintaxis: variables, if, arrays, funciones | Reescribir el ejemplo de Capa 1 a mano 3 veces |
| 2 | Leer código WP de un snippet `wp_head` | Explicar en voz alta qué hace |
| 3 | Leer un `.theme` o Twig + preprocess Drupal | Identificar variables |
| 4 | Escribir conmigo un módulo mínimo o helper | PR / archivo en staging |

**Recursos oficiales (cuando tengas tiempo):**  
php.net manual — solo capítulos: Language Reference básicos.  
No empieces por Laravel entero.

---

## Capa 6 — Ejercicios (hazlos)

### Ejercicio A

Sin mirar, escribe un `if` que diga “caro” si `$precio >= 500`.

### Ejercicio B

Explica qué imprime:

```php
$a = ["EN", "PT"];
echo $a[1];
```

(Respuesta: `PT`)

### Ejercicio C

¿Twig es PHP?  
Respuesta: Twig es **otro lenguaje de plantillas**; el motor Twig corre **en PHP** dentro de Drupal. Tú editas `.twig`; PHP lo compila detrás.

### Ejercicio D

¿Por qué un redirect 301 no se “hace en Twig” normalmente?  
Porque es regla de servidor/CMS (módulo Redirect / `.htaccess`), no presentación visual.

---

## Capa 7 — Cómo te ayudo yo

1. Pegas un archivo `.php` / `.theme` / `.module` (sin secrets).  
2. Te lo explico línea a línea en español.  
3. Escribimos el cambio juntos.  
4. Tú lo subes a staging con Ricardo.

No necesitas “ser experto PHP” antes del cutover. Necesitas **no asustarte** cuando abran un archivo y poder preguntar:

> “¿Esta función corre en el servidor al cargar el node, o solo al guardar?”

---

## Mini glosario PHP en una línea

| Término | Significado |
|---|---|
| `<?php` | Aquí empieza código PHP |
| `$var` | Variable |
| `echo` | Imprimir salida |
| `function` | Bloque reutilizable |
| `array` / `[]` | Lista |
| `class` | Molde de objeto (Drupal usa muchas) |
| `namespace` | Apellido del código para no chocar |
| `composer` | Instalador de paquetes PHP |
| `vendor/` | Carpeta donde Composer pone librerías |

Siguiente práctica: vuelve a `../drupal/09-TWIG-EXPLICADO.md` y marca qué parte es plantilla vs PHP.
