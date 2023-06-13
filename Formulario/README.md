<img width = 950px align = "center" src="https://github.com/Lucas-devSoft/Python/assets/111676352/b02ed5b7-61ed-4352-8294-36598e3eb536"></img>

# Segundo Proyecto Personal
 
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
 
*Desarrollé esta aplicación en el entorno de Windows utilizando el IDE Visual Studio Code para su ejecución en la consola del sistema operativo. Se trata de un proyecto simulado de formularios en el cual la información ingresada en cada campo se almacenará en una base de datos MongoDB, siempre y cuando el usuario lo desee. En caso contrario, algunas funcionalidades estarán limitadas y se mostrarán diferentes menús cuando no se establezca la conexión.
Además, al estar conectado, se ofrecerán más funcionalidades, como la posibilidad de enviar la información a través de Gmail y exportarla en un archivo externo en formato JSON o CSV.*
 
## Herramientas Utilizadas
 
### Entorno Virtual

*En el proyecto, empleo módulos necesarios mediante un entorno virtual para brindar un acceso sencillo a la aplicación sin requerir ninguna descarga en el sistema del usuario. Todos los componentes necesarios están instalados en el entorno virtual, lo que permite ejecutarlo en la consola de su propio sistema.*
 
### Módulos
 
*En el proyecto, utilizo los módulos **colorama**, **pymongo**, **smtplib** y **getpass**. Los modulos como **smtplib** y **getpass** estan preinstalados en python, **colorama** y **pymongo** no están incluidos en la instalación predeterminada de Python. Por lo tanto, es necesario instalarlos a través de  ``pip install``. Sin embargo, ya he instalado estos módulos en el entorno virtual, por lo que no será necesario que los instale en su sistema.*

### Programación
 
*El programa fue codificado en Python, utilizando la práctica de separar el código en módulos correspondientes. Esta estructura me permite realizar cambios de manera más sencilla en partes específicas del programa. Esta práctica no solo mejora la flexibilidad para modificar el software, sino que también contribuye a mantener un código más organizado y descriptivo.*
 
### Base de Datos
 
*La base de datos que utilizo en este proyecto es mongoDB, puede conectarse en modo local o con su cuenta MongoDB atlas.*
 
## Funcionalidades
 
- **Banner**

*El banner en general proporciona detalles sobre la conexión a la base de datos MongoDB, como el estado, el nombre del servidor, el nombre de la base de datos y la documentación con la que se está trabajando, así como la versión de MongoDB. En este caso particular, la información que se muestra corresponde a la base de datos predeterminada generada automáticamente por el código. Sin embargo, si el usuario crea una base de datos con su propio nombre, se establecerá la conexión con esa base de datos y el contenido del banner cambiará en consecuencia.*
 
- **Banner con conexión**

![conectado](https://github.com/Lucas-devSoft/Python/assets/111676352/30719ca3-ce31-4704-9684-4196a91c18d0)

- **Banner sin conexión**

![sin conexión](https://github.com/Lucas-devSoft/Python/assets/111676352/d9d2e3e4-7338-4e76-b2c9-f9fe435209c1)

- **Interacciones**

*Cada interacción en el programa cumple una función específica: permitir al usuario elegir lo que desea hacer y esperar una respuesta precisa que se ajuste a su solicitud, para así continuar con las diferentes funcionalidades del programa.*

- **Genera la conexión con la Base de Datos**

*Con esta funcionalidad, se establece la conexión con la base de datos MongoDB. Puedes generarla de manera local o utilizar una cuenta en MongoDB Atlas. Si seleccionas "no", se omitirá este paso y accederás directamente al menú de los formularios. El banner mostrará al usuario si se encuentra en modo de conexión o sin conexión.*

![Conexion](https://github.com/Lucas-devSoft/Python/assets/111676352/a06ef060-7e62-45f3-a7ca-ece24362038d)

- **Tipo de Conexión**

*En esta funcionalidad, se solicita al usuario que elija el tipo de conexión que desea establecer con MongoDB. Puede optar por una conexión local o utilizar una cuenta en MongoDB Atlas para almacenar los datos.*

![tipo de conexion](https://github.com/Lucas-devSoft/Python/assets/111676352/885354d6-f44d-4242-baeb-8525ef29818d)

- **Crear una Base de Datos con un nombre especifico en modo local**

*En este menú, el usuario tiene dos opciones: la primera es crear una base de datos con un nombre específico ingresado por el usuario, mientras que la segunda opción permite avanzar directamente desde una base de datos predeterminada que he definido en el código.*

![crear bd](https://github.com/Lucas-devSoft/Python/assets/111676352/b47066d9-5fcb-48e3-b407-2183a807e459)

- **Base de Datos Local creación y existencia**

*El usuario tiene la opción de crear una base de datos con el nombre que desee y agregar los datos del formulario dentro de ella. Además, se verificará si la base de datos existe o no.*

![Creado](https://github.com/Lucas-devSoft/Python/assets/111676352/35e4e8dd-28bf-479a-aca4-afb0c6515a3d)

![Existente](https://github.com/Lucas-devSoft/Python/assets/111676352/70d4b8f7-bc88-4bea-98b8-bd7466d6bb47)

- **Conexión Mongo Atlas**

*Se solicitarán los datos de la cuenta del usuario de MongoDB Atlas para establecer la conexión con su cuenta en la nube. Esto permitirá almacenar la información de los formularios de manera segura y confiable.*

![cuenta](https://github.com/Lucas-devSoft/Python/assets/111676352/a0352cf7-b511-4d2b-a2a6-409b219fc442)

- **Crear Base de Datos desde Atlas con un nombre específico**

*En esta funcionalidad un vez ya dento de la cuenta Mongo Atlas podremos crear una base de datos con nombre específico o generar una base de datos por defecto que se encuentra en el código. Esto permitirá almacenar todos los resultados de los formularios.*

![creacion DB](https://github.com/Lucas-devSoft/Python/assets/111676352/15b68485-117a-4c21-b76c-35452d9edd4a)

- **Base de datos atlas creación y existencia**

![Creada](https://github.com/Lucas-devSoft/Python/assets/111676352/bcaa5e61-52df-41ad-80fd-458796da00e4)

![Existente](https://github.com/Lucas-devSoft/Python/assets/111676352/cbb176f7-6a4e-4973-89f3-b60b31b13fe5)

- **Avisos de Formulario.**

*En esta ocasión, se notifica que el usuario ha completado el formulario y no se le permitirá volver a completarlo hasta que realice el reinicio.*

![completado](https://github.com/Lucas-devSoft/Python/assets/111676352/2749db4b-b590-461d-b2a8-c11d8374427a)

![previamente completado](https://github.com/Lucas-devSoft/Python/assets/111676352/676db97c-d53f-4374-9705-2c310535f04f)

- **Los 3 Formularios completos**

*Una vez que los tres formularios estén completos y si el usuario está conectado a la base de datos, se habilitará un menú especial para gestionar la información. En caso contrario, el menú será limitado, pero aún se podrá restablecer los formularios en cualquier momento.*

![completado full](https://github.com/Lucas-devSoft/Python/assets/111676352/d5a108dc-5eb4-40af-9afa-058cdb1ccf33)

- **Guardado de Datos**

*Una vez que la información se haya guardado, se activará el menú para visualizar lo que se ha almacenado en la base de datos.*

![guardado](https://github.com/Lucas-devSoft/Python/assets/111676352/6d31b907-a1ae-4473-8705-c53efdd97eb8)

![visualizacion](https://github.com/Lucas-devSoft/Python/assets/111676352/65c1f4bb-f4c8-4421-b53f-49c7894f6335)

- **Visualización del formulario A**

![A](https://github.com/Lucas-devSoft/Python/assets/111676352/3ad4ea2d-c829-457e-94f5-7467b243ca7e)

- **Visualización del formulario B**

![B](https://github.com/Lucas-devSoft/Python/assets/111676352/d7cccd5d-ace7-42dd-990d-737783228c9e)

- **Visualización del formulario C**

![C](https://github.com/Lucas-devSoft/Python/assets/111676352/0a7644d6-ff0e-40bc-8159-fdaa9c1c4546)

- **Exportación de furmularios a JSON**

![exportacion](https://github.com/Lucas-devSoft/Python/assets/111676352/d628eb4f-631c-49ee-95cf-a0d36992acbf)



- **Envio de los formulario por Gmail**

...

<hr>

- **Tipos de Errores**

*La función del error es alertar al usuario en todo momento cuando haya ingresado una respuesta incorrecta. Por lo tanto, para poder avanzar en el flujo del programa, será necesario que vuelva a intentarlo hasta que ingrese los datos correctos; de lo contrario, los mensajes de error persistirán.*

- **Error (Conexión a la Base de Datos)**

![Error conexion](https://github.com/Lucas-devSoft/Python/assets/111676352/832d52c3-cd22-4b9d-a0c6-a9693b0800bb)

- **Error (Menú)**

![Error Menu](https://github.com/Lucas-devSoft/Python/assets/111676352/75a6ed01-cb90-4c93-94e0-cec49904a5cb)

- **Error (Tipo de Conexión)**

![Error conexión](https://github.com/Lucas-devSoft/Python/assets/111676352/56d2b21c-ef30-4598-bc60-be34c1f7f079)

- **Error (Crear BD)**

![Error BD](https://github.com/Lucas-devSoft/Python/assets/111676352/f35e575a-1e17-4e97-b537-e12cce4034b7)

- **Error (Formato Nombre BD)

![Formato](https://github.com/Lucas-devSoft/Python/assets/111676352/24a5c5d8-b48a-4894-9297-21d2e63b26c4)

- **Error (Campo Invalido)**

![Formato invalido](https://github.com/Lucas-devSoft/Python/assets/111676352/461b9d65-7dcc-4366-b037-a42336ce30f5)

- **Mensaje de Cierre**

![Cierre](https://github.com/Lucas-devSoft/Python/assets/111676352/ca20b941-20ba-4695-9146-abda0a58918f)

<hr>

## Ejecución del Proyecto

*Contamos con 2 alternativas para correr el programa.*

- **Alternativa uno.**

1.  *Se necesita tener instalado Python en el sistema (Ultima Versión 3.11.3)* >  [Descargalo de Aquí](https://www.python.org/downloads/ "Página oficial de Python") 
 
2. *Si tenes Windows como SO y queres probar el programa podes descargarte ``Archivo Exe`` y dentro de la carpeta ``dist`` esta el ejecutable ``menu.exe``, das doble click sobre él y ya se ejecuta.*

- **Alternativa dos** 
  
1. *Se necesita tener instalado Python en el sistema (Ultima Versión 3.11.3)* >   [Descargalo de Aquí](https://www.python.org/downloads/ "Página oficial de Python") 
  
2. *Descargas el entorno virtual que contiene los moódulos necesarios para correrlo* >   [Descargalo Aquí](https://drive.google.com/drive/folders/127vdt47wluqg3wlVX53-jDB7UUEpwVK4?usp=drive_link "Google Drive")

3. *Luego en la raiz junto a .env colocas todos los Scripts descargados y activamos el entorno virtual*. [+Info](https://docs.python.org/es/3/tutorial/venv.html "Documentación venv")

![Muestra](https://github.com/Lucas-devSoft/Python/assets/111676352/13d12580-7c50-4cdc-925f-283b21fb817c)

*Para activar el entorno hacemos lo siguiente:*

*En el CMD de Windows se activa de esta forma:*

 ``.env\Scripts\activate.bat``

*En Unix o MacOS, ejecuta:*

 ``source .env/Scripts/activate``

*Cuando ingresamos correctamente al entorno virtual delante del Path nos aparecera el nombre del entorno de esta forma (.env).* 

![Entorno Virtual](https://github.com/Lucas-devSoft/Python/assets/111676352/f93faa08-999c-4afb-ade5-afedb03a9eea)

4. *En la consola estando en la carpeta raíz "Calculadora" ya podremos ejecutar el programa.*

 ``python menu.py``

5. *Para desactivar el entorno virtual.*

 ``deactivate``
   
## Desarrollador

![Open](https://github.com/Lucas-devSoft/Python/assets/111676352/6d78f829-b40e-4b95-9d98-c6ba05e26f03) <br>
[Perfil Linkedin](https://www.linkedin.com/in/lucasdevsoft2022/ "Perfil Linkedin")   |   [Pagina Web](https://lucas-devsoft.github.io/CV/ "Curriculum Web")
