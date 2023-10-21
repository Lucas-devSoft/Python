import math
import os

from colores import *


def Limpieza_consola():

    if os.name in ("nt", "dos"):  # si la maquina esta corriendo en Windows, use cls

        comando = "cls"

    else:

        comando = "clear"

    os.system(comando)


def Banner(Estado: str, Nombre_servidor: str, Nombre_base_de_datos: str, Documentacion: str):

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█   {texto}      Estado: {Estado}{fin+fondo}                                                 {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█   {texto}Nombre de BD: {texto_correcto}{Nombre_base_de_datos}{fin+fondo}            {texto}Colección: {texto_correcto}{Documentacion}{fin+fondo}      {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█   {texto}    Servidor: {texto_correcto}{Nombre_servidor}{fin+fondo}                     {fin+marco}█{fin}""")


def opción_A():

    try:

        Numero1 = int(input(
            f"{marco+fondo}█                {texto}Inserte el primer valor : {fin}                      "))
        print(f"{marco+fondo}█                                                                                      █{fin}")
        Numero2 = int(input(
            f"{marco+fondo}█               {texto}Inserte el segundo Valor : {fin}                      "))

        Resultado = Numero1 + Numero2

        print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█          {texto}El resultado de la adición es :                     {Resultado:^5}                   {marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")

        return Numero1, Numero2, Resultado

    except:

        return False


def opción_B():

    try:

        Numero1 = int(input(
            f"{marco+fondo}█                {texto}Inserte el primer valor : {fin}                      "))
        print(f"{marco+fondo}█                                                                                      █{fin}")
        Numero2 = int(input(
            f"{marco+fondo}█               {texto}Inserte el segundo Valor : {fin}                      "))

        Resultado = Numero1 - Numero2

        print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█      {texto}El resultado de la sustracción es :                     {Resultado:^5}                   {marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")

        return Numero1, Numero2, Resultado

    except:

        return False


def opción_C():

    try:

        Numero1 = int(input(
            f"{marco+fondo}█                {texto}Inserte el primer valor : {fin}                      "))
        print(f"{marco+fondo}█                                                                                      █{fin}")
        Numero2 = int(input(
            f"{marco+fondo}█               {texto}Inserte el segundo Valor : {fin}                      "))

        Resultado = Numero1 * Numero2

        print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█   {texto}El resultado de la multiplicación es :                     {Resultado:^5}                   {marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")

        return Numero1, Numero2, Resultado

    except:

        return False


def opción_D():

    try:

        Numero1 = int(input(
            f"{marco+fondo}█                {texto}Inserte el primer valor : {fin}                      "))
        print(f"{marco+fondo}█                                                                                      █{fin}")
        Numero2 = int(input(
            f"{marco+fondo}█               {texto}Inserte el segundo Valor : {fin}                      "))

        Resultado = Numero1 / Numero2

        print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█          {texto}El resultado de la división es :                     {Resultado:^5}                   {marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")

        return Numero1, Numero2, Resultado

    except:

        return False


def opción_E():

    try:

        Numero1 = int(input(
            f"{marco+fondo}█                {texto}Inserte el primer valor : {fin}                      "))
        print(f"{marco+fondo}█                                                                                      █{fin}")
        Numero2 = int(input(
            f"{marco+fondo}█               {texto}Inserte el segundo Valor : {fin}                      "))
        print(f"{marco+fondo}█                                                                                      █{fin}")

        Resultado = Numero1 ** Numero2

        print(f"""{marco+fondo}█          {texto}El resultado de la potenciación es :                     {Resultado:^5}                   {marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")

        return Numero1, Numero2, Resultado

    except:

        return False


def opción_F():

    Numero1 = int(input(
        f"{marco+fondo}█               {texto}Inserte el número base : {fin}                        "))
    print(f"{marco+fondo}█                                                                                      █{fin}")

    if Numero1 > 0:

        Numero2 = int(input(
            f"{marco+fondo}█               {texto}Inserte el número raíz : {fin}                        "))
        print(f"{marco+fondo}█                                                                                      █{fin}")

        if Numero2 > 0:

            Resultado = math.pow(Numero1, 1 / Numero2)

            print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█     {texto}El resultado de la radicación es :                       {Resultado:.3f}                   {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")

    return Numero1, Numero2, Resultado


def opción_G():

    Numero1 = int(input(
        f"{marco+fondo}█                    {texto}Inserte el número que quiere verificar : {fin}              "))

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

    return Numero1, Conclusión


def opción_H():

    i = 2
    cont = 0

    Numero1 = int(input(
        f"{marco+fondo}█         {texto}Inserte el número que quiere verificar si es primo : {fin}         "))

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

    return Numero1, Conclusión


def opción_I():

    hasta = int(input(
        f"{marco+fondo}█              {texto}Inserte el numero de rango en primos que quiere ver:  {fin}         "))

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

            print(f"{marco+fondo}█{texto}{primo:^13}", end="")

        else:

            print(f"{marco+fondo}█{texto}{primo:^16}{fin+marco}█{fin}")

        lugar += 1
