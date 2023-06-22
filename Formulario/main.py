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

    # logica.py
    Limpiar_consola()

    # mensaje.py
    Cartel()

    # mensajes.py
    Mensaje_de_conexion()

    # menu_desplazamiento.py
    retorno_si_no = Menu_Si_No()

    respuesta = retorno_si_no

    if respuesta == "si":

        while True:

            # logica.py
            Limpiar_consola()

            # mensaje.py
            Cartel()

            # mensajes.py
            Mensaje_tipo_de_conexion()

            # menu_desplazamiento.py
            Tipo_de_conexion = Menu_Local_Atlas()

            if Tipo_de_conexion == "local":

                global Conectado

                # conexion.py
                Conectado = Conexión_Local()

                if Conectado:

                    while True:

                        # logica.py
                        Limpiar_consola()

                        # mensaje.py
                        Cartel()

                        # mensajes.py
                        Renombrar_base_de_datos()

                        # menu_desplazamiento.py
                        retorna_renombre = Menu_Si_No_Conexion()

                        if retorna_renombre == "si":

                            while True:

                                # logica.py
                                Limpiar_consola()

                                # mensaje.py
                                Cartel()

                                # mensajes.py
                                Creando_nombre_de_la_base_de_datos()

                                # logica.py
                                retorno_nombre_bd = Datos_del_nombre_de_la_base_de_datos()

                                if retorno_nombre_bd == False:

                                    # errores.py
                                    Error_Creacion_BD()

                                else:

                                    Nombre_base_de_datos, Nombre_documentacion = retorno_nombre_bd[0:2]

                                    if Nombre_base_de_datos not in Conectado.list_database_names():

                                        Conectado.get_database(
                                            name=f"{Nombre_base_de_datos}").create_collection(
                                            name=f"{Nombre_documentacion}")

                                        # mensajes.py
                                        Creacion_exitosa()

                                    else:

                                        # mensajes.py
                                        Base_de_datos_existente()

                                    Estado = "Conectado"
                                    Estado = f"{texto_correcto}{Estado:^30}"
                                    Nombre_servidor = str(Conectado.address).replace(
                                        ",", ":").replace("(", "").replace(")", "").replace("'", "")
                                    Nombre_servidor = f"{texto_correcto}{Nombre_servidor:^49}"

                                    for i in Conectado.list_database_names():

                                        if i == Nombre_base_de_datos:

                                            Nombre_base_de_datos = i

                                    for x in Conectado.get_database(f"{Nombre_base_de_datos}").list_collection_names():

                                        if x == Nombre_documentacion:

                                            Nombre_documentacion = x

                                    Nombre_base_de_datos = f"{texto_correcto}{Nombre_base_de_datos:^30}"
                                    Nombre_documentacion = f"{texto_correcto}{Nombre_documentacion:^13}"

                                    break

                        elif retorna_renombre == "no":

                            if "Formularios" not in Conectado.list_database_names():

                                Conectado.Formularios.create_collection(
                                    name="Datos")

                            Estado = "Conectado"
                            Estado = f"{texto_correcto}{Estado:^30}"
                            Nombre_servidor = str(Conectado.address).replace(
                                ",", ":").replace("(", "").replace(")", "").replace("'", "")
                            Nombre_servidor = f"{texto_correcto}{Nombre_servidor:^49}"

                            for i in Conectado.list_database_names():

                                if i == "Formularios":

                                    Nombre_base_de_datos = i

                            for x in Conectado.get_database(f"{Nombre_base_de_datos}").list_collection_names():

                                if x == "Datos":

                                    Nombre_documentacion = x

                            Nombre_base_de_datos = f"{texto_correcto}{Nombre_base_de_datos:^30}"
                            Nombre_documentacion = f"{texto_correcto}{Nombre_documentacion:^13}"

                        else:

                            Error_Respuesta()  # errores.py
                            continue

                        break

                else:

                    Error_de_conexion()  # errores.py
                    continue

            elif Tipo_de_conexion == "atlas":

                while True:

                    # logica.py
                    Limpiar_consola()

                    # mensaje.py
                    Cartel()

                    # mensajes.py
                    Mensaje_cuenta_atlas()

                    # logica.py
                    retorno_cuenta_atlas = Cuenta_de_usuario_atlas()

                    Usuario, Password, Nombre_cluster, Identificador_cluster = retorno_cuenta_atlas[
                        0:4]

                    global Conectado_atlas

                    Conectado_atlas = Conexión_Atlas(Usuario, Password, Nombre_cluster, Identificador_cluster)

                    if Conectado_atlas:

                        while True:

                            # logica.py
                            Limpiar_consola()

                            # mensaje.py
                            Cartel()

                            # mensajes.py
                            Mensaje_estando_adentro_atlas(
                                Usuario, Nombre_cluster)

                            # menu_desplazamiento.py
                            retorna_renombre = Menu_Si_No_Conexion()

                            if retorna_renombre == "si":

                                while True:

                                    # logica.py
                                    Limpiar_consola()

                                    # mensaje.py
                                    Cartel()

                                    # mensajes.py
                                    Creando_nombre_de_la_base_de_datos()

                                    # logica.py
                                    retorno_nombre_bd = Datos_del_nombre_de_la_base_de_datos()

                                    if retorno_nombre_bd == False:

                                        # errores.py
                                        Error_Creacion_BD()

                                    else:

                                        Nombre_base_de_datos, Nombre_documentacion = retorno_nombre_bd[
                                            0:2]

                                        if Nombre_base_de_datos not in Conectado_atlas.list_database_names():

                                            Conectado_atlas.get_database(
                                                name=f"{Nombre_base_de_datos}").create_collection(
                                                name=f"{Nombre_documentacion}")

                                            # mensajes.py
                                            Creacion_exitosa()

                                        else:

                                            # mensajes.py
                                            Base_de_datos_existente()

                                        Estado = "Conectado"
                                        Estado = f"{texto_correcto}{Estado:^30}"
                                        Nombre_servidor = str(Conectado_atlas.address).replace(
                                            ",", ":").replace("(", "").replace(")", "").replace("'", "")
                                        Nombre_servidor = f"{texto_correcto}{Nombre_servidor}"

                                        for i in Conectado_atlas.list_database_names():

                                            if i == Nombre_base_de_datos:

                                                Nombre_base_de_datos = i

                                        for x in Conectado_atlas.get_database(f"{Nombre_base_de_datos}").list_collection_names():

                                            if x == Nombre_documentacion:

                                                Nombre_documentacion = x

                                        Nombre_base_de_datos = f"{texto_correcto}{Nombre_base_de_datos:^30}"
                                        Nombre_documentacion = f"{texto_correcto}{Nombre_documentacion:^13}"

                                    break

                            elif retorna_renombre == "no":

                                if "Formularios" not in Conectado_atlas.list_database_names():

                                    Conectado_atlas.Formularios.create_collection(
                                        name="Datos")

                                Estado = "Conectado"
                                Estado = f"{texto_correcto}{Estado:^30}"
                                Nombre_servidor = str(Conectado_atlas.address).replace(
                                    ",", ":").replace("(", "").replace(")", "").replace("'", "")
                                Nombre_servidor = f"{texto_correcto}{Nombre_servidor}"

                                for i in Conectado_atlas.list_database_names():

                                    if i == "Formularios":

                                        Nombre_base_de_datos = i

                                for x in Conectado_atlas.get_database(f"{Nombre_base_de_datos}").list_collection_names():

                                    if x == "Datos":

                                        Nombre_documentacion = x

                                Nombre_base_de_datos = f"{texto_correcto}{Nombre_base_de_datos:^30}"
                                Nombre_documentacion = f"{texto_correcto}{Nombre_documentacion:^13}"

                            else:

                                # errores.py
                                Error_Respuesta()
                                continue

                            break

                    else:

                        # errores.py
                        Error_de_conexion_Atlas()
                        continue

                    break

            else:

                # errores.py
                Error_Tipo_Conexión()
                continue

            break

    elif respuesta == "no":

        Estado = "Desconectado"
        Vacio = "N/A"
        Estado = f"{error_texto}{Estado:^30}"
        Nombre_servidor = f"{error_texto}{Vacio:^49}"
        Nombre_base_de_datos = f"{error_texto}{Vacio:^30}"
        Nombre_documentacion = f"{error_texto}{Vacio:^13}"
        pass

    else:

        # errores.py
        Error_Respuesta()
        continue

    break

while not (estado_A == f"{texto_correcto}COMPLETADO" and estado_B == f"{texto_correcto}COMPLETADO" and estado_C == f"{texto_correcto}COMPLETADO"):

    # logica.py
    Limpiar_consola()

    # mensaje.py
    Cartel()

    # mensajes.py
    opcion = Menu_formulario(Estado, Nombre_servidor, Nombre_base_de_datos,
                             Nombre_documentacion, estado_A, estado_B, estado_C)

    if opcion == "A" and not estado_A == f"{texto_correcto}COMPLETADO":

        while True:

            # logica.py
            Limpiar_consola()

            # mensaje.py
            Cartel()

            # logica.py
            retorna_A = opcion_A()

            if retorna_A:

                Nombre_Apellido, Estado_civil, Genero, Fecha_Nacimiento, Edad, Nacionalidad, Provincia, Localidad, Codigo_Postal, Celular, Correo = retorna_A[
                    0:11]

                # mensajes.py
                Mensaje_formulario_completado()

                # menu_desplazamiento.py
                retorno_volver = Menu_atras()

                if retorno_volver == "volver":

                    estado_A = f"{texto_correcto}COMPLETADO"
                    break

                elif retorno_volver == "fin":

                    # mensajes.py
                    Mensaje_Agradecimiento()

                else:

                    # errores.py
                    Error_menu_atras()
                    continue
            else:

                # errores.py
                Error_Campo()
                continue

            break

    elif opcion == "B" and not estado_B == f"{texto_correcto}COMPLETADO":

        while True:

            # logica.py
            Limpiar_consola()

            # mensaje.py
            Cartel()

            # logica.py
            retorno_B = opcion_B()

            if retorno_B:

                Nombre_empresa, Puesto_trabajo, Tiempo_trabajo, Ingreso_Laboral, Egreso_Laboral, Descripcion = retorno_B[
                    0:6]

                # mensajes.py
                Mensaje_formulario_completado()

                # menu_desplazamiento.py
                retorno_volver = Menu_atras()

                if retorno_volver == "volver":

                    estado_B = f"{texto_correcto}COMPLETADO"
                    break

                elif retorno_volver == "fin":

                    # mensajes.py
                    Mensaje_Agradecimiento()

                else:

                    # errores.py
                    Error_menu_atras()
                    continue

            else:

                # errores.py
                Error_Campo()
                continue

            break

    elif opcion == "C" and not estado_C == f"{texto_correcto}COMPLETADO":

        while True:

            # logica.py
            Limpiar_consola()

            # mensaje.py
            Cartel()

            # logica.py
            retorna_C = opcion_C()

            if retorna_C:

                Nombre_Institucion, Nombre_Titulo, Orientacion, Inicio_Academico, Egreso_Academico, Turno = retorna_C[
                    0:6]

                # mensajes.py
                Mensaje_formulario_completado()

                # menu_desplazamiento.py
                retorno_volver = Menu_atras()

                if retorno_volver == "volver":

                    estado_C = f"{texto_correcto}COMPLETADO"
                    break

                elif retorno_volver == "fin":

                    # mensajes.py
                    Mensaje_Agradecimiento()

                else:

                    # errores.py
                    Error_menu_atras()
                    continue

            else:

                # errores.py
                Error_Campo()
                continue

            break

    else:

        while True:

            if opcion != "A" and opcion != "B" and opcion != "C":

                # errores.py
                Error_Menu()
                break

            elif estado_A == f"{texto_correcto}COMPLETADO" or estado_B == f"{texto_correcto}COMPLETADO" or estado_C == f"{texto_correcto}COMPLETADO":

                # mensajes.py
                Mensaje_formulario_ya_completado()

                break

    while estado_A == f"{texto_correcto}COMPLETADO" and estado_B == f"{texto_correcto}COMPLETADO" and estado_C == f"{texto_correcto}COMPLETADO" and respuesta == "si":

        # logica.py
        Limpiar_consola()

        # mensaje.py
        Cartel()

        # mensajes.py
        Menu_formulario_completado(Estado, Nombre_servidor, Nombre_base_de_datos,
                                   Nombre_documentacion, estado_A, estado_B, estado_C)

        # menu_desplazamiento.py
        retorno_desplazamiento = Menu_de_desplazamiento_con_conexion()

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

            global Datos

            Datos = Datos_de_Formularios(Nombre_Apellido, Estado_civil, Genero, Fecha_Nacimiento, Edad, Nacionalidad, Provincia, Localidad, Codigo_Postal, Celular, Correo, Nombre_empresa,
                                         Puesto_trabajo, Tiempo_trabajo, Ingreso_Laboral, Egreso_Laboral, Descripcion, Nombre_Institucion, Nombre_Titulo, Orientacion, Inicio_Academico, Egreso_Academico, Turno)

            retorno_guardado = Guardar_Datos(Datos, Tipo_de_conexion, retorna_renombre, Conectado,
                                             Conectado_atlas, Nombre_base_de_datos, Nombre_documentacion)

            if retorno_guardado:

                # mensajes.py
                Mensaje_guardado_exitosamente()

                while True:

                    # logica.py
                    Limpiar_consola()

                    # mensaje.py
                    Cartel()

                    # mensajes.py
                    Menu_formulario_completado(
                        Estado, Nombre_servidor, Nombre_base_de_datos, Nombre_documentacion, estado_A, estado_B, estado_C)

                    # menu_desplazamiento.py
                    retorno_visualizacion = Menu_de_desplazamiento_visualizacion()

                    if retorno_visualizacion == "volver":

                        break

                    elif retorno_visualizacion == "a":

                        # logica.py
                        Limpiar_consola()

                        # mensaje.py
                        Cartel()

                        if Tipo_de_conexion == "local":

                            # mensajes.py
                            Mensaje_de_visualizacion_local_personales()

                        elif Tipo_de_conexion == "atlas":

                            # mensajes.py
                            Mensaje_de_visualizacion_atlas_personales()

                        # conexion.py
                        Mostrar_Datos_A(
                            Tipo_de_conexion, retorna_renombre, Conectado, Conectado_atlas, Nombre_base_de_datos, Nombre_documentacion)

                        # menu_desplazamiento.py
                        retorno_volver = Menu_atras()

                        if retorno_volver == "volver":

                            continue

                        elif retorno_volver == "fin":

                            # mensajes.py
                            Mensaje_Agradecimiento()

                        else:

                            # errores.py
                            Error_menu_atras()

                    elif retorno_visualizacion == "b":

                        # logica.py
                        Limpiar_consola()

                        # mensaje.py
                        Cartel()

                        if Tipo_de_conexion == "local":

                            # mensajes.py
                            Mensaje_de_visualizacion_local_laborales()

                        elif Tipo_de_conexion == "atlas":

                            # mensajes.py
                            Mensaje_de_visualizacion_atlas_laborales()

                        # conexion.py
                        Mostrar_Datos_B(
                            Tipo_de_conexion, retorna_renombre, Conectado, Conectado_atlas, Nombre_base_de_datos, Nombre_documentacion)

                        # menu_desplazamiento.py
                        retorno_volver = Menu_atras()

                        if retorno_volver == "volver":

                            continue

                        elif retorno_volver == "fin":

                            # mensajes.py
                            Mensaje_Agradecimiento()

                        else:

                            # errores.py
                            Error_menu_atras()

                    elif retorno_visualizacion == "c":

                        # logica.py
                        Limpiar_consola()

                        # mensaje.py
                        Cartel()

                        if Tipo_de_conexion == "local":

                            # mensajes.py
                            Mensaje_de_visualizacion_local_academico()

                        elif Tipo_de_conexion == "atlas":

                            # mensajes.py
                            Mensaje_de_visualizacion_atlas_academico()

                        # conexion.py
                        Mostrar_Datos_C(
                            Tipo_de_conexion, retorna_renombre, Conectado, Conectado_atlas, Nombre_base_de_datos, Nombre_documentacion)

                        # menu_desplazamiento.py
                        retorno_volver = Menu_atras()

                        if retorno_volver == "volver":

                            continue

                        elif retorno_volver == "fin":

                            # mensajes.py
                            Mensaje_Agradecimiento()

                        else:

                            # errores.py
                            Error_menu_atras()

                    else:

                        # errores.py
                        Error_Menu_Desplazamiento_Visualizacion()

            else:

                # mensajes.py
                Mensaje_error_guardado()

        elif retorno_desplazamiento == "exportar":

            # logica.py
            Datos = Datos_de_Formularios(Nombre_Apellido, Estado_civil, Genero, Fecha_Nacimiento, Edad, Nacionalidad, Provincia, Localidad, Codigo_Postal, Celular, Correo, Nombre_empresa,
                                         Puesto_trabajo, Tiempo_trabajo, Ingreso_Laboral, Egreso_Laboral, Descripcion, Nombre_Institucion, Nombre_Titulo, Orientacion, Inicio_Academico, Egreso_Academico, Turno)

            # logica.py
            retorno_exportacion = Exportacion_de_Formularios(Datos)

            if retorno_exportacion:

                # mensajes.py
                Mensaje_exportacion_correcta()

            else:

                # mensajes.py
                Mensaje_exportacion_incorrecta()

        elif retorno_desplazamiento == "enviar":

            while True:

                # logica.py
                Limpiar_consola()

                # mensaje.py
                Cartel()

                # mensajes.py
                Mensaje_correo_electronico()

                # Correo.py
                retorno_correo = Cuenta_de_acceso()

                while retorno_correo == 535:

                    # mensajes.py
                    Mensaje_error_cuenta()

                    break

                else:

                    while True:

                        # logica.py
                        Datos = Datos_de_Formularios(Nombre_Apellido, Estado_civil, Genero, Fecha_Nacimiento, Edad, Nacionalidad, Provincia, Localidad, Codigo_Postal, Celular, Correo, Nombre_empresa,
                                                     Puesto_trabajo, Tiempo_trabajo, Ingreso_Laboral, Egreso_Laboral, Descripcion, Nombre_Institucion, Nombre_Titulo, Orientacion, Inicio_Academico, Egreso_Academico, Turno)

                        # logica.py
                        Limpiar_consola()

                        # mensaje.py
                        Cartel()

                        Correo_electronico = retorno_correo

                        # mensajes.py
                        Mensaje_envio_de_mensaje(
                            Correo_electronico)

                        # Correo.py
                        retorno = Envio_del_mensaje(
                            Correo_electronico, Datos)

                        while retorno == False:

                            # errores.py
                            Error_envio_mail()

                            break

                        else:

                            if retorno:

                                # mensajes.py
                                Envio_exitoso()

                                # menu_desplazamiento.py
                                retorno_volver = Menu_atras()

                                if retorno_volver == "volver":

                                    break

                                elif retorno_volver == "fin":

                                    # mensajes.py
                                    Mensaje_Agradecimiento()

                                else:

                                    # errores.py
                                    Error_menu_atras()

                    break

        else:

            Error_Menu_Desplazamiento_Formularios_Completos()  # errores.py

    while estado_A == f"{texto_correcto}COMPLETADO" and estado_B == f"{texto_correcto}COMPLETADO" and estado_C == f"{texto_correcto}COMPLETADO" and respuesta == "no":

        # logica.py
        Limpiar_consola()

        # mensaje.py
        Cartel()

        # mensajes.py
        Menu_formulario_completado(Estado, Nombre_servidor, Nombre_base_de_datos,
                                   Nombre_documentacion, estado_A, estado_B, estado_C)

        # menu_desplazamiento.py
        retorno_desplazamiento = Menu_de_desplazamiento_sin_conexion()

        if retorno_desplazamiento == "reset":

            estado_A = f"{error_texto}INCOMPLETO"
            estado_B = f"{error_texto}INCOMPLETO"
            estado_C = f"{error_texto}INCOMPLETO"

            pass

        elif retorno_desplazamiento == "exportar":

            # logica.py
            Datos = Datos_de_Formularios(Nombre_Apellido, Estado_civil, Genero, Fecha_Nacimiento, Edad, Nacionalidad, Provincia, Localidad, Codigo_Postal, Celular, Correo, Nombre_empresa,
                                         Puesto_trabajo, Tiempo_trabajo, Ingreso_Laboral, Egreso_Laboral, Descripcion, Nombre_Institucion, Nombre_Titulo, Orientacion, Inicio_Academico, Egreso_Academico, Turno)

            # logica.py
            retorno_exportacion = Exportacion_de_Formularios(Datos)

            if retorno_exportacion:

                # mensajes.py
                Mensaje_exportacion_correcta()

            else:

                # mensajes.py
                Mensaje_exportacion_incorrecta()

        elif retorno_desplazamiento == "enviar":

            while True:

                # logica.py
                Limpiar_consola()

                # mensaje.py
                Cartel()

                # mensajes.py
                Mensaje_correo_electronico()

                # Correo.py
                retorno_correo = Cuenta_de_acceso()

                while retorno_correo == 535:

                    # mensajes.py
                    Mensaje_error_cuenta()  # mensajes.py

                    break

                else:

                    while True:

                        # logica.py
                        Datos = Datos_de_Formularios(Nombre_Apellido, Estado_civil, Genero, Fecha_Nacimiento, Edad, Nacionalidad, Provincia, Localidad, Codigo_Postal, Celular, Correo, Nombre_empresa,
                                                     Puesto_trabajo, Tiempo_trabajo, Ingreso_Laboral, Egreso_Laboral, Descripcion, Nombre_Institucion, Nombre_Titulo, Orientacion, Inicio_Academico, Egreso_Academico, Turno)

                        # logica.py
                        Limpiar_consola()

                        # mensaje.py
                        Cartel()

                        Correo_electronico = retorno_correo

                        # mensajes.py
                        Mensaje_envio_de_mensaje(
                            Correo_electronico)

                        # Correo.py
                        retorno = Envio_del_mensaje(
                            Correo_electronico, Datos)

                        while retorno == False:

                            # errores.py
                            Error_envio_mail()

                            break

                        else:

                            if retorno:

                                # mensajes.py
                                Envio_exitoso()

                                # menu_desplazamiento.py
                                retorno_volver = Menu_atras()

                                if retorno_volver == "volver":

                                    break

                                elif retorno_volver == "fin":

                                    # mensajes.py
                                    Mensaje_Agradecimiento()

                                else:

                                    # errores.py
                                    Error_menu_atras()
