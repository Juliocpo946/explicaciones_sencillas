# Lección 05 - Conversión de Tipos en Java 17

# ¿Qué es una conversión de tipos?

Una conversión de tipos consiste en transformar un dato de un tipo a otro.

Por ejemplo:

* Convertir un `int` en un `double`.
* Convertir un `double` en un `int`.
* Convertir un `String` en un `int`.
* Convertir un número en un `String`.

---

# Conversión implícita (Widening)

La realiza Java automáticamente cuando no existe riesgo de perder información.

```java
int age = 20;
double value = age;

System.out.println(value);
```

Salida

```text
20.0
```

En este caso no es necesario escribir ninguna instrucción adicional.

---

## Otro ejemplo

```java
char letter = 'A';
int ascii = letter;

System.out.println(ascii);
```

Salida

```text
65
```

Java convierte el carácter a su código Unicode.

---

# Conversión explícita (Casting)

Cuando existe posibilidad de perder información, el programador debe indicar la conversión.

La sintaxis es:

```java
(TargetType) variable
```

---

## Convertir double a int

```java
double price = 199.99;

int total = (int) price;

System.out.println(total);
```

Salida

```text
199
```

Observa que se pierde la parte decimal.

---

## Convertir long a int

```java
long population = 1000000L;

int value = (int) population;
```

Solo debe hacerse cuando el valor cabe dentro del rango de un `int`.

---

# Conversión entre enteros y decimales

```java
int number = 15;

double decimal = number;

System.out.println(decimal);
```

Resultado

```text
15.0
```

---

```java
double decimal = 15.75;

int number = (int) decimal;

System.out.println(number);
```

Resultado

```text
15
```

---

# Convertir String a int

Muchas veces los datos se leen como texto y es necesario convertirlos.

```java
String ageText = "25";

int age = Integer.parseInt(ageText);

System.out.println(age);
```

---

# Convertir String a double

```java
String priceText = "199.99";

double price = Double.parseDouble(priceText);

System.out.println(price);
```

---

# Convertir String a boolean

```java
String value = "true";

boolean active = Boolean.parseBoolean(value);

System.out.println(active);
```

---

# Convertir String a long

```java
String value = "500000";

long number = Long.parseLong(value);
```

---

# Convertir String a float

```java
String value = "15.8";

float number = Float.parseFloat(value);
```

---

# Convertir un número a String

```java
int age = 20;

String text = String.valueOf(age);

System.out.println(text);
```

---

También funciona con otros tipos.

```java
double salary = 15000.50;

String text = String.valueOf(salary);
```

---

# Concatenación

Cuando un `String` participa en una suma con `+`, Java convierte automáticamente el otro valor en texto.

```java
int age = 20;

System.out.println("Edad: " + age);
```

Salida

```text
Edad: 20
```

---

# Errores comunes

## Convertir texto no numérico

Incorrecto

```java
String value = "Hola";

int number = Integer.parseInt(value);
```

Produce una excepción porque `"Hola"` no representa un número.

---

## Perder información

```java
double value = 8.99;

int number = (int) value;
```

Resultado

```text
8
```

La parte decimal se elimina.

---

## Confundir conversión con concatenación

```java
System.out.println(10 + 20 + "30");
```

Salida

```text
3030
```

Primero se suma:

```text
10 + 20 = 30
```

Después se concatena:

```text
"30" + "30"
```

---

```java
System.out.println("30" + 10 + 20);
```

Salida

```text
301020
```

Como el primer elemento es un `String`, el resto también se trata como texto.

---

# Buenas prácticas

* Verificar que un texto realmente represente un número antes de convertirlo.
* Evitar conversiones innecesarias.
* Utilizar `String.valueOf()` para convertir cualquier dato a texto.
* Realizar un casting únicamente cuando sea necesario.
