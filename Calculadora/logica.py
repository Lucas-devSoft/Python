import math, os
from turtle import back

from colores import *

def Limpieza_consola():
    
    if os.name in ("nt", "dos"):  # si la maquina esta corriendo en Windows, use cls
        
        comando = "cls"

    else:
        
        comando = "clear"

    os.system(comando)

def opción_A():
    
    Operador = "+"

    print(f"""
{marco}╔══════════════════════════════════════════════════════════╦════════════════════╗{fin}
{marco}║{fondo}                                                          {fin+marco}║{fondo}                    {fin+marco}║{fin}
{marco}║{fondo}                       {texto}A ► Adición{fin+fondo}                        {fin+marco}║{fondo}        {texto}(+){fin+fondo}         {fin+marco}║{fin}
{marco}║{fondo}                                                          {fin+marco}║{fondo}                    {fin+marco}║{fin}
{marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}""")
    Numero1 = int(input(f"{marco}║{fondo}                {texto}Inserte el Primer valor{fin+fondo}                   {fin+marco}║{fin}          "))
    print(f"{marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}")
    Numero2 = int(input(f"{marco}║{fondo}                {texto}Inserte el Segundo Valor{fin+fondo}                  {fin+marco}║{fin}          "))
    
    Resultado = Numero1 + Numero2

    print(f"""{marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}
{marco}║{fondo}                                                          {fin+marco}║                    ║{fin}
{marco}║{fondo}                {texto}El resultado de la adición es{fin+fondo}             {fin+marco}║{fin}          {Resultado}         {marco}║{fin}
{marco}║{fondo}                                                          {fin+marco}║                    ║{fin}
{marco}╠══════════════════════════════════════════════════════════╩════════════════════╣{fin}""")

    return Numero1, Operador, Numero2, Resultado

def opción_B():
    
    Operador = "-"

    print(f"""
{marco}╔══════════════════════════════════════════════════════════╦════════════════════╗{fin}
{marco}║{fondo}                                                          {fin+marco}║{fondo}                    {fin+marco}║{fin}
{marco}║{fondo}                       {texto}B ► Sustracción{fin+fondo}                    {fin+marco}║{fondo}        {texto}(-){fin+fondo}         {fin+marco}║{fin}
{marco}║{fondo}                                                          {fin+marco}║{fondo}                    {fin+marco}║{fin}
{marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}""")
    Numero1 = int(input(f"{marco}║{fondo}                {texto}Inserte el primer valor{fin+fondo}                   {fin+marco}║{fin}          "))
    print(f"{marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}")
    Numero2 = int(input(f"{marco}║{fondo}                {texto}Inserte el segundo valor{fin+fondo}                  {fin+marco}║{fin}          "))

    Resultado = Numero1 - Numero2

    print(f"""{marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}
{marco}║{fondo}                                                          {fin+marco}║                    ║{fin}
{marco}║{fondo}                {texto}El resultado de la Sustracción es{fin+fondo}         {fin+marco}║{fin}          {Resultado}         {marco}║{fin}
{marco}║{fondo}                                                          {fin+marco}║                    ║{fin}
{marco}╠══════════════════════════════════════════════════════════╩════════════════════╣{fin}""")

    return Numero1, Operador, Numero2, Resultado

def opción_C():
    
    Operador = "*"

    print(f"""
{marco}╔══════════════════════════════════════════════════════════╦════════════════════╗{fin}
{marco}║{fondo}                                                          {fin+marco}║{fondo}                    {fin+marco}║{fin}
{marco}║{fondo}                       {texto}C ► Multiplicación{fin+fondo}                 {fin+marco}║{fondo}        {texto}(*){fin+fondo}         {fin+marco}║{fin}
{marco}║{fondo}                                                          {fin+marco}║{fondo}                    {fin+marco}║{fin}
{marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}""")
    Numero1 = int(input(f"{marco}║{fondo}                {texto}Inserte el primer valor{fin+fondo}                   {fin+marco}║{fin}          "))
    print(f"{marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}")
    Numero2 = int(input(f"{marco}║{fondo}                {texto}Inserte el segundo valor{fin+fondo}                  {fin+marco}║{fin}          "))

    Resultado = Numero1 * Numero2

    print(f"""{marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}
{marco}║{fondo}                                                          {fin+marco}║                    ║{fin}
{marco}║{fondo}           {texto}El resultado de la multiplicación es{fin+fondo}           {fin+marco}║{fin}          {Resultado}         {marco}║{fin}
{marco}║{fondo}                                                          {fin+marco}║                    ║{fin}
{marco}╠══════════════════════════════════════════════════════════╩════════════════════╣{fin}""")

    return Numero1, Operador, Numero2, Resultado

def opción_D():
    
    Operador = "/"

    print(f"""
{marco}╔══════════════════════════════════════════════════════════╦════════════════════╗{fin}
{marco}║{fondo}                                                          {fin+marco}║{fondo}                    {fin+marco}║{fin}
{marco}║{fondo}                    {texto}D ► División{fin+fondo}                          {fin+marco}║{fondo}        {texto}(/){fin+fondo}         {fin+marco}║{fin}
{marco}║{fondo}                                                          {fin+marco}║{fondo}                    {fin+marco}║{fin}
{marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}""")
    Numero1 = int(input(f"{marco}║{fondo}                {texto}Inserte el primer Valor{fin+fondo}                   {fin+marco}║{fin}          "))
    print(f"{marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}")
    Numero2 = int(input(f"{marco}║{fondo}                {texto}Inserte el segundo valor{fin+fondo}                  {fin+marco}║{fin}          "))

    Resultado = Numero1 / Numero2

    print(f"""{marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}
{marco}║{fondo}                                                          {fin+marco}║                    ║{fin}
{marco}║{fondo}              {texto}El resultado de la división es{fin+fondo}              {fin+marco}║{fin}         {Resultado:.2f}       {marco}║{fin}
{marco}║{fondo}                                                          {fin+marco}║                    ║{fin}
{marco}╠══════════════════════════════════════════════════════════╩════════════════════╣{fin}""")

    return Numero1, Operador, Numero2, Resultado

def opción_E():
    
    Operador = "b/e"

    print(f"""
{marco}╔══════════════════════════════════════════════════════════╦════════════════════╗{fin}
{marco}║{fondo}                                                          {fin+marco}║{fondo}                    {fin+marco}║{fin}
{marco}║{fondo}                  {texto}E ► Potenciación{fin+fondo}                        {fin+marco}║{fondo}        {texto}(b,e){fin+fondo}       {fin+marco}║{fin}
{marco}║{fondo}                                                          {fin+marco}║{fondo}                    {fin+marco}║{fin}
{marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}""")
    Numero1 = int(input(f"{marco}║{fondo}                {texto}Inserte el número base{fin+fondo}                    {fin+marco}║{fin}          "))
    print(f"{marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}")
    Numero2 = int(input(f"{marco}║{fondo}                {texto}Inserte el número del exponente{fin+fondo}           {fin+marco}║{fin}          "))

    Resultado = Numero1**Numero2

    print(f"""{marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}
{marco}║{fondo}                                                          {fin+marco}║                    ║{fin}
{marco}║{fondo}            {texto}El resultado de la Potenciación es{fin+fondo}            {fin+marco}║{fin}          {Resultado}        {marco}║{fin}
{marco}║{fondo}                                                          {fin+marco}║                    ║{fin}
{marco}╠══════════════════════════════════════════════════════════╩════════════════════╣{fin}""")

    return Numero1, Operador, Numero2, Resultado

def opción_F():
    
    Operador = "√"

    print(f"""
{marco}╔══════════════════════════════════════════════════════════╦════════════════════╗{fin}
{marco}║{fondo}                                                          {fin+marco}║{fondo}                    {fin+marco}║{fin}
{marco}║{fondo}                    {texto}F ► Radicación{fin+fondo}                        {fin+marco}║{fondo}          {texto}(√){fin+fondo}       {fin+marco}║{fin}
{marco}║{fondo}                                                          {fin+marco}║{fondo}                    {fin+marco}║{fin}
{marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}""")
    Numero1 = int(input(f"{marco}║{fondo}                {texto}Inserte el número base{fin+fondo}                    {fin+marco}║{fin}          "))

    if Numero1 > 0:
        
        print(f"{marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}")
        Numero2 = int(input(f"{marco}║{fondo}                {texto}Inserte el número de la raíz{fin+fondo}              {fin+marco}║{fin}          "))

        if Numero2 > 0:
            
            Resultado = math.pow(Numero1, 1 / Numero2)

            print(f"""{marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}
{marco}║{fondo}                                                          {fin+marco}║                    ║{fin}
{marco}║{fondo}             {texto}El resultado de la radicación es{fin+fondo}             {fin+marco}║{fin}         {Resultado:.2f}       {marco}║{fin}
{marco}║{fondo}                                                          {fin+marco}║                    ║{fin}
{marco}╠══════════════════════════════════════════════════════════╩════════════════════╣{fin}""")

    return Numero1, Operador, Numero2, Resultado

def opción_G():
    
    Operador = "Par/Impar"

    print(f"""
{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}║{fondo}                              {texto}G ► Es Par o Impar{fin+fondo}                               {fin+marco}║{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}╠══════════════════════════════════════════════════════════╦════════════════════╣{fin}""")

    Numero1 = int(input(f"{marco}║{fondo}               {texto}Inserte el número que quiere verificar{fin+fondo}     {fin+marco}║{fin}          "))
    print(f"{marco}╠══════════════════════════════════════════════════════════╩════════════════════╣{fin}")

    Resultado = Numero1 % 2

    if Resultado == 0:
        
        print(f"""{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}║{fondo}                     {texto}El ({Numero1}) esta dentro de los números pares.{fin+fondo}                 {fin+marco}║{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}""")

        Conclusión = "Par"

    else:
        
        print(f"""{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}║{fondo}                  {texto}El ({Numero1}) esta dentro de los números impares.{fin+fondo}                  {fin+marco}║{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}""")

        Conclusión = "Impar"

    return Numero1, Operador, Conclusión

def opción_H():
    
    Operador = "¿Es primo?"

    print(f"""
{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
{marco}║{fondo}                                                                               {fin+marco}║{fin}")
{marco}║{fondo}                            {texto}H ► Es un número primo ?{fin+fondo}                           {fin+marco}║{fin}")
{marco}║{fondo}                                                                               {fin+marco}║{fin}")
{marco}╠══════════════════════════════════════════════════════════╦════════════════════╣{fin}""")

    i = 2
    cont = 0

    Numero1 = int(input(f"{marco}║{fondo}  {texto}Inserte el número que quiere verificar si es primo.{fin+fondo}     {fin+marco}║{fin}          "))
    print(f"{marco}╠══════════════════════════════════════════════════════════╩════════════════════╣{fin}")

    while Numero1 > i and cont == 0:
        
        resto = Numero1 % i

        if resto == 0:
        
            cont += 1

        i += 1

    if cont != 0 or Numero1 == 1:
        
        print(f"""
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}║{fondo}                     {texto}El ({Numero1}) no esta dentro de los números primos{fin+fondo}              {fin+marco}║{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}""")

        Conclusión = "No es primo"

    else:
        print(f"""{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}║{fondo}                       {texto}El ({Numero1}) esta dentro de los números primos.{fin+fondo}              {fin+marco}║{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}""")

        Conclusión = "Es primo"

    return Numero1, Operador, Conclusión

def opción_I():
    
    print(f"""
{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}║{fondo}                          {texto}I ► Números primos por rango{fin+fondo}                         {fin+marco}║{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}╠══════════════════════════════════════════════════════════╦════════════════════╣{fin}""")

    hasta = int(input(f"{marco}║{fondo}    {texto}Inserte el número de rango que quiere ver en primos.{fin+fondo}  {fin+marco}║{fin}          "))

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

    print(f"""{marco}╔══════════════════════════════════════════════════════════╩════════════════════╗{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}║{fondo}                          {texto}Listado de números primos{fin+fondo}                            {fin+marco}║{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}╠════════════╦════════════╦════════════╦════════════╦════════════╦══════════════╣{fin}""")

    lugar = 1
    
    for primo in primos:
        
        if lugar % 6 != 0:
            
            print(f"{marco}║{fondo}",f"{texto}{primo:^10} {fin}{fin+marco}{fin}",end="")

        else:
            
            print(f"{marco}║{fondo}",f"{texto}{primo:^12}{fin+fondo}",f"{fin+marco}║{fin}")

        lugar += 1
    
    print()
    
def Cartel():
    
    print(f"""{marco}
 ███████╗   █████╗  ██╗       ██████╗ ██╗   ██╗ ██╗       █████╗  ██████╗   ██████╗  ██████╗   █████╗
██╔═════╝  ██╔══██╗ ██║      ██╔════╝ ██║   ██║ ██║      ██╔══██╗ ██╔══██╗ ██╔═══██╗ ██╔══██╗ ██╔══██╗
██║        ███████║ ██║      ██║      ██║   ██║ ██║      ███████║ ██║  ██║ ██║   ██║ ██████╔╝ ███████║
██║        ██╔══██║ ██║      ██║      ██║   ██║ ██║      ██╔══██║ ██║  ██║ ██║   ██║ ██╔══██╗ ██╔══██║
╚═██████╗  ██║  ██║ ███████╗ ╚██████╗ ╚██████╔╝ ███████╗ ██║  ██║ ██████╔╝ ╚██████╔╝ ██║  ██║ ██║  ██║
  ╚═════╝  ╚═╝  ╚═╝ ╚══════╝  ╚═════╝  ╚═════╝  ╚══════╝ ╚═╝  ╚═╝ ╚═════╝   ╚═════╝  ╚═╝  ╚═╝ ╚═╝  ╚═╝{fin}""")  
    