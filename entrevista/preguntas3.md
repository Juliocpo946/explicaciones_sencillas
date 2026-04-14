# Preguntas Habituales de Entrevista — Sin código aún

---

## HTML

**¿Cuál es la diferencia entre `<div>` y `<span>`?**
`div` es un elemento de bloque, ocupa toda la línea. `span` es inline, solo ocupa el espacio de su contenido. Ambos no tienen significado semántico, son contenedores genéricos.

**¿Qué es el DOCTYPE?**
Es la primera línea del HTML, le dice al navegador qué versión de HTML está usando. `<!DOCTYPE html>` indica HTML5. Sin él el navegador entra en "quirks mode" y puede renderizar cosas de forma inesperada.

**¿Diferencia entre `<script>` con `defer` y `async`?**
Ambos cargan el script sin bloquear el HTML. La diferencia es que `defer` espera a que el HTML termine de parsear para ejecutarse. `async` lo ejecuta en cuanto termina de descargarse sin importar si el HTML ya terminó.

**¿Qué es el atributo `alt` en las imágenes?**
Es el texto alternativo que se muestra si la imagen no carga. También lo usan los lectores de pantalla para describir la imagen a personas con discapacidad visual. Es importante para accesibilidad y SEO.

---

## CSS

**¿Qué es la herencia en CSS?**
Algunas propiedades CSS se heredan automáticamente de padre a hijo, como `color`, `font-family` y `font-size`. Otras no se heredan, como `border`, `margin` o `padding`. Puedes forzar herencia con el valor `inherit`.

**¿Diferencia entre `display: none` y `visibility: hidden`?**
`display: none` elimina el elemento del flujo, no ocupa espacio. `visibility: hidden` lo oculta visualmente pero sigue ocupando su espacio en el layout.

**¿Qué es `z-index`?**
Controla el orden de apilamiento de elementos posicionados. Un `z-index` mayor significa que el elemento aparece encima de otros. Solo funciona en elementos con `position` diferente a `static`.

**¿Diferencia entre `em` y `rem`?**
`em` es relativo al `font-size` del elemento padre inmediato. `rem` es relativo al `font-size` del elemento raíz (`html`). `rem` es más predecible porque no se acumula en elementos anidados.

**¿Qué es un preprocesador CSS?**
Es una herramienta que extiende CSS con funcionalidades extra como variables, anidamiento, mixins y funciones. Los más conocidos son SASS y LESS. Al final compilan a CSS normal.

---

## JavaScript

**¿Qué es el scope?**
Es el contexto en el que una variable existe y es accesible. Hay scope global (accesible en todo el código), scope de función (solo dentro de la función) y scope de bloque (solo dentro de `{}`con `let` y `const`).

**¿Qué es el hoisting?**
Es el comportamiento de JavaScript de mover las declaraciones de variables y funciones al inicio de su scope antes de ejecutar el código. Las funciones declaradas con `function` se suben completas. Las variables con `var` se suben pero sin su valor.

**¿Qué es el closure?**
Es cuando una función recuerda las variables de su scope exterior aunque esa función ya haya terminado de ejecutarse. Es uno de los conceptos más preguntados en entrevistas de JavaScript.

**¿Diferencia entre `null` y `undefined`?**
`undefined` significa que una variable fue declarada pero no tiene valor asignado. `null` es un valor asignado intencionalmente para indicar que algo está vacío o no existe. Ambos son falsy pero son tipos distintos.

**¿Qué es JSON?**
JavaScript Object Notation. Es un formato de texto para intercambiar datos entre sistemas. Se parece a un objeto de JavaScript pero es solo texto. Se convierte con `JSON.parse()` para leerlo y `JSON.stringify()` para convertirlo de vuelta.

**¿Diferencia entre `forEach` y `map`?**
`forEach` recorre el array y no retorna nada, se usa para efectos secundarios. `map` recorre el array y retorna uno nuevo transformado. Si necesitas el resultado usa `map`, si solo necesitas ejecutar algo usa `forEach`.

**¿Qué es el operador ternario?**
Es una forma corta de escribir un if/else en una sola línea. La estructura es `condicion ? valorSiTrue : valorSiFalse`. Se usa para asignaciones simples, no para lógica compleja.

---

## TypeScript

**¿Por qué usar TypeScript sobre JavaScript?**
Porque detecta errores en tiempo de desarrollo antes de ejecutar el código, hace el código más predecible y mantenible, mejora el autocompletado del editor y es casi obligatorio en proyectos grandes o en equipo.

**¿Qué es la inferencia de tipos?**
TypeScript puede deducir el tipo de una variable automáticamente según el valor que le asignas, sin que lo declares explícitamente. Si escribes `let nombre = "Ana"`, TypeScript ya sabe que es `string` sin que lo digas.

**¿Qué es `unknown` y en qué se diferencia de `any`?**
Ambos aceptan cualquier tipo de valor. La diferencia es que `any` te deja hacer cualquier operación sin validar. `unknown` te obliga a verificar el tipo antes de usarlo. `unknown` es la versión segura de `any`.

**¿Qué es un decorador en TypeScript?**
Es una función especial que se aplica a clases, métodos o propiedades para agregar comportamiento extra sin modificar el código original. Se usa mucho en frameworks como Angular y NestJS con la sintaxis `@NombreDecorador`.

---

## PHP

**¿Qué es la inyección SQL y cómo se previene?**
Es un ataque donde alguien inserta código SQL malicioso en un campo de formulario para manipular la base de datos. Se previene usando consultas preparadas con PDO en lugar de concatenar strings directamente en la consulta.

**¿Qué es Composer?**
Es el manejador de dependencias de PHP, equivalente a npm en JavaScript. Permite instalar librerías externas en tu proyecto y manejar sus versiones mediante el archivo `composer.json`.

**¿Diferencia entre sesiones y cookies?**
Las cookies se guardan en el navegador del usuario, son accesibles desde el cliente y tienen un límite de tamaño. Las sesiones se guardan en el servidor, son más seguras para datos sensibles y se identifican mediante un ID en una cookie.

**¿Qué es un namespace en PHP?**
Es una forma de organizar el código y evitar conflictos de nombres entre clases o funciones. Similar a los módulos en JavaScript. Se usa en proyectos grandes donde múltiples librerías pueden tener clases con el mismo nombre.

**¿Qué es MVC?**
Model View Controller. Es un patrón de arquitectura que separa la aplicación en tres capas: Model (lógica de datos y base de datos), View (lo que ve el usuario, el HTML) y Controller (recibe las peticiones, coordina Model y View). Laravel usa este patrón.

---
