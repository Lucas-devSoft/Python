from colores import *
from mensajes import *
from logica import *


def Error_Respuesta():

    print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█             {error_texto}Respuesta incorrecta, como respuesta se espera "si" o "no"                {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
    respuesta = input(
        f"{marco+fondo}█        {texto}REINTENTAR <r>      FIN DEL PROGRAMA <fin>       Respuesta : {fin}      ").lower()

    while respuesta != "r" and respuesta != "fin":

        print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█               {error_texto}Error nuevamente, como respuesta se espera "r" o "fin"                  {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
        respuesta = input(
            f"{marco+fondo}█        {texto}REINTENTAR <r>      FIN DEL PROGRAMA <fin>       Respuesta : {fin}      ").lower()

        if respuesta == "r":

            break

        elif respuesta == "fin":

            Mensaje_Agradecimiento()

    else:

        if respuesta == "r":

            pass

        elif respuesta == "fin":

            Mensaje_Agradecimiento()


def Error_Tipo_Conexión():

    print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█          {error_texto}Respuesta incorrecta, como respuesta se espera "local" o "atlas"             {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
    respuesta = input(
        f"{marco+fondo}█        {texto}REINTENTAR <r>      FIN DEL PROGRAMA <fin>       Respuesta : {fin}      ").lower()

    while respuesta != "r" and respuesta != "fin":

        print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█               {error_texto}Error nuevamente, como respuesta se espera "r" o "fin"                  {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
        respuesta = input(
            f"{marco+fondo}█        {texto}REINTENTAR <r>      FIN DEL PROGRAMA <fin>       Respuesta : {fin}      ").lower()

        if respuesta == "r":

            break

        elif respuesta == "fin":

            Mensaje_Agradecimiento()

    else:

        if respuesta == "r":

            pass

        elif respuesta == "fin":

            Mensaje_Agradecimiento()


def Error_de_conexion():

    print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█               {error_texto}Error de conexión, no se puede conectar con MongoDB                     {fin+marco}█{fin}
{marco+fondo}█        {error_texto}Posible causa: No tenga instalado el driver de MongoDB en su sistema.          {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
    respuesta = input(
        f"{marco+fondo}█        {texto}REINTENTAR <r>      FIN DEL PROGRAMA <fin>       Respuesta : {fin}      ").lower()

    while respuesta != "r" and respuesta != "fin":

        print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█               {error_texto}Error nuevamente, como respuesta se espera "r" o "fin"                  {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
        respuesta = input(
            f"{marco+fondo}█        {texto}REINTENTAR <r>      FIN DEL PROGRAMA <fin>       Respuesta : {fin}      ").lower()

        if respuesta == "r":

            break

        elif respuesta == "fin":

            Mensaje_Agradecimiento()

    else:

        if respuesta == "r":

            pass

        elif respuesta == "fin":

            Mensaje_Agradecimiento()


def Error_de_conexion_Atlas():

    print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█               {error_texto}Error de conexión, no se puede conectar con MongoDB                     {fin+marco}█{fin}
{marco+fondo}█{error_texto}Posibles causas: No este instalado el driver de mongoDB o datos de cuenta incorrectos. {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
    respuesta = input(
        f"{marco+fondo}█        {texto}REINTENTAR <r>      FIN DEL PROGRAMA <fin>       Respuesta : {fin}      ").lower()

    while respuesta != "r" and respuesta != "fin":

        print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█               {error_texto}Error nuevamente, como respuesta se espera "r" o "fin"                  {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
        respuesta = input(
            f"{marco+fondo}█        {texto}REINTENTAR <r>      FIN DEL PROGRAMA <fin>       Respuesta : {fin}      ").lower()

        if respuesta == "r":

            break

        elif respuesta == "fin":

            Mensaje_Agradecimiento()

    else:

        if respuesta == "r":

            pass

        elif respuesta == "fin":

            Mensaje_Agradecimiento()


def Error_Creacion_BD():

    print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█          {error_texto}No fue posible crear la base de datos, formato de nombre incorrecto!.        {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
    respuesta = input(
        f"{marco+fondo}█        {texto}REINTENTAR <r>      FIN DEL PROGRAMA <fin>       Respuesta : {fin}      ").lower()

    while respuesta != "r" and respuesta != "fin":

        print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█               {error_texto}Error nuevamente, como respuesta se espera "r" o "fin"                  {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
        respuesta = input(
            f"{marco+fondo}█        {texto}REINTENTAR <r>      FIN DEL PROGRAMA <fin>       Respuesta : {fin}      ").lower()

        if respuesta == "r":

            break

        elif respuesta == "fin":

            Mensaje_Agradecimiento()

    else:

        if respuesta == "r":

            pass

        elif respuesta == "fin":

            Mensaje_Agradecimiento()


def Error_Menu():

    print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█                    {error_texto}La opción elegida no esta dentro del menú                          {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
    respuesta = input(
        f"{marco+fondo}█        {texto}REINTENTAR <r>      FIN DEL PROGRAMA <fin>       Respuesta : {fin}      ").lower()

    while respuesta != "r" and respuesta != "fin":

        print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█              {error_texto}Error nuevamente, como respuesta se espera "r" o "fin"                   {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
        respuesta = input(
            f"{marco+fondo}█        {texto}REINTENTAR <r>      FIN DEL PROGRAMA <fin>       Respuesta : {fin}      ").lower()

        if respuesta == "r":

            break

        elif respuesta == "fin":

            Mensaje_Agradecimiento()

    else:

        if respuesta == "r":

            pass

        elif respuesta == "fin":

            Mensaje_Agradecimiento()


def Error_desplazamiento():

    while True:

        print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█           {error_texto}Respuesta inválida, como respuesta se espera 'r' o 'fin'                 {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
        respuesta = input(
            f"{marco+fondo}█        {texto}REINTENTAR <r>      FIN DEL PROGRAMA <fin>       Respuesta : {fin}      ").lower()

        if respuesta == "r":

            break

        elif respuesta == "fin":

            Mensaje_Agradecimiento()

        else:

            continue

        break


def Error_menu_atras():

    print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█          {error_texto}Respuesta inválida, como respuesta se espera 'volver' o 'fin'                {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
    respuesta = input(
        f"{marco+fondo}█        {texto}REINTENTAR <r>      FIN DEL PROGRAMA <fin>       Respuesta : {fin}      ").lower()

    while respuesta != "r" and respuesta != "fin":

        print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█              {error_texto}Error nuevamente, como respuesta se espera "r" o "fin"                   {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
        respuesta = input(
            f"{marco+fondo}█        {texto}REINTENTAR <r>      FIN DEL PROGRAMA <fin>       Respuesta : {fin}      ").lower()

        if respuesta == "r":

            break

        elif respuesta == "fin":

            Mensaje_Agradecimiento()

    else:

        if respuesta == "r":

            pass

        elif respuesta == "fin":

            Mensaje_Agradecimiento()


def Error_Campo():

    print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█           {error_texto}Formulario interrumpido por un error de formato en este campo.              {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
    respuesta = input(
        f"{marco+fondo}█        {texto}REINTENTAR <r>      FIN DEL PROGRAMA <fin>       Respuesta : {fin}      ").lower()

    while respuesta != "r" and respuesta != "fin":

        print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█              {error_texto}Error nuevamente, como respuesta se espera "r" o "fin"                   {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
        respuesta = input(
            f"{marco+fondo}█        {texto}REINTENTAR <r>      FIN DEL PROGRAMA <fin>       Respuesta : {fin}      ").lower()

        if respuesta == "r":

            break

        elif respuesta == "fin":

            Mensaje_Agradecimiento()

    else:

        if respuesta == "r":

            pass

        elif respuesta == "fin":

            Mensaje_Agradecimiento()


def Error_Menu_Desplazamiento_Formularios_Completos():

    print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█ {error_texto}Repuesta inválida, como respuesta se espera 'reset', 'exportar', 'guardar' o 'enviar' {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
    respuesta = input(
        f"{marco+fondo}█        {texto}REINTENTAR <r>      FIN DEL PROGRAMA <fin>       Respuesta : {fin}      ").lower()

    while respuesta != "r" and respuesta != "fin":

        print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█              {error_texto}Error nuevamente, como respuesta se espera "r" o "fin"                   {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
        respuesta = input(
            f"{marco+fondo}█        {texto}REINTENTAR <r>      FIN DEL PROGRAMA <fin>       Respuesta : {fin}      ").lower()

        if respuesta == "r":

            break

        elif respuesta == "fin":

            Mensaje_Agradecimiento()
    else:

        if respuesta == "r":

            pass

        elif respuesta == "fin":

            Mensaje_Agradecimiento()


def Error_Menu_Desplazamiento_Visualizacion():

    print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█      {error_texto}Respuesta inválida, como respuesta se espera 'volver', 'a', 'b' o 'c'            {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
    respuesta = input(
        f"{marco+fondo}█        {texto}REINTENTAR <r>      FIN DEL PROGRAMA <fin>       Respuesta : {fin}      ").lower()

    while respuesta != "r" and respuesta != "fin":

        print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█            {error_texto}Respuesta inválida, como respuesta se espera 'volver' o 'fin'              {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
        respuesta = input(
            f"{marco+fondo}█        {texto}REINTENTAR <r>      FIN DEL PROGRAMA <fin>       Respuesta : {fin}      ").lower()

        if respuesta == "r":

            break

        elif respuesta == "fin":

            Mensaje_Agradecimiento()

    else:

        if respuesta == "r":

            pass

        elif respuesta == "fin":

            Mensaje_Agradecimiento()


def Error_envio_mail():

    print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█                {error_texto}Error con el envio del mail, quiere volver a intentar?                 {fin+marco}█{fin}
{marco+fondo}█          {error_texto}Posible causas: Este mal escrito el mail o el destinatario no exista.        {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
    respuesta = input(
        f"{marco+fondo}█        {texto}REINTENTAR <r>      FIN DEL PROGRAMA <fin>       Respuesta : {fin}      ").lower()

    while respuesta != "r" and respuesta != "fin":

        print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█            {error_texto}Respuesta inválida, como respuesta se espera 'volver' o 'fin'              {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
        respuesta = input(
            f"{marco+fondo}█        {texto}REINTENTAR <r>      FIN DEL PROGRAMA <fin>       Respuesta : {fin}      ").lower()

        if respuesta == "r":

            break

        elif respuesta == "fin":

            Mensaje_Agradecimiento()

    else:

        if respuesta == "r":

            pass

        elif respuesta == "fin":

            Mensaje_Agradecimiento()
