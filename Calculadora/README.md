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
 
El proyecto se desarrolla en un entorno Windows y está diseñado para ejecutarse en la terminal del sistema operativo. Se trata de una calculadora que ofrece funcionalidades adicionales en comparación con una calculadora clásica. El usuario interactúa con la calculadora y tiene la opción de elegir si desea guardar la información de sus operaciones mediante una base de datos MongoDB implementada en el proyecto..
 
## Herramientas Utilizadas
 
### Entorno Virtual

En el proyecto, empleo módulos necesarios mediante un entorno virtual para brindar un acceso sencillo a la aplicación sin requerir ninguna descarga en el sistema del usuario. Todos los componentes necesarios están instalados en el entorno virtual, lo que permite ejecutarlo en la consola de su propio sistema. Si desea probarlo, a continuación encontrará el enlace. [Descargar](#ejecución-del-proyecto)
 
### Módulos
 
En el proyecto, utilizo los módulos **colorama** y **pymongo**, los cuales no están incluidos en la instalación predeterminada de Python. Por lo tanto, es necesario instalarlos a través de ``pip install``. Sin embargo, quiero asegurarle que ya he instalado estos módulos en el entorno virtual, por lo que no será necesario que los instale en su sistema.

### Programación
 
El programa fue implementado en Python y se desarrolló utilizando el entorno de programación Visual Studio Code. Los códigos se organizaron en módulos separados, lo que permite realizar cambios de manera más sencilla en partes específicas del programa. Esta práctica no solo mejora la flexibilidad para modificar el software, sino que también ayuda a mantener un código más organizado y descriptivo.
 
### Base de Datos
 
El proyecto utiliza la base de datos MongoDB y ha sido implementado para generar un historial de operaciones.
 
## Funcionalidades
 
- Banner

La función del banner en el programa es mostrar los cambios de estado en la conexión de la base de datos que el usuario va generando. En cada caso de conexión, se detallará la información correspondiente, la cual cambiará dependiendo de si se establece o no la conexión..
 
- Banner con Conexión

La imagen proporciona detalles exhaustivos, como el tipo de conexión, el nombre de la base de datos a la que está conectada, así como su colección y la versión de MongoDB. En este caso específico, la información que se muestra es la base de datos predeterminada, generada automáticamente a través del código. Sin embargo, si el usuario crea una base de datos con un nombre específico, se establecerá la conexión con esa base de datos y el banner cambiará en consecuencia.

![Conectado](https://github.com/Lucas-devSoft/Python/assets/111676352/72f1e900-a8d9-43ec-9352-11f1acdc24ef)

- Banner sin Conexión

La imagen ilustra el cambio de estado a "sin conexión" debido a la decisión del usuario de no conectarse a la base de datos. El banner indica claramente que el sistema está en modo sin conexión, lo que implica que no se guardarán datos.

![Sin conexión](https://github.com/Lucas-devSoft/Python/assets/111676352/ee04c8ab-05f7-4db7-b0eb-68f4b798a39e)


- Interacciones

Cada interacción en el programa cumple una función específica: permitir al usuario elegir lo que desea hacer y esperar una respuesta precisa que se ajuste a su solicitud, para así continuar con las diferentes funcionalidades del programa.

- Solicitud del Nombre

Esta función tiene como propósito dar una cálida bienvenida al usuario, además de su otra utilidad que consiste en establecer una conexión con la base de datos y asignar la correspondencia correspondiente a cada operación almacenada.

![Nombre](https://github.com/Lucas-devSoft/Python/assets/111676352/7b769a85-a8c4-46ed-86a9-a6647dc86ed5)

- Conexión a la Base de Datos

En esta función se establece la conexión con la base de datos. Si se ingresa "sí", se genera la conexión; de lo contrario, si se ingresa "no", el sistema redirige directamente al Menú de la Calculadora. Además, se muestra un mensaje destacado en el Banner para recordar al usuario que se encuentra en modo sin conexión.

![Conexión](https://github.com/Lucas-devSoft/Python/assets/111676352/29079f3e-5d5d-495e-9025-921610fff74b)

- Tipo de Conexión

En esta funcionalidad, se solicita al usuario que elija el tipo de conexión que desea establecer con MongoDB. Puede optar por una conexión local o utilizar una cuenta en MongoDB Atlas para almacenar los datos.

![Tipo de Conexión](https://github.com/Lucas-devSoft/Python/assets/111676352/e554011f-4663-42a7-a680-44afe3a8af72)

- Crear una Base de Datos Local con un nombre específico

Esta funcionalidad del menú permite al usuario elegir entre dos opciones: la primera consiste en avanzar creando una base de datos con un nombre específico elegido por él mismo, mientras que la segunda opción es avanzar directamente desde una base de datos predeterminada que he nombrado directamente en el código. Esta base de datos predeterminada se creará automáticamente cuando el usuario responda "no" y podrá cargar sus datos allí. En caso de que el usuario elija "no", la base de datos generada se llamará "Calculadora" y contendrá una colección llamada "Historial". Por otro lado, si el usuario responde "sí", la base de datos se llamará según la elección del usuario.

![Crear BD](https://github.com/Lucas-devSoft/Python/assets/111676352/35867c13-694c-45b4-a4a9-9a36dd6897ed)

- Base de Datos Local creación y existencia

En esta funcionalidad, el usuario tiene la capacidad de crear una base de datos (BD) con el nombre de su elección y agregar sus datos dentro de ella. Además, se implementa una detección automática para verificar si la BD ya existe. En caso de que la BD que se intenta crear ya esté presente, se mostrará el mensaje "La base de datos ya existe y está activada para guardar".

![BD Creada](https://github.com/Lucas-devSoft/Python/assets/111676352/81cc020c-5446-48fc-8d03-33a896a22163)
![BD Existente](https://github.com/Lucas-devSoft/Python/assets/111676352/dc340cf5-4212-4885-8c97-989ceda049e7)

- Conexión Mongo Atlas

En esta funcionalidad, se solicitarán al usuario los datos de su cuenta en Mongo Atlas para establecer la conexión con su base de datos. Esto permitirá almacenar las operaciones realizadas.

![Conexión Atlas](https://github.com/Lucas-devSoft/Python/assets/111676352/f65bad0b-bebc-4ae3-a3e7-4c2cc1374a64)

- Crear Base de Datos desde Atlas con un nombre específico

Esta funcionalidad se encarga de crear una nueva base de datos con el nombre elegido por el usuario, donde se podrán almacenar todas las operaciones realizadas en la calculadora.

![Crear BD Atlas](https://github.com/Lucas-devSoft/Python/assets/111676352/ee02cafd-86f2-4326-a6b6-cb9dbf439f4e)

- Base de datos Atlas Creación y Existencia

En las siguientes imágenes se presentan distintos mensajes destacados que surgen cuando se crea una base de datos inexistente o cuando se detecta que la base de datos ya existe, permitiendo así continuar con el programa.

![Creada](https://github.com/Lucas-devSoft/Python/assets/111676352/6679aed2-c171-421a-8ff1-f6ce3cb157d6)
![Existente](https://github.com/Lucas-devSoft/Python/assets/111676352/82aea4ba-565c-4712-8116-c817d7520318)

- Muestra el Historial de operaciones

Esta funcionalidad se activa cuando el usuario está conectado. De esta manera, el usuario puede visualizar todas sus operaciones durante el transcurso del programa, siempre y cuando esté conectado. En caso de que no lo esté, aparecerá un recordatorio indicando que el usuario se encuentra sin conexión.

![Historial](https://github.com/Lucas-devSoft/Python/assets/111676352/06e84d08-77b5-4e89-926e-0881dd811e2c)
![Recordatorio](https://github.com/Lucas-devSoft/Python/assets/111676352/e9b60347-20b3-469b-8d6d-6b9218a3b6e2)

<hr>

- Mensajes de Errores

La función del error es alertar al usuario en todo momento cuando haya ingresado una respuesta incorrecta. Por lo tanto, para poder avanzar en el flujo del programa, será necesario que vuelva a intentarlo hasta que ingrese los datos correctos; de lo contrario, los mensajes de error persistirán.

- Error (Solicitud del Nombre)

![Error Nombre](https://github.com/Lucas-devSoft/Python/assets/111676352/69e138cc-ef56-4c8b-b868-61a801ffdd4f)

- Error (Conexión a la Base de Datos)

![Error Conexión](https://github.com/Lucas-devSoft/Python/assets/111676352/1e821122-4cad-44a9-8d7e-13491d3f4716)

- Error (Menú)

![Error Menú](https://github.com/Lucas-devSoft/Python/assets/111676352/5cc721aa-4247-4947-9bf6-df999f75b692)

- Error (Datos Invalidos)

![Datos invalidos](https://github.com/Lucas-devSoft/Python/assets/111676352/7889de17-4464-450b-81fc-fc7132c2713d)

- Error (Tipo de Conexión)

![Error tipo de Conexión](https://github.com/Lucas-devSoft/Python/assets/111676352/a256226f-1279-46c5-83b1-7b6980c11cb6)

<hr>

## Ejecución del Proyecto

Contamos con 2 alternativas para usar el programa.

- Alternativa uno.

1.  Se necesita tener instalado Python en el sistema (Ultima Versión 3.11.3) >  [Descargalo de Aquí](https://www.python.org/downloads/ "Página oficial de Python") 
 
2. Si tenes Windows como SO y queres probar el programa podes descargarte "Exe-Calculadora" y dentro de ``dist`` esta el ejecutable ``menu.exe``, das doble click sobre él y ya se ejecuta.

- Alternativa dos: 
  
1. Se necesita tener instalado Python en el sistema (Ultima Versión 3.11.3) >   [Descargalo de Aquí](https://www.python.org/downloads/ "Página oficial de Python") 
  
2. Descargas el entorno virtual que contiene los moódulos necesarios para correrlo >   [Descargalo Aquí](https://drive.google.com/drive/u/1/folders/1b8E-k7cfCAzpT5wKOZRedXX86UHuEL9j "Google Drive")

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
[Lucas E. Sanchez](https://www.linkedin.com/in/lucasdevsoft2022/ "Perfil Linkedin")   |   [Pagina Web](https://lucas-devsoft.github.io/CV/ "Curriculum Web")



