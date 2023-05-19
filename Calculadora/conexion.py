""" Librerías (Módulos) """  

from    pymongo    import   MongoClient
from    getpass    import   getpass # hace invisible visualmente las contraseñas 

""" Scripts """ 

from    logica     import   Limpieza_consola
from    errores    import   Error_Mensaje_de_Conexión, Error_Mensaje_pre_Conexión
from    colores    import   *


def Conexión_Local(Nombre: str):
    
    while True:
        
        Limpieza_consola()
        
        print(f"{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
        print(f"{marco}║{fondo}                                                                               {fin+marco}║{fin}")
        print(f"{marco}║{fondo}     {texto}{Nombre.capitalize()}, ¿ Quiere generar una Base de datos con un nombre en especifico?{fin+fondo}    {fin+marco}║{fin}")
        print(f"{marco}║{fondo}                                                                               {fin+marco}║{fin}")
        print(f"{marco}╠═══════════════════════════════════════╦═══════════════════════════════════════╣{fin}")
        print(f"{marco}║{fondo}             {texto}Sí, Quiero  < si >{fin+fondo}        {fin+marco}║{fondo}        {texto}< no >  No, no quiero{fin+fondo}          {fin+marco}║{fin}")
        print(f"{marco}╚═══════════════════════════════════════╩═══════════════════════════════════════╝{fin}")
        Generando_BD = input("\n\t\t\t\t       ").lower()

        try:
            
            if Generando_BD == "si":
                
                global Conexión, db, dc, Nombre_DB, Nombre_DC

                Conexión = MongoClient("mongodb://localhost:27017/")

                if Conexión.admin.command("ping"):
                    
                    Limpieza_consola()

                    print(f"{marco}╔══════════════════════════════════════════════════════════════════════════════╗{fin}")
                    print(f"{marco}║{fondo}                                                                              {fin+marco}║{fin}")
                    print(f"{marco}║{fondo}                 {texto}Creación de la base de Datos con un nombre específico{fin+fondo}        {fin+marco}║{fin}")
                    print(f"{marco}║{fondo}                                                                              {fin+marco}║{fin}")
                    print(f"{marco}╠══════════════════════════════════════════════╦═══════════════════════════════╣{fin}")
                    Nombre_DB = input(f"{marco}║{fondo}        {texto}Nombre de la Base de Datos{fin+fondo}            {fin+marco}║{fin}                ")
                    print(f"{marco}╠══════════════════════════════════════════════╬═══════════════════════════════╣{fin}")
                    Nombre_DC = input(f"{marco}║{fondo}        {texto}Nombre de la Documentación{fin+fondo}            {fin+marco}║{fin}                ")
                    print(f"{marco}╠══════════════════════════════════════════════╩═══════════════════════════════╣{fin}")

                    if Nombre_DB not in Conexión.list_database_names():
                        
                        db = Conexión.get_database(name=f"{Nombre_DB}")
                        db.create_collection(name=f"{Nombre_DC}")

                        print(f"{marco}║{fondo}                                                                              {fin+marco}║{fin}")
                        print(f"{marco}║{fondo}                    {fin+texto_correcto}La Base de Datos fue creada con éxito.{fin+fondo}                    {fin+marco}║{fin}")
                        print(f"{marco}║{fondo}                {fin+texto_correcto}Presione ENTER para continuar con el programa.{fin+fondo}                {fin+marco}║{fin}")
                        print(f"{marco}║{fondo}                                                                              {fin+marco}║{fin}")
                        input(f"{marco}╚══════════════════════════════════════════════════════════════════════════════╝{fin}")

                    else:
                        
                        print(f"{marco}║{fondo}                                                                              {fin+marco}║{fin}")
                        print(f"{marco}║{fondo}            {fin+error_texto}La base de datos ya existe y ya esta activa para guardar!.{fin+fondo}        {fin+marco}║{fin}")
                        print(f"{marco}║{fondo}                {fin+error_texto}Presione ENTER para continuar con el programa.{fin+fondo}                {fin+marco}║{fin}")
                        print(f"{marco}║{fondo}                                                                              {fin+marco}║{fin}")
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
                Error_Mensaje_pre_Conexión()
                continue

        except:
            
            print("Error interno, Algo salio mal con la conexión!.")
            input()

        break

    return Generando_BD

def Mongo_Atlas_Conexión(Nombre: str):
    
    while True:

        print(f"{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
        print(f"{marco}║{fondo}                                                                               {fin+marco}║{fin}")
        print(f"{marco}║{fondo}                       {texto}Bienvenido a MongoDB Atlas{fin+fondo}                              {fin+marco}║{fin}")
        print(f"{marco}║{fondo}                                                                               {fin+marco}║{fin}")
        print(f"{marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
        Usuario = input(f"{marco}║{fondo}               {texto}Usuario{fin+fondo}               {marco}║{fin}         ")
        print(f"{marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
        contraseña = getpass(f"{marco}║{fondo}            {texto}Contraseña{fin+fondo}               {marco}║{fin}         ")
        print(f"{marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
        Cluster = input(f"{marco}║{fondo}      {texto}Nombre del Cluster{fin+fondo}             {marco}║{fin}         ")
        print(f"{marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
        Identificador = input(f"{marco}║{fondo}      {texto}Identificador del Cluster{fin+fondo}      {marco}║{fin}         ")
        print(f"{marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")

        global Atlas, Atlas_db, Atlas_dc , Atlas_Doc, Atlas_DB
        Atlas = MongoClient(f"mongodb+srv://{Usuario}:{contraseña}@{Cluster}.{Identificador}.mongodb.net/?retryWrites=true&w=majority")

        try:
    
            print(f"{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
            print(f"{marco}║{fondo}                                                                               {fin}║{fin}")
            print(f"{marco}║{fondo}     {texto}{Nombre.capitalize()}, ¿ Quiere generar una Base de datos con un nombre en especifico?{fin+fondo}    {fin+marco}║{fin}")
            print(f"{marco}║{fondo}                                                                               {fin}║{fin}")
            print(f"{marco}╠═══════════════════════════════════════╦═══════════════════════════════════════╣{fin}")
            print(f"{marco}║{fondo}             {texto}Sí, Quiero  < si >{fin+fondo}        {fin+marco}║{fondo}        {texto}< no >  No, no quiero{fin+fondo}          {fin+marco}║{fin}")
            print(f"{marco}╚═══════════════════════════════════════╩═══════════════════════════════════════╝{fin}")
            Pregunta = input("\n\t\t\t\t\t").lower()
            
            try:

                if Pregunta == "si":

                    if Atlas.admin.command("ping"):
                        
                        print(f"{marco}╔══════════════════════════════════════════════════════════════════════════════╗{fin}")
                        print(f"{marco}║{fondo}                                                                              {fin+marco}║{fin}")
                        print(f"{marco}║{fondo}                 {texto}Creación de la base de Datos con un nombre específico{fin+fondo}        {fin+marco}║{fin}")
                        print(f"{marco}║{fondo}                                                                              {fin+marco}║{fin}")
                        print(f"{marco}╠══════════════════════════════════════════════╦═══════════════════════════════╣{fin}")
                        Atlas_DB = input(f"{marco}║{fondo}        {texto}Nombre de la Base de Datos{fin+fondo}            {fin+marco}║{fin}                ")
                        print(f"{marco}╠══════════════════════════════════════════════╬═══════════════════════════════╣{fin}")
                        Atlas_Doc = input(f"{marco}║{fondo}        {texto}Nombre de la Documentación{fin+fondo}            {fin+marco}║{fin}                ")
                        print(f"{marco}╠══════════════════════════════════════════════╩═══════════════════════════════╣{fin}")

                        if Atlas_DB not in Atlas.list_database_names():
                            
                            Atlas_db = Atlas.get_database(name=f"{Atlas_DB}")
                            Atlas_db.create_collection(name=f"{Atlas_Doc}")

                            print(f"{marco}║{fondo}                                                                              {fin+marco}║{fin}")
                            print(f"{marco}║{fondo}                    {fin+texto_correcto}La Base de Datos fue creada con éxito.{fin+fondo}                    {fin+marco}║{fin}")
                            print(f"{marco}║{fondo}                {fin+texto_correcto}Presione ENTER para continuar con el programa.{fin+fondo}                {fin+marco}║{fin}")
                            print(f"{marco}║{fondo}                                                                              {fin+marco}║{fin}")
                            input(f"{marco}╚══════════════════════════════════════════════════════════════════════════════╝{fin}")

                        else:
                            
                            print(f"{marco}║{fondo}                                                                              {fin+marco}║{fin}")
                            print(f"{marco}║{fondo}            {fin+error_texto}La base de datos ya existe y ya esta activa para guardar!.{fin+fondo}        {fin+marco}║{fin}")
                            print(f"{marco}║{fondo}                {fin+error_texto}Presione ENTER para continuar con el programa.{fin+fondo}                {fin+marco}║{fin}")
                            print(f"{marco}║{fondo}                                                                              {fin+marco}║{fin}")
                            input(f"{marco}╚══════════════════════════════════════════════════════════════════════════════╝{fin}")

                        Atlas_db = Atlas[f"{Atlas_DB}"]
                        Atlas_dc = Atlas_db[f"{Atlas_Doc}"]

                elif Pregunta == "no":

                    if Atlas.admin.command("ping"):
                        
                        if "Calculadora" not in Atlas.list_database_names():
                            
                            Atlas_db = Atlas.get_database(name="Calculadora")
                            Atlas_db.create_collection(name="Historial")

                        Atlas_db = Atlas["Calculadora"]
                        Atlas_dc = Atlas_db["Historial"]
                        break

                else:
                    
                    Limpieza_consola()
                    Error_Mensaje_de_Conexión()
                    continue
            
            except:
                
                print("Error interno, Algo salio mal con la conexión!.")
                input()
                
        except:
            
            print("¡Error!, The something is wrong.")
        
        break    
    
    return Pregunta
        
def Banner(Respuesta_historial: str, retorna_conexion: str, Respuesta_tipo_conexion: str):
    
    
    if Respuesta_historial == "no" and retorna_conexion == "no" and  Respuesta_tipo_conexion == "no":
        
        print(f"{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
        print(f"{marco}║{fondo}                       {fin+error_texto}Estado de Conexión: Sin conexión{fin+fondo}                        {fin+marco}║{fin}")
        print(f"{marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")            
    
    else: 
        
        if retorna_conexion == "si":
            
            if Respuesta_tipo_conexion == "1":
            
                Nombre_servidor = f"{Conexión.HOST}:{Conexión.PORT}"
                Version = Conexión.server_info().get("version")
                Nombre_BD = Conexión.list_database_names()
                Nombre_Doc = db.list_collection_names()

                for lista_BD in Nombre_BD:
                    
                    if lista_BD == Nombre_DB:
                    
                        Nombre_BD = lista_BD

                for lista_Doc in Nombre_Doc:
                    
                    if lista_Doc == Nombre_DC:
                    
                        Nombre_Doc = lista_Doc
                
                print(f"{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
                print(f"{marco}║{fondo}                          {fin+texto_correcto}Estado de Conexión: Conectado{fin+fondo}                        {fin+marco}║{fin}")
                print(f"{marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
                print(f"{marco}║{fondo}      {fin+texto_correcto}Servidor: {Nombre_servidor}{fondo}         {fin+marco}║{fondo}      {fin+texto_correcto}Versión MongoDB: {Version}{fondo}          {fin+marco}║{fin}")
                print(f"{marco}╠════════════════════════════════════════╬══════════════════════════════════════╣{fin}")
                print(f"{marco}║{fondo}       {fin+texto_correcto}Nombre de la BD: {Nombre_BD}{fondo}           {fin+marco}║{fondo}     {fin+texto_correcto}Documentación: {Nombre_Doc}{fondo}         {fin+marco}║{fin}")
                print(f"{marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
            
            elif Respuesta_tipo_conexion == "2":
                
                Atlas_servidor = f"{Atlas.address[0]}:{Atlas.address[1]}"
                Version = Atlas.server_info().get("version")
                Atlas_BD = Atlas.list_database_names()
                Atlas_Doc = Atlas_db.list_collection_names()

                for lista_BD in Atlas_BD:
                    
                    if lista_BD == Atlas_DB:
                        
                        Atlas_BD = lista_BD

                for lista_Doc in Atlas_Doc:
                    
                    if lista_Doc == Atlas_Doc:
                        
                        Atlas_Doc = lista_Doc
                
                print(f"{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
                print(f"{marco}║{fondo}                          {fin+texto_correcto}Estado de Conexión: Conectado{fin+fondo}                        {fin+marco}║{fin}")
                print(f"{marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
                print(f"{marco}║{fondo}      {fin+texto_correcto}Servidor: {Atlas_servidor}{fondo}         {fin+marco}║{fondo}      {fin+texto_correcto}Versión MongoDB: {Version}{fondo}          {fin+marco}║{fin}")
                print(f"{marco}╠════════════════════════════════════════╬══════════════════════════════════════╣{fin}")
                print(f"{marco}║{fondo}       {fin+texto_correcto}Nombre de la BD: {Atlas_BD}{fondo}           {fin+marco}║{fondo}     {fin+texto_correcto}Documentación: {Atlas_Doc}{fondo}         {fin+marco}║{fin}")
                print(f"{marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
        
        elif retorna_conexion == "no":
            
            if Respuesta_tipo_conexion == "1":
            
                Nombre_servidor = f"{Conexión.HOST}:{Conexión.PORT}"
                Version = Conexión.server_info().get("version")
                Nombre_BD = Conexión.list_database_names()[0]
                Nombre_Doc = db.list_collection_names()[0]
                
                print(f"{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
                print(f"{marco}║{fondo}                          {fin+texto_correcto}Estado de Conexión: Conectado{fin+fondo}                        {fin+marco}║{fin}")
                print(f"{marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
                print(f"{marco}║{fondo}      {fin+texto_correcto}Servidor: {Nombre_servidor}{fondo}         {fin+marco}║{fondo}      {fin+texto_correcto}Versión MongoDB: {Version}{fondo}          {fin+marco}║{fin}")
                print(f"{marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
                print(f"{marco}║{fondo}     {fin+texto_correcto}Nombre de la BD: {Nombre_BD}{fondo}       {fin+marco}║{fondo}     {fin+texto_correcto}Documentación: {Nombre_Doc}{fondo}         {fin+marco}║{fin}")
                print(f"{marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")

            elif Respuesta_tipo_conexion == "2":
                
                Atlas_servidor = f"{Atlas.address[0]}:{Atlas.address[1]}"
                Version = Atlas.server_info().get("version")
                Atlas_BD = Atlas.list_database_names()[0]
                Atlas_Doc = Atlas_db.list_collection_names()[0]
                
                print(f"{marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
                print(f"{marco}║{fondo}                          {fin+texto_correcto}Estado de Conexión: Conectado{fin+fondo}                        {fin+marco}║{fin}")
                print(f"{marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
                print(f"{marco}║{fondo}  {fin+texto_correcto}Servidor: {Atlas_servidor}{fondo}  {fin+marco}║{fondo} {fin+texto_correcto}MongoDB: {Version}{fondo} {fin+marco}║{fin}")
                print(f"{marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
                print(f"{marco}║{fondo}     {fin+texto_correcto}Nombre de la BD: {Atlas_BD}{fondo}       {fin+marco}║{fondo}     {fin+texto_correcto}Documentación: {Atlas_Doc}{fondo}         {fin+marco}║{fin}")
                print(f"{marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")    

                
def Ingreso_Datos(Respuesta : str, Nombre : str, Numero1 : int, Operador : str, Numero2 : int, Resultado: int):
    
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
                

def Menu_BD ():
    
    print (" Bienvenido al Menu de tu Base de datos.")
    print ("")
    print (" A - Crear nueva Base de datos.")
    print (" B - Mostrar listado de Base de datos. ")
    print (" C - Guardar información en otra Base de Datos.  ")
    print (" D - Limpieza completa del historial de operaciones.  ")
    print (" E - Borrar un dato del historial de operaciones.  ")
    
    print("Trabajando en este Menu.....")
        
    input()