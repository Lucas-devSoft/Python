import time

from colores import *


def Error_Mensaje_de_Nombre():

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█              {error_texto}Se detecto el campo vacío o con un formato de nombre inválido.          {fin+marco}█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█          {texto}VOLVER A INTENTAR <volver>               FIN DEL PROGRAMA <fin>             {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
    """)
    opción = input("\t\t\t\t\t    ").lower()

    while opción != "volver" and opción != "fin":

        print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█          {error_texto}Respuesta inválida, como respuesta se espera 'volver' o 'fin'.              {fin+marco}█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█          {texto}VOLVER A INTENTAR <volver>               FIN DEL PROGRAMA <fin>             {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
        """)
        opción = input("\t\t\t\t\t    ").lower()

    else:

        if opción == "volver":

            pass

        elif opción == "fin":

            Mensaje_de_Agradecimiento()


def Error_Mensaje_de_BD():

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█             {error_texto}Respuesta inválida, como respuesta se espera 'si' o 'no'.                {fin+marco}█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█          {texto}VOLVER A INTENTAR <volver>               FIN DEL PROGRAMA <fin>             {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
    """)
    opción = input("\t\t\t\t\t    ").lower()

    while opción != "volver" and opción != "fin":

        print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      {fin+marco}█ {fin}
{marco+fondo}█          {error_texto}Respuesta inválida, como respuesta se espera 'volver' o 'fin'.              {fin+marco}█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█          {texto}VOLVER A INTENTAR <volver>               FIN DEL PROGRAMA <fin>             {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
        """)
        opción = input("\t\t\t\t\t    ").lower()

    else:

        if opción == "volver":

            pass

        elif opción == "fin":

            Mensaje_de_Agradecimiento()


def Error_Mensaje_de_Conexión():

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      {fin+marco}█ {fin}
{marco+fondo}█              {error_texto}Respuesta inválida, como respuesta se espera '1' o '2'.                 {fin+marco}█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█          {texto}VOLVER A INTENTAR <volver>               FIN DEL PROGRAMA <fin>             {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
    """)
    opción = input("\t\t\t\t\t    ").lower()

    while opción != "volver" and opción != "fin":

        print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      {fin+marco}█ {fin}
{marco+fondo}█          {error_texto}Respuesta inválida, como respuesta se espera 'volver' o 'fin'.              {fin+marco}█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█          {texto}VOLVER A INTENTAR <volver>               FIN DEL PROGRAMA <fin>             {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
        """)
        opción = input("\t\t\t\t\t    ").lower()

    else:

        if opción == "volver":

            pass

        elif opción == "fin":

            Mensaje_de_Agradecimiento()


def Error_Mensaje_pre_Conexión():

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      {fin+marco}█ {fin}
{marco+fondo}█              {error_texto}Respuesta inválida, como respuesta se espera 'si' o 'no'.               {fin+marco}█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█          {texto}VOLVER A INTENTAR <volver>               FIN DEL PROGRAMA <fin>             {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
    """)
    opción = input("\t\t\t\t\t    ").lower()

    while opción != "volver" and opción != "fin":

        print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      {fin+marco}█ {fin}
{marco+fondo}█        {error_texto}Respuesta inválida, como respuesta se espera 'volver' o 'fin'.                {fin+marco}█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█          {texto}VOLVER A INTENTAR <volver>               FIN DEL PROGRAMA <fin>             {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
        """)
        opción = input("\t\t\t\t\t    ").lower()

    else:

        if opción == "volver":

            pass

        elif opción == "fin":

            Mensaje_de_Agradecimiento()


def Error_Mensaje_de_Menu():

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█               {error_texto}La opción que elegiste no esta dentro del menú.                        {fin+marco}█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█          {texto}VOLVER A INTENTAR <volver>               FIN DEL PROGRAMA <fin>             {fin+marco}█{fin}        
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
    """)
    opción = input("\t\t\t\t\t    ").lower()

    while opción != "volver" and opción != "fin":

        print()

        print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█          {error_texto}Respuesta inválida, como respuesta se espera 'volver' o 'fin'.              {fin+marco}█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█          {texto}VOLVER A INTENTAR <volver>               FIN DEL PROGRAMA <fin>             {fin+marco}█{fin}        
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
        """)
        opción = input("\t\t\t\t\t    ").lower()

    else:

        if opción == "volver":

            pass

        elif opción == "fin":

            Mensaje_de_Agradecimiento()


def Mensaje_de_Agradecimiento():

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█                    {texto}Muchas gracias por probar mi programa.                            {fin+marco}█{fin}
{marco+fondo}█               {texto}El programa se cerrará automáticamente en 5 segundos.                  {fin+marco}█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
    """)

    time.sleep(5)

    exit()


def Mensaje_de_Error_Interno():

    print(f"""{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█               {error_texto}Error Interno! el retorno no esta devolviendo un valor                 {fin+marco}█{fin}
{marco+fondo}█          {error_texto}Posibles causas: Inserto letras como valor o un número erróneo.             {fin+marco}█{fin}""")

    return True


def Mensaje_de_Error_Opciones():

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█                {error_texto}La opción que elegiste no esta dentro del menú.                       {fin+marco}█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█          {texto}VOLVER A INTENTAR <volver>               FIN DEL PROGRAMA <fin>             {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
    """)
    opción = input("\t\t\t\t      ").lower()

    while opción != "volver" and opción != "fin":

        print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█         {error_texto}Respuesta inválida, como respuesta se espera 'volver' o 'fin'.               {fin+marco}█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█          {texto}VOLVER A INTENTAR <volver>               FIN DEL PROGRAMA <fin>             {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
        """)
        opción = input("\t\t\t\t      ").lower()

    else:

        if opción == "volver":

            pass

        elif opción == "fin":

            Mensaje_de_Agradecimiento()
