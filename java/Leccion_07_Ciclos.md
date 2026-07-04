# Lección 07 - Ciclos

# Objetivo

Al finalizar esta lección serás capaz de:

* Comprender qué es una estructura repetitiva.
* Identificar cuándo utilizar un ciclo.
* Utilizar `while`, `do-while`, `for` y `for-each`.
* Conocer el funcionamiento de `break` y `continue`.
* Evitar errores comunes como los ciclos infinitos.

---

# ¿Qué es un ciclo?

Hasta ahora nuestros programas ejecutaban cada instrucción una sola vez.

Por ejemplo:

```java
System.out.println("Hola");
System.out.println("Hola");
System.out.println("Hola");
System.out.println("Hola");
System.out.println("Hola");
```

El programa imprime cinco veces la misma palabra.

Aunque funciona, existe un problema.

Estamos escribiendo la misma instrucción varias veces.

Ahora imagina que necesitas imprimir "Hola" 1,000 veces.

¿Escribirías 1,000 líneas de código?

La respuesta es no.

Para resolver este problema existen los **ciclos**.

---

# ¿Qué es una estructura repetitiva?

Una estructura repetitiva permite ejecutar un bloque de código varias veces sin escribirlo repetidamente.

Podemos imaginar un ciclo como una instrucción que dice:

```text
Mientras la condición sea verdadera,
sigue ejecutando este bloque.
```

---

# ¿Cuándo utilizar un ciclo?

Los ciclos son útiles cuando conocemos que una tarea debe repetirse.

Ejemplos:

* Mostrar los números del 1 al 100.
* Calcular la suma de varios números.
* Recorrer un arreglo.
* Mostrar un menú hasta que el usuario decida salir.
* Leer información de varios estudiantes.

---

# El ciclo while

Es el ciclo más sencillo.

Sintaxis

```java
while (condición) {

}
```

Java primero evalúa la condición.

Si la condición es verdadera, ejecuta el bloque.

Al terminar vuelve a evaluar la condición.

Este proceso continúa hasta que la condición sea falsa.

---

## Primer ejemplo

```java
int number = 1;

while (number <= 5) {
    System.out.println(number);
    number++;
}
```

Salida

```text
1
2
3
4
5
```

---

# ¿Cómo funciona?

Al inicio:

```text
number = 1
```

Java pregunta:

```text
¿1 es menor o igual que 5?
```

Respuesta

```text
Sí
```

Entonces imprime:

```text
1
```

Después ejecuta:

```java
number++;
```

Ahora:

```text
number = 2
```

Y vuelve a realizar exactamente el mismo proceso.

---

# ¿Qué ocurre si olvidamos incrementar la variable?

```java
int number = 1;

while (number <= 5) {
    System.out.println(number);
}
```

La variable nunca cambia.

Siempre vale:

```text
1
```

La condición nunca deja de cumplirse.

El programa entra en un **ciclo infinito**.

---

# Ciclo do-while

La diferencia con `while` es que el bloque se ejecuta al menos una vez.

Sintaxis

```java
do {

} while (condición);
```

---

## Ejemplo

```java
int option = 1;

do {
    System.out.println("Bienvenido");
    option++;
} while (option <= 3);
```

Salida

```text
Bienvenido
Bienvenido
Bienvenido
```

---

# Diferencia entre while y do-while

## while

Primero verifica.

Después ejecuta.

```text
Condición

↓

¿Es verdadera?

↓

Sí

↓

Ejecuta
```

---

## do-while

Primero ejecuta.

Después verifica.

```text
Ejecuta

↓

Condición

↓

¿Continúa?
```

---

# El ciclo for

Es el ciclo más utilizado cuando conocemos cuántas veces debe repetirse una acción.

Sintaxis

```java
for (inicio; condición; incremento) {

}
```

Tiene tres partes.

---

## Inicialización

```java
int i = 1;
```

Se ejecuta únicamente una vez.

---

## Condición

```java
i <= 10
```

Mientras sea verdadera el ciclo continúa.

---

## Incremento

```java
i++
```

Se ejecuta al finalizar cada repetición.

---

# Ejemplo

```java
for (int i = 1; i <= 5; i++) {
    System.out.println(i);
}
```

Salida

```text
1
2
3
4
5
```

---

# Cuenta regresiva

```java
for (int i = 10; i >= 1; i--) {
    System.out.println(i);
}
```

Salida

```text
10
9
8
7
6
5
4
3
2
1
```

---

# Ciclos anidados

Un ciclo puede contener otro ciclo.

```java
for (int row = 1; row <= 3; row++) {

    for (int column = 1; column <= 4; column++) {
        System.out.print("* ");
    }

    System.out.println();
}
```

Salida

```text
* * * *
* * * *
* * * *
```

---

# El ciclo for-each

Se utiliza para recorrer arreglos y colecciones.

Ejemplo

```java
String[] names = {
    "Ana",
    "Luis",
    "Pedro"
};

for (String name : names) {
    System.out.println(name);
}
```

Salida

```text
Ana
Luis
Pedro
```

---

# break

Permite salir inmediatamente de un ciclo.

```java
for (int i = 1; i <= 10; i++) {

    if (i == 5) {
        break;
    }

    System.out.println(i);
}
```

Salida

```text
1
2
3
4
```

Cuando `i` vale 5 el ciclo termina.

---

# continue

Omite únicamente la iteración actual.

```java
for (int i = 1; i <= 5; i++) {

    if (i == 3) {
        continue;
    }

    System.out.println(i);
}
```

Salida

```text
1
2
4
5
```

El número 3 no se imprime.

---

# ¿Qué ciclo debo utilizar?

## while

Cuando no sabes cuántas veces se repetirá el proceso.

Ejemplo:

* Menús.
* Validaciones.
* Solicitar datos hasta que sean correctos.

---

## do-while

Cuando el bloque debe ejecutarse al menos una vez.

Ejemplo:

* Mostrar un menú por primera vez.

---

## for

Cuando conoces el número de repeticiones.

Ejemplo:

* Imprimir del 1 al 100.
* Recorrer posiciones.

---

## for-each

Cuando únicamente deseas recorrer un arreglo o una colección sin utilizar índices.

---

# Buenas prácticas

* Utiliza nombres descriptivos para las variables cuando sea posible.
* Evita ciclos infinitos.
* Mantén el cuerpo del ciclo lo más pequeño posible.
* No abuses de `break` y `continue`.
* Elige el ciclo adecuado para cada problema.

---

# Errores comunes

## Ciclo infinito

```java
while (true) {

}
```

Solo debe utilizarse cuando realmente se necesita.

---

## Olvidar incrementar la variable

```java
int i = 1;

while (i <= 10) {
    System.out.println(i);
}
```

Nunca termina.

---

## Modificar incorrectamente la variable del ciclo

```java
for (int i = 1; i <= 10; i++) {

    i += 5;

}
```

Puede provocar resultados inesperados.

---

# Ejercicios

1. Imprime los números del 1 al 20 utilizando `while`.
2. Imprime los números pares del 2 al 100 utilizando `for`.
3. Realiza una cuenta regresiva del 20 al 1.
4. Calcula la suma de los primeros 100 números.
5. Muestra la tabla de multiplicar de un número.
6. Dibuja un cuadrado utilizando `*` y ciclos anidados.
7. Recorre un arreglo utilizando `for-each`.

---

# Reto

Desarrolla un programa que permita:

1. Mostrar un menú.
2. Solicitar una opción al usuario.
3. Repetir el menú hasta que el usuario seleccione la opción **Salir**.
4. Utilizar un ciclo `do-while`.
5. Implementar un `switch` para procesar cada opción.

---

# Resumen

En esta lección aprendiste:

* `while`
* `do-while`
* `for`
* `for-each`
* Ciclos anidados
* `break`
* `continue`

Estos ciclos son una de las herramientas más utilizadas en programación y aparecerán constantemente en las siguientes lecciones, especialmente al trabajar con arreglos, colecciones y objetos.
