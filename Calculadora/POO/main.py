
import os
import time
import re

from getpass import getpass
from pymongo import MongoClient
from colores import *


def limpiar_pantalla():

    if os.name == 'nt':

        os.system('cls')


class Persona:

    def __init__(self, nombre):

        self.nombre = nombre

    def nombre_validar(self):

        while True:

            limpiar_pantalla()

            print(programa.cartel())

            print(f"""{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}""")

            self.nombre = input(
                f"{marco+fondo}█       {texto}Hola! Usuario bienvenido, ¿Cuál es su nombre? {fin}      ").capitalize()

            verificacion = re.search(r"[0-9]+", self.nombre)

            if not verificacion:

                print(f"""{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█                        {texto_correcto} El formato de su nombre es válido                            {fin+marco}█{fin}
{marco+fondo}█                           {texto}Siguiente paso en 5 segundos.                              {fin+marco}█{fin}
{marco}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{fin}""")

                time.sleep(5)

                return f"{texto_correcto}{self.nombre}"

            else:

                print(f"""{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█                      {error_texto} El formato de su nombre no es válido                           {fin+marco}█{fin}
{marco+fondo}█                       {texto}Se volvera a reintentar en 5 segundos.                         {fin+marco}█{fin}
{marco}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{fin}""")

                time.sleep(5)
                continue


class baseDatos:
    def __init__(self, conectividad):

        self.conectividad = conectividad

    def ConexionBD(self):

        while True:

            limpiar_pantalla()

            print(programa.cartel())

            print(f"""{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      {fin+marco}█{fin}""")

            self.conectividad = input(
                f"{marco+fondo}█  {texto}{programa.nombre} desea guardar la información en una base de datos? (Y/N) {fin}        ").upper()

            if programa.conectividad == "Y":

                while True:

                    limpiar_pantalla()

                    print(programa.cartel())

                    print(f"""{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                {texto}Menu de Conexión MongoDB.               {fin+marco}█{fin}
{marco+fondo}█                                                        █{fin}
{marco+fondo}█    {texto}1 ► Conectar a la base de datos de forma local.     {fin+marco}█{fin}
{marco+fondo}█                                                        █{fin}
{marco+fondo}█    {texto}2 ► Conectar a la base de datos en la nube.         {fin+marco}█{fin}
{marco+fondo}█                                                        █{fin}""")

                    try:

                        global opcionConexion

                        opcionConexion = int(input(
                            f"{marco+fondo}█       {texto}Respuesta : {fin}              "))

                        if opcionConexion == 1:

                            global Conexion

                            Conexion = MongoClient(
                                "mongodb://localhost:27017/")

                            if Conexion.admin.command("ping"):

                                print(f"""{marco+fondo}█                                                        █{fin}
{marco+fondo}█      {texto_correcto}Se conecto con éxito al servidor local.           {fin+marco}█{fin}
{marco+fondo}█     {texto}En 3 segundos entrará al menu de la calculadora.   {fin+marco}█{fin}
{marco}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{fin}""")

                                time.sleep(3)

                                if "Calculadora" not in Conexion.list_database_names():

                                    servidor = f"{texto_correcto}{Conexion.HOST}:{Conexion.PORT}{fin+fondo}"
                                    estado = f"{texto_correcto}Conectado{fin+fondo}"

                                    bd = Conexion["Calculadora"].create_collection(
                                        "Historial")

                                    base = list(
                                        Conexion.list_database_names())[0]
                                    documento = bd.name

                                    return f"{servidor:^57}", estado, f"{texto_correcto}{base:^10}{fin+fondo}", f"{texto_correcto}{documento}{fin+fondo}"

                                else:

                                    servidor = f"{texto_correcto}{Conexion.HOST}:{Conexion.PORT}"
                                    estado = f"{texto_correcto}Conectado"

                                    bd = Conexion["Calculadora"]["Historial"]

                                    base = list(
                                        Conexion.list_database_names())[0]
                                    documento = bd.name

                                    return f"{servidor:^57}", estado, f"{texto_correcto}{base:^10}{fin+fondo}", f"{texto_correcto}{documento}{fin+fondo}"

                        elif opcionConexion == 2:

                            while True:

                                limpiar_pantalla()

                                print(programa.cartel())

                                print(f"""{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█        {texto}Solicitud de datos de su servidor cloud         {marco}█{fin}
{marco+fondo}█                                                        █{fin}""")
                                usuario = input(
                                    f"{marco+fondo}█              {texto}Usuario : {fin}           ")
                                print(
                                    f"{marco+fondo}█                                                        █{fin}")
                                passw = getpass(
                                    f"{marco+fondo}█           {texto}Contraseña : {fin}           ")
                                print(
                                    f"{marco+fondo}█                                                        █{fin}")
                                cluster = input(
                                    f"{marco+fondo}█   {texto}Nombre del cluster : {fin}           ")
                                print(
                                    f"{marco+fondo}█                                                        █{fin}")
                                ids = input(
                                    f"{marco+fondo}█       {texto}ID del Cluster : {fin}           ")
                                print(f"""{marco+fondo}█                                                        █{fin}
{marco+fondo}█    {texto}Aguarde verificando los datos de su servidor...     {fin+marco}█{fin}""")

                                time.sleep(3)

                                try:

                                    global Atlas

                                    Atlas = MongoClient(
                                        f"mongodb+srv://{usuario}:{passw}@{cluster}.{ids}.mongodb.net/")

                                    if Atlas.admin.command("ping"):

                                        print(f"""{marco+fondo}█       {texto_correcto}Se conecto con éxito al servidor cloud.          {fin+marco}█{fin}
{marco+fondo}█     {texto}En 5 segundos entrará al menu de la calculadora.   {fin+marco}█{fin}
{marco}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{fin}""")

                                        time.sleep(5)

                                        if "Calculadora" not in Atlas.list_database_names():

                                            servidor = f"{texto_correcto}{list(Atlas.address)[0]}:{list(Atlas.address)[1]}{fin+fondo}"
                                            estado = f"{texto_correcto}Conectado{fin+fondo}"

                                            bd = Atlas["Calculadora"].create_collection(
                                                "Historial")

                                            base = list(
                                                Atlas.list_database_names())[0]
                                            documento = bd.name

                                            return servidor, estado, f"{texto_correcto}{base:^10}{fin+fondo}", f"{texto_correcto}{documento}{fin+fondo}"

                                        else:

                                            servidor = f"{texto_correcto}{Atlas.address[0]}:{Atlas.address[1]}{fin+fondo}"
                                            estado = f"{texto_correcto}Conectado"

                                            bd = Atlas["Calculadora"]["Historial"]

                                            base = list(
                                                Atlas.list_database_names())[0]
                                            documento = bd.name

                                            return servidor, estado, f"{texto_correcto}{base:^10}{fin+fondo}", f"{texto_correcto}{documento}{fin+fondo}"

                                except:

                                    print(f"""{marco+fondo}█                                                        █{fin}
{marco+fondo}█  {error_texto}Error! Ingrese correctamente los datos del servidor   {fin+marco}█{fin}
{marco+fondo}█       {texto}Se volvera a pedir sus datos en 5 segundos.      {fin+marco}█{fin}
{marco}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{fin}""")

                                    time.sleep(5)
                                    continue

                                break
                        else:

                            print(f"""{marco+fondo}█                                                        {fin+marco}█{fin}
{marco+fondo}█      {error_texto}Error, su respuesta no esta dentro del menú.      {fin+marco}█{fin}
{marco+fondo}█     {texto}Se volvera a pedir su respuesta en 5 segundos.     {fin+marco}█{fin}
{marco}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{fin}""")

                        time.sleep(5)
                        continue

                    except:

                        print(f"""{marco+fondo}█                                                        {fin+marco}█{fin}
{marco+fondo}█    {error_texto}Error, la respuesta no es numerica o es vacía.      {fin+marco}█{fin}
{marco+fondo}█    {texto}Se volvera a pedir su respuesta en 5 segundos.      {fin+marco}█{fin}
{marco}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{fin}""")
                        time.sleep(5)
                        continue

            elif self.conectividad == "N":

                vacio = f"{error_texto}N/A"
                estado = f"{error_texto}Desconectado"

                return f"{vacio:^54}", estado, f"{vacio:^20}", f"{vacio:^18}"

            else:

                print(f"""{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█                     {error_texto}¡Error! La respuesta esperada es Y/N.                            {fin+marco}█{fin}
{marco+fondo}█                  {texto}Se volvera a pedir su respuesta en 5 segundos.                      {fin+marco}█{fin}
{marco}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{fin}""")

                time.sleep(5)
                continue

    def guardarInformacion(self, nombre: str, numero1: int, numero2: int, resultado: str, operador: str):

        if opcionConexion == 1:

            if opcion >= 1 and opcion <= 4:

                bd = Conexion["Calculadora"]["Historial"]

                bd.insert_one({"Usuario": nombre.capitalize(),
                               "Numero 1": numero1,
                               "Numero 2": numero2,
                               "Resultado": resultado,
                               "Operación": operador})

                if bd.find({}):

                    print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                          {texto_correcto}El registro se guardo exitosamente.                         {fin+marco}█{fin}""")

            elif opcion == 5:

                bd = Conexion["Calculadora"]["Historial"]

                bd.insert_one({"Usuario": nombre.capitalize(),
                               "Base": numero1,
                               "Exponente": numero2,
                               "Resultado": resultado,
                               "Operación": operador})

                if bd.find({}):

                    print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                          {texto_correcto}El registro se guardo exitosamente.                         {fin+marco}█{fin}""")

            elif opcion == 6:

                bd = Conexion["Calculadora"]["Historial"]

                bd.insert_one({"Usuario": nombre.capitalize(),
                               "Radicando": numero1,
                               "Indice": numero2,
                               "Resultado": resultado,
                               "Operación": operador})

                if bd.find({}):

                    print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                          {texto_correcto}El registro se guardo exitosamente.                         {fin+marco}█{fin}""")

            elif opcion == 7:

                bd = Conexion["Calculadora"]["Historial"]

                bd.insert_one({"Usuario": nombre.capitalize(),
                               "Numero 1": numero1,
                               "Resultado": resultado,
                               "Operacion": operador, })

                if bd.find({}):

                    print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                          {texto_correcto}El registro se guardo exitosamente.                         {fin+marco}█{fin}""")

            else:

                pass

        elif opcionConexion == 2:

            if opcion >= 1 and opcion <= 4:

                bd = Atlas["Calculadora"]["Historial"]

                bd.insert_one({"Usuario": nombre.capitalize(),
                               "Numero 1": numero1,
                               "Numero 2": numero2,
                               "Resultado": resultado,
                               "Operación": operador})

                if bd.find({}):

                    print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                          {texto_correcto}El registro se guardo exitosamente.                         {fin+marco}█{fin}""")

            elif opcion == 5:

                bd = Atlas["Calculadora"]["Historial"]

                bd.insert_one({"Usuario": nombre.capitalize(),
                               "Base": numero1,
                               "Exponente": numero2,
                               "Resultado": resultado,
                               "Operación": operador})

                if bd.find({}):

                    print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                          {texto_correcto}El registro se guardo exitosamente.                         {fin+marco}█{fin}""")

            elif opcion == 6:

                bd = Atlas["Calculadora"]["Historial"]

                bd.insert_one({"Usuario": nombre.capitalize(),
                               "Radicando": numero1,
                               "Indice": numero2,
                               "Resultado": resultado,
                               "Operación": operador})

                if bd.find({}):

                    print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                          {texto_correcto}El registro se guardo exitosamente.                         {fin+marco}█{fin}""")

            elif opcion == 7:

                bd = Atlas["Calculadora"]["Historial"]

                bd.insert_one({"Usuario": nombre.capitalize(),
                               "Numero 1": numero1,
                               "Resultado": resultado,
                               "Operacion": operador, })

                if bd.find({}):

                    print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                          {texto_correcto}El registro se guardo exitosamente.                         {fin+marco}█{fin}""")

            else:

                pass


class Calculadora(Persona, baseDatos):
    def __init__(self, nombre, numero1, numero2, conectividad):
        Persona.__init__(self, nombre)
        baseDatos.__init__(self, conectividad)

        self.numero1 = numero1
        self.numero2 = numero2

    def cartel(self):

        return f"""{marco}
                     /$$                     /$$                 /$$                             
                    | $$                    | $$                | $$                             
  /$$$$$$$  /$$$$$$ | $$  /$$$$$$$ /$$   /$$| $$  /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$  /$$$$$$ 
 /$$_____/ |____  $$| $$ /$$_____/| $$  | $$| $$ |____  $$ /$$__  $$ /$$__  $$ /$$__  $$|____  $$
| $$        /$$$$$$$| $$| $$      | $$  | $$| $$  /$$$$$$$| $$  | $$| $$  \ $$| $$  \__/ /$$$$$$$
| $$       /$$__  $$| $$| $$      | $$  | $$| $$ /$$__  $$| $$  | $$| $$  | $$| $$      /$$__  $$
|  $$$$$$$|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$|  $$$$$$$|  $$$$$$$|  $$$$$$/| $$     |  $$$$$$$
 \_______/ \_______/|__/ \_______/ \______/ |__/ \_______/ \_______/ \______/ |__/      \_______/{fin}
 """

    def menuCalculadora(self, usuario: str, servidor: str, estado: str, base: str, documentacion: str):

        while True:

            global opcion

            limpiar_pantalla()

            print(programa.cartel())

            print(f"""{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█    {texto}Nombre del usuario                      {texto}Nombre del servidor                   {texto}Estado de conexión      {fin+marco}█{fin}
{marco+fondo}█          {usuario}              {servidor}         {estado}           {fin+marco}█{fin}
{marco+fondo}█                                                                                                          {fin+marco}█{fin}
{marco+fondo}█               {texto}Nombre de base de datos                              {texto}Nombre de la Documentación            {fin+marco}█{fin}
{marco+fondo}█                     {base}                                              {documentacion}                   {fin+marco}█{fin}
{marco+fondo}█                                                                                                          {fin+marco}█{fin}              
{marco+fondo}█                                     {texto}Calculadora en Python con POO                                        {fin+marco}█{fin}              
{marco+fondo}█                                                                                                          {fin+marco}█{fin}
{marco+fondo}█                   {texto}1 ► Adición          (+)                      {texto}5 ► Potencia        (b/e)                {fin+marco}█{fin}
{marco+fondo}█                                                                                                          {fin+marco}█{fin}
{marco+fondo}█                   {texto}2 ► Sustracción      (-)                      {texto}6 ► Radicación       (√)                 {fin+marco}█{fin}
{marco+fondo}█                                                                                                          {fin+marco}█{fin}
{marco+fondo}█                   {texto}3 ► Multiplicación   (*)                      {texto}7 ► ¿El número es par o impar?           {fin+marco}█{fin}
{marco+fondo}█                                                                                                          {fin+marco}█{fin}
{marco+fondo}█                   {texto}4 ► División         (/)                      {texto}8 ► Números primos                       {fin+marco}█{fin}
{marco+fondo}█                                                                                                          {fin+marco}█{fin}
{marco+fondo}█                                                {texto}9 ► Salir                                                 {fin+marco}█{fin}
{marco+fondo}█                                                                                                          {fin+marco}█{fin}""")

            try:

                opcion = int(input(
                    f"{marco+fondo}█                      {texto}Escriba su respuesta aqui : {fin}              "))

                match opcion:

                    case 1:

                        while True:

                            limpiar_pantalla()

                            print(programa.cartel())

                            print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}1 ► Adición                               (+)                    {marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")

                            try:

                                programa.numero1 = int(input(
                                    f"{marco+fondo}█                {texto}Inserte el primer valor : {fin}                      "))
                                programa.numero2 = int(input(
                                    f"{marco+fondo}█               {texto}Inserte el segundo valor : {fin}                      "))

                                operacion = "suma"

                                resultado = self.numero1 + self.numero2

                                print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█          {texto}El resultado de la adición es :                      {resultado:^4}                   {marco}█{fin}""")

                                if self.conectividad == "Y":

                                    programa.guardarInformacion(
                                        programa.nombre, programa.numero1, programa.numero2, resultado, operacion)
                                else:

                                    pass

                                print(f"""{marco+fondo}█                     {texto}Se volverá a visualizar su menú en 5 segundos.                   {fin+marco}█{fin}
{marco}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{fin}""")

                                time.sleep(5)

                            except ValueError:

                                print(f"""{marco+fondo}█                                                                                      {fin+marco}█{fin}
    {marco+fondo}█                           {error_texto}No se admiten caracteres como valor.                       {fin+marco}█{fin}
    {marco+fondo}█                   {texto}Se volverá a solicitar su respuesta en 5 segundos.                 {fin+marco}█{fin}
    {marco}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{fin}""")

                                time.sleep(5)
                                continue

                            break

                    case 2:

                        while True:

                            limpiar_pantalla()

                            print(programa.cartel())

                            print(f"""{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}2 ► Sustracción                           (-)                    {marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")

                            try:

                                programa.numero1 = int(input(
                                    f"{marco+fondo}█                {texto}Inserte el primer valor : {fin}                      "))
                                programa.numero2 = int(input(
                                    f"{marco+fondo}█               {texto}Inserte el segundo valor : {fin}                      "))

                                operacion = "resta"

                                resultado = self.numero1 - self.numero2

                                print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█      {texto}El resultado de la sustracción es :                      {resultado:^4}                   {marco}█{fin}""")

                                if self.conectividad == "Y":

                                    programa.guardarInformacion(
                                        programa.nombre, programa.numero1, programa.numero2, resultado, operacion)
                                else:

                                    pass

                                print(f"""{marco+fondo}█                     {texto}Se volverá a visualizar su menú en 5 segundos.                   {fin+marco}█{fin}
{marco}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{fin}""")

                                time.sleep(5)

                            except ValueError:

                                print(f"""{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█                           {error_texto}No se admiten caracteres como valor.                       {fin+marco}█{fin}
{marco+fondo}█                   {texto}Se volverá a solicitar su respuesta en 5 segundos.                 {fin+marco}█{fin}
{marco}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{fin}""")

                                time.sleep(5)
                                continue

                            break

                    case 3:

                        while True:

                            limpiar_pantalla()

                            print(programa.cartel())

                            print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}3 ► Multiplicación                         (*)                   {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")

                            try:

                                programa.numero1 = int(input(
                                    f"{marco+fondo}█                {texto}Inserte el primer valor : {fin}                      "))
                                programa.numero2 = int(input(
                                    f"{marco+fondo}█               {texto}Inserte el segundo valor : {fin}                      "))

                                operacion = "multiplcación"

                                resultado = self.numero1 * self.numero2

                                print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█   {texto}El resultado de la multiplicación es :                      {resultado:^4}                   {marco}█{fin}""")

                                if self.conectividad == "Y":

                                    programa.guardarInformacion(
                                        programa.nombre, programa.numero1, programa.numero2, resultado, operacion)
                                else:

                                    pass

                                print(f"""{marco+fondo}█                     {texto}Se volverá a visualizar su menú en 5 segundos.                   {fin+marco}█{fin}
{marco}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{fin}""")

                                time.sleep(5)

                            except ValueError:

                                print(f"""{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█                           {error_texto}No se admiten caracteres como valor.                       {fin+marco}█{fin}
{marco+fondo}█                   {texto}Se volverá a solicitar su respuesta en 5 segundos.                 {fin+marco}█{fin}
{marco}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{fin}""")

                                time.sleep(5)
                                continue

                            break

                    case 4:

                        while True:

                            limpiar_pantalla()

                            print(programa.cartel())

                            print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}4 ► División                               (/)                   {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")

                            try:

                                programa.numero1 = int(input(
                                    f"{marco+fondo}█                {texto}Inserte el primer valor : {fin}                      "))
                                programa.numero2 = int(input(
                                    f"{marco+fondo}█               {texto}Inserte el segundo valor : {fin}                      "))

                                operacion = "división"

                                resultado = self.numero1 / self.numero2

                                print(f"""{marco+fondo}█                                                                                      █{fin}
                {marco+fondo}█         {texto}El resultado de la división es :                      {resultado:^4}                   {marco}█{fin}""")

                                if self.conectividad == "Y":

                                    programa.guardarInformacion(
                                        programa.nombre, programa.numero1, programa.numero2, resultado, operacion)
                                else:

                                    pass

                                print(f"""{marco+fondo}█                     {texto}Se volverá a visualizar su menú en 5 segundos.                   {fin+marco}█{fin}
{marco}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{fin}""")

                                time.sleep(5)

                            except ValueError:

                                print(f"""{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█                           {error_texto}No se admiten caracteres como valor.                       {fin+marco}█{fin}
{marco+fondo}█                   {texto}Se volverá a solicitar su respuesta en 5 segundos.                 {fin+marco}█{fin}
{marco}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{fin}""")

                                time.sleep(5)
                                continue

                            except ZeroDivisionError:

                                print(f"""{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█                           {error_texto}No se puede dividir por cero.                              {fin+marco}█{fin}
{marco+fondo}█                   {texto}Se volverá a solicitar su respuesta en 5 segundos.                 {fin+marco}█{fin}
{marco}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{fin}""")

                                time.sleep(5)
                                continue

                            break

                    case 5:

                        while True:

                            limpiar_pantalla()

                            print(programa.cartel())

                            print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}5 ► Potenciación                           (b,e)                 {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")

                            try:

                                programa.numero1 = int(input(
                                    f"{marco+fondo}█                {texto}Inserte el número base : {fin}                      "))
                                programa.numero2 = int(input(
                                    f"{marco+fondo}█                  {texto}Inserte el exponente : {fin}                      "))

                                operacion = "potenciación"

                                resultado = self.numero1 ** self.numero2

                                print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█      {texto}El resultado de la potencia es :                      {resultado:^4}                      {marco}█{fin}""")

                                if self.conectividad == "Y":

                                    programa.guardarInformacion(
                                        programa.nombre, programa.numero1, programa.numero2, resultado, operacion)
                                else:

                                    pass

                                print(f"""{marco+fondo}█                     {texto}Se volverá a visualizar su menú en 5 segundos.                   {fin+marco}█{fin}
{marco}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{fin}""")

                                time.sleep(5)

                            except ValueError:

                                print(f"""{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█                           {error_texto}No se admiten caracteres como valor.                       {fin+marco}█{fin}
{marco+fondo}█                   {texto}Se volverá a solicitar su respuesta en 5 segundos.                 {fin+marco}█{fin}
{marco}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{fin}""")

                                time.sleep(5)
                                continue

                            break

                    case 6:

                        while True:

                            limpiar_pantalla()

                            print(programa.cartel())

                            print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                     {texto}6 ► Radicación                            (√)                    {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")

                            try:

                                programa.numero1 = int(input(
                                    f"{marco+fondo}█                {texto}Inserte el radicando : {fin}                      "))
                                programa.numero2 = int(input(
                                    f"{marco+fondo}█                   {texto}Inserte el indice : {fin}                      "))

                                operacion = "radicación"

                                resultado = pow(
                                    self.numero1, 1/self.numero2)

                                print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█     {texto}El resultado de la radicación es :                   {resultado:^4}                  {marco}█{fin}""")

                                if self.conectividad == "Y":

                                    programa.guardarInformacion(
                                        programa.nombre, programa.numero1, programa.numero2, resultado, operacion)
                                else:

                                    pass

                                print(f"""{marco+fondo}█                     {texto}Se volverá a visualizar su menú en 5 segundos.                   {fin+marco}█{fin}
{marco}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{fin}""")

                                time.sleep(5)

                            except ValueError:

                                print(f"""{marco+fondo}█                                                                                      {fin+marco}█{fin}
    {marco+fondo}█                           {error_texto}No se admiten caracteres como valor.                       {fin+marco}█{fin}
    {marco+fondo}█                   {texto}Se volverá a solicitar su respuesta en 5 segundos.                 {fin+marco}█{fin}
    {marco}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{fin}""")

                                time.sleep(5)
                                continue

                            break

                    case 7:

                        while True:

                            limpiar_pantalla()

                            print(programa.cartel())

                            print(f"""
    {marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
    {marco+fondo}█                                                                                      █{fin}
    {marco+fondo}█                         {texto}7 ► ¿El número es par o impar?                               {fin+marco}█{fin}
    {marco+fondo}█                                                                                      █{fin}""")

                            try:

                                programa.numero1 = int(input(
                                    f"{marco+fondo}█                {texto}Inserte el número a verificar: {fin}                      "))

                                operacion = "¿El número es par o impar?"

                                if self.numero1 % 2 == 0:

                                    resultado = "Número par"

                                    print(f"""{marco+fondo}█                                                                                      █{fin}
    {marco+fondo}█                            {texto}El número {self.numero1} esta dentro de los pares.                     {fin+marco}█{fin}""")

                                    if self.conectividad == "Y":

                                        programa.guardarInformacion(
                                            programa.nombre, programa.numero1, programa.numero2, resultado, operacion)
                                    else:

                                        pass

                                    print(f"""{marco+fondo}█                     {texto}Se volverá a visualizar su menú en 5 segundos.                   {fin+marco}█{fin}
{marco}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{fin}""")

                                    time.sleep(5)

                                else:

                                    resultado = "Numero impar"

                                    print(f"""{marco+fondo}█                                                                                      █{fin}
                {marco+fondo}█                          {texto}El número {self.numero1} esta dentro de los impares.                     {fin+marco}█{fin}""")

                                    if self.conectividad == "Y":

                                        programa.guardarInformacion(
                                            programa.nombre, programa.numero1, programa.numero2, resultado, operacion)
                                    else:

                                        pass

                                    print(f"""{marco+fondo}█                     {texto}Se volverá a visualizar su menú en 5 segundos.                   {fin+marco}█{fin}
{marco}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{fin}""")

                                    time.sleep(5)

                            except ValueError:

                                print(f"""{marco+fondo}█                                                                                      {fin+marco}█{fin}
    {marco+fondo}█                           {error_texto}No se admiten caracteres como valor.                       {fin+marco}█{fin}
    {marco+fondo}█                   {texto}Se volverá a solicitar su respuesta en 5 segundos.                 {fin+marco}█{fin}
    {marco}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{fin}""")

                                time.sleep(5)
                                continue

                            break

                    case 8:

                        while True:

                            limpiar_pantalla()

                            print(programa.cartel())

                            print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                              {texto}8 ► Rango de Números primos.                            {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")

                            try:

                                programa.numero1 = int(input(
                                    f"{marco+fondo}█                {texto}Inserte el rango de números: {fin}                      "))

                                primos = []

                                for numero in range(2, self.numero1 + 1):

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

                                        print(
                                            f"{marco+fondo}█{texto}{primo:^13}", end="")

                                    else:

                                        print(
                                            f"{marco+fondo}█{texto}{primo:^16}{fin+marco}█{fin}")

                                    lugar += 1

                                print(f"""\n{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█                     {texto}Se volverá a visualizar su menú en 5 segundos.                   {fin+marco}█{fin}
{marco}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{fin}""")

                                time.sleep(5)

                            except ValueError:

                                print(f"""{marco+fondo}█                                                                                      {fin+marco}█{fin}
{marco+fondo}█                           {error_texto}No se admiten caracteres como valor.                       {fin+marco}█{fin}
{marco+fondo}█                   {texto}Se volverá a solicitar su respuesta en 5 segundos.                 {fin+marco}█{fin}
{marco}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{fin}""")

                                time.sleep(5)
                                continue

                            break

                    case 9:

                        contador = 6

                        while not contador == 1:

                            contador -= 1

                            print(
                                f"Saliendo del programa en {contador}...")

                            time.sleep(1)

                    case _:

                        print(f"""{marco+fondo}█                                                                                                          {fin+marco}█{fin}
{marco+fondo}█                                {error_texto}Error, el valor insertado no está en el menu.                             {fin+marco}█{fin}
{marco+fondo}█                                {texto}Se volvera a pedir la respuesta en 5 segundos.                            {fin+marco}█{fin}
{marco}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{fin}""")

                        time.sleep(5)
                        continue

            except:

                print(f"""{marco+fondo}█                                                                                                          {fin+marco}█{fin}
{marco+fondo}█                                {error_texto}Error, la respuesta no es numerica o es vacía.                            {fin+marco}█{fin}
{marco+fondo}█                                {texto}Se volvera a pedir la respuesta en 5 segundos.                            {fin+marco}█{fin}
{marco}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{fin}""")
                time.sleep(5)



if __name__ == "__main__":

    # Instanciando el objeto para crear la calculadora
    programa = Calculadora(None, None, None, None)

    # Comienzo del programa
    while True:

        usuario = programa.nombre_validar()

        servidor, estado, base, documento = programa.ConexionBD()[0:4]

        programa.menuCalculadora(
            usuario, servidor, estado, base, documento)

        break
