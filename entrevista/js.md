# JavaScript — Explicación + Ejemplos

---

## 1. ¿Qué es JavaScript?

**Explicación:** JavaScript es el único lenguaje que los navegadores entienden de forma nativa. Corre del lado del cliente (navegador), lo que significa que no necesita servidor para ejecutarse. Se usa para hacer páginas interactivas: validar formularios, consumir APIs, manipular el HTML en tiempo real, animaciones, etc. También puede correr en el servidor usando **Node.js**.

```javascript
// Corre directo en el navegador
console.log("Hola desde el navegador");

// También válido en Node.js (servidor)
console.log("Hola desde el servidor");
```

---

## 2. ¿Diferencia entre `var`, `let` y `const`?

**Explicación:** Las tres declaran variables pero con comportamientos distintos. `var` es la forma antigua, tiene un scope global o de función y permite redeclararse, lo que genera bugs difíciles de detectar. `let` y `const` son modernas, tienen scope de bloque (solo viven dentro de `{}`). La diferencia entre ellas es que `let` permite reasignar el valor y `const` no.

```javascript
var nombre = "Ana";
var nombre = "Luis"; // permitido, no da error → peligroso

let edad = 25;
edad = 26;           // permitido reasignar
// let edad = 30;    // error → no se puede redeclarar

const PI = 3.14;
// PI = 3.15;        // error → no se puede reasignar

// Scope de bloque
if (true) {
  let dentro = "solo aqui";
  const tambien = "solo aqui";
}
// console.log(dentro); // error → no existe fuera del bloque
```

---

## 3. ¿Qué es una función flecha?

**Explicación:** Es una forma más corta de escribir funciones introducida en ES6. La diferencia principal no es solo la sintaxis, sino que las funciones flecha **no tienen su propio `this`**, heredan el `this` del contexto donde fueron creadas. Esto es importante cuando trabajas con clases o eventos.

```javascript
// Función tradicional
function sumar(a, b) {
  return a + b;
}

// Función flecha equivalente
const sumar = (a, b) => a + b;

// Si solo tiene un parámetro, no necesita paréntesis
const doble = n => n * 2;

// Si tiene varias líneas, necesita llaves y return
const describir = (nombre, edad) => {
  const mensaje = `${nombre} tiene ${edad} años`;
  return mensaje;
};

console.log(sumar(3, 4));       // 7
console.log(doble(5));          // 10
console.log(describir("Ana", 25)); // Ana tiene 25 años
```

---

## 4. ¿Qué es el DOM?

**Explicación:** DOM significa Document Object Model. Cuando el navegador carga un HTML, lo convierte en un árbol de objetos en memoria, eso es el DOM. JavaScript puede acceder a ese árbol para leer, modificar, agregar o eliminar elementos sin recargar la página. Es la base de toda interactividad en el navegador.

```javascript
// Seleccionar elementos
const titulo   = document.getElementById("titulo");
const parrafos = document.querySelectorAll("p");
const boton    = document.querySelector(".btn-principal");

// Modificar contenido y estilos
titulo.textContent  = "Nuevo título";
titulo.style.color  = "white";
titulo.style.fontSize = "24px";

// Crear y agregar un elemento nuevo
const nuevoParrafo = document.createElement("p");
nuevoParrafo.textContent = "Este párrafo fue creado con JS";
document.body.appendChild(nuevoParrafo);

// Eliminar un elemento
boton.remove();
```

---

## 5. ¿Cómo agregar un evento a una etiqueta?

**Explicación:** Los eventos permiten ejecutar código cuando el usuario hace algo: hace clic, escribe, mueve el mouse, envía un formulario, etc. La forma recomendada es `addEventListener` porque permite agregar múltiples eventos al mismo elemento sin sobreescribir los anteriores. Evita poner eventos directo en el HTML (`onclick="..."`) porque mezcla lógica con estructura.

```javascript
const boton = document.getElementById("btn");
const input = document.getElementById("campo");

// Evento de clic
boton.addEventListener("click", () => {
  console.log("Boton presionado");
});

// Evento al escribir
input.addEventListener("input", (evento) => {
  console.log("Valor actual:", evento.target.value);
});

// Evento al enviar formulario
const formulario = document.getElementById("form");
formulario.addEventListener("submit", (evento) => {
  evento.preventDefault(); // evita que recargue la página
  console.log("Formulario enviado");
});

// Otros eventos comunes
boton.addEventListener("mouseover", () => console.log("Mouse encima"));
boton.addEventListener("mouseout",  () => console.log("Mouse fuera"));
```

---

## 6. ¿Qué es un array y sus métodos más usados?

**Explicación:** Un array es una lista ordenada de valores. JavaScript tiene métodos muy útiles para trabajar con arrays sin usar ciclos manuales. Los más importantes son `map` (transforma cada elemento), `filter` (filtra según condición), `find` (encuentra el primero que cumpla), `reduce` (acumula un resultado) y `forEach` (recorre sin retornar nada).

```javascript
const productos = [
  { nombre: "Laptop",  precio: 1000 },
  { nombre: "Mouse",   precio: 25   },
  { nombre: "Teclado", precio: 60   }
];

// map → retorna un nuevo array transformado
const nombres = productos.map(p => p.nombre);
// ["Laptop", "Mouse", "Teclado"]

// filter → retorna solo los que cumplen la condición
const caros = productos.filter(p => p.precio > 50);
// [{ Laptop... }, { Teclado... }]

// find → retorna el primer elemento que coincida
const mouse = productos.find(p => p.nombre === "Mouse");
// { nombre: "Mouse", precio: 25 }

// reduce → acumula un valor
const total = productos.reduce((acc, p) => acc + p.precio, 0);
// 1085

// forEach → solo recorre, no retorna nada
productos.forEach(p => console.log(p.nombre));
```

---

## 7. ¿Qué es un objeto en JavaScript?

**Explicación:** Un objeto es una colección de pares clave-valor. Es la estructura de datos más usada en JavaScript. Puede contener cualquier tipo de valor incluyendo funciones, que en ese contexto se llaman métodos. `this` dentro de un método hace referencia al mismo objeto.

```javascript
const usuario = {
  nombre: "Luis",
  edad:   30,
  activo: true,

  saludar() {
    return `Hola, soy ${this.nombre}`;
  }
};

// Acceder a propiedades
console.log(usuario.nombre);        // Luis
console.log(usuario["edad"]);       // 30
console.log(usuario.saludar());     // Hola, soy Luis

// Agregar o modificar propiedades
usuario.email = "luis@mail.com";
usuario.edad  = 31;

// Destructuring → extraer propiedades en variables
const { nombre, edad } = usuario;
console.log(nombre, edad);          // Luis 31
```

---

## 8. ¿Qué es una Promesa y `async/await`?

**Explicación:** JavaScript es asíncrono, lo que significa que puede iniciar una tarea larga (como pedir datos a una API) y seguir ejecutando otras cosas mientras espera. Una Promesa representa ese resultado futuro, puede resolverse con éxito o fallar. `async/await` es una sintaxis más limpia para manejar promesas, hace que el código asíncrono se lea como si fuera síncrono.

```javascript
// Promesa básica
const promesa = new Promise((resolve, reject) => {
  const exito = true;
  if (exito) resolve("Datos obtenidos");
  else       reject("Algo falló");
});

promesa
  .then(resultado => console.log(resultado))  // Datos obtenidos
  .catch(error    => console.error(error));

// async/await → más legible
async function obtenerUsuario(id) {
  try {
    const respuesta = await fetch(`https://api.ejemplo.com/usuarios/${id}`);
    const datos     = await respuesta.json();
    console.log(datos);
  } catch (error) {
    console.error("Error al obtener usuario:", error);
  }
}

obtenerUsuario(1);
```

---

## 9. ¿Qué es el Event Loop?

**Explicación:** JavaScript es de un solo hilo, solo puede hacer una cosa a la vez. El Event Loop es el mecanismo que le permite manejar operaciones asíncronas sin bloquearse. Cuando una tarea asíncrona termina (como un fetch o un setTimeout), su callback se pone en una cola. El Event Loop revisa esa cola cuando el hilo principal está libre y la ejecuta.

```javascript
console.log("1 - inicio");

setTimeout(() => {
  console.log("2 - timeout");
}, 0); // aunque sea 0ms, va a la cola

Promise.resolve().then(() => {
  console.log("3 - promesa");
});

console.log("4 - fin");

// Salida:
// 1 - inicio
// 4 - fin
// 3 - promesa   → las promesas tienen prioridad sobre setTimeout
// 2 - timeout
```

---

## 10. ¿Qué es destructuring y spread?

**Explicación:** Destructuring permite extraer valores de arrays u objetos en variables de forma directa y limpia. Spread (`...`) permite expandir un array u objeto dentro de otro, es muy usado para copiar o combinar sin mutar el original.

```javascript
// Destructuring de objeto
const { nombre, email } = usuario;

// Destructuring de array
const [primero, segundo, ...resto] = [10, 20, 30, 40];
// primero = 10, segundo = 20, resto = [30, 40]

// Destructuring en parámetros de función
function mostrar({ nombre, edad }) {
  return `${nombre} tiene ${edad} años`;
}

// Spread en arrays
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const combinado = [...arr1, ...arr2]; // [1, 2, 3, 4, 5, 6]

// Spread en objetos → copia sin mutar el original
const base    = { nombre: "Ana", edad: 25 };
const updated = { ...base, edad: 26 };
// base sigue siendo { nombre: "Ana", edad: 25 }
```

---
