from colores import *
from logica import *


def Error_Menu():

    while True:

        print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█                    {error_texto}La opción elegida no esta dentro del menú                          {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█          {texto}VOLVER A INTENTAR <volver>                 FIN DEL PROGRAMA <fin>            {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
                """)

        respuesta = input("\t\t\t\t\t").lower()

        if respuesta == "volver":

            break

        elif respuesta == "fin":

            Mensaje_Agradecimiento()

        else:

            while respuesta != "volver" and respuesta != "fin":

                Limpiar_consola()
                Cartel()

                print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█            {error_texto}Respuesta inválida, como respuesta se espera 'volver' o 'fin'              {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█          {texto}VOLVER A INTENTAR <volver>                 FIN DEL PROGRAMA <fin>            {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
                """)

                respuesta = input("\t\t\t\t\t").lower()

                if respuesta == "volver":

                    break

                elif respuesta == "fin":

                    Mensaje_Agradecimiento()

        break


def Error_Campo():

    print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█           {error_texto}Formulario interrumpido por un error de formato en este campo.              {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█              {texto}REINTENTAR  <r>                    FIN DEL PROGRAMA <fin>                {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
    """)

    reintentar = input("\t\t\t\t\t").lower()

    if reintentar == "r":

        pass

    elif reintentar == "fin":

        Mensaje_Agradecimiento()

    else:

        while True:

            print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█             {error_texto}Respuesta incorrecta, como respuesta se espera "r" o "fin"                {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█          {texto}VOLVER A INTENTAR <volver>                 FIN DEL PROGRAMA <fin>            {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
                    """)

            respuesta = input("\t\t\t\t\t").lower()

            if respuesta == "volver":

                break

            elif respuesta == "fin":

                Mensaje_Agradecimiento()

            else:

                while respuesta != "volver" and respuesta != "fin":

                    Limpiar_consola()
                    Cartel()

                    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█            {error_texto}Respuesta inválida, como respuesta se espera 'volver' o 'fin'              {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█          {texto}VOLVER A INTENTAR <volver>                 FIN DEL PROGRAMA <fin>            {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
                    """)

                    respuesta = input("\t\t\t\t\t").lower()

                    if respuesta == "volver":

                        break

                    elif respuesta == "fin":

                        Mensaje_Agradecimiento()

            break


def Error_Respuesta():

    while True:

        print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█             {error_texto}Respuesta incorrecta, como respuesta se espera "si" o "no"                {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█          {texto}VOLVER A INTENTAR <volver>                 FIN DEL PROGRAMA <fin>            {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
                """)

        respuesta = input("\t\t\t\t\t").lower()

        if respuesta == "volver":

            break

        elif respuesta == "fin":

            Mensaje_Agradecimiento()

        else:

            while respuesta != "volver" and respuesta != "fin":

                Limpiar_consola()
                Cartel()

                print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█            {error_texto}Respuesta inválida, como respuesta se espera 'volver' o 'fin'              {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█          {texto}VOLVER A INTENTAR <volver>                 FIN DEL PROGRAMA <fin>            {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
                """)

                respuesta = input("\t\t\t\t\t").lower()

                if respuesta == "volver":

                    break

                elif respuesta == "fin":

                    Mensaje_Agradecimiento()

        break
