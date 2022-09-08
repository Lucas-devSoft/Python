from Funciones import *

print()

print                                                                               ( '        ┌───────────────────────────────────────────────────────────────┐      ')
print                                                                               ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
print                                                                               ( '  │     └───────────────────────────────────────────────────────────────┘     │')
print                                                                               ( '  │                                                                           │')
print                                                                               ( '  │       ╔═════════════════════════════════════════╦════════════════╗        │')
nombre = input                                                                      ( '  │       ║  Bienvenido usuario, Cuál es su nombre? ║     ').capitalize()
print                                                                               ( '  │       ╚═════════════════════════════════════════╩════════════════╝        │')

    
while nombre.isalpha() and len(nombre) >= 4:
        
    limpiar_consola()

    print()

    Menu(nombre) 
        
    print                                                                           ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
    opcion = input                                                                  (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
    print                                                                           ( '  │           ╚══════════════════════════════════════════╩════════╝           │')

    print()

    while True:
        
        match opcion:

            case 'A':
            
                print()
                print()
                
                limpiar_consola()

                print                                                                   ( '        ┌───────────────────────────────────────────────────────────────┐      ')
                print                                                                   ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
                print                                                                   ( '  │     └───────────────────────────────────────────────────────────────┘     │')
                print                                                                   ( '  │                                                                           │')
                print                                                                   ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
                print                                                                   (f'  │       ║        Hola {nombre}, has elegido la opción SUMAR           ║        │')
                print                                                                   ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
                print                     
                opcion_A()
                print                                                                   ( '  │               <Volver Menu> V                  <Salir> ENTER              │')
                retroceder = input                                                      ( '  └───────────────────────────────────────────────────────────────────────────┘\n\t\t\t\t\t').upper()
                
                if retroceder == 'V':
                    
                    limpiar_consola()
                    
                    Menu(nombre)
                    
                    print                                                                           ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
                    opcion = input                                                                  (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
                    print                                                                           ( '  │           ╚══════════════════════════════════════════╩════════╝           │') 
                    print("1")    
                    
                elif retroceder == '' or not (retroceder == 'V'):
                    break                        
                
            case 'B':

                print()
                print()
                
                limpiar_consola()

                print                                                                   ( '        ┌───────────────────────────────────────────────────────────────┐      ')
                print                                                                   ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
                print                                                                   ( '  │     └───────────────────────────────────────────────────────────────┘     │')
                print                                                                   ( '  │                                                                           │')
                print                                                                   ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
                print                                                                   (f'  │       ║        Hola {nombre}, has elegido la opción RESTAR          ║        │')
                print                                                                   ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
                print                                                                   ( '  │                                                                           │')
                opcion_B()
                print                                                                   ( '  │               <Volver Menu> V                  <Salir> ENTER              │')
                retroceder = input                                                      ( '  └───────────────────────────────────────────────────────────────────────────┘\n\t\t\t\t\t').upper()
                
                if retroceder == 'V':
                    
                    limpiar_consola()
                    
                    Menu(nombre)
                    
                    print                                                                           ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
                    opcion = input                                                                  (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
                    print                                                                           ( '  │           ╚══════════════════════════════════════════╩════════╝           │')     
                    
                elif retroceder == '' or not (retroceder == 'V'):
                    break
                    
                    
            case 'C':

                print()
                print()

                limpiar_consola()
                
                print                                                                   ( '        ┌───────────────────────────────────────────────────────────────┐      ')
                print                                                                   ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
                print                                                                   ( '  │     └───────────────────────────────────────────────────────────────┘     │')
                print                                                                   ( '  │                                                                           │')
                print                                                                   ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
                print                                                                   (f'  │       ║        Hola {nombre}, has elegido la opción MULTIPLICAR     ║        │')
                print                                                                   ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
                print                                                                   ( '  │                                                                           │')
                opcion_C()
                print                                                                   ( '  │               <Volver Menu> V                  <Salir> ENTER              │')
                retroceder = input                                                      ( '  └───────────────────────────────────────────────────────────────────────────┘\n\t\t\t\t\t').upper()
                
                if retroceder == 'V':
                    
                    limpiar_consola()
                    
                    Menu(nombre)
                    
                    print                                                                           ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
                    opcion = input                                                                  (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
                    print                                                                           ( '  │           ╚══════════════════════════════════════════╩════════╝           │')     
                    
                elif retroceder == '' or not (retroceder == 'V'):
                    break
                                

            case 'D':

                print()
                print()
                
                limpiar_consola()

                print                                                                   ( '        ┌───────────────────────────────────────────────────────────────┐      ')
                print                                                                   ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
                print                                                                   ( '  │     └───────────────────────────────────────────────────────────────┘     │')
                print                                                                   ( '  │                                                                           │')
                print                                                                   ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
                print                                                                   (f'  │       ║        Hola {nombre}, has elegido la opción DIVIDIR         ║        │')
                print                                                                   ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
                print                                                                   ( '  │                                                                           │')
                opcion_D()
                print                                                                   ( '  │               <Volver Menu> V                  <Salir> ENTER              │')
                retroceder = input                                                      ( '  └───────────────────────────────────────────────────────────────────────────┘\n\t\t\t\t\t').upper()
                
                if retroceder == 'V':
                    
                    limpiar_consola()
                    
                    Menu(nombre)
                    
                    print                                                                           ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
                    opcion = input                                                                  (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
                    print                                                                           ( '  │           ╚══════════════════════════════════════════╩════════╝           │')     
                    
                elif retroceder == '' or not (retroceder == 'V'):
                    break
                    
            
            case 'E':

                print()
                print()
                
                limpiar_consola()

                print                                                                   ( '        ┌───────────────────────────────────────────────────────────────┐      ')
                print                                                                   ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
                print                                                                   ( '  │     └───────────────────────────────────────────────────────────────┘     │')
                print                                                                   ( '  │                                                                           │')
                print                                                                   ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
                print                                                                   (f'  │       ║        Hola {nombre}, has elegido la opción EXPONENTE       ║        │')
                print                                                                   ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
                print                                                                   ( '  │                                                                           │')
                opcion_E()
                print                                                                   ( '  │               <Volver Menu> V                  <Salir> ENTER              │')
                retroceder = input                                                      ( '  └───────────────────────────────────────────────────────────────────────────┘\n\t\t\t\t\t').upper()
                
                if retroceder == 'V':
                    
                    limpiar_consola()
                    
                    Menu(nombre)
                    
                    print                                                                           ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
                    opcion = input                                                                  (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
                    print                                                                           ( '  │           ╚══════════════════════════════════════════╩════════╝           │')     
                    
                elif retroceder == '' or not (retroceder == 'V'):
                    break
                    
            
            case 'F':

                print()
                print()
                
                limpiar_consola()

                print                                                                   ( '        ┌───────────────────────────────────────────────────────────────┐      ')
                print                                                                   ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
                print                                                                   ( '  │     └───────────────────────────────────────────────────────────────┘     │')
                print                                                                   ( '  │                                                                           │')
                print                                                                   ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
                print                                                                   (f'  │       ║        Hola {nombre}, has elegido la opción RAICES          ║        │')
                print                                                                   ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
                print                                                                   ( '  │                                                                           │')
                opcion_F()
                print                                                                   ( '  │               <Volver Menu> V                  <Salir> ENTER              │')
                retroceder = input                                                      ( '  └───────────────────────────────────────────────────────────────────────────┘\n\t\t\t\t\t').upper()
                
                if retroceder == 'V':
                    
                    limpiar_consola()
                    
                    Menu(nombre)
                    
                    print                                                                           ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
                    opcion = input                                                                  (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
                    print                                                                           ( '  │           ╚══════════════════════════════════════════╩════════╝           │')     
                    
                elif retroceder == '' or not (retroceder == 'V'):
                    break
                    
            
            case 'G':

                print()
                print()
                
                limpiar_consola()

                print                                                                   ( '        ┌───────────────────────────────────────────────────────────────┐      ')
                print                                                                   ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
                print                                                                   ( '  │     └───────────────────────────────────────────────────────────────┘     │')
                print                                                                   ( '  │                                                                           │')
                print                                                                   ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
                print                                                                   (f'  │       ║        Hola {nombre}, has elegido la opción PARIDAD         ║        │')
                print                                                                   ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
                print                                                                   ( '  │                                                                           │')
                opcion_G()
                print                                                                   ( '  │               <Volver Menu> V                  <Salir> ENTER              │')
                retroceder = input                                                      ( '  └───────────────────────────────────────────────────────────────────────────┘\n\t\t\t\t\t').upper()
                
                if retroceder == 'V':
                    
                    limpiar_consola()
                    
                    Menu(nombre)
                    
                    print                                                                           ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
                    opcion = input                                                                  (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
                    print                                                                           ( '  │           ╚══════════════════════════════════════════╩════════╝           │')     
                    
                elif retroceder == '' or not (retroceder == 'V'):
                    break
                
            case _:
                
                limpiar_consola()

                print()
                print()

                print                                                                       ( '        ┌───────────────────────────────────────────────────────────────┐      ')
                print                                                                       ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
                print                                                                       ( '  │     └───────────────────────────────────────────────────────────────┘     │')
                print                                                                       ( '  │                                                                           │')
                print                                                                       ( '  │       ╔══════════════╦═══════════════════════════════════════════╗        │')
                print                                                                       ( '  │       ║ ⚠  Error  ⚠  ║  La opción elegida no esta en la lista    ║        │')
                print                                                                       ( '  │       ╠══════════════╩═══════════════════════════════╦═══════════╝        │')
                respuesta = input                                                           ( '  │       ║      Quiere SALIR (S) o REINTENTAR (R)       ║     ').upper()
                print                                                                       ( '  │       ╚══════════════════════════════════════════════╩═══════════╝        │')
                
                while respuesta != "S" and respuesta != "R":
                    
                    print                                                                   ( '  │                                                                           │')
                    print                                                                   ( '  │       ╔═══════════════╦══════════════════════════════════════════╗        │')
                    print                                                                   ( '  │       ║ ⚠  Error  ⚠   ║  Respuestas que se esperan son S o R     ║        │')
                    print                                                                   ( '  │       ╠═══════════════╩════════════════════════════════╦═════════╝        │')
                    respuesta = input                                                       ( '  │       ║      Quiere SALIR (S) o REINTENTAR (R)         ║     ').upper()
                    print                                                                   ( '  │       ╚════════════════════════════════════════════════╩═════════╝        │')
                        
                else: 

                    if respuesta == "S":
                        
                        print                                                               ( '  │                                                                           │')
                        print                                                               ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
                        print                                                               ( '  │       ║          Gracias por utilizar mi proyecto                ║        │')
                        print                                                               ( '  │       ║    Presione ENTER para finalizar con el programa         ║        │')
                        print                                                               ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
                        print                                                               ( '  └───────────────────────────────────────────────────────────────────────────┘')
                        input()
                        break
                    
                    elif respuesta == "R":
                        
                        limpiar_consola()
                        
                        Menu(nombre)
                        
                        print                                                                           ( '  │           ╔══════════════════════════════════════════╦════════╗           │')
                        opcion = input                                                                  (f'  │           ║  {nombre}, Elegi la opción que vas a usar   ║   ').upper()
                        print                                                                           ( '  │           ╚══════════════════════════════════════════╩════════╝           │') 
    break                    
else: 
    
    while nombre.isalnum() or nombre == '' or nombre.isspace() and len(nombre) <= 3:
    
        limpiar_consola()
        
        print                                                                       ( '        ┌───────────────────────────────────────────────────────────────┐      ')
        print                                                                       ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
        print                                                                       ( '  │     └───────────────────────────────────────────────────────────────┘     │')
        print                                                                       ( '  │                                                                           │')
        print                                                                       ( '  │       ╔═══════════════╦══════════════════════════════════════════╗        │')
        print                                                                       ( '  │       ║ ⚠  Error  ⚠   ║  Formato de nombre inválido o vacio.     ║        │')
        print                                                                       ( '  │       ╠═══════════════╩═══════════════════════════════╦══════════╝        │')
        respuesta = input                                                           ( '  │       ║      Quiere SALIR (S) o REINTENTAR (R)        ║     ').upper()
        print                                                                       ( '  │       ╚═══════════════════════════════════════════════╩══════════╝        │')

        while respuesta != "S" and respuesta != "R":
                
            print                                                                       ( '  │                                                                           │')
            print                                                                       ( '  │       ╔═══════════════╦══════════════════════════════════════════╗        │')
            print                                                                       ( '  │       ║ ⚠  Error  ⚠   ║  Respuestas que se esperan son S o R     ║        │')
            print                                                                       ( '  │       ╠═══════════════╩════════════════════════════════╦═════════╝        │')
            respuesta = input                                                           ( '  │       ║      Quiere SALIR (S) o REINTENTAR (R)         ║     ').upper()
            print                                                                       ( '  │       ╚════════════════════════════════════════════════╩═════════╝        │')
                
        else:
                
            if respuesta == "S":
                
                print                                                                   ( '  │                                                                           │')
                print                                                                   ( '  │       ╔══════════════════════════════════════════════════════════╗        │')
                print                                                                   ( '  │       ║          Gracias por utilizar mi proyecto                ║        │')
                print                                                                   ( '  │       ║    Presione ENTER para finalizar con el programa         ║        │')
                print                                                                   ( '  │       ╚══════════════════════════════════════════════════════════╝        │')
                print                                                                   ( '  └───────────────────────────────────────────────────────────────────────────┘')
                input()
                break
                
            if respuesta == "R":
                    
                limpiar_consola()
                
                print()
                print()

                print                                                                   ( '        ┌───────────────────────────────────────────────────────────────┐      ')
                print                                                                   ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
                print                                                                   ( '  │     └───────────────────────────────────────────────────────────────┘     │')
                print                                                                   ( '  │                                                                           │')
                print                                                                   ( '  │       ╔═════════════════════════════════════════╦════════════════╗        │')
                nombre = input                                                          ( '  │       ║   Hola Usuario, ¿ Cuál es su nombre ?   ║      ').capitalize()
                print                                                                   ( '  │       ╚═════════════════════════════════════════╩════════════════╝        │')               
