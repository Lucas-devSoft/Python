from  pymongo import   MongoClient
from   Logica import Limpieza_consola, Error_Mensaje_pre_Conexion
from  Colores import *

def Conexion_Local(Nombre : str):
    
    while True:
        
        Limpieza_consola()
        
        print                                       (f"                   {marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
        print                                       (f"                   {marco}║{fondo}                                                                               {fin}║{fin}") 
        print                                       (f"                   {marco}║{fondo}     {texto}{Nombre.capitalize()}, ¿ Quiere generar una Base de datos con un nombre en especifico?{fin+fondo}    {fin+marco}║{fin}")
        print                                       (f"                   {marco}║{fondo}                                                                               {fin}║{fin}")
        print                                       (f"                   {marco}╠═══════════════════════════════════════╦═══════════════════════════════════════╣{fin}")
        print                                       (f"                   {marco}║{fondo}                                       {fin+marco}║{fondo}                                       {fin}║{fin}") 
        print                                       (f"                   {marco}║{fondo}             {texto}Sí, Quiero  < si >{fin+fondo}        {fin+marco}║{fondo}        {texto}< no >  No, no quiero{fin+fondo}          {fin+marco}║{fin}")
        print                                       (f"                   {marco}║{fondo}                                       {fin+marco}║{fondo}                                       {fin}║{fin}")           
        print                                       (f"                   {marco}╚═══════════════════════════════════════╩═══════════════════════════════════════╝{fin}")
        Pregunta = input                            ("\n\t\t\t\t\t\t\t   ").lower()
        
        try:
            
            if Pregunta == "si":
            
                global Conexion, db, dc , Nombre_DB, Nombre_DC
                
                Conexion = MongoClient("mongodb://localhost:27017/") 
                
                if Conexion.is_primary:
                    
                    Limpieza_consola()
                    
                    print                           (f"                   {marco}╔══════════════════════════════════════════════╦════════════════════════════════╗{fin}")
                    print                           (f"                   {marco}║{fondo}                                              {fin+marco}║                                {marco}║{fin}") 
                    Nombre_DB = input               (f"                   {marco}║{fondo}        {texto}Nombre de la Base de Datos{fin+fondo}            {fin+marco}║{fin}                ")
                    print                           (f"                   {marco}║{fondo}                                              {fin+marco}║                                {marco}║{fin}") 
                    print                           (f"                   {marco}╠══════════════════════════════════════════════╬════════════════════════════════╣{fin}")
                    print                           (f"                   {marco}║{fondo}                                              {fin+marco}║                                {marco}║{fin}") 
                    Nombre_DC = input               (f"                   {marco}║{fondo}        {texto}Nombre de la Documentación{fin+fondo}            {fin+marco}║{fin}                ")
                    print                           (f"                   {marco}║{fondo}                                              {fin+marco}║                                {marco}║{fin}") 
                    print                           (f"                   {marco}╠══════════════════════════════════════════════╩════════════════════════════════╣{fin}")                
                    
                    if Nombre_DB not in Conexion.list_database_names():
                        
                        db        = Conexion.get_database(name=f"{Nombre_DB}")
                        db.create_collection(name=f"{Nombre_DC}") 
                        
                        print                       (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}") 
                        print                       (f"                   {marco}║{fondo}                    {fin+texto_correcto}La Base de Datos fue creada con exito!.{fin+fondo}                    {fin+marco}║{fin}")
                        print                       (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}") 
                        print                       (f"                   {marco}╚═══════════════════════════════════════════════════════════════════════════════╝{fin}")                
                        
                    else:
                        
                        print                       (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}") 
                        print                       (f"                   {marco}║{fondo}            {fin+error_texto}La base de datos ya existe y ya esta activa para guardar!.{fin+fondo}         {fin+marco}║{fin}")
                        print                       (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
                        print                       (f"                   {marco}╚═══════════════════════════════════════════════════════════════════════════════╝{fin}") 

                    db = Conexion[f"{Nombre_DB}"]
                    dc = db[f"{Nombre_DC}"]
                    
            elif Pregunta == "no":
                
                Conexion = MongoClient("mongodb://localhost:27017/")
                
                if Conexion.is_primary: 
                
                    if "Calculadora" not in Conexion.list_database_names():

                        db        = Conexion.get_database(name="Calculadora")
                        db.create_collection(name="Historial") 
                        
                        db = Conexion["Calculadora"]
                        dc = db["Historial"]

                    else:
                        
                        db = Conexion["Calculadora"]
                        dc = db["Historial"]
                        
                        break
                
            else: 
                    
                Limpieza_consola()

                Error_Mensaje_pre_Conexion()
                
                continue
                    
        except:
            
                print("Error interno, Algo salio mal!.")  
                input()
     
        break
    
    return Pregunta
            
def Banner_de_Conexion(Pregunta : str):
    
    try:
        
        if Conexion.is_primary:
            
            if Pregunta == "si" :
                
                Nombre_servidor = f"{Conexion.HOST}:{Conexion.PORT}" 
                Version = Conexion.server_info().get("version")
                Nombre_BD  = Conexion.list_database_names()
                Nombre_Doc = db.list_collection_names()
                
                for lista_BD in Nombre_BD:
                    
                    if lista_BD == Nombre_DB:
                        
                        Nombre_BD = lista_BD 
                
                for lista_Doc in Nombre_Doc: 
                        
                    if lista_Doc == Nombre_DC:
                        
                        Nombre_Doc = lista_Doc
                
                print                               (f"                   {marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")     
                print                               (f"                   {marco}║{fondo}                          {fin+texto_correcto}Estado de Conexión: Conectado{fin+fondo}                        {fin+marco}║{fin}")    
                print                               (f"                   {marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
                print                               (f"                   {marco}║{fondo}      {fin+texto_correcto}Servidor: {Nombre_servidor}{fondo}         {fin+marco}║{fondo}      {fin+texto_correcto}Versión MongoDB: {Version}{fondo}          {fin+marco}║{fin}")
                print                               (f"                   {marco}╠════════════════════════════════════════╬══════════════════════════════════════╣{fin}")
                print                               (f"                   {marco}║{fondo}       {fin+texto_correcto}Nombre de la BD: {Nombre_BD}{fondo}           {fin+marco}║{fondo}     {fin+texto_correcto}Documentación: {Nombre_Doc}{fondo}         {fin+marco}║{fin}") 
                print                               (f"                   {marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
            
            elif Pregunta == "no":    
                
                Nombre_servidor = f"{Conexion.HOST}:{Conexion.PORT}" 
                Version = Conexion.server_info().get("version")
                Nombre_BD  = Conexion.list_database_names()[0]
                Nombre_Doc = db.list_collection_names()[0]
                
                print                               (f"                   {marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")     
                print                               (f"                   {marco}║{fondo}                          {fin+texto_correcto}Estado de Conexión: Conectado{fin+fondo}                        {fin+marco}║{fin}")    
                print                               (f"                   {marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
                print                               (f"                   {marco}║{fondo}      {fin+texto_correcto}Servidor: {Nombre_servidor}{fondo}         {fin+marco}║{fondo}      {fin+texto_correcto}Versión MongoDB: {Version}{fondo}          {fin+marco}║{fin}")
                print                               (f"                   {marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
                print                               (f"                   {marco}║{fondo}     {fin+texto_correcto}Nombre de la BD: {Nombre_BD}{fondo}       {fin+marco}║{fondo}     {fin+texto_correcto}Documentación: {Nombre_Doc}{fondo}         {fin+marco}║{fin}") 
                print                               (f"                   {marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
    
    except:
    
        print                                   (f"                   {marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}") 
        print                                   (f"                   {marco}║{fondo}                       {fin+error_texto}Estado de Conexión: Sin conexión{fin+fondo}                        {fin+marco}║{fin}")  
        print                                   (f"                   {marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")      
    
""" def Mongo_Atlas_Conexion():
    
    try:
                
        User_Name = input("Please Insert your User:  ")
        Password  = input("Please Insert your Password:  ")
        Cluster   = input("Please Insert your Cluster Name :  ")
        
        Conexion = MongoClient(f"mongodb+srv://{User_Name}:{Password}@{Cluster}.mongodb.net/?retryWrites=true&w=majority")
            
        Conexion.drop_database(name_or_database="asd")

        Name_Atlas_db = input(" Please insert the name data base do you want create:      ")
        Name_Atlas_Documentation = input(" Please insert the name to the documentation do you want create:     ") 
        
        
        db       = Conexion[f"{Name_Atlas_db}"]
        document = db.create_collection(f"{Name_Atlas_Documentation}") 
        
        db_list  = Conexion.list_database_names()   
        document_list = db.listextoollection_names()    
        
        if f"{Name_Atlas_db}" in db_list and f"{Name_Atlas_Documentation}" in document_list:
            
            print("Data Base and Collection is Create Succesfully")
        
        else: 
            
            print("Error, Something went wrong!")
        
        #rzLKKvhywizonEtw

    except:
                
        print("¡Error!, The something is wrong.") """
    
"""
          
def Create_DB(option):
    
    
        Limpieza_consola()
        print()
        
        print                                                           (f"                          {m+b}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin+b_end}")
        print                                                           (f"                          {m+b}█                                                                           █{fin+b_end}")
        print                                                           (f"                          {m+b}█                 {t}would you like to create a database?{t_end}                      {marco}█{fin+b_end}")
        print                                                           (f"                          {m+b}█                                                                           █{fin+b_end}")
        print                                                           (f"                          {m+b}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin+b_end}")
        print                                                           (f"                          {m+b}█                                     █                                     █{fin+b_end}") 
        print                                                           (f"                          {m+b}█           {t}Yes, I want  < Y >{t_end}        {marco}█      {t}< N >  NO, I want not{t_end}          {marco}█{fin+b_end}")
        print                                                           (f"                          {m+b}█                                     █                                     █{fin+b_end}")           
        print                                                           (f"                          {m+b}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin+b_end}")
        Question = input                                                ("\n\t\t\t\t\t\t\t        ").upper() 
        
        if Question == "Y":
            
            print()
            
            print                                                       (f"                          {m+b}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin+b_end}")
            print                                                       (f"                          {m+b}█                                                                           █{fin+b_end}")
            Name_Local_db   = input                                     (f"                          {m+b}█    {t}Please insert the name data base do you want create :{t_end}                {marco}█{fin+b_end}")
            print                                                       (f"                          {m+b}█                                                                           █{fin+b_end}")
            print                                                       (f"                          {m+b}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin+b_end}")
            
            if f"{Name_Local_db}" in Conexion.list_database_names():
                    
                print("DataBase create succesfully") 
                Name_Local_Documentation = input(" Please insert the name to the documentation do you want create:     ")
                
            document        = db.create_collection(f"{Name_Local_Documentation}")        
            if f"{Name_Local_Documentation}" in db.listextoollection_names():
                    
                print                                                   (f"                          {m+b}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin+b_end}")
                print                                                   (f"                          {m+b}█                                                                           █{fin+b_end}")
                print                                                   (f"                          {m+b}█                  {t}Documentation create succesfully") 
                
            db              = Conexion[f"{Name_Local_db}"]
                
"""
def Insert_A_F(Nombre : str, Numero1 : int, Operador : str, Numero2 : int, Resultado : int):
        
    dc.insert_one({ "Nombre"   : Nombre,
                    "Valor_1"  : Numero1,
                    "Operador" : Operador,
                    "Valor_2"  : Numero2,
                    "Resultado": Resultado})
    
    for lista in dc.find({"Nombre"}):
        
        print(lista)
    
    
        
def Insert_G_H(Nombre : str, Numero1 : int, Operacion : str, Resultado : str):
        
    dc.insert_one({"Nombre" : Nombre, "Valor" : Numero1, "Operación": Operacion, "Resultado": Resultado})
    
    
    
           
""" def Delete():
    
    value_delete = input(" What information do you want delete? < One > or < All >:  ")
    
    collection.delete_one(f"{}")   """