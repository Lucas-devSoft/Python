""" Librerías (Módulos) """

import time

from pymongo import MongoClient
from getpass import getpass  # hace invisible visualmente las contraseñas
from colores import *


"""

    Base de datos local

"""


def Conexión_Local():

    try:

        Conexion = MongoClient("mongodb://localhost:27017/")

        if Conexion.admin.command("ping"):

            return Conexion

    except Exception as error:

        return error


def Renombre_Base_de_datos():

    global Nombre_DB, Nombre_DC

    print(f"{marco+fondo}█                                                                                      █{fin}")
    Nombre_DB = input(
        f"{marco+fondo}█           {texto}Nombre de la Base de Datos : {fin}              ")
    print(f"{marco+fondo}█                                                                                      █{fin}")
    Nombre_DC = input(
        f"{marco+fondo}█           {texto}Nombre de la Documentación : {fin}              ")

    return Nombre_DB, Nombre_DC


"""

    Base de datos Atlas

"""


def MongoDB_atlas():

    try:

        print(f"{marco+fondo}█                                                                                      █{fin}")
        Usuario = input(
            f"{marco+fondo}█               {texto}Nombre de usuario : {fin}                   ")
        print(f"{marco+fondo}█                                                                                      █{fin}")
        contraseña = getpass(
            f"{marco+fondo}█                      {texto}Contraseña : {fin}                   ")
        print(f"{marco+fondo}█                                                                                      █{fin}")
        Cluster = input(
            f"{marco+fondo}█              {texto}Nombre del cluster : {fin}                   ")
        print(f"{marco+fondo}█                                                                                      █{fin}")
        Identificador = input(
            f"{marco+fondo}█       {texto}Identificador del Cluster : {fin}                   ")
        print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                    {texto}Aguarde verificando los datos de su servidor..                    {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}""")

        time.sleep(3)

        global Atlas

        Atlas = MongoClient(
            f"mongodb+srv://{Usuario}:{contraseña}@{Cluster}.{Identificador}.mongodb.net/?retryWrites=true&w=majority")

        if Atlas.admin.command("ping"):

            return Atlas, Usuario, Cluster

        else:

            return False

    except Exception:

        return False


"""

    Ingresando los datos a la base de datos

"""


def Ingreso_de_datos_AF_local(creacion_db: str, Conexion_local: MongoClient, nombre: str, numero1: int, operacion: str, numero2: int, resultado: str):

    if creacion_db == "si":

        for i in Conexion_local.list_database_names():

            if i == Nombre_DB:

                Nombre_de_base_de_datos = i

        Documento = Conexion_local.get_database(
            name=Nombre_de_base_de_datos).get_collection(name=Nombre_DC)

        Documento.insert_one({"Historial": {"Nombre": nombre.capitalize(),
                                            "Numero 1": numero1,
                                            "Operador": operacion,
                                            "Numero 2": numero2,
                                            "Resultado": resultado}})

    elif creacion_db == "no":

        for i in Conexion_local.list_database_names():

            if i == "Calculadora":

                Nombre_de_base_de_datos = i

        Documento = Conexion_local.get_database(
            name=Nombre_de_base_de_datos).get_collection(name="Historial")

        Documento.insert_one({"Historial": {"Nombre": nombre.capitalize(),
                                            "Numero 1": numero1,
                                            "Operador": operacion,
                                            "Numero 2": numero2,
                                            "Resultado": resultado}})


def Ingreso_de_datos_GH_local(creacion_db: str, Conexion_local: MongoClient, nombre: str, numero1: int, operacion: str, conclusion: str):

    if creacion_db == "si":

        for i in Conexion_local.list_database_names():

            if i == Nombre_DB:

                Nombre_de_base_de_datos = i

        Documento = Conexion_local.get_database(
            name=Nombre_de_base_de_datos).get_collection(name=Nombre_DC)

        Documento.insert_one({"Historial": {"Nombre": nombre.capitalize(),
                                            "Numero 1": numero1,
                                            "Operador": operacion,
                                            "Resultado": conclusion}})

    elif creacion_db == "no":

        for i in Conexion_local.list_database_names():

            if i == "Calculadora":

                Nombre_de_base_de_datos = i

        Documento = Conexion_local.get_database(
            name=Nombre_de_base_de_datos).get_collection(name="Historial")

        Documento.insert_one({"Historial": {"Nombre": nombre.capitalize(),
                                            "Numero 1": numero1,
                                            "Operador": operacion,
                                            "Resultado": conclusion}})


def Ingreso_de_datos_AF_atlas(creacion_db: str, Conexion_atlas: MongoClient, nombre: str, numero1: int, operacion: str, numero2: int, resultado: str):

    if creacion_db == "si":

        for i in Conexion_atlas.list_database_names():

            if i == Nombre_DB:

                base_de_datos = i

        Documento = Conexion_atlas.get_database(
            name=base_de_datos).get_collection(name=Nombre_DC)

        Documento.insert_one({"Historial": {"Nombre": nombre.capitalize(),
                                            "Numero 1": numero1,
                                            "Operador": operacion,
                                            "Numero 2": numero2,
                                            "Resultado": resultado}})

    elif creacion_db == "no":

        for i in Conexion_atlas.list_database_names():

            if i == "Calculadora":

                Nombre_de_base_de_datos = i

        Documento = Conexion_atlas.get_database(
            name=Nombre_de_base_de_datos).get_collection(name="Historial")

        Documento.insert_one({"Historial": {"Nombre": nombre.capitalize(),
                                            "Numero 1": numero1,
                                            "Operador": operacion,
                                            "Numero 2": numero2,
                                            "Resultado": resultado}})


def Ingreso_de_datos_GH_atlas(creacion_db: str, Conexion_atlas: MongoClient, nombre: str, numero1: int, operacion: str, conclusion: str):

    if creacion_db == "si":

        for i in Conexion_atlas.list_database_names():

            if i == Nombre_DB:

                base_de_datos = i

        Documento = Conexion_atlas.get_database(
            name=base_de_datos).get_collection(name=Nombre_DC)

        Documento.insert_one({"Historial": {"Nombre": nombre.capitalize(),
                                            "Numero 1": numero1,
                                            "Operador": operacion,
                                            "Resultado": conclusion}})

    elif creacion_db == "no":

        for i in Conexion_atlas.list_database_names():

            if i == "Calculadora":

                Nombre_de_base_de_datos = i

        Documento = Conexion_atlas.get_database(
            name=Nombre_de_base_de_datos).get_collection(name="Historial")

        Documento.insert_one({"Historial": {"Nombre": nombre.capitalize(),
                                            "Numero 1": numero1,
                                            "Operador": operacion,
                                            "Resultado": conclusion}})


def Mostrar_datos_local(creacion_db: str, Conexion_local: MongoClient):

    if creacion_db == "si":

        documento = Conexion_local.get_database(
            name=Nombre_DB).get_collection(name=Nombre_DC)

        for i in documento.find():

            resultado = str(dict(i).get("Historial")).replace(
                "{", "").replace("}", "").replace("'", "").replace(",", "  ")

            print(
                f"{marco+fondo}█    {texto}{resultado:^75}         {marco+fondo}█{fin}")

    elif creacion_db == "no":

        documento = Conexion_local.get_database(
            name="Calculadora").get_collection(name="Historial")

        for i in documento.find():

            resultado = str(dict(i).get("Historial")).replace(
                "{", "").replace("}", "").replace("'", "").replace(",", "  ")

            print(
                f"{marco+fondo}█    {texto}{resultado:^75}         {marco+fondo}█{fin}")


def Mostrar_datos_atlas(creacion_db: str, Conexion_atlas: MongoClient):

    if creacion_db == "si":

        documento = Conexion_atlas.get_database(
            name=Nombre_DB).get_collection(name=Nombre_DC)

        for i in documento.find():

            resultado = str(dict(i).get("Historial")).replace(
                "{", "").replace("}", "").replace("'", "").replace(",", "  ")

            print(
                f"{marco+fondo}█       {texto}{resultado:^40}         {marco+fondo}█{fin}")

    elif creacion_db == "no":

        documento = Conexion_atlas.get_database(
            name="Calculadora").get_collection(name="Historial")

        for i in documento.find():

            resultado = str(dict(i).get("Historial")).replace(
                "{", "").replace("}", "").replace("'", "").replace(",", "  ")

            print(
                f"{marco+fondo}█       {texto}{resultado:^40}         {marco+fondo}█{fin}")


def Limpiar_datos_local(creacion_db: str, Conexion_local: MongoClient):

    if creacion_db == "si":

        documento = Conexion_local.get_database(
            Nombre_DB).get_collection(Nombre_DC)

        if documento.delete_many({}):

            return True

        else:

            return False

    elif creacion_db == "no":

        documento = Conexion_local.get_database(
            name="Calculadora").get_collection(name="Historial")

        if documento.delete_many({"Historial": {"$exists": True}}):

            return True

        else:

            return False


def Limpiar_datos_atlas(creacion_db: str, Conexion_atlas: MongoClient):

    if creacion_db == "si":

        documento = Conexion_atlas.get_database(
            Nombre_DB).get_collection(Nombre_DC)

        if documento.delete_many({}):

            return True

        else:

            return False

    elif creacion_db == "no":

        documento = Conexion_atlas.get_database(
            name="Calculadora").get_collection(name="Historial")

        if documento.delete_many({"Historial": {"$exists": True}}):

            return True

        else:

            return False
