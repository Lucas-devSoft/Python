import re
from Logic import *
from DataBaseMongo import *

while True:
    
    limpiar_consola()
    print('\n\n')

    print                                                   ( '┌───────────────────────────────────────────────────────────────────────────┐')
    print                                                   ( '│       ╔══════════════════════════════════════════════════════════╗        │')
    print                                                   ( "│       ║        WELCOME USER, ¿ WHAT IS YOUR NAME ?               ║        │")
    print                                                   ( '│       ╚══════════════════════════════════════════════════════════╝        │')
    print                                                   ( '└───────────────────────────────────────────────────────────────────────────┘')

    name = input()

    verification = re.search(r"[0-9]+",name)
        
    if not verification:
        
        while True:
            
            limpiar_consola()
            print('\n\n')
          
            print                                               ( '┌───────────────────────────────────────────────────────────────────────────┐')
            print                                               (f'│        Hello {name.capitalize()}, ¿Do you want to save a history opearations?           │')
            print                                               ( '├─────────────────────────────────────┬─────────────────────────────────────┤')
            print                                               ( '│           Yes, I want  < Y >        │      < N >  NO, I want not          │')
            print                                               ( '└─────────────────────────────────────┴─────────────────────────────────────┘')
            guardar = input                                     ( '\t\t\t\t      ').upper()
            
            if guardar == 'Y':
                
                MongoConnection()
                break
                
            elif guardar == 'N':
                
               break
        
            else:
                
                limpiar_consola()
                print('\n\n')

                print                                               ( '┌───────────────────────────────────────────────────────────────────────────┐')
                print                                               ( '│                                                                           │')
                print                                               ( '│       ╔═════════════════════════════════════════════════════════╗         │')
                print                                               ( '│       ║  ⚠      The Answer waited is < Y > or < N >         ⚠  ║         │')
                print                                               ( '│       ╚═════════════════════════════════════════════════════════╝         │')
                print                                               ( '│                                                                           │')
                print                                               ( '├──────────────────────────────────┬────────────────────────────────────────┤')
                print                                               ( '│    1 - Do you want to try again  │  2 - Do you want to exit the program   │')
                print                                               ( '└──────────────────────────────────┴────────────────────────────────────────┘')
                question = input                                    ( '\t\t\t\t     ')
                 
                while question != "1" and question != "2":
                    
                    print                                           ( '┌───────────────────────────────────────────────────────────────────────────┐')        
                    print                                           ( '│                                                                           │')
                    print                                           ( '│       ╔══════════════════════════════════════════════════════════╗        │')
                    print                                           ( '│       ║    ⚠          The Answer waited is 1 or 2          ⚠    ║        │')
                    print                                           ( '│       ╚══════════════════════════════════════════════════════════╝        │')
                    print                                           ( '├──────────────────────────────────┬────────────────────────────────────────┤')
                    print                                           ( '│    1 - Do you want to try again  │  2 - Do you want to exit the program   │')
                    print                                           ( '└──────────────────────────────────┴────────────────────────────────────────┘')
                    question =      input                           ('\t\t\t\t      ')
                               
                else:
                    
                    if question == "1":
                    
                        continue
                
                    elif question == "2":
                        
                        print                                       ( '│                                                                           │')
                        print                                       ( '│       ╔══════════════════════════════════════════════════════════╗        │')
                        print                                       ( '│       ║      Thank you so much for use my personal project       ║        │')
                        print                                       ( '│       ║         Press ENTER for finish with the program          ║        │')
                        print                                       ( '│       ╚══════════════════════════════════════════════════════════╝        │')
                        input                                       ( '└───────────────────────────────────────────────────────────────────────────┘')
                        
                        exit()  
                    
    else:
        
        limpiar_consola()
        print('\n\n')
        
        print                                               ( '┌───────────────────────────────────────────────────────────────────────────┐')
        print                                               ( '│                                                                           │')
        print                                               ( '│       ╔═════════════════════════════════════════════════════════╗         │')
        print                                               ( '│       ║ ⚠    The format name is invalid or value empty      ⚠  ║         │')
        print                                               ( '│       ╚═════════════════════════════════════════════════════════╝         │')
        print                                               ( '│                                                                           │')
        print                                               ( '├──────────────────────────────────┬────────────────────────────────────────┤')
        print                                               ( '│    1 - Do you want to try again  │  2 - Do you want to exit the program   │')
        print                                               ( '└──────────────────────────────────┴────────────────────────────────────────┘')
        question = input                                    ('\t\t\t\t    ')
        
        while question != "1" and question != "2":
                    
            print                                           ( '┌───────────────────────────────────────────────────────────────────────────┐')        
            print                                           ( '│                                                                           │')
            print                                           ( '│       ╔══════════════════════════════════════════════════════════╗        │')
            print                                           ( '│       ║    ⚠          The Answer waited is 1 or 2          ⚠    ║        │')
            print                                           ( '│       ╚══════════════════════════════════════════════════════════╝        │')
            print                                           ( '├──────────────────────────────────┬────────────────────────────────────────┤')
            print                                           ( '│    1 - Do you want to try again  │  2 - Do you want to exit the program   │')
            print                                           ( '└──────────────────────────────────┴────────────────────────────────────────┘')
            question =      input                           ('\t\t\t\t      ')
            
        else:
                
            if question == "1":
                
                continue
            
            elif question == "2":
                
                print                                       ( '│                                                                           │')
                print                                       ( '│       ╔══════════════════════════════════════════════════════════╗        │')
                print                                       ( '│       ║      Thank you so much for use my personal project       ║        │')
                print                                       ( '│       ║         Press ENTER for finish with the program          ║        │')
                print                                       ( '│       ╚══════════════════════════════════════════════════════════╝        │')
                input                                       ( '└───────────────────────────────────────────────────────────────────────────┘')
                
                exit()  
    
    cont = 0
    
    while True:
              
        limpiar_consola()
        print('\n\n')

        print                                               ( '      ┌───────────────────────────────────────────────────────────────┐      ')
        print                                               ( '┌─────┤             CALCULATOR INTERACTIVE WITH PYTHON                ├─────┐')
        print                                               ( '│     └───────────────────────────────────────────────────────────────┘     │')
        print                                               ( '|                                                                           |')
        print                                               ( '│       ╔═════════════════════════════════════════════════════════╗         │')
        print                                               (f'│       ║        Hello {name.capitalize()}, Welcome to calculator menu          ║         │')
        print                                               ( '│       ╚═════════════════════════════════════════════════════════╝         │')
        print                                               ( '│                                                                           │')
        print                                               ( '│              ╔═══════════════════════════════╦═════════════╗              │')
        print                                               ( '│              ║ A ► Addition                  ║     (+)     ║              │')
        print                                               ( '│              ╠═══════════════════════════════╬═════════════╣              │')
        print                                               ( '│              ║ B ► Subtract                  ║     (-)     ║              │')
        print                                               ( '│              ╠═══════════════════════════════╬═════════════╣              │')
        print                                               ( '│              ║ C ► Multiplication            ║     (*)     ║              │')
        print                                               ( '│              ╠═══════════════════════════════╬═════════════╣              │')
        print                                               ( '│              ║ D ► Division                  ║     (/)     ║              │')
        print                                               ( '│              ╠═══════════════════════════════╬═════════════╣              │')
        print                                               ( '│              ║ E ► Exponentiation            ║    (b,e)    ║              │')
        print                                               ( '│              ╠═══════════════════════════════╬═════════════╣              │')
        print                                               ( '│              ║ F ► Radication                ║     (√)     ║              │')
        print                                               ( '│              ╠═══════════════════════════════╩═════════════╣              │')
        print                                               ( '│              ║ G ► Even and odd                            ║              │')
        print                                               ( '│              ╠═════════════════════════════════════════════╣              │')
        print                                               ( '│              ║ H ► Is a number prime ?                     ║              │')
        print                                               ( '│              ╠═════════════════════════════════════════════╣              │')   
        print                                               ( '│              ║ I ► Show the number primes by rank          ║              │')
        print                                               ( '│              ╚═════════════════════════════════════════════╝              │')         
        print                                               ( '│           ╔═══════════════════════════════════════════════════╗           │')
        print                                               ( '│           ║     Please insert the option you want use         ║           │')
        print                                               ( '│           ╚═══════════════════════════════════════════════════╝           │')
        option = input                                      ('\t\t\t\t      ').upper()  
        
        if option == 'A':            
            
            limpiar_consola()
            print('\n\n')

            print                                           ( '┌───────────────────────────────────────────────────────────────────────────┐')
            print                                           ( '│                                                                           │')
            print                                           ( '│       ╔══════════════════════════════════════════════════════════╗        │')
            print                                           (f'│       ║     Hello {name.capitalize()}, the option you choise is Addition.      ║        │')
            print                                           ( '│       ╚══════════════════════════════════════════════════════════╝        │')                      
            
            return_A = option_A()
            
            cont     = cont+1
            Num1     = return_A[0]
            Operator = return_A[1]
            Num2     = return_A[2]
            Result   = return_A[3]
            
            MongoInsertDB(cont,name,Num1,Operator,Num2,Result)

            print                                           ( '├─────────────────────────────────────┬─────────────────────────────────────┤')
            print                                           ( '│              BACK TO MENU  < M >    │    < E >  EXIT THE PROGRAM          │')
            print                                           ( '└─────────────────────────────────────┴─────────────────────────────────────┘')
            back = input                                    ('\t\t\t\t      ').upper()
            
            if back == 'E':
                
                print                                       ( '│                                                                           │')
                print                                       ( '│       ╔══════════════════════════════════════════════════════════╗        │')
                print                                       ( '│       ║      Thank you so much for use my personal project       ║        │')
                print                                       ( '│       ║         Press ENTER for finish with the program          ║        │')
                print                                       ( '│       ╚══════════════════════════════════════════════════════════╝        │')
                input                                       ( '└───────────────────────────────────────────────────────────────────────────┘')
                
                exit()  
                
            elif back == 'M':
                
                continue

        elif option == 'B':
            
            limpiar_consola()
            print('\n\n')

            print                                           ( '┌───────────────────────────────────────────────────────────────────────────┐')
            print                                           ( '│                                                                           │')
            print                                           ( '│       ╔══════════════════════════════════════════════════════════╗        │')
            print                                           (f'│       ║     Hello {name.capitalize()}, the option you choise is Subtract.      ║        │')
            print                                           ( '│       ╚══════════════════════════════════════════════════════════╝        │')                      
            
            return_B = option_B()
            
            cont     = cont+1
            Num1     = return_B[0]
            Operator = return_B[1]
            Num2     = return_B[2]
            Result   = return_B[3]
            
            MongoInsertDB(cont,name,Num1,Operator,Num2,Result)

            print                                           ( '├─────────────────────────────────────┬─────────────────────────────────────┤')
            print                                           ( '│              BACK TO MENU  < M >    │    < E >  EXIT THE PROGRAM          │')
            print                                           ( '└─────────────────────────────────────┴─────────────────────────────────────┘')
            back = input                                    ('\t\t\t\t      ').upper()
            
            if back == 'E':
                
                print                                       ( '│                                                                           │')
                print                                       ( '│       ╔══════════════════════════════════════════════════════════╗        │')
                print                                       ( '│       ║      Thank you so much for use my personal project       ║        │')
                print                                       ( '│       ║         Press ENTER for finish with the program          ║        │')
                print                                       ( '│       ╚══════════════════════════════════════════════════════════╝        │')
                input                                       ( '└───────────────────────────────────────────────────────────────────────────┘')
                
                exit()  
                
            elif back == 'M':
                
                continue
                    
        elif option == 'C':

            limpiar_consola()
            print('\n\n')

            print                                           ( '┌───────────────────────────────────────────────────────────────────────────┐')
            print                                           ( '│                                                                           │')
            print                                           ( '│       ╔══════════════════════════════════════════════════════════╗        │')
            print                                           (f'│       ║     Hello {name.capitalize()}, the option you choise is Addition.      ║        │')
            print                                           ( '│       ╚══════════════════════════════════════════════════════════╝        │')                      
            
            return_C = option_C()
            
            cont     = cont+1
            Num1     = return_C[0]
            Operator = return_C[1]
            Num2     = return_C[2]
            Result   = return_C[3]
            
            MongoInsertDB(cont,name,Num1,Operator,Num2,Result)

            print                                           ( '├─────────────────────────────────────┬─────────────────────────────────────┤')
            print                                           ( '│              BACK TO MENU  < M >    │    < E >  EXIT THE PROGRAM          │')
            print                                           ( '└─────────────────────────────────────┴─────────────────────────────────────┘')
            back = input                                    ('\t\t\t\t      ').upper()
            
            if back == 'E':
                
                print                                       ( '│                                                                           │')
                print                                       ( '│       ╔══════════════════════════════════════════════════════════╗        │')
                print                                       ( '│       ║      Thank you so much for use my personal project       ║        │')
                print                                       ( '│       ║         Press ENTER for finish with the program          ║        │')
                print                                       ( '│       ╚══════════════════════════════════════════════════════════╝        │')
                input                                       ( '└───────────────────────────────────────────────────────────────────────────┘')
                
                exit()  
                
            elif back == 'M':
                
                continue 
                
        elif option == 'D':
            
            cont+1
                
            limpiar_consola()
            print('\n\n')

            print                                           ( '┌───────────────────────────────────────────────────────────────────────────┐')
            print                                           ( '│                                                                           │')
            print                                           ( '│       ╔══════════════════════════════════════════════════════════╗        │')
            print                                           (f'│       ║     Hello {name.capitalize()}, the option you choise is Addition.      ║        │')
            print                                           ( '│       ╚══════════════════════════════════════════════════════════╝        │')                      
            
            return_D = option_D()
            
            cont     = cont+1
            Num1     = return_D[0]
            Operator = return_D[1]
            Num2     = return_D[2]
            Result   = return_D[3]
            
            MongoInsertDB(cont,name,Num1,Operator,Num2,Result)

            print                                           ( '├─────────────────────────────────────┬─────────────────────────────────────┤')
            print                                           ( '│              BACK TO MENU  < M >    │    < E >  EXIT THE PROGRAM          │')
            print                                           ( '└─────────────────────────────────────┴─────────────────────────────────────┘')
            back = input                                    ('\t\t\t\t      ').upper()
            
            if back == 'E':
                
                print                                       ( '│                                                                           │')
                print                                       ( '│       ╔══════════════════════════════════════════════════════════╗        │')
                print                                       ( '│       ║      Thank you so much for use my personal project       ║        │')
                print                                       ( '│       ║         Press ENTER for finish with the program          ║        │')
                print                                       ( '│       ╚══════════════════════════════════════════════════════════╝        │')
                input                                       ( '└───────────────────────────────────────────────────────────────────────────┘')
                
                exit()  
                
            elif back == 'M':
                
                continue
                
        elif option == 'E':
                
            limpiar_consola()
            print('\n\n')

            print                                           ( '┌───────────────────────────────────────────────────────────────────────────┐')
            print                                           ( '│                                                                           │')
            print                                           ( '│       ╔══════════════════════════════════════════════════════════╗        │')
            print                                           (f'│       ║     Hello {name.capitalize()}, the option you choise is Addition.      ║        │')
            print                                           ( '│       ╚══════════════════════════════════════════════════════════╝        │')                      
            
            return_E = option_E()
            
            cont     = cont+1
            Num1     = return_E[0]
            Operator = return_E[1]
            Num2     = return_E[2]
            Result   = return_E[3]
            
            MongoInsertDB(cont,name,Num1,Operator,Num2,Result)

            print                                           ( '├─────────────────────────────────────┬─────────────────────────────────────┤')
            print                                           ( '│              BACK TO MENU  < M >    │    < E >  EXIT THE PROGRAM          │')
            print                                           ( '└─────────────────────────────────────┴─────────────────────────────────────┘')
            back = input                                    ('\t\t\t\t      ').upper()
            
            if back == 'E':
                
                print                                       ( '│                                                                           │')
                print                                       ( '│       ╔══════════════════════════════════════════════════════════╗        │')
                print                                       ( '│       ║      Thank you so much for use my personal project       ║        │')
                print                                       ( '│       ║         Press ENTER for finish with the program          ║        │')
                print                                       ( '│       ╚══════════════════════════════════════════════════════════╝        │')
                input                                       ( '└───────────────────────────────────────────────────────────────────────────┘')
                
                exit()  
                
            elif back == 'M':
                
                continue
                
        elif option == 'F':
            
            cont+1

            limpiar_consola()
            print('\n\n')

            print                                           ( '┌───────────────────────────────────────────────────────────────────────────┐')
            print                                           ( '│                                                                           │')
            print                                           ( '│       ╔══════════════════════════════════════════════════════════╗        │')
            print                                           (f'│       ║     Hello {name.capitalize()}, the option you choise is Addition.      ║        │')
            print                                           ( '│       ╚══════════════════════════════════════════════════════════╝        │')                      
            
            return_F = option_F()
            
            cont     = cont+1
            Num1     = return_F[0]
            Operator = return_F[1]
            Num2     = return_F[2]
            Result   = return_F[3]
            
            MongoInsertDB(cont,name,Num1,Operator,Num2,Result)

            print                                           ( '├─────────────────────────────────────┬─────────────────────────────────────┤')
            print                                           ( '│              BACK TO MENU  < M >    │    < E >  EXIT THE PROGRAM          │')
            print                                           ( '└─────────────────────────────────────┴─────────────────────────────────────┘')
            back = input                                    ('\t\t\t\t      ').upper()
            
            if back == 'E':
                
                print                                       ( '│                                                                           │')
                print                                       ( '│       ╔══════════════════════════════════════════════════════════╗        │')
                print                                       ( '│       ║      Thank you so much for use my personal project       ║        │')
                print                                       ( '│       ║         Press ENTER for finish with the program          ║        │')
                print                                       ( '│       ╚══════════════════════════════════════════════════════════╝        │')
                input                                       ( '└───────────────────────────────────────────────────────────────────────────┘')
                
                exit()  
                
            elif back == 'M':
                
                continue
                
        elif option == 'G':

            limpiar_consola()
            print('\n\n')

            print                                           ( '┌───────────────────────────────────────────────────────────────────────────┐')
            print                                           ( '│                                                                           │')
            print                                           ( '│       ╔══════════════════════════════════════════════════════════╗        │')
            print                                           (f'│       ║     Hello {name.capitalize()}, the option you choise is Addition.      ║        │')
            print                                           ( '│       ╚══════════════════════════════════════════════════════════╝        │')                      
            
            return_G = option_G()
            
            cont           = cont+1
            Num1           = return_F[0]
            Operator       = return_F[1]
            conclution     = return_F[2]
            
            MongoInsertDB(cont,name,Num1,Operator,conclution)

            print                                           ( '├─────────────────────────────────────┬─────────────────────────────────────┤')
            print                                           ( '│              BACK TO MENU  < M >    │    < E >  EXIT THE PROGRAM          │')
            print                                           ( '└─────────────────────────────────────┴─────────────────────────────────────┘')
            back = input                                    ('\t\t\t\t      ').upper()
            
            if back == 'E':
                
                print                                       ( '│                                                                           │')
                print                                       ( '│       ╔══════════════════════════════════════════════════════════╗        │')
                print                                       ( '│       ║      Thank you so much for use my personal project       ║        │')
                print                                       ( '│       ║         Press ENTER for finish with the program          ║        │')
                print                                       ( '│       ╚══════════════════════════════════════════════════════════╝        │')
                input                                       ( '└───────────────────────────────────────────────────────────────────────────┘')
                
                exit()  
                
            elif back == 'M':
                
                continue
                        
        elif option == 'H':
                
            limpiar_consola()
            print('\n\n')

            print                                           ( '┌───────────────────────────────────────────────────────────────────────────┐')
            print                                           ( '│                                                                           │')
            print                                           ( '│       ╔══════════════════════════════════════════════════════════╗        │')
            print                                           (f'│       ║     Hello {name.capitalize()}, the option you choise is Addition.      ║        │')
            print                                           ( '│       ╚══════════════════════════════════════════════════════════╝        │')                      
            
            return_H = option_H()
            
            cont           = cont+1
            Num1           = return_F[0]
            Operator       = return_F[1]
            conclution     = return_F[2]
            
            MongoInsertDB(cont,name,Num1,Operator,conclution)

            print                                           ( '├─────────────────────────────────────┬─────────────────────────────────────┤')
            print                                           ( '│              BACK TO MENU  < M >    │    < E >  EXIT THE PROGRAM          │')
            print                                           ( '└─────────────────────────────────────┴─────────────────────────────────────┘')
            back = input                                    ('\t\t\t\t      ').upper()
            
            if back == 'E':
                
                print                                       ( '│                                                                           │')
                print                                       ( '│       ╔══════════════════════════════════════════════════════════╗        │')
                print                                       ( '│       ║      Thank you so much for use my personal project       ║        │')
                print                                       ( '│       ║         Press ENTER for finish with the program          ║        │')
                print                                       ( '│       ╚══════════════════════════════════════════════════════════╝        │')
                input                                       ( '└───────────────────────────────────────────────────────────────────────────┘')
                
                exit()  
                
            elif back == 'M':
                
                continue
                
        elif option == 'I':
                    
            limpiar_consola()
            print('\n\n')

            print                                           ( '┌───────────────────────────────────────────────────────────────────────────┐')
            print                                           ( '│                                                                           │')
            print                                           ( '│       ╔══════════════════════════════════════════════════════════╗        │')
            print                                           (f'│       ║     Hello {name.capitalize()}, the option you choise is Addition.      ║        │')
            print                                           ( '│       ╚══════════════════════════════════════════════════════════╝        │')                      
            
            option_I()

            print                                           ( '├─────────────────────────────────────┬─────────────────────────────────────┤')
            print                                           ( '│              BACK TO MENU  < M >    │    < E >  EXIT THE PROGRAM          │')
            print                                           ( '└─────────────────────────────────────┴─────────────────────────────────────┘')
            back = input                                    ('\t\t\t\t      ').upper()
            
            if back == 'E':
                
                print                                       ( '│                                                                           │')
                print                                       ( '│       ╔══════════════════════════════════════════════════════════╗        │')
                print                                       ( '│       ║      Thank you so much for use my personal project       ║        │')
                print                                       ( '│       ║         Press ENTER for finish with the program          ║        │')
                print                                       ( '│       ╚══════════════════════════════════════════════════════════╝        │')
                input                                       ( '└───────────────────────────────────────────────────────────────────────────┘')
                
                exit()  
                
            elif back == 'M':
                
                continue
                
        else: 
                    
            limpiar_consola()
            print('\n\n')

            print                                       ( '┌───────────────────────────────────────────────────────────────────────────┐')
            print                                       ( '│                                                                           │')
            print                                       ( '│       ╔══════════════════════════════════════════════════════════╗        │')
            print                                       ( '│       ║      ⚠   The option choise is not in the Menu    ⚠       ║        │')
            print                                       ( '│       ╚══════════════════════════════════════════════════════════╝        │')
            print                                       ( '├──────────────────────────────────┬────────────────────────────────────────┤')
            print                                       ( '│    1 - Do you want to try again  │  2 - Do you want to exit the program   │')
            print                                       ( '└──────────────────────────────────┴────────────────────────────────────────┘')
            question =      input                       ('\t\t\t\t     ')

            while question != "1" and question != "2":
                
                print                                   ( '┌───────────────────────────────────────────────────────────────────────────┐')        
                print                                   ( '│                                                                           │')
                print                                   ( '│       ╔══════════════════════════════════════════════════════════╗        │')
                print                                   ( '│       ║    ⚠          The Answer waited is 1 or 2          ⚠    ║        │')
                print                                   ( '│       ╚══════════════════════════════════════════════════════════╝        │')
                print                                   ( '├──────────────────────────────────┬────────────────────────────────────────┤')
                print                                   ( '│    1 - Do you want to try again  │  2 - Do you want to exit the program   │')
                print                                   ( '└──────────────────────────────────┴────────────────────────────────────────┘')
                question =      input                   ('\t\t\t\t     ')
                
            else:
                        
                if question == "1":
                    
                    continue
                
                elif question == "2":
                    
                    print                                       ( '│                                                                           │')
                    print                                       ( '│       ╔══════════════════════════════════════════════════════════╗        │')
                    print                                       ( '│       ║      Thank you so much for use my personal project       ║        │')
                    print                                       ( '│       ║         Press ENTER for finish with the program          ║        │')
                    print                                       ( '│       ╚══════════════════════════════════════════════════════════╝        │')
                    input                                       ( '└───────────────────────────────────────────────────────────────────────────┘')
                    
                    exit()  
                     
                
    break
                