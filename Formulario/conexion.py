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


def Guardar_Datos(Tipo_de_conexion: str, retorna_renombre: str, Conectado: MongoClient, Nombre_base_de_datos: str, Nombre_documentacion: str, Conectado_atlas: MongoClient, Nombre_Apellido: str, Estado_civil: str, Genero: str, Fecha_Nacimiento: str, Edad: str, Nacionalidad: str, Provincia: str, Localidad: str, Codigo_Postal: str, Celular: str, Correo: str, Nombre_empresa: str, Puesto_trabajo: str, Tiempo_trabajo: str, Ingreso_Laboral: str, Egreso_Laboral: str, Descripcion: str, Nombre_Institucion: str, Nombre_Titulo: str, Orientacion: str, Inicio_Academico: str, Egreso_Academico: str, Turno: str):

    if Tipo_de_conexion == "local":

        if retorna_renombre == "no":

            Base_de_datos = Conectado.get_database(
                name="Formularios").get_collection("Datos")

        else:

            Base_de_datos = Conectado.get_database(
                name=f"{Nombre_base_de_datos}").get_collection(f"{Nombre_documentacion}")

        Base_de_datos.insert_one({"Datos Personales": {" Nombre y Apellido": f"{Nombre_Apellido:^58} .",
                                                       "       Estado Civil": f"{Estado_civil:^58} .",
                                                       "             Genero": f"{Genero:^58} .",
                                                       "Fecha de Nacimiento": f"{Fecha_Nacimiento:^58} .",
                                                       "               Edad": f"{Edad:^58} .",
                                                       "       Nacionalidad": f"{Nacionalidad:^58} .",
                                                       "          Provincia": f"{Provincia:^58} .",
                                                       "          Localidad": f"{Localidad:^58} .",
                                                       "      Codigo Postal": f"{Codigo_Postal:^58} .",
                                                       "            Celular": f"{Celular:^58} .",
                                                       "             Correo": f"{Correo:^58}"},
                                  "Datos Laborales": {"  Nombre de Empresa": f"{Nombre_empresa:^58} .",
                                                      "   Puesto de Trabajo": f"{Puesto_trabajo:^58} .",
                                                      "   Tiempo de Trabajo": f"{Tiempo_trabajo:^58} .",
                                                      "             Ingreso": f"{Ingreso_Laboral:^58} .",
                                                      "              Egreso": f"{Egreso_Laboral:^58} .",
                                                      "         Descripcion": f"{Descripcion:^58} "},
                                  "Datos Académicos": {"Nombre de Instituto": f"{Nombre_Institucion:^58} .",
                                                        "   Nombre del Título": f"{Nombre_Titulo:^58} .",
                                                        "         Orientación": f"{Orientacion:^58} .",
                                                        "   Ingreso Académico": f"{Inicio_Academico:^58} .",
                                                        "    Egreso Académico": f"{Egreso_Academico:^58} .",
                                                        "    Turno de cursada": f"{Turno:^58} ."}})

    elif Tipo_de_conexion == "atlas":

        if retorna_renombre == "no":

            Base_de_datos = Conectado_atlas.get_database(
                name="Formularios").get_collection("Datos")

        else:

            Base_de_datos = Conectado_atlas.get_database(
                name=f"{Nombre_base_de_datos}").get_collection(f"{Nombre_documentacion}")

            Base_de_datos.insert_one({"Datos Personales": {" Nombre y Apellido": f"{Nombre_Apellido:^63} .",
                                                           "       Estado Civil": f"{Estado_civil:^64} .",
                                                           "             Genero": f"{Genero:^64} .",
                                                           "Fecha de Nacimiento": f"{Fecha_Nacimiento:^64} .",
                                                           "               Edad": f"{Edad:^64} .",
                                                           "       Nacionalidad": f"{Nacionalidad:^64} .",
                                                           "          Provincia": f"{Provincia:^64} .",
                                                           "          Localidad": f"{Localidad:^64} .",
                                                           "      Codigo Postal": f"{Codigo_Postal:^64} .",
                                                           "            Celular": f"{Celular:^64} .",
                                                           "             Correo": f"{Correo:^64}"},
                                      "Datos Laborales": {" Nombre de Empresa": f"{Nombre_empresa:^64} .",
                                                          "   Puesto de Trabajo": f"{Puesto_trabajo:^64} .",
                                                          "   Tiempo de Trabajo": f"{Tiempo_trabajo:^64} .",
                                                          "             Ingreso": f"{Ingreso_Laboral:^64} .",
                                                          "              Egreso": f"{Egreso_Laboral:^64} .",
                                                          "         Descripcion": f"{Descripcion:^64} "},
                                      "Datos Académicos": {"Nombre de Instituto": f"{Nombre_Institucion:^64} .",
                                                            "   Nombre del Título": f"{Nombre_Titulo:^64} .",
                                                            "         Orientación": f"{Orientacion:^64} .",
                                                            "   Ingreso Académico": f"{Inicio_Academico:^64} .",
                                                            "    Egreso Académico": f"{Egreso_Academico:^64} .",
                                                            "    Turno de cursada": f"{Turno:^64} ."}})


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

        Identificador = dict(i).get("_id")

        return print(f"{marco+fondo}█       {texto}Identificador:                 {Identificador}                         {fin+marco}█{fin}\n", f"{marco+fondo}█{texto}", str(dict(i).get("Datos Personales")).replace("'", "").replace("{", "").replace(
            "}", f"       {fin+marco}█{fin}").replace(",", f"\n{marco+fondo}█{texto}").replace(".", f"      {fin+marco}█{fin}", 10))


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

        Identificador = dict(i).get("_id")

        return print(f"{marco+fondo}█       {texto}Identificador:                    {Identificador}                      {fin+marco}█{fin}\n", f"{marco+fondo}█{texto}", str(dict(i).get("Datos Laborales")).replace("'", "").replace("{", "").replace(
            "}", f"     {fin+marco}█{fin}").replace(",", f"\n{marco+fondo}█{texto}").replace(".", f"     {fin+marco}█{fin}", 5))


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

        Identificador = dict(i).get("_id")

        print(f"{marco+fondo}█       {texto}Identificador:                 {Identificador}                         {fin+marco}█{fin}\n", f"{marco+fondo}█{texto}", str(dict(i).get("Datos Académicos")).replace("'", "").replace("{", "").replace(
            "}", f"    {fin+marco}█{fin}").replace(",", f"\n{marco+fondo}█{texto}").replace(".", f"     {fin+marco}█{fin}", 5))


# def Borrar_historial():

#     if Conexión.admin.command("ping"):

#         dc.delete_many({"Operación": {"$exists": True}})

#     elif Atlas.admin.command("ping"):

#         dc.delete_many({"Operación": {"$exists": True}})
