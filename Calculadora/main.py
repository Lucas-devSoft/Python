""" Importaciones de Módulos """

from menu_desplazamiento import *
from mensajes import *
from errores import *
from conexion import *
from logica import *
from colores import *
import re

"""  Comienzo del programa """

while True:

    # logica.py
    Limpieza_consola()

    # mensajes.py
    Cartel()

    # mensajes.py
    nombre = Nombre()

    verificación = re.findall("[\W\d]+", nombre)

    if not verificación:

        while True:

            # logica.py
            Limpieza_consola()

            # mensajes.py
            Cartel()

            # mensajes.py
            Base_de_datos(nombre)

            # menu_desplazamiento.py
            retorno_respuesta = Si_No()

            if retorno_respuesta == "si":

                while True:

                    # logica.py
                    Limpieza_consola()

                    # mensajes.py
                    Cartel()

                    # mensajes.py
                    Tipo_de_conexion()

                    # menu_desplazamiento.py
                    retorno_tipo_conexion = Local_atlas()

                    if retorno_tipo_conexion == "local":

                        # conexión.py
                        Conexion_local = Conexión_Local()

                        if Conexion_local:

                            while True:

                                # logica.py
                                Limpieza_consola()

                                # mensajes.py
                                Cartel()

                                # mensajes.py
                                Creando_BD()

                                # menu_desplazamiento.py
                                retorno_BD = Si_No()

                                if retorno_BD == "si":

                                    # logica.py
                                    Limpieza_consola()

                                    # mensajes.py
                                    Cartel()

                                    # mensajes.py
                                    Base_de_datos_nueva()

                                    # conexion.py
                                    retorno_nombre = Renombre_Base_de_datos()

                                    if retorno_nombre:

                                        Nombre_de_base_datos, Documentacion = retorno_nombre[0:2]

                                        if Nombre_de_base_datos not in Conexion_local.list_database_names():

                                            Conexion_local.get_database(
                                                name=f"{Nombre_de_base_datos}").create_collection(name=f"{Documentacion}")

                                            # mensajes.py
                                            Creada_con_exito()

                                        else:

                                            # mensajes.py
                                            Base_existente()

                                    """
                                        Trae la BD creada por el usuario para el Banner
                                    """

                                    Estado = "Conectado"
                                    Estado = f"{texto_correcto}{Estado:^20}"
                                    Nombre_servidor = f"{texto_correcto}{Conexion_local.HOST}:{Conexion_local.PORT}"
                                    Nombre_servidor = f"{texto_correcto}{Nombre_servidor:^57}"

                                    for i in Conexion_local.list_database_names():

                                        if i == Nombre_de_base_datos:

                                            Nombre_de_base_de_datos = i

                                    Documentacion = Conexion_local.get_database(
                                        name=f"{Nombre_de_base_datos}").list_collection_names()[0]

                                    Nombre_de_base_de_datos = f"{texto_correcto}{Nombre_de_base_de_datos:^20}"
                                    Documentacion = f"{texto_correcto}{Documentacion:^20}"

                                elif retorno_BD == "no":

                                    if "Calculadora" not in Conexion_local.list_database_names():

                                        Conexion_local.Calculadora.create_collection(
                                            "Historial")

                                    """
                                        Trae la BD por defecto para el Banner
                                    
                                    """
                                    Estado = "Conectado"
                                    Estado = f"{texto_correcto}{Estado:^20}"
                                    Nombre_servidor = f"{texto_correcto}{Conexion_local.HOST}:{Conexion_local.PORT}"
                                    Nombre_servidor = f"{texto_correcto}{Nombre_servidor:^57}"

                                    for i in Conexion_local.list_database_names():

                                        if i == "Calculadora":

                                            Nombre_de_base_de_datos = i

                                    Documentacion = Conexion_local.Calculadora.list_collection_names()[
                                        0]

                                    Nombre_de_base_de_datos = f"{texto_correcto}{Nombre_de_base_de_datos:^20}"
                                    Documentacion = f"{texto_correcto}{Documentacion:^20}"

                                else:

                                    # errores.py
                                    Error_si_no()
                                    continue

                                break

                    elif retorno_tipo_conexion == "atlas":

                        while True:

                            # logica.py
                            Limpieza_consola()

                            # mensajes.py
                            Cartel()

                            # mensajes.py
                            Cuenta_atlas()

                            # conexion.py
                            Conexion_atlas = MongoDB_atlas()

                            if Conexion_atlas:

                                while True:

                                    # logica.py
                                    Limpieza_consola()

                                    # mensajes.py
                                    Cartel()

                                    Usuario, Nombre_cluster = Conexion_atlas[1:3]
                                    Conexion_atlas = Conexion_atlas[0]

                                    # mensajes.py
                                    Genera_base_de_datos_atlas(
                                        Usuario, Nombre_cluster)

                                    # menu_desplazamiento.py
                                    retorno_BD = Si_No()

                                    if retorno_BD == "si":

                                        # logica.py
                                        Limpieza_consola()

                                        # mensajes.py
                                        Cartel()

                                        # mensajes.py
                                        Creando_base_de_datos_atlas()

                                        # conexion.py
                                        retorno_nombre = Renombre_Base_de_datos()

                                        if retorno_nombre:

                                            Nombre_de_base_de_datos, Documentacion = retorno_nombre[0:2]

                                            if Nombre_de_base_de_datos not in Conexion_atlas.list_database_names():

                                                Conexion_atlas.get_database(
                                                    name=f"{Nombre_de_base_de_datos}").create_collection(name=f"{Documentacion}")

                                                # mensajes.py
                                                Creada_con_exito()

                                            else:

                                                # mensajes.py
                                                Base_existente()

                                        """
                                            Trae la BD creada por el usuario para el Banner
                                            
                                        """

                                        Estado = "Conectado"
                                        Estado = f"{texto_correcto}{Estado:^20}"
                                        Nombre_servidor = f"{texto_correcto}{Conexion_atlas.address}".replace("(", "").replace(")", "").replace(
                                            "'", "").replace(",", ":").replace(" ", "")
                                        Nombre_servidor = f"{texto_correcto}{Nombre_servidor:^45}"

                                        for i in Conexion_atlas.list_database_names():

                                            if i == Nombre_de_base_de_datos:

                                                Nombre_de_base_de_datos = i

                                        Documentacion = Conexion_atlas.get_database(
                                            name=f"{Nombre_de_base_de_datos}").list_collection_names()[0]

                                        Nombre_de_base_de_datos = f"{texto_correcto}{Nombre_de_base_de_datos:^20}"
                                        Documentacion = f"{texto_correcto}{Documentacion:^20}"

                                    elif retorno_BD == "no":

                                        if "Calculadora" not in Conexion_atlas.list_database_names():

                                            Conexion_atlas.Calculadora.create_collection(
                                                "Historial")

                                        """
                                            Trae la BD por defecto para el Banner
                                        
                                        """

                                        Estado = "Conectado"
                                        Estado = f"{texto_correcto}{Estado:^20}"
                                        Nombre_servidor = f"{texto_correcto}{Conexion_atlas.address}".replace("(", "").replace(")", "").replace(
                                            "'", "").replace(",", ":").replace(" ", "")
                                        Nombre_servidor = f"{texto_correcto}{Nombre_servidor:^30}"

                                        for i in Conexion_atlas.list_database_names():

                                            if i == "Calculadora":

                                                Nombre_de_base_de_datos = i

                                        Documentacion = Conexion_atlas.Calculadora.list_collection_names()[
                                            0]
                                        Nombre_de_base_de_datos = f"{texto_correcto}{Nombre_de_base_de_datos:^20}"
                                        Documentacion = f"{texto_correcto}{Documentacion:^20}"

                                    else:

                                        # errores.py
                                        Error_si_no()
                                        continue

                                    break
                            else:

                                # mensajes.py
                                Mensaje_de_error_atlas()
                                continue

                            break

                    else:

                        # errores.py
                        Error_Tipo_de_Conexión()
                        continue

                    break

            elif retorno_respuesta == "no":

                Estado = f"{error_texto}Desconectado        "
                Nombre_servidor = f"{error_texto}N/A                                             "
                Nombre_de_base_de_datos = f"{error_texto}N/A"
                Documentacion = f"{error_texto}N/A                                  "

            else:

                # errores.py
                Error_si_no()
                continue

            break
    else:

        # errores.py
        Error_Nombre()
        continue

    while True:

        # logica.py
        Limpieza_consola()

        # mensajes.py
        Cartel()

        # conexion.py
        Banner(Estado, Nombre_servidor, Nombre_de_base_de_datos,
               Documentacion)

        # mensajes.py
        retorno_menu = Menu()

        if retorno_menu == "A":

            while True:

                # logica.py
                Limpieza_consola()

                # mensajes.py
                Cartel()

                # mensajes.py
                Mensaje_suma()

                # logica.py
                retorna_A = opción_A()

                if retorna_A:

                    if retorno_respuesta == "no":

                        # mensajes.py
                        Mensaje_recordatorio_sin_conexion()

                        # menu_desplazamiento.py
                        retorno_menu = Menu_atras()

                        if retorno_menu == "volver":

                            break

                        elif retorno_menu == "fin":

                            # conexion.py
                            Mensaje_de_Agradecimiento()

                    else:

                        if retorno_respuesta == "si":

                            if retorno_tipo_conexion == "local":

                                numero1, numero2, resultado = retorna_A[0:3]

                                Operacion = "+"

                                # mensajes.py
                                Mensaje_historial_local()

                                # conexion.py
                                Ingreso_de_datos_AF_local(
                                    retorno_BD, Conexion_local, nombre, numero1, Operacion, numero2, resultado)

                                # conexion.py
                                Mostrar_datos_local(retorno_BD, Conexion_local)

                                # menu_desplazamiento.py
                                retorno_desplazamiento = Menu_desplazamiento_historial()

                                if retorno_desplazamiento == "limpiar":

                                    # conexion.py
                                    Limpiar_datos(retorno_BD, Conexion_local)

                                    # mensajes.py
                                    Mensaje_Borrado_exitoso()

                                    break

                                elif retorno_desplazamiento == "volver":

                                    break

                                else:

                                    # errores.py
                                    Error_Menu_desplazamiento_limpiar()

                            elif retorno_tipo_conexion == "atlas":

                                numero1, numero2, resultado = retorna_A[0:3]

                                Operacion = "+"

                                # conexion.py
                                Ingreso_de_datos_AF_atlas(
                                    retorno_BD, Conexion_atlas, nombre, numero1, Operacion, numero2, resultado)

                                # mensajes.py
                                Mensaje_historial_atlas()

                                # conexion.py
                                Mostrar_datos_atlas(retorno_BD, Conexion_atlas)

                                # menu_desplazamiento.py
                                retorno_desplazamiento = Menu_desplazamiento_historial()

                                if retorno_desplazamiento == "limpiar":

                                    # conexion.py
                                    Limpiar_datos(retorno_BD, Conexion_atlas)

                                    # mensajes.py
                                    Mensaje_Borrado_exitoso()

                                    break

                                elif retorno_desplazamiento == "volver":

                                    break

                                else:

                                    # errores.py
                                    Error_Menu_desplazamiento_limpiar()
                else:

                    # errores.py
                    Mensaje_de_Error_Interno()

        elif retorno_menu == "B":

            while True:

                # logica.py
                Limpieza_consola()

                # mensajes.py
                Cartel()

                # mensajes.py
                Mensaje_resta()

                # logica.py
                retorna_B = opción_B()

                if retorna_B:

                    if retorno_respuesta == "no":

                        # mensajes.py
                        Mensaje_recordatorio_sin_conexion()

                        # menu_desplazamiento.py
                        retorno_menu = Menu_atras()

                        if retorno_menu == "volver":

                            break

                        elif retorno_menu == "fin":

                            # conexion.py
                            Mensaje_de_Agradecimiento()

                    else:

                        if retorno_respuesta == "si":

                            if retorno_tipo_conexion == "local":

                                numero1, numero2, resultado = retorna_B[0:3]

                                Operacion = "-"

                                # conexion.py
                                Ingreso_de_datos_AF_local(
                                    retorno_BD, Conexion_local, nombre, numero1, Operacion, numero2, resultado)

                                # mensajes.py
                                Mensaje_historial_local()

                                # conexion.py
                                Mostrar_datos_local(retorno_BD, Conexion_local)

                                # menu_desplazamiento.py
                                retorno_desplazamiento = Menu_desplazamiento_historial()

                                if retorno_desplazamiento == "limpiar":

                                    # conexion.py
                                    Limpiar_datos(retorno_BD, Conexion_local)

                                    # mensajes.py
                                    Mensaje_Borrado_exitoso()

                                    break

                                elif retorno_desplazamiento == "volver":

                                    break

                                else:

                                    # errores.py
                                    Error_Menu_desplazamiento_limpiar()

                            elif retorno_tipo_conexion == "atlas":

                                numero1, numero2, resultado = retorna_B[0:3]

                                Operacion = "-"

                                # conexion.py
                                Ingreso_de_datos_AF_atlas(
                                    retorno_BD, Conexion_atlas, nombre, numero1, Operacion, numero2, resultado)

                                # mensajes.py
                                Mensaje_historial_atlas()

                                # conexion.py
                                Mostrar_datos_atlas(retorno_BD, Conexion_atlas)

                                # menu_desplazamiento.py
                                retorno_desplazamiento = Menu_desplazamiento_historial()

                                if retorno_desplazamiento == "limpiar":

                                    # conexion.py
                                    Limpiar_datos(retorno_BD, Conexion_atlas)

                                    # mensajes.py
                                    Mensaje_Borrado_exitoso()

                                    break

                                elif retorno_desplazamiento == "volver":

                                    break

                                else:

                                    # errores.py
                                    Error_Menu_desplazamiento_limpiar()

                else:

                    # errores.py
                    Mensaje_de_Error_Interno()

        elif retorno_menu == "C":

            while True:

                # logica.py
                Limpieza_consola()

                # mensajes.py
                Cartel()

                # mensajes.py
                Mensaje_multi()

                # logica.py
                retorna_C = opción_C()

                if retorna_C:

                    if retorno_respuesta == "no":

                        # mensajes.py
                        Mensaje_recordatorio_sin_conexion()

                        # menu_desplazamiento.py
                        retorno_menu = Menu_atras()

                        if retorno_menu == "volver":

                            break

                        elif retorno_menu == "fin":

                            # conexion.py
                            Mensaje_de_Agradecimiento()

                    else:

                        if retorno_respuesta == "si":

                            if retorno_tipo_conexion == "local":

                                numero1, numero2, resultado = retorna_C[0:3]

                                Operacion = "*"

                                # conexion.py
                                Ingreso_de_datos_AF_local(
                                    retorno_BD, Conexion_local, nombre, numero1, Operacion, numero2, resultado)

                                # mensajes.py
                                Mensaje_historial_local()

                                # conexion.py
                                Mostrar_datos_local(retorno_BD, Conexion_local)

                                # menu_desplazamiento.py
                                retorno_desplazamiento = Menu_desplazamiento_historial()

                                if retorno_desplazamiento == "limpiar":

                                    # conexion.py
                                    Limpiar_datos(retorno_BD, Conexion_local)

                                    # mensajes.py
                                    Mensaje_Borrado_exitoso()

                                    break

                                elif retorno_desplazamiento == "volver":

                                    break

                                else:

                                    # errores.py
                                    Error_Menu_desplazamiento_limpiar()

                            elif retorno_tipo_conexion == "atlas":

                                numero1, numero2, resultado = retorna_C[0:3]

                                Operacion = "*"

                                # conexion.py
                                Ingreso_de_datos_AF_atlas(
                                    retorno_BD, Conexion_atlas, nombre, numero1, Operacion, numero2, resultado)

                                # mensajes.py
                                Mensaje_historial_atlas()

                                # conexion.py
                                Mostrar_datos_atlas(retorno_BD, Conexion_atlas)

                                # menu_desplazamiento.py
                                retorno_desplazamiento = Menu_desplazamiento_historial()

                                if retorno_desplazamiento == "limpiar":

                                    # conexion.py
                                    Limpiar_datos(retorno_BD, Conexion_atlas)

                                    # mensajes.py
                                    Mensaje_Borrado_exitoso()

                                    break

                                elif retorno_desplazamiento == "volver":

                                    break

                                else:

                                    # errores.py
                                    Error_Menu_desplazamiento_limpiar()

                else:

                    # errores.py
                    Mensaje_de_Error_Interno()

        elif retorno_menu == "D":

            while True:

                # logica.py
                Limpieza_consola()

                # mensajes.py
                Cartel()

                # mensajes.py
                Mensaje_div()

                # logica.py
                retorna_D = opción_D()

                if retorna_D:

                    if retorno_respuesta == "no":

                        # mensajes.py
                        Mensaje_recordatorio_sin_conexion()

                        # menu_desplazamiento.py
                        retorno_menu = Menu_atras()

                        if retorno_menu == "volver":

                            break

                        elif retorno_menu == "fin":

                            # conexion.py
                            Mensaje_de_Agradecimiento()

                    else:

                        if retorno_respuesta == "si":

                            if retorno_tipo_conexion == "local":

                                numero1, numero2, resultado = retorna_D[0:3]

                                Operacion = "/"

                                # conexion.py
                                Ingreso_de_datos_AF_local(
                                    retorno_BD, Conexion_local, nombre, numero1, Operacion, numero2, resultado)

                                # mensajes.py
                                Mensaje_historial_local()

                                # conexion.py
                                Mostrar_datos_local(retorno_BD, Conexion_local)

                                # menu_desplazamiento.py
                                retorno_desplazamiento = Menu_desplazamiento_historial()

                                if retorno_desplazamiento == "limpiar":

                                    # conexion.py
                                    Limpiar_datos(retorno_BD, Conexion_local)

                                    # mensajes.py
                                    Mensaje_Borrado_exitoso()

                                    break

                                elif retorno_desplazamiento == "volver":

                                    break

                                else:

                                    # errores.py
                                    Error_Menu_desplazamiento_limpiar()

                            elif retorno_tipo_conexion == "atlas":

                                numero1, numero2, resultado = retorna_D[0:3]

                                Operacion = "/"

                                # conexion.py
                                Ingreso_de_datos_AF_atlas(
                                    retorno_BD, Conexion_atlas, nombre, numero1, Operacion, numero2, resultado)

                                # mensajes.py
                                Mensaje_historial_local()

                                # conexion.py
                                Mostrar_datos_atlas(retorno_BD, Conexion_atlas)

                                # menu_desplazamiento.py
                                retorno_desplazamiento = Menu_desplazamiento_historial()

                                if retorno_desplazamiento == "limpiar":

                                    # conexion.py
                                    Limpiar_datos(retorno_BD, Conexion_atlas)

                                    # mensajes.py
                                    Mensaje_Borrado_exitoso()

                                    break

                                elif retorno_desplazamiento == "volver":

                                    break

                                else:

                                    # errores.py
                                    Error_Menu_desplazamiento_limpiar()

                else:

                    # errores.py
                    Mensaje_de_Error_Interno()

        elif retorno_menu == "E":

            while True:

                # logica.py
                Limpieza_consola()

                # mensajes.py
                Cartel()

                # mensajes.py
                Mensaje_pote()

                # logica.py
                retorna_E = opción_E()

                if retorna_E:

                    if retorno_respuesta == "no":

                        # mensajes.py
                        Mensaje_recordatorio_sin_conexion()

                        # menu_desplazamiento.py
                        retorno_menu = Menu_atras()

                        if retorno_menu == "volver":

                            break

                        elif retorno_menu == "fin":

                            # conexion.py
                            Mensaje_de_Agradecimiento()

                    else:

                        if retorno_respuesta == "si":

                            if retorno_tipo_conexion == "local":

                                numero1, numero2, resultado = retorna_E[0:3]

                                Operacion = "b/e"

                                # conexion.py
                                Ingreso_de_datos_AF_local(
                                    retorno_BD, Conexion_local, nombre, numero1, Operacion, numero2, resultado)

                                # mensajes.py
                                Mensaje_historial_local()

                                # conexion.py
                                Mostrar_datos_local(retorno_BD, Conexion_local)

                                # menu_desplazamiento.py
                                retorno_desplazamiento = Menu_desplazamiento_historial()

                                if retorno_desplazamiento == "limpiar":

                                    # conexion.py
                                    Limpiar_datos(retorno_BD, Conexion_local)

                                    # mensajes.py
                                    Mensaje_Borrado_exitoso()

                                    break

                                elif retorno_desplazamiento == "volver":

                                    break

                                else:

                                    # errores.py
                                    Error_Menu_desplazamiento_limpiar()

                            elif retorno_tipo_conexion == "atlas":

                                numero1, numero2, resultado = retorna_E[0:3]

                                Operacion = "b/e"

                                # conexion.py
                                Ingreso_de_datos_AF_atlas(
                                    retorno_BD, Conexion_atlas, nombre, numero1, Operacion, numero2, resultado)

                                # mensajes.py
                                Mensaje_historial_atlas()

                                # conexion.py
                                Mostrar_datos_atlas(retorno_BD, Conexion_atlas)

                                # menu_desplazamiento.py
                                retorno_desplazamiento = Menu_desplazamiento_historial()

                                if retorno_desplazamiento == "limpiar":

                                    # conexion.py
                                    Limpiar_datos(retorno_BD, Conexion_atlas)

                                    # mensajes.py
                                    Mensaje_Borrado_exitoso()

                                    break

                                elif retorno_desplazamiento == "volver":

                                    break

                                else:

                                    # errores.py
                                    Error_Menu_desplazamiento_limpiar()

                else:

                    # errores.py
                    Mensaje_de_Error_Interno()

        elif retorno_menu == "F":

            while True:

                # logica.py
                Limpieza_consola()

                # mensajes.py
                Cartel()

                # mensajes.py
                Mensaje_radi()

                # logica.py
                retorna_F = opción_F()

                if retorna_F:

                    if retorno_respuesta == "no":

                        # mensajes.py
                        Mensaje_recordatorio_sin_conexion()

                        # menu_desplazamiento.py
                        retorno_menu = Menu_atras()

                        if retorno_menu == "volver":

                            break

                        elif retorno_menu == "fin":

                            # conexion.py
                            Mensaje_de_Agradecimiento()

                    else:

                        if retorno_respuesta == "si":

                            if retorno_tipo_conexion == "local":

                                numero1, numero2, resultado = retorna_F[0:3]

                                Operacion = "√"

                                # conexion.py
                                Ingreso_de_datos_AF_local(
                                    retorno_BD, Conexion_local, nombre, numero1, Operacion, numero2, resultado)

                                # mensajes.py
                                Mensaje_historial_local()

                                # conexion.py
                                Mostrar_datos_local(retorno_BD, Conexion_local)

                                # menu_desplazamiento.py
                                retorno_desplazamiento = Menu_desplazamiento_historial()

                                if retorno_desplazamiento == "limpiar":

                                    # conexion.py
                                    Limpiar_datos(retorno_BD, Conexion_local)

                                    # mensajes.py
                                    Mensaje_Borrado_exitoso()

                                    break

                                elif retorno_desplazamiento == "volver":

                                    break

                                else:

                                    # errores.py
                                    Error_Menu_desplazamiento_limpiar()

                            elif retorno_tipo_conexion == "atlas":

                                numero1, numero2, resultado = retorna_F[0:3]

                                Operacion = "√"

                                # conexion.py
                                Ingreso_de_datos_AF_atlas(
                                    retorno_BD, Conexion_atlas, nombre, numero1, Operacion, numero2, resultado)

                                # mensajes.py
                                Mensaje_historial_atlas()

                                # conexion.py
                                Mostrar_datos_atlas(retorno_BD, Conexion_atlas)

                                # menu_desplazamiento.py
                                retorno_desplazamiento = Menu_desplazamiento_historial()

                                if retorno_desplazamiento == "limpiar":

                                    # conexion.py
                                    Limpiar_datos(retorno_BD, Conexion_atlas)

                                    # mensajes.py
                                    Mensaje_Borrado_exitoso()

                                    break

                                elif retorno_desplazamiento == "volver":

                                    break

                                else:

                                    # errores.py
                                    Error_Menu_desplazamiento_limpiar()

                else:

                    # errores.py
                    Mensaje_de_Error_Interno()

        elif retorno_menu == "G":

            while True:

                # logica.py
                Limpieza_consola()

                # mensajes.py
                Cartel()

                # mensajes.py
                Mensaje_paridad()

                # logica.py
                retorna_G = opción_G()

                if retorna_G:

                    if retorno_respuesta == "no":

                        # mensajes.py
                        Mensaje_recordatorio_sin_conexion()

                        # menu_desplazamiento.py
                        retorno_menu = Menu_atras()

                        if retorno_menu == "volver":

                            break

                        elif retorno_menu == "fin":

                            # conexion.py
                            Mensaje_de_Agradecimiento()

                    else:

                        if retorno_respuesta == "si":

                            if retorno_tipo_conexion == "local":

                                numero1, resultado = retorna_G[0:2]

                                Operacion = "paridad"

                                # conexion.py
                                Ingreso_de_datos_GH_local(
                                    retorno_BD, Conexion_local, nombre, numero1, resultado)

                                # mensajes.py
                                Mensaje_historial_local()

                                # conexion.py
                                Mostrar_datos_local(retorno_BD, Conexion_local)

                                # menu_desplazamiento.py
                                retorno_desplazamiento = Menu_desplazamiento_historial()

                                if retorno_desplazamiento == "limpiar":

                                    # conexion.py
                                    Limpiar_datos(retorno_BD, Conexion_local)

                                    # mensajes.py
                                    Mensaje_Borrado_exitoso()

                                    break

                                elif retorno_desplazamiento == "volver":

                                    break

                                else:

                                    # errores.py
                                    Error_Menu_desplazamiento_limpiar()

                            elif retorno_tipo_conexion == "atlas":

                                numero1, resultado = retorna_G[0:2]

                                Operacion = "paridad"

                                # conexion.py
                                Ingreso_de_datos_GH_atlas(
                                    retorno_BD, Conexion_local, nombre, numero1, resultado)

                                # mensajes.py
                                Mensaje_historial_atlas()

                                # conexion.py
                                Mostrar_datos_atlas(retorno_BD, Conexion_atlas)

                                # menu_desplazamiento.py
                                retorno_desplazamiento = Menu_desplazamiento_historial()

                                if retorno_desplazamiento == "limpiar":

                                    # conexion.py
                                    Limpiar_datos(retorno_BD, Conexion_atlas)

                                    # mensajes.py
                                    Mensaje_Borrado_exitoso()

                                    break

                                elif retorno_desplazamiento == "volver":

                                    break

                                else:

                                    # errores.py
                                    Error_Menu_desplazamiento_limpiar()

                else:

                    # errores.py
                    Mensaje_de_Error_Interno()

        elif retorno_menu == "H":

            while True:

                # logica.py
                Limpieza_consola()

                # mensajes.py
                Cartel()

                # mensajes.py
                Mensaje_primo()

                # logica.py
                retorna_H = opción_H()

                if retorna_H:

                    if retorno_respuesta == "no":

                        # mensajes.py
                        Mensaje_recordatorio_sin_conexion()

                        # menu_desplazamiento.py
                        retorno_menu = Menu_atras()

                        if retorno_menu == "volver":

                            break

                        elif retorno_menu == "fin":

                            # conexion.py
                            Mensaje_de_Agradecimiento()

                    else:

                        if retorno_respuesta == "si":

                            if retorno_tipo_conexion == "local":

                                numero1, resultado = retorna_H[0:2]

                                Operacion = "paridad"

                                # conexion.py
                                Ingreso_de_datos_GH_local(
                                    retorno_BD, Conexion_local, nombre, numero1, resultado)

                                # mensajes.py
                                Mensaje_historial_local()

                                # conexion.py
                                Mostrar_datos_local(retorno_BD, Conexion_local)

                                # menu_desplazamiento.py
                                retorno_desplazamiento = Menu_desplazamiento_historial()

                                if retorno_desplazamiento == "limpiar":

                                    # conexion.py
                                    Limpiar_datos(retorno_BD, Conexion_local)

                                    # mensajes.py
                                    Mensaje_Borrado_exitoso()

                                    break

                                elif retorno_desplazamiento == "volver":

                                    break

                                else:

                                    # errores.py
                                    Error_Menu_desplazamiento_limpiar()

                            elif retorno_tipo_conexion == "atlas":

                                numero1, resultado = retorna_H[0:2]

                                Operacion = "paridad"

                                # conexion.py
                                Ingreso_de_datos_GH_atlas(
                                    retorno_BD, Conexion_local, nombre, numero1, resultado)

                                # mensajes.py
                                Mensaje_historial_atlas()

                                # conexion.py
                                Mostrar_datos_atlas(retorno_BD, Conexion_atlas)

                                # menu_desplazamiento.py
                                retorno_desplazamiento = Menu_desplazamiento_historial()

                                if retorno_desplazamiento == "limpiar":

                                    # conexion.py
                                    Limpiar_datos(retorno_BD, Conexion_atlas)

                                    # mensajes.py
                                    Mensaje_Borrado_exitoso()

                                    break

                                elif retorno_desplazamiento == "volver":

                                    break

                                else:

                                    # errores.py
                                    Error_Menu_desplazamiento_limpiar()

                else:

                    # errores.py
                    Mensaje_de_Error_Interno()

        elif retorno_menu == "I":

            while True:

                # logica.py
                Limpieza_consola()

                # mensajes.py
                Cartel()

                # mensajes.py
                Mensaje_primos_rango()

                # logica.py
                retorna_I = opción_I()

                # menu_desplazamiento.py
                retorno_respuesta = Menu_atras()

                if retorno_respuesta == "volver":

                    break

                elif retorno_respuesta == "fin":

                    # mensajes.py
                    Mensaje_de_Agradecimiento()

                    break

                else:

                    # errores.py
                    Mensaje_error_atras()

        else:

            # errores.py
            Error_Mensaje_de_Menu()
