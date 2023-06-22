<img width = 950px align = "center" src="https://github.com/Lucas-devSoft/Python/assets/111676352/b02ed5b7-61ed-4352-8294-36598e3eb536"></img>

# Segundo Proyecto Personal
 
## Sección de Índices 

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Herramientas utilizadas](#herramientas-utilizadas)
- [Funcionalidades](#funcionalidades)
  - [Banner](#banner)       
    - Con Conexión
    - Sin conexion         
  - [Interacciones](#interacciones)
  - [Errores](#errores)
- [Ejecutable](#ejecutable)
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
 
## Banner

*El banner en general proporciona detalles sobre la conexión a la base de datos MongoDB, como el estado, el nombre del servidor, el nombre de la base de datos y la documentación con la que se está trabajando, así como la versión de MongoDB. En este caso particular, la información que se muestra corresponde a la base de datos predeterminada generada automáticamente por el código. Sin embargo, si el usuario crea una base de datos con su propio nombre, se establecerá la conexión con esa base de datos y el contenido del banner cambiará en consecuencia.*
 
- **Local - Con conexión, base de datos por defecto**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/27101c31-aa44-48d8-a662-6f034d215939)

- **Local - Con conexión, con nombre de base de datos elegido por el usuario** 

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/9a2f4153-5087-4bf2-b98d-1b2749701bed)

- **Nube - Con conexión, base de datos por defecto**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/b373e536-c898-48f7-9d90-b6257ddeb5f5)

- **Nube - Con conexión, con nombre de base de datos elegido por el usuario**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/9b23af85-3682-4d4b-9442-de3ee357057e)

- **Sin conexión**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/83282db0-d140-4923-af17-96f57cb396ba)

## Interacciones

*Cada interacción en el programa cumple una función específica: permitir al usuario elegir lo que desea hacer y esperar una respuesta precisa que se ajuste a su solicitud, para así continuar con las diferentes funcionalidades del programa.*

- **Generando la conexión con la Base de Datos**

![Conexion](https://github.com/Lucas-devSoft/Python/assets/111676352/a06ef060-7e62-45f3-a7ca-ece24362038d)

- **Tipo de Conexión**

![tipo de conexion](https://github.com/Lucas-devSoft/Python/assets/111676352/885354d6-f44d-4242-baeb-8525ef29818d)

- **Local - Creando base de datos con un renombre por el usuario**

![Sin título2](https://github.com/Lucas-devSoft/Python/assets/111676352/fbc75659-7979-4ee3-b1c1-900b74ef4fa7)

- **Local - Creación y existencia de base de datos**

**Creacion exitosa**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/75606483-d1dc-4334-8334-24914e50ea68)

**Ya existente**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/9083b038-5325-4020-9490-e0283cd4ab84)

- **Conexión al servidor de MongoDB Atlas**

*Se solicitarán los datos del servidor de la cuenta del usuario de MongoDB Atlas para establecer la conexión con su cuenta en la nube. Esto permitirá almacenar la información de los formularios de manera segura y confiable.*

![cuenta](https://github.com/Lucas-devSoft/Python/assets/111676352/a0352cf7-b511-4d2b-a2a6-409b219fc442)

- **Nube - Creando base de datos con un renombre por el usuario**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/77510c0a-89de-4a25-87c5-d3e977909adb)

- **Nube - Creación y existencia de base de datos**

**Creación exitosa**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/4c8dabb1-1224-406c-b309-994a93437a96)

**Ya existe**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/ee5ba130-73df-45b0-b4de-be445f10c071)

- **Avisos de Formularios**

*En esta ocasión, se notifica que el usuario ha completado el formulario y no se le permitirá volver a completarlo hasta que realice el reinicio.*

**Completado satisfactoriamente**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/ecd7d1ee-d3a7-4273-95eb-53a0fa05825c)

**Formulario ya completado**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/00b6d9bd-9ff8-486a-8177-57a06e5980e7)

- **Los 3 Formularios completos**

*Una vez que los tres formularios estén completos y si el usuario está conectado a la base de datos, se habilitará una opción del menú para guardar la información. En caso contrario, el menú guardar no aparecera dentro de la misma.*

**Con conexión**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/eb2c0ca5-38de-450b-a6ba-e5c90e421fd3)

**Sin conexión**

*La opcíón guardar no esta habilitada*

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/1da298d7-7368-47ce-a761-eb8f91b752f1)

- **Guardando los Datos**

*Una vez que la información se haya guardado, se activará el menú para visualizar lo que se ha almacenado en la base de datos.*

**Datos guardados**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/51c0e1ce-2fac-48d9-8f68-5d90f462df60)

**Menu de visualización habilitado**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/3febeedc-8631-4388-a7ab-69ed252f8fbd)

- **Visualización del formulario A**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/38bb86c3-4757-43e9-8aec-b62eeeb8c956)

- **Visualización del formulario B**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/bc52199a-299e-4aeb-9300-b896bdda268f)

- **Visualización del formulario C**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/b14f9a3f-0532-40da-aedf-212be95e0ad4)

- **Exportación de furmularios a JSON** 

*La exportación de la información de los formularios verificará la existencia del archivo de exportación. En caso de que el archivo no exista, se creará automáticamente. Por otro lado, si el archivo ya existe, se mostrará una advertencia de su existencia.*

*Exportacion exitosa*

![exportacion](https://github.com/Lucas-devSoft/Python/assets/111676352/d628eb4f-631c-49ee-95cf-a0d36992acbf)

*Archivo existente*

![ya existe](https://github.com/Lucas-devSoft/Python/assets/111676352/24c26c81-d790-4813-96e1-82b42feb8fe5)

*visualización del contenido*

![archivo creado](https://github.com/Lucas-devSoft/Python/assets/111676352/af21fd66-7ce3-4318-8756-b512cf0629fa)

- **Cuenta de ingreso a Gmail**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/87df4188-8f09-429b-b465-0b11f1e0cd08)

- **Pasos previo para el envio de Gmail**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/5e2c9ba8-db08-4b3e-b2d8-6c3304a2fc28)

- **Envio del Email**

*Mensaje enviado con exito*

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/ac83b385-864f-4436-9fb5-c5c503b65091)

*Correo recibido con exito*

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/feea2a01-d72c-42c2-b133-44beda0825a1)

<hr>

## Errores

*La función del error es alertar al usuario en todo momento cuando haya ingresado una respuesta incorrecta. Por lo tanto, para poder avanzar en el flujo del programa, será necesario que vuelva a intentarlo hasta que ingrese los datos correctos; de lo contrario, los mensajes de error persistirán.*

- **Error (Conexión a la Base de Datos)**

![error conexion](https://github.com/Lucas-devSoft/Python/assets/111676352/5f89a5df-5c39-41b0-a041-c42186e95691)

- **Error (Menú)**

![error menu](https://github.com/Lucas-devSoft/Python/assets/111676352/ef446434-dcdc-40a0-af5d-5a4e4990f8cc)

- **Error (Tipo de Conexión)**

![error_tipo](https://github.com/Lucas-devSoft/Python/assets/111676352/4a6544a6-1fd4-42da-836b-e63a590c20d9)

- **Error (Crear BD)**

![error crear](https://github.com/Lucas-devSoft/Python/assets/111676352/44383565-4873-4455-829b-15b002e0a827)

- **Error (Campo Invalido)**

![error campo](https://github.com/Lucas-devSoft/Python/assets/111676352/1d4a1a36-2a46-4b91-835c-64c4630565c3)

- **Error menu de formularios completo**

![error extendido](https://github.com/Lucas-devSoft/Python/assets/111676352/ea56470d-2ee7-4e89-9b29-d5dfd295cd32)

- **Error de menu visualizaciones**

![error visualizaciones](https://github.com/Lucas-devSoft/Python/assets/111676352/27403752-41aa-49ca-85c0-204342e8fc5c)

- **Mensaje de Cierre**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/78b94648-eddd-437e-a819-b0daf6bb0626)

<hr>

## Ejecutable

*Si tenes sistema operativo Windows y tenes curiosidad por probar el programa, te dejo el ejecutable en la carpeta Ejecutable dentro de la subcarpeta vas a encontrar el archivo .exe*

<hr>
   
## Desarrollador

![Open](https://github.com/Lucas-devSoft/Python/assets/111676352/6d78f829-b40e-4b95-9d98-c6ba05e26f03) <br>
[Perfil Linkedin](https://www.linkedin.com/in/lucasdevsoft2022/ "Perfil Linkedin")   |   [Pagina Web](https://lucas-devsoft.github.io/CV/ "Curriculum Web")
