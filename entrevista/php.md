Tienes razón, voy a rehacerlos con explicación clara + ejemplo. Empezamos con **PHP**.

---

# PHP — Explicación + Ejemplos

---

## 1. ¿Qué es PHP y para qué se usa?

**Explicación:** PHP es un lenguaje que corre en el **servidor**, no en el navegador. Cuando un usuario entra a una página, el servidor ejecuta PHP, genera HTML y lo manda al navegador. Se usa para manejar formularios, conectarse a bases de datos, crear APIs y sistemas web completos.

```php
<?php
  echo "Hola mundo"; // El servidor genera esto y lo manda al navegador
?>
```

---

## 2. ¿Diferencia entre `echo` y `print`?

**Explicación:** Ambos muestran texto, pero `echo` es más rápido porque no retorna ningún valor. `print` retorna `1`, lo que permite usarlo dentro de expresiones, aunque en práctica casi siempre se usa `echo`.

```php
echo "Hola";        // Solo imprime, sin valor de retorno
print "Hola";       // Imprime y retorna 1

// Caso donde print tiene sentido
$resultado = print "Texto";
echo $resultado;    // 1
```

---

## 3. ¿Qué son las variables en PHP?

**Explicación:** En PHP toda variable empieza con `$`. Son de tipado dinámico, lo que significa que no declaras el tipo, PHP lo detecta según el valor que le asignes.

```php
$nombre = "Ana";     // string
$edad   = 25;        // integer
$precio = 9.99;      // float
$activo = true;      // boolean
$vacio  = null;      // null
```

---

## 4. ¿Diferencia entre `==` y `===`?

**Explicación:** `==` solo compara el **valor**, PHP puede convertir tipos para que coincidan. `===` compara **valor y tipo** al mismo tiempo, es más estricto y seguro. En entrevistas siempre recomienda `===` para evitar bugs inesperados.

```php
0 == "0"    // true  → PHP convierte "0" a número
0 === "0"   // false → uno es int, otro es string

0 == false  // true  → PHP los trata igual
0 === false // false → tipos distintos
```

---

## 5. ¿Qué es un array en PHP?

**Explicación:** Un array es una estructura que guarda múltiples valores en una sola variable. En PHP hay dos tipos: indexado (posiciones numéricas) y asociativo (clave-valor, como un diccionario).

```php
// Indexado → accedes por posición
$frutas = ["manzana", "pera", "uva"];
echo $frutas[0]; // manzana

// Asociativo → accedes por clave
$usuario = [
  "nombre" => "Luis",
  "email"  => "luis@mail.com",
  "edad"   => 28
];
echo $usuario["nombre"]; // Luis

// Recorrer array
foreach ($usuario as $clave => $valor) {
  echo "$clave: $valor";
}
```

---

## 6. ¿Cómo se hace una función en PHP?

**Explicación:** Las funciones agrupan código reutilizable. Pueden recibir parámetros y retornar valores. PHP también permite tipar los parámetros y el retorno para mayor seguridad.

```php
// Función básica
function saludar($nombre) {
  return "Hola, " . $nombre;
}

// Con tipos definidos (recomendado)
function sumar(int $a, int $b): int {
  return $a + $b;
}

echo saludar("Ana"); // Hola, Ana
echo sumar(3, 4);    // 7
```

---

## 7. ¿Cómo conectar PHP con una base de datos?

**Explicación:** PDO (PHP Data Objects) es la forma recomendada de conectarse a bases de datos porque funciona con varios motores (MySQL, PostgreSQL, etc.) y protege contra inyección SQL usando consultas preparadas con `?` o `:parametro`.

```php
// Conexión
$conn = new PDO(
  "mysql:host=localhost;dbname=mi_db",
  "root",
  "password"
);

// Consulta segura con parámetro
$stmt = $conn->prepare("SELECT * FROM usuarios WHERE id = ?");
$stmt->execute([1]);
$usuario = $stmt->fetch(PDO::FETCH_ASSOC);

echo $usuario["nombre"];
```

---

## 8. ¿Qué es `$_POST` y `$_GET`?

**Explicación:** Son variables superglobales que PHP usa para recibir datos del usuario. `$_GET` recibe datos desde la URL (visibles), ideal para búsquedas. `$_POST` recibe datos del cuerpo del formulario (no visibles en URL), ideal para contraseñas o datos sensibles.

```php
// URL: pagina.php?nombre=Ana
$nombre = $_GET["nombre"];   // Ana

// Formulario con method="POST"
$email    = $_POST["email"];
$password = $_POST["password"];

// Siempre validar antes de usar
if (!empty($_POST["email"])) {
  $email = htmlspecialchars($_POST["email"]); // evita XSS
}
```

---

## 9. ¿Qué es una clase en PHP?

**Explicación:** Una clase es una plantilla para crear objetos. Define atributos (datos) y métodos (comportamiento). `__construct` es el método que se ejecuta automáticamente al crear un objeto. Los modificadores `public`, `private` y `protected` controlan quién puede acceder a cada parte.

```php
class Producto {
  public string $nombre;
  private float $precio;

  public function __construct(string $nombre, float $precio) {
    $this->nombre = $nombre;
    $this->precio = $precio;
  }

  // Getter para precio (privado, no accesible directo)
  public function getPrecio(): float {
    return $this->precio;
  }

  public function mostrar(): string {
    return "{$this->nombre} cuesta \${$this->precio}";
  }
}

$p = new Producto("Laptop", 999.99);
echo $p->mostrar();       // Laptop cuesta $999.99
echo $p->getPrecio();     // 999.99
```

---

## 10. ¿Diferencia entre `include` y `require`?

**Explicación:** Ambos insertan el contenido de otro archivo PHP. La diferencia está en qué pasa si el archivo no existe. `include` solo lanza una advertencia y el script sigue corriendo. `require` detiene completamente la ejecución, úsalo cuando el archivo sea crítico para que el sistema funcione.

```php
include "config.php";   // Si no existe → advertencia, sigue ejecutando
require "config.php";   // Si no existe → error fatal, se detiene todo

// Versiones _once evitan cargar el mismo archivo dos veces
include_once "funciones.php";
require_once "conexion.php";
```

---
