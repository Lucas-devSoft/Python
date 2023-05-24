""" Librerías (Módulos) """  

from    pymongo    import   MongoClient
from    getpass    import   getpass # hace invisible visualmente las contraseñas 

""" Scripts """ 

from    logica     import   Limpieza_consola, Cartel
from    errores    import   Error_Mensaje_de_Conexión, Error_Mensaje_pre_Conexión
from    colores    import   *

def Conexión_Local(Nombre: str):
    
    while True:
        
        Limpieza_consola()
        
        print()
        Cartel()
        
        print(f"""
{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}║{fondo}     {texto}{Nombre.capitalize()}, ¿ Quiere generar una Base de datos con un nombre en especifico?{fin+fondo}    {fin+marco}║{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}╠═══════════════════════════════════════╦═══════════════════════════════════════╣{fin}
{marco}║{fondo}             {texto}Sí, Quiero  < si >{fin+fondo}        {fin+marco}║{fondo}        {texto}< no >  No, no quiero{fin+fondo}          {fin+marco}║{fin}
{marco}╚═══════════════════════════════════════╩═══════════════════════════════════════╝{fin}
        """)
        Generando_BD = input("\t\t\t\t       ").lower()

        try:
            
            global Conexión, db, dc, Nombre_DB, Nombre_DC
            Conexión = MongoClient("mongodb://localhost:27017/")
            
            if Generando_BD == "si":
                
                if Conexión.admin.command("ping"):
                    
                    Limpieza_consola()
                    
                    print()
                    Cartel()

                    print(f"""
{marco}╔══════════════════════════════════════════════════════════════════════════════╗{fin}
{marco}║{fondo}                                                                              {fin+marco}║{fin}
{marco}║{fondo}                 {texto}Creación de la base de Datos con un nombre específico{fin+fondo}        {fin+marco}║{fin}
{marco}║{fondo}                                                                              {fin+marco}║{fin}
{marco}╠══════════════════════════════════════════════╦═══════════════════════════════╣{fin}""")
                    Nombre_DB = input(f"{marco}║{fondo}        {texto}Nombre de la Base de Datos{fin+fondo}            {fin+marco}║{fin}                ")
                    print(f"{marco}╠══════════════════════════════════════════════╬═══════════════════════════════╣{fin}")
                    Nombre_DC = input(f"{marco}║{fondo}        {texto}Nombre de la Documentación{fin+fondo}            {fin+marco}║{fin}                ")
                    print(f"{marco}╠══════════════════════════════════════════════╩═══════════════════════════════╣{fin}")

                    if Nombre_DB not in Conexión.list_database_names():
                        
                        db = Conexión.get_database(name=f"{Nombre_DB}")
                        db.create_collection(name=f"{Nombre_DC}")

                        print(f"""{marco}║{fondo}                                                                              {fin+marco}║{fin}
{marco}║{fondo}                    {fin+texto_correcto}La Base de Datos fue creada con éxito.{fin+fondo}                    {fin+marco}║{fin}
{marco}║{fondo}                {fin+texto_correcto}Presione ENTER para continuar con el programa.{fin+fondo}                {fin+marco}║{fin}
{marco}║{fondo}                                                                              {fin+marco}║{fin}""")
                        input(f"{marco}╚══════════════════════════════════════════════════════════════════════════════╝{fin}")

                    else:
                        
                        print(f"""{marco}║{fondo}                                                                              {fin+marco}║{fin}
{marco}║{fondo}            {fin+error_texto}La base de datos ya existe y ya esta activa para guardar!.{fin+fondo}        {fin+marco}║{fin}
{marco}║{fondo}                {fin+error_texto}Presione ENTER para continuar con el programa.{fin+fondo}                {fin+marco}║{fin}
{marco}║{fondo}                                                                              {fin+marco}║{fin}""")
                        input(f"{marco}╚══════════════════════════════════════════════════════════════════════════════╝{fin}")

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
                
                print()
                Cartel()
                print()
                
                Error_Mensaje_pre_Conexión()
                continue

        except:
            
            print("Algo salio mal con la conexión o no tiene instalado el Driver de MongoDB en su sistema.")
            input()

        break

    return Generando_BD

def Mongo_Atlas_Conexión():
    
    while True:
        
        try:
        
            Limpieza_consola() 
            Cartel()
        
            print(f"""
{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}║{fondo}                       {texto}Bienvenido a MongoDB Atlas{fin+fondo}                              {fin+marco}║{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}╠═════════════════════════════════════╦═════════════════════════════════════════╣{fin}""")
            Usuario = input(f"{marco}║{fondo}               {texto}Usuario{fin+fondo}               {fin+marco}║{fin}         ")
            print(f"{marco}╠═════════════════════════════════════╬═════════════════════════════════════════╣{fin}")
            contraseña = getpass(f"{marco}║{fondo}            {texto}Contraseña{fin+fondo}               {fin+marco}║{fin}         ")
            print(f"{marco}╠═════════════════════════════════════╬═════════════════════════════════════════╣{fin}")
            Cluster = input(f"{marco}║{fondo}      {texto}Nombre del Cluster{fin+fondo}             {fin+marco}║{fin}         ")
            print(f"{marco}╠═════════════════════════════════════╬═════════════════════════════════════════╣{fin}")
            Identificador = input(f"{marco}║{fondo}      {texto}Identificador del Cluster{fin+fondo}      {fin+marco}║{fin}         ")
            print(f"{marco}╚═════════════════════════════════════╩═════════════════════════════════════════╣{fin}")

            global Atlas, Atlas_db, Atlas_dc, Atlas_DC, Atlas_DB
            Atlas = MongoClient(f"mongodb+srv://{Usuario}:{contraseña}@{Cluster}.{Identificador}.mongodb.net/?retryWrites=true&w=majority")

            if Atlas.admin.command("ping"):
                
                Limpieza_consola() 
                Cartel()
                
                print(f"""
{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}
{marco}║{fondo}          {texto}Bienvenido{fin+fondo} {fin+texto_correcto} {Usuario} {fin+fondo+texto} ya estas conectado al cluster{fin} {texto_correcto+Cluster+fondo}         {fin+marco}║{fin}
{marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}                
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}║{fondo}          {texto}¿Desea generar una Base de datos con un nombre especifico?{fin+fondo}           {fin+marco}║{fin}
{marco}║{fondo}                                                                               {fin+marco}║{fin}
{marco}╠═══════════════════════════════════════╦═══════════════════════════════════════╣{fin}
{marco}║{fondo}     {texto}Sí, quiero otro nombre <si>{fin+fondo}       {fin+marco}║{fondo}    {texto}No, mantengo el por defecto <no>{fin+fondo}   {fin+marco}║{fin}
{marco}╚═══════════════════════════════════════╩═══════════════════════════════════════╝{fin}
                """)
                pregunta = input("\t\t\t\t\t").lower()
            
            if pregunta == "si":
                
                Limpieza_consola()
                Cartel()

                print(f"""
{marco}╔══════════════════════════════════════════════════════════════════════════════╗{fin}
{marco}║{fondo}                                                                              {fin+marco}║{fin}
{marco}║{fondo}                 {texto}Creación de la base de Datos con un nombre específico{fin+fondo}        {fin+marco}║{fin}
{marco}║{fondo}                                                                              {fin+marco}║{fin}
{marco}╠══════════════════════════════════════════════╦═══════════════════════════════╣{fin}""")
                Atlas_DB = input(f"{marco}║{fondo}        {texto}Nombre de la Base de Datos{fin+fondo}            {fin+marco}║{fin}                ")
                print(f"{marco}╠══════════════════════════════════════════════╬═══════════════════════════════╣{fin}")
                Atlas_DC = input(f"{marco}║{fondo}        {texto}Nombre de la Documentación{fin+fondo}            {fin+marco}║{fin}                ")
                print(f"{marco}╠══════════════════════════════════════════════╩═══════════════════════════════╣{fin}")

                if Atlas_DB not in Atlas.list_database_names():
                    
                    Atlas_db = Atlas.get_database(name=f"{Atlas_DB}")
                    Atlas_db.create_collection(name=f"{Atlas_DC}")

                    print(f"""{marco}║{fondo}                                                                              {fin+marco}║{fin}
{marco}║{fondo}                    {fin+texto_correcto}La Base de Datos fue creada con éxito.{fin+fondo}                    {fin+marco}║{fin}
{marco}║{fondo}                {fin+texto_correcto}Presione ENTER para continuar con el programa.{fin+fondo}                {fin+marco}║{fin}
{marco}║{fondo}                                                                              {fin+marco}║{fin}""")
                    input("{marco}╚══════════════════════════════════════════════════════════════════════════════╝{fin}")

                else:
                    
                    print(f"""{marco}║{fondo}                                                                              {fin+marco}║{fin}
{marco}║{fondo}            {fin+error_texto}La base de datos ya existe y ya esta activa para guardar!.{fin+fondo}        {fin+marco}║{fin}
{marco}║{fondo}                {fin+error_texto}Presione ENTER para continuar con el programa.{fin+fondo}                {fin+marco}║{fin}
{marco}║{fondo}                                                                              {fin+marco}║{fin}""")
                    input(f"{marco}╚══════════════════════════════════════════════════════════════════════════════╝{fin}")

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
            
            print(f"""{marco}║{fondo}             {fin+error_texto}Error!!. La información de la cuenta es incorrecta.{fin+fondo}               {fin+marco}║{fin}
{marco}║{fondo}                    {fin+error_texto}Presione Enter para volver a intentar.{fin+fondo}                     {fin+marco}║{fin}""")
            input(f"{marco}╚═══════════════════════════════════════════════════════════════════════════════╝{fin}")           
        
def Banner(retorna_conexion: str, Respuesta_tipo_conexion: str):

    if retorna_conexion == "si":
        
        Estado = f"{fondo}   {fin+texto_correcto} Conectado{fin}"
        
        if Respuesta_tipo_conexion == "1":
        
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
            
            return Estado, f"{fin} {texto_correcto}{Nombre_servidor} {fin}", f"{fin} {texto_correcto}{Version} {fin}", f"{fin} {texto_correcto}{Nombre_BD} {fin}", f"{fin} {texto_correcto}{Nombre_Doc} {fin}"
        
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
        
        Estado = f"{fondo}   {fin+texto_correcto} Conectado{fin}"
        
        if Respuesta_tipo_conexion == "1":
        
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

            return Estado, f"{fin} {texto_correcto}{Nombre_servidor} {fin}", f"{fin} {texto_correcto}{Version} {fin}", f"{fin} {texto_correcto}{Nombre_BD} {fin}", f"{fin} {texto_correcto}{Nombre_Doc} {fin}"

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
        
    return f"{fin+error_texto} Desconectado{fin}", f"{fondo}            {fin+error_texto} N/A {fin}", f"{fondo}  {fin+error_texto} N/A {fin}", f"{fondo}        {fin+error_texto} N/A {fin}", f"{fondo}      {fin+error_texto} N/A {fin}" 
                
def Ingreso_Datos_AF(Respuesta : str, Nombre : str, Numero1 : int, Operador : str, Numero2 : int, Resultado: int):
    
    try:
    
        if Respuesta == "1" :

            dc.insert_one({"Operación" : {  "Nombre"   : Nombre.capitalize(), 
                                            "Valor_1"  : Numero1, 
                                            "Operador" : Operador, 
                                            "Valor_2"  : Numero2, 
                                            "Resultado": Resultado}})
        
            print(f"{marco}║{fondo}             {texto}Historial de Operaciones desde tu Base de Datos{fin+fondo}                   {fin+marco}║{fin}")
            print(f"{marco}╠══════════════════╦═════════════╦══════════════╦═════════════╦═════════════════╣{fin}")
            
            for i in dc.find().limit(6):
                
                print(f"{marco}║{fondo+texto}  ",str(dict(i).get("Operación")).replace("{","").replace("}","").replace("'","").replace(",",f"  {fin+marco}║{fin+fondo+texto}"),f"   {fin+marco}║{fin}")
            
        elif Respuesta == "2":
            
            Atlas_dc.insert_one({"Operación" : {    "Nombre"   : Nombre.capitalize(), 
                                                    "Valor_1"  : Numero1, 
                                                    "Operador" : Operador, 
                                                    "Valor_2"  : Numero2, 
                                                    "Resultado": Resultado}})

            for i in Atlas_dc.find():
                
                print(f"{marco}║{fondo}  ",str(dict(i).get("Operación")).replace("{","").replace("}","").replace("'","").replace(",",f"  {fin+marco}║{fin+fondo}"),f"   {fin+marco}║{fin}")
    
    except:
        
        print("Ocurrió algo con la conexion por lo que no se puede agregar información")


def Ingreso_Datos_GH(Respuesta : str, Nombre : str, Numero : int, Operador: str, Conclusión: str):
    
    try:
    
        if Respuesta == "1" :

            dc.insert_one({"Operación" : {  "Nombre"   : Nombre.capitalize(), 
                                            "Valor"    : Numero, 
                                            "Operador" : Operador,  
                                            "Resultado": Conclusión}})
        
            print(f"{marco}║{fondo}             {texto}Historial de Operaciones desde tu Base de Datos{fin+fondo}                   {fin+marco}║{fin}")
            print(f"{marco}╠══════════════════╦═════════════╦══════════════╦═════════════╦═════════════════╣{fin}")
            
            for i in dc.find().limit(6):
                
                print(f"{marco}║{fondo+texto}  ",str(dict(i).get("Operación")).replace("{","").replace("}","").replace("'","").replace(",",f"  {fin+marco}║{fin+fondo+texto}"),f"   {fin+marco}║{fin}")
            
        elif Respuesta == "2":
            
            Atlas_dc.insert_one({"Operación" : {    "Nombre"   : Nombre.capitalize(), 
                                                    "Valor"    : Numero, 
                                                    "Operador" : Operador,  
                                                    "Resultado": Conclusión}})
            for i in Atlas_dc.find():
                
                print(f"{marco}║{fondo}  ",str(dict(i).get("Operación")).replace("{","").replace("}","").replace("'","").replace(",",f"  {fin+marco}║{fin+fondo}"),f"   {fin+marco}║{fin}")
    
    except:
        
        print("Ocurrió algo con la conexion por lo que no se puede agregar información")

        
def Borrar_historial():
    
    if Conexión.admin.command("ping"):
        
        dc.delete_many({"Operación" : {"$exists" : True}})
            
    elif  Atlas.admin.command("ping"):
        
        dc.delete_many({"Operación" : {"$exists" : True}})