import time

from colores import *
from logica import Cartel


def Error_Mensaje_de_Nombre():
    
    print(f"""
{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}║{fondo}          {fin+error_texto}Se detecto el campo vacío o con un formato de nombre inválido.{fin}{fondo}       {fin+marco}║{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}
{marco}║{fondo}     {texto}volver a intentar <volver>{fin+fondo}       {fin+marco}║{fondo}        {texto}fin del programa <fin>{fin+fondo}          {fin+marco}║{fin}
{marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}
    """)
    opción = input("\t\t\t\t      ").lower()

    while opción != "volver" and opción != "fin":

        print(f"""
{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}║{fondo}      {fin+error_texto}Respuesta inválida se espera < volver > o < salir > como respuesta.{fin}{fondo}      {fin+marco}║{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}
{marco}║{fondo}     {texto}volver a intentar <volver>{fin+fondo}       {fin+marco}║{fondo}        {texto}fin del programa <fin>{fin+fondo}          {fin+marco}║{fin}
{marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}
        """)
        opción = input("\t\t\t\t      ").lower()

    else:
        
        if opción == "volver":
            
            pass

        elif opción == "fin":
            
            Mensaje_de_Agradecimiento()


def Error_Mensaje_de_BD():
    
    print(f"""
{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}║{fondo}          {fin+error_texto}Respuesta invalida se espera < si > o < no > como respuesta.{fin+fondo}         {fin+marco}║{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}
{marco}║{fondo}     {texto}volver a intentar <volver>{fin+fondo}       {fin+marco}║{fondo}        {texto}fin del programa <fin>{fin+fondo}          {fin+marco}║{fin}
{marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}
    """)
    opción = input("\t\t\t\t      ").lower()

    while opción != "volver" and opción != "fin":

        print(f"""
{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}║{fondo}      {fin+error_texto}Respuesta inválida se espera < volver > o < salir > como respuesta.{fin}{fondo}      {fin+marco}║{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}
{marco}║{fondo}     {texto}volver a intentar <volver>{fin+fondo}       {fin+marco}║{fondo}        {texto}fin del programa <fin>{fin+fondo}          {fin+marco}║{fin}
{marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}
        """)
        opción = input("\t\t\t\t      ").lower()

    else:
        
        if opción == "volver":
            
            pass

        elif opción == "fin":
            
            Mensaje_de_Agradecimiento()


def Error_Mensaje_de_Conexión():
    
    print(f"""
{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}║{fondo}          {fin+error_texto}Respuesta inválida se espera < 1 > o < 2 > como respuesta.{fin}{fondo}           {fin+marco}║{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}
{marco}║{fondo}     {texto}volver a intentar <volver>{fin+fondo}       {fin+marco}║{fondo}        {texto}fin del programa <fin>{fin+fondo}          {fin+marco}║{fin}
{marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}
    """)
    opción = input("\t\t\t\t      ").lower()

    while opción != "volver" and opción != "fin":

        print(f"""
{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}║{fondo}       {fin+error_texto}Respuesta inválida se espera < volver > o < salir > como respuesta.{fin}{fondo}     {fin+marco}║{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}
{marco}║{fondo}     {texto}volver a intentar <volver>{fin+fondo}       {fin+marco}║{fondo}        {texto}fin del programa <fin>{fin+fondo}          {fin+marco}║{fin}
{marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}
        """)
        opción = input("\t\t\t\t      ").lower()

    else:
        
        if opción == "volver":
            
            pass

        elif opción == "fin":
            
            Mensaje_de_Agradecimiento()


def Error_Mensaje_pre_Conexión():
    
    print(f"""
{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}║{fondo}          {fin+error_texto}Respuesta invalida se espera < si > o < no > como respuesta.{fin+fondo}         {fin+marco}║{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}
{marco}║{fondo}     {texto}volver a intentar <volver>{fin+fondo}       {fin+marco}║{fondo}        {texto}fin del programa <fin>{fin+fondo}          {fin+marco}║{fin}
{marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}
    """)
    opción = input("\t\t\t\t      ").lower()

    while opción != "volver" and opción != "fin":

        print(f"""
{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}║{fondo}      {fin+error_texto}Respuesta inválida se espera < volver > o < salir > como respuesta.{fin}{fondo}      {fin+marco}║{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}
{marco}║{fondo}     {texto}volver a intentar <volver>{fin+fondo}       {fin+marco}║{fondo}        {texto}fin del programa <fin>{fin+fondo}          {fin+marco}║{fin}
{marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}
        """)
        opción = input("\t\t\t\t      ").lower()

    else:
        
        if opción == "volver":
            
            pass

        elif opción == "fin":
            
            Mensaje_de_Agradecimiento()


def Error_Mensaje_de_Menu():
    
    print(f"""
{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}║{fondo}               {fin+error_texto}La opción que elegiste no esta dentro del Menu{fin+fondo}                  {fin+marco}║{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}
{marco}║{fondo}     {texto}volver a intentar <volver>{fin+fondo}       {fin+marco}║{fondo}        {texto}fin del programa <fin>{fin+fondo}          {fin+marco}║{fin}
{marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}
    """)
    opción = input("\t\t\t\t      ").lower()

    while opción != "volver" and opción != "fin":
        
        print()

        print(f"""{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}║{fondo}      {fin+error_texto}Respuesta inválida se espera < volver > o < salir > como respuesta.{fin+fondo}      {fin+marco}║{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}
{marco}║{fondo}     {texto}volver a intentar <volver>{fin+fondo}       {fin+marco}║{fondo}        {texto}fin del programa <fin>{fin+fondo}          {fin+marco}║{fin}
{marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}
        """)
        opción = input("\t\t\t\t      ").lower()

    else:
        
        if opción == "volver":
            
            pass

        elif opción == "fin":
            
            Mensaje_de_Agradecimiento()


def Mensaje_de_Agradecimiento():

    print(f"""
{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}║{fondo}                    {texto}Muchas gracias por probar mi programa.{fin+fondo}                     {fin+marco}║{fin}
{marco}║{fondo}               {texto}El programa se cerrará automáticamente en 5 segundos.{fin+fondo}           {fin+marco}║{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}╚═══════════════════════════════════════════════════════════════════════════════╝{fin}
    """)

    time.sleep(5)

    exit()


def Mensaje_de_Error_Interno():
    
    print(f"""{marco}╠══════════════════════════════════════════════════════════╩════════════════════╣{fin}
{marco}║{fondo}          {fin+error_texto}Error Interno! el retorno no esta devolviendo un valor{fin+fondo}               {fin+marco}║{fin}
{marco}║{fondo}        {fin+error_texto}Posibles causas: Inserto letras como valor o un número erróneo.{fin+fondo}        {fin+marco}║{fin}""")
    
    return True


def Mensaje_de_Error_Opciones():
    
    print(f"""
{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}║{fondo}               {fin+error_texto}La opción que elegiste no esta dentro del menú{fin+fondo}                  {fin+marco}║{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}
{marco}║{fondo}     {texto}volver a intentar <volver>{fin+fondo}       {fin+marco}║{fondo}        {texto}fin del programa <fin>{fin+fondo}          {fin+marco}║{fin}
{marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}
    """)
    opción = input("\t\t\t\t      ").lower()

    while opción != "volver" and opción != "fin":

        print(f"""
{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}║{fondo}      {fin+error_texto}Respuesta inválida se espera < volver > o < salir > como respuesta.{fin+fondo}      {fin+marco}║{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}
{marco}║{fondo}     {texto}volver a intentar <volver>{fin+fondo}       {fin+marco}║{fondo}        {texto}fin del programa <fin>{fin+fondo}          {fin+marco}║{fin}
{marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}
        """)
        opción = input("\t\t\t\t      ").lower()

    else:
        
        if opción == "volver":
            
            pass

        elif opción == "fin":
            
            Mensaje_de_Agradecimiento()