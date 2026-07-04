# String Pool, Inmutabilidad y Comparación de Cadenas

En la parte anterior aprendiste qué es un `String`, por qué es una clase y cómo crear uno.

Ahora veremos cómo Java almacena los `String` en memoria y por qué su comportamiento es diferente al de otros objetos.

---

# ¿Dónde se almacena un String?

Cuando escribimos:

```java
String language = "Java";
```

Muchos piensan que la variable contiene directamente el texto.

Realmente no sucede así.

La variable almacena una **referencia** al objeto `String`.

Podemos imaginarlo así.

```text
Variable

language
    │
    │
    ▼
+------------+
|   "Java"   |
+------------+
```

La variable apunta al objeto donde realmente se encuentra el texto.

---

# ¿Qué es una referencia?

Una referencia puede imaginarse como una dirección.

No contiene el objeto.

Contiene la ubicación donde se encuentra el objeto.

Una analogía sería un domicilio.

Supongamos que quieres visitar una casa.

Tu libreta de direcciones no contiene la casa.

Solo contiene la dirección.

Lo mismo ocurre con una referencia.

---

# Dos variables pueden apuntar al mismo String

Observa el siguiente ejemplo.

```java
String first = "Java";
String second = "Java";
```

Muchos principiantes creen que Java crea dos objetos.

En realidad ocurre algo diferente.

```text
first
   │
   │
   ├───────────────┐
   │               │
   ▼               ▼
        +----------------+
        |     "Java"     |
        +----------------+
   ▲
   │
second
```

Ambas variables apuntan exactamente al mismo objeto.

¿Por qué?

Porque Java intenta ahorrar memoria.

---

# ¿Qué es el String Pool?

El **String Pool** es una zona especial de memoria donde Java guarda los textos creados mediante literales.

Por ejemplo.

```java
String country = "México";
```

Si posteriormente escribimos:

```java
String nation = "México";
```

Java revisa primero el String Pool.

Pregunta:

> ¿Ya existe un String con el texto "México"?

Si la respuesta es sí...

No crea uno nuevo.

Simplemente hace que ambas variables apunten al mismo objeto.

Esto reduce considerablemente el consumo de memoria.

---

# ¿Qué ocurre con new String()?

Observa.

```java
String first = new String("Java");
String second = new String("Java");
```

Ahora sí existen dos objetos distintos.

```text
first

   │
   ▼

+------------+
|   "Java"   |
+------------+

second

   │
   ▼

+------------+
|   "Java"   |
+------------+
```

Aunque el contenido sea exactamente el mismo.

Por eso normalmente se recomienda utilizar:

```java
String language = "Java";
```

En lugar de:

```java
String language = new String("Java");
```

---

# ¿Qué significa que un String sea inmutable?

Esta es una de las características más importantes de Java.

La palabra **inmutable** significa:

> Una vez creado un objeto, su contenido no puede modificarse.

Veamos un ejemplo.

```java
String name = "Juan";
```

Ahora intentemos cambiarlo.

```java
name = "Pedro";
```

Muchos creen que Java modifica el texto.

No es cierto.

Lo que realmente sucede es esto.

Primero.

```text
name

 │
 ▼

+-----------+
|  "Juan"   |
+-----------+
```

Después.

```java
name = "Pedro";
```

Java crea otro objeto.

```text
           +-----------+
           |  "Juan"   |
           +-----------+

name

 │
 ▼

+------------+
|  "Pedro"   |
+------------+
```

El objeto `"Juan"` nunca cambió.

Simplemente la variable dejó de apuntarlo.

Ahora apunta a otro objeto.

Por eso decimos que `String` es inmutable.

---

# ¿Por qué Java hizo esto?

Porque un objeto inmutable es:

* Más seguro.
* Más fácil de compartir.
* Más eficiente.
* Más rápido para trabajar internamente.

Además evita errores cuando varias variables utilizan el mismo texto.

---

# Comparar Strings

Supongamos el siguiente código.

```java
String first = "Java";
String second = "Java";
```

¿Cómo comprobamos si son iguales?

Muchos principiantes escriben.

```java
System.out.println(first == second);
```

El resultado será.

```text
true
```

Pero esto puede ser engañoso.

---

# ¿Qué hace realmente ==?

El operador `==` **no compara el contenido**.

Compara las referencias.

Pregunta.

> ¿Ambas variables apuntan exactamente al mismo objeto?

En este caso sí.

Por eso devuelve.

```text
true
```

---

# Veamos otro ejemplo.

```java
String first = new String("Java");
String second = new String("Java");

System.out.println(first == second);
```

Resultado.

```text
false
```

¿Por qué?

Porque existen dos objetos distintos.

```text
first ─────► Objeto A

second ────► Objeto B
```

Aunque ambos contienen:

```text
Java
```

---

# ¿Cómo comparar correctamente el contenido?

Para eso existe el método:

```java
equals()
```

Ejemplo.

```java
String first = new String("Java");
String second = new String("Java");

System.out.println(first.equals(second));
```

Resultado.

```text
true
```

Ahora Java pregunta.

> ¿El contenido es el mismo?

Y no.

> ¿Son el mismo objeto?

Esa comparación ya no importa.

---

# Comparación visual

Usando `==`

```text
¿Misma referencia?

Sí → true

No → false
```

Usando `equals()`

```text
¿Mismo texto?

Sí → true

No → false
```

---

# ¿Cuál debo utilizar?

Regla sencilla.

Para comparar texto:

Siempre utiliza.

```java
equals()
```

No utilices.

```java
==
```

Salvo que realmente quieras saber si ambas variables apuntan exactamente al mismo objeto.

En la práctica casi nunca necesitarás eso.

---

# equalsIgnoreCase()

Este método compara el contenido ignorando mayúsculas y minúsculas.

Ejemplo.

```java
String first = "JAVA";
String second = "java";

System.out.println(first.equals(second));
```

Resultado.

```text
false
```

Ahora.

```java
System.out.println(first.equalsIgnoreCase(second));
```

Resultado.

```text
true
```

Porque este método no distingue entre:

```text
A
```

y

```text
a
```

---

# Error muy común

Muchos principiantes hacen esto.

```java
Scanner scanner = new Scanner(System.in);

String option = scanner.nextLine();

if (option == "SI") {

}
```

Aunque el usuario escriba.

```text
SI
```

Puede que la condición sea falsa.

La forma correcta es.

```java
if (option.equals("SI")) {

}
```

O si no importa si escribe mayúsculas o minúsculas.

```java
if (option.equalsIgnoreCase("SI")) {

}
```

---

# Buenas prácticas

* Utiliza literales siempre que sea posible.
* Evita crear `String` con `new`.
* Compara texto utilizando `equals()`.
* Si deseas ignorar mayúsculas utiliza `equalsIgnoreCase()`.
* Recuerda que un `String` nunca cambia; cuando parece cambiar, Java crea un objeto nuevo.

---

# Ejercicios

1. Crea dos variables con el mismo literal y compáralas con `==`.
2. Crea dos objetos utilizando `new String()` y compáralos con `==`.
3. Repite el ejercicio utilizando `equals()`.
4. Compara `"JAVA"` y `"java"` utilizando `equals()`.
5. Repite el ejercicio utilizando `equalsIgnoreCase()`.
6. Explica con tus palabras qué significa que un `String` sea inmutable.
