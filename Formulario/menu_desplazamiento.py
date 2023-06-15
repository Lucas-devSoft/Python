from colores import *

"""
    Menu de desplazamiento del main

"""


def Menu_Si_No():

    print(f"{marco+fondo}█                                                                                       █{fin}")
    pregunta = input(
        f"{marco+fondo}█        {texto}SI, QUIERO <si>        NO, NO QUIERO <no>        Respuesta : {fin}      ").lower()

    return pregunta


def Menu_Local_Atlas():

    print(f"{marco+fondo}█                                                                                       █{fin}")
    pregunta_bd = input(
        f"{marco+fondo}█     {texto}MongoDB Local <local>     MongoDB Atlas <atlas>     Respuesta : {fin}       ").lower()

    return pregunta_bd


"""
    Menu de desplazamiento de conexion

"""


def Menu_Si_No_Conexion():

    print(f"{marco+fondo}█                                                                                       █{fin}")
    pregunta = input(
        f"{marco+fondo}█        {texto}SI, QUIERO <si>        NO, NO QUIERO <no>        Respuesta : {fin}      ").lower()

    return pregunta


def Menu_atras():

    print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
    volver = input(
        f"{marco+fondo}█    {texto}VOLVER AL MENÚ <volver>    FIN DEL PROGRAMA <fin>    Respuesta : {fin}      ").lower()

    return volver


def Menu_de_desplazamiento_con_conexion():

    print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█         {texto}RESETEAR        GUARDAR       EXPORTAR       ENVIAR           RESPUESTA       {fin+marco}█{fin}""")
    resultado = input(
        f"{marco+fondo}█          {texto}<reset>       <guardar>     <exportar>     <enviar>   : {fin}     ").lower()

    return resultado


def Menu_de_desplazamiento_visualizacion():

    print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█  {texto}RETROCEDER    VISUALIZAR DATOS   VISUALIZAR DATOS   VISUALIZAR DATOS   RESPUESTA     {fin+marco}█{fin}""")
    ver = input(
        f"{marco+fondo}█   {texto}<volver>           <a>                <b>                 <c>       : {fin}     ").lower()

    return ver


def Menu_de_desplazamiento_sin_conexion():

    print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
    resultado = input(
        f"{marco+fondo}█ {texto}RESETEAR <reset>  EXPORTAR <exportar>  ENVIAR <enviar>  respuesta : {fin}     ").lower()

    return resultado


def Menu_de_reconfirmacion():

    print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
    pregunta = input(
        f"{marco+fondo}█   {texto}Estoy seguro <si>      Me equivoque de mail <no>        Respuesta : {fin}      ").lower()

    return pregunta
