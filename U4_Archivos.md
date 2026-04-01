# Archivos en C++

---

## ¿Por qué se necesitan los archivos?

Cuando un programa termina, toda la información guardada en variables y arreglos desaparece. Los archivos resuelven eso: permiten que los datos sobrevivan al cierre del programa.

```
SIN archivos:                      CON archivos:

  Programa corre                     Programa corre
       │                                  │
  Guarda datos en                    Guarda datos en
  variables/arreglos                 un archivo .txt
       │                                  │
  Programa termina                   Programa termina
       │                                  │
  ❌ Datos perdidos                  ✅ Datos en disco
                                          │
                                     Programa vuelve
                                     a correr
                                          │
                                     ✅ Datos disponibles
```

Esto se llama **persistencia de datos**.

---

## ¿Cómo funciona en C++?

Se necesitan dos librerías:

```cpp
#include <iostream>   // para cout y cin
#include <fstream>    // para leer y escribir archivos
```

La librería `<fstream>` provee dos herramientas principales:

```
<fstream>
    │
    ├── ofstream  →  para ESCRIBIR en archivos  (output = salida)
    │
    └── ifstream  →  para LEER de archivos      (input  = entrada)
```

---

## Modos de apertura

```
┌────────────┬────────────────────────────────────────────────────┐
│   Modo     │   Qué hace                                         │
├────────────┼────────────────────────────────────────────────────┤
│ ios::out   │ Abre para escribir. Crea el archivo si no existe.  │
│            │ Si ya existe, borra su contenido y empieza de cero.│
├────────────┼────────────────────────────────────────────────────┤
│ ios::in    │ Abre para leer. El archivo debe existir.           │
├────────────┼────────────────────────────────────────────────────┤
│ ios::app   │ Abre para agregar. No borra el contenido previo.   │
│            │ Los datos nuevos se añaden al final.               │
└────────────┴────────────────────────────────────────────────────┘
```

### Diferencia entre `ios::out` y `ios::app`

```
Archivo actual: [ Juan | Adriana ]

Con ios::out:                     Con ios::app:
  Se borra todo primero             Se conserva el contenido
  [ vacío ]                         [ Juan | Adriana ]
  Se escribe nuevo dato             Se agrega al final
  [ Carlos ]                        [ Juan | Adriana | Carlos ]
```

---

## Escribir un archivo

Se usa `ofstream`. El flujo de datos va del programa hacia el archivo.

```
  Programa
     │
     │  archivoSalida << matricula << nombre
     │
     ▼
  datos.txt
```

```cpp
#include <iostream>
#include <fstream>
using namespace std;

int escribirArchivo() {
    ofstream archivoSalida("datos.txt", ios::out);

    if (!archivoSalida) {              // verificar que se abrió bien
        cerr << "No se puede crear el archivo";
        exit(1);
    }

    string nombre;
    int matricula;

    cout << "Escriba su matricula y nombre." << endl;
    cout << "Escriba ? para terminar." << endl;

    while (cin >> matricula >> nombre) {
        archivoSalida << matricula << ' ' << nombre << endl;
    }

    return 0;    // el archivo se cierra automáticamente aquí
}

int main() {
    escribirArchivo();
}
```

Si el usuario escribe `123456 Juan` y `894560 Adriana`, el archivo queda así:

```
datos.txt
┌─────────────────────┐
│ 123456 Juan         │
│ 894560 Adriana      │
└─────────────────────┘
```

---

## Leer un archivo

Se usa `ifstream`. El flujo de datos va del archivo hacia el programa.

```
  datos.txt
     │
     │  archivoEntrada >> matricula >> nombre
     │
     ▼
  Programa  →  cout
```

```cpp
#include <iostream>
#include <fstream>
using namespace std;

int leerArchivo() {
    ifstream archivoEntrada("datos.txt", ios::in);

    if (!archivoEntrada) {             // verificar que se abrió bien
        cerr << "No se puede abrir el archivo";
        exit(1);
    }

    string nombre;
    int matricula;

    cout << "Matricula \t Nombre" << endl;

    while (archivoEntrada >> matricula >> nombre) {
        cout << matricula << "\t\t" << nombre << endl;
    }

    return 0;
}

int main() {
    leerArchivo();
}
```

Con el archivo del ejemplo anterior, la salida en pantalla es:

```
Matricula        Nombre
123456           Juan
894560           Adriana
```

---

## Ciclo de vida de un archivo

```
  1. Declarar        ofstream archivo("nombre.txt", ios::out);
        │
        ▼
  2. Verificar       if (!archivo) { cerr << "Error"; exit(1); }
        │
        ▼
  3. Usar            archivo << dato;     (escritura)
                     archivo >> variable; (lectura)
        │
        ▼
  4. Cerrar          automático al terminar la función
                     (también se puede llamar archivo.close())
```

> El archivo se cierra solo cuando el objeto `ofstream` o `ifstream` sale de su función. No es necesario cerrarlo manualmente, aunque se puede hacer con `.close()`.

---

## Verificación de apertura

Siempre se debe verificar que el archivo se abrió correctamente antes de usarlo.

```
ofstream archivoSalida("datos.txt", ios::out);

if (!archivoSalida)           ←  si el archivo NO se pudo abrir
{
    cerr << "Error";          ←  mostrar mensaje de error
    exit(1);                  ←  terminar el programa
}

// si llegamos aquí, el archivo se abrió bien
archivoSalida << datos;
```

---

## Agregar datos sin borrar (ios::app)

```cpp
ofstream archivoSalida("datos.txt", ios::app);
```

```
Antes:                         Después de escribir "Carlos":
┌─────────────────────┐        ┌─────────────────────┐
│ 123456 Juan         │        │ 123456 Juan         │
│ 894560 Adriana      │   →    │ 894560 Adriana      │
└─────────────────────┘        │ 112233 Carlos       │
                                └─────────────────────┘
```

Con `ios::out` el resultado sería:

```
┌─────────────────────┐
│ 112233 Carlos       │   ← Juan y Adriana se perdieron
└─────────────────────┘
```

---

## Resumen visual rápido

```
ESCRIBIR        ofstream archivo("nombre.txt", ios::out);
                archivo << dato;

LEER            ifstream archivo("nombre.txt", ios::in);
                archivo >> variable;

AGREGAR         ofstream archivo("nombre.txt", ios::app);
                archivo << dato;

VERIFICAR       if (!archivo) { cerr << "Error"; exit(1); }

CERRAR          automático al salir de la función
```