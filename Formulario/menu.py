from colores import *
from conexion import *
from errores import *

estado_A = f"{error_texto}INCOMPLETO"
estado_B = f"{error_texto}INCOMPLETO"
estado_C = f"{error_texto}INCOMPLETO"

while True:

    Limpiar_consola()
    Cartel()

    print(f"""        
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█         {texto}¿Quiere generar una conexión a la base de datos de MongoDB?                   {fin+marco}█{fin}    
{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█          {texto}SI, QUIERO <si>                              NO, NO QUIERO <no>              {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}    
    """)

    pregunta = input("\t\t\t\t\t").lower()

    if pregunta == "si":

        while True:

            Limpiar_consola()
            Cartel()

            print(f"""        
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█                  {texto}¿En que base de datos quiere generar la conexión?                    {fin+marco}█{fin}    
{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█          {texto}MongoDB Local <local>                     MongoDB Atlas <atlas>              {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
            """)

            pregunta = input("\t\t\t\t\t").lower()

            if pregunta == "local":

                retorno_conexion = Conexión_Local()
                break

            elif pregunta == "atlas":

                retorno_conexio = Mongo_Atlas_Conexión()
                break

            else:

                Error_Menu()
                continue

    elif pregunta == "no":

        retorno_conexion = "no"

    else:

        Error_Respuesta()
        continue

    break

retorno_banner = Banner(retorno_conexion, pregunta)
Estado, Nombre_servidor, Version, Nombre_BD, Nombre_Doc = retorno_banner[0:5]

while not (estado_A == f"{texto_correcto}COMPLETADO" and estado_B == f"{texto_correcto}COMPLETADO" and estado_C == f"{texto_correcto}COMPLETADO") or pregunta == "no":

    Limpiar_consola()
    Cartel()

    print(f"""        
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█   {texto}Estado de la Conexión : {Estado}                                                {fin+marco}█{fin}
{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█   {texto}Servidor : {Nombre_servidor}{fondo}                 {texto}MongoDB V. : {Version}{fondo}                   {fin+marco}█{fin}
{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█   {texto}Base de Datos : {Nombre_BD}{fondo}            {texto}Documentación : {Nombre_Doc}{fondo}                {fin+marco}█{fin}
{marco+fondo}█                                                                                       █{fin}
{marco+fondo}█                       {texto}Formularios                                  Estados            {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█             {texto}A ► DATOS PERSONALES DEL USUARIO                      {estado_A}          {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█             {texto}B ► DATOS LABORALES DEL USUARIO                       {estado_B}          {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█             {texto}C ► DATOS ACADÉMICOS DEL USUARIO                      {estado_C}          {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")

    respuesta = input(
        f"{marco+fondo}█      {texto}Escriba la letra del formulario que desea realizar : {fin}          ").upper()

    if respuesta == "A" and not f"{texto_correcto}COMPLETADO" in estado_A:

        while True:

            Limpiar_consola()
            Cartel()

            retorna_A = opcion_A()

            if retorna_A:

                Nombre_Apellido, Estado_civil, Genero, Fecha_Nacimiento, Edad, Nacionalidad, Provincia, Localidad, Codigo_Postal, Celular, Correo = retorna_A[
                    0:11]

                Ingreso_Datos_A(pregunta, Nombre_Apellido, Estado_civil, Genero, Fecha_Nacimiento,
                                Edad, Nacionalidad, Provincia, Localidad, Codigo_Postal, Celular, Correo)

                print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}        
{marco+fondo}█                     {texto_correcto}El formulario fue completado correctamente                        {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█            {texto}VOLVER AL MENÚ <volver>                 FIN DEL PROGRAMA <fin>             {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
            """)

                volver = input("\t\t\t\t\t").lower()

                if volver == "volver":

                    estado_A = f"{texto_correcto}COMPLETADO"
                    break

                elif volver == "fin":

                    Mensaje_Agradecimiento()

            else:

                Error_Campo()

    elif respuesta == "B" and not f"{texto_correcto}COMPLETADO" in estado_B:

        while True:

            Limpiar_consola()
            Cartel()

            retorno_B = opcion_B()

            if retorno_B:

                Nombre_empresa, Puesto_trabajo, Tiempo_trabajo, Ingreso, Egreso, Sueldo = retorno_B[
                    0:6]
                Ingreso_Datos_B(pregunta, Nombre_empresa, Puesto_trabajo,
                                Tiempo_trabajo, Ingreso, Egreso, Sueldo)

                print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}        
{marco+fondo}█                     {texto_correcto}El formulario fue completado correctamente                        {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█            {texto}VOLVER AL MENÚ <volver>                 FIN DEL PROGRAMA <fin>             {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
            """)

                volver = input("\t\t\t\t\t").lower()

                if volver == "volver":

                    estado_B = f"{texto_correcto}COMPLETADO"
                    break

                elif volver == "fin":

                    Mensaje_Agradecimiento()

            else:

                Error_Campo()

    elif respuesta == "C" and not f"{texto_correcto}COMPLETADO" in estado_C:

        while True:

            Limpiar_consola()
            Cartel()

            retorna_C = opcion_C()

            if retorna_C:

                Nombre_empresa, Nombre_Titulo, Orientacion, Inicio, Egreso, Turno = retorna_C[
                    0:6]
                Ingreso_Datos_C(pregunta, Nombre_empresa,
                                Nombre_Titulo, Orientacion, Inicio, Egreso, Turno)

                print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}        
{marco+fondo}█                     {texto_correcto}El formulario fue completado correctamente                        {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█            {texto}VOLVER AL MENÚ <volver>                 FIN DEL PROGRAMA <fin>             {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
            """)

                volver = input("\t\t\t\t\t").lower()

                if volver == "volver":

                    estado_C = f"{texto_correcto}COMPLETADO"
                    break

                elif volver == "fin":

                    Mensaje_Agradecimiento()

            else:

                Error_Campo()

    else:

        if f"{texto_correcto}COMPLETADO" in estado_A or f"{texto_correcto}COMPLETADO" in estado_B or f"{texto_correcto}COMPLETADO" in estado_C:

            print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█            {error_texto}El formulario que quiere realizar ya aparece como completado!.             {fin+marco}█{fin}
{marco+fondo}█                            {texto}Presione ENTER para continuar.                             {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}                   
            """)

            input()

        elif f"{texto_correcto}COMPLETADO" in estado_A and f"{texto_correcto}COMPLETADO" in estado_B and f"{texto_correcto}COMPLETADO" in estado_C:

                print(f"""{marco+fondo}█                                                                                       {fin+marco}█{fin}        
{marco+fondo}█                {texto_correcto}Todos los formulario fueron completados correctamente!.                       {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█            {texto}RESETEAR <reset>                 FIN DEL PROGRAMA <fin>             {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
                """)

                volver = input("\t\t\t\t\t").lower()

                if volver == "reset":

                    estado_A = f"{error_texto}INCOMPLETO"
                    estado_B = f"{error_texto}INCOMPLETO"
                    estado_C = f"{error_texto}INCOMPLETO"

                    break

                elif volver == "fin":

                    Mensaje_Agradecimiento()

else:

    while f"{texto_correcto}COMPLETADO" in estado_A and f"{texto_correcto}COMPLETADO" in estado_B and f"{texto_correcto}COMPLETADO" in estado_C and not pregunta == "no":

        Limpiar_consola()
        Cartel()

        print(f"""        
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                       {texto}Formularios                                  Estados            {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█             {texto}A ► DATOS PERSONALES DEL USUARIO                      {estado_A}          {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█             {texto}B ► DATOS LABORALES DEL USUARIO                       {estado_B}          {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█             {texto}C ► DATOS ACADÉMICOS DEL USUARIO                      {estado_C}          {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█    {texto}RESETEAR <reset>      RESULTADO A <a>      RESULTADO B <b>      RESULTADO C <c>    {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
        """)

        resultados = input("\t\t\t\t\t").lower()

        if resultados == "a":

            Mostrar_Datos_A(pregunta)

        elif resultados == "b":

            Mostrar_Datos_B(pregunta)

        elif resultados == "c":

            Mostrar_Datos_C(pregunta)

        elif resultados == "reset":

            estado_A = f"{error_texto}INCOMPLETO"
            estado_B = f"{error_texto}INCOMPLETO"
            estado_C = f"{error_texto}INCOMPLETO"

            break

        else:

            Error_Menu()
