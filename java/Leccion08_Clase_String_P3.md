# Métodos de la clase String en Java 17

En las partes anteriores aprendiste:

* Qué es un `String`.
* Cómo se almacena en memoria.
* Qué es el **String Pool**.
* Qué significa que sea **inmutable**.
* Cómo comparar cadenas correctamente utilizando `equals()`.

Ahora aprenderás los métodos más utilizados de la clase `String`.

---

# ¿Qué es un método?

Recuerda que `String` es una clase.

Las clases poseen **métodos**.

Un método es una acción que un objeto puede realizar.

Por ejemplo.

```java
String language = "Java";
```

El objeto `language` puede realizar distintas acciones.

```java
language.length();
language.toUpperCase();
language.toLowerCase();
language.substring(1);
```

Cada una de ellas devuelve un resultado diferente.

---

# length()

Permite conocer la cantidad de caracteres que contiene un texto.

Sintaxis.

```java
string.length();
```

Ejemplo.

```java
String language = "Java";

System.out.println(language.length());
```

Salida.

```text
4
```

¿Por qué el resultado es 4?

Porque la palabra contiene cuatro caracteres.

```text
J
a
v
a
```

Los espacios también cuentan.

```java
String text = "Hola Mundo";

System.out.println(text.length());
```

Salida.

```text
10
```

---

# charAt()

Obtiene un carácter utilizando su posición.

Sintaxis.

```java
string.charAt(indice);
```

Ejemplo.

```java
String language = "Java";

System.out.println(language.charAt(0));
```

Salida.

```text
J
```

Otro ejemplo.

```java
System.out.println(language.charAt(2));
```

Salida.

```text
v
```

Recordemos las posiciones.

```text
+-----+-----+-----+-----+
|  J  |  a  |  v  |  a  |
+-----+-----+-----+-----+
   0     1     2     3
```

Si utilizas una posición inexistente.

```java
language.charAt(10);
```

Java lanzará una excepción porque ese índice no existe.

---

# substring()

Permite obtener una parte del texto.

Primer ejemplo.

```java
String language = "Programacion";

System.out.println(language.substring(0, 5));
```

Salida.

```text
Progr
```

El segundo parámetro no se incluye.

Observa.

```text
P r o g r a m a c i o n
0 1 2 3 4 5
```

Java toma desde la posición 0 hasta antes de la posición 5.

También puede utilizarse un solo parámetro.

```java
System.out.println(language.substring(5));
```

Salida.

```text
amacion
```

---

# contains()

Permite verificar si un texto contiene otro.

```java
String email = "usuario@gmail.com";

System.out.println(email.contains("@"));
```

Salida.

```text
true
```

Otro ejemplo.

```java
System.out.println(email.contains(".com"));
```

Resultado.

```text
true
```

---

# startsWith()

Verifica si el texto comienza con cierta cadena.

```java
String url = "https://openai.com";

System.out.println(url.startsWith("https"));
```

Salida.

```text
true
```

---

# endsWith()

Verifica si termina con determinado texto.

```java
String file = "documento.pdf";

System.out.println(file.endsWith(".pdf"));
```

Salida.

```text
true
```

---

# indexOf()

Busca la primera aparición de un carácter o texto.

```java
String language = "Programacion";

System.out.println(language.indexOf("a"));
```

Salida.

```text
5
```

Si el texto no existe.

```java
System.out.println(language.indexOf("z"));
```

Salida.

```text
-1
```

El valor `-1` significa:

> No encontrado.

---

# lastIndexOf()

Busca la última aparición.

```java
String language = "Programacion";

System.out.println(language.lastIndexOf("a"));
```

Salida.

```text
7
```

---

# toUpperCase()

Convierte el texto a mayúsculas.

```java
String name = "Juan";

System.out.println(name.toUpperCase());
```

Salida.

```text
JUAN
```

---

# toLowerCase()

Convierte el texto a minúsculas.

```java
String country = "MÉXICO";

System.out.println(country.toLowerCase());
```

Salida.

```text
méxico
```

---

# trim()

Elimina espacios al inicio y al final.

```java
String text = "   Hola Mundo   ";

System.out.println(text.trim());
```

Salida.

```text
Hola Mundo
```

Observa que los espacios entre palabras no desaparecen.

---

# strip()

Desde Java 11 existe `strip()`.

Cumple una función similar a `trim()`, pero maneja correctamente más tipos de espacios Unicode.

En la mayoría de los programas ambos producen el mismo resultado.

```java
String text = "   Java   ";

System.out.println(text.strip());
```

---

# replace()

Reemplaza texto.

```java
String text = "Hola Mundo";

System.out.println(text.replace("Mundo", "Java"));
```

Salida.

```text
Hola Java
```

Recuerda.

El objeto original no cambia.

Siempre se crea un nuevo `String`.

---

# replaceAll()

Utiliza expresiones regulares.

Por ahora basta con saber que permite reemplazos más avanzados.

```java
String phone = "555-123-456";

System.out.println(phone.replaceAll("-", ""));
```

Salida.

```text
555123456
```

---

# split()

Divide un texto.

```java
String colors = "Rojo,Verde,Azul";

String[] values = colors.split(",");
```

Resultado.

```text
values[0] = Rojo

values[1] = Verde

values[2] = Azul
```

Este método se utiliza constantemente cuando se trabaja con archivos CSV.

---

# isEmpty()

Indica si la cadena tiene longitud cero.

```java
String text = "";

System.out.println(text.isEmpty());
```

Salida.

```text
true
```

---

# isBlank()

Comprueba si la cadena está vacía o únicamente contiene espacios.

```java
String text = "      ";

System.out.println(text.isBlank());
```

Salida.

```text
true
```

Comparación.

```text
""           -> isEmpty() = true
""           -> isBlank() = true

"     "      -> isEmpty() = false
"     "      -> isBlank() = true
```

---

# repeat()

Disponible desde Java 11.

Permite repetir un texto.

```java
System.out.println("*".repeat(10));
```

Salida.

```text
**********
```

---

# formatted()

Disponible desde Java 15.

```java
String message = "Hola %s".formatted("Juan");

System.out.println(message);
```

Salida.

```text
Hola Juan
```

---

# Encadenamiento de métodos

Es posible llamar varios métodos seguidos.

```java
String name = "   juan   ";

String result = name.trim()
                    .toUpperCase()
                    .replace("J", "P");

System.out.println(result);
```

Salida.

```text
PUAN
```

Cada método devuelve un nuevo `String`.

---

# Buenas prácticas

* Utiliza `equals()` para comparar texto.
* Evita usar `==`.
* Aprovecha los métodos existentes antes de escribir código manualmente.
* Recuerda que los `String` son inmutables.
* Guarda el resultado cuando un método devuelve un nuevo `String`.

Ejemplo.

Incorrecto.

```java
String name = "Juan";

name.toUpperCase();

System.out.println(name);
```

Salida.

```text
Juan
```

Correcto.

```java
String name = "Juan";

name = name.toUpperCase();

System.out.println(name);
```

Salida.

```text
JUAN
```

---

# Errores comunes

## Comparar con `==`

Incorrecto.

```java
name == "Juan"
```

Correcto.

```java
name.equals("Juan")
```

---

## Pensar que `replace()` modifica el texto

Incorrecto.

```java
name.replace("a", "o");
```

El resultado se pierde.

Correcto.

```java
name = name.replace("a", "o");
```

---

## Acceder a un índice inexistente

```java
name.charAt(100);
```

Provoca una excepción.

---

# Ejercicios

1. Mostrar la longitud de un nombre.
2. Obtener el primer carácter de una palabra.
3. Obtener el último carácter utilizando `length()`.
4. Convertir un texto a mayúsculas.
5. Convertir un texto a minúsculas.
6. Verificar si un correo contiene `"@"`.
7. Verificar si un archivo termina en `.pdf`.
8. Dividir una lista de nombres utilizando `split()`.
9. Reemplazar todos los espacios por guiones.
10. Validar si una cadena está vacía utilizando `isEmpty()`.
11. Validar si una cadena contiene únicamente espacios utilizando `isBlank()`.
12. Crear una línea de separación utilizando `repeat()`.

---

# Reto

Desarrolla un programa que solicite al usuario:

* Nombre completo.
* Correo electrónico.
* Ciudad.

Después debe mostrar:

* Nombre en mayúsculas.
* Nombre en minúsculas.
* Cantidad de caracteres del nombre.
* Primera letra del nombre.
* Última letra del nombre.
* Verificar si el correo contiene `"@"`.
* Verificar si termina en `.com`.
* Eliminar espacios al inicio y al final del nombre.
* Mostrar una línea de 50 caracteres utilizando `repeat()`.

---

# Resumen

En esta lección aprendiste:

* Cómo funciona la clase `String`.
* Qué significa que sea inmutable.
* Cómo comparar cadenas correctamente.
* Los métodos más utilizados para manipular texto.
* Buenas prácticas al trabajar con cadenas.

La clase `String` es una de las más utilizadas en Java. Dominar sus métodos te permitirá procesar nombres, correos electrónicos, archivos, datos de usuarios y cualquier información textual de forma eficiente.
