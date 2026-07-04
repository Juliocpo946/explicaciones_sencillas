# Lección 02 - Variables y Tipos de Datos en Java 17


# ¿Qué es una variable?

Una variable es un espacio de memoria donde Java almacena información para poder utilizarla posteriormente.

Imagina una caja.

Cada caja tiene una etiqueta y dentro guarda un valor.

Ejemplo:

```
Nombre de la caja

age

Contenido

25
```

Cuando el programa necesite conocer la edad, únicamente buscará la caja llamada **age**.

---

# ¿Por qué existen las variables?

Sin variables un programa no podría recordar información.

Por ejemplo:

* Nombre de un usuario.
* Edad.
* Precio de un producto.
* Saldo bancario.
* Temperatura.
* Resultado de una operación.

Toda esa información se almacena en variables.

---

# Sintaxis

Toda variable tiene la siguiente estructura.

```java
DataType variableName = value;
```

Cada parte tiene un significado.

**DataType**

Indica qué tipo de información se almacenará.

**variableName**

Es el nombre que identifica la variable.

**=**

Es el operador de asignación.

Su función es guardar un valor.

**value**

Es el dato que se almacenará.

---

# Primer ejemplo

```java
String name = "Juan";
```

¿Qué sucede?

1. Java reserva memoria.
2. La memoria será para almacenar texto.
3. Guarda el texto "Juan".
4. La memoria recibe el nombre **name**.

---

# Variables de tipo entero

```java
int age = 20;
```

Aquí Java almacena el número entero 20.

No lleva comillas porque es un número.

---

# Variables de tipo texto

```java
String city = "Tuxtla Gutiérrez";
```

Todo texto debe escribirse entre comillas dobles.

Incorrecto

```java
String city = Tuxtla;
```

Correcto

```java
String city = "Tuxtla";
```

---

# Tipos primitivos

Java posee ocho tipos primitivos.

## byte

Números pequeños.

```java
byte level = 5;
```

---

## short

```java
short population = 32000;
```

---

## int

El entero más utilizado.

```java
int age = 28;
```

---

## long

Para números muy grandes.

```java
long distance = 3000000000L;
```

La letra **L** indica que el número es de tipo long.

---

## float

Decimales.

```java
float temperature = 26.5F;
```

La letra **F** indica que el valor es float.

---

## double

También almacena decimales.

Es el más utilizado.

```java
double salary = 15000.75;
```

---

## char

Almacena un único carácter.

```java
char grade = 'A';
```

Utiliza comillas simples.

---

## boolean

Solo puede contener dos valores.

```java
boolean approved = true;
```

o

```java
boolean approved = false;
```

---

# String

Aunque no es un tipo primitivo, es uno de los más utilizados.

Sirve para almacenar texto.

```java
String firstName = "Carlos";
String lastName = "López";
```

---

# Imprimir variables

```java
String name = "María";
int age = 21;

System.out.println(name);
System.out.println(age);
```

También podemos combinarlas.

```java
System.out.println("Nombre: " + name);
System.out.println("Edad: " + age);
```

---

# Modificar el valor de una variable

Una variable puede cambiar.

```java
int age = 20;

age = 21;

System.out.println(age);
```

Resultado

```
21
```

---

# Constantes

Una constante no puede cambiar su valor.

Se declara utilizando **final**.

```java
final double PI = 3.1416;
```

Si intentamos modificarla, Java producirá un error.

---

# Reglas para nombrar variables

Correcto

```java
userName
userAge
totalPrice
studentGrade
```

Incorrecto

```java
User Name
1age
int
class
```

---

# Buenas prácticas

Utiliza nombres descriptivos.

Incorrecto

```java
int a;
double b;
```

Correcto

```java
int customerAge;
double productPrice;
```

---

# Errores comunes

## Olvidar el punto y coma

Incorrecto

```java
int age = 20
```

Correcto

```java
int age = 20;
```

---

## Asignar un tipo incorrecto

Incorrecto

```java
int age = "20";
```

Correcto

```java
int age = 20;
```

---

## Usar comillas incorrectas

Incorrecto

```java
char letter = "A";
```

Correcto

```java
char letter = 'A';
```

