# Guía de Respuestas para Entrevista

---

## 1. ¿Qué es HTML Semántico?

Es usar etiquetas que describen el **significado** del contenido, no solo su apariencia.

```html
<!-- No semántico -->
<div id="nav">...</div>
<div id="content">...</div>

<!-- Semántico -->
<header>...</header>
<nav>...</nav>
<main>...</main>
<article>...</article>
<footer>...</footer>
```

**Respuesta corta:** *"Son etiquetas que le dan significado al contenido, mejoran el SEO y la accesibilidad."*

---

## 2. Formulario en HTML solo con etiquetas

```html
<form action="/enviar" method="POST">
  <label for="nombre">Nombre:</label>
  <input type="text" id="nombre" name="nombre" required>

  <label for="email">Email:</label>
  <input type="email" id="email" name="email" required>

  <label for="mensaje">Mensaje:</label>
  <textarea id="mensaje" name="mensaje"></textarea>

  <button type="submit">Enviar</button>
</form>
```

---

## 3. Modelo de Caja en CSS (Box Model)

Todo elemento HTML es una caja con 4 capas:

```
┌─────────────────────────┐
│        MARGIN           │  ← Espacio externo
│  ┌───────────────────┐  │
│  │     BORDER        │  │  ← Borde
│  │  ┌─────────────┐  │  │
│  │  │   PADDING   │  │  │  ← Espacio interno
│  │  │  ┌───────┐  │  │  │
│  │  │  │CONTENT│  │  │  │  ← Contenido
│  │  │  └───────┘  │  │  │
│  │  └─────────────┘  │  │
│  └───────────────────┘  │
└─────────────────────────┘
```

```css
div {
  width: 200px;
  padding: 10px;
  border: 2px solid #333;
  margin: 20px;
  box-sizing: border-box; /* el padding no aumenta el tamaño total */
}
```

---

## 4. Cómo centrar un `div` en HTML/CSS

```css
/* Forma moderna con Flexbox */
.contenedor {
  display: flex;
  justify-content: center;  /* horizontal */
  align-items: center;      /* vertical */
  height: 100vh;
}

/* Con margin auto (solo horizontal) */
.caja {
  width: 300px;
  margin: 0 auto;
}
```

---

## 5. ¿Qué es el Diseño Responsivo?

Que el sitio **se adapte a cualquier tamaño de pantalla** (móvil, tablet, desktop).

```css
/* Media queries */
.contenedor {
  width: 100%;
}

@media (min-width: 768px) {
  .contenedor {
    width: 750px;
  }
}

@media (min-width: 1200px) {
  .contenedor {
    width: 1100px;
  }
}
```

**Respuesta corta:** *"Diseño que se adapta al dispositivo usando media queries, unidades relativas y layouts flexibles."*

---

## 6. ¿Qué es el DOM en JavaScript?

*(Nota: probablemente preguntarán DOM, no "dump")*

El **DOM (Document Object Model)** es la representación en memoria del HTML como un árbol de objetos que JavaScript puede manipular.

```javascript
// Seleccionar elemento
const titulo = document.getElementById("titulo");

// Modificar contenido
titulo.textContent = "Nuevo texto";

// Modificar estilo
titulo.style.color = "blue";

// Crear y agregar elemento
const parrafo = document.createElement("p");
parrafo.textContent = "Hola mundo";
document.body.appendChild(parrafo);
```

---

## 7. Cómo poner un evento a una etiqueta

```javascript
// Forma recomendada: addEventListener
const boton = document.getElementById("btn");

boton.addEventListener("click", function() {
  alert("Clic detectado");
});

// Con función flecha
boton.addEventListener("mouseover", () => {
  console.log("Mouse encima");
});

// Directo en HTML (menos recomendado)
// <button onclick="miFuncion()">Click</button>
```

---

## 8. ¿Qué es la Programación Orientada a Objetos (POO)?

Paradigma que organiza el código en **objetos** que combinan datos (atributos) y comportamiento (métodos).

**4 pilares:**
- **Encapsulamiento** — ocultar datos internos
- **Herencia** — una clase extiende otra
- **Polimorfismo** — mismo método, diferente comportamiento
- **Abstracción** — exponer solo lo necesario

```javascript
class Animal {
  constructor(nombre) {
    this.nombre = nombre;
  }
  hablar() {
    console.log(`${this.nombre} hace un sonido`);
  }
}

class Perro extends Animal {
  hablar() {
    console.log(`${this.nombre} ladra`); // polimorfismo
  }
}

const perro = new Perro("Rex");
perro.hablar(); // Rex ladra
```

---

## 9. ¿Para qué sirve una Clase?

Es una **plantilla** para crear objetos con la misma estructura.

```javascript
class Usuario {
  constructor(nombre, email) {
    this.nombre = nombre;
    this.email = email;
  }

  saludar() {
    return `Hola, soy ${this.nombre}`;
  }
}

const u1 = new Usuario("Ana", "ana@mail.com");
const u2 = new Usuario("Luis", "luis@mail.com");

console.log(u1.saludar()); // Hola, soy Ana
```

---

## 10. ¿Has trabajado con APIs? ¿Cómo se estructuran?

**Respuesta sugerida:** *"Sí, con APIs REST. Se consumen mediante HTTP usando métodos GET, POST, PUT, DELETE. La respuesta generalmente viene en JSON."*

```javascript
// Consumir una API con fetch (GET)
async function obtenerUsuarios() {
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/users");
    const datos = await response.json();
    console.log(datos);
  } catch (error) {
    console.error("Error al obtener datos:", error);
  }
}

// POST - enviar datos
async function crearUsuario(usuario) {
  const response = await fetch("https://api.ejemplo.com/usuarios", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(usuario)
  });
  return await response.json();
}
```

**Estructura de una API REST:**
```
GET    /usuarios        → obtener todos
GET    /usuarios/1      → obtener uno
POST   /usuarios        → crear
PUT    /usuarios/1      → actualizar
DELETE /usuarios/1      → eliminar
```

---
