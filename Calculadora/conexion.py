""" Librerías (Módulos) """  

from    pymongo    import   MongoClient
from    getpass    import   getpass # hace invisible visualmente las contraseñas 

""" Scripts """ 

from    logica     import   Limpieza_consola, Cartel
from    errores    import   Error_Mensaje_pre_Conexión
from    colores    import   *

def Conexión_Local():
    
    while True:
        
        Limpieza_consola()
        Cartel()
        
        print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█          {texto}¿Quiere generar una Base de datos con un nombre en especifico?              {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█               {texto}Sí, QUIERO  <si>                NO, NO QUIERO <no>                     {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
            """)
        Generando_BD = input("\t\t\t\t\t    ").lower()

        try:
            
            global Conexión, db, dc, Nombre_DB, Nombre_DC
            Conexión = MongoClient("mongodb://localhost:27017/")
            
            if Generando_BD == "si":
                
                if Conexión.admin.command("ping"):
                    
                    Limpieza_consola()
                    Cartel()

                    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█           {texto}Creación de la base de datos con un nombre específico.                     {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")
                    Nombre_DB = input(f"{marco+fondo}█           {texto}Nombre de la Base de Datos : {fin}              ")
                    Nombre_DC = input(f"{marco+fondo}█           {texto}Nombre de la Documentación : {fin}              ")
                    print(f"{marco+fondo}█                                                                                      █{fin}""")

                    if Nombre_DB not in Conexión.list_database_names():
                        
                        db = Conexión.get_database(name=f"{Nombre_DB}")
                        db.create_collection(name=f"{Nombre_DC}")

                        print(f"""{marco+fondo}█                         {texto_correcto}La base de datos fue creada con éxito.                       {fin+marco}█{fin}
{marco+fondo}█                     {texto_correcto}Presione ENTER para continuar con el programa.                   {fin+marco}█{fin}  
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}""")
                        input()

                    else:
                        
                        print(f"""{marco+fondo}█                 {error_texto}La base de datos ya existe y ya esta activa para guardar!.           {fin+marco}█{fin}
{marco+fondo}█                       {error_texto}Presione ENTER para continuar con el programa.                 {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}""")
                        input()

                    db = Conexión[f"{Nombre_DB}"]
                    dc = db[f"{Nombre_DC}"]

            elif Generando_BD == "no":
                
                Conexión = MongoClient("mongodb://localhost:27017/")

                if Conexión.admin.command("ping"):
                    
                    if "Calculadora" not in Conexión.list_database_names():
                        
                        db = Conexión.get_database(name="Calculadora")
                        db.create_collection(name="Historial")

                    db = Conexión["Calculadora"]
                    dc = db["Historial"]
                    break

            else:
                
                Limpieza_consola()
                Cartel()
                Error_Mensaje_pre_Conexión()
                continue

        except:
            
            print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█             {error_texto}Error!!. La información de la cuenta es incorrecta.                      {fin+marco}█{fin}
{marco+fondo}█                    {error_texto}Presione Enter para volver a intentar.                            {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}""") 
            input()

        break
    
    return Generando_BD
        
def Mongo_Atlas_Conexión():
    
    while True:
        
        try:
        
            Limpieza_consola() 
            Cartel()
        
            print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                       {texto}Bienvenido a cuenta MongoDB Atlas                              {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")
            Usuario = input(f"{marco+fondo}█               {texto}Nombre de usuario : {fin}                   ")
            contraseña = getpass(f"{marco+fondo}█                      {texto}Contraseña : {fin}                   ")
            Cluster = input(f"{marco+fondo}█              {texto}Nombre del cluster : {fin}                   ")
            Identificador = input(f"{marco+fondo}█       {texto}Identificador del Cluster : {fin}                   ")  
            
            global Atlas, Atlas_db, Atlas_dc, Atlas_DC, Atlas_DB
            Atlas = MongoClient(f"mongodb+srv://{Usuario}:{contraseña}@{Cluster}.{Identificador}.mongodb.net/?retryWrites=true&w=majority")

            if Atlas.admin.command("ping"):
                
                Limpieza_consola() 
                Cartel()
                
                print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█            {texto}Bienvenido {texto_correcto+Usuario+fin+fondo+texto} ya estas conectado al cluster {texto_correcto+Cluster+fondo}                {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█            {texto}¿Desea generar una Base de datos con un nombre especifico?                {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█         {texto}SI, QUIERO OTRO NOMBRE <si>          NO, MANTENGO EL POR DEFECTO <no>        {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
                """)
                pregunta = input("\t\t\t\t\t").lower()
            
            if pregunta == "si":
                
                Limpieza_consola()
                Cartel()

                print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█           {texto}Creación de la base de datos con un nombre específico.                     {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")
                Atlas_DB = input(f"{marco+fondo}█           {texto}Nombre de la Base de Datos : {fin}              ")
                Atlas_DC = input(f"{marco+fondo}█           {texto}Nombre de la Documentación : {fin}              ")

                if Atlas_DB not in Atlas.list_database_names():
                    
                    Atlas_db = Atlas.get_database(name=f"{Atlas_DB}")
                    Atlas_db.create_collection(name=f"{Atlas_DC}")

                    print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                         {texto_correcto}La base de datos fue creada con éxito.                       {fin+marco}█{fin}
{marco+fondo}█                     {texto_correcto}Presione ENTER para continuar con el programa.                   {fin+marco}█{fin}  
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}""")
                    input()

                else:
                    
                    print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█                 {error_texto}La base de datos ya existe y ya esta activa para guardar!.           {fin+marco}█{fin}
{marco+fondo}█                       {error_texto}Presione ENTER para continuar con el programa.                 {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}""")
                    input()

                Atlas_db = Atlas[f"{Atlas_DB}"]
                Atlas_dc = Atlas_db[f"{Atlas_DC}"]

                return pregunta
                
            elif pregunta == "no":

                if Atlas.admin.command("ping"):
                    
                    if "Calculadora" not in Atlas.list_database_names():
                        
                        Atlas_db = Atlas.get_database(name="Calculadora")
                        Atlas_db.create_collection(name="Historial")

                    Atlas_db = Atlas["Calculadora"]
                    Atlas_dc = Atlas_db["Historial"]
                    
                    return pregunta
                
            else:
                    
                Limpieza_consola()
                Cartel()
                Error_Mensaje_pre_Conexión()
                continue    
                
        except:
            
            print(f"""{marco+fondo}█                                                                                      █{fin}
{marco+fondo}█             {error_texto}Error!!. La información de la cuenta es incorrecta.                      {fin+marco}█{fin}
{marco+fondo}█                    {error_texto}Presione Enter para volver a intentar.                            {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}""") 
            input()          

        break
    
    return pregunta
        
def Banner(retorna_conexion: str, Respuesta_tipo_conexion: str):

    if retorna_conexion == "si":
        
        if Respuesta_tipo_conexion == "1":
            
            Estado = f"{fondo}   {texto_correcto}Conectado"
            Nombre_servidor = f"{Conexión.HOST}:{Conexión.PORT}"
            Version = Conexión.server_info().get("version")
            Nombre_BD = Conexión.list_database_names()
            Nombre_Doc = db.list_collection_names() 
            
            for i in Nombre_BD:
                
                if Nombre_DB == i :
                    
                    Nombre_BD = i
            
            for x in Nombre_Doc:
                
                if Nombre_DC == x :
                    
                    Nombre_Doc = x
            
            return Estado, f"{texto_correcto}{Nombre_servidor}", f"{fondo} {texto_correcto}{Version}   ", f"{fondo} {texto_correcto}{Nombre_BD} ", f"{fondo} {texto_correcto}{Nombre_Doc}           "
        
        elif Respuesta_tipo_conexion == "2":
            
            Nombre_servidor = f"{Atlas.address[0]}:{Atlas.address[1]}"
            Version = Atlas.server_info().get("version")
            Atlas_BD = Atlas.list_database_names()
            Atlas_Doc = Atlas_db.list_collection_names()
            
            for i in Atlas_BD:
                
                if Atlas_DB == i :
                    
                    Atlas_BD = i
            
            for x in Atlas_Doc:
                
                if Atlas_DC == x :
                    
                    Atlas_Doc = x

            return Estado, f"{fin} {texto_correcto}{Nombre_servidor} {fin}", f"{fin} {texto_correcto}{Version} {fin}", f"{fin} {texto_correcto}{Atlas_BD} {fin}", f"{fin} {texto_correcto}{Atlas_Doc} {fin}"
    
    elif retorna_conexion == "no":
        
        if Respuesta_tipo_conexion == "1":
            
            Estado = f"   {texto_correcto}Conectado"
            Nombre_servidor = f"{Conexión.HOST}:{Conexión.PORT}"
            Version = Conexión.server_info().get("version")
            Nombre_BD = Conexión.list_database_names()
            Nombre_Doc = db.list_collection_names()
            
            for i in Nombre_BD:
                
                if 'Calculadora' == i:
                    
                    Nombre_BD = i
            
            for x in Nombre_Doc:
                
                if 'Historial' == x :
                    
                    Nombre_Doc = x

            return Estado, f" {texto_correcto}{Nombre_servidor} {fin}", f" {texto_correcto}{Version} {fin}", f" {texto_correcto}{Nombre_BD} {fin}", f" {texto_correcto}{Nombre_Doc} {fin}"

        elif Respuesta_tipo_conexion == "2":
            
            Nombre_servidor = f"{Atlas.address[0]}:{Atlas.address[1]}"
            Version = Atlas.server_info().get("version")
            Atlas_BD = Atlas.list_database_names()
            Atlas_Doc = Atlas_db.list_collection_names()
            
            for i in Atlas_BD:
                
                if 'Calculadora' == i:
                    
                    Atlas_BD = i
            
            for x in Atlas_Doc:
                
                if 'Historial' == x :
                    
                    Atlas_Doc = x
            
            return Estado, f"{fin} {texto_correcto}{Nombre_servidor} {fin}", f"{fin} {texto_correcto}{Version} {fin}", f"{fin} {texto_correcto}{Atlas_BD} {fin}", f"{fin} {texto_correcto}{Atlas_Doc} {fin}"
        
    return f"{error_texto}Desconectado", f"{error_texto}N/A{fin}", f"{error_texto}N/A                  {fin}", f"{error_texto}N/A{fin}", f"{error_texto}N/A                  {fin}" 
                
def Ingreso_Datos_AF(Respuesta : str, Nombre : str, Numero1 : int, Operador : str, Numero2 : int, Resultado: int):
    
    try:
    
        if Respuesta == "1" :

            dc.insert_one({"Operación" : {  "Nombre"   : Nombre.capitalize(), 
                                            "Valor_1"  : Numero1, 
                                            "Operador" : Operador, 
                                            "Valor_2"  : Numero2, 
                                            "Resultado": Resultado}})
        
            print(f"""{marco+fondo}█                  {texto}Historial de movimientos desde MongoDB Localhost.                   {fin+marco}█{fin}
{marco+fondo}█                                                                                      █{fin}""")
            
            for i in dc.find():
                
                print(f"{marco+fondo}█     {texto}",str(dict(i).get("Operación")).replace("{","").replace("}","").replace("'","").replace(",","   "),f"       {fin+marco}█{fin}")
            
        elif Respuesta == "2":
            
            Atlas_dc.insert_one({"Operación" : {    "Nombre"   : Nombre.capitalize(), 
                                                    "Valor_1"  : Numero1, 
                                                    "Operador" : Operador, 
                                                    "Valor_2"  : Numero2, 
                                                    "Resultado": Resultado}})

            print(f"""{marco}║{fondo}                  {texto}Historial de movimientos desde MongoDB Atlas{fin+fondo}                   {fin+marco}║{fin}")
{marco+fondo}█                                                                                 █{fin}""")
            
            for i in Atlas_dc.find():
                
                print(f"{marco+fondo}█   {texto}",str(dict(i).get("Operación")).replace("{","").replace("}","").replace("'","").replace(",","   "),f"    {fin+marco}█{fin}")
    
    except:
        
        print("Ocurrió algo con la conexion por lo que no se puede agregar información")

def Ingreso_Datos_GH(Respuesta : str, Nombre : str, Numero : int, Operador: str, Conclusión: str):
    
    try:
    
        if Respuesta == "1" :

            dc.insert_one({"Operación" : {  "Nombre"   : Nombre.capitalize(), 
                                            "Valor"    : Numero, 
                                            "Operador" : Operador,  
                                            "Resultado": Conclusión}})
        
            print(f"{marco}║{fondo}             {texto}Historial de Operaciones con MongoDB Local{fin+fondo}                   {fin+marco}║{fin}")
            print(f"{marco}╠══════════════════╦═════════════╦══════════════╦═════════════╦═════════════════╣{fin}")
            
            for i in dc.find().limit(6):
                
                print(f"{marco}║{fondo}  {texto}",str(dict(i).get("Operación")).replace("{","").replace("}","").replace("'","").replace(",",f"  {fin+marco}║{fin+fondo} {texto}"),f"   {fin+marco}║{fin}")
            
        elif Respuesta == "2":
            
            Atlas_dc.insert_one({"Operación" : {    "Nombre"   : Nombre.capitalize(), 
                                                    "Valor"    : Numero, 
                                                    "Operador" : Operador,  
                                                    "Resultado": Conclusión}})
            
            print(f"{marco}║{fondo}             {texto}Historial de Operaciones con MongoDB Atlas{fin+fondo}                   {fin+marco}║{fin}")
            print(f"{marco}╠══════════════════╦═════════════╦══════════════╦═════════════╦═════════════════╣{fin}")
            
            for i in Atlas_dc.find():
                
                print(f"{marco}║{fondo+texto}  ",str(dict(i).get("Operación")).replace("{","").replace("}","").replace("'","").replace(",",f"  {fin+marco}║{fin+fondo+texto}"),f"   {fin+marco}║{fin}")
    
    except:
        
        print("Ocurrió algo con la conexion por lo que no se puede agregar información")

        
def Borrar_historial():
    
    if Conexión.admin.command("ping"):
        
        dc.delete_many({"Operación" : {"$exists" : True}})
            
    elif  Atlas.admin.command("ping"):
        
        dc.delete_many({"Operación" : {"$exists" : True}})