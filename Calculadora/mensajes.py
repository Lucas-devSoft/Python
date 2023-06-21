from colores import *


"""
    Nombre del Proyecto

"""

def Cartel():
    
    print(f"""{marco}
██████╗ █████╗ ██╗     ██████╗██╗   ██╗██╗      █████╗ ██████╗  ██████╗ ██████╗  █████╗
██╔═══╝██╔══██╗██║     ██╔═══╝██║   ██║██║     ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔══██╗
██║    ███████║██║     ██║    ██║   ██║██║     ███████║██║  ██║██║   ██║██████╔╝███████║
██║    ██╔══██║██║     ██║    ██║   ██║██║     ██╔══██║██║  ██║██║   ██║██╔══██╗██╔══██║
██████╗██║  ██║███████╗██████╗████████║███████╗██║  ██║██████╔╝╚██████╔╝██║  ██║██║  ██║
╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝╚═══════╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝{fin}""")


"""
    Mensaje de la peticion del Nombre

"""


def Nombre():

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}""")
    nombre = input(
        f"{marco+fondo}█  {texto}Hola! Usuario bienvenido, ¿Cuál es su nombre?   Respuesta : {fin}     ")

    return nombre


"""

    Mensaje Si quiere crear una Base de datos

"""


def Base_de_datos(nombre: str):

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█                    {texto}Hola {nombre.capitalize():^5} bienvenido a mi programa!                              {fin+marco}█ {fin}
{marco+fondo}█                                                                                      {fin+marco}█ {fin}
{marco+fondo}█       {texto}¿Quieres generar un historial de tus operaciones en la Base de datos?          {fin+marco}█ {fin}""")


"""

    Mensaje Con que tipo de Base de datos quiere entrar 

"""


def Tipo_de_conexion():

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█               {texto}Que tipo de conexión quiere generar con la Base de datos.              {fin+marco}█ {fin}
{marco+fondo}█                                                                                      {fin+marco}█ {fin}
{marco+fondo}█                {error_texto}Recomiendo: Tener instalado MongoDB en su sistema.                    {fin+marco}█ {fin}""")


"""

    Mensajes para la conexion Local

"""


def Creando_BD():

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█          {texto}¿Quiere generar una Base de datos con su propio renombre?                   {fin+marco}█{fin}""")


"""

    Mensaje de ingreso a la sección de la creación de la base de datos.

"""

def Base_de_datos_nueva():
    
    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█           {texto}Creación de la base de datos con un nombre específico.                     {fin+marco}█{fin}""")


"""

    Mensaje Base de datos creada con exito

"""


def Creada_con_exito():
    
    print(f"""{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█                         {texto_correcto}La base de datos fue creada con éxito.                       {fin+marco}█{fin}
{marco+fondo}█                     {texto_correcto}Presione ENTER para continuar con el programa.                   {fin+marco}█{fin}  
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}""")
    input()


"""

    Mensaje Base de datos existente

"""


def Base_existente():

    print(f"""{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█                 {error_texto}La base de datos ya existe y ya esta activa para guardar!.           {fin+marco}█{fin}
{marco+fondo}█                       {error_texto}Presione ENTER para continuar con el programa.                 {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}""")
    input()


"""

    Mensajes para la conexion atlas

"""


def Cuenta_atlas():
    
    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                       {texto}Bienvenido a cuenta de MongoDB Atlas                           {fin+marco}█{fin}""")


def Creando_base_de_datos_atlas(): 
    
    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}Creación del nombre para su Base de datos.                       {fin+marco}█{fin}""")
    
    
def Genera_base_de_datos_atlas(Usuario: str, Nombre_cluster: str):

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█    {texto}Estado : {texto_correcto}Conectado{fin}{fondo}        {texto}Usuario : {texto_correcto}{Usuario}{fin}{fondo}        {texto}Cluster : {texto_correcto}{Nombre_cluster}{fondo}            {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█            {texto}¿Desea generar una Base de datos con un nombre especifico?                {fin+marco}█{fin}""")
    

"""

    Mensaje de que la cuenta de atlas is incorrecta

"""


def Mensaje_de_error_atlas():
    
    print(f"""{marco+fondo}█                                                                                      {marco+fondo}█{fin}
{marco+fondo}█                            {error_texto}Los datos del servidor no existen                         {marco+fondo}█{fin}
{marco+fondo}█                        {texto}Presiones ENTER para volver a intentar...                     {marco+fondo}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}""")
    input()


"""

    Mensaje menú principal de la calculadora

"""


def Menu():
    
    print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                      {texto}Calculadora desarrollada con Python                             {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}A ► Adición                                (+)                   {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}B ► Sustracción                            (-)                   {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}C ► Multiplicación                         (*)                   {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}D ► División                               (/)                   {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}E ► Potenciación                          (b,e)                  {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}F ► Radicación                             (√)                   {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}G ► ¿El número es par o impar?                                   {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}H ► ¿El número es primo?                                         {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}I ► Rango de números primos                                      {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")
    opcion = input(f"{marco+fondo}█                      {texto}Escriba su respuesta aqui : {fin}              ").upper()    
    
    return opcion


"""

    Mensaje de la opción elegida

"""


def Mensaje_suma():

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}A ► Adición                               (+)                    {marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")


def Mensaje_resta():

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}B ► Sustracción                            (-)                   {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")


def Mensaje_multi():

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}C ► Multiplicación                         (*)                   {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")


def Mensaje_div():  

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}D ► División                               (/)                   {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")


def Mensaje_pote():

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}E ► Potenciación                           (b,e)                 {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")


def Mensaje_radi():

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}F ► Radicación                            (√)                    {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")


def Mensaje_paridad():

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                         {texto}G ► ¿El número es par o impar?                               {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")


def Mensaje_primo():

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                         {texto}H ► ¿El número es primo?                                     {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")


def Mensaje_primos_rango():

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                          {texto}I ► Rango de números primos.                                {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")


def Mensaje_recordatorio_sin_conexion():
    
    print(f"{marco+fondo}█      {error_texto}Recordatorio: Estas en modo sin conexión, no se guardaran sus movimientos.      {fin+marco}█{fin}")
    
    
def Mensaje_historial_local():
    
    print(f"""{marco+fondo}█                  {texto}Historial de movimientos desde MongoDB Localhost.                   {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")


def Mensaje_historial_atlas():
    
    print(f"""{marco+fondo}█                    {texto}Historial de movimientos desde MongoDB Atlas.                     {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")
    
    
def Mensaje_Borrado_exitoso():
    
    print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                        {texto_correcto}Los datos fueron borrados exitosamente.                       {fin+marco}█{fin}
{marco+fondo}█                     {texto}Presione ENTER para continuar con el programa.                   {fin+marco}█{fin}  
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}""")
    input()