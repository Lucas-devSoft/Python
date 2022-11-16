from Funciones import *

print()
    
print                                                                                                   ( '        ┌───────────────────────────────────────────────────────────────┐      ')
print                                                                                                   ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
print                                                                                                   ( '  │     └───────────────────────────────────────────────────────────────┘     │')
print                                                                                                   ( '  │                                                                           │')
print                                                                                                   ( '  │       ╔═════════════════════════════════════════╦════════════════╗        │')
nombre = input                                                                                          ( '  │       ║  Bienvenido usuario, Cuál es su nombre? ║     ').capitalize()
print                                                                                                   ( '  │       ╚═════════════════════════════════════════╩════════════════╝        │') 

while not (nombre.isalpha() and len(nombre) > 3):
    
    limpiar_consola()
    
    print                                                                                               ( '        ┌───────────────────────────────────────────────────────────────┐      ')
    print                                                                                               ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
    print                                                                                               ( '  │     └───────────────────────────────────────────────────────────────┘     │')
    print                                                                                               ( '  │                                                                           │')
    print                                                                                               ( '  │       ╔═══════════════╦══════════════════════════════════════════╗        │')
    print                                                                                               ( '  │       ║ ⚠  Error  ⚠   ║  Formato de nombre inválido o vacio.     ║        │')
    print                                                                                               ( '  │       ╠═══════════════╩═══════════════════════════════╦══════════╝        │')
    respuesta = input                                                                                   ( '  │       ║      Quiere SALIR (S) o REINTENTAR (R)        ║     ').upper()
    print                                                                                               ( '  │       ╚═══════════════════════════════════════════════╩══════════╝        │')

    while respuesta != "S" and respuesta != "R":
                
        print                                                                                           ( '  │                                                                           │')
        print                                                                                           ( '  │       ╔═══════════════╦══════════════════════════════════════════╗        │')
        print                                                                                           ( '  │       ║ ⚠  Error  ⚠   ║  Respuestas que se esperan son S o R     ║        │')
        print                                                                                           ( '  │       ╠═══════════════╩════════════════════════════════╦═════════╝        │')
        respuesta = input                                                                               ( '  │       ║      Quiere SALIR (S) o REINTENTAR (R)         ║     ').upper()
        print                                                                                           ( '  │       ╚════════════════════════════════════════════════╩═════════╝        │')
            
    else:
        
        if respuesta == "S":
            
            print                                                                                       ( '  │                                                                           │')
            print                                                                                       ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
            print                                                                                       ( '  │       ║          Gracias por utilizar mi proyecto                ║        │')
            print                                                                                       ( '  │       ║    Presione ENTER para finalizar con el programa         ║        │')
            print                                                                                       ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
            print                                                                                       ( '  └───────────────────────────────────────────────────────────────────────────┘')
            input()           
            
            break
        
        elif respuesta == 'R':
            
            limpiar_consola()

            print()

            print                                                                                       ( '        ┌───────────────────────────────────────────────────────────────┐      ')
            print                                                                                       ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
            print                                                                                       ( '  │     └───────────────────────────────────────────────────────────────┘     │')
            print                                                                                       ( '  │                                                                           │')
            print                                                                                       ( '  │       ╔═════════════════════════════════════════╦════════════════╗        │')
            nombre = input                                                                              ( '  │       ║   Hola Usuario, ¿ Cuál es su nombre ?   ║      ').capitalize()
            print                                                                                       ( '  │       ╚═════════════════════════════════════════╩════════════════╝        │') 

while nombre.isalpha() and len(nombre) > 3:

    limpiar_consola()

    print()

    print                                                                                               ( '        ┌───────────────────────────────────────────────────────────────┐      ')
    print                                                                                               ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
    print                                                                                               ( '  │     └───────────────────────────────────────────────────────────────┘     │')
    print                                                                                               ( '  │                                                                           │')
    print                                                                                               ( '  │       ╔═════════════════════════════════════════════════════════╗         │')
    print                                                                                               (f'  │       ║   Hola {nombre}, Bienvenido/a a mi Proyecto Personal       ║         │')
    print                                                                                               ( '  │       ╚═════════════════════════════════════════════════════════╝         │')
    print                                                                                               ( '  │                                                                           │')
    print                                                                                               ( '  │              ╔═════════════════════════════════════════════╗              │')
    print                                                                                               ( '  │              ║        Calculadora interactiva Python       ║              │')
    print                                                                                               ( '  │              ╠═══════════════════════════════╦═════════════╣              │')
    print                                                                                               ( '  │              ║ A ► Adición             (+)   ║   SUMAR     ║              │')
    print                                                                                               ( '  │              ╠═══════════════════════════════╬═════════════╣              │')
    print                                                                                               ( '  │              ║ B ► Sustracción         (-)   ║   RESTAR    ║              │')
    print                                                                                               ( '  │              ╠═══════════════════════════════╬═════════════╣              │')
    print                                                                                               ( '  │              ║ C ► Multiplicación      (*)   ║ MULTIPLICAR ║              │')
    print                                                                                               ( '  │              ╠═══════════════════════════════╬═════════════╣              │')
    print                                                                                               ( '  │              ║ D ► División            (/)   ║   DIVIDIR   ║              │')
    print                                                                                               ( '  │              ╠═══════════════════════════════╬═════════════╣              │')
    print                                                                                               ( '  │              ║ E ► Exponenciación    (b,e)   ║  EXPONENTE  ║              │')
    print                                                                                               ( '  │              ╠═══════════════════════════════╬═════════════╣              │')
    print                                                                                               ( '  │              ║ F ► Radicación          (√)   ║   RAICES    ║              │')
    print                                                                                               ( '  │              ╠═══════════════════════════════╬═════════════╣              │')
    print                                                                                               ( '  │              ║ G ► Número PAR o IMPAR        ║   PARIDAD   ║              │')
    print                                                                                               ( '  │              ╠═══════════════════════════════╬═════════════╣              │')
    print                                                                                               ( '  │              ║ H ► Números Primos Individual ║  PRIMALIDAD ║              │')
    print                                                                                               ( '  │              ╠═══════════════════════════════╬═════════════╣              │')   
    print                                                                                               ( '  │              ║ I ► Números Primos por Rango  ║  PRIMALIDAD ║              │')
    print                                                                                               ( '  │              ╚═══════════════════════════════╩═════════════╝              │')      
        
    print                                                                                               ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
    opcion = input                                                                                      (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
    print                                                                                               ( '  │           ╚══════════════════════════════════════════╩════════╝           │')

    print()
                     
    while not (opcion == 'A' or opcion == 'B' or opcion == 'C' or opcion == 'D' or opcion == 'E' or opcion == 'F' or opcion == 'G' or opcion == 'H' or opcion == 'I'):
            
        limpiar_consola()

        print()

        print                                                                                   ( '        ┌───────────────────────────────────────────────────────────────┐      ')
        print                                                                                   ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
        print                                                                                   ( '  │     └───────────────────────────────────────────────────────────────┘     │')
        print                                                                                   ( '  │                                                                           │')
        print                                                                                   ( '  │       ╔══════════════╦═══════════════════════════════════════════╗        │')
        print                                                                                   ( '  │       ║ ⚠  Error  ⚠  ║  La opción elegida no esta en la lista    ║        │')
        print                                                                                   ( '  │       ╠══════════════╩═══════════════════════════════╦═══════════╝        │')
        respuesta = input                                                                       ( '  │       ║      Quiere SALIR (S) o REINTENTAR (R)       ║     ').upper()
        print                                                                                   ( '  │       ╚══════════════════════════════════════════════╩═══════════╝        │')

        while respuesta != 'S' and respuesta != 'R':
            
            print                                                                               ( '  │                                                                           │')
            print                                                                               ( '  │       ╔═══════════════╦══════════════════════════════════════════╗        │')
            print                                                                               ( '  │       ║ ⚠  Error  ⚠   ║  Respuestas que se esperan son S o R     ║        │')
            print                                                                               ( '  │       ╠═══════════════╩════════════════════════════════╦═════════╝        │')
            respuesta = input                                                                   ( '  │       ║      Quiere SALIR (S) o REINTENTAR (R)         ║     ').upper()
            print                                                                               ( '  │       ╚════════════════════════════════════════════════╩═════════╝        │')
            
        else:
                    
            if respuesta == 'S':
                
                print                                                                           ( '  │                                                                           │')
                print                                                                           ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
                print                                                                           ( '  │       ║          Gracias por utilizar mi proyecto                ║        │')
                print                                                                           ( '  │       ║    Presione ENTER para finalizar con el programa         ║        │')
                print                                                                           ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
                print                                                                           ( '  └───────────────────────────────────────────────────────────────────────────┘')
                input()
                
                break
            
            elif respuesta == 'R':
                
                limpiar_consola()
            
                Menu(nombre)
                        
                print                                                                               ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
                opcion = input                                                                      (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
                print                                                                               ( '  │           ╚══════════════════════════════════════════╩════════╝           │')       
        
    while opcion == 'A' or opcion == 'B' or opcion == 'C' or opcion == 'D'  or opcion == 'E' or opcion == 'F' or opcion == 'G' or opcion == 'H' or opcion == 'I':       
              
        if opcion == 'A':
                    
            print()
            
            limpiar_consola()

            print                                                                                   ( '        ┌───────────────────────────────────────────────────────────────┐      ')
            print                                                                                   ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
            print                                                                                   ( '  │     └───────────────────────────────────────────────────────────────┘     │')
            print                                                                                   ( '  │                                                                           │')
            print                                                                                   ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
            print                                                                                   (f'  │       ║        Hola {nombre}, has elegido la opción SUMAR           ║        │')
            print                                                                                   ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
            print                     
            
            opcion_A()
            
            print                                                                                   ( '  ├─────────────────────────────────────┬─────────────────────────────────────┤')
            print                                                                                   ( '  │            VOLVER AL MENU  < M >    │    < S >  SALIR DEL PROGRAMA        │')
            retroceder = input                                                                      ( '  └─────────────────────────────────────┴─────────────────────────────────────┘\n\t\t\t\t\t').upper()
            
            if retroceder == 'S':
                
                break
                 
            elif retroceder == 'M':
                
                limpiar_consola()
            
                Menu(nombre)
                        
                print                                                                               ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
                opcion = input                                                                      (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
                print                                                                               ( '  │           ╚══════════════════════════════════════════╩════════╝           │')  
        
        elif opcion == 'B':
                    
            print()
            
            limpiar_consola()

            print                                                                                   ( '        ┌───────────────────────────────────────────────────────────────┐      ')
            print                                                                                   ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
            print                                                                                   ( '  │     └───────────────────────────────────────────────────────────────┘     │')
            print                                                                                   ( '  │                                                                           │')
            print                                                                                   ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
            print                                                                                   (f'  │       ║        Hola {nombre}, has elegido la opción RESTAR          ║        │')
            print                                                                                   ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
            print                                                                                   ( '  │                                                                           │')
            
            opcion_B()
            
            print                                                                                   ( '  ├─────────────────────────────────────┬─────────────────────────────────────┤')
            print                                                                                   ( '  │            VOLVER AL MENU  < M >    │    < S >  SALIR DEL PROGRAMA        │')
            retroceder = input                                                                      ( '  └─────────────────────────────────────┴─────────────────────────────────────┘\n\t\t\t\t\t').upper()
            
            if retroceder == 'S':
                
                break
            
            elif retroceder == 'M':
                
                limpiar_consola()
            
                Menu(nombre)
                        
                print                                                                               ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
                opcion = input                                                                      (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
                print                                                                               ( '  │           ╚══════════════════════════════════════════╩════════╝           │')              
                    
        elif opcion == 'C':

            print()

            limpiar_consola()
            
            print                                                                                   ( '        ┌───────────────────────────────────────────────────────────────┐      ')
            print                                                                                   ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
            print                                                                                   ( '  │     └───────────────────────────────────────────────────────────────┘     │')
            print                                                                                   ( '  │                                                                           │')
            print                                                                                   ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
            print                                                                                   (f'  │       ║        Hola {nombre}, has elegido la opción MULTIPLICAR     ║        │')
            print                                                                                   ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
            print                                                                                   ( '  │                                                                           │')
            
            opcion_C()
            
            print                                                                                   ( '  ├─────────────────────────────────────┬─────────────────────────────────────┤')
            print                                                                                   ( '  │            VOLVER AL MENU  < M >    │    < S >  SALIR DEL PROGRAMA        │')
            retroceder = input                                                                      ( '  └─────────────────────────────────────┴─────────────────────────────────────┘\n\t\t\t\t\t').upper()
            
            if retroceder == 'S':
                
                break
            
            elif retroceder == 'M':
                
                limpiar_consola()
            
                Menu(nombre)
                        
                print                                                                               ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
                opcion = input                                                                      (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
                print                                                                               ( '  │           ╚══════════════════════════════════════════╩════════╝           │')                                                                           ( '  │           ╚══════════════════════════════════════════╩════════╝           │')     
                
        elif opcion == 'D':
                
            print()
            
            limpiar_consola()

            print                                                                                   ( '        ┌───────────────────────────────────────────────────────────────┐      ')
            print                                                                                   ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
            print                                                                                   ( '  │     └───────────────────────────────────────────────────────────────┘     │')
            print                                                                                   ( '  │                                                                           │')
            print                                                                                   ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
            print                                                                                   (f'  │       ║        Hola {nombre}, has elegido la opción DIVIDIR         ║        │')
            print                                                                                   ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
            print                                                                                   ( '  │                                                                           │')
            
            opcion_D()
            
            print                                                                                   ( '  ├─────────────────────────────────────┬─────────────────────────────────────┤')
            print                                                                                   ( '  │            VOLVER AL MENU  < M >    │    < S >  SALIR DEL PROGRAMA        │')
            retroceder = input                                                                      ( '  └─────────────────────────────────────┴─────────────────────────────────────┘\n\t\t\t\t\t').upper()
            
            if retroceder == 'S':
                
                break
            
            elif retroceder == 'M':
                
                limpiar_consola()
            
                Menu(nombre)
                        
                print                                                                               ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
                opcion = input                                                                      (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
                print                                                                               ( '  │           ╚══════════════════════════════════════════╩════════╝           │')     
                
        elif opcion == 'E':
                
            print()
            
            limpiar_consola()

            print                                                                                   ( '        ┌───────────────────────────────────────────────────────────────┐      ')
            print                                                                                   ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
            print                                                                                   ( '  │     └───────────────────────────────────────────────────────────────┘     │')
            print                                                                                   ( '  │                                                                           │')
            print                                                                                   ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
            print                                                                                   (f'  │       ║        Hola {nombre}, has elegido la opción EXPONENTE       ║        │')
            print                                                                                   ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
            print                                                                                   ( '  │                                                                           │')
            
            opcion_E()
            
            print                                                                                   ( '  ├─────────────────────────────────────┬─────────────────────────────────────┤')
            print                                                                                   ( '  │            VOLVER AL MENU  < M >    │    < S >  SALIR DEL PROGRAMA        │')
            retroceder = input                                                                      ( '  └─────────────────────────────────────┴─────────────────────────────────────┘\n\t\t\t\t\t').upper()
            
            if retroceder == 'S':
                
                break
            
            elif retroceder == 'M':
                
                limpiar_consola()
            
                Menu(nombre)
                        
                print                                                                               ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
                opcion = input                                                                      (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
                print                                                                               ( '  │           ╚══════════════════════════════════════════╩════════╝           │') 
                
        elif opcion == 'F':

            print()
            
            limpiar_consola()

            print                                                                                   ( '        ┌───────────────────────────────────────────────────────────────┐      ')
            print                                                                                   ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
            print                                                                                   ( '  │     └───────────────────────────────────────────────────────────────┘     │')
            print                                                                                   ( '  │                                                                           │')
            print                                                                                   ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
            print                                                                                   (f'  │       ║        Hola {nombre}, has elegido la opción RAICES          ║        │')
            print                                                                                   ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
            print                                                                                   ( '  │                                                                           │')
            
            opcion_F()
            
            print                                                                                   ( '  ├─────────────────────────────────────┬─────────────────────────────────────┤')
            print                                                                                   ( '  │            VOLVER AL MENU  < M >    │    < S >  SALIR DEL PROGRAMA        │')
            retroceder = input                                                                      ( '  └─────────────────────────────────────┴─────────────────────────────────────┘\n\t\t\t\t\t').upper()
            
            if retroceder == 'S':
                
                break
            
            elif retroceder == 'M':
                
                limpiar_consola()
            
                Menu(nombre)
                        
                print                                                                               ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
                opcion = input                                                                      (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
                print                                                                               ( '  │           ╚══════════════════════════════════════════╩════════╝           │')    
                
        elif opcion == 'G':

            print()
            
            limpiar_consola()

            print                                                                                   ( '        ┌───────────────────────────────────────────────────────────────┐      ')
            print                                                                                   ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
            print                                                                                   ( '  │     └───────────────────────────────────────────────────────────────┘     │')
            print                                                                                   ( '  │                                                                           │')
            print                                                                                   ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
            print                                                                                   (f'  │       ║        Hola {nombre}, has elegido la opción PARIDAD         ║        │')
            print                                                                                   ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
            print                                                                                   ( '  │                                                                           │')
            
            opcion_G()
            
            print                                                                                   ( '  ├─────────────────────────────────────┬─────────────────────────────────────┤')
            print                                                                                   ( '  │            VOLVER AL MENU  < M >    │    < S >  SALIR DEL PROGRAMA        │')
            retroceder = input                                                                      ( '  └─────────────────────────────────────┴─────────────────────────────────────┘\n\t\t\t\t\t').upper()
            
            if retroceder == 'S':
                
                break  
            
            elif retroceder == 'M':
                
                limpiar_consola()
            
                Menu(nombre)
                        
                print                                                                               ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
                opcion = input                                                                      (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
                print                                                                               ( '  │           ╚══════════════════════════════════════════╩════════╝           │')   
                        
        elif opcion == 'H':
                
            print()
            
            limpiar_consola()

            print                                                                                   ( '        ┌───────────────────────────────────────────────────────────────┐      ')
            print                                                                                   ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
            print                                                                                   ( '  │     └───────────────────────────────────────────────────────────────┘     │')
            print                                                                                   ( '  │                                                                           │')
            print                                                                                   ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
            print                                                                                   (f'  │       ║        Hola {nombre}, has elegido la opción PRIMALIDAD         ║        │')
            print                                                                                   ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
            print                                                                                   ( '  │                                                                           │')
            
            opcion_H()
            
            print                                                                                   ( '  ├─────────────────────────────────────┬─────────────────────────────────────┤')
            print                                                                                   ( '  │            VOLVER AL MENU  < M >    │    < S >  SALIR DEL PROGRAMA        │')
            retroceder = input                                                                      ( '  └─────────────────────────────────────┴─────────────────────────────────────┘\n\t\t\t\t\t').upper()
            
            if retroceder == 'S':
                
                break
            
            elif retroceder == 'M':
                
                limpiar_consola()
            
                Menu(nombre)
                        
                print                                                                               ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
                opcion = input                                                                      (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
                print                                                                               ( '  │           ╚══════════════════════════════════════════╩════════╝           │')   
            
                
        elif opcion == 'I':
                    
            print()
            
            limpiar_consola()

            print                                                                                   ( '        ┌───────────────────────────────────────────────────────────────┐      ')
            print                                                                                   ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
            print                                                                                   ( '  │     └───────────────────────────────────────────────────────────────┘     │')
            print                                                                                   ( '  │                                                                           │')
            print                                                                                   ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
            print                                                                                   (f'  │       ║       Hola {nombre}, has elegido la opción PRIMALIDAD       ║        │')
            print                                                                                   ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
            print                                                                                   ( '  │                                                                           │')    
            
            opcion_I()
            
            print                                                                                   ( '  ├─────────────────────────────────────┬─────────────────────────────────────┤')
            print                                                                                   ( '  │            VOLVER AL MENU  < M >    │    < S >  SALIR DEL PROGRAMA        │')
            retroceder = input                                                                      ( '  └─────────────────────────────────────┴─────────────────────────────────────┘\n\t\t\t\t\t').upper()
            
            if retroceder == 'S':
                
                break                               
            
            elif retroceder == 'M':
                
                limpiar_consola()
            
                Menu(nombre)
                        
                print                                                                               ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
                opcion = input                                                                      (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
                print                                                                               ( '  │           ╚══════════════════════════════════════════╩════════╝           │')        
            
    break