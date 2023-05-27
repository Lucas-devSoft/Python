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
 
*El proyecto se desarrolla en un entorno Windows y está diseñado para ejecutarse en la terminal del sistema operativo. Se trata de una calculadora que ofrece funcionalidades adicionales en comparación con una calculadora clásica. El usuario interactúa con la calculadora y tiene la opción de elegir si desea guardar la información de sus operaciones mediante una base de datos MongoDB implementada en el proyecto.*
 
## Herramientas Utilizadas
 
### Entorno Virtual

*En el proyecto, empleo módulos necesarios mediante un entorno virtual para brindar un acceso sencillo a la aplicación sin requerir ninguna descarga en el sistema del usuario. Todos los componentes necesarios están instalados en el entorno virtual, lo que permite ejecutarlo en la consola de su propio sistema. Si desea probarlo, a continuación encontrará el enlace.* [Descargar](#ejecución-del-proyecto)
 
### Módulos
 
*En el proyecto, utilizo los módulos **colorama** y **pymongo**, los cuales no están incluidos en la instalación predeterminada de Python. Por lo tanto, es necesario instalarlos a través de ``pip install``. Sin embargo, quiero asegurarle que ya he instalado estos módulos en el entorno virtual, por lo que no será necesario que los instale en su sistema.*

### Programación
 
*El programa fue implementado en Python y se desarrolló utilizando el entorno de programación Visual Studio Code. Los códigos se organizaron en módulos separados, lo que permite realizar cambios de manera más sencilla en partes específicas del programa. Esta práctica no solo mejora la flexibilidad para modificar el software, sino que también ayuda a mantener un código más organizado y descriptivo.*
 
### Base de Datos
 
*El proyecto utiliza la base de datos MongoDB y ha sido implementado para generar un historial de operaciones.*
 
## Funcionalidades
 
- **Banner**

*La función del banner en el programa es mostrar los cambios de estado en la conexión de la base de datos que el usuario va generando. En cada caso de conexión, se detallará la información correspondiente, la cual cambiará dependiendo de si se establece o no la conexión.*
 
- **Banner con Conexión**

*La imagen proporciona detalles exhaustivos, como el tipo de conexión, el nombre de la base de datos a la que está conectada, así como su colección y la versión de MongoDB. En este caso específico, la información que se muestra es la base de datos predeterminada, generada automáticamente a través del código. Sin embargo, si el usuario crea una base de datos con un nombre específico, se establecerá la conexión con esa base de datos y el banner cambiará en consecuencia.*

![Con conexión](https://github.com/Lucas-devSoft/Python/assets/111676352/445f99d0-0476-4c67-973b-4916ce4b5ed7)

- **Banner sin Conexión**

*La imagen ilustra el cambio de estado a "sin conexión" debido a la decisión del usuario de no conectarse a la base de datos. El banner indica claramente que el sistema está en modo sin conexión, lo que implica que no se guardarán datos.*

![Sin conexión](https://github.com/Lucas-devSoft/Python/assets/111676352/0a913a95-74df-451b-955e-1bf570bf3846)

- **Interacciones**

*Cada interacción en el programa cumple una función específica: permitir al usuario elegir lo que desea hacer y esperar una respuesta precisa que se ajuste a su solicitud, para así continuar con las diferentes funcionalidades del programa.*

- **Solicitud del Nombre**

*Esta función tiene como propósito dar una cálida bienvenida al usuario, además de su otra utilidad que consiste en establecer una conexión con la base de datos y asignar la correspondencia correspondiente a cada operación almacenada.*

![Nombre](https://github.com/Lucas-devSoft/Python/assets/111676352/cc10ba01-2f0f-4f47-9974-610f5739e405)

- **Conexión a la Base de Datos**

*En esta función se establece la conexión con la base de datos. Si se ingresa "sí", se genera la conexión; de lo contrario, si se ingresa "no", el sistema redirige directamente al Menú de la Calculadora. Además, se muestra un mensaje destacado en el Banner para recordar al usuario que se encuentra en modo sin conexión.*

![Conexión](https://github.com/Lucas-devSoft/Python/assets/111676352/e6b7fb3f-0a7c-440a-b309-46ecf03e2efb)

- **Tipo de Conexión**

*En esta funcionalidad, se solicita al usuario que elija el tipo de conexión que desea establecer con MongoDB. Puede optar por una conexión local o utilizar una cuenta en MongoDB Atlas para almacenar los datos.*

![Tipo Conexión](https://github.com/Lucas-devSoft/Python/assets/111676352/4093a8e9-cb1b-4792-b4ab-4f6ab6299a26)

- **Crear una Base de Datos Local con un nombre específico**

*Esta funcionalidad del menú permite al usuario elegir entre dos opciones: la primera consiste en avanzar creando una base de datos con un nombre específico elegido por él mismo, mientras que la segunda opción es avanzar directamente desde una base de datos predeterminada que he nombrado directamente en el código. Esta base de datos predeterminada se creará automáticamente cuando el usuario responda "no" y podrá cargar sus datos allí. En caso de que el usuario elija "no", la base de datos generada se llamará "Calculadora" y contendrá una colección llamada "Historial". Por otro lado, si el usuario responde "sí", la base de datos se llamará según la elección del usuario.*

![Crear BD](https://github.com/Lucas-devSoft/Python/assets/111676352/ed5c49c9-08bd-4703-b601-180d5bf4d63b)

- **Base de Datos Local creación y existencia**

*En esta funcionalidad, el usuario tiene la capacidad de crear una base de datos (BD) con el nombre de su elección y agregar sus datos dentro de ella. Además, se implementa una detección automática para verificar si la BD ya existe*

![BD Creadad](https://github.com/Lucas-devSoft/Python/assets/111676352/3d5c9036-c901-4afa-a4bc-f29ba4dbf24e)

*En caso de que la BD que se intenta crear ya esté presente, se mostrará el mensaje "La base de datos ya existe y está activada para guardar".*

![BD Existente](https://github.com/Lucas-devSoft/Python/assets/111676352/dab2d484-d649-4d4a-ae91-826cf9ccf368)

- **Conexión Mongo Atlas**

*En esta funcionalidad, se solicitarán al usuario los datos de su cuenta en Mongo Atlas para establecer la conexión con su base de datos. Esto permitirá almacenar las operaciones realizadas.*

![Conexión Atlas](https://github.com/Lucas-devSoft/Python/assets/111676352/62d992fe-412b-4b2b-9791-085f373a4262)

- **Crear Base de Datos desde Atlas con un nombre específico**

*Esta funcionalidad se encarga de crear una nueva base de datos con el nombre elegido por el usuario en mongoDB Atlas, donde se podrán almacenar todas las operaciones realizadas en la calculadora.*

![BD Nombre Especifico](https://github.com/Lucas-devSoft/Python/assets/111676352/c7b9f9b7-65fd-4abd-8a67-f5a9a07d975c)

- **Base de datos atlas creación y existencia**

*En las siguientes imágenes se presentan distintos mensajes destacados que surgen cuando se crea una base de datos inexistente creandola o existente, permitiendo así continuar con el programa.*

![creada](https://github.com/Lucas-devSoft/Python/assets/111676352/942d6885-88a5-4527-985a-69e8f313a1cc)

![existente](https://github.com/Lucas-devSoft/Python/assets/111676352/24777647-2b45-465e-82a1-4e1a51a235ed)

- **Muestra el Historial de operaciones**

*El historial se genera cuando el usuario se conecta a la base de datos.*

![Historial](https://github.com/Lucas-devSoft/Python/assets/111676352/29a13a51-42a3-41c8-aa6f-aa94c9559c8b)

*En caso contrario, si el usuario está desconectado, recibirá un recordatorio indicando que no está conectado.*

![Recondatorio](https://github.com/Lucas-devSoft/Python/assets/111676352/0120bec2-352f-4e37-b2c9-df72c2fb0d17)

<hr>

- Tipos de Errores

La función del error es alertar al usuario en todo momento cuando haya ingresado una respuesta incorrecta. Por lo tanto, para poder avanzar en el flujo del programa, será necesario que vuelva a intentarlo hasta que ingrese los datos correctos; de lo contrario, los mensajes de error persistirán.

- Error (Solicitud del Nombre)

![Nombre](https://github.com/Lucas-devSoft/Python/assets/111676352/09d6d720-afb8-478f-a639-78acec68826d)

- Error (Conexión a la Base de Datos)

![Conexión](https://github.com/Lucas-devSoft/Python/assets/111676352/ee0b5a77-f53a-4bc9-b7ea-0250d07ef2c1)

- Error (Menú)

![Menú](https://github.com/Lucas-devSoft/Python/assets/111676352/ad3c140f-d2a6-444d-8e96-7206c767329b)

- Error (Tipo de Conexión)

![Tipo Conexión](https://github.com/Lucas-devSoft/Python/assets/111676352/e8fab442-6cf1-4917-bc8e-6363da32e48f)

- Error (Datos Invalidos)

![Datos](https://github.com/Lucas-devSoft/Python/assets/111676352/9585790e-f005-47db-97d3-3d051d258e4b)

<hr>

## Ejecución del Proyecto

Contamos con 2 alternativas para correr el programa.

- Alternativa uno.

1.  Se necesita tener instalado Python en el sistema (Ultima Versión 3.11.3) >  [Descargalo de Aquí](https://www.python.org/downloads/ "Página oficial de Python") 
 
2. Si tenes Windows como SO y queres probar el programa podes descargarte ``Archivo Exe`` y dentro de la carpeta ``dist`` esta el ejecutable ``menu.exe``, das doble click sobre él y ya se ejecuta.

- Alternativa dos: 
  
1. Se necesita tener instalado Python en el sistema (Ultima Versión 3.11.3) >   [Descargalo de Aquí](https://www.python.org/downloads/ "Página oficial de Python") 
  
2. Descargas el entorno virtual que contiene los moódulos necesarios para correrlo >   [Descargalo Aquí](https://drive.google.com/drive/folders/127vdt47wluqg3wlVX53-jDB7UUEpwVK4?usp=drive_link "Google Drive")

3. Luego en la raiz junto a .env colocas todos los Scripts descargados y activamos el entorno virtual. [+Info](https://docs.python.org/es/3/tutorial/venv.html "Documentación venv")

![Muestra](https://github.com/Lucas-devSoft/Python/assets/111676352/13d12580-7c50-4cdc-925f-283b21fb817c)

Para activar el entorno hacemos lo siguiente:

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
[Perfil Linkedin](https://www.linkedin.com/in/lucasdevsoft2022/ "Perfil Linkedin")   |   [Pagina Web](https://lucas-devsoft.github.io/CV/ "Curriculum Web")
