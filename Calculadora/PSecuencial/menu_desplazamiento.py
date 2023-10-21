from colores import *


def Si_No():

    print(f"{marco+fondo}█                                                                                      █{fin}")
    respuesta = input(
        f"{marco+fondo}█    {texto}Si quiero <si>    No, no quiero <no>     Respuesta : {fin}      ").lower()

    return respuesta


def Local_atlas():

    print(f"{marco+fondo}█                                                                                      █{fin}")
    respuesta = input(
        f"{marco+fondo}█  {texto}Conexion local <local>     Conexion atlas <atlas>     Respuesta : {fin}     ").lower()

    return respuesta


def Menu_desplazamiento_historial():

    print(f"{marco+fondo}█                                                                                      █{fin}")
    respuesta = input(
        f"{marco+fondo}█  {texto}Limpiar historial <limpiar>     Volver al menú <volver>     Respuesta : {fin}     ").lower()

    return respuesta


def Menu_atras():

    print(f"{marco+fondo}█                                                                                      █{fin}")
    respuesta = input(
        f"{marco+fondo}█  {texto}Volver al menú <volver>        Fin del Programa <fin>    Respuesta : {fin}     ").lower()

    return respuesta
