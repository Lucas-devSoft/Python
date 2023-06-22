from pymongo import MongoClient
from colores import *


"""

    Genera la conexión con MongoDB Local

"""


def Conexión_Local():

    try:

        Conexión = MongoClient("mongodb://localhost:27017/")

        if Conexión.admin.command('ping'):

            return Conexión

    except:

        return False


"""

    Genera la conexión con MongoDB Atlas

"""


def Conexión_Atlas(Usuario, Password, Nombre_cluster, Identificador_cluster):

    try:

        Atlas = MongoClient(
            f"mongodb+srv://{Usuario}:{Password}@{Nombre_cluster}.{Identificador_cluster}.mongodb.net/?retryWrites=true&w=majority")

        if Atlas.admin.command("ping"):

            return Atlas

    except:

        return False


"""

    Insercion de datos

"""


def Guardar_Datos(Datos: dict, Tipo_de_conexion: str, retorna_renombre: str, Conectado: MongoClient, Conectado_atlas: MongoClient, Nombre_base_de_datos: str, Nombre_documentacion: str):

    if Tipo_de_conexion == "local":

        if retorna_renombre == "no":

            Base_de_datos = Conectado.get_database(
                name="Formularios").get_collection("Datos")

        else:

            Base_de_datos = Conectado.get_database(
                name=f"{Nombre_base_de_datos}").get_collection(f"{Nombre_documentacion}")

        if Base_de_datos.insert_one(Datos):

            return True

        else:

            return False

    elif Tipo_de_conexion == "atlas":

        if retorna_renombre == "no":

            Base_de_datos = Conectado_atlas.get_database(
                name="Formularios").get_collection("Datos")

        else:

            Base_de_datos = Conectado_atlas.get_database(
                name=f"{Nombre_base_de_datos}").get_collection(f"{Nombre_documentacion}")

        if Base_de_datos.insert_one(Datos):

            return True

        else:

            return False


"""

    Visualización de Datos

"""


def Mostrar_Datos_A(Tipo_de_conexion: str, retorna_renombre: str, Conectado: MongoClient, Conectado_atlas: MongoClient, Nombre_base_de_datos: str, Nombre_documentacion: str):

    if Tipo_de_conexion == "local" and retorna_renombre == "no":

        Documentacion = Conectado.get_database(
            name="Formularios").get_collection("Datos")

    elif Tipo_de_conexion == "atlas" and retorna_renombre == "no":

        Documentacion = Conectado_atlas.get_database(
            name="Formularios").get_collection("Datos")

    elif Tipo_de_conexion == "local" and retorna_renombre == "si":

        Documentacion = Conectado.get_database(
            name=f"{ Nombre_base_de_datos}").get_collection(f"{Nombre_documentacion}")

    elif Tipo_de_conexion == "atlas" and retorna_renombre == "si":

        Documentacion = Conectado_atlas.get_database(
            name=f"{ Nombre_base_de_datos}").get_collection(f"{Nombre_documentacion}")

    for i in Documentacion.find():

        Identificador = str(dict(i).get("_id"))
        Datos_personales = str(dict(i).get("Datos Personales"))

        Resultado = f"""{marco+fondo}█        {texto}Identificador:                 {Identificador:^25}                       {fin+marco}█{fin}
{marco+fondo}█{texto}   {Datos_personales:^30}      {fin+marco}█{fin}
{marco+fondo}█                                                                                       █{fin}""".replace("'", "").replace("{", "").replace(
            "}", "").replace(",", f"\n{marco+fondo}█{texto}").replace(".", f"     {fin+marco}█{fin}", 10)

        print(Resultado)


def Mostrar_Datos_B(Tipo_de_conexion: str, retorna_renombre: str, Conectado: MongoClient, Conectado_atlas: MongoClient, Nombre_base_de_datos: str, Nombre_documentacion: str):

    if Tipo_de_conexion == "local" and retorna_renombre == "no":

        Documentacion = Conectado.get_database(
            name="Formularios").get_collection("Datos")

    elif Tipo_de_conexion == "atlas" and retorna_renombre == "no":

        Documentacion = Conectado_atlas.get_database(
            name="Formularios").get_collection("Datos")

    elif Tipo_de_conexion == "local" and retorna_renombre == "si":

        Documentacion = Conectado.get_database(
            name=f"{ Nombre_base_de_datos}").get_collection(f"{Nombre_documentacion}")

    elif Tipo_de_conexion == "atlas" and retorna_renombre == "si":

        Documentacion = Conectado_atlas.get_database(
            name=f"{ Nombre_base_de_datos}").get_collection(f"{Nombre_documentacion}")

    for i in Documentacion.find():

        Identificador = str(dict(i).get("_id"))
        Datos_personales = str(dict(i).get("Datos Laborales"))

        Resultado = f"""{marco+fondo}█        {texto}Identificador:                 {Identificador:^25}                       {fin+marco}█{fin}
{marco+fondo}█{texto}   {Datos_personales:^30}      {fin+marco}█{fin}
{marco+fondo}█                                                                                       █{fin}""".replace("'", "").replace("{", "").replace(
            "}", "").replace(",", f"\n{marco+fondo}█{texto}").replace(".", f"     {fin+marco}█{fin}", 10)

        print(Resultado)


def Mostrar_Datos_C(Tipo_de_conexion: str, retorna_renombre: str, Conectado: MongoClient, Conectado_atlas: MongoClient, Nombre_base_de_datos: str, Nombre_documentacion: str):

    if Tipo_de_conexion == "local" and retorna_renombre == "no":

        Documentacion = Conectado.get_database(
            name="Formularios").get_collection("Datos")

    elif Tipo_de_conexion == "atlas" and retorna_renombre == "no":

        Documentacion = Conectado_atlas.get_database(
            name="Formularios").get_collection("Datos")

    elif Tipo_de_conexion == "local" and retorna_renombre == "si":

        Documentacion = Conectado.get_database(
            name=f"{ Nombre_base_de_datos}").get_collection(f"{Nombre_documentacion}")

    elif Tipo_de_conexion == "atlas" and retorna_renombre == "si":

        Documentacion = Conectado_atlas.get_database(
            name=f"{ Nombre_base_de_datos}").get_collection(f"{Nombre_documentacion}")

    for i in Documentacion.find():

        Identificador = str(dict(i).get("_id"))
        Datos_personales = str(dict(i).get("Datos Académicos"))

        Resultado = f"""{marco+fondo}█        {texto}Identificador:                 {Identificador:^25}                       {fin+marco}█{fin}
{marco+fondo}█{texto}{Datos_personales:^30}      {fin+marco}█{fin}
{marco+fondo}█                                                                                       █{fin}""".replace("'", "").replace("{", "").replace(
            "}", "").replace(",", f"\n{marco+fondo}█{texto}").replace(".", f"     {fin+marco}█{fin}", 10)

        print(Resultado)


# def Borrar_historial():

#     if Conexión.admin.command("ping"):

#         dc.delete_many({"Operación": {"$exists": True}})

#     elif Atlas.admin.command("ping"):

#         dc.delete_many({"Operación": {"$exists": True}})
