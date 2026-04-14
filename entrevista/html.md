Empezamos con **HTML**.

---

# HTML — Explicación + Ejemplos

---

## 1. ¿Qué es HTML?

**Explicación:** HTML (HyperText Markup Language) es el lenguaje de estructura de toda página web. No es un lenguaje de programación, es un lenguaje de marcado. Define qué elementos existen en la página y su jerarquía, pero no su apariencia ni comportamiento, eso lo hacen CSS y JavaScript respectivamente.

```html
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8">
    <title>Mi página</title>
  </head>
  <body>
    <h1>Hola mundo</h1>
    <p>Este es un párrafo.</p>
  </body>
</html>
```

---

## 2. ¿Qué es HTML Semántico?

**Explicación:** Es usar etiquetas que describen el significado del contenido, no solo su apariencia. Antes todo era `<div>`, ahora existen etiquetas específicas para cada sección. Esto mejora el SEO (los buscadores entienden mejor la página), la accesibilidad (lectores de pantalla para personas con discapacidad) y la legibilidad del código.

```html
<!-- No semántico → todo es div sin significado -->
<div id="header">...</div>
<div id="menu">...</div>
<div id="contenido">...</div>
<div id="footer">...</div>

<!-- Semántico → cada etiqueta describe su propósito -->
<header>        <!-- encabezado de la página -->
  <nav>         <!-- menú de navegación -->
    <ul>
      <li><a href="/">Inicio</a></li>
      <li><a href="/about">Nosotros</a></li>
    </ul>
  </nav>
</header>

<main>          <!-- contenido principal -->
  <section>     <!-- sección temática -->
    <article>   <!-- contenido independiente -->
      <h2>Título del artículo</h2>
      <p>Contenido...</p>
    </article>
  </section>

  <aside>       <!-- contenido secundario / barra lateral -->
    <p>Publicidad o links relacionados</p>
  </aside>
</main>

<footer>        <!-- pie de página -->
  <p>© 2026 Mi empresa</p>
</footer>
```

---

## 3. ¿Cómo hacer un formulario solo con etiquetas HTML?

**Explicación:** Un formulario usa la etiqueta `<form>` como contenedor. `action` define a dónde se envían los datos y `method` define cómo (GET visible en URL, POST oculto). Cada campo tiene su etiqueta `<label>` vinculada por el atributo `for` que coincide con el `id` del input. Esto es importante para accesibilidad.

```html
<form action="/enviar" method="POST">

  <!-- Campo de texto -->
  <label for="nombre">Nombre:</label>
  <input type="text" id="nombre" name="nombre" required placeholder="Tu nombre">

  <!-- Campo de email -->
  <label for="email">Correo:</label>
  <input type="email" id="email" name="email" required>

  <!-- Campo de contraseña -->
  <label for="password">Contraseña:</label>
  <input type="password" id="password" name="password" minlength="8">

  <!-- Campo numérico -->
  <label for="edad">Edad:</label>
  <input type="number" id="edad" name="edad" min="1" max="120">

  <!-- Select / desplegable -->
  <label for="pais">País:</label>
  <select id="pais" name="pais">
    <option value="">Selecciona...</option>
    <option value="mx">México</option>
    <option value="co">Colombia</option>
  </select>

  <!-- Área de texto -->
  <label for="mensaje">Mensaje:</label>
  <textarea id="mensaje" name="mensaje" rows="4"></textarea>

  <!-- Checkbox -->
  <label>
    <input type="checkbox" name="terminos" required>
    Acepto los términos
  </label>

  <!-- Radio buttons -->
  <label><input type="radio" name="genero" value="m"> Masculino</label>
  <label><input type="radio" name="genero" value="f"> Femenino</label>

  <!-- Botones -->
  <button type="submit">Enviar</button>
  <button type="reset">Limpiar</button>

</form>
```

---

## 4. ¿Diferencia entre etiquetas en bloque e inline?

**Explicación:** Las etiquetas de bloque ocupan todo el ancho disponible y empiezan en una nueva línea. Las inline solo ocupan el espacio de su contenido y no rompen el flujo del texto.

```html
<!-- Bloque → ocupan toda la línea -->
<div>Soy un div</div>
<p>Soy un párrafo</p>
<h1>Soy un título</h1>
<section>Soy una sección</section>

<!-- Inline → viven dentro del texto -->
<p>
  Este texto tiene una
  <span>parte resaltada</span>
  y un <a href="#">enlace</a>
  y texto <strong>en negrita</strong>
  y texto <em>en cursiva</em>.
</p>
```

---

## 5. ¿Qué son los atributos en HTML?

**Explicación:** Los atributos dan información adicional a las etiquetas. Van dentro de la etiqueta de apertura con el formato `nombre="valor"`. Algunos son globales (funcionan en cualquier etiqueta) y otros son específicos de ciertos elementos.

```html
<!-- Atributos comunes -->
<img src="foto.jpg" alt="Descripción de la imagen" width="300">

<a href="https://google.com" target="_blank" rel="noopener">Google</a>

<input type="text" id="campo" name="campo" placeholder="Escribe aquí" required disabled>

<!-- Atributos globales → funcionan en cualquier etiqueta -->
<div id="unico"             <!-- identificador único en la página -->
     class="tarjeta activa" <!-- clases para CSS -->
     style="color: red"     <!-- estilo inline -->
     title="Tooltip"        <!-- texto al hacer hover -->
     data-id="123">         <!-- datos personalizados para JS -->
</div>
```

---

## 6. ¿Qué es el atributo `data-*`?

**Explicación:** Los atributos `data-*` permiten guardar información personalizada en etiquetas HTML para que JavaScript la pueda leer sin necesidad de hacer llamadas extra al servidor. Son muy usados en aplicaciones dinámicas.

```html
<button
  data-id="42"
  data-accion="eliminar"
  data-nombre="Producto A"
  id="btn-eliminar">
  Eliminar
</button>
```

```javascript
const boton = document.getElementById("btn-eliminar");

boton.addEventListener("click", () => {
  const id     = boton.dataset.id;      // "42"
  const accion = boton.dataset.accion;  // "eliminar"
  console.log(`Ejecutando ${accion} sobre id ${id}`);
});
```

---

## 7. ¿Qué es accesibilidad en HTML?

**Explicación:** Accesibilidad significa que tu página puede ser usada por personas con discapacidades visuales, motoras, etc. HTML tiene atributos ARIA y buenas prácticas para esto. En entrevistas valoran que lo menciones aunque sea brevemente.

```html
<!-- Mal → sin contexto para lectores de pantalla -->
<button>X</button>
<img src="logo.png">

<!-- Bien → con contexto accesible -->
<button aria-label="Cerrar ventana">X</button>
<img src="logo.png" alt="Logo de la empresa">

<!-- role → define el rol del elemento -->
<div role="alert">Error al guardar los datos</div>

<!-- aria-hidden → oculta elemento de lectores de pantalla -->
<span aria-hidden="true">★★★★☆</span>
```

---

## 8. ¿Qué va en el `<head>`?

**Explicación:** El `<head>` contiene metadatos, es decir, información sobre la página que no se muestra visualmente pero es importante para el navegador, los buscadores y las redes sociales.

```html
<head>
  <!-- Codificación de caracteres -->
  <meta charset="UTF-8">

  <!-- Diseño responsivo obligatorio -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- SEO -->
  <meta name="description" content="Descripción de mi página">

  <!-- Título en la pestaña del navegador -->
  <title>Mi Página</title>

  <!-- CSS externo -->
  <link rel="stylesheet" href="estilos.css">

  <!-- Favicon -->
  <link rel="icon" href="favicon.ico">

  <!-- JS al final del head o body -->
  <script src="app.js" defer></script>
</head>
```

---

## 9. ¿Diferencia entre `id` y `class`?

**Explicación:** `id` es un identificador único, solo debe existir uno por página. `class` puede repetirse en múltiples elementos. En CSS, `id` se selecciona con `#` y `class` con `.`. En la práctica se recomienda usar clases para estilos e ids solo cuando JavaScript necesita encontrar un elemento específico.

```html
<!-- id → único en toda la página -->
<header id="header-principal">...</header>

<!-- class → reutilizable en múltiples elementos -->
<div class="tarjeta">Producto 1</div>
<div class="tarjeta">Producto 2</div>
<div class="tarjeta destacada">Producto 3</div>
```

```css
#header-principal { background: #111; }  /* id con # */
.tarjeta          { border: 1px solid; } /* class con . */
.tarjeta.destacada { border-color: gold; } /* doble clase */
```

---

## 10. ¿Qué es un `<meta viewport>` y por qué importa?

**Explicación:** Sin esta etiqueta, los navegadores móviles simulan una pantalla de escritorio y reducen todo, haciendo el sitio ilegible. Con el viewport le dices al navegador que adapte el ancho al dispositivo real. Es la base del diseño responsivo.

```html
<!-- Sin esto → en móvil se ve todo muy pequeño -->

<!-- Con esto → el navegador adapta el ancho al dispositivo -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!--
  width=device-width  → ancho igual al del dispositivo
  initial-scale=1.0   → sin zoom inicial
-->
```

---

Listo HTML completo. Ahora **CSS**.

---

# CSS — Explicación + Ejemplos

---

## 1. ¿Qué es CSS?

**Explicación:** CSS (Cascading Style Sheets) es el lenguaje que controla la apariencia visual del HTML. Separar estructura (HTML) de presentación (CSS) es una buena práctica fundamental. La palabra "cascada" significa que los estilos se aplican en orden y los más específicos o los que vienen después sobreescriben a los anteriores.

```css
/* Sintaxis básica */
selector {
  propiedad: valor;
}

/* Ejemplo */
h1 {
  color: white;
  font-size: 32px;
  font-family: Arial, sans-serif;
}
```

---

## 2. ¿Qué es el Modelo de Caja (Box Model)?

**Explicación:** Todo elemento HTML es una caja rectangular compuesta por 4 capas. De adentro hacia afuera: **content** (el contenido), **padding** (espacio interno entre contenido y borde), **border** (el borde), **margin** (espacio externo entre el elemento y otros). Con `box-sizing: border-box` el padding y border se incluyen dentro del ancho declarado, lo que hace el layout más predecible.

```css
.caja {
  width: 200px;
  height: 100px;

  padding: 16px;           /* espacio interno */
  border: 2px solid #333;  /* borde */
  margin: 20px;            /* espacio externo */

  /* Sin esto: ancho real = 200 + 16*2 + 2*2 = 236px */
  /* Con esto: ancho real = 200px exactos */
  box-sizing: border-box;
}

/* Buena práctica → aplicarlo a todo */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
```

---

## 3. ¿Cómo centrar un div?

**Explicación:** Hay varias formas según el caso. Flexbox es la más moderna y recomendada. Cada una tiene su caso de uso: margin auto es para centrado horizontal simple, Flexbox para centrado en ambos ejes, Grid para layouts más complejos.

```css
/* Centrado horizontal con margin auto */
.caja {
  width: 300px;
  margin: 0 auto;
}

/* Centrado horizontal y vertical con Flexbox */
.contenedor {
  display: flex;
  justify-content: center; /* horizontal */
  align-items: center;     /* vertical */
  height: 100vh;
}

/* Centrado con Grid */
.contenedor {
  display: grid;
  place-items: center;     /* shorthand de ambos ejes */
  height: 100vh;
}

/* Centrado absoluto */
.caja {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
```

---

## 4. ¿Qué es Flexbox?

**Explicación:** Flexbox es un sistema de layout unidimensional, trabaja en una sola dirección (fila o columna). Se activa con `display: flex` en el contenedor padre. Permite distribuir, alinear y ordenar elementos hijos de forma flexible sin usar floats ni posicionamiento manual.

```css
.contenedor {
  display: flex;
  flex-direction: row;          /* fila (default) o column */
  justify-content: space-between; /* distribución horizontal */
  align-items: center;            /* alineación vertical */
  gap: 16px;                      /* espacio entre hijos */
  flex-wrap: wrap;                /* permite que bajen de línea */
}

/* Propiedades en los hijos */
.hijo {
  flex: 1;        /* crece para ocupar espacio disponible */
  flex: 0 0 200px; /* no crece, no encoge, ancho fijo 200px */
}
```

```html
<div class="contenedor">
  <div class="hijo">1</div>
  <div class="hijo">2</div>
  <div class="hijo">3</div>
</div>
```

---

## 5. ¿Qué es el Diseño Responsivo?

**Explicación:** Es que el sitio se vea bien en cualquier tamaño de pantalla. Se logra con tres herramientas: media queries (reglas CSS según el tamaño), unidades relativas (%, em, rem, vw, vh en lugar de px fijos) y layouts flexibles (Flexbox o Grid). El enfoque recomendado es **mobile first**: diseñar primero para móvil y luego agregar estilos para pantallas más grandes.

```css
/* Mobile first → base para móvil */
.contenedor {
  width: 100%;
  padding: 16px;
  font-size: 14px;
}

/* Tablet → desde 768px */
@media (min-width: 768px) {
  .contenedor {
    max-width: 720px;
    margin: 0 auto;
    font-size: 16px;
  }
}

/* Desktop → desde 1200px */
@media (min-width: 1200px) {
  .contenedor {
    max-width: 1100px;
    font-size: 18px;
  }
}

/* Unidades relativas */
.texto {
  font-size: 1rem;    /* relativo al root (html) */
  padding: 2em;       /* relativo al font-size del elemento */
  width: 80%;         /* relativo al padre */
  height: 50vh;       /* relativo al alto de la ventana */
}
```

---

## 6. ¿Qué es la especificidad en CSS?

**Explicación:** Cuando varios selectores apuntan al mismo elemento, CSS decide cuál tiene prioridad usando un sistema de puntos llamado especificidad. Inline styles ganan siempre, luego ids, luego clases, luego etiquetas. Conocer esto evita el abuso de `!important`.

```css
/* Especificidad de menor a mayor */

p              { color: gray; }    /* etiqueta → 0,0,1 */
.texto         { color: blue; }    /* clase     → 0,1,0 */
#titulo        { color: green; }   /* id        → 1,0,0 */
                                   /* inline    → 1,0,0,0 */

/* Combinaciones suman puntos */
p.texto        { color: red; }     /* etiqueta + clase → 0,1,1 */
#titulo.activo { color: white; }   /* id + clase       → 1,1,0 */

/* !important sobreescribe todo → evitar en lo posible */
p { color: purple !important; }
```

---

## 7. ¿Diferencia entre `position` relative, absolute y fixed?

**Explicación:** `static` es el valor por defecto, el elemento sigue el flujo normal. `relative` se mueve relativo a su posición original sin salir del flujo. `absolute` se posiciona relativo al ancestro con position no static, sale del flujo normal. `fixed` se posiciona relativo a la ventana del navegador y no se mueve al hacer scroll.

```css
/* relative → se mueve desde donde estaría normalmente */
.relativo {
  position: relative;
  top: 10px;
  left: 20px;
}

/* absolute → se posiciona dentro de su padre con position */
.padre {
  position: relative; /* necesario para que el hijo sea absoluto dentro */
}
.absoluto {
  position: absolute;
  top: 0;
  right: 0;         /* esquina superior derecha del padre */
}

/* fixed → siempre visible, no se mueve con el scroll */
.navbar {
  position: fixed;
  top: 0;
  width: 100%;
  background: #111;
}
```

---

## 8. ¿Qué son las variables CSS?

**Explicación:** Las variables CSS (custom properties) permiten definir valores reutilizables en un solo lugar. Si necesitas cambiar el color principal de toda la app, cambias un solo valor. Se declaran con `--nombre` y se usan con `var(--nombre)`. Casi siempre se declaran en `:root` para que estén disponibles globalmente.

```css
/* Declaración en root → disponibles en todo el documento */
:root {
  --color-primario:  #1a1a2e;
  --color-acento:    #16213e;
  --color-texto:     #e0e0e0;
  --espaciado-base:  16px;
  --radio-borde:     8px;
}

/* Uso */
.tarjeta {
  background:    var(--color-primario);
  color:         var(--color-texto);
  padding:       var(--espaciado-base);
  border-radius: var(--radio-borde);
}

.boton {
  background: var(--color-acento);
  padding:    calc(var(--espaciado-base) / 2) var(--espaciado-base);
}
```

---

## 9. ¿Qué es la pseudoclase y el pseudoelemento?

**Explicación:** Las pseudoclases seleccionan elementos según su estado (`:hover`, `:focus`, `:nth-child`). Los pseudoelementos seleccionan una parte del elemento (`::before`, `::after`, `::placeholder`). Se diferencian por uno o dos puntos, aunque los navegadores aceptan ambos.

```css
/* Pseudoclases → estado del elemento */
a:hover     { color: #4af; }           /* cuando el mouse está encima */
input:focus { outline: 2px solid #4af; } /* cuando está seleccionado */
li:first-child { font-weight: bold; }   /* primer hijo */
li:nth-child(2) { color: gray; }        /* segundo hijo */
button:disabled { opacity: 0.5; }       /* botón deshabilitado */

/* Pseudoelementos → parte del elemento */
p::first-line   { font-weight: bold; }  /* primera línea del párrafo */

.tarjeta::before {
  content: "";          /* obligatorio aunque esté vacío */
  display: block;
  width: 4px;
  background: #4af;
}

input::placeholder {
  color: #666;
  font-style: italic;
}
```

---

## 10. ¿Qué es la transición y animación en CSS?

**Explicación:** `transition` suaviza el cambio entre dos estados de un elemento, por ejemplo al hacer hover. `animation` con `@keyframes` permite animaciones más complejas y continuas que no dependen de interacción del usuario.

```css
/* Transición → suaviza cambios de estado */
.boton {
  background: #1a1a2e;
  color: white;
  padding: 10px 20px;
  transition: background 0.3s ease, transform 0.2s ease;
}

.boton:hover {
  background: #16213e;
  transform: scale(1.05);
}

/* Animación con keyframes → movimiento continuo */
@keyframes pulso {
  0%   { opacity: 1;   transform: scale(1); }
  50%  { opacity: 0.6; transform: scale(1.05); }
  100% { opacity: 1;   transform: scale(1); }
}

.alerta {
  animation: pulso 2s ease infinite;
}

/* Animación de entrada */
@keyframes entrada {
  from { opacity: 0; transform: translateY(-20px); }
  to   { opacity: 1; transform: translateY(0); }
}

.modal {
  animation: entrada 0.3s ease forwards;
}
```

---