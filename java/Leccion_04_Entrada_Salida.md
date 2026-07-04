# Lección 04 - Entrada y Salida de Datos en Java 17

## Objetivo

Aprender a mostrar información en la consola y leer datos ingresados por
el usuario utilizando `Scanner`.

## Mostrar información

### System.out.print()

Imprime texto sin realizar un salto de línea.

``` java
System.out.print("Hola ");
System.out.print("Mundo");
```

Salida:

``` text
Hola Mundo
```

### System.out.println()

Imprime el texto y después realiza un salto de línea.

``` java
System.out.println("Hola");
System.out.println("Mundo");
```

Salida:

``` text
Hola
Mundo
```

### System.out.printf()

Permite dar formato a la salida.

``` java
String name = "Juan";
int age = 20;

System.out.printf("Nombre: %s%n", name);
System.out.printf("Edad: %d%n", age);
```

Marcadores comunes:

  Marcador   Tipo
  ---------- ----------------
  %s         String
  %d         int
  %f         double/float
  %b         boolean
  %c         char
  %n         Salto de línea

## Leer datos con Scanner

Antes de usar Scanner debe importarse.

``` java
import java.util.Scanner;
```

Crear el objeto:

``` java
Scanner scanner = new Scanner(System.in);
```

`System.in` representa el teclado.

## Leer un String

``` java
System.out.print("Nombre: ");
String name = scanner.nextLine();
```

## Leer un int

``` java
System.out.print("Edad: ");
int age = scanner.nextInt();
```

## Leer un double

``` java
System.out.print("Estatura: ");
double height = scanner.nextDouble();
```

## Leer un boolean

``` java
System.out.print("¿Es estudiante? (true/false): ");
boolean student = scanner.nextBoolean();
```

## Leer un solo carácter

Scanner no tiene un método `nextChar()`.

``` java
System.out.print("Inicial: ");
char initial = scanner.next().charAt(0);
```

## next() vs nextLine()

`next()` lee hasta el primer espacio.

``` text
Juan Pérez
```

Resultado:

``` text
Juan
```

`nextLine()` lee toda la línea.

Resultado:

``` text
Juan Pérez
```

## Problema común con nextLine()

``` java
int age = scanner.nextInt();
scanner.nextLine();
String name = scanner.nextLine();
```

Después de `nextInt()` conviene llamar a `nextLine()` para consumir el
salto de línea pendiente.

## Programa completo

``` java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.print("Nombre: ");
        String name = scanner.nextLine();

        System.out.print("Edad: ");
        int age = scanner.nextInt();

        System.out.print("Promedio: ");
        double average = scanner.nextDouble();

        System.out.println();
        System.out.println("Resumen");
        System.out.println("Nombre: " + name);
        System.out.println("Edad: " + age);
        System.out.println("Promedio: " + average);

        scanner.close();
    }

}
```

## Buenas prácticas

-   Crear un solo `Scanner` para `System.in`.
-   Cerrar el `Scanner` al finalizar.
-   Utilizar `nextLine()` cuando se esperan textos con espacios.
-   Mostrar mensajes claros antes de solicitar datos.

## Errores comunes

-   Olvidar `import java.util.Scanner;`
-   Escribir letras cuando se espera un número.
-   Confundir `next()` con `nextLine()`.
-   Olvidar consumir el salto de línea después de `nextInt()`.


