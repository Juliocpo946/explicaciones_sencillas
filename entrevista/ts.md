# TypeScript — Explicación + Ejemplos

---

## 1. ¿Qué es TypeScript?

**Explicación:** TypeScript es JavaScript con tipado estático. Lo desarrolló Microsoft y es un superset de JavaScript, lo que significa que todo JavaScript válido es TypeScript válido. La diferencia es que TypeScript te obliga a definir los tipos de datos, lo que permite detectar errores antes de ejecutar el código, directamente en el editor. Al final TypeScript se compila a JavaScript normal porque los navegadores no lo entienden directamente.

```typescript
// JavaScript → sin tipos, el error aparece en ejecución
function sumar(a, b) {
  return a + b;
}
sumar(5, "3"); // "53" → bug silencioso

// TypeScript → el error aparece antes de ejecutar
function sumar(a: number, b: number): number {
  return a + b;
}
sumar(5, "3"); // Error en el editor: "3" no es number
```

---

## 2. ¿Qué son los tipos básicos?

**Explicación:** TypeScript tiene tipos primitivos que se asignan con `:` después del nombre de la variable. Si asignas un valor al declarar, TypeScript puede inferir el tipo automáticamente sin que lo escribas, pero es buena práctica escribirlo explícitamente en parámetros y retornos de funciones.

```typescript
// Tipos primitivos
let nombre:  string  = "Ana";
let edad:    number  = 25;
let activo:  boolean = true;
let vacio:   null    = null;
let nada:    undefined = undefined;

// TypeScript infiere el tipo automáticamente
let ciudad = "Tuxtla"; // TypeScript sabe que es string
// ciudad = 123;       // Error → no puedes asignar number a string

// Arrays
let numeros:  number[]  = [1, 2, 3];
let nombres:  string[]  = ["Ana", "Luis"];
let mixto:    (string | number)[] = ["Ana", 25]; // union type

// any → desactiva el tipado, evitar en lo posible
let dato: any = "puede ser cualquier cosa";
dato = 123;    // permitido, pero pierdes los beneficios de TS
```

---

## 3. ¿Qué es una Interface?

**Explicación:** Una interface define la forma que debe tener un objeto, es decir, qué propiedades debe tener y de qué tipo. No genera código JavaScript al compilar, solo existe en tiempo de desarrollo para validar estructuras. Si una propiedad lleva `?` es opcional. Es la forma más usada para tipar objetos en TypeScript.

```typescript
interface Usuario {
  id:       number;
  nombre:   string;
  email:    string;
  edad?:    number;   // opcional
  readonly rol: string; // no se puede modificar después de asignar
}

// El objeto debe cumplir la interface
const usuario: Usuario = {
  id:     1,
  nombre: "Ana",
  email:  "ana@mail.com",
  rol:    "admin"
  // edad es opcional, no es necesario incluirla
};

// usuario.rol = "user"; // Error → es readonly

// Interface en función
function mostrarUsuario(u: Usuario): string {
  return `${u.nombre} (${u.email})`;
}
```

---

## 4. ¿Qué es un Type?

**Explicación:** `type` es similar a interface pero más flexible. Puede definir objetos, uniones, intersecciones y tipos complejos. La diferencia práctica con interface es que `type` no se puede extender con `extends` de la misma forma y no se puede reabrir para agregar propiedades. En la comunidad se usa interface para objetos y type para todo lo demás.

```typescript
// Type para objeto → similar a interface
type Producto = {
  nombre: string;
  precio: number;
};

// Union type → puede ser uno u otro
type ID = number | string;
let userId: ID = 123;
userId = "abc-456"; // también válido

// Literal type → solo valores específicos
type Rol      = "admin" | "editor" | "viewer";
type Direccion = "norte" | "sur" | "este" | "oeste";

let rolUsuario: Rol = "admin";
// rolUsuario = "superadmin"; // Error → no está en el tipo

// Intersection type → combina dos tipos
type Admin = Usuario & { permisos: string[] };
```

---

## 5. ¿Diferencia entre Interface y Type?

**Explicación:** Ambos definen estructuras pero con diferencias clave. Interface puede extenderse y reabrirse (declarar la misma interface dos veces las fusiona). Type es más expresivo para unions, intersecciones y tipos complejos. En la práctica para objetos usa interface, para todo lo demás usa type.

```typescript
// Interface → se puede extender y reabrir
interface Animal {
  nombre: string;
}

interface Animal {
  edad: number; // se fusiona con la anterior
}

interface Perro extends Animal {
  raza: string;
}

const perro: Perro = {
  nombre: "Rex",
  edad:   3,
  raza:   "Labrador"
};

// Type → no se puede reabrir, pero soporta más casos
type Resultado = "exito" | "error" | "pendiente";
type Respuesta = { data: unknown } & { status: Resultado };
```

---

## 6. ¿Cómo tipar funciones?

**Explicación:** En TypeScript se tipan los parámetros y el valor de retorno. Si una función no retorna nada se usa `void`. Si puede retornar null o undefined se declara explícitamente. También puedes definir el tipo de una función completa como variable.

```typescript
// Parámetros y retorno tipados
function dividir(a: number, b: number): number {
  return a / b;
}

// Función que no retorna nada
function log(mensaje: string): void {
  console.error(mensaje);
}

// Retorno que puede ser null
function buscarUsuario(id: number): Usuario | null {
  // lógica de búsqueda
  return null;
}

// Parámetro opcional y con valor por defecto
function saludar(nombre: string, formal: boolean = false): string {
  return formal ? `Buenos días, ${nombre}` : `Hola, ${nombre}`;
}

// Tipo de función como variable
type Operacion = (a: number, b: number) => number;

const multiplicar: Operacion = (a, b) => a * b;
const restar:      Operacion = (a, b) => a - b;
```

---

## 7. ¿Qué son los Generics?

**Explicación:** Los generics permiten crear funciones, clases o interfaces que funcionan con cualquier tipo sin perder el tipado. En lugar de usar `any` (que desactiva el tipado), usas una variable de tipo `<T>` que TypeScript reemplaza con el tipo real cuando la usas. Es muy usado en funciones de utilidad y en respuestas de APIs.

```typescript
// Sin generics → pierdes el tipo
function primerElemento(arr: any[]): any {
  return arr[0];
}

// Con generics → TypeScript sabe el tipo de retorno
function primerElemento<T>(arr: T[]): T {
  return arr[0];
}

const num    = primerElemento([1, 2, 3]);       // TypeScript sabe: number
const nombre = primerElemento(["Ana", "Luis"]); // TypeScript sabe: string

// Generic en interface → muy usado para respuestas de API
interface Respuesta<T> {
  data:    T;
  status:  number;
  mensaje: string;
}

const respuestaUsuario: Respuesta<Usuario> = {
  data:    { id: 1, nombre: "Ana", email: "ana@mail.com", rol: "admin" },
  status:  200,
  mensaje: "OK"
};
```

---

## 8. ¿Qué es Enum?

**Explicación:** Un enum es un conjunto de constantes con nombre. Hace el código más legible porque en lugar de usar números o strings hardcodeados usas nombres descriptivos. TypeScript tiene enums numéricos (por defecto) y de string. En la práctica los de string son más recomendados porque su valor es legible en tiempo de ejecución.

```typescript
// Enum numérico → valores 0, 1, 2 automáticamente
enum Estado {
  Pendiente,   // 0
  Activo,      // 1
  Inactivo     // 2
}

// Enum de string → recomendado, valor legible
enum Rol {
  Admin   = "ADMIN",
  Editor  = "EDITOR",
  Viewer  = "VIEWER"
}

// Uso
interface Cuenta {
  nombre: string;
  rol:    Rol;
  estado: Estado;
}

const cuenta: Cuenta = {
  nombre: "Ana",
  rol:    Rol.Admin,
  estado: Estado.Activo
};

// Comparación
if (cuenta.rol === Rol.Admin) {
  console.log("Tiene acceso total");
}
```

---

## 9. ¿Cómo tipar una clase?

**Explicación:** Las clases en TypeScript tienen modificadores de acceso: `public` (accesible desde cualquier lado), `private` (solo dentro de la clase), `protected` (dentro de la clase y subclases). También puedes implementar interfaces con `implements` para garantizar que la clase tenga cierta forma.

```typescript
interface Serializable {
  serializar(): string;
}

class Producto implements Serializable {
  public  nombre:   string;
  private precio:   number;
  protected stock:  number;

  constructor(nombre: string, precio: number, stock: number) {
    this.nombre = nombre;
    this.precio = precio;
    this.stock  = stock;
  }

  public getPrecio(): number {
    return this.precio;
  }

  public serializar(): string {
    return JSON.stringify({ nombre: this.nombre, precio: this.precio });
  }
}

class ProductoDigital extends Producto {
  private url: string;

  constructor(nombre: string, precio: number, url: string) {
    super(nombre, precio, 0);
    this.url = url;
  }

  // Puede acceder a stock porque es protected
  verificarStock(): boolean {
    return this.stock > 0;
  }
}
```

---

## 10. ¿Cómo tipar una respuesta de API?

**Explicación:** Uno de los usos más comunes de TypeScript en el mundo real es tipar las respuestas de APIs. Esto garantiza que cuando consumes datos externos, tu código sabe exactamente qué estructura tiene la respuesta y el editor te avisa si intentas acceder a una propiedad que no existe.

```typescript
// Defines la forma de los datos que esperas
interface Post {
  id:     number;
  title:  string;
  body:   string;
  userId: number;
}

// Función tipada para consumir la API
async function obtenerPost(id: number): Promise<Post | null> {
  try {
    const respuesta = await fetch(`https://jsonplaceholder.typicode.com/posts/${id}`);

    if (!respuesta.ok) return null;

    const datos: Post = await respuesta.json();
    return datos;

  } catch (error) {
    console.error(`[${new Date().toISOString()}] [API] [ERROR] Fallo al obtener post ${id}`);
    return null;
  }
}

// Uso con verificación de null
async function main() {
  const post = await obtenerPost(1);

  if (post === null) return;

  console.log(post.title); // TypeScript sabe que es string
  // console.log(post.xyz); // Error → xyz no existe en Post
}
```

---
