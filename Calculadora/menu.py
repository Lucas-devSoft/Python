""" Importaciones de Módulos """

from errores import *
from conexion import *
from logica import *
from colores import *
import re

""" Importaciones de Scripts """


"""  Comienzo del programa """

while True:

    Limpieza_consola()
    Cartel()

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█                     {texto}Hola! Usuario bienvenido, ¿Cuál es tu nombre?                    {fin+marco}█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
    """)
    nombre = input("\t\t\t\t\t    ")

    verificación = re.findall("[\W\d]+", nombre)

    if not verificación:

        while True:

            Limpieza_consola()
            Cartel()

            print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█                    {texto}Hola {nombre.capitalize()} bienvenido a mi programa!                              {fin+marco}█ {fin}
{marco+fondo}█                                                                                      {fin+marco}█ {fin}
{marco+fondo}█       {texto}¿Quieres generar un historial de tus operaciones en la Base de datos?          {fin+marco}█ {fin}
{marco+fondo}█                                                                                      {fin+marco}█ {fin}
{marco+fondo}█         {texto}SI, QUIERO GUARDAR <si>             NO, NO QUIERO GUARDAR <no>               {fin+marco}█ {fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
            """)
            respuesta_historial = input("\t\t\t\t\t    ")

            if respuesta_historial == "si":

                while True:

                    Limpieza_consola()
                    Cartel()

                    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█                {texto}Bien {nombre.capitalize()}, ahora elige que tipo de conexión deseas.                  {fin+marco}█ {fin}
{marco+fondo}█                                                                                      {fin+marco}█ {fin}
{marco+fondo}█                {error_texto}Recomendado: Tener instalado MongoDB en su sistema.                   {fin+marco}█ {fin}
{marco+fondo}█                                                                                      {fin+marco}█ {fin}
{marco+fondo}█          {texto}1 - Desde localhost                     {texto}2 - Desde cuenta atlas{fin+fondo}              {fin+marco}█ {fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
                    """)
                    respuesta_tipo_conexion = input("\t\t\t\t\t    ")

                    if respuesta_tipo_conexion == "1":

                        retorna_conexion = Conexión_Local()  # Bien
                        break

                    elif respuesta_tipo_conexion == "2":

                        retorna_conexion = Mongo_Atlas_Conexión()
                        break

                    else:

                        Limpieza_consola()
                        Cartel()
                        Error_Mensaje_de_Conexión()  # Bien

                break

            elif respuesta_historial == "no":

                respuesta_tipo_conexion = "no"
                retorna_conexion = "no"
                break  # Bien

            else:

                Limpieza_consola()
                Cartel()
                Error_Mensaje_de_BD()  # Bien

    else:

        Limpieza_consola()
        Cartel()
        Error_Mensaje_de_Nombre()  # Bien
        continue

    break

while True:

    Limpieza_consola()
    Cartel()

    retorna_banner = Banner(retorna_conexion, respuesta_tipo_conexion)

    Estado, Nombre_servidor, Version, Nombre_BD, Nombre_Doc = retorna_banner[0:5]

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█   {texto}Estado de la Conexión : {Estado}                                               {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█   {texto}Servidor : {Nombre_servidor}{fondo}                 {texto}MongoDB V. : {Version}{fondo}                  {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█   {texto}Base de Datos : {Nombre_BD}{fondo}            {texto}Documentación : {Nombre_Doc}{fondo}               {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}
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
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
""")

    opcion = input("\t\t\t\t\t    ").upper()

    if opcion == "A":

        try:

            Limpieza_consola()
            Cartel()

            retorna_A = opción_A()

            if respuesta_historial == "no":

                print(f"{marco+fondo}█      {error_texto}Recordatorio: Estas en modo sin conexión, no se guardaran sus movimientos.      {fin+marco}█{fin}")

            else:

                numero1, operador, numero2, resultado = retorna_A[0:4]
                Ingreso_Datos_AF(respuesta_tipo_conexion, nombre,
                                 numero1, operador, numero2, resultado)

        except:

            retorno_interno = Mensaje_de_Error_Interno()

        if respuesta_historial == "si":

            print(f"""{marco+fondo}█                                                                                      █{fin}       
{marco+fondo}█   {texto}VOLVER AL MENÚ <volver>   LIMPIAR HISTORIAL <limpiar>   FIN DEL PROGRAMA <fin>     {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
            """)

        else:

            print(f"""{marco+fondo}█                                                                                      █{fin}       
{marco+fondo}█            {texto}VOLVER AL MENÚ <volver>                   FIN DEL PROGRAMA <fin>          {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
            """)

        volver = input("\t\t\t\t\t    ").lower()

        if volver == "fin":

            Mensaje_de_Agradecimiento()

        elif volver == "volver":

            continue

        elif respuesta_historial == "si" and volver == "limpiar":

            Limpieza_consola()
            Borrar_historial()

        else:

            Limpieza_consola()
            Cartel()
            Mensaje_de_Error_Opciones()

    elif opcion == "B":

        try:

            Limpieza_consola()
            Cartel()

            retorna_B = opción_B()

            if respuesta_historial == "no":

                print(f"{marco+fondo}█      {error_texto}Recordatorio: Estas en modo sin conexión, no se guardaran sus movimientos.      {fin+marco}█{fin}")

            else:

                numero1, operador, numero2, resultado = retorna_B[0:4]
                Ingreso_Datos_AF(respuesta_tipo_conexion, nombre,
                                 numero1, operador, numero2, resultado)

        except:

            Mensaje_de_Error_Interno()

        if respuesta_historial == "si":

            print(f"""{marco+fondo}█                                                                                      █{fin}       
{marco+fondo}█   {texto}VOLVER AL MENÚ <volver>   LIMPIAR HISTORIAL <limpiar>   FIN DEL PROGRAMA <fin>     {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
            """)

        else:

            print(f"""{marco+fondo}█                                                                                      █{fin}       
{marco+fondo}█            {texto}VOLVER AL MENÚ <volver>                   FIN DEL PROGRAMA <fin>          {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
            """)

        volver = input("\t\t\t\t\t    ").lower()

        if volver == "fin":

            Mensaje_de_Agradecimiento()

        elif volver == "volver":

            continue

        elif respuesta_historial == "si" and volver == "limpiar":

            Limpieza_consola()
            Borrar_historial()

        else:

            Limpieza_consola()
            Cartel()
            Mensaje_de_Error_Opciones()

    elif opcion == "C":

        try:

            Limpieza_consola()
            Cartel()

            retorna_C = opción_C()

            if respuesta_historial == "no":

                print(f"{marco+fondo}█      {error_texto}Recordatorio: Estas en modo sin conexión, no se guardaran sus movimientos.      {fin+marco}█{fin}")

            else:

                numero1, operador, numero2, resultado = retorna_C[0:4]
                Ingreso_Datos_AF(respuesta_tipo_conexion, nombre,
                                 numero1, operador, numero2, resultado)

        except:

            Mensaje_de_Error_Interno()

        if respuesta_historial == "si":

            print(f"""{marco+fondo}█                                                                                      █{fin}       
{marco+fondo}█   {texto}VOLVER AL MENÚ <volver>   LIMPIAR HISTORIAL <limpiar>   FIN DEL PROGRAMA <fin>     {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
            """)

        else:

            print(f"""{marco+fondo}█                                                                                      █{fin}       
{marco+fondo}█            {texto}VOLVER AL MENÚ <volver>                   FIN DEL PROGRAMA <fin>          {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
            """)

        volver = input("\t\t\t\t\t    ").lower()

        if volver == "fin":

            Mensaje_de_Agradecimiento()

        elif volver == "volver":

            continue

        elif respuesta_historial == "si" and volver == "limpiar":

            Limpieza_consola()
            Borrar_historial()

        else:

            Limpieza_consola()
            Cartel()
            Mensaje_de_Error_Opciones()

    elif opcion == "D":

        try:

            Limpieza_consola()
            Cartel()

            retorna_D = opción_D()

            if respuesta_historial == "no":

                print(f"{marco+fondo}█      {error_texto}Recordatorio: Estas en modo sin conexión, no se guardaran sus movimientos.      {fin+marco}█{fin}")

            else:

                Numero1, Operador, Numero2, Resultado = retorna_D[0:4]
                Ingreso_Datos_AF(respuesta_tipo_conexion, nombre,
                                 Numero1, Operador, Numero2, Resultado)

        except:

            Mensaje_de_Error_Interno()

        if respuesta_historial == "si":

            print(f"""{marco+fondo}█                                                                                      █{fin}       
{marco+fondo}█   {texto}VOLVER AL MENÚ <volver>   LIMPIAR HISTORIAL <limpiar>   FIN DEL PROGRAMA <fin>     {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
            """)

        else:

            print(f"""{marco+fondo}█                                                                                      █{fin}       
{marco+fondo}█            {texto}VOLVER AL MENÚ <volver>                   FIN DEL PROGRAMA <fin>          {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
            """)

        volver = input("\t\t\t\t\t    ").lower()

        if volver == "fin":

            Mensaje_de_Agradecimiento()

        elif volver == "volver":

            continue

        elif respuesta_historial == "si" and volver == "limpiar":

            Limpieza_consola()
            Borrar_historial()

        else:

            Limpieza_consola()
            Cartel()
            Mensaje_de_Error_Opciones()

    elif opcion == "E":

        try:

            Limpieza_consola()
            Cartel()

            retorna_E = opción_E()

            if respuesta_historial == "no":

                print(f"{marco+fondo}█      {error_texto}Recordatorio: Estas en modo sin conexión, no se guardaran sus movimientos.      {fin+marco}█{fin}")

            else:

                numero1, operador, numero2, resultado = retorna_E[0:4]
                Ingreso_Datos_AF(respuesta_tipo_conexion, nombre,
                                 numero1, operador, numero2, resultado)

        except:

            Mensaje_de_Error_Interno()

        if respuesta_historial == "si":

            print(f"""{marco+fondo}█                                                                                      █{fin}       
{marco+fondo}█   {texto}VOLVER AL MENÚ <volver>   LIMPIAR HISTORIAL <limpiar>   FIN DEL PROGRAMA <fin>     {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
            """)

        else:

            print(f"""{marco+fondo}█                                                                                      █{fin}       
{marco+fondo}█            {texto}VOLVER AL MENÚ <volver>                   FIN DEL PROGRAMA <fin>          {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
            """)

        volver = input("\t\t\t\t\t    ").lower()

        if volver == "fin":

            Mensaje_de_Agradecimiento()

        elif volver == "volver":

            continue

        elif respuesta_historial == "si" and volver == "limpiar":

            Borrar_historial()

        else:

            Limpieza_consola()
            Cartel()
            Mensaje_de_Error_Opciones()

    elif opcion == "F":

        try:

            Limpieza_consola()
            Cartel()

            retorna_F = opción_F()

            if respuesta_historial == "no":

                print(f"{marco+fondo}█      {error_texto}Recordatorio: Estas en modo sin conexión, no se guardaran sus movimientos.      {fin+marco}█{fin}")

            else:

                numero1, operador, numero2, resultado = retorna_F[0:4]
                Ingreso_Datos_AF(respuesta_tipo_conexion, nombre,
                                 numero1, operador, numero2, resultado)

        except:

            Mensaje_de_Error_Interno()

        if respuesta_historial == "si":

            print(f"""{marco+fondo}█                                                                                      █{fin}       
{marco+fondo}█   {texto}VOLVER AL MENÚ <volver>   LIMPIAR HISTORIAL <limpiar>   FIN DEL PROGRAMA <fin>     {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
            """)

        else:

            print(f"""{marco+fondo}█                                                                                      █{fin}       
{marco+fondo}█            {texto}VOLVER AL MENÚ <volver>                   FIN DEL PROGRAMA <fin>          {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
            """)

        volver = input("\t\t\t\t\t    ").lower()

        if volver == "fin":

            Mensaje_de_Agradecimiento()

        elif volver == "volver":

            continue

        elif respuesta_historial == "si" and volver == "limpiar":

            Limpieza_consola()
            Borrar_historial()

        else:

            Limpieza_consola()
            Cartel()
            Mensaje_de_Error_Opciones()

    elif opcion == "G":

        try:

            Limpieza_consola()
            Cartel()

            retorna_G = opción_G()

            if respuesta_historial == "no":

                print(f"{marco+fondo}█      {error_texto}Recordatorio: Estas en modo sin conexión, no se guardaran sus movimientos.      {fin+marco}█{fin}")

            else:

                numero1, operador, conclusión = retorna_G[0:3]
                Ingreso_Datos_GH(respuesta_tipo_conexion, nombre, numero1, operador, conclusión)

        except:

            Mensaje_de_Error_Interno()

        if respuesta_historial == "si":

            print(f"""{marco+fondo}█                                                                                      █{fin}       
{marco+fondo}█   {texto}VOLVER AL MENÚ <volver>   LIMPIAR HISTORIAL <limpiar>   FIN DEL PROGRAMA <fin>     {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
            """)

        else:

            print(f"""{marco+fondo}█                                                                                      █{fin}       
{marco+fondo}█            {texto}VOLVER AL MENÚ <volver>                   FIN DEL PROGRAMA <fin>          {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
            """)

        volver = input("\t\t\t\t\t    ").lower()

        if volver == "fin":

            Mensaje_de_Agradecimiento()

        elif volver == "volver":

            continue

        elif respuesta_historial == "si" and volver == "limpiar":

            Limpieza_consola()
            Borrar_historial()

        else:

            Limpieza_consola()
            Cartel()
            Mensaje_de_Error_Opciones()

    elif opcion == "H":

        try:

            Limpieza_consola()
            Cartel()

            retorna_H = opción_H()

            if respuesta_historial == "no":

                print(f"{marco+fondo}█      {error_texto}Recordatorio: Estas en modo sin conexión, no se guardaran sus movimientos.      {fin+marco}█{fin}")

            else:

                numero, operador, conclusion = retorna_H[0:3]
                Ingreso_Datos_GH(respuesta_tipo_conexion,
                                 nombre, numero, operador, conclusion)

        except:

            Mensaje_de_Error_Interno()

        if respuesta_historial == "si":

            print(f"""{marco+fondo}█                                                                                      █{fin}       
{marco+fondo}█   {texto}VOLVER AL MENÚ <volver>   LIMPIAR HISTORIAL <limpiar>   FIN DEL PROGRAMA <fin>     {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
            """)

        else:

            print(f"""{marco+fondo}█                                                                                      █{fin}       
{marco+fondo}█            {texto}VOLVER AL MENÚ <volver>                   FIN DEL PROGRAMA <fin>          {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
            """)

        volver = input("\t\t\t\t\t    ").lower()

        if volver == "fin":

            Mensaje_de_Agradecimiento()

        elif volver == "volver":

            continue

        elif respuesta_historial == "si" and volver == "limpiar":

            Limpieza_consola()
            Borrar_historial()

        else:

            Limpieza_consola()
            Cartel()
            Mensaje_de_Error_Opciones()

    elif opcion == "I":

        try:

            Limpieza_consola()
            Cartel()

            opción_I()

        except:

            Mensaje_de_Error_Interno()

        print(f"""{marco+fondo}█                                                                                      █{fin}       
{marco+fondo}█            {texto}VOLVER AL MENÚ <volver>                   FIN DEL PROGRAMA <fin>          {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
            """)

        volver = input("\t\t\t\t\t    ").lower()

        if volver == "salir":

            Mensaje_de_Agradecimiento()

        elif volver == "volver":

            continue

    else:

        Limpieza_consola()
        Cartel()

        Error_Mensaje_de_Menu()  # Bien
