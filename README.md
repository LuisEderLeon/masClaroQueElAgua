# Mas CLARO que el agua

      ⢀⣤⣶⡾⡿⠟⠿⠿⠿⠻⣷⣶⣤⣀      
    ⣠⣾⢿⢏⡡⣄⣠⢠⣀⣄⣠⣀⣄⣉⠞⣿⢷⣤⡀   
  ⣠⣾⢿⣽⣻⢾⣽⣞⣷⣻⣞⡾⣵⣯⢾⣭⡿⣞⣯⣿⣳⣄  
 ⣴⡿⣽⣻⡾⣯⣿⢾⣽⡾⣷⣻⢿⣽⡾⣿⣽⣻⣽⣟⣾⣽⣻⣧ 
⢰⡿⣽⣟⡷⣿⣽⢾⣻⣷⣻⣽⢯⣿⢾⣽⡷⣯⡇⢸⡾⡽⠊⣱⢿⡇
⣿⢿⡝⢊⣉⣉⠺⣿⠉⣷⠻⠽⠿⣽⠻⠾⢽⡷⠷⠺⣍⣠⡾⣯⣟⣿
⣿⣻ ⣿⢯⣟⠶⢮ ⡧⠔⢓ ⣿ ⣶⡎⢰⢶⡆⠸⣏⣉⣉⣸⢿
⣿⡽⣧⣈⣉⣉⣤⡿⣀⣇⣘⣛⣀⡿⣀⣷⣳⣈⣉⣁⣼⣻⢾⣽⢯⣿
⠸⣟⣷⣯⢿⣽⣾⣻⢿⡽⣯⢿⣽⣻⣟⡷⣿⣽⣻⣽⢾⣻⣯⣟⣯⡇
 ⠻⣷⢯⣿⣞⡷⣟⣯⣿⣻⢯⡷⣟⡾⣟⣷⣯⣟⣾⢿⣽⣞⣯⡟ 
  ⠙⢿⣳⣯⢿⣻⣽⡾⣽⢯⣻⣝⣻⡽⣾⣳⡿⣽⣻⣾⡽⠋  
    ⠛⢽⣟⣯⡷⣟⣯⢿⣱⢯⣷⣻⣽⢷⣟⣿⡳⠛⠁   
      ⠉⠛⠹⠿⣽⣻⣯⣿⢾⣽⠾⠟⠛⠈                   

Simple proyecto de Python, que desea ayudar con la gestion de usuarios y servicios por medio de diferentes funciones, faciles de usar para un usuario sin conocimientos tecnicos.




## CRUDs

El proyecto posee dos CRUDs (Create, Read, Update, Delete) especificos para los usuarios y los servicios, y todos los cambios quedan registrados en sus respectivos JSON.

### Usuarios

El CRUD de usuarios permite crear, enlistar, modificar y eliminar usuarios, y adicionalmente, tambien se pueden asociar ciertos servicios a un usuario, dependiendo de como se desee usar.

### Servicios

El CRUD de servicios es mas simple que el de usuarios, puesto que solo dispone de crear, enlistar, modificar y eliminar servicios.

## Ventas

El programa trae tres funcionalidades relacionadas con las ventas de los clientes. Esto con el propósito de mejorar la gestión de estas.

### Consultar

Al ingresar el documento de un cliente, el usuario podra ver todas las compras que este ha tenido, lo que facilita el orden y la contabilidad de las mismas.

### Añadir

Luego de ver las ventas de un cliente, el programa le preguntará al usuario si desea añadirle una venta al cliente. Esto con el fin de facilitar el manejo de las ventas al siempre ver cuales son las ventas actuales de un cliente y asi evitar error humano de repetir el registro de una venta.

### Sugerir

Existe una función llamada Sugerir Ventas a un cliente, que como su nombre lo indica, le dara al usuario un producto que le deberia recomendar al cliente, basado en sus compras anteriores.

## Reportes

El programa cuenta con un sistema de reportes robusto, dentro del archivo reportes.txt, donde se guarda información de todos los errores que se puedan llegar a cometer durante la ejecución del programa. Estos reportes contienen la fecha y una breve descripción del error ocurrido. Entre los errores más comunes esta el ingresar una letra al momento de pedirle un número al usuario. Debido a lo robusto que es el sistema de reportes, el programa nunca se detendrá si el usuario no lo desea así. 
