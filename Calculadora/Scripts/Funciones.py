from Historial_BD import *
import math, os 

def limpiar_consola():
    
    comando = 'clear'
    
    if os.name in ('nt', 'dos'):  # si la maquina esta corriendo en Windows, use cls
    
        comando = 'cls'
    
    else:
        
        comando
    
    os.system(comando)

def Menu(nombre,guardar):
    
        print                                               ( '      ┌───────────────────────────────────────────────────────────────┐      ')
        print                                               ( '┌─────┤   Desarrollado con el Lenguaje de Python BY Lucas E.Sanchez   ├─────┐')
        print                                               ( '│     └───────────────────────────────────────────────────────────────┘     │')
        print                                               ( '|                                                                           |')
        conectar_BD                                         (guardar)
        print                                               ( '│                                                                           │')
        print                                               ( '│       ╔═════════════════════════════════════════════════════════╗         │')
        print                                               (f'│       ║   Hola {nombre.capitalize()}, Bienvenido/a a mi Proyecto Personal       ║         │')
        print                                               ( '│       ╚═════════════════════════════════════════════════════════╝         │')
        print                                               ( '│                                                                           │')
        print                                               ( '│              ╔═════════════════════════════════════════════╗              │')
        print                                               ( '│              ║        Calculadora interactiva Python       ║              │')
        print                                               ( '│              ╠═══════════════════════════════╦═════════════╣              │')
        print                                               ( '│              ║ A ► Adición             (+)   ║   SUMAR     ║              │')
        print                                               ( '│              ╠═══════════════════════════════╬═════════════╣              │')
        print                                               ( '│              ║ B ► Sustracción         (-)   ║   RESTAR    ║              │')
        print                                               ( '│              ╠═══════════════════════════════╬═════════════╣              │')
        print                                               ( '│              ║ C ► Multiplicación      (*)   ║ MULTIPLICAR ║              │')
        print                                               ( '│              ╠═══════════════════════════════╬═════════════╣              │')
        print                                               ( '│              ║ D ► División            (/)   ║   DIVIDIR   ║              │')
        print                                               ( '│              ╠═══════════════════════════════╬═════════════╣              │')
        print                                               ( '│              ║ E ► Exponenciación    (b,e)   ║  EXPONENTE  ║              │')
        print                                               ( '│              ╠═══════════════════════════════╬═════════════╣              │')
        print                                               ( '│              ║ F ► Radicación          (√)   ║   RAICES    ║              │')
        print                                               ( '│              ╠═══════════════════════════════╬═════════════╣              │')
        print                                               ( '│              ║ G ► Número PAR o IMPAR        ║   PARIDAD   ║              │')
        print                                               ( '│              ╠═══════════════════════════════╬═════════════╣              │')
        print                                               ( '│              ║ H ► Números Primos Individual ║  PRIMALIDAD ║              │')
        print                                               ( '│              ╠═══════════════════════════════╬═════════════╣              │')   
        print                                               ( '│              ║ I ► Números Primos por Rango  ║  PRIMALIDAD ║              │')
        print                                               ( '│              ╚═══════════════════════════════╩═════════════╝              │') 
    

def opcion_A(nombre,opcion):
    
    Operaciones = 'SUMAR'

    print                                                   ( '│           ╔════════════════════════════════════╦═════════════╗            │')
    print                                                   (f'│           ║  A ► Adición                   (+) ║    {Operaciones}    ║            │')
    print                                                   ( '│           ╠════════════════════════════════════╬═════════════╣            │')
            
    try:
        
        numero1 = int (input                                ( '│           ║  Escriba el primer valor numérico  ║   '))
        print                                               ( '│           ╠════════════════════════════════════╬═════════════╣            │')
        numero2 = int (input                                ( '│           ║  Escriba el segundo valor numérico ║   '))

        resultado = numero1 + numero2
            
        print                                               ( '│           ╠════════════════════════════════════╬═════════════╣            │')
        print                                               (f'│           ║   El resultado de la Adición es    ║   {resultado}         ║            │')
        print                                               ( '│           ╚════════════════════════════════════╩═════════════╝            │')
        print                                               ( '│                                                                           │')
        
        guardado_datos(nombre,opcion,Operaciones,numero1,numero2,resultado)
                    
    except ValueError:
            
        print                                               ( '│           ╠═══════════════╦════════════════════╩═════════════╗            │')
        print                                               ( '│           ║ ⚠  Error  ⚠   ║ NO se admiten letras como valor  ║            │')
        print                                               ( '│           ╚═══════════════╩══════════════════════════════════╝            │')
    
    
def opcion_B(nombre,opcion):
    
    Operaciones = 'RESTAR'

    print                                                   ( '│           ╔════════════════════════════════════╦═════════════╗            │')
    print                                                   (f'│           ║  B ► Sustracción               (-) ║   {Operaciones}    ║            │')
    print                                                   ( '│           ╠════════════════════════════════════╬═════════════╣            │')
            
    try:
        
        numero1 = int (input                                ( '│           ║  Escriba el primer valor numérico  ║   '))
        print                                               ( '│           ╠════════════════════════════════════╬═════════════╣            │')
        numero2 = int (input                                ( '│           ║  Escriba el segundo valor numérico ║   '))

        resultado = numero1 - numero2
            
        print                                               ( '│           ╠════════════════════════════════════╬═════════════╣            │')
        print                                               (f'│           ║  El resultado de la sustraccion es ║   {resultado}         ║            │')
        print                                               ( '│           ╚════════════════════════════════════╩═════════════╝            │')
        
        guardado_datos(nombre,opcion,Operaciones,numero1,numero2,resultado)
                    
    except ValueError:
            
        print                                               ( '│           ╠═══════════════╦════════════════════╩═════════════╗            │')
        print                                               ( '│           ║ ⚠  Error  ⚠   ║ NO se admiten letras como valor  ║            │')
        print                                               ( '│           ╚═══════════════╩══════════════════════════════════╝            │')
        
            
def opcion_C(nombre,opcion):
    
    Operaciones = 'MULTIPLICAR'

    print                                                   ( '│           ╔════════════════════════════════════╦═════════════╗            │')
    print                                                   (f'│           ║  C ► Multiplicación            (*) ║ {Operaciones} ║            │')
    print                                                   ( '│           ║════════════════════════════════════╬═════════════╣            │')
            
    try:
        
        numero1 = int (input                                ( '│           ║  Escriba el primer valor numérico  ║   '))
        print                                               ( '│           ╠════════════════════════════════════╬═════════════╣            │')
        numero2 = int (input                                ( '│           ║  Escriba el segundo valor numérico ║   '))

        resultado = numero1 * numero2
            
        print                                               ( '│           ╠════════════════════════════════════╬═════════════╣            │')
        print                                               (f'│           ║  Resultado de la Multiplicación es ║   {resultado}         ║            │')
        print                                               ( '│           ╚════════════════════════════════════╩═════════════╝            │')
        
        guardado_datos(nombre,opcion,Operaciones,numero1,numero2,resultado)
                    
    except ValueError:
            
        print                                               ( '│           ╠═══════════════╦════════════════════╩═════════════╗            │')
        print                                               ( '│           ║ ⚠  Error  ⚠   ║ NO se admiten letras como valor  ║            │')
        print                                               ( '│           ╚═══════════════╩══════════════════════════════════╝            │')
        


def opcion_D(nombre,opcion):
    
    Operaciones = 'DIVIDIR'

    print                                                   ( '│           ╔════════════════════════════════════╦═════════════╗            │')
    print                                                   (f'│           ║  D ► División                  (/) ║   {Operaciones}   ║            │')
    print                                                   ( '│           ╠════════════════════════════════════╬═════════════╣            │')
        
    try:
            
        numero1 = int (input                                ( '│           ║  Escriba el primer valor numérico  ║   '))
        print                                               ( '│           ╠════════════════════════════════════╬═════════════╣            │')
        numero2 = int (input                                ( '│           ║  Escriba el segundo valor numérico ║   '))
        
        resultado = numero1 / numero2
                    
        print                                               ( '│           ╠════════════════════════════════════╬═════════════╣            │')
        print                                               (f'│           ║   El resultado de la división es   ║   {resultado:.2f}      ║            │')
        print                                               ( '│           ╚════════════════════════════════════╩═════════════╝            │')
        
        guardado_datos(nombre,opcion,Operaciones,numero1,numero2,resultado)
        
    except ValueError:
        
        print                                               ( '│           ╠═══════════════╦════════════════════╩═════════════╗            │')
        print                                               ( '│           ║ ⚠  Error  ⚠   ║ NO se admiten letras como valor  ║            │')
        print                                               ( '│           ╚═══════════════╩══════════════════════════════════╝            │')
        
    except ZeroDivisionError:
    
        print                                               ( '│           ╠═══════════════╦════════════════════╩═════════════╗            │')
        print                                               ( '│           ║ ⚠  Error  ⚠   ║    NO se puede dividir entre 0   ║            │')
        print                                               ( '│           ╚═══════════════╩══════════════════════════════════╝            │')
            
             

def opcion_E(nombre,opcion):
    
    Operaciones = 'EXPONENTE'

    print                                                   ( '│           ╔════════════════════════════════════╦═════════════╗            │')
    print                                                   (f'│           ║  E ► Exponenciación          (b/e) ║  {Operaciones}  ║            │')
    print                                                   ( '│           ╠════════════════════════════════════╬═════════════╣            │')
         
    try:   
            
        numero1 = int (input                                ( '│           ║      Escriba el número de base     ║   '))
        print                                               ( '│           ╠════════════════════════════════════╬═════════════╣            │')
        numero2 = int (input                                ( '│           ║    Escriba el número de exponente  ║   '))
        resultado = numero1 ** numero2
            
        print                                               ( '│           ╠════════════════════════════════════╬═════════════╣            │')
        print                                               (f'│           ║ El resultado de la Exponenciación  ║   {resultado}        ║            │')
        print                                               ( '│           ╚════════════════════════════════════╩═════════════╝            │')
        
        guardado_datos(nombre,opcion,Operaciones,numero1,numero2,resultado)
                    
    except ValueError:
            
        print                                               ( '│           ╠═══════════════╦════════════════════╩═════════════╗            │')
        print                                               ( '│           ║ ⚠  Error  ⚠   ║ NO se admiten letras como valor  ║            │')
        print                                               ( '│           ╚═══════════════╩══════════════════════════════════╝            │')
        

def opcion_F(nombre,opcion):

    Operaciones = 'RAICES'

    print                                                   ( '│           ╔════════════════════════════════════╦═════════════╗            │')
    print                                                   (f'│           ║   F ► Radicación               (√) ║    {Operaciones}   ║            │')
    print                                                   ( '│           ╠════════════════════════════════════╬═════════════╣            │')
    
    try:
        
        numero1 = int (input                                ( '│           ║     Escriba el número de base      ║   '))
        
        if numero1 > 0 :  
            
            print                                           ( '│           ╠════════════════════════════════════╬═════════════╣            │')
            numero2 = int (input                            ( '│           ║   Escriba el número de elevación   ║   '))
            resultado = math.pow(numero1,1 / numero2)
            
            print                                           ( '│           ╠════════════════════════════════════╬═════════════║            │')
            print                                           (f'│           ║   El resultado de la Radicación es ║   {resultado:.2f}      ║            │')
            print                                           ( '│           ╚════════════════════════════════════╩═════════════╝            │')
           
            guardado_datos(nombre,opcion,Operaciones,numero1,numero2,resultado)
              
        else:

            print                                           ( '│           ╠═══════════════╦════════════════════╩═════════════╗            │')
            print                                           ( '│           ║ ⚠  Error  ⚠   ║  NO se admiten valores negativos ║            │')
            print                                           ( '│           ╚═══════════════╩══════════════════════════════════╝            │')
            
            
    except ValueError:
            
        print                                               ( '│           ╠═══════════════╦════════════════════╩═════════════╗            │')
        print                                               ( '│           ║ ⚠  Error  ⚠   ║ NO se admiten letras como valor  ║            │')
        print                                               ( '│           ╚═══════════════╩══════════════════════════════════╝            │')
        
    
def opcion_G(nombre,opcion):
    
    Operaciones = 'PARIDAD'
    
    print                                                   ( '│           ╔════════════════════════════════════╦═════════════╗            │')
    print                                                   (f'│           ║  G ► El Número es PAR o IMPAR      ║   {Operaciones}   ║            │')
    print                                                   ( '│           ╠════════════════════════════════════╬═════════════╣            │')
       
    try:   
            
        numero1 = int (input                                ( '│           ║   Escriba el número a verificar    ║     '))
        
         
        resultado = numero1 % int (2)
    
        if resultado == 0 :
            
            print                                           ( '│           ╠════════════════════════════════════╩═════════════╣            │')
            print                                           (f'│           ║    El ({numero1}) esta dentro de los números PARES     ║            │')
            print                                           ( '│           ╚══════════════════════════════════════════════════╝            │')
            
            guardado_datos(nombre, opcion, Operaciones, numero1, numero2=None, resultado ="PAR")
            
            
        else:
            
            print                                           ( '│           ╠════════════════════════════════════╩═════════════╣            │')
            print                                           (f'│           ║    El ({numero1}) esta dentro de los números IMPARES   ║            │')
            print                                           ( '│           ╚══════════════════════════════════════════════════╝            │')
            
            guardado_datos(nombre, opcion, Operaciones, numero1, numero2=None, resultado = "IMPAR")
           
                
    except ValueError:
            
        print                                               ( '│           ╠═══════════════╦════════════════════╩═════════════╗            │')
        print                                               ( '│           ║ ⚠  Error  ⚠   ║ NO se admiten letras como valor  ║            │')
        print                                               ( '│           ╚═══════════════╩══════════════════════════════════╝            │')
        
            
def opcion_H(nombre,opcion):
    
    Operaciones = 'PRIMALIDAD'
    
    print                                                   ( '│           ╔════════════════════════════════════╦═════════════╗            │')
    print                                                   (f'│           ║  H ► Números Primos Individual     ║ {Operaciones}  ║            │')
    print                                                   ( '│           ╠════════════════════════════════════╬═════════════╣            │')
    
    try :
           
        i=2
        cont = 0
        
        numero1 = int (input                                ( '│           ║        validar numeracion prima    ║     '))

        while numero1 > i and cont == 0:
            
            resto = numero1 % i 
            
            if resto == 0:
                
                cont += 1
                
            i+=1
            
        if cont != 0 or numero1 == 1 :
                
            print                                           ( '│           ╠════════════════════════════════════╩═════════════╣            │')
            print                                           (f'│           ║         El ({numero1}) NO ES UN NUMERO PRIMO            ║            │')
            print                                           ( '│           ╚══════════════════════════════════════════════════╝            │')
            guardado_datos(nombre, opcion, Operaciones, numero1, numero2=None, resultado = "NO ES PRIMO")     
            
        else:

            print                                           ( '│           ╠════════════════════════════════════╩═════════════╣            │')
            print                                           (f'│           ║          El ({numero1}) ES UN NUMERO PRIMO              ║            │')
            print                                           ( '│           ╚══════════════════════════════════════════════════╝            │')
            guardado_datos(nombre, opcion, Operaciones, numero1, numero2=None, resultado = "ES PRIMO")    
            
    except ValueError:
        
        print                                               ( '│           ╠═══════════════╦════════════════════╩═════════════╗            │')
        print                                               ( '│           ║ ⚠  Error  ⚠   ║ NO se admiten letras como valor  ║            │')
        print                                               ( '│           ╚═══════════════╩══════════════════════════════════╝            │')
        
        
def opcion_I():
    
    print                                                   ( '│           ╔════════════════════════════════════╦═════════════╗            │')
    print                                                   ( '│           ║  I ► Números Primos por Rango      ║ PRIMALIDAD  ║            │')
    print                                                   ( '│           ╠════════════════════════════════════╬═════════════╣            │')

    try :
            
        hasta = int (input                                  ( '│           ║        Ingrese el rango maximo     ║     '))
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
        print( '├───────────────────────────────────────────────────────────────────────────┤')
        print( '|                   RESULTADO DE LOS NUMEROS PRIMOS                         |')
        print( '├───────────────────────────────────────────────────────────────────────────┤')
        for primo in primos:
            
            if lugar%11 !=0 :
                
                print ('|',f'{primo}'.center(4,' '),end= ' ')      
            else:
                print (f'|{primo}'.center(5,' '),'|')  
        
            lugar += 1
                                    
    except ValueError:
        
        print                                               ( '│           ╠═══════════════╦════════════════════╩═════════════╗            │')
        print                                               ( '│           ║ ⚠  Error  ⚠   ║ NO se admiten letras como valor  ║            │')
        print                                               ( '│           ╚═══════════════╩══════════════════════════════════╝            │')               