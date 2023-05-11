""" Importaciones de Modulos """

from  Colores import *
from   Logica import *
from Conexion import *

import re

"""  Comienzo del programa """

while True:

    Limpieza_consola()

    print                            (f"                   {marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
    print                            (f"                   {marco}║{fondo}                                                                               {fin}║{fin}")
    print                            (f"                   {marco}║{fondo}                   {texto}Bienvenido Usuario, ¿ Cuál es su nombre ?{fin+fondo}                   {fin+marco}║{fin}")
    print                            (f"                   {marco}║{fondo}                                                                               {fin}║{fin}")
    print                            (f"                   {marco}╚═══════════════════════════════════════════════════════════════════════════════╝{fin}")
    Nombre = input                   ("\n\t\t\t\t\t\t\t")

    Verificación = re.findall("[\W\d]+",Nombre)
        
    if not Verificación:
        
        while True:
            
            Limpieza_consola()
            
            print                    (f"                   {marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
            print                    (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
            print                    (f"                   {marco}║{fondo}                        {texto}Hola {Nombre.capitalize()} bienvenido a mi programa!{fin+fondo}                   {fin+marco}║{fin}")
            print                    (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
            print                    (f"                   {marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
            print                    (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
            print                    (f"                   {marco}║{fondo}      {texto}¿Quieres generar un historial de tus operaciones en la Base de datos?{fin+fondo}    {fin+marco}║{fin}")
            print                    (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
            print                    (f"                   {marco}╠═══════════════════════════════════════╦═══════════════════════════════════════╣{fin}")
            print                    (f"                   {marco}║{fondo}                                       {fin+marco}║{fondo}                                       {fin+marco}║{fin}") 
            print                    (f"                   {marco}║{fondo}             {texto}Sí, Quiero  < si >{fin+fondo}        {fin+marco}║{fondo}        {texto}< no >  No, no quiero{fin+fondo}          {fin+marco}║{fin}")
            print                    (f"                   {marco}║{fondo}                                       {fin+marco}║{fondo}                                       {fin+marco}║{fin}")           
            print                    (f"                   {marco}╚═══════════════════════════════════════╩═══════════════════════════════════════╝{fin}")
            Respuesta = input        ("\n\t\t\t\t\t\t\t   ").lower()
            
            if Respuesta == "si":
                
                while True:
                    
                    Limpieza_consola()
                    
                    print            (f"                   {marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
                    print            (f"                   {marco}║{fondo}                                                                               {fin}║{fin}")
                    print            (f"                   {marco}║{fondo}               {texto}Bien {Nombre.capitalize()}, ahora elige que tipo de conexión deseas.{fin+fondo}            {fin+marco}║{fin}")
                    print            (f"                   {marco}║{fondo}                                                                               {fin}║{fin}")
                    print            (f"                   {marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
                    print            (f"                   {marco}║{fondo}                                                                               {fin}║{fin}")
                    print            (f"                   {marco}║{fondo}                {fin+error_texto}Recomendado: Tener instalado MongoDB en su sistema.{fin+fondo}            {fin+marco}║{fin}")
                    print            (f"                   {marco}║{fondo}                                                                               {fin}║{fin}")
                    print            (f"                   {marco}╠═════════════════════════════════════════╦═════════════════════════════════════╣{fin}")
                    print            (f"                   {marco}║{fondo}                                         {fin+marco}║{fondo}                                     {fin}║{fin}")
                    print            (f"                   {marco}║{fondo}            {texto}1 - De Forma Local{fin+fondo}           {fin+marco}║{fondo}         {texto}2 - Con mongo Atlas{fin+fondo}         {fin+marco}║{fin}")
                    print            (f"                   {marco}║{fondo}                                         {fin+marco}║{fondo}                                     {fin}║{fin}")
                    print            (f"                   {marco}╚═════════════════════════════════════════╩═════════════════════════════════════╝{fin}")
                    
                    Respuesta = input    ("\n\t\t\t\t\t\t\t   ")
                    
                    if Respuesta == "1":

                        retorna_respuesta = Conexion_Local(Nombre)    # Bien
                        
                        break
                    
                    elif Respuesta == "2":
                        
                        #Mongo_Atlas_Connection() 
                        pass 

                    else :
                        
                        Limpieza_consola()
                      
                        Error_Mensaje_de_Conexion()   #Bien
                
                break
                
            elif Respuesta == "no":
                
                retorna_respuesta = "no"
                
                break                          #Bien
        
            else:
                
                Limpieza_consola()
                
                Error_Mensaje_de_BD()        #Bien
                          
    else:
        
        Limpieza_consola()
        
        Error_Mensaje_de_Nombre()      #Bien

        continue
    
    break
          
while True:
    
    Limpieza_consola()
    
    Banner_de_Conexion(retorna_respuesta) 
    print                            (f"                   {marco}║{fondo}                     {texto}Calculadora desarrollada con Python{fin+fondo}                       {fin+marco}║{fin}") 
    print                            (f"                   {marco}╠══════════════════════════════════════════════════╦════════════════════════════╣{fin}")
    print                            (f"                   {marco}║{fondo}                                                  {fin+marco}║{fondo}                            {fin+marco}║{fin}")  
    print                            (f"                   {marco}║{fondo}                    {texto}A ► Adición{fin+fondo}                   {fin+marco}║{fondo}            {texto}(+){fin+fondo}             {fin+marco}║{fin}")
    print                            (f"                   {marco}║{fondo}                                                  {fin+marco}║{fondo}                            {fin+marco}║{fin}")   
    print                            (f"                   {marco}╠══════════════════════════════════════════════════╬════════════════════════════╣{fin}")
    print                            (f"                   {marco}║{fondo}                                                  {fin+marco}║{fondo}                            {fin+marco}║{fin}")   
    print                            (f"                   {marco}║{fondo}                    {texto}B ► Sustracción{fin+fondo}               {fin+marco}║{fondo}            {texto}(-){fin+fondo}             {fin+marco}║{fin}")
    print                            (f"                   {marco}║{fondo}                                                  {fin+marco}║{fondo}                            {fin+marco}║{fin}")   
    print                            (f"                   {marco}╠══════════════════════════════════════════════════╬════════════════════════════╣{fin}")
    print                            (f"                   {marco}║{fondo}                                                  {fin+marco}║{fondo}                            {fin+marco}║{fin}")   
    print                            (f"                   {marco}║{fondo}                    {texto}C ► Multiplicación{fin+fondo}            {fin+marco}║{fondo}            {texto}(*){fin+fondo}             {fin+marco}║{fin}")
    print                            (f"                   {marco}║{fondo}                                                  {fin+marco}║{fondo}                            {fin+marco}║{fin}")   
    print                            (f"                   {marco}╠══════════════════════════════════════════════════╬════════════════════════════╣{fin}")
    print                            (f"                   {marco}║{fondo}                                                  {fin+marco}║{fondo}                            {fin+marco}║{fin}")   
    print                            (f"                   {marco}║{fondo}                    {texto}D ► División{fin+fondo}                  {fin+marco}║{fondo}            {texto}(/){fin+fondo}             {fin+marco}║{fin}")
    print                            (f"                   {marco}║{fondo}                                                  {fin+marco}║{fondo}                            {fin+marco}║{fin}")   
    print                            (f"                   {marco}╠══════════════════════════════════════════════════╬════════════════════════════╣{fin}")
    print                            (f"                   {marco}║{fondo}                                                  {fin+marco}║{fondo}                            {fin+marco}║{fin}")   
    print                            (f"                   {marco}║{fondo}                    {texto}E ► Exponenciación{fin+fondo}            {fin+marco}║{fondo}           {texto}(b,e){fin+fondo}            {fin+marco}║{fin}")
    print                            (f"                   {marco}║{fondo}                                                  {fin+marco}║{fondo}                            {fin+marco}║{fin}")   
    print                            (f"                   {marco}╠══════════════════════════════════════════════════╬════════════════════════════╣{fin}")
    print                            (f"                   {marco}║{fondo}                                                  {fin+marco}║{fondo}                            {fin+marco}║{fin}")   
    print                            (f"                   {marco}║{fondo}                    {texto}F ► Radicación{fin+fondo}                {fin+marco}║{fondo}            {texto}(√){fin+fondo}             {fin+marco}║{fin}")
    print                            (f"                   {marco}║{fondo}                                                  {fin+marco}║{fondo}                            {fin+marco}║{fin}")   
    print                            (f"                   {marco}╠══════════════════════════════════════════════════╩════════════════════════════╣{fin}")
    print                            (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")   
    print                            (f"                   {marco}║{fondo}                    {texto}G ► Par o Impar{fin+fondo}                                            {fin+marco}║{fin}")
    print                            (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")   
    print                            (f"                   {marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
    print                            (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")   
    print                            (f"                   {marco}║{fondo}                    {texto}H ► El número es primo ?{fin+fondo}                                   {fin+marco}║{fin}")
    print                            (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")   
    print                            (f"                   {marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
    print                            (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")   
    print                            (f"                   {marco}║{fondo}                    {texto}I ► Rango de números primos{fin+fondo}                                {fin+marco}║{fin}")
    print                            (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")   
    print                            (f"                   {marco}╚═══════════════════════════════════════════════════════════════════════════════╝{fin}\n")
    print                            (f"                   {marco}╔══════════════════════════════════════════════════╦════════════════════════════╗{fin}")
    option = input                   (f"                   {marco}║{fondo}         {texto}{Nombre.capitalize()}, Elige una opción del Menu{fin+fondo}         {fin+marco}║{fin}               ").upper()  
    
    if option == "A":            
        
        Limpieza_consola()         
        
        try:
            
            Retorna_A = option_A()
            
            if Respuesta == "no" :
            
                print                (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}") 
                print                (f"                   {marco}║{fondo}     {fin+error_texto}Recordatorio: Sin conexión por lo que no se guardará sus operaciones.{fin+fondo}     {fin+marco}║{fin}")
                print                (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
            
            else :
                
                Numero1, Operador, Numero2, Resultado = Retorna_A[0:4]
                 
                Insert_A_F(Nombre, Numero1, Operador, Numero2, Resultado)                           
            
        except:
            
            print                    (f"                   {marco}╠══════════════════════════════════════════════════════════╩════════════════════╣{fin}")
            print                    (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}") 
            print                    (f"                   {marco}║{fondo}         {fin+error_texto}Error Interno! el retorno no esta devuelviendo un valor{fin+fondo}               {fin+marco}║{fin}")
            print                    (f"                   {marco}║{fondo}        {fin+error_texto}Posibles causas: Inserto letras como valor o un número erroneo.{fin+fondo}        {fin+marco}║{fin}")
            print                    (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
                    
        print                        (f"                   {marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}") 
        print                        (f"                   {marco}║{fondo}     {texto}Volver al Menu  < volver >{fin+fondo}       {fin+marco}║{fondo}     {texto}< salir >  Salir del programa{fin+fondo}      {fin+marco}║{fin}")
        print                        (f"                   {marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}") 
        Volver = input               ("\n\t\t\t\t\t\t\t   ").lower()
        
        if Volver == "salir":
            
            Mensaje_de_Agradecimiento()
            
        elif Volver == "volver":
            
            continue

    elif option == "B":
        
        Limpieza_consola()
        
        try:
            
            Retorna_B = option_B()
            
            if Respuesta == "no" :
            
                print                (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}") 
                print                (f"                   {marco}║{fondo}     {fin+error_texto}Recordatorio: Sin conexión por lo que no se guardará sus operaciones.{fin+fondo}     {fin+marco}║{fin}")
                print                (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
            
            else :
                
        
                Numero1, Operador, Numero2, Resultado = Retorna_B[0:4]
            
                Insert_A_F(Nombre, Numero1, Operador, Numero2, Resultado)
        
        except:
            
            print                    (f"                   {marco}╠══════════════════════════════════════════════════════════╩════════════════════╣{fin}")
            print                    (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}") 
            print                    (f"                   {marco}║{fondo}         {fin+error_texto}Error Interno! el retorno no esta devuelviendo un valor{fin+fondo}               {fin+marco}║{fin}")
            print                    (f"                   {marco}║{fondo}        {fin+error_texto}Posibles causas: Inserto letras como valor o un número erroneo.{fin+fondo}        {fin+marco}║{fin}")
            print                    (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
                    
        print                        (f"                   {marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}") 
        print                        (f"                   {marco}║{fondo}     {texto}Volver al Menu  < volver >{fin+fondo}       {fin+marco}║{fondo}     {texto}< salir >  Salir del programa{fin+fondo}      {fin+marco}║{fin}")
        print                        (f"                   {marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}") 
        Volver = input                                     ("\n\t\t\t\t\t\t\t         ").upper()
        
        if Volver == "salir":
            
           Mensaje_de_Agradecimiento()   
            
        elif Volver == "volver":
            
            continue
                
    elif option == "C":

        Limpieza_consola()                   
        
        try:
        
            Retorna_C = option_C()
            
            if Respuesta == "no" :
            
                print                (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}") 
                print                (f"                   {marco}║{fondo}     {fin+error_texto}Recordatorio: Sin conexión por lo que no se guardará sus operaciones.{fin+fondo}     {fin+marco}║{fin}")
                print                (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
            
            else :
            
                Numero1, Operador, Numero2, Resultado = Retorna_C[0:4]
                
                Insert_A_F(Nombre, Numero1, Operador, Numero2, Resultado)

        except:
            
            print                    (f"                   {marco}╠══════════════════════════════════════════════════════════╩════════════════════╣{fin}")
            print                    (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}") 
            print                    (f"                   {marco}║{fondo}         {fin+error_texto}Error Interno! el retorno no esta devuelviendo un valor{fin+fondo}               {fin+marco}║{fin}")
            print                    (f"                   {marco}║{fondo}        {fin+error_texto}Posibles causas: Inserto letras como valor o un número erroneo.{fin+fondo}        {fin+marco}║{fin}")
            print                    (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
                    
        print                        (f"                   {marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}") 
        print                        (f"                   {marco}║{fondo}     {texto}Volver al Menu  < volver >{fin+fondo}       {fin+marco}║{fondo}     {texto}< salir >  Salir del programa{fin+fondo}      {fin+marco}║{fin}")
        print                        (f"                   {marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}") 
        Volver = input                                     ("\n\t\t\t\t\t\t\t         ").upper()
        
        if Volver == "salir":
            
            Mensaje_de_Agradecimiento() 
            
        elif Volver == "volver":
            
            continue 
            
    elif option == "D":
        
        Limpieza_consola()
        
        try:
            
            Retorna_D = option_D()
            
            if Respuesta == "no" :
            
                print                (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}") 
                print                (f"                   {marco}║{fondo}     {fin+error_texto}Recordatorio: Sin conexión por lo que no se guardará sus operaciones.{fin+fondo}     {fin+marco}║{fin}")
                print                (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
            
            else :
            
                Numero1, Operador, Numero2, Resultado = Retorna_D[0:4]
                
                Insert_A_F(Nombre, Numero1, Operador, Numero2, Resultado)

        except:
            
            print                    (f"                   {marco}╠══════════════════════════════════════════════════════════╩════════════════════╣{fin}")
            print                    (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}") 
            print                    (f"                   {marco}║{fondo}         {fin+error_texto}Error Interno! el retorno no esta devuelviendo un valor{fin+fondo}               {fin+marco}║{fin}")
            print                    (f"                   {marco}║{fondo}        {fin+error_texto}Posibles causas: Inserto letras como valor o un número erroneo.{fin+fondo}        {fin+marco}║{fin}")
            print                    (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
                    
        print                        (f"                   {marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}") 
        print                        (f"                   {marco}║{fondo}     {texto}Volver al Menu  < volver >{fin+fondo}       {fin+marco}║{fondo}     {texto}< salir >  Salir del programa{fin+fondo}      {fin+marco}║{fin}")
        print                        (f"                   {marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}") 
        Volver = input                                     ("\n\t\t\t\t\t\t\t         ").upper()
        
        if Volver == "salir":
            
            Mensaje_de_Agradecimiento() 
            
        elif Volver == "volver":
            
            continue
            
    elif option == "E":
            
        Limpieza_consola()

        try:
            
            Retorna_E = option_E()
            
            if Respuesta == "no" :
            
                print                (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}") 
                print                (f"                   {marco}║{fondo}     {fin+error_texto}Recordatorio: Sin conexión por lo que no se guardará sus operaciones.{fin+fondo}     {fin+marco}║{fin}")
                print                (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
            
            else :
            
                Numero1, Operador, Numero2, Resultado = Retorna_E[0:4]
                
                Insert_A_F(Nombre, Numero1, Operador, Numero2, Resultado)

        except:
            
            print                    (f"                   {marco}╠══════════════════════════════════════════════════════════╩════════════════════╣{fin}")
            print                    (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}") 
            print                    (f"                   {marco}║{fondo}         {fin+error_texto}Error Interno! el retorno no esta devuelviendo un valor{fin+fondo}               {fin+marco}║{fin}")
            print                    (f"                   {marco}║{fondo}        {fin+error_texto}Posibles causas: Inserto letras como valor o un número erroneo.{fin+fondo}        {fin+marco}║{fin}")
            print                    (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
                    
        print                        (f"                   {marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}") 
        print                        (f"                   {marco}║{fondo}     {texto}Volver al Menu  < volver >{fin+fondo}       {fin+marco}║{fondo}     {texto}< salir >  Salir del programa{fin+fondo}      {fin+marco}║{fin}")
        print                        (f"                   {marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}")  
        Volver = input                                     ("\n\t\t\t\t\t\t\t         ").upper()
        
        if Volver == "salir":
            
            Mensaje_de_Agradecimiento()   
            
        elif Volver == "volver":
            
            continue
            
    elif option == "F":
        
        Limpieza_consola()                  
        
        try: 
        
            Retorna_F =option_F()
            
            if Respuesta == "no" :
            
                print                (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}") 
                print                (f"                   {marco}║{fondo}     {fin+error_texto}Recordatorio: Sin conexión por lo que no se guardará sus operaciones.{fin+fondo}     {fin+marco}║{fin}")
                print                (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
            
            else :
            
                Numero1, Operador, Numero2, Resultado = Retorna_F[0:4]
            
                Insert_A_F(Nombre, Numero1, Operador, Numero2, Resultado) 

        except:
        
            print                    (f"                   {marco}╠══════════════════════════════════════════════════════════╩════════════════════╣{fin}")
            print                    (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}") 
            print                    (f"                   {marco}║{fondo}         {fin+error_texto}Error Interno! el retorno no esta devuelviendo un valor{fin+fondo}               {fin+marco}║{fin}")
            print                    (f"                   {marco}║{fondo}        {fin+error_texto}Posibles causas: Inserto letras como valor o un número erroneo.{fin+fondo}        {fin+marco}║{fin}")
            print                    (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
                    
        print                        (f"                   {marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}") 
        print                        (f"                   {marco}║{fondo}     {texto}Volver al Menu  < volver >{fin+fondo}       {fin+marco}║{fondo}     {texto}< salir >  Salir del programa{fin+fondo}      {fin+marco}║{fin}")
        print                        (f"                   {marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}") 
        Volver = input                                     ("\n\t\t\t\t\t\t\t         ").upper()
        
        if Volver == "salir":
            
            Mensaje_de_Agradecimiento()   
            
        elif Volver == "volver":
            
            continue 
                        
    elif option == "G":

        Limpieza_consola()

        try:
        
            Retorna_G = option_G()
            
            if Respuesta == "no" :
            
                print                (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}") 
                print                (f"                   {marco}║{fondo}     {fin+error_texto}Recordatorio: Sin conexión por lo que no se guardará sus operaciones.{fin+fondo}     {fin+marco}║{fin}")
                print                (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
            
            else :
                
                Numero1, Operador, Conclusion = Retorna_G[0:3]
                
                Insert_G_H(Nombre, Numero1, Operador, Conclusion)

        except:
            
            print                    (f"                   {marco}╠══════════════════════════════════════════════════════════╩════════════════════╣{fin}")
            print                    (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}") 
            print                    (f"                   {marco}║{fondo}         {fin+error_texto}Error Interno! el retorno no esta devuelviendo un valor{fin+fondo}               {fin+marco}║{fin}")
            print                    (f"                   {marco}║{fondo}        {fin+error_texto}Posibles causas: Inserto letras como valor o un número erroneo.{fin+fondo}        {fin+marco}║{fin}")
            print                    (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
                    
        print                        (f"                   {marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}") 
        print                        (f"                   {marco}║{fondo}     {texto}Volver al Menu  < volver >{fin+fondo}       {fin+marco}║{fondo}     {texto}< salir >  Salir del programa{fin+fondo}      {fin+marco}║{fin}")
        print                        (f"                   {marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}")  
        Volver = input                                     ("\n\t\t\t\t\t\t\t         ").upper()
        
        if Volver == "salir":
            
            Mensaje_de_Agradecimiento()     
            
        elif Volver == "volver":
            
            continue
                    
    elif option == "H":
            
        Limpieza_consola()
        print("\n\n")

        try:
        
            Retorna_H = option_H()
                
            Num1, Operator, conclution = Retorna_H[0:3]
            
            Insert_G_H(Nombre, Num1, Operator, conclution)

        except:
            
            print                    (f"                   {marco}╠══════════════════════════════════════════════════════════╩════════════════════╣{fin}")
            print                    (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}") 
            print                    (f"                   {marco}║{fondo}         {fin+error_texto}Error Interno! el retorno no esta devuelviendo un valor{fin+fondo}               {fin+marco}║{fin}")
            print                    (f"                   {marco}║{fondo}        {fin+error_texto}Posibles causas: Inserto letras como valor o un número erroneo.{fin+fondo}        {fin+marco}║{fin}")
            print                    (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
                    
        print                        (f"                   {marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}") 
        print                        (f"                   {marco}║{fondo}     {texto}Volver al Menu  < volver >{fin+fondo}       {fin+marco}║{fondo}     {texto}< salir >  Salir del programa{fin+fondo}      {fin+marco}║{fin}")
        print                        (f"                   {marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}") 
        Volver = input                                     ("\n\t\t\t\t\t\t\t         ").upper()
        
        if Volver == "salir":
            
            Mensaje_de_Agradecimiento()    
            
        elif Volver == "volver":
            
            continue
            
    elif option == "I":
                
        Limpieza_consola()
        print("\n\n")

        try:            
        
            option_I()
            
        except:
            
            print                    (f"                   {marco}╠══════════════════════════════════════════════════════════╩════════════════════╣{fin}")
            print                    (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}") 
            print                    (f"                   {marco}║{fondo}         {fin+error_texto}Error Interno! el retorno no esta devuelviendo un valor{fin+fondo}               {fin+marco}║{fin}")
            print                    (f"                   {marco}║{fondo}        {fin+error_texto}Posibles causas: Inserto letras como valor o un número erroneo.{fin+fondo}        {fin+marco}║{fin}")
            print                    (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
                    
        print                        (f"                   {marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}") 
        print                        (f"                   {marco}║{fondo}     {texto}Volver al Menu  < volver >{fin+fondo}       {fin+marco}║{fondo}     {texto}< salir >  Salir del programa{fin+fondo}      {fin+marco}║{fin}")
        print                        (f"                   {marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}") 
        Volver = input                                     ("\n\t\t\t\t\t\t\t         ").upper()
        
        if Volver == "salir":
            
            Mensaje_de_Agradecimiento()   
            
        elif Volver == "volver":
            
            continue
            
    else:   
        
        Limpieza_consola()
           
        Error_Mensaje_de_Menu()  # Bien