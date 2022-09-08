import math, os

def limpiar_consola():
    comando = 'clear'
    if os.name in ('nt', 'dos'):  # si la maquina esta corriendo en Windows, use cls
        comando = 'cls'
    os.system(comando)

def Menu(nombre):
    
    print                                                                           ( '        ┌───────────────────────────────────────────────────────────────┐      ')
    print                                                                           ( '  ┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
    print                                                                           ( '  │     └───────────────────────────────────────────────────────────────┘     │')
    print                                                                           ( '  │                                                                           │')
    print                                                                           ( '  │       ╔═════════════════════════════════════════════════════════╗         │')
    print                                                                           (f'  │       ║   Hola {nombre}, Bienvenido/a a mi Proyecto Personal       ║         │')
    print                                                                           ( '  │       ╚═════════════════════════════════════════════════════════╝         │')
    print                                                                           ( '  │                                                                           │')
    print                                                                           ( '  │              ╔═════════════════════════════════════════════╗              │')
    print                                                                           ( '  │              ║        Calculadora interactiva Python       ║              │')
    print                                                                           ( '  │              ╠═══════════════════════════════╦═════════════╣              │')
    print                                                                           ( '  │              ║  A ► Adición             (+)  ║   SUMAR     ║              │')
    print                                                                           ( '  │              ║═══════════════════════════════╬═════════════╣              │')
    print                                                                           ( '  │              ║  B ► Sustracción         (-)  ║   RESTAR    ║              │')
    print                                                                           ( '  │              ║═══════════════════════════════╬═════════════╣              │')
    print                                                                           ( '  │              ║  C ► Multiplicación      (*)  ║ MULTIPLICAR ║              │')
    print                                                                           ( '  │              ║═══════════════════════════════╬═════════════╣              │')
    print                                                                           ( '  │              ║  D ► División            (/)  ║   DIVIDIR   ║              │')
    print                                                                           ( '  │              ║═══════════════════════════════╬═════════════╣              │')
    print                                                                           ( '  │              ║  E ► Exponenciación    (b,e)  ║  EXPONENTE  ║              │')
    print                                                                           ( '  │              ║═══════════════════════════════╬═════════════╣              │')
    print                                                                           ( '  │              ║  F ► Radicación          (√)  ║   RAICES    ║              │')
    print                                                                           ( '  │              ║═══════════════════════════════╬═════════════╣              │')
    print                                                                           ( '  │              ║  G ► Número PAR o IMPAR       ║   PARIDAD   ║              │')
    print                                                                           ( '  │              ╚═══════════════════════════════╩═════════════╝              │')    
           
    

def opcion_A():
    
    
    print                                                                   ( '  │           ╔════════════════════════════════════╦═════════════╗            │')
    print                                                                   ( '  │           ║  A ► Adición                   (+) ║    SUMAR    ║            │')
    print                                                                   ( '  │           ╠════════════════════════════════════╬═════════════╣            │')
             
    try:
        
        numero1 = int (input                                                ( '  │           ║  Escriba el primer valor numérico  ║   '))
        print                                                               ( '  │           ╠════════════════════════════════════╬═════════════╣            │')
        numero2 = int (input                                                ( '  │           ║  Escriba el segundo valor numérico ║   '))

        resultado = numero1 + numero2
            
        print                                                               ( '  │           ╠════════════════════════════════════╬═════════════╣            │')
        print                                                               (f'  │           ║   El resultado de la Adición es    ║   {resultado}         ║            │')
        print                                                               ( '  │           ╚════════════════════════════════════╩═════════════╝            │')
        print                                                               ( '  │                                                                           │')
        print                                                               ( '  ├───────────────────────────────────────────────────────────────────────────┤')
                      
    except ValueError:
            
        print                                                               ( '  │           ╠═══════════════╦════════════════════╩═════════════╗            │')
        print                                                               ( '  │           ║ ⚠  Error  ⚠   ║ NO se admiten letras como valor  ║            │')
        print                                                               ( '  │           ╚═══════════════╩══════════════════════════════════╝            │')
        print                                                               ( '  ├───────────────────────────────────────────────────────────────────────────┤')
            
    
def opcion_B():
    
    print                                                                   ( '  │           ╔════════════════════════════════════╦═════════════╗            │')
    print                                                                   ( '  │           ║  B ► Sustracción               (-) ║   RESTAR    ║            │')
    print                                                                   ( '  │           ╠════════════════════════════════════╬═════════════╣            │')
            
    try:
        
        numero1 = int (input                                                ( '  │           ║  Escriba el primer valor numérico  ║   '))
        print                                                               ( '  │           ╠════════════════════════════════════╬═════════════╣            │')
        numero2 = int (input                                                ( '  │           ║  Escriba el segundo valor numérico ║   '))

        resultado = numero1 - numero2
            
        print                                                               ( '  │           ╠════════════════════════════════════╬═════════════╣            │')
        print                                                               (f'  │           ║  El resultado de la sustraccion es ║   {resultado}         ║            │')
        print                                                               ( '  │           ╚════════════════════════════════════╩═════════════╝            │')
        print                                                               ( '  ├───────────────────────────────────────────────────────────────────────────┤')
                    
    except ValueError:
            
        print                                                               ( '  │           ╠═══════════════╦════════════════════╩═════════════╗            │')
        print                                                               ( '  │           ║ ⚠  Error  ⚠   ║ NO se admiten letras como valor  ║            │')
        print                                                               ( '  │           ╚═══════════════╩══════════════════════════════════╝            │')
        print                                                               ( '  ├───────────────────────────────────────────────────────────────────────────┤')
            
def opcion_C():
    
    print                                                                   ( '  │           ╔════════════════════════════════════╦═════════════╗            │')
    print                                                                   ( '  │           ║  C ► Multiplicación            (*) ║ MULTIPLICAR ║            │')
    print                                                                   ( '  │           ║════════════════════════════════════╬═════════════╣            │')
            
    try:
        
        numero1 = int (input                                                ( '  │           ║  Escriba el primer valor numérico  ║   '))
        print                                                               ( '  │           ╠════════════════════════════════════╬═════════════╣            │')
        numero2 = int (input                                                ( '  │           ║  Escriba el segundo valor numérico ║   '))

        resultado = numero1 * numero2
            
        print                                                               ( '  │           ╠════════════════════════════════════╬═════════════╣            │')
        print                                                               (f'  │           ║  Resultado de la Multiplicación es ║   {resultado}         ║            │')
        print                                                               ( '  │           ╚════════════════════════════════════╩═════════════╝            │')
        print                                                               ( '  ├───────────────────────────────────────────────────────────────────────────┤')
                    
    except ValueError:
            
        print                                                               ( '  │           ╠═══════════════╦════════════════════╩═════════════╗            │')
        print                                                               ( '  │           ║ ⚠  Error  ⚠   ║ NO se admiten letras como valor  ║            │')
        print                                                               ( '  │           ╚═══════════════╩══════════════════════════════════╝            │')
        print                                                               ( '  ├───────────────────────────────────────────────────────────────────────────┤')


def opcion_D():
    
    print                                                                   ( '  │           ╔════════════════════════════════════╦═════════════╗            │')
    print                                                                   ( '  │           ║  D ► División                  (/) ║   DIVIDIR   ║            │')
    print                                                                   ( '  │           ╠════════════════════════════════════╬═════════════╣            │')
        
    try:
            
        numero1 = int (input                                                ( '  │           ║  Escriba el primer valor numérico  ║   '))
        print                                                               ( '  │           ╠════════════════════════════════════╬═════════════╣            │')
        numero2 = int (input                                                ( '  │           ║  Escriba el segundo valor numérico ║   '))
        
        resultado = numero1 / numero2
                    
        print                                                               ( '  │           ╠════════════════════════════════════╬═════════════╣            │')
        print                                                               (f'  │           ║   El resultado de la división es   ║   {resultado:.2f}      ║            │')
        print                                                               ( '  │           ╚════════════════════════════════════╩═════════════╝            │')
        print                                                               ( '  ├───────────────────────────────────────────────────────────────────────────┤')
        
    except ValueError:
        
        print                                                               ( '  │           ╠═══════════════╦════════════════════╩═════════════╗            │')
        print                                                               ( '  │           ║ ⚠  Error  ⚠   ║ NO se admiten letras como valor  ║            │')
        print                                                               ( '  │           ╚═══════════════╩══════════════════════════════════╝            │')
        print                                                               ( '  ├───────────────────────────────────────────────────────────────────────────┤')
                

    except ZeroDivisionError:
    
            print                                                           ( '  │           ╠═══════════════╦════════════════════╩═════════════╗            │')
            print                                                           ( '  │           ║ ⚠  Error  ⚠   ║    NO se puede dividir entre 0   ║            │')
            print                                                           ( '  │           ╚═══════════════╩══════════════════════════════════╝            │')
            print                                                           ( '  ├───────────────────────────────────────────────────────────────────────────┤')
             

def opcion_E():
    
    print                                                                   ( '  │           ╔════════════════════════════════════╦═════════════╗            │')
    print                                                                   ( '  │           ║  E ► Exponenciación          (b,e) ║  EXPONENTE  ║            │')
    print                                                                   ( '  │           ╠════════════════════════════════════╬═════════════╣            │')
         
    try:   
            
        base = int (input                                                   ( '  │           ║      Escriba el número de base     ║   '))
        print                                                               ( '  │           ╠════════════════════════════════════╬═════════════╣            │')
        exponente = int (input                                              ( '  │           ║    Escriba el número de exponente  ║   '))
        resultado = base ** exponente
            
        print                                                               ( '  │           ╠════════════════════════════════════╬═════════════╣            │')
        print                                                               (f'  │           ║ El resultado de la Exponenciación  ║   {resultado}        ║            │')
        print                                                               ( '  │           ╚════════════════════════════════════╩═════════════╝            │')
        print                                                               ( '  ├───────────────────────────────────────────────────────────────────────────┤')
                    
    except ValueError:
            
        
        print                                                               ( '  │           ╠═══════════════╦════════════════════╩═════════════╗            │')
        print                                                               ( '  │           ║ ⚠  Error  ⚠   ║ NO se admiten letras como valor  ║            │')
        print                                                               ( '  │           ╚═══════════════╩══════════════════════════════════╝            │')
        print                                                               ( '  ├───────────────────────────────────────────────────────────────────────────┤')

def opcion_F():
       
    print                                                                   ( '  │           ╔════════════════════════════════════╦═════════════╗            │')
    print                                                                   ( '  │           ║   F ► Radicación               (√) ║    RAICES   ║            │')
    print                                                                   ( '  │           ╠════════════════════════════════════╬═════════════╣            │')
    
    try:
        
        numero_base = int (input                                            ( '  │           ║     Escriba el número de base      ║   '))
        
        if numero_base > 0 :  
            print                                                           ( '  │           ╠════════════════════════════════════╬═════════════╣            │')
            numero_raiz = int (input                                        ( '  │           ║   Escriba el número de elevación   ║   '))
            resultado = math.pow(numero_base,1 / numero_raiz)
            
            print                                                           ( '  │           ╠════════════════════════════════════╬═════════════║            │')
            print                                                           (f'  │           ║   El resultado de la Radicación es ║   {resultado:.2f}      ║            │')
            print                                                           ( '  │           ╚════════════════════════════════════╩═════════════╝            │')
            print                                                           ( '  ├───────────────────────────────────────────────────────────────────────────┤')
        
        else:
            print                                                           ( '  │           ╠═══════════════╦════════════════════╩═════════════╗            │')
            print                                                           ( '  │           ║ ⚠  Error  ⚠   ║  NO se admiten valores negativos ║            │')
            print                                                           ( '  │           ╚═══════════════╩══════════════════════════════════╝            │')
            print                                                           ( '  ├───────────────────────────────────────────────────────────────────────────┤')
            
    except ValueError:
            
        print                                                               ( '  │           ╠═══════════════╦════════════════════╩═════════════╗            │')
        print                                                               ( '  │           ║ ⚠  Error  ⚠   ║ NO se admiten letras como valor  ║            │')
        print                                                               ( '  │           ╚═══════════════╩══════════════════════════════════╝            │')
        print                                                               ( '  ├───────────────────────────────────────────────────────────────────────────┤')
    
def opcion_G():
    
    print                                                                   ( '  │           ╔════════════════════════════════════╦═════════════╗            │')
    print                                                                   ( '  │           ║  G ► El Número es PAR o IMPAR      ║   PARIDAD   ║            │')
    print                                                                   ( '  │           ╠════════════════════════════════════╬═════════════╣            │')
       
    try:   
            
        numero1 = int (input                                                ( '  │           ║   Escriba el número a verificar    ║     '))
        
         
        resultado = numero1 % int (2)
    
        if resultado == 0 :
            
            print                                                           ( '  │           ╠════════════════════════════════════╩═════════════╣            │')
            print                                                           (f'  │           ║  El ({numero1}) esta dentro de los números PARES ║            │')
            print                                                           ( '  │           ╚══════════════════════════════════════════════════╝            │')
            print                                                           ( '  ├───────────────────────────────────────────────────────────────────────────┤')
            
        else :
            
            print                                                           ( '  │           ╠════════════════════════════════════╩═════════════╣            │')
            print                                                           (f'  │           ║ El ({numero1}) esta dentro de los números IMPARES║            │')
            print                                                           ( '  │           ╚══════════════════════════════════════════════════╝            │')
            print                                                           ( '  ├───────────────────────────────────────────────────────────────────────────┤')
                
    except ValueError:
            
        print                                                               ( '  │           ╠═══════════════╦════════════════════╩═════════════╗            │')
        print                                                               ( '  │           ║ ⚠  Error  ⚠   ║ NO se admiten letras como valor  ║            │')
        print                                                               ( '  │           ╚═══════════════╩══════════════════════════════════╝            │')
        print                                                               ( '  ├───────────────────────────────────────────────────────────────────────────┤')
            
