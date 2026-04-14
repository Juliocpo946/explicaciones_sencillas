# Preguntas que pudieron faltar

---

## Git — Muy preguntado en cualquier entrevista

**¿Qué es Git?**
Es un sistema de control de versiones. Permite guardar el historial de cambios de un proyecto, trabajar en equipo sin pisarse el código y regresar a versiones anteriores si algo sale mal.

**¿Diferencia entre Git y GitHub?**
Git es la herramienta que corre en tu computadora. GitHub es una plataforma en la nube donde subes tu repositorio para compartirlo o trabajar en equipo. También existen GitLab y Bitbucket que hacen lo mismo.

**¿Qué es un commit?**
Es una fotografía del estado del código en un momento específico. Cada commit tiene un mensaje que describe qué cambió y un identificador único.

**¿Qué es una rama (branch)?**
Es una línea de desarrollo independiente. Se usa para trabajar en una funcionalidad nueva sin afectar el código principal. Cuando terminas, haces un merge para unirla de vuelta.

**¿Diferencia entre `merge` y `rebase`?**
`merge` une dos ramas creando un commit de fusión, conserva el historial completo. `rebase` mueve los commits de una rama encima de otra, genera un historial más limpio y lineal pero reescribe el historial.

**Comandos más preguntados:**
- `git init` — inicia un repositorio
- `git clone` — copia un repositorio remoto
- `git add .` — prepara todos los cambios
- `git commit -m "mensaje"` — guarda los cambios
- `git push` — sube cambios al remoto
- `git pull` — baja cambios del remoto
- `git branch` — lista o crea ramas
- `git checkout` — cambia de rama
- `git merge` — une ramas
- `git status` — muestra el estado actual

---

## Conceptos Generales de Programación

**¿Qué es una API REST?**
Es un estilo de arquitectura para comunicar sistemas a través de HTTP. Usa los métodos GET, POST, PUT, DELETE para operar sobre recursos. La respuesta generalmente es JSON. REST tiene reglas como ser stateless (el servidor no recuerda al cliente entre peticiones).

**¿Qué es el protocolo HTTP?**
Es el protocolo de comunicación entre cliente y servidor en la web. El cliente manda una petición con un método y el servidor responde con un código de estado y datos.

**Códigos de estado HTTP más comunes:**
- `200` — OK, todo bien
- `201` — Created, recurso creado
- `400` — Bad Request, la petición tiene errores
- `401` — Unauthorized, no autenticado
- `403` — Forbidden, autenticado pero sin permiso
- `404` — Not Found, recurso no existe
- `500` — Internal Server Error, error en el servidor

**¿Qué es CORS?**
Cross-Origin Resource Sharing. Es una política de seguridad del navegador que bloquea peticiones a un dominio diferente al de la página actual. Se configura en el servidor para permitir o bloquear orígenes específicos.

**¿Qué es un token JWT?**
JSON Web Token. Es una forma de autenticación stateless. El servidor genera un token firmado con los datos del usuario, el cliente lo guarda y lo manda en cada petición. El servidor lo verifica sin necesitar base de datos.

**¿Diferencia entre autenticación y autorización?**
Autenticación es verificar quién eres (login, contraseña). Autorización es verificar qué puedes hacer (permisos, roles). Primero se autentica, luego se autoriza.

**¿Qué es una base de datos relacional vs no relacional?**
Relacional (SQL) organiza datos en tablas con filas y columnas, tienen relaciones entre sí. Ejemplos: MySQL, PostgreSQL. No relacional (NoSQL) guarda datos en documentos, clave-valor o grafos, más flexible en estructura. Ejemplos: MongoDB, Redis.

---

## Conceptos de Frontend

**¿Qué es SPA (Single Page Application)?**
Es una aplicación web que carga una sola página HTML y actualiza el contenido dinámicamente sin recargar. React, Vue y Angular son frameworks para construir SPAs. La navegación es más rápida porque solo se piden datos, no páginas completas.

**¿Qué es el Virtual DOM?**
Es una copia en memoria del DOM real. Frameworks como React trabajan sobre el Virtual DOM, calculan los cambios mínimos necesarios y solo actualizan esas partes en el DOM real. Esto lo hace más eficiente que manipular el DOM directamente.

**¿Qué es lazy loading?**
Es cargar recursos solo cuando se necesitan en lugar de cargar todo al inicio. Por ejemplo, cargar imágenes solo cuando el usuario llega a esa parte de la página, o cargar módulos de JavaScript solo cuando el usuario navega a esa sección.

**¿Qué es el localStorage y sessionStorage?**
Ambos guardan datos en el navegador. `localStorage` persiste aunque cierres el navegador. `sessionStorage` se borra al cerrar la pestaña. Se usan para guardar preferencias, tokens o estado de la aplicación del lado del cliente.

**¿Qué es accesibilidad web (a11y)?**
Es que el sitio pueda ser usado por personas con discapacidades. Incluye usar HTML semántico, atributos `alt` en imágenes, buen contraste de colores, navegación por teclado y atributos ARIA para lectores de pantalla.

---

## Conceptos de Backend

**¿Qué es un middleware?**
Es una función que se ejecuta entre que llega la petición y que el servidor responde. Se usa para autenticar, validar datos, registrar logs o manejar errores. En Express (Node.js) y Laravel (PHP) es un concepto central.

**¿Qué es un ORM?**
Object Relational Mapper. Es una herramienta que permite interactuar con la base de datos usando objetos y clases en lugar de escribir SQL directo. Eloquent en Laravel y Prisma en Node.js son ejemplos populares.

**¿Qué es la inyección de dependencias?**
Es un patrón donde una clase no crea sus propias dependencias sino que las recibe desde afuera. Hace el código más fácil de probar y mantener porque puedes cambiar las dependencias sin modificar la clase.

**¿Qué es el principio SOLID?**
Son 5 principios de diseño de software para código mantenible y escalable. S: responsabilidad única. O: abierto para extensión, cerrado para modificación. L: sustitución de Liskov. I: segregación de interfaces. D: inversión de dependencias.

**¿Qué son las variables de entorno?**
Son variables de configuración que se guardan fuera del código, en el sistema operativo o en un archivo `.env`. Se usan para guardar credenciales, URLs de bases de datos, claves de API y cualquier valor que cambie entre entornos (desarrollo, producción).

---

## Preguntas de Lógica y Actitud

**¿Cómo manejas un bug que no puedes resolver?**
Respuesta sugerida: Primero intento reproducirlo de forma consistente, luego reviso los logs, busco en la documentación y en foros como Stack Overflow. Si sigo sin resolverlo pido ayuda a un compañero porque dos pares de ojos ven más que uno.

**¿Cómo te mantienes actualizado en tecnología?**
Respuesta sugerida: Leo documentación oficial, sigo blogs técnicos, veo tutoriales y practico proyectos personales. También mencionaría comunidades como Dev.to o YouTube.

**¿Has trabajado con metodologías ágiles?**
Respuesta sugerida: Scrum o Kanban. Scrum trabaja en sprints de tiempo fijo con ceremonias como daily, sprint planning y retrospectiva. Kanban usa un tablero visual con columnas de estado para gestionar el flujo de trabajo.

**¿Qué harías si no entiendes un requerimiento?**
Respuesta sugerida: Preguntar antes de asumir. Es mejor aclarar dudas al inicio que desarrollar algo incorrecto y tener que rehacerlo. Pediría ejemplos concretos o casos de uso para entender mejor lo que se necesita.

---
