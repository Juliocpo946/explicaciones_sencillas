# Arreglos en C++

---

## ¿Qué es un arreglo?

Un arreglo es una fila de cajitas en memoria. Cada cajita guarda un valor del mismo tipo y tiene un número de posición llamado **índice**, que siempre empieza en **0**.

```
Declaración:
    int lista[5];

Visualización en memoria:
    ┌────────┬────────┬────────┬────────┬────────┐
    │        │        │        │        │        │
    └────────┴────────┴────────┴────────┴────────┘
    lista[0] lista[1] lista[2] lista[3] lista[4]

Después de asignar valores:
    lista[0] = 10;
    lista[1] = 25;
    lista[2] = 7;
    lista[3] = 42;
    lista[4] = 3;

    ┌────────┬────────┬────────┬────────┬────────┐
    │   10   │   25   │   7    │   42   │   3    │
    └────────┴────────┴────────┴────────┴────────┘
    lista[0] lista[1] lista[2] lista[3] lista[4]
```

> **Regla de oro:** Si declaras `int lista[5]`, los índices válidos son del 0 al 4. El índice 5 no existe y acceder a él es un error.

---

## Tipos de arreglos

### Unidimensional — una sola fila

```
int lista[10];

┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │  ← índices
└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
  [0] [1] [2] [3] [4] [5] [6] [7] [8] [9]
```

### Bidimensional (matriz) — filas y columnas

```
int b[3][5];

         col 0  col 1  col 2  col 3  col 4
        ┌──────┬──────┬──────┬──────┬──────┐
fila 0  │ b[0][0] b[0][1] b[0][2] b[0][3] b[0][4] │
        ├──────┴──────┴──────┴──────┴──────┤
fila 1  │ b[1][0] b[1][1] b[1][2] b[1][3] b[1][4] │
        ├──────┬──────┬──────┬──────┬──────┤
fila 2  │ b[2][0] b[2][1] b[2][2] b[2][3] b[2][4] │
        └──────┴──────┴──────┴──────┴──────┘

Forma simplificada:
        ┌────┬────┬────┬────┬────┐
fila 0  │    │    │    │    │    │
        ├────┼────┼────┼────┼────┤
fila 1  │    │    │    │    │    │
        ├────┼────┼────┼────┼────┤
fila 2  │    │    │    │    │    │
        └────┴────┴────┴────┴────┘
```

---

## Leer y llenar arreglos unidimensionales

### Llenar con un ciclo (escritura)

```
El ciclo recorre cada posición y pide un valor al usuario:

i = 0 → cin >> lista[0]   ┌───┐
i = 1 → cin >> lista[1]   │ ? │ ← el usuario escribe aquí
i = 2 → cin >> lista[2]   └───┘
...
i = 9 → cin >> lista[9]
```

```cpp
int lista[10];

for (int i = 0; i <= 9; i++) {
    cout << "Ingresa el elemento: ";
    cin >> lista[i];
}
```

### Imprimir con un ciclo (lectura)

```
i = 0 → cout << lista[0]  →  imprime: Ana
i = 1 → cout << lista[1]  →  imprime: Carlos
i = 2 → cout << lista[2]  →  imprime: Pablo
```

```cpp
string nombres[] = {"Ana", "Carlos", "Pablo"};

for (int i = 0; i < 3; i++) {
    cout << nombres[i] << endl;
}
```

---

## Leer y llenar arreglos bidimensionales

Se necesitan **dos ciclos anidados**: el externo recorre filas, el interno recorre columnas.

```
Orden de recorrido (fila por fila):

        col 0  col 1  col 2
        ┌─────┬─────┬─────┐
fila 0  │  1  →  2  →  3  │  ← i=0, j avanza de 0 a 2
        ├─────┼─────┼─────┤
fila 1  │  4  →  5  →  6  │  ← i=1, j avanza de 0 a 2
        ├─────┼─────┼─────┤
fila 2  │  7  →  8  →  9  │  ← i=2, j avanza de 0 a 2
        └─────┴─────┴─────┘
```

```cpp
// Escritura
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        cin >> b[i][j];
    }
}

// Lectura
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        cout << b[i][j] << " ";
    }
    cout << endl;
}
```

### Modificar una fila completa

```
Asignar 5 a toda la fila 2:

        col 0  col 1  col 2
        ┌─────┬─────┬─────┐
fila 0  │     │     │     │  ← sin cambios
        ├─────┼─────┼─────┤
fila 1  │     │     │     │  ← sin cambios
        ├─────┼─────┼─────┤
fila 2  │  5  │  5  │  5  │  ← a[2][0], a[2][1], a[2][2] = 5
        └─────┴─────┴─────┘
```

```cpp
for (int j = 0; j < 3; j++) {
    a[2][j] = 5;
}
```

### Modificar una columna completa

```
Asignar 10 a toda la columna 0:

        col 0  col 1  col 2
        ┌─────┬─────┬─────┐
fila 0  │ 10  │     │     │
        ├─────┼─────┼─────┤
fila 1  │ 10  │     │     │
        ├─────┼─────┼─────┤
fila 2  │ 10  │     │     │
        └─────┴─────┴─────┘
```

```cpp
for (int i = 0; i < 3; i++) {
    a[i][0] = 10;
}
```

---

## Búsqueda secuencial

Recorre el arreglo elemento por elemento buscando un valor. Si lo encuentra devuelve su posición; si no, devuelve -1.

```
Arreglo: [ 8 | 15 | 3 | 27 | 11 ]
            [0]  [1] [2]  [3]  [4]

Buscando el valor 27:

  Paso 1: datos[0] = 8  ≠ 27  → seguir
  Paso 2: datos[1] = 15 ≠ 27  → seguir
  Paso 3: datos[2] = 3  ≠ 27  → seguir
  Paso 4: datos[3] = 27 = 27  → ENCONTRADO en posición 3
  Paso 5: (no se necesita llegar aquí)
```

### Implementación que retorna la posición

```cpp
int buscar(int datos[], int n, int valorBuscado) {
    int posicion = -1;

    for (int i = 0; i <= n - 1; i++) {
        if (datos[i] == valorBuscado) {
            posicion = i;
        }
    }

    return posicion;    // -1 si no se encontró
}
```

### Implementación con bandera (se detiene al primer resultado)

```cpp
void buscar(int datos[], int n, int valorBuscado) {
    int bandera = 0;

    for (int i = 0; i < n; i++) {
        if (datos[i] == valorBuscado) {
            cout << "Encontrado en posicion " << i << endl;
            bandera = 1;
            i = n;    // fuerza el fin del ciclo
        }
    }

    if (bandera == 0) {
        cout << "Valor no encontrado" << endl;
    }
}
```

> **Diferencia clave:** La primera implementación sigue recorriendo aunque ya encontró el valor (útil si hay duplicados). La segunda para al primer resultado (más eficiente si el arreglo es grande y solo necesitas el primero).

---

## Búsqueda en matrices (arreglos bidimensionales)

### Buscar en toda la matriz

```
Buscando el valor 7 en esta matriz:

        col 0  col 1  col 2
        ┌─────┬─────┬─────┐
fila 0  │  1  │  4  │  9  │
        ├─────┼─────┼─────┤
fila 1  │  2  │  7  │  5  │  ← ENCONTRADO en [1][1]
        ├─────┼─────┼─────┤
fila 2  │  8  │  3  │  6  │
        └─────┴─────┴─────┘
```

```cpp
for (int i = 0; i < tamanoFilas; i++) {
    for (int j = 0; j < tamanoColumnas; j++) {
        if (matriz[i][j] == valorBuscado)
            cout << "Encontrado en [" << i << "][" << j << "]" << endl;
    }
}
```

### Buscar solo en una fila específica

```
Buscar en la fila 1 únicamente:

        col 0  col 1  col 2
        ┌─────┬─────┬─────┐
fila 0  │     │     │     │  ← ignorada
        ├─────┼─────┼─────┤
fila 1  │  2  →  7  →  5  │  ← solo aquí
        ├─────┼─────┼─────┤
fila 2  │     │     │     │  ← ignorada
        └─────┴─────┴─────┘
```

```cpp
int fila = 1;

for (int j = 0; j < tamanoColumnas; j++) {
    if (matriz[fila][j] == valorBuscado)
        cout << "Encontrado en [" << fila << "][" << j << "]" << endl;
}
```

### Buscar solo en una columna específica

```
Buscar en la columna 0 únicamente:

        col 0  col 1  col 2
        ┌─────┬─────┬─────┐
fila 0  │  1  │     │     │  ← solo col 0
        ├─────┼─────┼─────┤
fila 1  │  2  │     │     │  ← solo col 0
        ├─────┼─────┼─────┤
fila 2  │  8  │     │     │  ← solo col 0
        └─────┴─────┴─────┘
         ↑ recorrida verticalmente
```

```cpp
int columna = 0;

for (int i = 0; i < tamanoFilas; i++) {
    if (matriz[i][columna] == valorBuscado)
        cout << "Encontrado en [" << i << "][" << columna << "]" << endl;
}
```

---

## Resumen visual rápido

```
DECLARAR        int lista[5];             una fila de 5 enteros
ACCEDER         lista[2]                  tercer elemento (índice 2)
RECORRER 1D     for i de 0 a n-1
RECORRER 2D     for i (filas) + for j (columnas) anidados
BUSCAR          comparar cada elemento con el valor buscado
RESULTADO       posición encontrada, o -1 si no existe
```