
# Lección 06 - Estructuras Condicionales

# ¿Qué es una estructura condicional?

Hasta este momento nuestros programas se ejecutaban de principio a fin siguiendo exactamente el mismo camino.

Ejemplo:

```java
System.out.println("Hola");
System.out.println("Bienvenido");
System.out.println("Fin");
```

Siempre ocurrirá lo mismo.

```text
Hola
Bienvenido
Fin
```

Sin importar quién ejecute el programa.

Sin embargo, en la vida real los programas deben tomar decisiones.

Por ejemplo:

* Si el usuario es mayor de edad, permitir el acceso.
* Si la contraseña es correcta, iniciar sesión.
* Si hay productos disponibles, permitir la compra.
* Si la calificación es mayor o igual a 6, aprobar al estudiante.

A este tipo de decisiones se les conoce como **estructuras condicionales**.

---

# ¿Qué significa una condición?

Una condición es una expresión que únicamente puede tener dos resultados.

```text
true
```

o

```text
false
```

No existen otros valores.

Por ejemplo:

```java
10 > 5
```

Resultado

```text
true
```

---

```java
5 > 10
```

Resultado

```text
false
```

---

```java
20 == 20
```

Resultado

```text
true
```

---

Todas estas expresiones producen un valor boolean.

---

# La sentencia if

La estructura más sencilla es `if`.

Sintaxis

```java
if (condición) {

}
```

La palabra reservada `if` significa:

> "Si esta condición es verdadera, ejecuta este bloque de código."

---

## Primer ejemplo

```java
int age = 20;

if (age >= 18) {
    System.out.println("Eres mayor de edad.");
}
```

Paso a paso:

1. Se crea la variable `age`.
2. Se almacena el valor `20`.
3. Java evalúa la condición.

```java
age >= 18
```

Como 20 es mayor que 18:

```text
true
```

Entonces ejecuta:

```java
System.out.println("Eres mayor de edad.");
```

Salida

```text
Eres mayor de edad.
```

---

## ¿Qué ocurre si la condición es falsa?

```java
int age = 15;

if (age >= 18) {
    System.out.println("Puedes votar.");
}
```

Java evalúa:

```java
15 >= 18
```

Resultado

```text
false
```

Como la condición es falsa, el bloque de código no se ejecuta.

Salida

```text
(No aparece ningún mensaje)
```

---

# Uso de llaves

Aunque Java permite escribir un `if` con una sola instrucción sin llaves:

```java
if (age >= 18)
    System.out.println("Mayor de edad");
```

Se recomienda utilizar siempre llaves.

Correcto

```java
if (age >= 18) {
    System.out.println("Mayor de edad");
}
```

Esto mejora la legibilidad y evita errores cuando se agregan nuevas instrucciones.

---

# if - else

Muchas veces necesitamos ejecutar un bloque cuando la condición es verdadera y otro cuando es falsa.

Sintaxis

```java
if (condición) {

} else {

}
```

Ejemplo

```java
int age = 16;

if (age >= 18) {
    System.out.println("Puede ingresar.");
} else {
    System.out.println("Acceso denegado.");
}
```

Salida

```text
Acceso denegado.
```

---

# if - else if - else

Permite evaluar varias condiciones.

```java
int score = 85;

if (score >= 90) {
    System.out.println("Excelente");
} else if (score >= 80) {
    System.out.println("Muy bien");
} else if (score >= 70) {
    System.out.println("Bien");
} else if (score >= 60) {
    System.out.println("Suficiente");
} else {
    System.out.println("Reprobado");
}
```

Java evalúa las condiciones de arriba hacia abajo.

Cuando encuentra una verdadera, deja de revisar las demás.

---

# Condiciones compuestas

Podemos combinar varias condiciones utilizando operadores lógicos.

## Operador AND (&&)

```java
int age = 20;
boolean hasLicense = true;

if (age >= 18 && hasLicense) {
    System.out.println("Puede conducir.");
}
```

Ambas condiciones deben ser verdaderas.

---

## Operador OR (||)

```java
boolean hasCash = false;
boolean hasCard = true;

if (hasCash || hasCard) {
    System.out.println("Puede pagar.");
}
```

Solo una condición necesita ser verdadera.

---

## Operador NOT (!)

```java
boolean active = false;

if (!active) {
    System.out.println("La cuenta está desactivada.");
}
```

Invierte el valor del boolean.

---

# switch

Cuando una variable puede tomar varios valores conocidos, `switch` suele ser más claro que una cadena de `if`.

```java
int day = 3;

switch (day) {
    case 1:
        System.out.println("Lunes");
        break;

    case 2:
        System.out.println("Martes");
        break;

    case 3:
        System.out.println("Miércoles");
        break;

    default:
        System.out.println("Día inválido");
}
```

---

# ¿Qué hace break?

`break` indica que el `switch` debe terminar.

Si se omite:

```java
case 1:
    System.out.println("Lunes");

case 2:
    System.out.println("Martes");
```

Si el valor es `1`, también imprimirá `"Martes"`.

Este comportamiento se conoce como **fall-through**.

---

# switch con String

```java
String option = "A";

switch (option) {
    case "A":
        System.out.println("Opción A");
        break;

    case "B":
        System.out.println("Opción B");
        break;

    default:
        System.out.println("Opción inválida");
}
```

---

# Operador ternario

Es una forma abreviada de escribir un `if-else` sencillo.

```java
String result = age >= 18 ? "Mayor" : "Menor";
```

Equivale a:

```java
String result;

if (age >= 18) {
    result = "Mayor";
} else {
    result = "Menor";
}
```

Utilízalo únicamente cuando la condición sea simple.

---

# Buenas prácticas

* Utiliza llaves aunque el bloque tenga una sola instrucción.
* Evita anidar demasiados `if`.
* Escribe condiciones fáciles de leer.
* Usa `switch` cuando compares una misma variable con muchos valores.
* Usa el operador ternario solo para expresiones simples.

---

# Errores comunes

## Confundir `=` con `==`

Incorrecto

```java
if (age = 18)
```

Correcto

```java
if (age == 18)
```

---

## Colocar punto y coma después del if

Incorrecto

```java
if (age >= 18);
{
    System.out.println("Mayor");
}
```

El bloque se ejecutará siempre.

---

## Olvidar el bloque else

En algunos casos es necesario contemplar qué debe ocurrir cuando la condición sea falsa.

---

# Ejercicios

1. Determina si una persona es mayor de edad.
2. Determina si un número es positivo o negativo.
3. Calcula la calificación obtenida utilizando `if-else if`.
4. Crea un menú utilizando `switch`.
5. Determina si un año es bisiesto.
6. Utiliza el operador ternario para indicar si un número es par o impar.

---

# Reto

Desarrolla un programa que solicite:

* Nombre.
* Edad.
* Promedio.

El programa debe indicar:

* Si es mayor de edad.
* Si aprobó o reprobó.
* Si obtuvo una calificación excelente (mayor o igual a 90).
* Mostrar un mensaje personalizado dependiendo del resultado.


