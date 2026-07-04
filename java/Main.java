import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        //Tipodedato + nombreVariable = valor;
       
        System.out.println("Nombre");
        String nombre = scan.next();
        //scan seria un obejto next() es un metodo o su funcion que nos permite capturar un valor de tipo String
        // Apellidos
        scan.nextLine(); // Limpiar el buffer
        System.out.println("Apellidos");
        String apellidos = scan.nextLine();
        // Perez Ortiz
        System.out.println("Nombre completo: " + nombre + " " + apellidos);
        scanner.close();
        }
}