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
    
    print                                                                                       ( '        ┌───────────────────────────────────────────────────────────────┐      ')
    print                                                                                       ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
    print                                                                                       ( '  │     └───────────────────────────────────────────────────────────────┘     │')
    print                                                                                       ( '  │                                                                           │')
    print                                                                                       ( '  │       ╔═══════════════╦══════════════════════════════════════════╗        │')
    print                                                                                       ( '  │       ║ ⚠  Error  ⚠   ║  Formato de nombre inválido o vacio.     ║        │')
    print                                                                                       ( '  │       ╠═══════════════╩═══════════════════════════════╦══════════╝        │')
    respuesta = input                                                                           ( '  │       ║      Quiere SALIR (S) o REINTENTAR (R)        ║     ').upper()
    print                                                                                       ( '  │       ╚═══════════════════════════════════════════════╩══════════╝        │')

    while respuesta != "S" and respuesta != "R":
            
        print                                                                                   ( '  │                                                                           │')
        print                                                                                   ( '  │       ╔═══════════════╦══════════════════════════════════════════╗        │')
        print                                                                                   ( '  │       ║ ⚠  Error  ⚠   ║  Respuestas que se esperan son S o R     ║        │')
        print                                                                                   ( '  │       ╠═══════════════╩════════════════════════════════╦═════════╝        │')
        respuesta = input                                                                       ( '  │       ║      Quiere SALIR (S) o REINTENTAR (R)         ║     ').upper()
        print                                                                                   ( '  │       ╚════════════════════════════════════════════════╩═════════╝        │')
            
    else:
        
        if respuesta == "S":
            
            print                                                                               ( '  │                                                                           │')
            print                                                                               ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
            print                                                                               ( '  │       ║          Gracias por utilizar mi proyecto                ║        │')
            print                                                                               ( '  │       ║    Presione ENTER para finalizar con el programa         ║        │')
            print                                                                               ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
            print                                                                               ( '  └───────────────────────────────────────────────────────────────────────────┘')
            input()
            
            break
            
        elif respuesta == "R":
                
            limpiar_consola()
            
            print()
            print()

            print                                                                               ( '        ┌───────────────────────────────────────────────────────────────┐      ')
            print                                                                               ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
            print                                                                               ( '  │     └───────────────────────────────────────────────────────────────┘     │')
            print                                                                               ( '  │                                                                           │')
            print                                                                               ( '  │       ╔═════════════════════════════════════════╦════════════════╗        │')
            nombre = input                                                                      ( '  │       ║   Hola Usuario, ¿ Cuál es su nombre ?   ║      ').capitalize()
            print                                                                               ( '  │       ╚═════════════════════════════════════════╩════════════════╝        │')  

else: 
    
    #while nombre.isalpha() and len(nombre) > 3:
    
    limpiar_consola()

    print()

    Menu(nombre) 
        
    print                                                                                           ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
    opcion = input                                                                                  (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
    print                                                                                           ( '  │           ╚══════════════════════════════════════════╩════════╝           │')

    print()

    while opcion == 'A' or opcion == 'B' or opcion == 'C' or opcion == 'D' or opcion == 'E' or opcion == 'F' or opcion == 'G' or opcion == 'H' or opcion == 'I':
        
        match opcion:

            case 'A':
            
                print()
                print()
                
                limpiar_consola()

                print                                                                               ( '        ┌───────────────────────────────────────────────────────────────┐      ')
                print                                                                               ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
                print                                                                               ( '  │     └───────────────────────────────────────────────────────────────┘     │')
                print                                                                               ( '  │                                                                           │')
                print                                                                               ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
                print                                                                               (f'  │       ║        Hola {nombre}, has elegido la opción SUMAR           ║        │')
                print                                                                               ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
                print                     
                opcion_A()
                print                                                                               ( '  │ <Volver al Menu> V                                   <Quiero Salir> ENTER │')
                retroceder = input                                                                  ( '  └───────────────────────────────────────────────────────────────────────────┘\n\t\t\t\t\t').upper()
                
                if retroceder == 'V':
                    
                    limpiar_consola()
                    
                    Menu(nombre)
                    
                    print                                                                           ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
                    opcion = input                                                                  (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
                    print                                                                           ( '  │           ╚══════════════════════════════════════════╩════════╝           │')     
                
                break                                  
                
            case 'B':

                print()
                print()
                
                limpiar_consola()

                print                                                                               ( '        ┌───────────────────────────────────────────────────────────────┐      ')
                print                                                                               ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
                print                                                                               ( '  │     └───────────────────────────────────────────────────────────────┘     │')
                print                                                                               ( '  │                                                                           │')
                print                                                                               ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
                print                                                                               (f'  │       ║        Hola {nombre}, has elegido la opción RESTAR          ║        │')
                print                                                                               ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
                print                                                                               ( '  │                                                                           │')
                opcion_B()
                print                                                                               ( '  │ <Volver al Menu> V                                   <Quiero Salir> ENTER │')
                retroceder = input                                                                  ( '  └───────────────────────────────────────────────────────────────────────────┘\n\t\t\t\t\t').upper()
                
                if retroceder == 'V':
                    
                    limpiar_consola()
                    
                    Menu(nombre)
                    
                    print                                                                           ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
                    opcion = input                                                                  (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
                    print                                                                           ( '  │           ╚══════════════════════════════════════════╩════════╝           │')     
                    
                break
                    
                    
            case 'C':

                print()
                print()

                limpiar_consola()
                
                print                                                                               ( '        ┌───────────────────────────────────────────────────────────────┐      ')
                print                                                                               ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
                print                                                                               ( '  │     └───────────────────────────────────────────────────────────────┘     │')
                print                                                                               ( '  │                                                                           │')
                print                                                                               ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
                print                                                                               (f'  │       ║        Hola {nombre}, has elegido la opción MULTIPLICAR     ║        │')
                print                                                                               ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
                print                                                                               ( '  │                                                                           │')
                opcion_C()
                print                                                                               ( '  │ <Volver al Menu> V                                   <Quiero Salir> ENTER │')
                retroceder = input                                                                  ( '  └───────────────────────────────────────────────────────────────────────────┘\n\t\t\t\t\t').upper()
                
                if retroceder == 'V':
                    
                    limpiar_consola()
                    
                    Menu(nombre)
                    
                    print                                                                           ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
                    opcion = input                                                                  (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
                    print                                                                           ( '  │           ╚══════════════════════════════════════════╩════════╝           │')     
                    
                break
                                

            case 'D':

                print()
                print()
                
                limpiar_consola()

                print                                                                               ( '        ┌───────────────────────────────────────────────────────────────┐      ')
                print                                                                               ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
                print                                                                               ( '  │     └───────────────────────────────────────────────────────────────┘     │')
                print                                                                               ( '  │                                                                           │')
                print                                                                               ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
                print                                                                               (f'  │       ║        Hola {nombre}, has elegido la opción DIVIDIR         ║        │')
                print                                                                               ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
                print                                                                               ( '  │                                                                           │')
                opcion_D()
                print                                                                               ( '  │ <Volver al Menu> V                                   <Quiero Salir> ENTER │')
                retroceder = input                                                                  ( '  └───────────────────────────────────────────────────────────────────────────┘\n\t\t\t\t\t').upper()
                
                if retroceder == 'V':
                    
                    limpiar_consola()
                    
                    Menu(nombre)
                    
                    print                                                                           ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
                    opcion = input                                                                  (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
                    print                                                                           ( '  │           ╚══════════════════════════════════════════╩════════╝           │')     
                    
                break
                    
            
            case 'E':

                print()
                print()
                
                limpiar_consola()

                print                                                                               ( '        ┌───────────────────────────────────────────────────────────────┐      ')
                print                                                                               ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
                print                                                                               ( '  │     └───────────────────────────────────────────────────────────────┘     │')
                print                                                                               ( '  │                                                                           │')
                print                                                                               ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
                print                                                                               (f'  │       ║        Hola {nombre}, has elegido la opción EXPONENTE       ║        │')
                print                                                                               ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
                print                                                                               ( '  │                                                                           │')
                opcion_E()
                print                                                                               ( '  │ <Volver al Menu> V                                   <Quiero Salir> ENTER │')
                retroceder = input                                                                  ( '  └───────────────────────────────────────────────────────────────────────────┘\n\t\t\t\t\t').upper()
                
                if retroceder == 'V':
                    
                    limpiar_consola()
                    
                    Menu(nombre)
                    
                    print                                                                           ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
                    opcion = input                                                                  (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
                    print                                                                           ( '  │           ╚══════════════════════════════════════════╩════════╝           │')     
                    
                break
                    
            
            case 'F':

                print()
                print()
                
                limpiar_consola()

                print                                                                               ( '        ┌───────────────────────────────────────────────────────────────┐      ')
                print                                                                               ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
                print                                                                               ( '  │     └───────────────────────────────────────────────────────────────┘     │')
                print                                                                               ( '  │                                                                           │')
                print                                                                               ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
                print                                                                               (f'  │       ║        Hola {nombre}, has elegido la opción RAICES          ║        │')
                print                                                                               ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
                print                                                                               ( '  │                                                                           │')
                opcion_F()
                print                                                                               ( '  │ <Volver al Menu> V                                   <Quiero Salir> ENTER │')
                retroceder = input                                                                  ( '  └───────────────────────────────────────────────────────────────────────────┘\n\t\t\t\t\t').upper()
                
                if retroceder == 'V':
                    
                    limpiar_consola()
                    
                    Menu(nombre)
                    
                    print                                                                           ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
                    opcion = input                                                                  (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
                    print                                                                           ( '  │           ╚══════════════════════════════════════════╩════════╝           │')     
                    
                break
                    
            
            case 'G':

                print()
                print()
                
                limpiar_consola()

                print                                                                               ( '        ┌───────────────────────────────────────────────────────────────┐      ')
                print                                                                               ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
                print                                                                               ( '  │     └───────────────────────────────────────────────────────────────┘     │')
                print                                                                               ( '  │                                                                           │')
                print                                                                               ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
                print                                                                               (f'  │       ║        Hola {nombre}, has elegido la opción PARIDAD         ║        │')
                print                                                                               ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
                print                                                                               ( '  │                                                                           │')
                opcion_G()
                print
                print                                                                               ( '  │ <Volver al Menu> V                                   <Quiero Salir> ENTER │')
                retroceder = input                                                                  ( '  └───────────────────────────────────────────────────────────────────────────┘\n\t\t\t\t\t').upper()
                
                if retroceder == 'V':
                    
                    limpiar_consola()
                    
                    Menu(nombre)
                    
                    print                                                                           ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
                    opcion = input                                                                  (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
                    print                                                                           ( '  │           ╚══════════════════════════════════════════╩════════╝           │')     
                    
                break
            
            case 'H':
            
                print()
                print()
                
                limpiar_consola()

                print                                                                               ( '        ┌───────────────────────────────────────────────────────────────┐      ')
                print                                                                               ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
                print                                                                               ( '  │     └───────────────────────────────────────────────────────────────┘     │')
                print                                                                               ( '  │                                                                           │')
                print                                                                               ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
                print                                                                               (f'  │       ║        Hola {nombre}, has elegido la opción PRIMALIDAD         ║        │')
                print                                                                               ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
                print                                                                               ( '  │                                                                           │')
                opcion_H()
                print
                print                                                                               ( '  │ <Volver al Menu> V                                   <Quiero Salir> ENTER │')
                retroceder = input                                                                  ( '  └───────────────────────────────────────────────────────────────────────────┘\n\t\t\t\t\t').upper()
                
                if retroceder == 'V':
                    
                    limpiar_consola()
                    
                    Menu(nombre)
                    
                    print                                                                           ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
                    opcion = input                                                                  (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
                    print                                                                           ( '  │           ╚══════════════════════════════════════════╩════════╝           │')     
                    
                break
            
            case 'I':
                
                print()
                print()
                
                limpiar_consola()

                print                                                                               ( '        ┌───────────────────────────────────────────────────────────────┐      ')
                print                                                                               ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
                print                                                                               ( '  │     └───────────────────────────────────────────────────────────────┘     │')
                print                                                                               ( '  │                                                                           │')
                print                                                                               ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
                print                                                                               (f'  │       ║       Hola {nombre}, has elegido la opción PRIMALIDAD       ║        │')
                print                                                                               ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
                print                                                                               ( '  │                                                                           │')    
                opcion_I()
                print
                print                                                                               ( '  │ <Volver al Menu> V                                   <Quiero Salir> ENTER │')
                retroceder = input                                                                  ( '  └───────────────────────────────────────────────────────────────────────────┘\n\t\t\t\t\t').upper()
                
                if retroceder == 'V':
                    
                    limpiar_consola()
                    
                    Menu(nombre)
                    
                    print                                                                           ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
                    opcion = input                                                                  (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
                    print                                                                           ( '  │           ╚══════════════════════════════════════════╩════════╝           │')     
                    
                break

            case _:
                    
                limpiar_consola()

                print()
                print()

                print                                                                               ( '        ┌───────────────────────────────────────────────────────────────┐      ')
                print                                                                               ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
                print                                                                               ( '  │     └───────────────────────────────────────────────────────────────┘     │')
                print                                                                               ( '  │                                                                           │')
                print                                                                               ( '  │       ╔══════════════╦═══════════════════════════════════════════╗        │')
                print                                                                               ( '  │       ║ ⚠  Error  ⚠  ║  La opción elegida no esta en la lista    ║        │')
                print                                                                               ( '  │       ╠══════════════╩═══════════════════════════════╦═══════════╝        │')
                respuesta = input                                                                   ( '  │       ║      Quiere SALIR (S) o REINTENTAR (R)       ║     ').upper()
                print                                                                               ( '  │       ╚══════════════════════════════════════════════╩═══════════╝        │')
                
                while respuesta != "S" and respuesta != "R":
                    
                    print                                                                           ( '  │                                                                           │')
                    print                                                                           ( '  │       ╔═══════════════╦══════════════════════════════════════════╗        │')
                    print                                                                           ( '  │       ║ ⚠  Error  ⚠   ║  Respuestas que se esperan son S o R     ║        │')
                    print                                                                           ( '  │       ╠═══════════════╩════════════════════════════════╦═════════╝        │')
                    respuesta = input                                                               ( '  │       ║      Quiere SALIR (S) o REINTENTAR (R)         ║     ').upper()
                    print                                                                           ( '  │       ╚════════════════════════════════════════════════╩═════════╝        │')
                        
                else: 

                    if respuesta == "S":
                        
                        print                                                                       ( '  │                                                                           │')
                        print                                                                       ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
                        print                                                                       ( '  │       ║          Gracias por utilizar mi proyecto                ║        │')
                        print                                                                       ( '  │       ║    Presione ENTER para finalizar con el programa         ║        │')
                        print                                                                       ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
                        print                                                                       ( '  └───────────────────────────────────────────────────────────────────────────┘')
                        input()
                        break
                    
                    elif respuesta == "R":
                        
                        limpiar_consola()
                        
                        Menu(nombre)
                        
                        print                                                                       ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
                        opcion = input                                                              (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
                        print                                                                       ( '  │           ╚══════════════════════════════════════════╩════════╝           │')   
                break
    else: 
        
        print (' pasa por aca')