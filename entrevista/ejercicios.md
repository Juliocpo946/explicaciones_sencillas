# Ejercicios Habituales de Entrevista

---

## 1. FizzBuzz
El más clásico de todos. Imprime números del 1 al 20, pero si es divisible por 3 imprime "Fizz", por 5 "Buzz", por ambos "FizzBuzz".

**JavaScript**
```javascript
for (let i = 1; i <= 20; i++) {
  if (i % 3 === 0 && i % 5 === 0) console.log("FizzBuzz");
  else if (i % 3 === 0) console.log("Fizz");
  else if (i % 5 === 0) console.log("Buzz");
  else console.log(i);
}
```

**TypeScript**
```typescript
for (let i: number = 1; i <= 20; i++) {
  if (i % 3 === 0 && i % 5 === 0) console.log("FizzBuzz");
  else if (i % 3 === 0) console.log("Fizz");
  else if (i % 5 === 0) console.log("Buzz");
  else console.log(i);
}
```

**PHP**
```php
for ($i = 1; $i <= 20; $i++) {
  if ($i % 3 === 0 && $i % 5 === 0) echo "FizzBuzz\n";
  elseif ($i % 3 === 0) echo "Fizz\n";
  elseif ($i % 5 === 0) echo "Buzz\n";
  else echo $i . "\n";
}
```

---

## 2. Invertir un string
Dado un string, retornarlo al revés.

**JavaScript**
```javascript
function invertir(str) {
  return str.split("").reverse().join("");
}

console.log(invertir("hola")); // "aloh"
```

**TypeScript**
```typescript
function invertir(str: string): string {
  return str.split("").reverse().join("");
}

console.log(invertir("hola")); // "aloh"
```

**PHP**
```php
function invertir(string $str): string {
  return strrev($str);
}

echo invertir("hola"); // "aloh"
```

---

## 3. Verificar si un string es palíndromo
Un palíndromo se lee igual al derecho y al revés. Ejemplo: "ana", "reconocer".

**JavaScript**
```javascript
function esPalindromo(str) {
  const limpio   = str.toLowerCase();
  const invertido = limpio.split("").reverse().join("");
  return limpio === invertido;
}

console.log(esPalindromo("Ana"));       // true
console.log(esPalindromo("reconocer")); // true
console.log(esPalindromo("hola"));      // false
```

**TypeScript**
```typescript
function esPalindromo(str: string): boolean {
  const limpio    = str.toLowerCase();
  const invertido = limpio.split("").reverse().join("");
  return limpio === invertido;
}
```

**PHP**
```php
function esPalindromo(string $str): bool {
  $limpio = strtolower($str);
  return $limpio === strrev($limpio);
}

var_dump(esPalindromo("reconocer")); // true
var_dump(esPalindromo("hola"));      // false
```

---

## 4. Encontrar el número mayor de un array

**JavaScript**
```javascript
function mayorNumero(nums) {
  return Math.max(...nums);
}

console.log(mayorNumero([3, 7, 1, 9, 4])); // 9
```

**TypeScript**
```typescript
function mayorNumero(nums: number[]): number {
  return Math.max(...nums);
}
```

**PHP**
```php
function mayorNumero(array $nums): int|float {
  return max($nums);
}

echo mayorNumero([3, 7, 1, 9, 4]); // 9
```

---

## 5. Contar cuántas veces aparece un elemento en un array

**JavaScript**
```javascript
function contarOcurrencias(arr, elemento) {
  return arr.filter(item => item === elemento).length;
}

console.log(contarOcurrencias([1, 2, 2, 3, 2], 2)); // 3
```

**TypeScript**
```typescript
function contarOcurrencias<T>(arr: T[], elemento: T): number {
  return arr.filter(item => item === elemento).length;
}
```

**PHP**
```php
function contarOcurrencias(array $arr, mixed $elemento): int {
  return count(array_filter($arr, fn($item) => $item === $elemento));
}

echo contarOcurrencias([1, 2, 2, 3, 2], 2); // 3
```

---

## 6. Eliminar duplicados de un array

**JavaScript**
```javascript
function sinDuplicados(arr) {
  return [...new Set(arr)];
}

console.log(sinDuplicados([1, 2, 2, 3, 3, 4])); // [1, 2, 3, 4]
```

**TypeScript**
```typescript
function sinDuplicados<T>(arr: T[]): T[] {
  return [...new Set(arr)];
}
```

**PHP**
```php
function sinDuplicados(array $arr): array {
  return array_values(array_unique($arr));
}

print_r(sinDuplicados([1, 2, 2, 3, 3, 4])); // [1, 2, 3, 4]
```

---

## 7. Sumar todos los números de un array

**JavaScript**
```javascript
function sumarArray(nums) {
  return nums.reduce((acc, num) => acc + num, 0);
}

console.log(sumarArray([1, 2, 3, 4, 5])); // 15
```

**TypeScript**
```typescript
function sumarArray(nums: number[]): number {
  return nums.reduce((acc, num) => acc + num, 0);
}
```

**PHP**
```php
function sumarArray(array $nums): int|float {
  return array_sum($nums);
}

echo sumarArray([1, 2, 3, 4, 5]); // 15
```

---

## 8. Verificar si un número es primo

**JavaScript**
```javascript
function esPrimo(n) {
  if (n < 2) return false;
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return false;
  }
  return true;
}

console.log(esPrimo(7));  // true
console.log(esPrimo(10)); // false
```

**TypeScript**
```typescript
function esPrimo(n: number): boolean {
  if (n < 2) return false;
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return false;
  }
  return true;
}
```

**PHP**
```php
function esPrimo(int $n): bool {
  if ($n < 2) return false;
  for ($i = 2; $i <= sqrt($n); $i++) {
    if ($n % $i === 0) return false;
  }
  return true;
}

var_dump(esPrimo(7));  // true
var_dump(esPrimo(10)); // false
```

---

## 9. Factorial de un número

**JavaScript**
```javascript
function factorial(n) {
  if (n <= 1) return 1;
  return n * factorial(n - 1);
}

console.log(factorial(5)); // 120
```

**TypeScript**
```typescript
function factorial(n: number): number {
  if (n <= 1) return 1;
  return n * factorial(n - 1);
}
```

**PHP**
```php
function factorial(int $n): int {
  if ($n <= 1) return 1;
  return $n * factorial($n - 1);
}

echo factorial(5); // 120
```

---

## 10. Ordenar array de objetos por propiedad

**JavaScript**
```javascript
const productos = [
  { nombre: "Mouse",   precio: 25  },
  { nombre: "Laptop",  precio: 999 },
  { nombre: "Teclado", precio: 60  }
];

const ordenados = productos.sort((a, b) => a.precio - b.precio);
console.log(ordenados);
// Mouse 25, Teclado 60, Laptop 999
```

**TypeScript**
```typescript
interface Producto {
  nombre: string;
  precio: number;
}

function ordenarPorPrecio(productos: Producto[]): Producto[] {
  return [...productos].sort((a, b) => a.precio - b.precio);
}
```

**PHP**
```php
$productos = [
  ["nombre" => "Mouse",   "precio" => 25],
  ["nombre" => "Laptop",  "precio" => 999],
  ["nombre" => "Teclado", "precio" => 60]
];

usort($productos, fn($a, $b) => $a["precio"] - $b["precio"]);
print_r($productos);
```

---

## 11. HTML + CSS — Tarjeta de perfil
Ejercicio visual muy común: construir un componente con solo HTML y CSS.

**HTML**
```html
<div class="tarjeta">
  <img src="avatar.jpg" alt="Foto de perfil" class="avatar">
  <div class="info">
    <h2 class="nombre">Ana García</h2>
    <p class="cargo">Desarrolladora Frontend</p>
    <p class="descripcion">Apasionada por crear interfaces limpias y accesibles.</p>
  </div>
  <div class="acciones">
    <button class="btn-primario">Seguir</button>
    <button class="btn-secundario">Mensaje</button>
  </div>
</div>
```

**CSS**
```css
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tarjeta {
  width: 300px;
  background: #1a1a2e;
  border-radius: 12px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  color: #e0e0e0;
}

.avatar {
  width: 90px;
  height: 90px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid #16213e;
}

.info {
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.nombre      { font-size: 18px; font-weight: bold; }
.cargo       { font-size: 13px; color: #888; }
.descripcion { font-size: 14px; line-height: 1.5; }

.acciones {
  display: flex;
  gap: 10px;
}

.btn-primario,
.btn-secundario {
  padding: 8px 20px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  transition: opacity 0.2s ease;
}

.btn-primario   { background: #16213e; color: #e0e0e0; }
.btn-secundario { background: transparent; color: #e0e0e0; border: 1px solid #444; }

.btn-primario:hover,
.btn-secundario:hover { opacity: 0.8; }
```

---

## 12. HTML + CSS — Formulario responsivo

**HTML**
```html
<form class="formulario" action="/enviar" method="POST">
  <h2 class="titulo-form">Contáctanos</h2>

  <div class="campo">
    <label for="nombre">Nombre</label>
    <input type="text" id="nombre" name="nombre" placeholder="Tu nombre" required>
  </div>

  <div class="campo">
    <label for="email">Email</label>
    <input type="email" id="email" name="email" placeholder="tu@email.com" required>
  </div>

  <div class="campo">
    <label for="mensaje">Mensaje</label>
    <textarea id="mensaje" name="mensaje" rows="4" placeholder="Escribe aquí..."></textarea>
  </div>

  <button type="submit" class="btn-enviar">Enviar mensaje</button>
</form>
```

**CSS**
```css
.formulario {
  width: 100%;
  max-width: 480px;
  margin: 0 auto;
  background: #1a1a2e;
  padding: 32px;
  border-radius: 12px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.titulo-form {
  color: #e0e0e0;
  font-size: 20px;
  text-align: center;
}

.campo {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.campo label {
  color: #aaa;
  font-size: 13px;
}

.campo input,
.campo textarea {
  background: #16213e;
  border: 1px solid #333;
  border-radius: 6px;
  padding: 10px 14px;
  color: #e0e0e0;
  font-size: 14px;
  outline: none;
  transition: border-color 0.2s ease;
  resize: none;
}

.campo input:focus,
.campo textarea:focus {
  border-color: #4a90e2;
}

.btn-enviar {
  background: #16213e;
  color: #e0e0e0;
  border: none;
  border-radius: 6px;
  padding: 12px;
  font-size: 15px;
  cursor: pointer;
  transition: opacity 0.2s ease;
}

.btn-enviar:hover { opacity: 0.8; }

@media (max-width: 480px) {
  .formulario { padding: 20px; }
}
```
