<img width = "950px" align = "center" src="https://github.com/Lucas-devSoft/Python/assets/111676352/69fa3548-30c5-4304-b9e1-01619683b517"></img> 

# Primer Proyecto Personal
 
## Sección de Índices 

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Herramientas utilizadas](#herramientas-utilizadas)
- [Funcionalidades](#funcionalidades)
  - Banner        
    - Con Conexión
    - Sin conexion         
  - Interacciones
  - Mensajes de Errores
- [Ejecución del Proyecto](#ejecución-del-proyecto)
- [Desarrollador](#desarrollador)
 
## Descripción del Proyecto
 
Está desarrollado en entorno Windows, está diseñado para ejecutarse en la terminal del sistema operativo. El proyecto es una simple imitación de una calculadora, salvo que lleva otras funcionalidades para retornar que la clásica calculadora, el usuario interactuará con ella y deberá de elegir  si quiere guardar o no la información de sus operaciones a través de la base de datos MongoDB que implemente.
 
## Herramientas Utilizadas
 
### Entorno Virtual

En el proyecto utilizo los módulos necesarios a través de un entorno virtual para facilitar el acceso a la aplicación y no tener que descargar absolutamente nada en el sistema del usuario, ya que está todo instalado en el mismo entorno virtual para correrlo en consola de sus sistema, si le apetece probarlo lo estare dejando abajo. [Descargar](#ejecución-del-proyecto)
 
### Módulos
 
En el proyecto utilizo los módulos **colorama** y **pymongo** que son módulos que no vienen por defecto al instalar Python, por ende se deben de instalar a través de ``pip install``. Reitero que dejaré estos módulos ya instalados en el entorno virtual para no instalar nada en su sistema.

### Programación
 
El programa está codificado con el lenguaje de programación **Python** en el entorno de desarrollo **Visual Studio Code**, los codigos estan separados en módulos para mantener la facilitadad de generar cualquier cambio del programa retocando una parte específica, además de esta forma el código permanece mas ordenado y descriptivo.
 
### Base de Datos
 
El proyecto trabaja con la base de datos **MongoDB** está implementada para generar un historial de operaciones.
 
## Funcionalidades
 
- Banner

La función del banner en el programa está para mostrar los cambios de estado en la conexión de base de datos que va generando el usuario, en cada caso de conexión se va a ir detallando la información del mismo y va a ir cambiar dependiendo si se conecta o no.
 
- Banner con Conexión

La imagen muestra información detallada como (tipo de conexión, nombre de la BD a la que está conectada al igual que su colección y la versión de MongoDB). En este caso en particular La información que trae es la base de datos por defecto, es decir la originada por código, pero en el caso de que el usuario llegue a generar una con un nombre específico se conectara a ella y el banner cambiará.

![Con Conexión](https://github.com/Lucas-devSoft/Python/assets/111676352/5d8ae635-cbdf-41ca-865a-f4fda2ffab58)

- Banner sin Conexión

La imagen muestra el cambio de estado a "sin conexión" porque el usuario ha elegido no conectarse a la base de datos. El Banner demostró que su estado está en modo sin conexión, por lo tanto, no se guardará información.

![Sin Conexión](https://github.com/Lucas-devSoft/Python/assets/111676352/d652da2a-80ec-47b7-9eb3-4b33fec5ad77)

- Interacciones

La función de cada interacción en el programa es para que el usuario elija qué es lo que desea hacer y espera a recibir una respuesta precisa en referencia a lo solicitado para continuar con cada funcionalidad del programa.

- Solicitud del Nombre

Esta funcionalidad esta para brindar una gentil bienvenida al usuario y además su otra utilidad está en el caso de generar una conexión a la base de datos agregar su correspondencia a cada operación guardada.

![Nombre](https://github.com/Lucas-devSoft/Python/assets/111676352/70aff83b-1a3b-4f2f-ba0d-9b13b26ac759)

- Conexión a la Base de Datos

En esta funcionalidad se realiza la conexión a la base de datos. Caso de escribir ‘sí’ se genera la conexión, caso contrario ‘no’ va directamente al Menú de la Calculadora, destacando en el Banner un mensaje de recordatorio que el usuario está en modo sin conexión.

![Conexión](https://github.com/Lucas-devSoft/Python/assets/111676352/2a218909-30b3-4307-976a-1d005e991a9b)

- Tipo de Conexión

En esta funcionalidad solicita que tipo de conexión quiere generar el usuario con MongoDB, es decir de forma local o bien mediante cuenta MongoDB Atlas para realizar el guardado de los datos.

![Tipo de conexión](https://github.com/Lucas-devSoft/Python/assets/111676352/b0ec526f-e399-4cd2-ba75-8e6210148ad1)

- Crear una Base de Datos con un nombre específico

En esta funcionalidad de este Menú es que el usuario elija si quiere avanzar creando una base de datos con un nombre en específico que él elija o bien avanzar directamente desde una base de datos por defecto que yo nombre directamente en el código para que se creara en cuanto el usuario ponga que ‘no’ y pueda cargar sus datos ahí. En el caso de ‘no’ la Base de datos que se generará se llamara “Calculadora” con una colección llamada “Historial” en el caso de ‘sí’ se llamara como el usuario haya elegido.

![Creando una BD](https://github.com/Lucas-devSoft/Python/assets/111676352/06c28543-a130-434d-b9e4-ee068f14a9af)

- Base de Datos Creada y Existente

En esta funcionalidad el usuario puede generar su BD con el nombre que desee y pueda insertar sus datos dentro de la misma. Esta funcionalidad también detecta si la BD existe o no, si la BD que quiere crear ya existe arrojara “La base de datos ya existe y está activada para guardar".

![BD Creada](https://github.com/Lucas-devSoft/Python/assets/111676352/6d6ddc32-f822-4c07-b243-845fa0fc99b0)
![BD Existente](https://github.com/Lucas-devSoft/Python/assets/111676352/33cd9cb3-a4f3-42d5-8d12-290a4fa57e51)

- Muestra el Historial de operaciones

Esta funcionalidad se activa cuando el usuario está conectado, va a poder visualizar todas sus operaciones en el transcurso del programa siempre y cuando este conectado, en caso de no estarlo aparecera un recordatorio de que el usuario esta sin conexión.

![Otro Menu](https://github.com/Lucas-devSoft/Python/assets/111676352/390f7fe3-3d94-4e86-8213-259bca1ff84e)
![Recordatorio](https://github.com/Lucas-devSoft/Python/assets/111676352/ab56064c-67cf-4e46-80c8-6be0e0c8834e)

<hr>


- Mensajes de Errores

La función del error es advertir durante todo el programa que el usuario ha insertado una respuesta incorrecta, por lo tanto, para poder continuar con el flujo del programa debera reintentar hasta insertar datos correctos sino los mensajes de error persistiran.

- Error (Solicitud del Nombre)

![Error Nombre](https://github.com/Lucas-devSoft/Python/assets/111676352/73aac8b5-c898-400f-9e35-8715032bb419)

- Error (Conexión a la Base de Datos)

![Error Conexión](https://github.com/Lucas-devSoft/Python/assets/111676352/b2c43d73-aefe-4fec-af76-5bada5da62b3)

- Error (Menú)

![Error Menu](https://github.com/Lucas-devSoft/Python/assets/111676352/e35dba11-c4be-49bb-9bb0-5ee3e4daf5ec)

- Error (Tipo de Conexión)

![Error Tipo Conexión](https://github.com/Lucas-devSoft/Python/assets/111676352/4e2f4f53-1e4e-4bf5-9261-4d9e409a1846)

<hr>

## Ejecución del Proyecto

Para correr este programa contamos con los siguientes pasos.
  
  1. Se necesita tener instalado Python en el sistema (Ultima Versión 3.11.3). [Descargar de Aquí](https://www.python.org/downloads/ "Página oficial de Python") 
  
  2. Descargas el proyecto completo "Calculadora" o solo el entorno virtual que contiene los moódulos necesarios para correrlo. [Descargalo Aquí](https://drive.google.com/drive/u/1/folders/1b8E-k7cfCAzpT5wKOZRedXX86UHuEL9j "Google Drive")

  3. Si descargaste el proyecto completo "Calculadora" debemos activar el entorno virtual. [+Info](https://docs.python.org/es/3/tutorial/venv.html "Documentación venv")
   
      En el CMD de Windows se activa de esta forma:

         ``.env\Scripts\activate.bat``

       En Unix o MacOS, ejecuta:

          ``source .env/Scripts/activate``

       Cuando ingresamos correctamente al entorno virtual delante del Path nos aparecera el nombre del entorno de esta forma (.env). 

       ![Entorno Virtual](https://github.com/Lucas-devSoft/Python/assets/111676352/f93faa08-999c-4afb-ade5-afedb03a9eea)

  4. En la consola estando en la carpeta raíz "Calculadora" ya podremos ejecutar el programa.

      ``python menu.py``

  5. Para desactivar el entorno virtual.

      ``deactivate``
   
## Desarrollador

![Open](https://github.com/Lucas-devSoft/Python/assets/111676352/6d78f829-b40e-4b95-9d98-c6ba05e26f03) <br>
[Lucas E. Sanchez](https://www.linkedin.com/in/lucasdevsoft2022/ "Perfil Linkedin")   |   [Pagina Web](https://lucas-devsoft.github.io/CV/ "Curriculum Web")



