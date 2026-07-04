# Lección 08 - La clase String en Java 17

# Objetivo

Al finalizar esta parte serás capaz de:

* Comprender qué es un `String`.
* Entender por qué `String` es una clase y no un tipo primitivo.
* Conocer las diferentes formas de crear un `String`.
* Comprender cómo Java almacena los textos.
* Entender qué significa que un `String` sea inmutable.

---

# Introducción

Hasta ahora hemos trabajado con distintos tipos de datos.

Por ejemplo:

```java
int age = 20;
double salary = 15000.50;
char grade = 'A';
boolean active = true;
```

Todos ellos permiten almacenar un tipo específico de información.

Pero...

¿Cómo almacenamos texto?

Por ejemplo:

* Un nombre.
* Una dirección.
* Un correo electrónico.
* Un mensaje.
* Una contraseña.

Para eso Java utiliza la clase **String**.

---

# ¿Qué es String?

`String` es una clase incluida en Java que permite almacenar y manipular cadenas de caracteres.

Una cadena de caracteres es simplemente una secuencia de letras, números, símbolos o espacios.

Por ejemplo:

```text
Hola
```

```text
Juan Pérez
```

```text
[email protected]
```

```text
Java 17
```

Todos ellos son cadenas de texto.

---

# ¿Por qué String empieza con mayúscula?

Observa este código.

```java
String name = "Juan";
```

Ahora compáralo con este.

```java
int age = 20;
```

Muchos principiantes preguntan:

> ¿Por qué `String` comienza con mayúscula e `int` no?

La respuesta es sencilla.

Porque **`int` es un tipo de dato primitivo**, mientras que **`String` es una clase**.

En Java existe una convención muy importante.

Los nombres de las clases siempre comienzan con mayúscula.

Por ejemplo:

```java
String
Scanner
Integer
Double
ArrayList
```

Mientras que los tipos primitivos se escriben completamente en minúsculas.

```java
int
double
char
boolean
long
float
short
byte
```

---

# ¿Qué diferencia existe entre una clase y un tipo primitivo?

Los tipos primitivos son los datos más básicos que entiende Java.

Ejemplos:

```java
int
double
boolean
char
```

Cada uno almacena un único valor.

En cambio, una clase puede almacenar datos y además ofrecer funcionalidades.

Por ejemplo:

```java
String name = "Juan";
```

Ese objeto puede hacer muchas cosas.

```java
System.out.println(name.length());
System.out.println(name.toUpperCase());
System.out.println(name.toLowerCase());
```

Los tipos primitivos no tienen métodos.

Por ejemplo, esto no existe.

```java
int age = 20;

age.length();
```

Porque un `int` únicamente almacena un número.

Un `String`, además de almacenar texto, ofrece múltiples operaciones para trabajar con él.

---

# ¿Qué es una cadena de caracteres?

Imagina la palabra:

```text
Java
```

Aunque nosotros vemos una sola palabra, Java realmente la interpreta como varios caracteres.

```text
J
a
v
a
```

Podemos representarlo como una colección ordenada de caracteres.

```text
+-----+-----+-----+-----+
|  J  |  a  |  v  |  a  |
+-----+-----+-----+-----+
```

Cada posición tiene un índice.

```text
+-----+-----+-----+-----+
|  J  |  a  |  v  |  a  |
+-----+-----+-----+-----+
   0     1     2     3
```

Observa que el primer índice siempre es **0**.

Esto sucede con prácticamente todas las estructuras de datos en Java.

---

# Declarar una variable String

La forma más común es:

```java
String name = "Juan";
```

Analicemos cada parte.

```java
String
```

Indica el tipo de dato.

---

```java
name
```

Es el nombre de la variable.

---

```java
=
```

Es el operador de asignación.

---

```java
"Juan"
```

Es un literal de tipo String.

Todo texto debe escribirse entre comillas dobles.

---

# ¿Qué ocurre si olvidamos las comillas?

Incorrecto.

```java
String name = Juan;
```

Java intentará buscar una variable llamada `Juan`.

Como no existe, aparecerá un error de compilación.

Correcto.

```java
String name = "Juan";
```

---

# Crear un String vacío

En ocasiones necesitamos crear una cadena sin contenido.

```java
String text = "";
```

Observa que existen dos comillas.

Entre ellas no hay ningún carácter.

Eso representa una cadena vacía.

No significa que la variable sea `null`.

Simplemente contiene un texto cuya longitud es cero.

---

# ¿Puedo guardar números dentro de un String?

Sí.

```java
String age = "20";
```

Pero hay una diferencia muy importante.

Esto:

```java
20
```

es un número.

Mientras que esto:

```java
"20"
```

es texto.

Aunque visualmente parezcan iguales, Java los trata de forma completamente distinta.

Por ejemplo.

```java
int number = 20;

System.out.println(number + 5);
```

Resultado.

```text
25
```

Ahora observa.

```java
String number = "20";

System.out.println(number + 5);
```

Resultado.

```text
205
```

¿Por qué?

Porque Java ya no realiza una suma.

Lo que hace es unir ambos textos.

A este proceso se le conoce como **concatenación**.

En la siguiente parte aprenderás este concepto con mucho más detalle.

---

# Formas de crear un String

Existen dos maneras principales.

## Primera forma

Utilizando un literal.

```java
String city = "Veracruz";
```

Es la forma más utilizada y recomendada.

---

## Segunda forma

Utilizando el operador `new`.

```java
String city = new String("Veracruz");
```

Ambas crean un objeto `String`.

Sin embargo, normalmente se recomienda utilizar la primera forma porque es más simple y aprovecha mejor la memoria.

En la siguiente parte aprenderás por qué ocurre esto cuando estudiemos el **String Pool**.
