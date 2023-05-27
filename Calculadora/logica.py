import math, os

from colores import *

def Cartel():
    
    print(f"""{marco}
██████╗ █████╗ ██╗     ██████╗██╗   ██╗██╗      █████╗ ██████╗  ██████╗ ██████╗  █████╗
██╔═══╝██╔══██╗██║     ██╔═══╝██║   ██║██║     ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔══██╗
██║    ███████║██║     ██║    ██║   ██║██║     ███████║██║  ██║██║   ██║██████╔╝███████║
██║    ██╔══██║██║     ██║    ██║   ██║██║     ██╔══██║██║  ██║██║   ██║██╔══██╗██╔══██║
██████╗██║  ██║███████╗██████╗████████║███████╗██║  ██║██████╔╝╚██████╔╝██║  ██║██║  ██║
╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝╚═══════╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝{fin}""")
    
def Limpieza_consola():
    
    if os.name in ("nt", "dos"):  # si la maquina esta corriendo en Windows, use cls
        
        comando = "cls"

    else:
        
        comando = "clear"

    os.system(comando)

def opción_A():
    
    Operador = "+"

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}A ► Adición                               (+)                    {marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")
    Numero1 = int(input(f"{marco+fondo}█                {texto}Inserte el primer valor : {fin}                      "))
    Numero2 = int(input(f"{marco+fondo}█               {texto}Inserte el segundo Valor : {fin}                      "))
    
    Resultado = Numero1 + Numero2

    print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█          {texto}El resultado de la adición es :                       {Resultado}                     {marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")

    return Numero1, Operador, Numero2, Resultado

def opción_B():
    
    Operador = "-"

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}B ► Sustracción                            (-)                   {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")
    Numero1 = int(input(f"{marco+fondo}█                {texto}Inserte el primer valor : {fin}                       "))
    Numero2 = int(input(f"{marco+fondo}█               {texto}Inserte el segundo valor : {fin}                       "))

    Resultado = Numero1 - Numero2

    print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█      {texto}El resultado de la sustracción es :                        {Resultado}                    {marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")

    return Numero1, Operador, Numero2, Resultado

def opción_C():
    
    Operador = "*"

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}C ► Multiplicación                         (*)                   {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")
    Numero1 = int(input(f"{marco+fondo}█                {texto}Inserte el primer valor : {fin}                       "))
    Numero2 = int(input(f"{marco+fondo}█               {texto}Inserte el segundo valor : {fin}                       "))

    Resultado = Numero1 * Numero2

    print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█   {texto}El resultado de la multiplicación es :                        {Resultado}                    {marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")

    return Numero1, Operador, Numero2, Resultado

def opción_D():
    
    Operador = "/"

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}D ► División                               (/)                   {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")
    Numero1 = int(input(f"{marco+fondo}█               {texto}Inserte el primer Valor : {fin}                        "))
    Numero2 = int(input(f"{marco+fondo}█              {texto}Inserte el segundo valor : {fin}                        "))

    Resultado = Numero1 / Numero2

    print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█        {texto}El resultado de la división es :                       {Resultado:.2f}                   {marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")

    return Numero1, Operador, Numero2, Resultado

def opción_E():
    
    Operador = "b/e"

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}E ► Potenciación                           (b,e)                 {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")
    Numero1 = int(input(f"{marco+fondo}█                {texto}Inserte el número base : {fin}                        "))
    Numero2 = int(input(f"{marco+fondo}█       {texto}Inserte el número del exponente : {fin}                        "))

    Resultado = Numero1**Numero2

    print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█    {texto}El resultado de la potenciación es :                         {Resultado}                   {marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")

    return Numero1, Operador, Numero2, Resultado

def opción_F():
    
    Operador = "√"

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}F ► Radicación                            (√)                    {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")
    Numero1 = int(input(f"{marco+fondo}█               {texto}Inserte el número base : {fin}                        "))

    if Numero1 > 0:
        
        Numero2 = int(input(f"{marco+fondo}█               {texto}Inserte el número raíz : {fin}                        "))

        if Numero2 > 0:
            
            Resultado = math.pow(Numero1, 1 / Numero2)

            print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█     {texto}El resultado de la radicación es :                       {Resultado:.3f}                   {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")

    return Numero1, Operador, Numero2, Resultado

def opción_G():
    
    Operador = "Par/Impar"

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                         {texto}G ► ¿El número es par o impar?                               {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")
    Numero1 = int(input(f"{marco+fondo}█                    {texto}Inserte el número que quiere verificar : {fin}              "))

    Resultado = Numero1 % 2

    if Resultado == 0:
        
        print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                       {texto}El ({Numero1}) esta dentro de los números pares.                       {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")

        Conclusión = "Par"

    else:
        
        print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                  {texto}El ({Numero1}) esta dentro de los números impares.                          {fin+marco}█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}""")

        Conclusión = "Impar"

    return Numero1, Operador, Conclusión

def opción_H():
    
    Operador = "¿Es primo?"

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                         {texto}H ► ¿El número es primo?                                     {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")

    i = 2
    cont = 0

    Numero1 = int(input(f"{marco+fondo}█         {texto}Inserte el número que quiere verificar si es primo : {fin}         "))

    while Numero1 > i and cont == 0:
        
        resto = Numero1 % i

        if resto == 0:
        
            cont += 1

        i += 1

    if cont != 0 or Numero1 == 1:
        
        print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                    {texto}El ({Numero1}) no esta dentro de los números primos.                      {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")

        Conclusión = "No es primo"

    else:
        print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}El ({Numero1}) esta dentro de los números primos.                        {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")

        Conclusión = "Es primo"

    return Numero1, Operador, Conclusión

def opción_I():
    
    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                          {texto}I ► Rango de números primos.                                {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")

    hasta = int(input(f"{marco+fondo}█              {texto}Inserte el rango en primos que quiere ver :  {fin}         "))

    primos = []

    for numero in range(2, hasta + 1):
        
        esPrimo = True

        if numero == 2:
            
            primos.append(numero)

        else:
            
            i = 2

            while i < (pow(numero, 1 / 2) + 1):
                
                resto = numero % i

                if resto == 0:
                    
                    esPrimo = False
                    break

                i += 1

            if esPrimo == True:
                
                primos.append(numero)

    print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                               {texto}Tabla de números primos                                {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")

    lugar = 1
    
    for primo in primos:
        
        if lugar % 6 != 0:
            
            print(f"{marco+fondo}█{texto}{primo:^13}",end = "")

        else:
            
            print(f"{marco+fondo}█{texto}{primo:^16}{fin+marco}█{fin}") 
        
        lugar += 1
    print()