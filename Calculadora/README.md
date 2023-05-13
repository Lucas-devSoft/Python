<img width = "950px" align = "center" src="https://github.com/Lucas-devSoft/Python/assets/111676352/69fa3548-30c5-4304-b9e1-01619683b517"></img> 
 
<h1 align = "center"> Proyecto Personal N°1 </h1>
 
<h2>Sección de Índices.</h2>

<ul>
    <li><a href = "#Descripción" > Descripción del Proyecto</a></li>
    <li><a href = "#Herramientas"> Herramientas utilizadas</a></li>
    <li><a href = "#Funcionalidades"> Funcionalidades</a>
        <ul>
            <li>Banner
                <ul>
                    <li>Conexión</li>
                    <li>Sin conexion</li>
                </ul>
             </li>
             <li>Menus</li>
             <li>Mensajes de Errores</li>
        </ul>
    </li>     
    <li><a href = "#"> Ejecución del Proyecto</a></li>
    <li><a href = "#"> Desarrollador</a></li>
</ul>
 
<h2 id = "Descripción">Descripción del Proyecto</h2>
 
<p>El proyecto está desarrollado en entorno Windows, su funcionamiento está diseñado para ejecutarse en la terminal de su sistema operativo. Es una simple imitación de una calculadora, salvo que lleva otras funcionalidades para retornar que la clásica calculadora, el usuario deberá optar por guardar o no su propio historial de operaciones en una base de datos que implemente.</p>
 
<h2 id = "Herrramientas">Herramientas Utilizadas</h2>
 
<h3>Entorno Virtual</h3>

<p>En el proyecto utilizo el entorno virtual para facilitar el acceso a la aplicación y no tener que descargar absolutamente nada en el sistema del usuario, ya que está todo instalado en el mismo entorno virtual que estoy dejando a descargar. <a href="#">Descargar</a> </p>
 
<h3>Módulos</h3>
 
<p>En el proyecto utilizo los módulos <b>Colorama</b> y <b>pymongo</b> que son módulos que no vienen por defecto en Python.</p>
 
<h3>Programación</h3>
 
<p>El programa está codificado con el lenguaje de programación <b>Python</b> en el entorno de desarrollo <b>Visual Studio Code</b> separados por módulos para ahorrar líneas de código, mantener un código ordenado y facilitar cualquier futura mejora en el programa, implementando documentación a través de los comentarios.</p>
 
<h3>Base de Datos</h3>
 
<p>En todos los proyectos que vaya realizando, utilizo o utilizaré la base de datos <b>MongoDB</b> para aprender y comprender como se trabaja con la BD JSON.</p>
 
<h2 id = "Funcionalidades">Funcionalidades</h2>
 
<li><b>Banner</b></li>

<br>
 
<p>La función del banner en el programa representa de alguna forma la muestra de los estados de conexión que va eligiendo el usuario hacia la base de datos, en caso de conectar se detalla la información del mismo y la información presentada es distinta si se conecta desde una base de datos con un nombre en específico o por defecto.</p>
 
<li><b>Banner con Conexión</b></li>

<br>

<p><img src = "https://github.com/Lucas-devSoft/Python/assets/111676352/beb02be4-30b3-4f42-98c5-c2c9c622ee7f"> 
<sub>En la imagen como se puede apreciar la extensión de MongoDB en visual estudio code me permite ver las bases de datos que tengo creadas en local host, como mencioné anteriormente, el Banner muestra información mostrando detalles como (tipo de conexión, nombre de la BD a la que está conectada al igual que su colección y su versión). La información que muestra es la BD por defecto la que fue originada en el código, pero en el caso de que el usuario llegue a generar una nueva automáticamente se conectara a ella y se mostrara en el banner.</sub></p>

<li><b>Banner sin Conexión</b></li>

<br>

<p><img src = "https://github.com/Lucas-devSoft/Python/assets/111676352/64b8fd15-8289-4e6e-9a36-f778c32fc396">
 
<sub>Como se puede apreciar en la imagen, en el banner del Menú se lanza el estado de conexión con el que ingreso el usuario, en este caso como es un ‘no’. El banner mostró que la calculadora está sin conexión, por ende no se guardara información.</sub></p>

<hr>

<li><b>Menus</b></li>

<br>

<p>La función de cada menú en el programa es para interactuar con el usuario y esperar una respuesta del mismo para continuar con cada funcionalidad del programa.</p>

<li><b>Menú Solicitud de Nombre</b></li>

<br>

<p><img src="https://github.com/Lucas-devSoft/Python/assets/111676352/ab9a8dec-e785-4872-8656-d5885ff460c6">
<sub>Esta funcionalidad esta para brindar una gentil bienvenida al programa al usuario y además su otra utilidad está en el caso de generar una conexión a la base de datos se agrega a la información a quién corresponde cada operación guardada.<br>
´Ejemplo - { _id : Autodesignado, Nombre: Lucas , Valor_1: 4 , Operador : + , Valor_2 : 4 , Resultado : 8}´.<br>
Es un ejemplo de como se subirá la insercion de los datos sin embargo a la hora de mostrarlo por pantalla se veran solo los valores sin claves.</sub></p>

<li><b>Menú Conexión a la Base de Datos</b></li>

<br>

<p><img src = "https://github.com/Lucas-devSoft/Python/assets/111676352/bd872f9c-9307-4ab9-bb6f-8009e5d15af7">
<sub>En esta funcionalidad se realiza la conexión a la base de datos, en el caso de escribir ‘sí’ se genera la conexión y en el caso de optar por ‘no’ va directamente al Menú de la Calculadora, destacando en el Banner un mensaje recordatorio que el usuario está en modo sin conexión.</sub></p>

<li><b>Menú del tipo de Conexión</b></li>

<br>
 
<p><img src = "https://github.com/Lucas-devSoft/Python/assets/111676352/cc695969-bbb4-4807-8fd9-185a35906151">
<sub>En este menú se solicita el tipo de conexión que se va a generar en MongoDB, es decir de forma local o bien mediante cuenta MongoDB Atlas para realizar el guardado de los datos, en caso de dar una respuesta errónea se lanzará un mensaje de error como en los casos anteriores.</sub></p>

<li><b>Menú de Generación de la BD</b></li>

<br>

<p><img src = "https://github.com/Lucas-devSoft/Python/assets/111676352/09b646d5-7d79-463a-b85b-b029da433799">
<sub>La funcionalidad de este Menú es que el usuario elija si quiere avanzar creando una base de datos con un nombre en específico que él elija o bien avanzar directamente desde una base de datos por defecto que yo nombre directamente en el código para que se creara en cuanto el usuario ponga que ‘no’ y pueda cargar sus datos ahí. En el caso de ‘no’ la Base de datos que se generará se llamara “Calculadora” con una colección llamada “Historial” en el caso de ‘sí’ se llamara como el usuario haya elegido.</sub></p>



<li><b>Creación de la BD</b></li>

<br>

<p><img src = "https://github.com/Lucas-devSoft/Python/assets/111676352/928deae3-29ae-4976-8156-c8619cb06ff0">
<sub>La funcionalidad de esta parte del programa es que el usuario pueda crear su base de datos con un nombre en específico y pueda cargar sus datos ahí. Si la Base de datos que quiere crear contiene el mismo nombre de una base de datos ya existente, optará por arrojar otro tipo de mensaje como “La base de datos ya existe y está activada para guardar.”</sub></p>

<hr>

<li><b>Errores</b></li>

<br>

<p>La función del error es advertir durante todo el programa que el usuario ha insertado una respuesta incorrecta, por lo que para poder continuar va a tener que reintentar hasta que inserte datos correctos y así mismo poder continuar con el flujo del programa.</p>

<li><b>Mensaje de error del nombre</b></li>

<br>

<p><img src = "https://github.com/Lucas-devSoft/Python/assets/111676352/89011179-e27e-4940-9abc-d606bdcaea7a"><br>
<sub>Devuelve este mensaje de error cuando se ingresa un nombre en un formato inválido o bien recibe como valor un espacio vacío. También se aprecia en la imagen como es insistente el error, cuando en el mismo mensaje de error también se brinda una respuesta errónea, al escribir <b>volver</b> vuelve nuevamente a la solicitud del nombre.</sub></p>

 <li><b>Mensaje de error de conexión</b></li>
 
 <br>
 
<p><img src = "https://github.com/Lucas-devSoft/Python/assets/111676352/93193661-d58d-40db-bf00-9936fa3f3a9e">
<sub>Devuelve este mensaje de error cuando se ingresa una respuesta inválida o bien recibe como valor un espacio vacío. También se aprecia en la imagen como insiste el error, cuando en el mismo mensaje de error se brinda una respuesta errónea, al escribir <b>volver</b> vuelve nuevamente a la solicitud de si quiere generar una conexión.</sub></p>
 
 
 <li><b>Error con el tipo de Conexión</b></li>
 
 <br>
 
 <p><img src = "https://github.com/Lucas-devSoft/Python/assets/111676352/0585cbf8-83ac-447a-ad16-b31c63b3ceb9">
<sub>En cada caso de error cambia su forma de respuesta marcando el sentido de la petición, es decir, que se informa al usuario que tipo de respuesta se espera para poder continuar con el programa o no.</sub></p>


<li><b>Mensaje de Error del Menú</b></li>

<br>

<p><img src = "https://github.com/Lucas-devSoft/Python/assets/111676352/963442f9-e1f6-4a06-928f-8032229a47d8">
<sub>Este Mensaje aparece cuando la opción que inserta el usuario no está dentro del Menú.</sub></p>

<hr>

<h2>Ejecución del Proyecto</h2>
<p>Para una correcta funcionalidad del programa se debera tener instalado:<br>
- <a href = "https://www.python.org/" type = "_blank">Python</a>
- 
</p>
De esta forma podremos activar el entorno virtual desde windows.
<img src = "https://github.com/Lucas-devSoft/Python/assets/111676352/0c3d8fc2-11df-401d-9976-7c346ced3f13">


