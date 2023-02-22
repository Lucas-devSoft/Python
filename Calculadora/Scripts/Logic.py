import math, os 

def limpiar_consola():
    
    comando = 'clear'
    
    if os.name in ('nt', 'dos'):  # si la maquina esta corriendo en Windows, use cls
    
        comando = 'cls'
    
    else:
        
        comando
    
    os.system(comando)
        

def option_A():
    
    operator = "Addition"

    print                                                   ( '│           ╔════════════════════════════════════╦═════════════╗            │')
    print                                                   (f'│           ║ A ► Addition                       ║     (+)     ║            │')
    print                                                   ( '│           ╠════════════════════════════════════╬═════════════╣            │')
            
    try:
        
        Num1 = int (input                                   ( '│           ║   Insert the first number value    ║   '))
        print                                               ( '│           ╠════════════════════════════════════╬═════════════╣            │')
        Num2 = int (input                                   ( '│           ║   Insert the second number value   ║   '))

        Result = Num1 + Num2
            
        print                                               ( '│           ╠════════════════════════════════════╬═════════════╣            │')
        print                                               (f'│           ║   The result to the Addition is    ║   {Result}         ║            │')
        print                                               ( '│           ╚════════════════════════════════════╩═════════════╝            │')
        print                                               ( '│                                                                           │')
                    
    except ValueError:
            
        print                                               ( '│           ╠════════════════════════════════════╩═════════════╗            │')
        print                                               ( '│           ║  ⚠   Letters are not supported as a value   ⚠    ║            │')
        print                                               ( '│           ╚══════════════════════════════════════════════════╝            │')
    
    return Num1, operator, Num2, Result
    
def option_B():
    
    operator = "Subtract"

    print                                                   ( '│           ╔════════════════════════════════════╦═════════════╗            │')
    print                                                   (f'│           ║ B ► Subtract                       ║     (-)     ║            │')
    print                                                   ( '│           ╠════════════════════════════════════╬═════════════╣            │')
            
    try:
        
        Num1 = int (input                                   ( '│           ║    Insert the first number value   ║   '))
        print                                               ( '│           ╠════════════════════════════════════╬═════════════╣            │')
        Num2 = int (input                                   ( '│           ║    Insert the second number value  ║   '))

        Result = Num1 - Num2
            
        print                                               ( '│           ╠════════════════════════════════════╬═════════════╣            │')
        print                                               (f'│           ║   The result to the Subtract is    ║   {Result}         ║            │')
        print                                               ( '│           ╚════════════════════════════════════╩═════════════╝            │')
        
                    
    except ValueError:
            
        print                                               ( '│           ╠════════════════════════════════════╩═════════════╗            │')
        print                                               ( '│           ║  ⚠   Letters are not supported as a value   ⚠    ║            │')
        print                                               ( '│           ╚══════════════════════════════════════════════════╝            │')
        
    return Num1, operator, Num2, Result    
            
def option_C():
    
    operator = "Multiplication"

    print                                                   ( '│           ╔════════════════════════════════════╦═════════════╗            │')
    print                                                   (f'│           ║ C ► Multiplication                 ║     (*)     ║            │')
    print                                                   ( '│           ║════════════════════════════════════╬═════════════╣            │')
            
    try:
        
        Num1 = int (input                                   ( '│           ║     Insert the first number value  ║   '))
        print                                               ( '│           ╠════════════════════════════════════╬═════════════╣            │')
        Num2 = int (input                                   ( '│           ║     Insert the second number value ║   '))

        Result = Num1 * Num2
            
        print                                               ( '│           ╠════════════════════════════════════╬═════════════╣            │')
        print                                               (f'│           ║ The result to the Multiplication is║   {Result}         ║            │')
        print                                               ( '│           ╚════════════════════════════════════╩═════════════╝            │')
        
                    
    except ValueError:
            
        print                                               ( '│           ╠════════════════════════════════════╩═════════════╗            │')
        print                                               ( '│           ║  ⚠   Letters are not supported as a value   ⚠    ║            │')
        print                                               ( '│           ╚══════════════════════════════════════════════════╝            │')
        
    return Num1, operator, Num2, Result

def option_D():
    
    operator = "Division"

    print                                                   ( '│           ╔════════════════════════════════════╦═════════════╗            │')
    print                                                   (f'│           ║ D ► Division                       ║     (/)     ║            │')
    print                                                   ( '│           ╠════════════════════════════════════╬═════════════╣            │')
        
    try:
            
        Num1 = int (input                                   ( '│           ║     Insert the first number value  ║   '))
        print                                               ( '│           ╠════════════════════════════════════╬═════════════╣            │')
        Num2 = int (input                                   ( '│           ║     Insert the second number value ║   '))
        
        Result = Num1 / Num2
                    
        print                                               ( '│           ╠════════════════════════════════════╬═════════════╣            │')
        print                                               (f'│           ║    The result to the Division is   ║   {Result:.2f}      ║            │')
        print                                               ( '│           ╚════════════════════════════════════╩═════════════╝            │')
        
        
    except ValueError:
        
        print                                               ( '│           ╠════════════════════════════════════╩═════════════╗            │')
        print                                               ( '│           ║  ⚠   Letters are not supported as a value   ⚠   ║            │')
        print                                               ( '│           ╚══════════════════════════════════════════════════╝            │')
        
    except ZeroDivisionError:
    
        print                                               ( '│           ╠════════════════════════════════════╩═════════════╗            │')
        print                                               ( '│           ║   ⚠    You can not division for zero    ⚠       ║            │')
        print                                               ( '│           ╚══════════════════════════════════════════════════╝            │')          

    return Num1, operator, Num2, Result

def option_E():
    
    operator = "Exponentiation"

    print                                                   ( '│           ╔════════════════════════════════════╦═════════════╗            │')
    print                                                   (f'│           ║ E ► Exponentiation                 ║    (b,e)    ║            │')
    print                                                   ( '│           ╠════════════════════════════════════╬═════════════╣            │')
         
    try:   
            
        Num1 = int (input                                   ( '│           ║       Insert the number base       ║   '))
        print                                               ( '│           ╠════════════════════════════════════╬═════════════╣            │')
        Num2 = int (input                                   ( '│           ║       Insert the number exponent   ║   '))
        Result = Num1 ** Num2
            
        print                                               ( '│           ╠════════════════════════════════════╬═════════════╣            │')
        print                                               (f'│           ║The result to the Exponentiation is ║   {Result}        ║            │')
        print                                               ( '│           ╚════════════════════════════════════╩═════════════╝            │')
        
                    
    except ValueError:
            
        print                                               ( '│           ╠════════════════════════════════════╩═════════════╗            │')
        print                                               ( '│           ║  ⚠   Letters are not supported as a value   ⚠   ║            │')
        print                                               ( '│           ╚══════════════════════════════════════════════════╝            │')
    
    return Num1, operator, Num2, Result    

def option_F():
    
    operator = "Radication"

    print                                                   ( '│           ╔════════════════════════════════════╦═════════════╗            │')
    print                                                   (f'│           ║ F ► Radication                     ║     (√)     ║            │')
    print                                                   ( '│           ╠════════════════════════════════════╬═════════════╣            │')
    
    try:
        
        Num1 = int (input                                   ( '│           ║       Insert the number base       ║   '))
        
        if Num1 > 0 :  
            
            print                                           ( '│           ╠════════════════════════════════════╬═════════════╣            │')
            Num2 = int (input                               ( '│           ║        Insert the number index     ║   '))
            Result = math.pow(Num1,1 / Num2)
            
            print                                           ( '│           ╠════════════════════════════════════╬═════════════║            │')
            print                                           (f'│           ║    The result to the Radication is ║   {Result:.2f}      ║            │')
            print                                           ( '│           ╚════════════════════════════════════╩═════════════╝            │')
              
        else:

            print                                           ( '│           ╠════════════════════════════════════╩═════════════╗            │')
            print                                           ( '│           ║ ⚠ Negative number are not supported as a value ⚠║            │')
            print                                           ( '│           ╚══════════════════════════════════════════════════╝            │')
            
            
    except ValueError:
            
        print                                               ( '│           ╠════════════════════════════════════╩═════════════╗            │')
        print                                               ( '│           ║  ⚠   Letters are not supported as a value   ⚠   ║            │')
        print                                               ( '│           ╚══════════════════════════════════════════════════╝            │')
   
    return Num1, operator, Num2, Result     
    
def option_G():
    
    operator = "Even or odd"
    
    print                                                   ( '│           ╔══════════════════════════════════════════════════╗            │')
    print                                                   (f'│           ║ G ► Even or odd                                  ║            │')
    print                                                   ( '│           ╠════════════════════════════════════╦═════════════╣            │')
       
    try:   
            
        Num1 = int (input                                   ( '│           ║     Insert the number to verify    ║     '))
         
        Result = Num1 % int (2)
    
        if Result == 0 :
            
            print                                           ( '│           ╠════════════════════════════════════╩═════════════╣            │')
            print                                           (f'│           ║     The ({Num1}) is inside the even numbers      ║            │')
            print                                           ( '│           ╚══════════════════════════════════════════════════╝            │')
            
            Conclution = "Even"
               
        else:
            
            print                                           ( '│           ╠════════════════════════════════════╩═════════════╣            │')
            print                                           (f'│           ║     The ({Num1}) is inside the odd numbers       ║            │')
            print                                           ( '│           ╚══════════════════════════════════════════════════╝            │')
            
            Conclution = "Odd"
                      
    except ValueError:
            
        print                                               ( '│           ╠════════════════════════════════════╩═════════════╗            │')
        print                                               ( '│           ║  ⚠   Letters are not supported as a value   ⚠   ║            │')
        print                                               ( '│           ╚══════════════════════════════════════════════════╝            │')
     
    return Num1, operator, Conclution
            
def option_H():
    
    Operator = "Is a number prime ?"

    print                                                   ( '│           ╔══════════════════════════════════════════════════╗            │')
    print                                                   (f'│           ║ H ► Is a number prime ?                          ║            │')
    print                                                   ( '│           ╠═════════════════════════════════════════╦════════╣            │')
    
    try :
           
        i=2
        cont = 0
        
        Num1 = int (input                                   ( '│           ║ Insert a number to verify if is a prime ║     '))

        while Num1 > i and cont == 0:
            
            resto = Num1 % i 
            
            if resto == 0:
                
                cont += 1
                
            i+=1
            
        if cont != 0 or Num1 == 1 :
                
            print                                           ( '│           ╠════════════════════════════════════╩═════════════╣            │')
            print                                           (f'│           ║         The ({Num1}) is not a number primes      ║            │')
            print                                           ( '│           ╚══════════════════════════════════════════════════╝            │')
            
            Conclution = "Is not number prime"
            
        else:

            print                                           ( '│           ╠════════════════════════════════════╩═════════════╣            │')
            print                                           (f'│           ║         The ({Num1}) is a number primes          ║            │')
            print                                           ( '│           ╚══════════════════════════════════════════════════╝            │')
            
            Conclution = "Is a number prime"
            
    except ValueError:
        
        print                                               ( '│           ╠════════════════════════════════════╩═════════════╗            │')
        print                                               ( '│           ║  ⚠   Letters are not supported as a value   ⚠   ║            │')
        print                                               ( '│           ╚══════════════════════════════════════════════════╝            │')
        
    return Num1, Operator, Conclution 
       
def option_I():
    
    print                                                   ( '│           ╔══════════════════════════════════════════════════╗            │')
    print                                                   ( '│           ║ I ► Show the number primes by rank               ║            │')
    print                                                   ( '│           ╠════════════════════════════════════╦═════════════╣            │')

    try :
            
        hasta = int (input                                  ( '│           ║        Insert the max range        ║     '))
        print                                               ( '│           ╚════════════════════════════════════╩═════════════╝            │')
        
        primos = []
        
        for num in range (2,hasta+1):
            
            esPrimo = True
            
            if num == 2:
                
                primos.append(num)
            
            else:
                
                i=2
                
                while i < (pow(num,1/2) + 1):
                    
                    resto = num % i
                    
                    if resto == 0:
                    
                        esPrimo = False
                        
                        break
                    
                    i+=1
                
                if esPrimo == True:
                    
                    primos.append(num)

        lugar = 1
        
        print                                               ( '├───────────────────────────────────────────────────────────────────────────┤')
        print                                               ( '|                       GROUP OF NUMBERS PRIMES                             |')
        print                                               ( '├───────────────────────────────────────────────────────────────────────────┤')
        for primo in primos:
            
            if lugar%11 !=0 :
                
                print ('|',f'{primo}'.center(4,' '),end= ' ')
                      
            else:
                
                print (f'|{primo}'.center(5,' '),'|')  
        
            lugar += 1
                                    
    except ValueError:
        
        print                                               ( '│           ╠════════════════════════════════════╩═════════════╗            │')
        print                                               ( '│           ║  ⚠   Letters are not supported as a value   ⚠   ║            │')
        print                                               ( '│           ╚══════════════════════════════════════════════════╝            │')               