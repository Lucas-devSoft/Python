from datetime import date
from getpass import getpass  # hace invisible visualmente las contraseñas
import time
import re
import os
import json


from colores import *


"""
    logica de la aplicacion

"""


def opcion_A():

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█                         {texto}Formulario de datos personales                                {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
    Nombre_Apellido = input(
        f"{marco+fondo}█                     {texto}Nombre y Apellido : {fin}        ")

    verificacion = re.search(r"^[^\d.,\-{}]*$", Nombre_Apellido)

    if verificacion:

        print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
        Estado_civil = input(
            f"{marco+fondo}█                          {texto}Estado Civil : {fin}        ")

        verificacion = re.search(r"^[^\d.,\-{}]*$", Estado_civil)

        if verificacion:

            print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
            Genero = input(
                f"{marco+fondo}█                                {texto}Genero : {fin}        ")

            verificacion = re.search(r"^[^\d.,\-{}]*$", Genero)

            if verificacion:

                try:

                    print(
                        f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                    Fecha_Nacimiento = date(int(input(f"{marco+fondo}█              {texto}Año de Nacimiento (YYYY) : {fin}        ")),
                                            int(input(
                                                f"{marco+fondo}█                {texto}Mes de Nacimiento (MM) : {fin}        ")),
                                            int(input(f"{marco+fondo}█                {texto}Dia de Nacimiento (DD) : {fin}        ")))

                    Fecha_actual = date.today()
                    Edad = Fecha_actual.year - Fecha_Nacimiento.year

                    Fecha_Nacimiento = Fecha_Nacimiento.strftime("%d/%m/%Y")

                except:

                    return False

                print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                Nacionalidad = input(
                    f"{marco+fondo}█                          {texto}Nacionalidad : {fin}        ")

                verificacion = re.search(r"^[^\d.,\-{}]*$", Nacionalidad)

                if verificacion:

                    print(
                        f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                    Provincia = input(
                        f"{marco+fondo}█                             {texto}Provincia : {fin}        ")

                    verificacion = re.search(r"^[^\d.,\-{}]*$", Provincia)

                    if verificacion:

                        print(
                            f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                        Localidad = input(
                            f"{marco+fondo}█                             {texto}Localidad : {fin}        ")

                        verificacion = re.search(r"^[^\d.,\-{}]*$", Localidad)

                        if verificacion:

                            print(
                                f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                            Codigo_Postal = input(
                                f"{marco+fondo}█                         {texto}Código Postal : {fin}        ")

                            verificacion = re.search(
                                r"^[^\D.,\-{}]{4}$", Codigo_Postal)

                            if verificacion:

                                print(
                                    f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                                Celular = input(
                                    f"{marco+fondo}█        {texto}(sin 0 ni 15) Teléfono Celular : {fin}        ")

                                verificacion = re.search(
                                    r"^[^\D.,\-{}]{10}$", Celular)

                                if verificacion:

                                    print(
                                        f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                                    Correo = input(
                                        f"{marco+fondo}█                    {texto}Correo Electrónico : {fin}        ")

                                    verificacion = re.search(
                                        r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", Correo)

                                    if verificacion:

                                        return Nombre_Apellido, Estado_civil, Genero, Fecha_Nacimiento, Edad, Nacionalidad, Provincia, Localidad, Codigo_Postal, Celular, Correo

                                    else:

                                        return False

                                else:

                                    return False

                            else:

                                return False

                        else:

                            return False

                    else:

                        return False

                else:

                    return False

            else:

                return False

        else:

            return False

    else:

        return False


def opcion_B():

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█                         {texto}Formulario de datos laborales                                 {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")

    Trabajo = input(
        f"{marco+fondo}█         {texto}¿Se encuentra trabajando actualmente? (si/no) : {fin}            ")

    if Trabajo == 'si':

        print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
        Nombre_empresa = input(
            f"{marco+fondo}█                                  {texto}Nombre de la empresa : {fin}           ")

        verificacion = re.search(r"^[^\d.,\-{}]*$", Nombre_empresa)

        if verificacion:

            print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
            Puesto_trabajo = input(
                f"{marco+fondo}█                                     {texto}Puesto de trabajo : {fin}           ")

            verificacion = re.search(r"^[^\d.,\-{}]*$", Puesto_trabajo)

            if verificacion:

                print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                Tiempo_trabajo = input(
                    f"{marco+fondo}█                 {texto}(Full Time/Part Time) Jornada Laboral : {fin}           ")

                verificacion = re.search(r"^[^\d.,\-{}]*$", Tiempo_trabajo)

                if verificacion:

                    print(
                        f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                    Ingreso = input(
                        f"{marco+fondo}█                                        {texto}Año de ingreso : {fin}           ")

                    verificacion = re.search(r"^[^\D.,\-{}]{4}$", Ingreso)

                    if verificacion:

                        print(
                            f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                        Egreso = input(
                            f"{marco+fondo}█                        {texto}(Año/Actualidad) Año de egreso : {fin}           ")

                        verificacion = re.search(r"^[^\D.,\-{}]{4}$", Egreso)

                        if verificacion:

                            try:

                                print(
                                    f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                                Sueldo = float(input(
                                    f"{marco+fondo}█                                     {texto}Salario en brutos : {fin}           "))

                            except:

                                return False

                            if Sueldo:

                                return Nombre_empresa, Puesto_trabajo, Tiempo_trabajo, Ingreso, Egreso, Sueldo

                            else:

                                return False

                        else:

                            return False

                    else:

                        return False

            else:

                return False

        else:

            return False

    elif Trabajo == 'no':

        print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
        Nombre_empresa = input(
            f"{marco+fondo}█            {texto}Nombre la ultima empresa en la que trabajo : {fin}            ")

        verificacion = re.search(r"^[^\d.,\-{}]*$", Nombre_empresa)

        if verificacion:

            print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
            Puesto_trabajo = input(
                f"{marco+fondo}█                                     {texto}Puesto de trabajo : {fin}            ")

            verificacion = re.search(r"^[^\d.,\-{}]*$", Puesto_trabajo)

            if verificacion:

                print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                Tiempo_trabajo = input(
                    f"{marco+fondo}█       {texto}(Full Time/Part Time) Jornada Laboral trabajada : {fin}            ")

                verificacion = re.search(r"^[^\d.,\-{}]*$", Tiempo_trabajo)

                if verificacion:

                    print(
                        f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                    Ingreso = input(
                        f"{marco+fondo}█                                       {texto}Año que ingresó : {fin}            ")

                    verificacion = re.search(r"^[^\D.,\-{}]{4}$", Ingreso)

                    if verificacion:

                        print(
                            f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                        Egreso = input(
                            f"{marco+fondo}█                                        {texto}Año que egresó : {fin}            ")

                        verificacion = re.search(r"^[^\D.,\-{}]{4}$", Egreso)

                        if verificacion:

                            print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█                       {texto}Breve descripcion de las tareas realizadas                      {marco+fondo}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")

                            Descripcion = input(f"{marco+fondo}█    {texto}")

                            verificacion = re.search(
                                r"^[^\d\-{}]*$", Descripcion)

                            if verificacion:

                                return Nombre_empresa, Puesto_trabajo, Tiempo_trabajo, Ingreso, Egreso, Descripcion

                            else:

                                return False

                        else:

                            return False

                    else:

                        return False

                else:

                    return False

            else:

                return False

        else:

            return False

    else:

        return False


def opcion_C():

    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█                         {texto}Formulario de datos académicos                                {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
    Estudio = input(
        f"{marco+fondo}█   {texto}¿Se encuentra estudiando actualmente? (si/no) : {fin}           ")

    if Estudio == "si":

        print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
        Nombre_Intitucion = input(
            f"{marco+fondo}█                        {texto}Nombre de la institución : {fin}           ")

        verificacion = re.search(r"^[^.,\-{}]*$", Nombre_Intitucion)

        if verificacion:

            print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
            Nombre_Titulo = input(
                f"{marco+fondo}█                               {texto}Nombre del título : {fin}           ")

            verificacion = re.search(r"^[^\d.,\-{}]*$", Nombre_Titulo)

            if verificacion:

                print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                Orientacion = input(
                    f"{marco+fondo}█                           {texto}Orientación Académica : {fin}           ")

                verificacion = re.search(r"^[^\d.,\-{}]*$", Orientacion)

                if verificacion:

                    print(
                        f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                    Inicio = input(
                        f"{marco+fondo}█                                   {texto}Año de inicio : {fin}           ")

                    verificacion = re.search(r"^[^\D.,\-{}]{4}$", Inicio)

                    if verificacion:

                        print(
                            f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                        Egreso = input(
                            f"{marco+fondo}█                  {texto}(Año/Actualidad) Año de egreso : {fin}           ")

                        verificacion = re.search(r"^[^\D.,\-{}]{4}$", Egreso)

                        if verificacion:

                            print(
                                f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                            Turno = input(
                                f"{marco+fondo}█            {texto}(Mañana/Tarde/Noche)Turno de cursada : {fin}           ")

                            verificacion = re.search(r"^[^\d.,\-{}]*$", Turno)

                            if verificacion:

                                return Nombre_Intitucion, Nombre_Titulo, Orientacion, Inicio, Egreso, Turno

                            else:

                                return False

                        else:

                            return False

                    else:

                        return False

                else:

                    return False

            else:

                return False

        else:

            return False

    elif Estudio == "no":

        print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
        Nombre_Institucion = input(
            f"{marco+fondo}█                 {texto}Nombre de la ultima institución : {fin}           ")

        verificacion = re.search(r"^[^.,\-{}]*$", Nombre_Institucion)

        if verificacion:

            print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
            Nombre_Titulo = input(
                f"{marco+fondo}█                               {texto}Nombre del título : {fin}           ")

            verificacion = re.search(r"^[^\d.,\-{}]*$", Nombre_Titulo)

            if verificacion:

                print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                Orientacion = input(
                    f"{marco+fondo}█                           {texto}Orientación Académica : {fin}           ")

                verificacion = re.search(r"^[^\d.,\-{}]*$", Orientacion)

                if verificacion:

                    print(
                        f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                    Inicio = input(
                        f"{marco+fondo}█                                   {texto}Año de inicio : {fin}           ")

                    verificacion = re.search(r"^[^\D.,\-{}]{4}$", Inicio)

                    if verificacion:

                        print(
                            f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                        Egreso = input(
                            f"{marco+fondo}█                                   {texto}Año de egreso : {fin}           ")

                        verificacion = re.search(r"^[^\D.,\-{}]{4}$", Egreso)

                        if verificacion:

                            print(
                                f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                            Turno = input(
                                f"{marco+fondo}█          {texto}(Mañana/Tarde/Noche)Turno que cursaste : {fin}           ")

                            verificacion = re.search(r"^[^\d.,\-{}]*$", Turno)

                            if verificacion:

                                return Nombre_Institucion, Nombre_Titulo, Orientacion, Inicio, Egreso, Turno

                            else:

                                return False

                        else:

                            return False

                    else:

                        return False

                else:

                    return False

            else:

                return False

        else:

            return False

    else:

        return False


"""

    logica para trabajar con la base de datos

"""


def Datos_del_nombre_de_la_base_de_datos():

    Nombre_BD = input(
        f"{marco+fondo}█           {texto}Nombre de su Base de Datos : {fin}              ")

    verificacion = re.search(r"^[^\d.,\-{}]*$", Nombre_BD)

    if verificacion:

        print(
            f"{marco+fondo}█                                                                                       █{fin}")
        Nombre_DC = input(
            f"{marco+fondo}█           {texto}Nombre de la Documentación : {fin}              ")

        verificacion = re.search(
            r"^[^\d.,\-{}]*$", Nombre_DC)

        if verificacion:

            return Nombre_BD, Nombre_DC

    return False


def Cuenta_de_usuario_atlas():

    Usuario = input(
        f"{marco+fondo}█               {texto}Nombre de usuario : {fin}                   ")
    print(f"{marco+fondo}█                                                                                       █{fin}")
    Password = getpass(
        f"{marco+fondo}█                      {texto}Contraseña : {fin}                   ")
    print(f"{marco+fondo}█                                                                                       █{fin}")
    Nombre_cluster = input(
        f"{marco+fondo}█              {texto}Nombre del cluster : {fin}                   ")
    print(f"{marco+fondo}█                                                                                       █{fin}")
    Identificador_cluster = input(
        f"{marco+fondo}█       {texto}Identificador del Cluster : {fin}                   ")
    print(f"""{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█              {texto}Aguarde estamos ingresando a su servidor de MongoDB Atlas...             {fin+marco}█{fin}""")

    time.sleep(3)

    return Usuario, Password, Nombre_cluster, Identificador_cluster


"""

    logica para trabajar con la Exportación

"""


def Exportacion_de_Formularios(Nombre_Apellido: str, Estado_civil: str, Genero: str, Fecha_Nacimiento: str, Edad: str, Nacionalidad: str, Provincia: str, Localidad: str, Codigo_Postal: str, Celular: str, Correo: str, Nombre_empresa: str, Puesto_trabajo: str, Tiempo_trabajo: str, Ingreso: int, Egreso: str, Descripcion: str, Nombre_Institucion: str, Nombre_Titulo: str, Orientacion: str, Inicio_Academico: str, Egreso_Academico: str, Turno: str):

    Datos = ({"Datos Personales": {"  Nombre y Apellido": f"{Nombre_Apellido:^58}",
                                   "       Estado Civil": f"{Estado_civil:^58}",
                                   "             Genero": f"{Genero:^58}",
                                   "Fecha de Nacimiento": f"{Fecha_Nacimiento:^58}",
                                   "               Edad": f"{Edad:^58}",
                                   "       Nacionalidad": f"{Nacionalidad:^58}",
                                   "          Provincia": f"{Provincia:^58}",
                                   "          Localidad": f"{Localidad:^58}",
                                   "      Codigo Postal": f"{Codigo_Postal:^58}",
                                   "            Celular": f"{Celular:^58}",
                                   "             Correo": f"{Correo:^58}"},
              "Datos Laborales": {"   Nombre de Empresa": f"{Nombre_empresa:^58}",
                                  "   Puesto de Trabajo": f"{Puesto_trabajo:^58}",
                                  "   Tiempo de Trabajo": f"{Tiempo_trabajo:^58}",
                                  "             Ingreso": f"{Ingreso:^58}",
                                  "              Egreso": f"{Egreso:^58}",
                                  "         Descripcion": f"{Descripcion:^58}"},
             "Datos Académicos": {"Nombre de Instituto": f"{Nombre_Institucion:^58}",
                                   "  Nombre del Título": f"{Nombre_Titulo:^58}",
                                   "        Orientación": f"{Orientacion:^58}",
                                   "  Ingreso Académico": f"{Inicio_Academico:^58}",
                                   "   Egreso Académico": f"{Egreso_Academico:^58}",
                                   "   Turno de cursada": f"{Turno:^58}"}})

    if not os.path.exists("Formularios_exportados.json"):

        with open("Formularios_exportados.json", "a", encoding="UTF-8") as f:

            json.dump(Datos, f, indent=4, ensure_ascii=False)

            return True

    elif os.path.exists("Formularios_exportados.json"):

        return False


"""

    Limpieza de la consola

"""


def Limpiar_consola():

    command = 'clear'

    if os.name in ('nt', 'dos'):  # if the machine running in windows, use command cls

        command = 'cls'

    else:

        command

    os.system(command)
