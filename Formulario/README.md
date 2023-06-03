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
 
*Este proyecto se ha desarrollado en un entorno Windows para ejecutarse en la consola del sistema operativo. Es un proyecto simulado de formularios en el cual la información ingresada en cada campo se almacenará en una base de datos MongoDB si el usuario así lo desea. En caso contrario, las funcionalidades serán diferentes, lo que implica que apareceran distintos menúes cuando no se establezca conexión con una base de datos. Además, se incluirá otra funcionalidad que permitirá enviar la información a través del correo electrónico si el usuario lo desea.*
 
## Herramientas Utilizadas
 
### Entorno Virtual

*En el proyecto, empleo módulos necesarios mediante un entorno virtual para brindar un acceso sencillo a la aplicación sin requerir ninguna descarga en el sistema del usuario. Todos los componentes necesarios están instalados en el entorno virtual, lo que permite ejecutarlo en la consola de su propio sistema.*
 
### Módulos
 
*En el proyecto, utilizo los módulos **colorama**, **pymongo**, **smtplib** y **getpass**. Los modulos como **smtplib** y **getpass** estan preinstalados en python, **colorama** y **pymongo** no están incluidos en la instalación predeterminada de Python. Por lo tanto, es necesario instalarlos a través de  ``pip install``. Sin embargo, ya he instalado estos módulos en el entorno virtual, por lo que no será necesario que los instale en su sistema.*

### Programación
 
*El programa fue implementado en Python y se desarrolló utilizando el entorno de programación Visual Studio Code. Los códigos se organizaron en módulos separados, lo que permite realizar cambios de manera más sencilla en partes específicas del programa. Esta práctica no solo mejora la flexibilidad para modificar el software, sino que también ayuda a mantener un código más organizado y descriptivo.*
 
### Base de Datos
 
*La base de datos que utilizo en este proyecto es mongoDB, puede conectarse en modo local o con cuenta personal atlas.*
 
## Funcionalidades
 
- **Banner**

*La función del banner en el programa es mostrar los cambios de estado en la conexión de la base de datos que el usuario va generando. En cada caso de conexión, se detallará la información correspondiente, la cual cambiará dependiendo de si se establece o no la conexión.*
 
- **Banner con Conexión**

*La imagen proporciona detalles exhaustivos, como el tipo de conexión, el nombre de la base de datos a la que está conectada, así como su colección y la versión de MongoDB. En este caso específico, la información que se muestra es la base de datos predeterminada, generada automáticamente a través del código. Sin embargo, si el usuario crea una base de datos con un nombre específico, se establecerá la conexión con esa base de datos y el banner cambiará en consecuencia.*

![Con conexión](https://github.com/Lucas-devSoft/Python/assets/111676352/949a588a-ed77-415e-baf6-d573806bb49d)

- **Banner sin Conexión**

*La imagen ilustra el cambio de estado a "sin conexión" debido a la decisión del usuario de no conectarse a la base de datos. El banner indica claramente que el sistema está en modo sin conexión, lo que implica que no se guardarán datos.*

![Sin conexión](https://github.com/Lucas-devSoft/Python/assets/111676352/a6a3b825-85ce-4e1c-9b91-c0c2ac7b0745)

- **Interacciones**

*Cada interacción en el programa cumple una función específica: permitir al usuario elegir lo que desea hacer y esperar una respuesta precisa que se ajuste a su solicitud, para así continuar con las diferentes funcionalidades del programa.*

- **Conexión a la Base de Datos**

*En esta función se establece la conexión con la base de datos. Si se ingresa "sí", se genera la conexión; de lo contrario, si se ingresa "no", el sistema redirige directamente al Menú con los formularios. Además, se muestra un mensaje destacado en el Banner para recordar al usuario que se encuentra en modo sin conexión.*

![Base de datos](https://github.com/Lucas-devSoft/Python/assets/111676352/f441dd89-3e06-498d-b38b-efc2868a6de7)

- **Tipo de Conexión**

*En esta funcionalidad, se solicita al usuario que elija el tipo de conexión que desea establecer con MongoDB. Puede optar por una conexión local o utilizar una cuenta en MongoDB Atlas para almacenar los datos.*

![Tipo conexión](https://github.com/Lucas-devSoft/Python/assets/111676352/a02da7c9-da08-4847-85c9-894fa86df469)

- **Crear una Base de Datos Local con un nombre específico**

*Esta funcionalidad del menú permite al usuario elegir entre dos opciones: la primera consiste en avanzar creando una base de datos con un nombre específico elegido por él mismo, mientras que la segunda opción es avanzar directamente desde una base de datos predeterminada que he nombrado directamente en el código. Esta base de datos predeterminada se creará automáticamente cuando el usuario responda "no" y podrá cargar sus datos allí. En caso de que el usuario elija "no", la base de datos generada se llamará "Formularios" y contendrá una colección llamada "Datos". Por otro lado, si el usuario responde "sí", la base de datos se llamará según la elección del usuario.*

![Creacion](https://github.com/Lucas-devSoft/Python/assets/111676352/3d746043-6fbe-4737-ad65-680fc7dc5ec7)

- **Base de Datos Local creación y existencia**

*En esta funcionalidad, el usuario tiene la capacidad de crear una base de datos (BD) con el nombre de su elección y agregar sus datos dentro de ella. Además, se implementa una detección automática para verificar si la BD ya existe*

![Creada](https://github.com/Lucas-devSoft/Python/assets/111676352/324515f7-d0a0-43b0-9f32-2202223d0e7c)

![Existente](https://github.com/Lucas-devSoft/Python/assets/111676352/8746e6fd-f10c-452e-96fd-e5f12d11955b)

- **Conexión Mongo Atlas**

*En esta funcionalidad, se solicitarán al usuario los datos de su cuenta en Mongo Atlas para establecer la conexión con su base de datos. Esto permitirá almacenar las operaciones realizadas.*

![Cuenta](https://github.com/Lucas-devSoft/Python/assets/111676352/e26aae56-5e1d-4504-a4a8-5a492607cfea)

- **Crear Base de Datos desde Atlas con un nombre específico**

![Crear](https://github.com/Lucas-devSoft/Python/assets/111676352/d26bdf4d-0df6-44f7-b222-c322c751a9f3)

- **Base de datos atlas creación y existencia**

![Creada](https://github.com/Lucas-devSoft/Python/assets/111676352/4b350cee-5033-4d1b-b165-53608629ccab)

![Existente](https://github.com/Lucas-devSoft/Python/assets/111676352/ecb463f6-10a6-4999-b246-875d1dde8142)

- **Visualización del formulario**

...

<hr>

- **Tipos de Errores**

...

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

...
   
## Desarrollador

![Open](https://github.com/Lucas-devSoft/Python/assets/111676352/6d78f829-b40e-4b95-9d98-c6ba05e26f03) <br>
[Perfil Linkedin](https://www.linkedin.com/in/lucasdevsoft2022/ "Perfil Linkedin")   |   [Pagina Web](https://lucas-devsoft.github.io/CV/ "Curriculum Web")
