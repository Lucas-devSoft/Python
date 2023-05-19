""" Importaciones de Módulos """

import re

""" Importaciones de Scripts """

from colores import *
from logica import *
from conexion import *
from errores import *

"""  Comienzo del programa """

while True:
    
    Limpieza_consola()    
    

    print(f"{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
    print(f"{marco}║{fondo}                                                                               {fin+marco}║{fin}")
    print(f"{marco}║{fondo}                   {texto}Bienvenido Usuario, ¿ Cuál es su nombre ?{fin+fondo}                   {fin+marco}║{fin}")
    print(f"{marco}║{fondo}                                                                               {fin+marco}║{fin}")
    print(f"{marco}╚═══════════════════════════════════════════════════════════════════════════════╝{fin}")
    Nombre = input("\n\t\t\t\t       ")

    Verificación = re.findall("[\W\d]+", Nombre)

    if not Verificación:
        
        while True:
            
            Limpieza_consola()

            print(f"{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
            print(f"{marco}║{fondo}                                                                               {fin+marco}║{fin}")
            print(f"{marco}║{fondo}                        {texto}Hola {Nombre.capitalize()} bienvenido a mi programa!{fin+fondo}                   {fin+marco}║{fin}")
            print(f"{marco}║{fondo}                                                                               {fin+marco}║{fin}")
            print(f"{marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
            print(f"{marco}║{fondo}                                                                               {fin+marco}║{fin}")
            print(f"{marco}║{fondo}      {texto}¿Quieres generar un historial de tus operaciones en la Base de datos?{fin+fondo}    {fin+marco}║{fin}")
            print(f"{marco}║{fondo}                                                                               {fin+marco}║{fin}")
            print(f"{marco}╠═══════════════════════════════════════╦═══════════════════════════════════════╣{fin}")
            print(f"{marco}║{fondo}                                       {fin+marco}║{fondo}                                       {fin+marco}║{fin}")
            print(f"{marco}║{fondo}             {texto}Sí, Quiero  < si >{fin+fondo}        {fin+marco}║{fondo}        {texto}< no >  No, no quiero{fin+fondo}          {fin+marco}║{fin}")
            print(f"{marco}║{fondo}                                       {fin+marco}║{fondo}                                       {fin+marco}║{fin}")
            print(f"{marco}╚═══════════════════════════════════════╩═══════════════════════════════════════╝{fin}")
            Respuesta_historial = input("\n\t\t\t\t       ").lower()

            if Respuesta_historial == "si":
                
                while True:
                    
                    Limpieza_consola()

                    print(f"{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
                    print(f"{marco}║{fondo}                                                                               {fin+marco}║{fin}")
                    print(f"{marco}║{fondo}               {texto}Bien {Nombre.capitalize()}, ahora elige que tipo de conexión deseas.{fin+fondo}            {fin+marco}║{fin}")
                    print(f"{marco}║{fondo}                                                                               {fin+marco}║{fin}")
                    print(f"{marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
                    print(f"{marco}║{fondo}                {fin+error_texto}Recomendado: Tener instalado MongoDB en su sistema.{fin+fondo}            {fin+marco}║{fin}")
                    print(f"{marco}╠═════════════════════════════════════════╦═════════════════════════════════════╣{fin}")
                    print(f"{marco}║{fondo}                                         {fin+marco}║{fondo}                                     {fin+marco}║{fin}")
                    print(f"{marco}║{fondo}            {texto}1 - De Forma Local{fin+fondo}           {fin+marco}║{fondo}         {texto}2 - Con mongo Atlas{fin+fondo}         {fin+marco}║{fin}")
                    print(f"{marco}║{fondo}                                         {fin+marco}║{fondo}                                     {fin+marco}║{fin}")
                    print(f"{marco}╚═════════════════════════════════════════╩═════════════════════════════════════╝{fin}")
                    Respuesta_tipo_conexion = input("\n\t\t\t\t          ")

                    if Respuesta_tipo_conexion == "1":
                        
                        Limpieza_consola()
                        
                        retorna_conexion = Conexión_Local(Nombre)  # Bien
                        break

                    elif Respuesta_tipo_conexion == "2":
                        
                        Limpieza_consola()
                        
                        retorna_conexion = Mongo_Atlas_Conexión(Nombre)
                        break

                    else:
                        
                        Limpieza_consola()
                        Error_Mensaje_de_Conexión()  # Bien

                break

            elif Respuesta_historial == "no":
                
                Respuesta_tipo_conexion = "no"
                retorna_conexion = "no"
                break  # Bien

            else:
                
                Limpieza_consola()
                Error_Mensaje_de_BD()  # Bien

    else:
        
        Limpieza_consola()
        Error_Mensaje_de_Nombre()  # Bien

        continue

    break

while True:
    
    Limpieza_consola()
    
    Banner(Respuesta_historial, retorna_conexion, Respuesta_tipo_conexion)
    print(f"{marco}║{fondo}                                                                               {fin+marco}║{fin}")
    print(f"{marco}║{fondo}                     {texto}Calculadora desarrollada con Python{fin+fondo}                       {fin+marco}║{fin}")
    print(f"{marco}║{fondo}                                                                               {fin+marco}║{fin}")
    print(f"{marco}╠══════════════════════════════════════════════════╦════════════════════════════╣{fin}")
    print(f"{marco}║{fondo}                    {texto}A ► Adición{fin+fondo}                   {fin+marco}║{fondo}            {texto}(+){fin+fondo}             {fin+marco}║{fin}")
    print(f"{marco}╠══════════════════════════════════════════════════╬════════════════════════════╣{fin}")
    print(f"{marco}║{fondo}                    {texto}B ► Sustracción{fin+fondo}               {fin+marco}║{fondo}            {texto}(-){fin+fondo}             {fin+marco}║{fin}")
    print(f"{marco}╠══════════════════════════════════════════════════╬════════════════════════════╣{fin}")
    print(f"{marco}║{fondo}                    {texto}C ► Multiplicación{fin+fondo}            {fin+marco}║{fondo}            {texto}(*){fin+fondo}             {fin+marco}║{fin}")
    print(f"{marco}╠══════════════════════════════════════════════════╬════════════════════════════╣{fin}")
    print(f"{marco}║{fondo}                    {texto}D ► División{fin+fondo}                  {fin+marco}║{fondo}            {texto}(/){fin+fondo}             {fin+marco}║{fin}")
    print(f"{marco}╠══════════════════════════════════════════════════╬════════════════════════════╣{fin}")
    print(f"{marco}║{fondo}                    {texto}E ► Potenciación{fin+fondo}              {fin+marco}║{fondo}           {texto}(b,e){fin+fondo}            {fin+marco}║{fin}")
    print(f"{marco}╠══════════════════════════════════════════════════╬════════════════════════════╣{fin}")
    print(f"{marco}║{fondo}                    {texto}F ► Radicación{fin+fondo}                {fin+marco}║{fondo}            {texto}(√){fin+fondo}             {fin+marco}║{fin}")
    print(f"{marco}╠══════════════════════════════════════════════════╩════════════════════════════╣{fin}")
    print(f"{marco}║{fondo}                    {texto}G ► Par o Impar{fin+fondo}                                            {fin+marco}║{fin}")
    print(f"{marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
    print(f"{marco}║{fondo}                    {texto}H ► El número es primo ?{fin+fondo}                                   {fin+marco}║{fin}")
    print(f"{marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
    print(f"{marco}║{fondo}                    {texto}I ► Rango de números primos{fin+fondo}                                {fin+marco}║{fin}")
    print(f"{marco}╚═══════════════════════════════════════════════════════════════════════════════╝{fin}\n")
    
    print(f"{marco}╔══════════════════════════════════════════════════╦════════════════════════════╗{fin}")
    opcion = input(f"{marco}║{fondo}         {texto}{Nombre.capitalize()}, Elige una opción del Menu{fin+fondo}         {fin+marco}║{fin}               ").upper()

    if opcion == "A":

        try:
            
            Limpieza_consola()
            
            Retorna_A = opción_A()

            if Respuesta_historial == "no":
                
                print(f"{marco}║{fondo}      {fin+error_texto}Recordatorio: Esta sin conexión, no se guardaran sus operaciones.{fin+fondo}        {fin+marco}║{fin}")
                print(f"{marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}")
        
            else:
                
                Numero1, Operador, Numero2, Resultado = Retorna_A[0:4]
                Ingreso_Datos(Respuesta_tipo_conexion, Nombre, Numero1, Operador, Numero2, Resultado)

        except:
            
            Mensaje_de_Error_Interno()
        
        if Respuesta_historial == "si":
            
            print(f"{marco}╠══════════════════╩══╦══════════╩══════════════╬═════════════╩═════════════════╣{fin}")
            print(f"{marco}║{fondo}  {texto}Retroceder  < r >{fin+fondo}  {fin+marco}║{fondo}  {texto}Base de datos  < bd >{fin+fondo}  {fin+marco}║{fondo}   {texto}fin del programa < fin >{fin+fondo}    {fin+marco}║{fin}")
            print(f"{marco}╚═════════════════════╩═════════════════════════╩═══════════════════════════════╝{fin}")
        
        else :
                    
            print(f"{marco}║{fondo}           {texto}Retroceder  < r >{fin+fondo}          {fin+marco}║{fondo}        {texto}Fin del Programa < fin >{fin+fondo}        {fin+marco}║{fin}")
            print(f"{marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}")

        Volver = input("\n\t\t\t\t      ").lower()
        
        if Volver == "fin":
            
            Mensaje_de_Agradecimiento()

        elif Volver == "r":
            
            continue
        
        elif Respuesta_historial == "si" and Volver == "bd":
            
            Limpieza_consola()
            Menu_BD()
        
        else: 
            
            Limpieza_consola()
            Mensaje_de_Error_Opciones()

    elif opcion == "B":
        
        Limpieza_consola()

        try:
            
            Retorna_B = opción_B()

            if Respuesta_historial == "no":
        
                print(f"{marco}║{fondo}      {fin+error_texto}Recordatorio: Esta sin conexión, no se guardaran sus operaciones.{fin+fondo}        {fin+marco}║{fin}")
                print(f"{marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}")

            else:
                
                Numero1, Operador, Numero2, Resultado = Retorna_B[0:4]
                Ingreso_Datos(Respuesta_tipo_conexion, Nombre, Numero1, Operador, Numero2, Resultado)

        except:
            
            Mensaje_de_Error_Interno()

        if Respuesta_historial == "si":
            
            print(f"{marco}╠══════════════════╩══╦══════════╩══════════════╬═════════════╩═════════════════╣{fin}")
            print(f"{marco}║{fondo}  {texto}Retroceder  < r >{fin+fondo}  {fin+marco}║{fondo}  {texto}Base de datos  < bd >{fin+fondo}  {fin+marco}║{fondo}   {texto}fin del programa < fin >{fin+fondo}    {fin+marco}║{fin}")
            print(f"{marco}╚═════════════════════╩═════════════════════════╩═══════════════════════════════╝{fin}")
        
        else :
                    
            print(f"{marco}║{fondo}           {texto}Retroceder  < r >{fin+fondo}          {fin+marco}║{fondo}        {texto}Fin del Programa < fin >{fin+fondo}        {fin+marco}║{fin}")
            print(f"{marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}")

        Volver = input("\n\t\t\t\t       ").lower()
        
        if Volver == "fin":
            
            Mensaje_de_Agradecimiento()

        elif Volver == "r":
            
            continue
        
        elif Respuesta_historial == "si" and Volver == "bd":
            
            Limpieza_consola()
            Menu_BD()
        
        else: 
            
            Limpieza_consola()
            Mensaje_de_Error_Opciones()

    elif opcion == "C":
        
        Limpieza_consola()

        try:
            
            Retorna_C = opción_C()

            if Respuesta_historial == "no":
                
                print(f"{marco}║{fondo}      {fin+error_texto}Recordatorio: Esta sin conexión, no se guardaran sus operaciones.{fin+fondo}        {fin+marco}║{fin}")
                print(f"{marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}")
        
            else:
                
                Numero1, Operador, Numero2, Resultado = Retorna_C[0:4]
                Ingreso_Datos(Respuesta_tipo_conexion, Nombre, Numero1, Operador, Numero2, Resultado)

        except:
            
            Mensaje_de_Error_Interno() 
        
        if Respuesta_historial == "si":
            
            print(f"{marco}╠══════════════════╩══╦══════════╩══════════════╬═════════════╩═════════════════╣{fin}")
            print(f"{marco}║{fondo}  {texto}Retroceder  < r >{fin+fondo}  {fin+marco}║{fondo}  {texto}Base de datos  < bd >{fin+fondo}  {fin+marco}║{fondo}   {texto}fin del programa < fin >{fin+fondo}    {fin+marco}║{fin}")
            print(f"{marco}╚═════════════════════╩═════════════════════════╩═══════════════════════════════╝{fin}")
        
        else :
                    
            print(f"{marco}║{fondo}           {texto}Retroceder  < r >{fin+fondo}          {fin+marco}║{fondo}        {texto}Fin del Programa < fin >{fin+fondo}        {fin+marco}║{fin}")
            print(f"{marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}")

        Volver = input("\n\t\t\t\t       ").lower()
        
        if Volver == "fin":
            
            Mensaje_de_Agradecimiento()

        elif Volver == "r":
            
            continue
        
        elif Respuesta_historial == "si" and Volver == "bd":
            
            Limpieza_consola()
            Menu_BD()
        
        else: 
            
            Limpieza_consola()
            Mensaje_de_Error_Opciones()

    elif opcion == "D":
        
        Limpieza_consola()

        try:
            
            Retorna_D = opción_D()

            if Respuesta_historial == "no":
                
                print(f"{marco}║{fondo}      {fin+error_texto}Recordatorio: Esta sin conexión, no se guardaran sus operaciones.{fin+fondo}        {fin+marco}║{fin}")
                print(f"{marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}")
        
            else:
                
                Numero1, Operador, Numero2, Resultado = Retorna_D[0:4]
                Ingreso_Datos(Respuesta_tipo_conexion, Nombre, Numero1, Operador, Numero2, Resultado)

        except:
            
            Mensaje_de_Error_Interno()

        if Respuesta_historial == "si":
            
            print(f"{marco}╠══════════════════╩══╦══════════╩══════════════╬═════════════╩═════════════════╣{fin}")
            print(f"{marco}║{fondo}  {texto}Retroceder  < r >{fin+fondo}  {fin+marco}║{fondo}  {texto}Base de datos  < bd >{fin+fondo}  {fin+marco}║{fondo}   {texto}fin del programa < fin >{fin+fondo}    {fin+marco}║{fin}")
            print(f"{marco}╚═════════════════════╩═════════════════════════╩═══════════════════════════════╝{fin}")
        
        else :
                    
            print(f"{marco}║{fondo}           {texto}Retroceder  < r >{fin+fondo}          {fin+marco}║{fondo}        {texto}Fin del Programa < fin >{fin+fondo}        {fin+marco}║{fin}")
            print(f"{marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}")

        Volver = input("\n\t\t\t\t       ").lower()
        
        if Volver == "fin":
            
            Mensaje_de_Agradecimiento()

        elif Volver == "r":
            
            continue
        
        elif Respuesta_historial == "si" and Volver == "bd":
            
            Limpieza_consola()
            Menu_BD()
        
        else: 
            
            Limpieza_consola()
            Mensaje_de_Error_Opciones()

    elif opcion == "E":
        
        Limpieza_consola()

        try:
            
            Retorna_E = opción_E()

            if Respuesta_historial == "no":
                
                print(f"{marco}║{fondo}      {fin+error_texto}Recordatorio: Esta sin conexión, no se guardaran sus operaciones.{fin+fondo}        {fin+marco}║{fin}")
                print(f"{marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}")
        
            else:
                
                Numero1, Operador, Numero2, Resultado = Retorna_E[0:4]
                Ingreso_Datos(Respuesta_tipo_conexion, Nombre, Numero1, Operador, Numero2, Resultado)

        except:
            
            Mensaje_de_Error_Interno()

        if Respuesta_historial == "si":
            
            print(f"{marco}╠══════════════════╩══╦══════════╩══════════════╬═════════════╩═════════════════╣{fin}")
            print(f"{marco}║{fondo}  {texto}Retroceder  < r >{fin+fondo}  {fin+marco}║{fondo}  {texto}Base de datos  < bd >{fin+fondo}  {fin+marco}║{fondo}   {texto}fin del programa < fin >{fin+fondo}    {fin+marco}║{fin}")
            print(f"{marco}╚═════════════════════╩═════════════════════════╩═══════════════════════════════╝{fin}")
        
        else :
                    
            print(f"{marco}║{fondo}           {texto}Retroceder  < r >{fin+fondo}          {fin+marco}║{fondo}        {texto}Fin del Programa < fin >{fin+fondo}        {fin+marco}║{fin}")
            print(f"{marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}")

        Volver = input("\n\t\t\t\t       ").lower()
        
        if Volver == "fin":
            
            Mensaje_de_Agradecimiento()

        elif Volver == "r":
            
            continue
        
        elif Respuesta_historial == "si" and Volver == "bd":
            
            Limpieza_consola()
            Menu_BD()
        
        else: 
            
            Limpieza_consola()
            Mensaje_de_Error_Opciones()

    elif opcion == "F":
        
        Limpieza_consola()

        try:
            Retorna_F = opción_F()

            if Respuesta_historial == "no":
                
                print(f"{marco}║{fondo}      {fin+error_texto}Recordatorio: Esta sin conexión, no se guardaran sus operaciones.{fin+fondo}        {fin+marco}║{fin}")
                print(f"{marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}")
        
            else:
                
                Numero1, Operador, Numero2, Resultado = Retorna_F[0:4]
                Ingreso_Datos(Respuesta_tipo_conexion, Nombre, Numero1, Operador, Numero2, Resultado)

        except:
            
            Mensaje_de_Error_Interno()

        if Respuesta_historial == "si":
            
            print(f"{marco}╠══════════════════╩══╦══════════╩══════════════╬═════════════╩═════════════════╣{fin}")
            print(f"{marco}║{fondo}  {texto}Retroceder  < r >{fin+fondo}  {fin+marco}║{fondo}  {texto}Base de datos  < bd >{fin+fondo}  {fin+marco}║{fondo}   {texto}fin del programa < fin >{fin+fondo}    {fin+marco}║{fin}")
            print(f"{marco}╚═════════════════════╩═════════════════════════╩═══════════════════════════════╝{fin}")
        
        else :
                    
            print(f"{marco}║{fondo}           {texto}Retroceder  < r >{fin+fondo}          {fin+marco}║{fondo}        {texto}Fin del Programa < fin >{fin+fondo}        {fin+marco}║{fin}")
            print(f"{marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}")

        Volver = input("\n\t\t\t\t       ").lower()
        
        if Volver == "fin":
            
            Mensaje_de_Agradecimiento()

        elif Volver == "r":
            
            continue
        
        elif Respuesta_historial == "si" and Volver == "bd":
            
            Limpieza_consola()
            Menu_BD()
        
        else: 
            
            Limpieza_consola()
            Mensaje_de_Error_Opciones()

    elif opcion == "G":
        
        Limpieza_consola()

        try:
            
            Retorna_G = opción_G()

            if Respuesta_historial == "no":
                
                print(f"{marco}║{fondo}      {fin+error_texto}Recordatorio: Esta sin conexión, no se guardaran sus operaciones.{fin+fondo}        {fin+marco}║{fin}")
                print(f"{marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}")
        
            else:
                
                Numero1, Operador, Conclusión = Retorna_G[0:3]
                Insert_G_H(Nombre, Numero1, Operador, Conclusión)

        except:
            
            Mensaje_de_Error_Interno()
        
        if Respuesta_historial == "si":
            
            print(f"{marco}╠══════════════════╩══╦══════════╩══════════════╬═════════════╩═════════════════╣{fin}")
            print(f"{marco}║{fondo}  {texto}Retroceder  < r >{fin+fondo}  {fin+marco}║{fondo}  {texto}Base de datos  < bd >{fin+fondo}  {fin+marco}║{fondo}   {texto}fin del programa < fin >{fin+fondo}    {fin+marco}║{fin}")
            print(f"{marco}╚═════════════════════╩═════════════════════════╩═══════════════════════════════╝{fin}")
        
        else :
                    
            print(f"{marco}║{fondo}           {texto}Retroceder  < r >{fin+fondo}          {fin+marco}║{fondo}        {texto}Fin del Programa < fin >{fin+fondo}        {fin+marco}║{fin}")
            print(f"{marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}")

        Volver = input("\n\t\t\t\t       ").lower()
        
        if Volver == "fin":
            
            Mensaje_de_Agradecimiento()

        elif Volver == "r":
            
            continue
        
        elif Respuesta_historial == "si" and Volver == "bd":
            
            Limpieza_consola()
            Menu_BD()
        
        else: 
            
            Limpieza_consola()
            Mensaje_de_Error_Opciones()

    elif opcion == "H":
        
        Limpieza_consola()

        try:
            
            Retorna_H = opción_H()

            if Respuesta_historial == "no":
                
                print(f"{marco}║{fondo}      {fin+error_texto}Recordatorio: Esta sin conexión, no se guardaran sus operaciones.{fin+fondo}        {fin+marco}║{fin}")
                print(f"{marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}")
        
            else:
                
                Numero, Operador, Conclusión = Retorna_H[0:3]
                Insert_G_H(Nombre, Numero, Operador, Conclusión)

        except:
            
            Mensaje_de_Error_Interno()

        if Respuesta_historial == "si":
            
            print(f"{marco}╠══════════════════╩══╦══════════╩══════════════╬═════════════╩═════════════════╣{fin}")
            print(f"{marco}║{fondo}  {texto}Retroceder  < r >{fin+fondo}  {fin+marco}║{fondo}  {texto}Base de datos  < bd >{fin+fondo}  {fin+marco}║{fondo}   {texto}fin del programa < fin >{fin+fondo}    {fin+marco}║{fin}")
            print(f"{marco}╚═════════════════════╩═════════════════════════╩═══════════════════════════════╝{fin}")
        
        else :
                    
            print(f"{marco}║{fondo}           {texto}Retroceder  < r >{fin+fondo}          {fin+marco}║{fondo}        {texto}Fin del Programa < fin >{fin+fondo}        {fin+marco}║{fin}")
            print(f"{marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}")

        Volver = input("\n\t\t\t\t       ").lower()
        
        if Volver == "fin":
            
            Mensaje_de_Agradecimiento()

        elif Volver == "r":
            
            continue
        
        elif Respuesta_historial == "si" and Volver == "bd":
            
            Limpieza_consola()
            Menu_BD()
        
        else: 
            
            Limpieza_consola()
            Mensaje_de_Error_Opciones()

    elif opcion == "I":
        
        Limpieza_consola()

        try:
            
            opción_I()

        except:
            
            Mensaje_de_Error_Interno()

        print(f"{marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}")
        print(f"{marco}║{fondo}     {texto}Volver al Menu  < volver >{fin+fondo}       {fin+marco}║{fondo}     {texto}< salir >  Salir del programa{fin+fondo}      {fin+marco}║{fin}")
        print(f"{marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}")
        Volver = input("\n\t\t\t\t\t").lower()

        if Volver == "salir":
            
            Mensaje_de_Agradecimiento()

        elif Volver == "volver":
            
            continue

    else:
        
        Limpieza_consola()
        Error_Mensaje_de_Menu()  # Bien
