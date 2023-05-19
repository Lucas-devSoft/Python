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

![Con Conexión](https://github.com/Lucas-devSoft/Python/assets/111676352/5d8ae635-cbdf-41ca-865a-f4fda2ffab58)

*La imagen muestra información detallada como (tipo de conexión, nombre de la BD a la que está conectada al igual que su colección y la versión de MongoDB). En este caso en particular La información que trae es la base de datos por defecto, es decir la originada por código, pero en el caso de que el usuario llegue a generar una con un nombre específico se conectara a ella y el banner cambiará.*

- Banner sin Conexión

![Sin Conexión](https://github.com/Lucas-devSoft/Python/assets/111676352/d652da2a-80ec-47b7-9eb3-4b33fec5ad77)

*La imagen muestra el cambio de estado a "sin conexión" porque el usuario ha elegido no conectarse a la base de datos. El Banner demostró que su estado está en modo sin conexión, por lo tanto, no se guardará información.*

- Interacciones

La función de cada interacción en el programa es para que el usuario elija qué es lo que desea hacer y espera a recibir una respuesta precisa en referencia a lo solicitado para continuar con cada funcionalidad del programa.

- Solicitud del Nombre

![Nombre](https://github.com/Lucas-devSoft/Python/assets/111676352/70aff83b-1a3b-4f2f-ba0d-9b13b26ac759)

*Esta funcionalidad esta para brindar una gentil bienvenida al usuario y además su otra utilidad está en el caso de generar una conexión a la base de datos agregar su correspondencia a cada operación guardada.*

- Conexión a la Base de Datos

![Conexión](https://github.com/Lucas-devSoft/Python/assets/111676352/2a218909-30b3-4307-976a-1d005e991a9b)

*En esta funcionalidad se realiza la conexión a la base de datos. Caso de escribir ‘sí’ se genera la conexión, caso contrario ‘no’ va directamente al Menú de la Calculadora, destacando en el Banner un mensaje de recordatorio que el usuario está en modo sin conexión.*

- Tipo de Conexión

![Tipo de conexión](https://github.com/Lucas-devSoft/Python/assets/111676352/b0ec526f-e399-4cd2-ba75-8e6210148ad1)

*En esta funcionalidad solicita que tipo de conexión quiere generar el usuario con MongoDB, es decir de forma local o bien mediante cuenta MongoDB Atlas para realizar el guardado de los datos.*

- Crear una Base de Datos con un nombre específico

![Creando una BD](https://github.com/Lucas-devSoft/Python/assets/111676352/06c28543-a130-434d-b9e4-ee068f14a9af)

*En esta funcionalidad de este Menú es que el usuario elija si quiere avanzar creando una base de datos con un nombre en específico que él elija o bien avanzar directamente desde una base de datos por defecto que yo nombre directamente en el código para que se creara en cuanto el usuario ponga que ‘no’ y pueda cargar sus datos ahí. En el caso de ‘no’ la Base de datos que se generará se llamara “Calculadora” con una colección llamada “Historial” en el caso de ‘sí’ se llamara como el usuario haya elegido.*

- Base de Datos creada


![](https://github.com/Lucas-devSoft/Python/assets/111676352/928deae3-29ae-4976-8156-c8619cb06ff0)

*La funcionalidad de esta parte del programa es que el usuario pueda crear su base de datos con un nombre en específico y pueda cargar sus datos ahí. Si la Base de datos que quiere crear contiene el mismo nombre de una base de datos ya existente, optará por arrojar otro tipo de mensaje como “La base de datos ya existe y está activada para guardar.*

- Errores

*La función del error es advertir durante todo el programa que el usuario ha insertado una respuesta incorrecta, por lo que para poder continuar va a tener que reintentar hasta que inserte datos correctos y así mismo poder continuar con el flujo del programa.*

- Error (Solicitud del Nombre)

![](https://github.com/Lucas-devSoft/Python/assets/111676352/89011179-e27e-4940-9abc-d606bdcaea7a)

- Error (Conexión a la Base de Datos)

![](https://github.com/Lucas-devSoft/Python/assets/111676352/93193661-d58d-40db-bf00-9936fa3f3a9e)
 
- Error (Tipo de Conexión)

![](https://github.com/Lucas-devSoft/Python/assets/111676352/0585cbf8-83ac-447a-ad16-b31c63b3ceb9)

- Error (Menú)

![](https://github.com/Lucas-devSoft/Python/assets/111676352/963442f9-e1f6-4a06-928f-8032229a47d8)

<hr>

## Ejecución del Proyecto

Alternativas para el correcto funcionamiento del programa.

- Alternativa uno.

  1. Descargar el proyecto entero "Calculadora", contiene el entorno virtual ya con todo preparado para correr. [Descargalo Aquí](https://drive.google.com/drive/u/1/folders/1b8E-k7cfCAzpT5wKOZRedXX86UHuEL9j "Google Drive")

  2. Estando en la carpeta raiz "Calculadora" activamos el entorno virtual. [+Info](https://docs.python.org/es/3/tutorial/venv.html)
   
      En el CMD de Windows se activa de esta forma:

         ``.env\Scripts\activate.bat``

       En Unix o MacOS, ejecuta:

          ``source .env/bin/activate``

       Cuando ingresamos correctamente al entorno virtual delante del Path nos aparecera el nombre del entorno de esta forma (.env). 

       ![](https://github.com/Lucas-devSoft/Python/assets/111676352/0c3d8fc2-11df-401d-9976-7c346ced3f13)

  3. Ya podremos ejecutar el programa.

      ``python Menu.py``

  4. Para desactivar el entorno virtual.

      ``deactivate``

- Alternativa dos.

  1. Se necesita tener instalado Python (Ultima Versión 3.11.3).  [Descargar de Aquí](https://www.python.org/downloads/ "Página oficial de Python") 

  2. ¿Descargaste solo los Scripts? ¿no queres instalar módulos en tu sistema?, creá tu propio entorno virtual en la carpeta raíz de los Scripts. 

     ``python -m venv Nombre_del_entorno``

  3. Entramos al nuevo entorno virtual estando adentro es posible que se deba actualizar el PIP.

      En el CMD de Windows se activa de esta forma.

        ``.env\Scripts\activate.bat``

      En Unix o MacOS, ejecuta:

        ``source .env/Scripts/activate``

      Para actualizar el PIP se debera colocar el siguiente comando(Windows).

        ``python -m pip install --upgrade pip``

  4. Una vez actualizado instalamos los módulos de trabajo

     ``pip install colorama`` y ``pip install pymongo``
   
  5. Ya podremos ejecutar el programa.

     ``python Menu.py``
   
## Desarrollador

![Open](https://github.com/Lucas-devSoft/Python/assets/111676352/6d78f829-b40e-4b95-9d98-c6ba05e26f03) <br>
[Lucas E. Sanchez](https://www.linkedin.com/in/lucasdevsoft2022/ "Perfil Linkedin")   |   [Pagina Web](https://lucas-devsoft.github.io/CV/ "Curriculum Web")



