import time

from colores import *


"""
    Mensajes del main

"""


def Cartel():
    
    print(f"""{marco}
  /$$$$$$                                            /$$                     /$$                    
 /$$__  $$                                          | $$                    |__/                    
| $$  \__//$$$$$$   /$$$$$$  /$$$$$$/$$$$  /$$   /$$| $$  /$$$$$$   /$$$$$$  /$$  /$$$$$$   /$$$$$$$
| $$$$   /$$__  $$ /$$__  $$| $$_  $$_  $$| $$  | $$| $$ |____  $$ /$$__  $$| $$ /$$__  $$ /$$_____/
| $$_/  | $$  \ $$| $$  \__/| $$ \ $$ \ $$| $$  | $$| $$  /$$$$$$$| $$  \__/| $$| $$  \ $$|  $$$$$$ 
| $$    | $$  | $$| $$      | $$ | $$ | $$| $$  | $$| $$ /$$__  $$| $$      | $$| $$  | $$ \____  $$
| $$    |  $$$$$$/| $$      | $$ | $$ | $$|  $$$$$$/| $$|  $$$$$$$| $$      | $$|  $$$$$$/ /$$$$$$$/
|__/     \______/ |__/      |__/ |__/ |__/ \______/ |__/ \_______/|__/      |__/ \______/ |_______/ {fin}""")


def Mensaje_Agradecimiento():
    
    print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█                       {texto}Gracias por probar mi proyecto personal                         {fin+marco}█{fin}
{marco+fondo}█               {texto}En 5 segundos se cerrará el programa automáticamente.                   {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}""")
    
    time.sleep(5)
    exit()


def Mensaje_de_conexion():

    print(f"""        
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█         {texto}¿Quiere generar una conexión a la base de datos de MongoDB?                   {fin+marco}█{fin}""")


def Mensaje_tipo_de_conexion():

    print(f"""        
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█                  {texto}¿En que base de datos quiere generar la conexión?                    {fin+marco}█{fin}""")


"""
    Mensajes en Conexion Local

"""


def Renombrar_base_de_datos():

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█             {texto}¿Quiere crear una Base de datos con su propio renombre?                   {fin+marco}█{fin}""")


def Creando_nombre_de_la_base_de_datos():

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█                {texto}Creando la base de datos con su propio renombre.                       {fin+marco}█{fin}
{marco+fondo}█                                                                                       █{fin}""")


def Creacion_exitosa():

    print(f"""{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█                         {texto_correcto}La base de datos fue creada con éxito.                        {fin+marco}█{fin}
{marco+fondo}█                     {texto_correcto}Presione ENTER para continuar con el programa.                    {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}""")
    input()


def Base_de_datos_existente():

    print(f"""{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█                 {error_texto}La base de datos ya existe y ya esta activa para guardar!.            {fin+marco}█{fin}
{marco+fondo}█                       {error_texto}Presione ENTER para continuar con el programa.                  {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}""")
    input()


"""
    Mensajes en Conexion Atlas

"""


def Mensaje_cuenta_atlas():
    
    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█               {texto}Bienvendo vas a ingresar al servidor de tu cuenta Atlas                 {fin+marco}█{fin}
{marco+fondo}█                                                                                       █{fin}""")
    

def Mensaje_estando_adentro_atlas(Usuario, Nombre_cluster):
    
    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█    {texto}Estado :  {texto_correcto+"Conectado"+fin+fondo+texto}       Cuenta: {texto_correcto+Usuario+fin+fondo+texto}       Nombre del cluster: {texto_correcto+Nombre_cluster+fondo}      {fin+marco}█{fin}
{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█             {texto}¿Quiere crear una Base de datos con su propio renombre?                   {fin+marco}█{fin}""")
    
    
def Menu_formulario(Estado: str, Nombre_servidor: str, Nombre_base_de_datos: str,
                    Nombre_documentacion: str, estado_A: str, estado_B: str, estado_C: str):
    
    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█  {texto}Estado de la Conexión : {Estado}                               {fin+marco}█{fin}
{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█          {texto}Base de Datos : {Nombre_base_de_datos} {texto}Documentación : {Nombre_documentacion} {fin+marco}█{fin}
{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█    {texto}Nombre del Servidor : {Nombre_servidor}            {fin+marco}█{fin}                
{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█                       {texto}Formularios                                  Estados            {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█             {texto}A ► DATOS PERSONALES DEL USUARIO                      {estado_A}          {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█             {texto}B ► DATOS LABORALES DEL USUARIO                       {estado_B}          {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█             {texto}C ► DATOS ACADÉMICOS DEL USUARIO                      {estado_C}          {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")

    respuesta = input(
        f"{marco+fondo}█      {texto}Escriba la letra del formulario que desea realizar : {fin}          ").upper()
    
    return respuesta


def Menu_formulario_completado(Estado: str, Nombre_servidor: str, Base_de_Datos: str,
                    Documentacion: str, estado_A: str, estado_B: str, estado_C: str):
    
    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█  {texto}Estado de la Conexión : {Estado}                               {fin+marco}█{fin}
{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█          {texto}Base de Datos : {Base_de_Datos} {texto}Documentación : {Documentacion} {fin+marco}█{fin}
{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█    {texto}Nombre del Servidor : {Nombre_servidor}            {fin+marco}█{fin}                
{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█                       {texto}Formularios                                  Estados            {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█             {texto}A ► DATOS PERSONALES DEL USUARIO                      {estado_A}          {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█             {texto}B ► DATOS LABORALES DEL USUARIO                       {estado_B}          {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█             {texto}C ► DATOS ACADÉMICOS DEL USUARIO                      {estado_C}          {fin+marco}█{fin}""")




def Mensaje_formulario_completado():
    
    print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█                     {texto_correcto}El formulario fue completado correctamente                        {fin+marco}█{fin}""")
    

def Mensaje_formulario_ya_completado():
    
    print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█            {error_texto}El formulario que quiere realizar ya aparece como completado!.             {fin+marco}█{fin}
{marco+fondo}█                            {texto}Presione ENTER para continuar.                             {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}""")
    input()


"""
    Mensajes para Conexion local

"""


def Mensaje_guardado_exitosamente():
    
    print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█                      {texto_correcto}La información fue guardada exitosamente.                        {fin+marco}█{fin}
{marco+fondo}█                            {texto}Presione ENTER para continuar.                             {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}""")
    input()


def Mensaje_error_guardado():
    
    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                      {error_texto}La información no pudo ser guardada.             {fin+marco}█{fin}
{marco+fondo}█                            {texto}Presione ENTER para continuar.                             {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}""")
    input()
    
    
def Mensaje_de_visualizacion_local_personales():
    
    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█      {texto}Visualización del formulario de "Datos Personales" en MongoDB Local.             {fin+marco}█{fin}
{marco+fondo}█                                                                                       █{fin}""")
    
def Mensaje_de_visualizacion_local_laborales():
    
    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█      {texto}Visualización del formulario de "Datos Laborales" en MongoDB Local.              {fin+marco}█{fin}
{marco+fondo}█                                                                                       █{fin}""")
    

def Mensaje_de_visualizacion_local_academico():
    
    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█      {texto}Visualización del formulario de "Datos Académicos" en MongoDB Local.             {fin+marco}█{fin}
{marco+fondo}█                                                                                       █{fin}""")    


"""
    Mensajes para Conexion atlas

"""


def Mensaje_de_visualizacion_atlas_personales():
    
    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█      {texto}Visualización del formulario de "Datos Personales" en cuenta Atlas.             {fin+marco}█{fin}
{marco+fondo}█                                                                                       █{fin}""")
    

def Mensaje_de_visualizacion_atlas_laborales():
    
    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█      {texto}Visualización del formulario de "Datos Laborales" en cuenta Atlas.              {fin+marco}█{fin}
{marco+fondo}█                                                                                       █{fin}""")
    

def Mensaje_de_visualizacion_atlas_academico():
    
    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█      {texto}Visualización del formulario de "Datos Académicos" en cuenta Atlas.             {fin+marco}█{fin}
{marco+fondo}█                                                                                       █{fin}""")
    

"""

    Mensajes para exportacion.

"""


def Mensaje_exportacion_correcta():
    
    print(f"""{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█                   {texto_correcto}Exportación de los formularios exitosamente.                        {fin+marco}█{fin}
{marco+fondo}█                            {texto}Presione ENTER para continuar.                             {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}""")
    
    input()


def Mensaje_exportacion_incorrecta():
    
    print(f"""{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█    {error_texto}Error al intentar exportar los formularios, posiblemente el archivo ya exista.     {fin+marco}█{fin}
{marco+fondo}█                            {texto}Presione ENTER para continuar.                             {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}""")
    
    input()
    

"""

    Mensajes para el correo

"""  

    
def Mensaje_correo_electronico():
    
    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█                {texto}Estas por enviar la información por correo electrónico.                {fin+marco}█{fin}""")
    

def Mensaje_cuenta_aceptada():
    
    print(f"""{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█                         {texto_correcto}Cuenta aceptada correctamente!.                            {fin+marco}█{fin}
{marco+fondo}█                            {texto}Presione ENTER para continuar.                             {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}""")


def Mensaje_error_cuenta():
    
    print(f"""{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█                    {error_texto}El usuario o la contraseña no son correctos                        {fin+marco}█{fin}
{marco+fondo}█                            {texto}Presione ENTER para continuar.                             {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}""")
    input()
    
    
def Mensaje_envio_de_mensaje(Correo_electronico):
    
    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█      {texto}La información se enviará con el correo : {texto_correcto}{Correo_electronico}.        {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
    

def Envio_exitoso():

    print(f"""{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█                          {texto_correcto}Mensaje enviado correctamente!.                              {fin+marco}█{fin}""")