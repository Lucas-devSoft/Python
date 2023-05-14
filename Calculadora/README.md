<img width = "950px" align = "center" src="https://github.com/Lucas-devSoft/Python/assets/111676352/69fa3548-30c5-4304-b9e1-01619683b517"></img> 

# Primer Proyecto Personal
 
## Sección de Índices 

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Herramientas utilizadas](#herramientas-utilizadas)
- [Funcionalidades](#funcionalidades)
  - Banner        
    - Conexión
    - Sin conexion         
  - Menus
  - Mensajes de Errores
- [Ejecución del Proyecto](#ejecución-del-proyecto)
- [Desarrollador](#desarrollador)
 
## Descripción del Proyecto
 
El proyecto está desarrollado en entorno Windows, su funcionamiento está diseñado para ejecutarse en la terminal de su sistema operativo. Es una simple imitación de una calculadora, salvo que lleva otras funcionalidades para retornar que la clásica calculadora, el usuario deberá optar por guardar o no su historial de operaciones en una base de datos que implemente.
 
## Herramientas Utilizadas
 
### Entorno Virtual

En el proyecto utilizo el entorno virtual para facilitar el acceso a la aplicación y no tener que descargar absolutamente nada en el sistema del usuario, ya que está todo instalado en el mismo entorno virtual que estoy dejando abajo. [Descargar](#ejecución-del-proyecto)
 
### Módulos
 
En el proyecto utilizo los módulos **colorama** y **pymongo** que son módulos que no vienen por defecto en Python, en caso de no querer descargar mi entorno virtual se deberan instalar en su sistema.

### Programación
 
El programa está codificado con el lenguaje de programación **Python** en el entorno de desarrollo **Visual Studio Code** separados por módulos para ahorrar líneas de código, mantener un código ordenado y facilitar cualquier futura mejora en el programa retocando en partes específicas dejando comentarios como documentación.
 
### Base de Datos
 
En este proyecto utilizaré la base de datos **MongoDB** para poder aprender y comprender como se trabaja con la BD tipo JSON.
 
## Funcionalidades
 
- Banner

La función del banner en el programa representa una muestra de los cambios de estados de conexión que va generando el usuario con la base de 
datos, en caso de conectar se detalla la información del mismo y la información va a cambiar dependiendo de la base de datos con la que se conecte.
 
- Banner con Conexión

![](https://github.com/Lucas-devSoft/Python/assets/111676352/beb02be4-30b3-4f42-98c5-c2c9c622ee7f)
*En la imagen como se puede apreciar la extensión de MongoDB en Visual Studio Code me permite ver las bases de datos que tengo creadas en localhost, como mencioné anteriormente, el banner muestra información detallada como (tipo de conexión, nombre de la BD a la que está conectada al igual que su colección y la versión). En este caso en particular La información que trae es la BD por defecto la que fue originada en el código, pero en el caso de que el usuario llegue a generar una con un nombre en específico se conectara a ella y se mostrara en el banner.*

- Banner sin Conexión

![](https://github.com/Lucas-devSoft/Python/assets/111676352/64b8fd15-8289-4e6e-9a36-f778c32fc396)
*Como se puede apreciar en la imagen, en el banner del Menú se lanza el estado de conexión con el que ingreso el usuario, en este caso como es un ‘no’. El banner mostró que la calculadora está sin conexión, por ende no se guardara información.*

- Menus

La función de cada menú en el programa es para interactuar con el usuario y esperar una respuesta del mismo para continuar con cada funcionalidad del programa.

- Solicitud del Nombre

![](https://github.com/Lucas-devSoft/Python/assets/111676352/ab9a8dec-e785-4872-8656-d5885ff460c6)

*Esta funcionalidad esta para brindar una gentil bienvenida al usuario y además su otra utilidad está en el caso de generar una conexión a la base de datos agrega a la Base de datos a quién corresponde cada operación guardada.*<br>
*Ejemplo - { _id : Autodesignado, Nombre: Lucas , Valor_1: 4 , Operador : + , Valor_2 : 4 , Resultado : 8}*<br>
*Es un ejemplo de como se subirá la insercion de los datos sin embargo a la hora de mostrarlo por pantalla se veran solo los valores sin claves.*

- Conexión a la Base de Datos

![](https://github.com/Lucas-devSoft/Python/assets/111676352/bd872f9c-9307-4ab9-bb6f-8009e5d15af7)

*En esta funcionalidad se realiza la conexión a la base de datos, en el caso de escribir ‘sí’ se genera la conexión y en el caso de optar por ‘no’ va directamente al Menú de la Calculadora, destacando en el Banner un mensaje recordatorio que el usuario está en modo sin conexión.*

- Tipo de Conexión

![](https://github.com/Lucas-devSoft/Python/assets/111676352/cc695969-bbb4-4807-8fd9-185a35906151)

*En este menú se solicita el tipo de conexión que se va a generar en MongoDB, es decir de forma local o bien mediante cuenta MongoDB Atlas para realizar el guardado de los datos, en caso de dar una respuesta errónea se lanzará un mensaje de error como en los casos anteriores.*

- Creando la Base de Datos

![](https://github.com/Lucas-devSoft/Python/assets/111676352/09b646d5-7d79-463a-b85b-b029da433799)

*La funcionalidad de este Menú es que el usuario elija si quiere avanzar creando una base de datos con un nombre en específico que él elija o bien avanzar directamente desde una base de datos por defecto que yo nombre directamente en el código para que se creara en cuanto el usuario ponga que ‘no’ y pueda cargar sus datos ahí. En el caso de ‘no’ la Base de datos que se generará se llamara “Calculadora” con una colección llamada “Historial” en el caso de ‘sí’ se llamara como el usuario haya elegido.*

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
[Lucas Ezequiel Sanchez](https://www.linkedin.com/in/lucasdevsoft2022/ "Perfil Linkedin") [Pagina Web](https://lucas-devsoft.github.io/CV/)



