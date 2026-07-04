# Lección 1 - Introducción a Java 17


## ¿Qué es Java?

Java es un lenguaje de programación orientado a objetos creado para
desarrollar aplicaciones que puedan ejecutarse en distintos sistemas
operativos sin modificar el código fuente.

Su filosofía es:

> Escribir una vez, ejecutar en cualquier lugar.

## ¿Cómo funciona Java?

1.  Escribes un archivo `.java`.
2.  El compilador `javac` lo convierte en un archivo `.class`.
3.  La JVM ejecuta el archivo `.class`.

``` text
Main.java
    |
 javac
    |
Main.class
    |
 JVM
    |
 Programa en ejecución
```

## Componentes principales

### JDK

Contiene las herramientas para desarrollar aplicaciones Java.

### JVM

Es la máquina virtual que ejecuta el código compilado.

### JRE

Incluye la JVM y los componentes necesarios para ejecutar programas.

## Primer programa

``` java
public class Main {

    public static void main(String[] args) {
        System.out.println("Hola Mundo");
    }

}
```

### Explicación

-   `public`: permite acceder a la clase desde cualquier lugar.
-   `class`: indica que se está definiendo una clase.
-   `Main`: nombre de la clase y del archivo (`Main.java`).
-   `public static void main(String[] args)`: punto de entrada del
    programa.
-   `System.out.println()`: imprime información en la consola.

