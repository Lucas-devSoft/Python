from colores import *
from conexion import *
from errores import *
from menu_desplazamiento import *
from mensajes import *
from correo import *

estado_A = f"{error_texto}INCOMPLETO"
estado_B = f"{error_texto}INCOMPLETO"
estado_C = f"{error_texto}INCOMPLETO"

while True:

    Limpiar_consola()  # logica.py
    Cartel()  # mensaje.py

    Mensaje_de_conexion()  # mensajes.py

    retorno_si_no = Menu_Si_No()  # menu_desplazamiento.py

    respuesta = retorno_si_no

    if respuesta == "si":

        while True:

            Limpiar_consola()  # logica.py  # logica.py
            Cartel()  # mensaje.py  # logica.py

            Mensaje_tipo_de_conexion()  # mensajes.py

            retorno_tipo_conexion = Menu_Local_Atlas()  # menu_desplazamiento.py

            Tipo_de_conexion = retorno_tipo_conexion

            if Tipo_de_conexion == "local":

                retorno_conexion = Conexión_Local()  # conexion.py

                global Conectado

                Conectado = retorno_conexion

                if Conectado:

                    while True:

                        Limpiar_consola()  # logica.py  # logica.py
                        Cartel()  # mensaje.py  # logica.py

                        Renombrar_base_de_datos()  # mensajes.py

                        retorna_renombre = Menu_Si_No_Conexion()  # menu_desplazamiento.py

                        if retorna_renombre == "si":

                            while True:

                                Limpiar_consola()  # logica.py  # logica.py
                                Cartel()  # mensaje.py  # logica.py

                                Creando_nombre_de_la_base_de_datos()  # mensajes.py

                                retorno_nombre_bd = Datos_del_nombre_de_la_base_de_datos()  # logica.py

                                if retorno_nombre_bd == False:

                                    Error_Creacion_BD()  # errores.py

                                else:

                                    Nombre_base_de_datos, Nombre_documentacion = retorno_nombre_bd[0:2]

                                    if Nombre_base_de_datos not in Conectado.list_database_names():

                                        Conectado.get_database(
                                            name=f"{Nombre_base_de_datos}").create_collection(
                                            name=f"{Nombre_documentacion}")

                                        Creacion_exitosa()  # mensajes.py

                                    else:

                                        Base_de_datos_existente()  # mensajes.py

                                    Nombre_servidor = Conectado.address

                                    Version = Conectado.server_info()[
                                        'version']

                                    Estado = f"{texto_correcto}Conectado"
                                    Nombre_servidor = f"{texto_correcto}{Nombre_servidor}                                ".replace(
                                        ",", ":").replace("(", "").replace(")", "").replace("'", "")
                                    Version = f"{texto_correcto}{Version} "
                                    Nombre_base_de_datos = f"{texto_correcto}{Nombre_base_de_datos}"
                                    Nombre_documentacion = f"{texto_correcto}{Nombre_documentacion}"

                                    break

                        elif retorna_renombre == "no":

                            if "Formularios" not in Conectado.list_database_names():

                                Conectado.Formularios.create_collection(
                                    name="Datos")

                            Nombre_servidor = Conectado.address

                            Version = Conectado.server_info()[
                                'version']

                            Nombre_base_de_datos = Conectado.list_database_names()[
                                0]

                            Nombre_documentacion = Conectado.Formularios.list_collection_names()[
                                0]

                            Estado = f"{texto_correcto}Conectado"
                            Nombre_servidor = f"{texto_correcto}{Nombre_servidor}                                ".replace(
                                ",", ":").replace("(", "").replace(")", "").replace("'", "")
                            Version = f"{texto_correcto}{Version} "
                            Nombre_base_de_datos = f"{texto_correcto}{Nombre_base_de_datos}"
                            Nombre_documentacion = f"{texto_correcto}{Nombre_documentacion}"

                        else:

                            Error_Respuesta()  # errores.py
                            continue

                        break

                else:

                    Error_de_conexion()  # errores.py
                    continue

            elif Tipo_de_conexion == "atlas":

                while True:

                    Limpiar_consola()  # logica.py  # logica.py
                    Cartel()  # mensaje.py  # logica.py

                    Mensaje_cuenta_atlas()  # mensajes.py

                    retorno_cuenta_atlas = Cuenta_de_usuario_atlas()  # logica.py

                    Usuario, Password, Nombre_cluster, Identificador_cluster = retorno_cuenta_atlas[
                        0:4]

                    retorno_Atlas = Conexión_Atlas(Usuario, Password, Nombre_cluster, Identificador_cluster)

                    global Conectado_atlas

                    Conectado_atlas = retorno_Atlas

                    if Conectado_atlas:

                        while True:

                            Limpiar_consola()  # logica.py  # logica.py
                            Cartel()  # mensaje.py  # logica.py

                            Mensaje_estando_adentro_atlas(
                                Usuario, Nombre_cluster)  # mensajes.py

                            retorna_renombre = Menu_Si_No_Conexion()  # menu_desplazamiento.py

                            if retorna_renombre == "si":

                                while True:

                                    Limpiar_consola()  # logica.py  # logica.py
                                    Cartel()  # mensaje.py  # logica.py

                                    Creando_nombre_de_la_base_de_datos()  # mensajes.py

                                    retorno_nombre_bd = Datos_del_nombre_de_la_base_de_datos()  # logica.py

                                    if retorno_nombre_bd == False:

                                        Error_Creacion_BD()  # errores.py

                                    else:

                                        Nombre_base_de_datos, Nombre_documentacion = retorno_nombre_bd[
                                            0:2]

                                        if Nombre_base_de_datos not in Conectado_atlas.list_database_names():

                                            Conectado_atlas.get_database(
                                                name=f"{Nombre_base_de_datos}").create_collection(
                                                name=f"{Nombre_documentacion}")

                                            Creacion_exitosa()  # mensajes.py

                                        else:

                                            Base_de_datos_existente()  # mensajes.py

                                        Nombre_servidor = Conectado_atlas.address

                                        Version = Conectado_atlas.server_info()[
                                            'version']

                                        Estado = f"{texto_correcto}Conectado"
                                        Nombre_servidor = f"{texto_correcto}{Nombre_servidor}".replace(
                                            ",", ":").replace("(", "").replace(")", "").replace("'", "").replace(" ", "")
                                        Version = f"{texto_correcto}{Version} "
                                        Nombre_base_de_datos = f"{texto_correcto}{Nombre_base_de_datos}"
                                        Nombre_documentacion = f"{texto_correcto}{Nombre_documentacion}"

                                    break

                            elif retorna_renombre == "no":

                                if "Formularios" not in Conectado_atlas.list_database_names():

                                    Conectado_atlas.Formularios.create_collection(
                                        name="Datos")

                                Nombre_servidor = Conectado_atlas.address

                                Version = Conectado_atlas.server_info()[
                                    'version']

                                Nombre_base_de_datos = Conectado_atlas.list_database_names()[
                                    0]

                                Nombre_documentacion = Conectado_atlas.Formularios.list_collection_names()[
                                    0]

                                Estado = f"{texto_correcto}Conectado"
                                Nombre_servidor = f"{texto_correcto}{Nombre_servidor}".replace(
                                    ",", ":").replace("(", "").replace(")", "").replace("'", "").replace(" ", "")
                                Version = f"{texto_correcto}{Version} "
                                Nombre_base_de_datos = f"{texto_correcto}{Nombre_base_de_datos}"
                                Nombre_documentacion = f"{texto_correcto}{Nombre_documentacion}"

                            else:

                                Error_Respuesta()  # errores.py
                                continue

                            break

                    else:

                        Error_de_conexion_Atlas()  # errores.py
                        continue

                    break

            else:

                Error_Tipo_Conexión()  # errores.py
                continue

            break

    elif respuesta == "no":

        Estado = f"{error_texto}Desconectado"
        Version = f"{error_texto}N/A"
        Nombre_servidor = f"{error_texto}N/A                                             "
        Nombre_base_de_datos = f"{error_texto}N/A"
        Nombre_documentacion = f"{error_texto}N/A          "

        pass

    else:

        Error_Respuesta()  # errores.py
        continue

    break

while not (estado_A == f"{texto_correcto}COMPLETADO" and estado_B == f"{texto_correcto}COMPLETADO" and estado_C == f"{texto_correcto}COMPLETADO"):

    Limpiar_consola()  # logica.py
    Cartel()  # mensaje.py

    retorno_formulario = Menu_formulario(Estado, Version, Nombre_servidor, Nombre_base_de_datos,
                                         Nombre_documentacion, estado_A, estado_B, estado_C)  # mensajes.py

    if retorno_formulario == "A" and not estado_A == f"{texto_correcto}COMPLETADO":

        while True:

            Limpiar_consola()  # logica.py
            Cartel()  # mensaje.py

            retorna_A = opcion_A()

            if retorna_A:

                Nombre_Apellido, Estado_civil, Genero, Fecha_Nacimiento, Edad, Nacionalidad, Provincia, Localidad, Codigo_Postal, Celular, Correo = retorna_A[
                    0:11]

                Mensaje_formulario_completado()  # mensajes.py

                retorno_volver = Menu_atras()  # menu_desplazamiento.py

                if retorno_volver == "volver":

                    estado_A = f"{texto_correcto}COMPLETADO"
                    break

                elif retorno_volver == "fin":

                    Mensaje_Agradecimiento()  # mensajes.py

                else:

                    Error_menu_atras()  # errores.py
                    continue
            else:

                Error_Campo()  # errores.py
                continue

            break

    elif retorno_formulario == "B" and not estado_B == f"{texto_correcto}COMPLETADO":

        while True:

            Limpiar_consola()  # logica.py
            Cartel()  # mensaje.py

            retorno_B = opcion_B()

            if retorno_B:

                Nombre_empresa, Puesto_trabajo, Tiempo_trabajo, Ingreso_Laboral, Egreso_Laboral, Descripcion = retorno_B[
                    0:6]

                Mensaje_formulario_completado()  # mensajes.py

                retorno_volver = Menu_atras()  # menu_desplazamiento.py

                if retorno_volver == "volver":

                    estado_B = f"{texto_correcto}COMPLETADO"
                    break

                elif retorno_volver == "fin":

                    Mensaje_Agradecimiento()  # mensajes.py

                else:

                    Error_menu_atras()  # errores.py
                    continue

            else:

                Error_Campo()  # errores.py
                continue

            break

    elif retorno_formulario == "C" and not estado_C == f"{texto_correcto}COMPLETADO":

        while True:

            Limpiar_consola()  # logica.py
            Cartel()  # mensaje.py

            retorna_C = opcion_C()

            if retorna_C:

                Nombre_Institucion, Nombre_Titulo, Orientacion, Inicio_Academico, Egreso_Academico, Turno = retorna_C[
                    0:6]

                Mensaje_formulario_completado()  # mensajes.py

                retorno_volver = Menu_atras()  # menu_desplazamiento.py

                if retorno_volver == "volver":

                    estado_C = f"{texto_correcto}COMPLETADO"
                    break

                elif retorno_volver == "fin":

                    Mensaje_Agradecimiento()  # mensajes.py

                else:

                    Error_menu_atras()  # errores.py
                    continue

            else:

                Error_Campo()  # errores.py
                continue

            break

    else:

        while True:

            if retorno_formulario != "A" and retorno_formulario != "B" and retorno_formulario != "C":

                Error_Menu()
                break

            elif estado_A == f"{texto_correcto}COMPLETADO" or estado_B == f"{texto_correcto}COMPLETADO" or estado_C == f"{texto_correcto}COMPLETADO":

                Mensaje_formulario_ya_completado()  # mensajes.py
                break

    while estado_A == f"{texto_correcto}COMPLETADO" and estado_B == f"{texto_correcto}COMPLETADO" and estado_C == f"{texto_correcto}COMPLETADO":

        Limpiar_consola()  # logica.py
        Cartel()  # mensaje.py

        Menu_formulario_completado(Estado, Version, Nombre_servidor, Nombre_base_de_datos,
                                   Nombre_documentacion, estado_A, estado_B, estado_C)  # mensajes.py

        retorno_desplazamiento = Menu_de_desplazamiento_con_conexion()  # menu_desplazamiento.py

        if retorno_desplazamiento == "reset":

            estado_A = f"{error_texto}INCOMPLETO"
            estado_B = f"{error_texto}INCOMPLETO"
            estado_C = f"{error_texto}INCOMPLETO"

            pass

        elif retorno_desplazamiento == "guardar":

            if Tipo_de_conexion == "local":

                Conectado_atlas = False

            else:

                Conectado = False

            Guardar_Datos(Tipo_de_conexion, retorna_renombre, Conectado, Nombre_base_de_datos, Nombre_documentacion, Conectado_atlas, Nombre_Apellido, Estado_civil, Genero, Fecha_Nacimiento, Edad, Nacionalidad, Provincia, Localidad,
                          Codigo_Postal, Celular, Correo, Nombre_empresa, Puesto_trabajo, Tiempo_trabajo, Ingreso_Laboral, Egreso_Laboral, Descripcion, Nombre_Institucion, Nombre_Titulo, Orientacion, Inicio_Academico, Egreso_Academico, Turno)

            while True:

                Limpiar_consola()  # logica.py
                Cartel()  # mensaje.py

                Menu_formulario_completado(
                    Estado, Version, Nombre_servidor, Nombre_base_de_datos, Nombre_documentacion, estado_A, estado_B, estado_C)  # mensajes.py

                retorno_visualizacion = Menu_de_desplazamiento_visualizacion()  # menu_desplazamiento.py

                if retorno_visualizacion == "volver":

                    break

                elif retorno_visualizacion == "a":

                    Limpiar_consola()  # logica.py
                    Cartel()  # mensaje.py

                    if Tipo_de_conexion == "local":

                        Mensaje_de_visualizacion_local_personales()

                    elif Tipo_de_conexion == "atlas":

                        Mensaje_de_visualizacion_atlas_personales()

                    Mostrar_Datos_A(
                        Tipo_de_conexion, retorna_renombre, Conectado, Conectado_atlas, Nombre_base_de_datos, Nombre_documentacion)

                    retorno_volver = Menu_atras()  # menu_desplazamiento.py

                    if retorno_volver == "volver":

                        continue

                    elif retorno_volver == "fin":

                        Mensaje_Agradecimiento()  # mensajes.py

                    else:

                        Error_menu_atras()  # errores.py

                elif retorno_visualizacion == "b":

                    Limpiar_consola()  # logica.py
                    Cartel()  # mensaje.py

                    if Tipo_de_conexion == "local":

                        Mensaje_de_visualizacion_local_laborales()

                    elif Tipo_de_conexion == "atlas":

                        Mensaje_de_visualizacion_atlas_laborales()

                    Mostrar_Datos_B(
                        Tipo_de_conexion, retorna_renombre, Conectado, Conectado_atlas, Nombre_base_de_datos, Nombre_documentacion)

                    retorno_volver = Menu_atras()  # menu_desplazamiento.py

                    if retorno_volver == "volver":

                        continue

                    elif retorno_volver == "fin":

                        Mensaje_Agradecimiento()  # mensajes.py

                    else:

                        Error_menu_atras()  # errores.py

                elif retorno_visualizacion == "c":

                    Limpiar_consola()  # logica.py
                    Cartel()  # mensaje.py

                    if Tipo_de_conexion == "local":

                        Mensaje_de_visualizacion_local_academico()

                    elif Tipo_de_conexion == "atlas":

                        Mensaje_de_visualizacion_atlas_academico()

                    Mostrar_Datos_C(
                        Tipo_de_conexion, retorna_renombre, Conectado, Conectado_atlas, Nombre_base_de_datos, Nombre_documentacion)

                    retorno_volver = Menu_atras()  # menu_desplazamiento.py

                    if retorno_volver == "volver":

                        continue

                    elif retorno_volver == "fin":

                        Mensaje_Agradecimiento()  # mensajes.py

                    else:

                        Error_menu_atras()  # errores.py

                else:

                    Error_Menu_Desplazamiento_Visualizacion()  # errores.py

        elif retorno_desplazamiento == "exportar":

            retorno_exportacion = Exportacion_de_Formularios(Nombre_Apellido, Estado_civil, Genero, Fecha_Nacimiento, Edad, Nacionalidad, Provincia, Localidad, Codigo_Postal, Celular, Correo, Nombre_empresa,
                                                             Puesto_trabajo, Tiempo_trabajo, Ingreso_Laboral, Egreso_Laboral, Descripcion, Nombre_Institucion, Nombre_Titulo, Orientacion, Inicio_Academico, Egreso_Academico, Turno)

            if retorno_exportacion:

                Mensaje_exportacion_correcta()  # mensajes.py

            else:

                Mensaje_exportacion_incorrecta()  # mensajes.py

        elif retorno_desplazamiento == "enviar":

            while True:

                Limpiar_consola()  # logica.py
                Cartel()  # mensaje.py

                Mensaje_correo_electronico()  # mensajes.py

                retorno_correo = Cuenta_de_acceso()  # Correo.py

                while retorno_correo == 535:

                    Mensaje_error_cuenta()  # mensajes.py

                    input()

                    break

                else:

                    if retorno_correo:

                        Limpiar_consola()  # logica.py
                        Cartel()  # mensaje.py

                        Correo_electronico = retorno_correo

                        Mensaje_envio_de_mensaje(
                            Correo_electronico)  # mensajes.py

                        Enviar_Mensaje(Correo_electronico)  # Correo.py

                        input()

        else:

            Error_Menu_Desplazamiento_Formularios_Completos()  # errores.py

#

#             retorno_exportacion = Exportacion_Formularios(Nombre_Apellido, Estado_civil, Genero, Fecha_Nacimiento, Edad, Nacionalidad, Provincia, Localidad, Codigo_Postal, Celular, Correo, Nombre_empresa,
#                                                           Puesto_trabajo, Tiempo_trabajo, Ingreso_Laboral, Egreso_Laboral, Descripcion, Nombre_Institucion, Nombre_Titulo, Orientacion, Inicio_Academico, Egreso_Academico, Turno)

#             if retorno_exportacion:

#                 print(
#                     f"\t\t{texto_correcto}EL archivo se creo con exito!. ENTER para continuar.")

#             else:

#                 print(
#                     f"\t\t{error_texto}EL archivo no se creo con exito!. ENTER para continuar.")

#             input()
#             continue

#         elif resultados == "enviar":

#             pass

#         else:

#             Error_Menu_Desplazamiento_Formularios_Completos()
