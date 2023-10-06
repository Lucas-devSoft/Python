<img width = "950px" align = "center" src="https://github.com/Lucas-devSoft/Python/assets/111676352/69fa3548-30c5-4304-b9e1-01619683b517"></img> 

# Primer Proyecto Personal
 
## Sección de Índices 

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Herramientas utilizadas](#herramientas-utilizadas)
- [Funcionalidades](#funcionalidades)
  - [Banner](#Banner)        
    - Con Conexión
    - Sin conexion         
  - [Interacciones](#Interacciones)
  - [Mensajes de Errores](#Errores)
- [Ejecutable](#Ejecutable)
- [Desarrollador](#desarrollador)
 
## Descripción del Proyecto
 
*El proyecto trata de una calculadora que ofrece funcionalidades adicionales a una calculadora tradicional de (suma, resta, multiplicación y división). Este programa le ofrece al usuario la opción de guardar los datos que se recibe como resultado en una base de datos en este caso el proyecto lleva una conexión a MongoDB forma local o en la nube. El proyecto se desarrolló en el entorno de Windows utilizando el IDE Visual Studio Code, y está diseñado para ser ejecutado en la terminal del sistema operativo.*
 
## Herramientas Utilizadas
 
### Entorno Virtual

*Instale los módulos necesarios en un entorno virtual llamado 'env' para brindar un acceso rápido y sencillo a la aplicación para evitar la descarga o instalación en el equipo del usuario. Todos los componentes necesarios están instalados en el entorno virtual, lo que hace funcional al programa ejecutandolo desde la consola desde 'env'.*
 
### Módulos
 
*En el proyecto, utilizo los módulos **colorama** y **pymongo**, los cuales no están incluidos en la instalación predeterminada de Python. Por lo tanto, es necesario instalarlos a través de ``pip install``. Sin embargo, quiero asegurarle que ya he instalado estos módulos en el entorno virtual, por lo que no será necesario que los instale en su sistema.*

### Programación
 
*Fue desarrollado utilizando el lenguaje de programación Python. El código de este proyecto esta dividido en módulos lo que facilita realizar modificaciones de manera más sencilla en secciones específicas del programa. Esta práctica no solo mejora la flexibilidad para modificar el software, sino que también contribuye a mantener un código más organizado y descriptivo.*
 
### Base de Datos
 
*se puede utilizar la base de datos MongoDB en firma local o en la nube para generar el historial de operaciones.*
 
## Funcionalidades
 
### Banner

*La función del banner en el programa consiste en proporcionar al usuario información detallada acerca de los cambios de estado de la conexión con la base de datos. En cada caso de conexión, se mostrará de manera precisa la información correspondiente.*
 
- **Banner activo con conexión**

**Local - Conectado a la BD por defecto**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/63d3f25d-598d-4e2b-b182-d7a5557a4722)

**Local - Conectado a la BD creada por el usuario**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/d4094247-7590-4f90-9a76-d4f81d68aa04)

**Atlas - Conectado a la BD por defecto**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/1e982239-ba3b-4b82-a6df-df3b04074b14)

**Atlas - Conectado a la BD creada por el usuario**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/e3f6efca-ab44-464b-bb4c-14b55e4d0f82)

- **Banner inactivo sin Conexión**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/7d8b406e-df00-4ee9-a0b8-56224b6c8663)

### Interacciones

*Dado que el proyecto está destinado a una consola, el usuario siempre interactuará con el programa, y cada respuesta esperada le permitirá avanzar en el flujo del proyecto. El usuario podrá elegir lo que desea hacer y continuar con las diversas funcionalidades del programa.*

- **Solicitud del Nombre**

*La utilidad del nombre está en dar una bienvenida al usuario y además utilizar el mismo como registro para el historial de operaciones*

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/cc5a6bfd-522f-4a90-9a9f-ad5e59b4a2ae)

- **Conexión a la Base de Datos**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/debd97ad-2b64-42e4-8820-dde6475aca96)

- **Tipo de Conexión**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/92c2b597-2826-467c-8df3-baeb3053b999)

- **Local - Consulta si creá un BD con el nombre que eliga el usuario**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/adca6973-35f7-43d1-9ff6-ac4c26a5ea2c)

- **Local - Base de Datos creada y existente**

**Base de datos creada con exito**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/e25e77c6-c1c6-4a84-a447-6ef311256aaf)

**Base de datos ya existente**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/bb126bc8-3561-40ef-b199-e9293c476c5c)

- **Conexión al servidor en la nube de MongoDb Atlas**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/22405e59-5fa7-442b-ac3b-2a646ec39b51)

- **Atlas - Consulta si creá una BD con el nombre elegido por el usuario**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/fffdf1f9-fcce-40fa-8849-afd547ea1425)

- **Atlas - Base de datos creada y existente**

**Base de datos creada exitosamente**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/debfd9da-732c-4c13-be5e-67f44c8d8796)

**Base de datos ya existente**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/7fdc0ba5-3a91-4bc4-8ba1-68575924ea50)

- **Muestra el Historial de operaciones**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/6ddad3d2-1bbe-435f-9b3f-8c8e3bbbb111)

*En caso contrario, si el usuario está desconectado, recibirá un recordatorio indicando que no está conectado.*

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/02db44ef-fd31-47e5-a46d-9c7f29d39805)

- **Borrado de historial**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/f47261f4-0a94-4d1b-95a1-86bbf32b87c2)

<hr>

### Errores

*La función del error es alertar al usuario en todo momento cuando haya ingresado una respuesta incorrecta. Por lo tanto, para poder avanzar en el flujo del programa, será necesario que vuelva a intentarlo hasta que ingrese los datos correctos; de lo contrario, los mensajes de error persistirán.*

- **Error - Solicitud Nombre**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/7ca2f5d8-b96e-4bfc-a87b-cb946f9e3326)

- **Error - Consulta de conexión a la BD**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/1595d068-0608-49bd-b588-9009b64bc04d)

- **Error - Elección de opciones del menú**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/a10aa0ce-95b4-4bfe-9591-fe61c432f128)

- **Error - Consulta sobre el tipo de conexión**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/c26c314a-eb9d-41e3-8af8-b32452211c65)

- **Error - Consulta sobre la generación de BD**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/d207e071-1b10-4b15-a7a0-15a9c90ab12b)

- **Error - Formato del prompts**

![Sin título](https://github.com/Lucas-devSoft/Python/assets/111676352/dcfc0fac-189a-4bbf-8ef0-40f6106c5eeb)

<hr>

## Ejecutable 

*Si tenes Windows como sistema operativo aqui en Github dejo el ejecutable para descargar el programa y ejecutarlo. Una ves descargada la carpeta "Ejecutable .exe" entras a la subcarpeta "dist" y ahi esta el main.exe*

<hr>
   
## Desarrollador

![Open](https://github.com/Lucas-devSoft/Python/assets/111676352/6d78f829-b40e-4b95-9d98-c6ba05e26f03) <br>
[Perfil Linkedin](https://www.linkedin.com/in/lucasdevsoft2022/ "Perfil Linkedin")   |   [Pagina Web](https://lucas-devsoft.github.io/CV/ "Curriculum Web")
