from colores import *
from mensajes import *


def Error_Nombre():

    print(f"""{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█             {error_texto}Error con el formato del nombre o el campo esta vacío.                   {fin+marco}█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}""")
    opción = input(
        f"{marco+fondo}█    {texto}REINTENTAR <r>       Fin del Programa <fin>     Respuesta : {fin}        ").lower()

    while opción != "r" and opción != "fin":

        print(f"""{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█             {error_texto}Error nuevamente, como respuesta se espera 'r' o 'fin'.                  {fin+marco}█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}""")
        opción = input(
            f"{marco+fondo}█    {texto}REINTENTAR <r>       Fin del Programa <fin>     Respuesta : {fin}        ").lower()

        if opción == "r":

            pass

        elif opción == "fin":

            Mensaje_de_Agradecimiento()

    else:

        if opción == "r":

            pass

        elif opción == "fin":

            Mensaje_de_Agradecimiento()


def Error_si_no():

    print(f"""{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█             {error_texto}Respuesta inválida, como respuesta se espera 'si' o 'no'.                {fin+marco}█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}""")
    opción = input(
        f"{marco+fondo}█    {texto}REINTENTAR <r>       Fin del Programa <fin>     Respuesta : {fin}        ").lower()

    while opción != "r" and opción != "fin":

        print(f"""{marco+fondo}█                                                                                      {fin+marco}█ {fin}
{marco+fondo}█             {error_texto}Error nuevamente, como respuesta se espera 'r' o 'fin'.                  {fin+marco}█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}""")
        opción = input(
            f"{marco+fondo}█    {texto}REINTENTAR <r>       Fin del Programa <fin>     Respuesta : {fin}        ").lower()

        if opción == "r":

            pass

        elif opción == "fin":

            Mensaje_de_Agradecimiento()

    else:

        if opción == "r":

            pass

        elif opción == "fin":

            Mensaje_de_Agradecimiento()


def Error_Tipo_de_Conexión():

    print(f"""{marco+fondo}█                                                                                      {fin+marco}█ {fin}
{marco+fondo}█       {error_texto}Respuesta inválida, como respuesta se espera 'local' o 'atlas'.                {fin+marco}█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}""")
    opción = input(
        f"{marco+fondo}█    {texto}REINTENTAR <r>       Fin del Programa <fin>     Respuesta : {fin}        ").lower()

    while opción != "r" and opción != "fin":

        print(f"""{marco+fondo}█                                                                                      {fin+marco}█ {fin}
{marco+fondo}█             {error_texto}Error nuevamente, como respuesta se espera 'r' o 'fin'.                  {fin+marco}█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}""")
        opción = input(
            f"{marco+fondo}█    {texto}REINTENTAR <r>       Fin del Programa <fin>     Respuesta : {fin}        ").lower()

        if opción == "r":

            pass

        elif opción == "fin":

            Mensaje_de_Agradecimiento()

    else:

        if opción == "r":

            pass

        elif opción == "fin":

            Mensaje_de_Agradecimiento()


def Error_Menu_desplazamiento_limpiar():

    print(f"""{marco+fondo}█                                                                                      {fin+marco}█ {fin}
{marco+fondo}█       {error_texto}Respuesta inválida, como respuesta se espera 'limpiar' o 'volver'.             {fin+marco}█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}""")
    opción = input(
        f"{marco+fondo}█    {texto}REINTENTAR <r>       Fin del Programa <fin>     Respuesta : {fin}        ").lower()

    while opción != "r" and opción != "fin":

        print(f"""{marco+fondo}█                                                                                      {fin+marco}█ {fin}
{marco+fondo}█             {error_texto}Error nuevamente, como respuesta se espera 'r' o 'fin'.                  {fin+marco}█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}""")
        opción = input(
            f"{marco+fondo}█    {texto}REINTENTAR <r>       Fin del Programa <fin>     Respuesta : {fin}        ").lower()

        if opción == "r":

            pass

        elif opción == "fin":

            Mensaje_de_Agradecimiento()

    else:

        if opción == "r":

            pass

        elif opción == "fin":

            Mensaje_de_Agradecimiento()


def Error_Mensaje_de_Menu():

    print(f"""{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█               {error_texto}La opción que elegiste no esta dentro del menú.                        {fin+marco}█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}""")
    opción = input(
        f"{marco+fondo}█    {texto}REINTENTAR <r>       Fin del Programa <fin>     Respuesta : {fin}        ").lower()

    while opción != "r" and opción != "fin":

        print(f"""{marco+fondo}█                                                                                      {fin+marco}█ {fin}
{marco+fondo}█             {error_texto}Error nuevamente, como respuesta se espera 'r' o 'fin'.                  {fin+marco}█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}""")
        opción = input(
            f"{marco+fondo}█    {texto}REINTENTAR <r>       Fin del Programa <fin>     Respuesta : {fin}        ").lower()

        if opción == "volver":

            pass

        elif opción == "fin":

            Mensaje_de_Agradecimiento()

    else:

        if opción == "volver":

            pass

        elif opción == "fin":

            Mensaje_de_Agradecimiento()


def Mensaje_de_Error_Interno():

    print(f"""{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█               {error_texto}Error Interno! el retorno no esta devolviendo un valor                 {fin+marco}█{fin}
{marco+fondo}█          {error_texto}Posibles causas: Inserto letras como valor o un número erróneo.             {fin+marco}█{fin}
{marco+fondo}█                        {texto}Presiones ENTER para volver a intentar...                     {marco+fondo}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}""")
    input()


def Mensaje_error_atras():

    print(f"""{marco+fondo}█                                                                                      {fin+marco}█ {fin}
{marco+fondo}█         {error_texto}Respuesta inválida, como respuesta se espera 'volver' o 'fin'.               {fin+marco}█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}""")
    opción = input(
        f"{marco+fondo}█    {texto}REINTENTAR <r>       Fin del Programa <fin>     Respuesta : {fin}        ").lower()

    while opción != "r" and opción != "fin":

        print(f"""{marco+fondo}█                                                                                      {fin+marco}█ {fin}
{marco+fondo}█             {error_texto}Error nuevamente, como respuesta se espera 'r' o 'fin'.                  {fin+marco}█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}""")
        opción = input(
            f"{marco+fondo}█    {texto}REINTENTAR <r>       Fin del Programa <fin>     Respuesta : {fin}        ").lower()

        if opción == "r":

            pass

        elif opción == "fin":

            Mensaje_de_Agradecimiento()

    else:

        if opción == "r":

            pass

        elif opción == "fin":

            Mensaje_de_Agradecimiento()
