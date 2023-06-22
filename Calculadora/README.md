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
- [Ejecutable](#Ejecutable)
- [Desarrollador](#desarrollador)
 
## Descripción del Proyecto
 
*El proyecto se desarrolló en el entorno de Windows utilizando el IDE Visual Studio Code, y está diseñado para ser ejecutado en la terminal del sistema operativo. Se trata de una calculadora que ofrece diversas funcionalidades adicionales en comparación con una calculadora clásica. El usuario puede interactuar con la calculadora y tiene la opción de guardar la información de sus operaciones utilizando una base de datos como MongoDB, que está implementada en el proyecto.*
 
## Herramientas Utilizadas
 
### Entorno Virtual

*En el proyecto, empleo los módulos necesarios mediante un entorno virtual para brindar un acceso sencillo a la aplicación sin requerir ninguna descarga en el sistema del usuario. Todos los componentes necesarios están instalados en el entorno virtual, lo que permite ejecutarlo en la consola de su propio sistema.*
 
### Módulos
 
*En el proyecto, utilizo los módulos **colorama** y **pymongo**, los cuales no están incluidos en la instalación predeterminada de Python. Por lo tanto, es necesario instalarlos a través de ``pip install``. Sin embargo, quiero asegurarle que ya he instalado estos módulos en el entorno virtual, por lo que no será necesario que los instale en su sistema.*

### Programación
 
*El programa fue desarrollado utilizando el lenguaje de programación Python. Los códigos se estructuraron en módulos separados, lo que facilita realizar modificaciones de manera más sencilla en secciones específicas del programa. Esta práctica no solo mejora la flexibilidad para modificar el software, sino que también contribuye a mantener un código más organizado y descriptivo.*
 
### Base de Datos
 
*El proyecto utiliza la base de datos MongoDB y ha sido implementado para generar un historial de operaciones.*
 
## Funcionalidades
 
- **Banner**

*La función del banner en el programa consiste en proporcionar al usuario información detallada acerca de los cambios de estado de la conexión con la base de datos. En cada caso de conexión, se mostrará de manera precisa la información correspondiente.*
 
- **Banner con conexión MongoDB Local**

**Base de datos por defecto**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/ee26f9ce-9263-46f8-aac6-14b64396ec78)

**Base de datos creada por el usuario**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/125426ac-f418-428a-80ec-9900f3d335f0)

- **Banner con conexión MongoDB Atlas**

**Base de datos por defecto**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/ce6fcda0-1275-4d72-9c0d-b2a6350a710c)

**Base de datos creada por el usuario**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/ccb6b0b4-9218-4008-bf40-7efb2d0a5520)

- **Banner sin Conexión**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/44e91780-2f64-427e-9f1c-939f6043717f)

- **Interacciones**

*Dado que el proyecto está destinado a una consola, el usuario siempre interactuará con el programa, y cada respuesta esperada le permitirá avanzar en el flujo del proyecto. El usuario podrá elegir lo que desea hacer y continuar con las diversas funcionalidades del programa.*

- **Solicitud del Nombre**

*La utilidad del nombre está en dar una bienvenida al usuario y además utilizar el mismo como registro para el historial de operaciones*

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/3af36988-2147-44e5-a6d7-88743c9db6ad)

- **Conexión a la Base de Datos**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/5314a5b6-5618-4d48-b8c7-24a3cbbc8532)

- **Tipo de Conexión**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/3a3b9842-55db-4c58-921c-24dab1fab029)

- **Local - Crea una Base de Datos con el nombre que eliga el usuario**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/2858b0a8-997c-47b2-9a66-e3e17712cd33)

- **Local - Base de Datos creada y existente**

**Base de datos creada**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/f3c54eb8-266a-4caa-9598-16ba23a3d0c4)

**Base de datos existente**

![BD Existente](https://github.com/Lucas-devSoft/Python/assets/111676352/dab2d484-d649-4d4a-ae91-826cf9ccf368)

- **Conexión al servidor en la nube de cuenta Atlas del usuario**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/feb5bc2a-1d8a-4ed3-a260-a1b27a38eeeb)

- **Nube - Crea una Base de Datos desde Atlas con un nombre elegido por el usuario**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/d8b7a81b-960f-4d90-ad84-1eb33d04ee0a)

- **Nube - Base de datos creada y existente**

**Base de datos creada**

![creada](https://github.com/Lucas-devSoft/Python/assets/111676352/942d6885-88a5-4527-985a-69e8f313a1cc)

**Base de datos existente**

![existente](https://github.com/Lucas-devSoft/Python/assets/111676352/24777647-2b45-465e-82a1-4e1a51a235ed)

- **Muestra el Historial de operaciones**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/1d374f6c-9d55-4e08-902a-d87d1ecf1915)

*En caso contrario, si el usuario está desconectado, recibirá un recordatorio indicando que no está conectado.*

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/376679f7-3064-4ea2-a3d5-eea1b2ba83f4)

- **Borrado de historial**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/6e869dc0-cb9c-4586-9b69-3e062b1d2317)

<hr>

- **Tipos de Errores**

*La función del error es alertar al usuario en todo momento cuando haya ingresado una respuesta incorrecta. Por lo tanto, para poder avanzar en el flujo del programa, será necesario que vuelva a intentarlo hasta que ingrese los datos correctos; de lo contrario, los mensajes de error persistirán.*

- **Error (Solicitud del Nombre)**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/fb139e8b-daf7-45bb-bd38-c29e8c2ad21b)

- **Error (Conexión a la Base de Datos)**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/13f4baa4-ee52-4155-94be-66a805dd9cd3)

- **Error (Menú)**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/1a80eedf-eeb2-40b5-951a-f58bc51c1c25)

- **Error (Tipo de Conexión)**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/60daba34-9bbb-483f-a967-d226a1746ff3)

- **Error (Datos Invalidos)**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/9c94c9b1-a3c9-4b36-ab07-20c369d20bfb)

<hr>

## Ejecutable 

*Si tenes Windows como sistema operativo aqui en Github dejo el ejecutable para descargar el programa y ejecutarlo. Una ves descargada la carpeta Ejecutable entras a la subcarpeta dist y ahi esta el main.exe*

<hr>
   
## Desarrollador

![Open](https://github.com/Lucas-devSoft/Python/assets/111676352/6d78f829-b40e-4b95-9d98-c6ba05e26f03) <br>
[Perfil Linkedin](https://www.linkedin.com/in/lucasdevsoft2022/ "Perfil Linkedin")   |   [Pagina Web](https://lucas-devsoft.github.io/CV/ "Curriculum Web")
