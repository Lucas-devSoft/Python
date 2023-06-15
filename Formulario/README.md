<img width = 950px align = "center" src="https://github.com/Lucas-devSoft/Python/assets/111676352/b02ed5b7-61ed-4352-8294-36598e3eb536"></img>

# Segundo Proyecto Personal
 
## Sección de Índices 

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Herramientas utilizadas](#herramientas-utilizadas)
- [Funcionalidades](#funcionalidades)
  - Banner(#Banner)       
    - Con Conexión
    - Sin conexion         
  - [Interacciones](#Interacciones)
  - [Errores](#Errores)
- [Desarrollador](#desarrollador)
 
## Descripción del Proyecto
 
*He desarrollado esta aplicación en el entorno de Windows utilizando el IDE Visual Studio Code para su ejecución en la consola del sistema operativo. El proyecto simula formularios en los que se puede ingresar información en varios campos. Esta información se almacenará en una base de datos (MongoDB) si el usuario lo desea. La funcionalidad principal de la aplicación depende de la conexión a la base de datos: si no se establece una conexión, la opción de guardar no estará disponible. Además, la aplicación ofrece otras funcionalidades, como la capacidad de enviar la información a través de Gmail y exportarla en formato JSON a un archivo externo.*
 
## Herramientas Utilizadas
 
### Entorno Virtual

*En el proyecto, empleo los módulos necesarios en un entorno virtual para brindar un acceso sencillo a la aplicación sin requerir ninguna descarga en el sistema del usuario. Todos los componentes necesarios están instalados en el entorno virtual, lo que permite ejecutarlo en la consola de su propio sistema.*
 
### Módulos
 
*En el proyecto, utilizo los módulos **colorama**, **pymongo**, **smtplib** y **getpass**. Los modulos como **smtplib** y **getpass** estan preinstalados en python, **colorama** y **pymongo** no están incluidos en la instalación predeterminada de Python.*

### Programación
 
*El proyecto se codificó en Python, siguiendo la práctica de separar el código en módulos correspondientes. Esta estructura me permitió realizar cambios de forma más sencilla en partes específicas del programa. Esta práctica no solo aumenta la flexibilidad para modificar el software, sino que también ayuda a mantener un código más organizado y descriptivo.*
 
### Base de Datos
 
*La base de datos que utilizo en este proyecto es mongoDB, el usuario puede conectarse en modo local o con su cuenta MongoDB atlas.*
 
## Funcionalidades
 
- **Banner**

*El banner en general proporciona detalles sobre la conexión a la base de datos MongoDB, como el estado, el nombre del servidor, el nombre de la base de datos y la documentación con la que se está trabajando, así como la versión de MongoDB. En este caso particular, la información que se muestra corresponde a la base de datos predeterminada generada automáticamente por el código. Sin embargo, si el usuario crea una base de datos con su propio nombre, se establecerá la conexión con esa base de datos y el contenido del banner cambiará en consecuencia.*
 
- **Con conexión**

![conectado](https://github.com/Lucas-devSoft/Python/assets/111676352/30719ca3-ce31-4704-9684-4196a91c18d0)

- **Sin conexión**

![sin conexión](https://github.com/Lucas-devSoft/Python/assets/111676352/d9d2e3e4-7338-4e76-b2c9-f9fe435209c1)

- **Interacciones**

*Cada interacción en el programa cumple una función específica: permitir al usuario elegir lo que desea hacer y esperar una respuesta precisa que se ajuste a su solicitud, para así continuar con las diferentes funcionalidades del programa.*

- **Generando la conexión con la Base de Datos**

*Con esta funcionalidad, se establece la conexión con la base de datos MongoDB. Puedes generarla de manera local o utilizar una cuenta en MongoDB Atlas. Si seleccionas "no", se omitirá este paso y accederás directamente al menú de los formularios. El banner mostrará al usuario si se encuentra en modo de conexión o sin conexión.*

![Conexion](https://github.com/Lucas-devSoft/Python/assets/111676352/a06ef060-7e62-45f3-a7ca-ece24362038d)

- **Tipo de Conexión**

*En esta funcionalidad, se solicita al usuario que elija el tipo de conexión que desea establecer con MongoDB. Puede optar por una conexión local o utilizar una cuenta en MongoDB Atlas para almacenar los datos.*

![tipo de conexion](https://github.com/Lucas-devSoft/Python/assets/111676352/885354d6-f44d-4242-baeb-8525ef29818d)

- **Creando un nombre especifico en modo local**

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

*La exportación de la información de los formularios verificará la existencia del archivo de exportación. En caso de que el archivo no exista, se creará automáticamente. Por otro lado, si el archivo ya existe, se mostrará una advertencia de su existencia.*

![exportacion](https://github.com/Lucas-devSoft/Python/assets/111676352/d628eb4f-631c-49ee-95cf-a0d36992acbf)

![ya existe](https://github.com/Lucas-devSoft/Python/assets/111676352/24c26c81-d790-4813-96e1-82b42feb8fe5)

![archivo creado](https://github.com/Lucas-devSoft/Python/assets/111676352/af21fd66-7ce3-4318-8756-b512cf0629fa)

- **Envio de los formulario por Gmail**

..

- **Cuenta de ingreso a Gmail**

![Cuenta](https://github.com/Lucas-devSoft/Python/assets/111676352/5c07bc99-9ccf-4331-b566-7eb2b95f7198)

- **Cuenta ingresada**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/543ac34b-ec5c-42d9-9778-8a4c33662407)

- **Envio exitoso**

![envio](https://github.com/Lucas-devSoft/Python/assets/111676352/675aae16-df65-41e0-b6dc-f3cb83a96345)

![llego](https://github.com/Lucas-devSoft/Python/assets/111676352/433fe785-c30a-4866-a398-6ce0df23aed6)

<hr>

- **Tipos de Errores**

*La función del error es alertar al usuario en todo momento cuando haya ingresado una respuesta incorrecta. Por lo tanto, para poder avanzar en el flujo del programa, será necesario que vuelva a intentarlo hasta que ingrese los datos correctos; de lo contrario, los mensajes de error persistirán.*

- **Error (Conexión a la Base de Datos)**

![error conexion](https://github.com/Lucas-devSoft/Python/assets/111676352/5f89a5df-5c39-41b0-a041-c42186e95691)

- **Error (Menú)**

![error menu](https://github.com/Lucas-devSoft/Python/assets/111676352/ef446434-dcdc-40a0-af5d-5a4e4990f8cc)

- **Error (Tipo de Conexión)**

![error_tipo](https://github.com/Lucas-devSoft/Python/assets/111676352/4a6544a6-1fd4-42da-836b-e63a590c20d9)

- **Error (Crear BD)**

![error crear](https://github.com/Lucas-devSoft/Python/assets/111676352/44383565-4873-4455-829b-15b002e0a827)

- **Error (Formato Nombre BD)

![error formato](https://github.com/Lucas-devSoft/Python/assets/111676352/4f21d9e3-3bd6-4602-90d4-e2db23248d24)

- **Error (Campo Invalido)**

![error campo](https://github.com/Lucas-devSoft/Python/assets/111676352/1d4a1a36-2a46-4b91-835c-64c4630565c3)

- **Error menu de formularios completo**

![error extendido](https://github.com/Lucas-devSoft/Python/assets/111676352/ea56470d-2ee7-4e89-9b29-d5dfd295cd32)

- **Error de menu visualizaciones**

![error visualizaciones](https://github.com/Lucas-devSoft/Python/assets/111676352/27403752-41aa-49ca-85c0-204342e8fc5c)

- **Mensaje de Cierre**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/78b94648-eddd-437e-a819-b0daf6bb0626)

<hr>
   
## Desarrollador

![Open](https://github.com/Lucas-devSoft/Python/assets/111676352/6d78f829-b40e-4b95-9d98-c6ba05e26f03) <br>
[Perfil Linkedin](https://www.linkedin.com/in/lucasdevsoft2022/ "Perfil Linkedin")   |   [Pagina Web](https://lucas-devsoft.github.io/CV/ "Curriculum Web")
