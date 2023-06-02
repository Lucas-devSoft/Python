from datetime import date
import re, os, time

from colores import *

def Cartel():
    
    print(f"""{marco}
███████╗ ██████╗ ██████╗ ███╗   ███╗██╗   ██╗██╗      █████╗ ██████╗ ██╗ ██████╗ ███████╗
██╔════╝██╔═══██╗██╔══██╗████╗ ████║██║   ██║██║     ██╔══██╗██╔══██╗██║██╔═══██╗██╔════╝
█████╗  ██║   ██║██████╔╝██╔████╔██║██║   ██║██║     ███████║██████╔╝██║██║   ██║███████╗
██╔══╝  ██║   ██║██╔══██╗██║╚██╔╝██║██║   ██║██║     ██╔══██║██╔══██╗██║██║   ██║╚════██║
██║     ╚██████╔╝██║  ██║██║ ╚═╝ ██║╚██████╔╝███████╗██║  ██║██║  ██║██║╚██████╔╝███████║
╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚══════╝{fin}""")


def Limpiar_consola():

    command = 'clear'
    
    if os.name in ('nt', 'dos'):  # if the machine running in windows, use command cls
    
        command = 'cls'
    
    else:
        
        command
    
    os.system(command)


def Mensaje_Agradecimiento():
    
    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█                       {texto}Gracias por probar mi proyecto personal                         {fin+marco}█{fin}
{marco+fondo}█               {texto}En 5 segundos se cerrará el programa automáticamente.                   {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█{fin}
        """)
    
    time.sleep(5)
    exit()

    
def opcion_A():
    
    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█                         {texto}Formulario de datos personales                                {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
    Nombre_Apellido = input(f"{marco+fondo}█                     {texto}Nombre y Apellido : {fin}        ")   
    
    verificacion = re.search(r"^[^\d.,\-{}]*$",Nombre_Apellido)
    
    if verificacion:

        print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
        Estado_civil = input(f"{marco+fondo}█                          {texto}Estado Civil : {fin}        ")  
        
        verificacion = re.findall(r"^[^\d.,\-{}]*$",Estado_civil)

        if verificacion:
            
            print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
            Genero = input(f"{marco+fondo}█                                {texto}Genero : {fin}        ")  
            
            verificacion = re.findall(r"^[^\d.,\-{}]*$",Genero)
            
            if verificacion:
                
                try:
                    
                    print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                    Fecha_Nacimiento = date (int(input(f"{marco+fondo}█              {texto}Año de Nacimiento (YYYY) : {fin}        ")),
                                            int(input(f"{marco+fondo}█                {texto}Mes de Nacimiento (MM) : {fin}        ")),
                                            int(input(f"{marco+fondo}█                {texto}Dia de Nacimiento (DD) : {fin}        ")))

                    Fecha_actual = date.today()
                    Edad = Fecha_actual.year - Fecha_Nacimiento.year
                    
                except:
                    
                    return False    
                    
                print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                Nacionalidad = input(f"{marco+fondo}█                          {texto}Nacionalidad : {fin}        ")  
                
                verificacion = re.findall(r"^[^\d.,\-{}]*$",Nacionalidad)
                
                if verificacion:
                    
                    print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                    Provincia = input(f"{marco+fondo}█                             {texto}Provincia : {fin}        ")  
                    
                    verificacion = re.findall(r"^[^\d.,\-{}]*$",Provincia)
                    
                    if verificacion:
                        
                        print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                        Localidad = input(f"{marco+fondo}█                             {texto}Localidad : {fin}        ")  
                        
                        verificacion = re.findall(r"^[^\d.,\-{}]*$",Localidad)
                        
                        if verificacion:
                            
                            print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                            Codigo_Postal = input(f"{marco+fondo}█                         {texto}Código Postal : {fin}        ")  

                            verificacion = re.findall(r"[\d]{4}",Codigo_Postal)

                            if verificacion:
                                
                                print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                                Celular = input(f"{marco+fondo}█        {texto}(sin 0 ni 15) Teléfono Celular : {fin}        ")  

                                verificacion = re.findall(r"[\d]{10}",Celular)

                                if verificacion:
                                    
                                    print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                                    Correo = input(f"{marco+fondo}█                    {texto}Correo Electrónico : {fin}        ")  

                                    verificacion = re.findall(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",Correo)
                            
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
    
    while True:
                                
        print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█                         {texto}Formulario de datos laborales                                 {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
        
        Trabajo = input(f"{marco+fondo}█         {texto}¿Se encuentra trabajando actualmente? (si/no) : {fin}            ")
        
        if Trabajo == 'si':
                
            print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
            Nombre_empresa = input(f"{marco+fondo}█                         {texto}Nombre de la empresa : {fin}           ")
            
            verificacion = re.search(r"^[^\d.,\-{}]*$",Nombre_empresa)
            
            if verificacion:
                
                print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                Puesto_trabajo = input (f"{marco+fondo}█                     {texto}Puesto de trabajo : {fin}           ")

                verificacion = re.search(r"^[^\d.,\-{}]*$",Puesto_trabajo)
                
                if verificacion:
                    
                    print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                    Tiempo_trabajo = input(f"{marco+fondo}█       {texto}(Full Time/Part Time) Jornada Laboral : {fin}           ")

                    verificacion = re.search(r"^[^\d.,\-{}]*$",Tiempo_trabajo)
                    
                    if verificacion :
                        
                        try:
                        
                            print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                            Ingreso = int (input(f"{marco+fondo}█       {texto}Año de ingreso : {fin}           "))
                            
                            print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                            Egreso = int (input(f"{marco+fondo}█       {texto}(Año/Actualidad) Año de egreso : {fin}           "))

                            print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                            Sueldo = float (input(f"{marco+fondo}█       {texto}Salario en brutos : {fin}           "))

                        except:
                            
                            return False  
                        
                        if Ingreso and Egreso and Sueldo:
                            
                            return Nombre_empresa, Puesto_trabajo, Tiempo_trabajo, Ingreso, Egreso, Sueldo
                        
                    else:
                        
                        return False
                                                                                                                
                else:
                    
                    return False
                    
            else:
                
                return False
                                                                                                    
        elif Trabajo == 'no':
            
            print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
            Nombre_empresa = input(f"{marco+fondo}█         {texto}Nombre de la ultima empresa en la que trabajo : {fin}            ")
            
            verificacion = re.search(r"^[^\d.,\-{}]*$",Nombre_empresa)
            
            if verificacion:
                
                print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                Puesto_trabajo = input (f"{marco+fondo}█                                     {texto}Puesto de trabajo : {fin}            ")

                verificacion = re.search(r"^[^\d.,\-{}]*$",Puesto_trabajo)
                
                if verificacion:
                    
                    print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                    Tiempo_trabajo = input(f"{marco+fondo}█       {texto}(Full Time/Part Time) Jornada Laboral trabajada : {fin}            ")

                    verificacion = re.search(r"^[^\d.,\-{}]*$",Tiempo_trabajo)
                    
                    if verificacion :
                        
                        try:
                        
                            print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                            Ingreso = int (input(f"{marco+fondo}█                                       {texto}Año que ingresó : {fin}            "))
                        
                        except:
                            
                            return False     
                        
                        print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                        Egreso = input(f"{marco+fondo}█                       {texto}(Año/Actualidad) Año que egresó : {fin}            ")

                        verificacion = re.search(r"^[^.,\-{}]*$",Tiempo_trabajo)
                        
                        if verificacion:
                            
                            try: 
                                
                                print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                                Sueldo = float (input(f"{marco+fondo}█                                     {texto}Salario en brutos : {fin}            "))
                            
                            except:
                                
                                return False

                            if Ingreso and Egreso and Sueldo:
                                
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

def opcion_C():
                                                    
    print(f"""
{marco+fondo}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}
{marco+fondo}█                         {texto}Formulario de datos académicos                                {fin+marco}█{fin}
{marco+fondo}█                                                                                       {fin+marco}█{fin}""")
    Estudio = input(f"{marco+fondo}█   {texto}¿Se encuentra estudiando actualmente? (si/no) : {fin}           ")

    if Estudio == "si" :
                
        print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
        Nombre_empresa = input(f"{marco+fondo}█                        {texto}Nombre de la institución : {fin}           ")
            
        verificacion = re.search(r"^[^.,\-{}]*$",Nombre_empresa)
        
        if verificacion :
            
            print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
            Nombre_Titulo = input (f"{marco+fondo}█                               {texto}Nombre del título : {fin}           ")

            verificacion = re.search(r"^[^\d.,\-{}]*$",Nombre_Titulo)
            
            if verificacion :
                
                print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                Orientacion = input(f"{marco+fondo}█                           {texto}Orientación Académica : {fin}           ")

                verificacion = re.search(r"^[^\d.,\-{}]*$",Orientacion)
                
                if verificacion :
                    
                    try:
                        
                        print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                        Inicio = int (input(f"{marco+fondo}█                                   {texto}Año de inicio : {fin}           "))
                        
                        print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                        Egreso = int (input(f"{marco+fondo}█                  {texto}(Año/Actualidad) Año de egreso : {fin}           "))

                    except:
                        
                        return False
                    
                    if Inicio != False and Egreso != False:
                        
                        print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                        Turno = input(f"{marco+fondo}█            {texto}(Mañana/Tarde/Noche)Turno de cursada : {fin}           ")
                    
                        verificacion = re.search(r"^[^\d.,\-{}]*$",Turno)
                        
                        if verificacion :
                            
                            return Nombre_empresa, Nombre_Titulo, Orientacion, Inicio, Egreso, Turno
                    
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
        Nombre_empresa = input(f"{marco+fondo}█                 {texto}Nombre de la ultima institución : {fin}           ")
            
        verificacion = re.search(r"^[^.,\-{}]*$",Nombre_empresa)
        
        if verificacion :
            
            print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
            Nombre_Titulo = input (f"{marco+fondo}█                               {texto}Nombre del título : {fin}           ")

            verificacion = re.search(r"^[^\d.,\-{}]*$",Nombre_Titulo)
            
            if verificacion :
                
                print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                Orientacion = input(f"{marco+fondo}█                           {texto}Orientación Académica : {fin}           ")

                verificacion = re.search(r"^[^\d.,\-{}]*$",Orientacion)
                
                if verificacion :
                    
                    try:
                    
                        print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                        Inicio = int (input(f"{marco+fondo}█                                   {texto}Año de inicio : {fin}           "))
                        
                    except:
                        
                        return False
                    
                    print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                    Egreso = input(f"{marco+fondo}█                  {texto}(Año/Actualidad) Año de egreso : {fin}           ")

                    verificacion = re.search(r"^[^\D.,\-{}]*$",Egreso)
                    
                    if verificacion :
                        
                        print(f"{marco+fondo}█                                                                                       {fin+marco}█{fin}")
                        Turno = input(f"{marco+fondo}█            {texto}(Mañana/Tarde/Noche)Turno de cursada : {fin}           ")
                    
                        verificacion = re.search(r"^[^\d.,\-{}]*$",Turno)
                        
                        if verificacion :
                            
                            return Nombre_empresa, Nombre_Titulo, Orientacion, Inicio, Egreso, Turno

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
    
    else :
        
        return False