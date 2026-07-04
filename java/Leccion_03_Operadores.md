# Lección 03 - Operadores en Java 17


# ¿Qué es un operador?

Un operador es un símbolo que realiza una operación sobre uno o más valores.

Por ejemplo, cuando escribimos:

```java
int result = 10 + 5;
```

El símbolo `+` es un operador.

Recibe dos valores:

* 10
* 5

Y produce un nuevo resultado:

```text
15
```

Existen distintos tipos de operadores dependiendo de la operación que realizan.

---

# Operadores aritméticos

Sirven para realizar operaciones matemáticas.

## Suma (+)

```java
int a = 10;
int b = 5;

int result = a + b;

System.out.println(result);
```

Salida

```text
15
```

---

## Resta (-)

```java
int result = 10 - 5;

System.out.println(result);
```

Salida

```text
5
```

---

## Multiplicación (*)

```java
int result = 8 * 4;

System.out.println(result);
```

Salida

```text
32
```

---

## División (/)

```java
int result = 20 / 4;

System.out.println(result);
```

Salida

```text
5
```

Si ambos números son enteros, el resultado también será un entero.

```java
System.out.println(7 / 2);
```

Salida

```text
3
```

Para obtener decimales:

```java
System.out.println(7.0 / 2);
```

Salida

```text
3.5
```

---

## Residuo (%)

Devuelve el residuo de una división.

```java
System.out.println(10 % 3);
```

Salida

```text
1
```

Es muy utilizado para saber si un número es par o impar.

```java
int number = 18;

System.out.println(number % 2);
```

Resultado

```text
0
```

Si el resultado es cero, el número es par.

---

# Operadores de asignación

Sirven para asignar o actualizar valores.

## Asignación simple

```java
int age = 20;
```

---

## Suma y asignación

```java
int score = 10;

score += 5;

System.out.println(score);
```

Salida

```text
15
```

Es equivalente a:

```java
score = score + 5;
```

---

## Resta y asignación

```java
score -= 2;
```

---

## Multiplicación y asignación

```java
score *= 4;
```

---

## División y asignación

```java
score /= 2;
```

---

## Residuo y asignación

```java
score %= 3;
```

---

# Operadores relacionales

Comparan dos valores.

Siempre devuelven un boolean.

---

## Igual que (==)

```java
System.out.println(10 == 10);
```

Resultado

```text
true
```

---

## Diferente de (!=)

```java
System.out.println(10 != 8);
```

Resultado

```text
true
```

---

## Mayor que (>)

```java
System.out.println(15 > 8);
```

---

## Menor que (<)

```java
System.out.println(5 < 10);
```

---

## Mayor o igual (>=)

```java
System.out.println(10 >= 10);
```

---

## Menor o igual (<=)

```java
System.out.println(5 <= 8);
```

---

# Operadores lógicos

Trabajan con valores boolean.

---

## AND (&&)

Devuelve true únicamente cuando ambas condiciones son verdaderas.

```java
int age = 20;
boolean hasLicense = true;

System.out.println(age >= 18 && hasLicense);
```

Resultado

```text
true
```

---

## OR (||)

Devuelve true cuando al menos una condición es verdadera.

```java
boolean hasCash = false;
boolean hasCard = true;

System.out.println(hasCash || hasCard);
```

Resultado

```text
true
```

---

## NOT (!)

Invierte un valor boolean.

```java
boolean active = true;

System.out.println(!active);
```

Resultado

```text
false
```

---

# Incremento

Incrementa una unidad.

```java
int number = 5;

number++;

System.out.println(number);
```

Salida

```text
6
```

También puede escribirse:

```java
++number;
```

---

# Decremento

Reduce una unidad.

```java
int number = 5;

number--;

System.out.println(number);
```

Salida

```text
4
```

---

# Diferencia entre ++variable y variable++

```java
int x = 5;

System.out.println(++x);
```

Resultado

```text
6
```

Primero incrementa y después imprime.

---

```java
int x = 5;

System.out.println(x++);
```

Resultado

```text
5
```

Después de imprimir, la variable vale:

```text
6
```

---

# Precedencia de operadores

Java sigue un orden para resolver operaciones.

Ejemplo

```java
System.out.println(5 + 4 * 2);
```

Resultado

```text
13
```

Primero realiza:

```text
4 * 2
```

Después:

```text
5 + 8
```

Si deseas cambiar el orden utiliza paréntesis.

```java
System.out.println((5 + 4) * 2);
```

Resultado

```text
18
```

---

# Errores comunes

## Confundir = con ==

Incorrecto

```java
if (age = 18)
```

Correcto

```java
if (age == 18)
```

---

## Dividir entre cero

```java
int result = 10 / 0;
```

Provoca una excepción en tiempo de ejecución.

---

## Olvidar los paréntesis

Incorrecto

```java
System.out.println("Resultado: " + 5 + 3);
```

Salida

```text
Resultado: 53
```

Correcto

```java
System.out.println("Resultado: " + (5 + 3));
```

Salida

```text
Resultado: 8
```

---

# Ejercicios

1. Calcula el área de un rectángulo.
2. Calcula el promedio de tres calificaciones.
3. Determina si un número es par.
4. Verifica si una persona es mayor de edad.
5. Verifica si puede conducir considerando edad y licencia.
6. Incrementa una variable diez veces utilizando `++`.

