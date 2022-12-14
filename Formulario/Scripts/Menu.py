from Logica import *

global estado_A,estado_B,estado_C,Finalizado

estado_A ='INCOMPLETO'
estado_B ='INCOMPLETO'
estado_C ='INCOMPLETO'

while True:
    
    print('\n\n')
    
    limpiar_consola()
    
    print                                                                   ( '              ┌───────────────────────────────────────────────────────────────┐      ')
    print                                                                   ( '        ┌─────┤  DESARROLLADO CON EL LENGUAJE DE PYTHON POR LUCAS E. SANCHEZ  ├─────┐')
    print                                                                   ( '        │     └───────────────────────────────────────────────────────────────┘     │')
    print                                                                   ( '        │              ╔═════════════════════════════════════════════╗              │')
    print                                                                   ( '        │              ║   FORMULARIO CON SALIDA DE DATOS A JSON     ║              │')
    print                                                                   ( '        │              ╚═════════════════════════════════════════════╝              │')
    print                                                                   ( '        │                                                                           │')
    print                                                                   ( '        │            ╔════════════════════════════════════╦════════════╗            │')
    print                                                                   (f'        │            ║ A ► FORMULARIO DE DATOS PERSONALES ║ {estado_A} ║            │')
    print                                                                   ( '        │            ╠════════════════════════════════════╬════════════╣            │')
    print                                                                   (f'        │            ║ B ► FORMULARIO DE DATOS LABORALES  ║ {estado_B} ║            │')
    print                                                                   ( '        │            ╠════════════════════════════════════╬════════════╣            │')
    print                                                                   (f'        │            ║ C ► FORMULARIO DE DATOS ACADEMICOS ║ {estado_C} ║            │')
    print                                                                   ( '        │            ╚════════════════════════════════════╩════════════╝            │')
    print                                                                   ( '        |                                                                           |')

    print                                                                   ( '        │              ╔═════════════════════════════════════════════╗              │')
    opcion = input                                                          ( '        │              ║  ELIJA LA OPCION QUE VA A COMPLETAR :   ').upper()
    print                                                                   ( '        │              ╚═════════════════════════════════════════════╝              │')


    while opcion != 'A' and opcion != 'B' and opcion != 'C':

        limpiar_consola()

        print('\n\n') 

        print                                                               ( '              ┌───────────────────────────────────────────────────────────────┐      ')
        print                                                               ( '        ┌─────┤  DESARROLLADO CON EL LENGUAJE DE PYTHON POR LUCAS E. SANCHEZ  ├─────┐')
        print                                                               ( '        │     └───────────────────────────────────────────────────────────────┘     │')
        print                                                               ( '        │                                                                           │')
        print                                                               ( '        │              ╔═════════════════════════════════════════════╗              │')
        print                                                               ( '        │              ║   LA OPCION ELEGIDA NO ESTA EN LA LISTA     ║              │')
        print                                                               ( '        │              ╠════════════════════════╦════════════════════╣              │')
        print                                                               ( '        │              ║        SALIR  < S >    ║  < R > REINTENTAR  ║              |')
        respuesta = input                                                   ( '        │              ╚════════════════════════╩════════════════════╝              │\n\t\t\t\t\t\t').upper()

        while respuesta != 'S' and respuesta != 'R':
            
            print                                                           ( '        │              ╔═════════════════════════════════════════════╗              │')
            print                                                           ( '        │              ║  RESPUESTA INVALIDA SE ESPERA < S > O < R > ║              │')
            print                                                           ( '        │              ╠════════════════════════╦════════════════════╣              │')
            print                                                           ( '        │              ║        SALIR  < S >    ║  < R > REINTENTAR  ║              |')
            respuesta = input                                               ( '        │              ╚════════════════════════╩════════════════════╝              │\n\t\t\t\t\t\t').upper()
            
        else:
                    
            if respuesta == 'S':
                
                print                                                       ( '        ┌───────────────────────────────────────────────────────────────────────────┐')
                print                                                       ( '        │       ╔══════════════════════════════════════════════════════════╗        │')
                print                                                       ( '        │       ║          GRACIAS POR UTILIZAR MI PROYECTO                ║        │')
                print                                                       ( '        │       ║    PRESIONE ENTER PARA FINALIZAR CON EL PROGRAMA.        ║        │')
                print                                                       ( '        │       ╚══════════════════════════════════════════════════════════╝        │')
                input                                                       ( '        └───────────────────────────────────────────────────────────────────────────┘')
                
                exit() 

            elif respuesta == 'R':

                limpiar_consola()

                print('\n\n') 

                Menu(estado_A,estado_B,estado_C)
                
                print                                                       ( '        │              ╔═════════════════════════════════════════════╗              │')
                opcion = input                                              ( '        │              ║  ELIJA LA OPCION QUE VA A COMPLETAR :   ').upper()
                print                                                       ( '        │              ╚═════════════════════════════════════════════╝              │')
        
    while opcion == 'A' and estado_A == 'INCOMPLETO' and (not estado_A == 'COMPLETADO') or opcion == 'B' and estado_B == 'INCOMPLETO' and (not estado_B == 'COMPLETADO') or opcion == 'C' and estado_C == 'INCOMPLETO' and (not estado_C == 'COMPLETADO'):
        
        Finalizado = False
        
        if opcion == 'A':
            
            resultado_A = opcion_A(Finalizado)
            
            match resultado_A:
                
                case True:
                    
                    print                                                   ( '        │              ╚══════════════════════════════════════════════╝             │')
                    print                                                   ( '        ├───────────────────────────────────────────────────────────────────────────┤')
                    print                                                   ( '        │               El Formulario fue completado Exitosamente!                  │')
                    print                                                   ( '        ├─────────────────────────────────────┬─────────────────────────────────────┤')
                    print                                                   ( '        │            VOLVER AL MENU  < M >    │    < S >  SALIR DEL PROGRAMA        │')
                    retroceder = input                                      ( '        └─────────────────────────────────────┴─────────────────────────────────────┘\n\t\t\t\t\t      ').upper()
                    
                    if retroceder == 'M':
                        
                        limpiar_consola()

                        print('\n\n')

                        estado_A = 'COMPLETADO'
                        
                        Menu(estado_A,estado_B,estado_C)
                        
                        print                                               ( '        │              ╔═════════════════════════════════════════════╗              │')
                        opcion = input                                      ( '        │              ║  ELIJA LA OPCION QUE VA A COMPLETAR :   ').upper()
                        print                                               ( '        │              ╚═════════════════════════════════════════════╝              │')
                    
                    elif retroceder == 'S':
                        
                        print                                               ( '        ┌───────────────────────────────────────────────────────────────────────────┐')
                        print                                               ( '        │       ╔══════════════════════════════════════════════════════════╗        │')
                        print                                               ( '        │       ║          GRACIAS POR UTILIZAR MI PROYECTO                ║        │')
                        print                                               ( '        │       ║    PRESIONE ENTER PARA FINALIZAR CON EL PROGRAMA.        ║        │')
                        print                                               ( '        │       ╚══════════════════════════════════════════════════════════╝        │')
                        input                                               ( '        └───────────────────────────────────────────────────────────────────────────┘')
                        
                        exit()
                    
                case False:
                    
                    print                                                   ( '        │              ╚══════════════════════════════════════════════╝             │')
                    print                                                   ( '        ├───────────────────────────────────────────────────────────────────────────┤')
                    print                                                   ( '        │         Formulario interrumpido por brindar informacion erronea !         │')
                    print                                                   ( '        ├─────────────────────────────────────┬─────────────────────────────────────┤')
                    print                                                   ( '        │         VOLVER A INTENTAR  < R >    │    < S >  SALIR DEL PROGRAMA        │')
                    retroceder = input                                      ( '        └─────────────────────────────────────┴─────────────────────────────────────┘\n\t\t\t\t\t      ').upper()

                    if retroceder == 'R':
                        
                        limpiar_consola()

                        print('\n\n')

                        estado_A = 'INCOMPLETO'    
                        
                        Menu(estado_A,estado_B,estado_C)
                        
                        print                                               ( '        │              ╔═════════════════════════════════════════════╗              │')
                        opcion = input                                      ( '        │              ║  ELIJA LA OPCION QUE VA A COMPLETAR :   ').upper()
                        print                                               ( '        │              ╚═════════════════════════════════════════════╝              │')
                        
                    elif retroceder == 'S':
                        
                        print                                               ( '        ┌───────────────────────────────────────────────────────────────────────────┐')
                        print                                               ( '        │       ╔══════════════════════════════════════════════════════════╗        │')
                        print                                               ( '        │       ║          GRACIAS POR UTILIZAR MI PROYECTO                ║        │')
                        print                                               ( '        │       ║    PRESIONE ENTER PARA FINALIZAR CON EL PROGRAMA.        ║        │')
                        print                                               ( '        │       ╚══════════════════════════════════════════════════════════╝        │')
                        input                                               ( '        └───────────────────────────────────────────────────────────────────────────┘')
                        
                        exit()      
        
       
                        
        if opcion == 'B':

            resultado_B = opcion_B(Finalizado)
            
            match resultado_B:
                
                case True:
                    
                    print                                                   ( '        │              ╚══════════════════════════════════════════════╝             │')
                    print                                                   ( '        ├───────────────────────────────────────────────────────────────────────────┤')
                    print                                                   ( '        │               El Formulario fue completado Exitosamente!                  │')
                    print                                                   ( '        ├─────────────────────────────────────┬─────────────────────────────────────┤')
                    print                                                   ( '        │            VOLVER AL MENU  < M >    │    < S >  SALIR DEL PROGRAMA        │')
                    retroceder = input                                      ( '        └─────────────────────────────────────┴─────────────────────────────────────┘\n\t\t\t\t\t      ').upper()
                    
                    if retroceder == 'M':
                        
                        limpiar_consola()

                        print('\n\n')

                        estado_B = 'COMPLETADO'
                        
                        Menu(estado_A,estado_B,estado_C)
                        
                        print                                               ( '        │              ╔═════════════════════════════════════════════╗              │')
                        opcion = input                                      ( '        │              ║  ELIJA LA OPCION QUE VA A COMPLETAR :   ').upper()
                        print                                               ( '        │              ╚═════════════════════════════════════════════╝              │')
                    
                    elif retroceder == 'S':
                    
                        print                                               ( '        ┌───────────────────────────────────────────────────────────────────────────┐')
                        print                                               ( '        │       ╔══════════════════════════════════════════════════════════╗        │')
                        print                                               ( '        │       ║          GRACIAS POR UTILIZAR MI PROYECTO                ║        │')
                        print                                               ( '        │       ║    PRESIONE ENTER PARA FINALIZAR CON EL PROGRAMA.        ║        │')
                        print                                               ( '        │       ╚══════════════════════════════════════════════════════════╝        │')
                        input                                               ( '        └───────────────────────────────────────────────────────────────────────────┘')
                        
                        exit()      
                    
                case False:
                    
                    print                                                   ( '        │              ╚══════════════════════════════════════════════╝             │')
                    print                                                   ( '        ├───────────────────────────────────────────────────────────────────────────┤') 
                    print                                                   ( '        │         Formulario interrumpido por brindar informacion erronea !         │')
                    print                                                   ( '        ├─────────────────────────────────────┬─────────────────────────────────────┤')
                    print                                                   ( '        │         VOLVER A INTENTAR  < R >    │    < S >  SALIR DEL PROGRAMA        │')
                    retroceder = input                                      ( '        └─────────────────────────────────────┴─────────────────────────────────────┘\n\t\t\t\t\t      ').upper()

                    if retroceder == 'R':
                        
                        limpiar_consola()

                        print('\n\n')

                        estado_B = 'INCOMPLETO'
                        
                        Menu(estado_A,estado_B,estado_C)
                        
                        print                                               ( '        │              ╔═════════════════════════════════════════════╗              │')
                        opcion = input                                      ( '        │              ║  ELIJA LA OPCION QUE VA A COMPLETAR :   ').upper()
                        print                                               ( '        │              ╚═════════════════════════════════════════════╝              │')
                        
                    elif retroceder == 'S':
                        
                        print                                               ( '        ┌───────────────────────────────────────────────────────────────────────────┐')
                        print                                               ( '        │       ╔══════════════════════════════════════════════════════════╗        │')
                        print                                               ( '        │       ║          GRACIAS POR UTILIZAR MI PROYECTO                ║        │')
                        print                                               ( '        │       ║    PRESIONE ENTER PARA FINALIZAR CON EL PROGRAMA.        ║        │')
                        print                                               ( '        │       ╚══════════════════════════════════════════════════════════╝        │')
                        input                                               ( '        └───────────────────────────────────────────────────────────────────────────┘')
                        
                        exit()            
            
        
        elif opcion == 'C' :

            resultado_C = opcion_C(Finalizado)
            
            match resultado_C:
                
                case True:
                    
                    print                                                   ( '        │              ╚══════════════════════════════════════════════╝             │')
                    print                                                   ( '        ├───────────────────────────────────────────────────────────────────────────┤')
                    print                                                   ( '        │               El Formulario fue completado Exitosamente!                  │')
                    print                                                   ( '        ├─────────────────────────────────────┬─────────────────────────────────────┤')
                    print                                                   ( '        │            VOLVER AL MENU  < M >    │    < S >  SALIR DEL PROGRAMA        │')
                    retroceder = input                                      ( '        └─────────────────────────────────────┴─────────────────────────────────────┘\n\t\t\t\t\t      ').upper()
                    
                    if retroceder == 'M':
                        
                        limpiar_consola()

                        print('\n\n')

                        estado_C = 'COMPLETADO'
                        
                        Menu(estado_A,estado_B,estado_C)
                        
                        print                                               ( '        │              ╔═════════════════════════════════════════════╗              │')
                        opcion = input                                      ( '        │              ║  ELIJA LA OPCION QUE VA A COMPLETAR :   ').upper()
                        print                                               ( '        │              ╚═════════════════════════════════════════════╝              │')
                    
                    elif retroceder == 'S':
                    
                        print                                               ( '        ┌───────────────────────────────────────────────────────────────────────────┐')
                        print                                               ( '        │       ╔══════════════════════════════════════════════════════════╗        │')
                        print                                               ( '        │       ║          GRACIAS POR UTILIZAR MI PROYECTO                ║        │')
                        print                                               ( '        │       ║    PRESIONE ENTER PARA FINALIZAR CON EL PROGRAMA.        ║        │')
                        print                                               ( '        │       ╚══════════════════════════════════════════════════════════╝        │')
                        input                                               ( '        └───────────────────────────────────────────────────────────────────────────┘')
                        
                        exit()      
                    
                case False:
                    
                    print                                                   ( '        │              ╚══════════════════════════════════════════════╝             │')
                    print                                                   ( '        ├───────────────────────────────────────────────────────────────────────────┤')
                    print                                                   ( '        │         Formulario interrumpido por brindar informacion erronea !         │')
                    print                                                   ( '        ├─────────────────────────────────────┬─────────────────────────────────────┤')
                    print                                                   ( '        │         VOLVER A INTENTAR  < R >    │    < S >  SALIR DEL PROGRAMA        │')
                    retroceder = input                                      ( '        └─────────────────────────────────────┴─────────────────────────────────────┘\n\t\t\t\t\t      ').upper()

                    if retroceder == 'R':
                        
                        limpiar_consola()

                        print('\n\n')

                        estado_C = 'INCOMPLETO'
                        
                        Menu(estado_A,estado_B,estado_C)
                        
                        print                                               ( '        │              ╔═════════════════════════════════════════════╗              │')
                        opcion = input                                      ( '        │              ║  ELIJA LA OPCION QUE VA A COMPLETAR :   ').upper()
                        print                                               ( '        │              ╚═════════════════════════════════════════════╝              │')
                        
                    elif retroceder == 'S':
                        
                        print                                               ( '        ┌───────────────────────────────────────────────────────────────────────────┐')
                        print                                               ( '        │       ╔══════════════════════════════════════════════════════════╗        │')
                        print                                               ( '        │       ║          GRACIAS POR UTILIZAR MI PROYECTO                ║        │')
                        print                                               ( '        │       ║    PRESIONE ENTER PARA FINALIZAR CON EL PROGRAMA.        ║        │')
                        print                                               ( '        │       ╚══════════════════════════════════════════════════════════╝        │')
                        input                                               ( '        └───────────────────────────────────────────────────────────────────────────┘')
                        
                        exit()            
            
    else:
        
        if estado_A == 'COMPLETADO' or estado_B == 'COMPLETADO' or estado_C == 'COMPLETADO':
        
            print                                                               ( '        ├───────────────────────────────────────────────────────────────────────────┤')
            print                                                               (f'        |               EL formulario {opcion}, ya a sido completado                       |')
            print                                                               ( '        └───────────────────────────────────────────────────────────────────────────┘')
            input()
        
    while estado_A == 'COMPLETADO' and estado_B == 'COMPLETADO' and estado_C == 'COMPLETADO':
        
        limpiar_consola()

        print('\n\n')
        
        Menu(estado_A,estado_B,estado_C)
        
        print                                                   ( '        ├───────────────────────────────────────────────────────────────────────────┤')
        print                                                   ( '        │    Felicitaciones todos los datos del formulario han sido completados!    │')
        print                                                   ( '        ├─────────────────────────────────────┬─────────────────────────────────────┤')
        print                                                   ( '        │        LIMPIAR FORMULARIO  < L >    │    < S >  SALIR DEL PROGRAMA        │')
        resetear = input                                        ( '        └─────────────────────────────────────┴─────────────────────────────────────┘\n\t\t\t\t\t      ').upper()
        
        if resetear == 'L' or resetear == 'S':
            
            if resetear == 'L':
                
                estado_A = 'INCOMPLETO'
                estado_B = 'INCOMPLETO'
                estado_C = 'INCOMPLETO'
            
            elif resetear == 'S':
                
                print                                               ( '        ┌───────────────────────────────────────────────────────────────────────────┐')
                print                                               ( '        │       ╔══════════════════════════════════════════════════════════╗        │')
                print                                               ( '        │       ║          GRACIAS POR UTILIZAR MI PROYECTO                ║        │')
                print                                               ( '        │       ║    PRESIONE ENTER PARA FINALIZAR CON EL PROGRAMA.        ║        │')
                print                                               ( '        │       ╚══════════════════════════════════════════════════════════╝        │')
                input                                               ( '        └───────────────────────────────────────────────────────────────────────────┘')
                
                exit()      
        
        else:
        
            Msg_error_reseteo(resetear)    