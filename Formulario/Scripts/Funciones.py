from datetime import date
from Funciones_Errores import *
import json, re , os

"""
    
    FUNCION LIMPIAR CONSOLA
    
"""


def limpiar_consola():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')  
  
    
"""

    FUNCION DE GUARDADO DE DATOS JSON

"""

def guardar_datos(Datos_Personales):
    
    with open('Datos_Registrados.json','a',encoding='utf8') as archivo:
       
        for personales in Datos_Personales:
           
            json.dump(personales,archivo,indent=4,default=str,ensure_ascii=False)  
    
    if os.path.exists('Datos_Registrados.json'):
    
        return True  
    
def guardar_datos(Datos_Laborales):
    
    with open('Datos_Registrados.json','a',encoding='utf8') as archivo:
       
        for personales in Datos_Laborales:
           
            json.dump(personales,archivo,indent=4,default=str,ensure_ascii=False)  
    
    if os.path.exists('Datos_Registrados.json'):
    
        return True  
    
    
def guardar_datos(Datos_Academicos):
    
    with open('Datos_Registrados.json','a',encoding='utf8') as archivo:
       
        for personales in Datos_Academicos:
           
            json.dump(personales,archivo,indent=4,default=str,ensure_ascii=False)  
    
    if os.path.exists('Datos_Registrados.json'):
    
        return True  

def Menu(estado_A,estado_B,estado_C):
       
    if estado_A == True and estado_B == False and estado_C == False:           
                        
        estado_A = 'COMPLETADO'
        estado_B = 'INCOMPLETO'
        estado_C = 'INCOMPLETO'
                
    elif estado_B == True and estado_A == False and estado_C == False:
                    
        estado_B = 'COMPLETADO'
        estado_A = 'INCOMPELTO'
        estado_C = 'INCOMPLETO'
                    
    elif estado_C == True and estado_A == False and estado_B == False: 
                    
        estado_C = 'COMPLETADO'
        estado_A = 'INCOMPLETO'
        estado_B = 'INCOMPLETO'     
               
    print                                                                                        ( '              ┌───────────────────────────────────────────────────────────────┐      ')
    print                                                                                        ( '        ┌─────┤  DESARROLLADO CON EL LENGUAJE DE PYTHON POR LUCAS E. SANCHEZ  ├─────┐')
    print                                                                                        ( '        │     └───────────────────────────────────────────────────────────────┘     │')
    print                                                                                        ( '        │              ╔═════════════════════════════════════════════╗              │')
    print                                                                                        ( '        │              ║   FORMULARIO CON SALIDA DE DATOS A JSON     ║              │')
    print                                                                                        ( '        │              ╚═════════════════════════════════════════════╝              │')
    print                                                                                        ( '        │                                                                           │')
    print                                                                                        ( '        │            ╔════════════════════════════════════╦════════════╗            │')
    print                                                                                        (f'        │            ║ A ► FORMULARIO DE DATOS PERSONALES ║ {estado_A} ║            │')
    print                                                                                        ( '        │            ╠════════════════════════════════════╬════════════╣            │')
    print                                                                                        (f'        │            ║ B ► FORMULARIO DE DATOS LABORALES  ║ {estado_B} ║            │')
    print                                                                                        ( '        │            ╠════════════════════════════════════╬════════════╣            │')
    print                                                                                        (f'        │            ║ C ► FORMULARIO DE DATOS ACADEMICOS ║ {estado_C} ║            │')
    print                                                                                        ( '        │            ╚════════════════════════════════════╩════════════╝            │')
    print                                                                                        ( '        |                                                                           |')
                
def opcion_A(Finalizado):
        
    limpiar_consola()
        
    print('\n\n')
    
    print                                                                                        ( '              ┌───────────────────────────────────────────────────────────────┐      ')
    print                                                                                        ( '        ┌─────┤  DESARROLLADO CON EL LENGUAJE DE PYTHON POR LUCAS E. SANCHEZ  ├─────┐')
    print                                                                                        ( '        │     └───────────────────────────────────────────────────────────────┘     │')
    print                                                                                        ( '        ├───────────────────────────────────────────────────────────────────────────┤')
    print                                                                                        (f'        │---------------> ESTAS EN FORMULARIO DE DATOS PERSONALES <-----------------│')
    print                                                                                        ( '        ├───────────────────────────────────────────────────────────────────────────┤')    
    print                                                                                        ( '        │              ╔══════════════════════════════════════════════╗             │')
    print                                                                                        ( '        │              ║          INGRESE SU NOMBRE COMPLETO          ║             |')
    print                                                                                        ( '        │              ╠══════════════════════════════════════════════╣             │')
    nombre                                                                     =            input( '        │              ║                   ').upper()
    
    #verificacion de incoherencias en el nombre cono regex (que no tenga numeros)
    
    verificacion_1 = re.search(r"^[a-zA-Z\s]+",nombre)
    verificacion_2 = re.search(r"[0-9]+",nombre)
    
    if len(nombre) >= 3 and verificacion_1 and not (verificacion_2):                
        print                                                                                    ( '        │              ╠══════════════════════════════════════════════╣             │')                                                                                                  
        print                                                                                    ( '        │              ║            INGRESE SU APELLIDO               ║             |')
        print                                                                                    ( '        │              ╠══════════════════════════════════════════════╣             │')
        apellido                                                               =            input( '        │              ║                   ').upper()

        verificacion_1 = re.search(r"^[a-zA-Z\s]+",apellido)
        verificacion_2 = re.search(r"[0-9]+",apellido)
        
        if len(apellido) > 3 and verificacion_1 and not (verificacion_2) :
        
            print                                                                                ( '        │              ╠══════════════════════════════════════════════╣             │') 
            print                                                                                ( '        │              ║        ES JEFE/A DE FAMILIA < SI/NO >        ║             |')
            print                                                                                ( '        │              ╠══════════════════════════════════════════════╣             │')
            Jefe                                                               =            input( '        │              ║                   ').upper()

            if Jefe == 'SI' or Jefe == 'NO':
                
                print                                                                            ( '        │              ╠═══════════════╦══════════════╦═══════════════╣             │') 
                print                                                                            ( '        │              ║ SOLTER@ < S > ║ CASAD@ < C > ║ VIUD@  < V >  ║             │')
                print                                                                            ( '        │              ╠═══════════════╩═════╦════════╩═══════════════╣             │') 
                print                                                                            ( '        │              ║   DIVORCIAD@ < D >  ║  UNION DE HECHO < UH > ║             │')
                print                                                                            ( '        │              ╠═════════════════════╩════════════════════════╣             │') 
                print                                                                            ( '        │              ║        INGRESE SU ESTADO CIVIL               ║             |')
                print                                                                            ( '        │              ╠══════════════════════════════════════════════╣             │') 
                estado                                                         =            input( '        │              ║                   ').upper()
        
                if estado == 'S' or estado == 'C' or estado == 'V' or estado == 'D' or estado == 'UH':
            
                    match estado:
                        
                        case 'S':

                            estado = 'SOLTERO/A'

                        case 'C':

                            estado = 'CASADO/A'

                        case 'V':

                            estado = 'DIVORCIADO/A'

                        case 'D':

                            estado = 'VIUDO/A'

                        case 'UH':
                            
                            estado = 'UNION DE HECHO'
                    try:                          
                        
                        print                                                                    ( '        │              ╠══════════════════════════════════════════════╣             │') 
                        print                                                                    ( '        │              ║      INGRESE SU FECHA DE NACIMIENTO          ║             |')
                        print                                                                    ( '        │              ╠══════════════════════════════╦═══════════════╣             │') 
                        Fecha_Nacimiento                                       = date ( int(input( '        │              ║              (1 - 9999) AÑO  ║        ')),
                                                                                        int(input( '        │              ║              (1 - 12)   MES  ║        ')),
                                                                                        int(input( '        │              ║              (1 - 31)   DIA  ║        ')))
                        
                        fecha_actual = date.today()
                        Edad = fecha_actual.year - Fecha_Nacimiento.year
                        
                    except ValueError: 
                        
                        Msg_error_nacimiento()
                        
                        return False
                         
                    print                                                                        ( '        │              ╠══════════════════════════════╩═══════════════╣             │') 
                    print                                                                        ( '        │              ║         INGRESE SU NACIONALIDAD              ║             |')
                    print                                                                        ( '        │              ╠══════════════════════════════════════════════╣             │') 
                    Nacionalidad                                               =            input( '        │              ║                   ').upper()
                        
                    verificacion_1 = re.search(r"^[a-zA-Z\s]+",Nacionalidad)
                    verificacion_2 = re.search(r"[0-9]+",Nacionalidad)
                    
                    if len(Nacionalidad) >= 5 and verificacion_1 and not (verificacion_2):
                    
                        print                                                                    ( '        │              ╠══════════════════════════════════════════════╣             │') 
                        print                                                                    ( '        │              ║        INGRESE SU CIUDAD / PROVINCIA         ║             |')
                        print                                                                    ( '        │              ╠══════════════════════════════════════════════╣             │') 
                        ciudad                                                 =            input( '        │              ║                   ').upper()

                        verificacion_1 = re.search(r"^[a-zA-Z\s]+",ciudad)
                        verificacion_2 = re.search(r"[0-9]+",ciudad)
                        
                        if len(ciudad) >= 5 and verificacion_1 and not (verificacion_2):
                    
                            
                            print                                                                ( '        │              ╠══════════════════════════════════════════════╣             │') 
                            print                                                                ( '        │              ║            INGRESE SU LOCALIDAD              ║             |')
                            print                                                                ( '        │              ╠══════════════════════════════════════════════╣             │') 
                            localidad                                          =            input( '        │              ║                   ').upper()    
                            
                            verificacion_1 = re.search(r"^[a-zA-Z\s]+",localidad)
                            verificacion_2 = re.search(r"[0-9]+",localidad)

                            if len (localidad) >= 5 and verificacion_1 and not (verificacion_2) : 
                                
                                try:
                                
                                    print                                                        ( '        │              ╠══════════════════════════════════════════════╣             │') 
                                    print                                                        ( '        │              ║           INGRESE SU CODIGO POSTAL           ║             |')
                                    print                                                        ( '        │              ╠══════════════════════════════════════════════╣             │') 
                                    codigo_postal                              =       int(input ( '        |              ║                   ').upper())         

                                    if len(str(codigo_postal)) == 4 :
                                    
                                        print                                                    ( '        │              ╠═════════════════╦════════════════╦═══════════╣             │') 
                                        print                                                    ( '        │              ║ MASCULINO < M > ║ FEMENINO < F > ║ OTRO < O >║             │')
                                        print                                                    ( '        │              ╠═════════════════╩════════════════╩═══════════╣             │') 
                                        print                                                    ( '        │              ║            INGRESE SU GENERO                 ║             │')
                                        print                                                    ( '        │              ╠══════════════════════════════════════════════╣             │') 
                                        Genero                                 =           input ( '        |              ║                   ').upper() 
                                        
                                        if Genero == 'M' or Genero == 'F' or Genero == 'O':
                                            
                                            match Genero:
                                                
                                                case 'M':

                                                    Genero = 'MASCULINO'

                                                case 'F': 

                                                    Genero = 'FEMENINO'

                                                case 'O':

                                                    Genero = 'OTRO GENERO'
                                    
                                        else:
                                        
                                            Msg_error_Genero()
                                            
                                            return False                                
                                    else:
                                        
                                        Msg_error_Codigo(codigo_postal)
                                        
                                        return False      
                                    
                                except ValueError:
                                        
                                    Msg_error_try()
                        
                                    return False
                            else:
                                    
                                Msg_error_Localidad(localidad,verificacion_1,verificacion_2)
                                
                                return False
                        else:
                                
                            Msg_error_Ciudad(ciudad,verificacion_1,verificacion_2)
                            
                            return False               
                    else:
                                
                        Msg_error_Nacionalidad(Nacionalidad,verificacion_1,verificacion_2)  
                        
                        return False                                                                             
                else:
                                
                    Msg_error_Estado(estado) 
                    
                    return False      
            else:
                            
                Msg_error_Jefe(Jefe) 
                
                return False                     
        else:
                            
            Msg_error_Apellido(apellido,verificacion_1,verificacion_2) 
            
            return False 
    else:
                    
        Msg_error_Nombre(nombre,verificacion_1,verificacion_2)
        
        return False  
          
    Datos_Personales = {
        
                         'DATOS_PERSONALES': 
                            
                            [{          
                        
                                'NOMBRE'                      : nombre,
                                'APELLIDO'                    : apellido,
                                'ES_JEFE/A_DE_HOGAR'          : Jefe,
                                'ESTADO_CIVIL'                : estado,
                                'FECHA_DE_NACIMIENTO'         : Fecha_Nacimiento,
                                'EDAD'                        : Edad,
                                'NACIONALIDAD'                : Nacionalidad,
                                'CIUDAD'                      : ciudad,
                                'LOCALIDAD'                   : localidad,
                                'CODIGO POSTAL'               : codigo_postal,
                                'GENERO'                      : Genero, 
                                    
                            }]
                        }
                        
    
                                                    
    guardado = guardar_datos (Datos_Personales.items()) 
    
    if guardado:
        
        Finalizado = True
        
    elif not guardado:
        
        Finalizado = False
    
    return Finalizado

     
def opcion_B(Finalizado): 
    
    limpiar_consola()
        
    print('\n\n')
                                
    print                                                                                        ( '              ┌───────────────────────────────────────────────────────────────┐      ')
    print                                                                                        ( '        ┌─────┤  DESARROLLADO CON EL LENGUAJE DE PYTHON POR LUCAS E. SANCHEZ  ├─────┐')
    print                                                                                        ( '        │     └───────────────────────────────────────────────────────────────┘     │')
    print                                                                                        ( '        ├───────────────────────────────────────────────────────────────────────────┤')
    print                                                                                        (f'        │---------------> ESTAS EN FORMULARIO DE DATOS LABORALES <------------------│')
    print                                                                                        ( '        ├───────────────────────────────────────────────────────────────────────────┤')
    print                                                                                        ( '        │              ╔══════════════════════════════════════════════╗             │')                              
    print                                                                                        ( '        │              ║ SE ENCUENTRA TRABAJANDO ACTUALMENTE < SI/NO >║             |')
    print                                                                                        ( '        │              ╠══════════════════════════════════════════════╣             │')
    trabajo                                                                    =          input  ( '        |              ║                   ').upper()
    
    if trabajo == 'SI' or trabajo == 'NO':
        
        if trabajo == 'SI':
            
            print                                                                                ( '        │              ╠══════════════════════════════════════════════╣             │') 
            print                                                                                ( '        │              ║     INGRESE EL NOMBRE DE LA EMPRESA          ║             |')
            print                                                                                ( '        │              ╠══════════════════════════════════════════════╣             │')
            nombre_empresa                                                     =            input( '        |              ║                   ').upper()
            
            verificacion_1 = re.search(r"^[a-zA-Z\s]+",nombre_empresa)
            verificacion_2 = re.search(r"[0-9]+",nombre_empresa)
            
            if len(nombre_empresa) > 5 and verificacion_1 and not (verificacion_2):
                
                print                                                                            ( '        │              ╠══════════════════════════════════════════════╣             │')
                print                                                                            ( '        │              ║   INGRESE EL CUIT DE LA EMPRESA CON (-)      ║             |')
                print                                                                            ( '        │              ╠══════════════════════════════════════════════╣             │')
                cuit_empresa                                                   =         input   ( '        |              ║                   ')

                verificacion_1 = re.search(r"[0-9]{2}[-][0-9]{8}[-][0-9]{1}",cuit_empresa)
                verificacion_2 = re.search(r"[a-zA-Z]+",cuit_empresa)
                
                if len(cuit_empresa) == 13 and verificacion_1 and not (verificacion_2):
                    
                    print                                                                        ( '        │              ╠═══════════════╦════════════╦═════════════════╣             │')
                    print                                                                        ( '        │              ║ COMPLETA < C >║ MEDIA < M >║ FREELANCER < F >║             │')
                    print                                                                        ( '        │              ╠═══════════════╩════════════╩═════════════════╣             │')  
                    print                                                                        ( '        │              ║   INGRESE LA JORNADA LABORAL QUE REALIZA     ║             |')
                    print                                                                        ( '        │              ╠══════════════════════════════════════════════╣             │')
                    Jornada_laboral                                            =        input    ( '        |              ║                   ').upper()
                
                    if Jornada_laboral == 'C' or Jornada_laboral == 'M' or Jornada_laboral == 'F':
                        
                        match Jornada_laboral:
                            
                            case 'C':
                                Jornada_laboral = 'JORNADA COMPLETA'
                                
                            case 'M':
                                Jornada_laboral = 'JORNADA MEDIA'
                                
                            case 'F':
                                Jornada_laboral = 'FREELANCER'
                        
                        
                        print                                                                    ( '        │              ╠══════════════════════════════════════════════╣             │')
                        print                                                                    ( '        │              ║   INGRESE EL ÁREA EN EL QUE SE DESEMPEÑA     ║             |')
                        print                                                                    ( '        │              ╠══════════════════════════════════════════════╣             │')
                        sector                                                 =        input    ( '        |              ║                   ').upper()
                        
                        verificacion_1 = re.search(r"^[a-zA-Z\s.]+",sector)
                        verificacion_2 = re.search(r"[0-9]+",sector)
                        
                        if len (sector) > 5 and verificacion_1 and not (verificacion_2):
                            
                            try:
                                
                                print                                                            ( '        │              ╠══════════════════════════════════════════════╣             │')                           
                                print                                                            ( '        │              ║    INGRESE SU SALARIO MENSUAL EN BRUTOS      ║             |')
                                print                                                            ( '        │              ╠══════════════════════════════════════════════╣             │')
                                sueldo                                         =    float(input  ( '        |              ║                   '))
                                
                            except ValueError:
                                
                                Msg_error_try()
                                
                                return False
                                                                                                
                        else:
                            
                            Msg_error_sector(sector,verificacion_1,verificacion_2)
                            
                            return False                           
                    else:
                        
                        Msg_error_Jornada_laboral(Jornada_laboral)
                        
                        return False                                                                                         
                else:
                    
                    Msg_error_cuit_empresa(cuit_empresa,verificacion_1,verificacion_2)
                    
                    return False
            else:
                    
                Msg_error_nombre_Empresa(nombre_empresa,verificacion_1,verificacion_2)
                
                return False
                                                                                                
        elif trabajo == 'NO':
            
            nombre_empresa  = 'N/A'
            cuit_empresa    = 'N/A'
            Jornada_laboral = 'N/A'
            sector          = 'N/A'                                           
            sueldo          =  0.0                                   
                 
    else:
        
        Msg_error_Trabajo(trabajo)
         
        return False 
        
    Datos_Laborales = { 

                'DATOS_LABORALES':
                        
                    [{ 

                        'ACTIVIDAD_LABORAL' : trabajo,
                        'NOMBRE_DE_EMPRESA' : nombre_empresa,
                        'CUIT_EMPRESA'      : cuit_empresa,
                        'JORNADA_LABORAL'   : Jornada_laboral,
                        'ÁREA_LABORAL'      : sector,
                        'HABERES_BRUTOS'    : sueldo,                           

                    }]
                }
                                            
    guardado = guardar_datos (Datos_Laborales.items())

    if guardado:
    
        Finalizado = True
    
    elif not guardado:
        
        Finalizado = False 
            
    return Finalizado

def opcion_C(Finalizado):
    
    limpiar_consola()
        
    print('\n\n')
                                                    
    print                                                                                        ( '              ┌───────────────────────────────────────────────────────────────┐      ')
    print                                                                                        ( '        ┌─────┤  DESARROLLADO CON EL LENGUAJE DE PYTHON POR LUCAS E. SANCHEZ  ├─────┐')
    print                                                                                        ( '        │     └───────────────────────────────────────────────────────────────┘     │')
    print                                                                                        ( '        ├───────────────────────────────────────────────────────────────────────────┤')
    print                                                                                        (f'        │---------------> ESTAS EN FORMULARIO DE DATOS ACADÉMICOS <-----------------│')
    print                                                                                        ( '        ├───────────────────────────────────────────────────────────────────────────┤')
    print                                                                                        ( '        │              ╔══════════════════════════════════════════════╗             │')  
    print                                                                                        ( '        |              ║    ESTA ESTUDIANDO ACTUALMENTE  < SI/NO >    ║             |')
    print                                                                                        ( '        │              ╠══════════════════════════════════════════════╣             │')
    estudio                                                                    =      input      ( '        |              ║                  ').upper()

    if estudio == 'SI' or estudio == 'NO':

        if estudio == 'SI':
                
            print                                                                                ( '        │              ╔══════════════════════════════════════════════╗             │')  
            print                                                                                ( '        |              ║   INGRESE EL NOMBRE DE LA INSTITUCION        ║             |')
            print                                                                                ( '        │              ╠══════════════════════════════════════════════╣             │')
            nombre_institucion                                                 =           input ( '        |              ║   ').upper()                                                                                   

            verificacion_1 = re.search(r"^[a-zA-Z\s]+[0-9]+",nombre_institucion)
            
            if len(nombre_institucion) > 5 and verificacion_1:

                print                                                                            ( '        │              ╠═══════════════════════╦══════════════════════╣             │')
                print                                                                            ( '        │              ║     SECUNDARIO < S >  ║    TERCIARIO < T >   ║             │')
                print                                                                            ( '        │              ╠═══════════════════════╬══════════════════════╣             │')
                print                                                                            ( '        │              ║       FACULTAD < F >  ║  PROFESORADO < P >   ║             |')
                print                                                                            ( '        │              ╠═══════════════════════╩══════════════════════╣             │')      
                print                                                                            ( '        |              ║       INGRESE EL GRADO ACADEMICO ACTUAL      ║             |')
                print                                                                            ( '        │              ╠══════════════════════════════════════════════╣             │')
                grado_academico                                                =           input ( '        |              ║                  ').upper()                                       

                if grado_academico == 'S' or grado_academico == 'T' or grado_academico == 'F' or grado_academico == 'P': 

                    match grado_academico:

                        case 'S':
                            
                            grado_academico = 'SECUNDARIA'
                        
                        case 'T':

                            grado_academico = 'TERCIARIO'

                        case 'F':

                            grado_academico = 'FACULTAD'
                        
                        case 'P':

                            grado_academico = 'PROFESORADO'

                    try:
                    
                        print                                                                    ( '        │              ╠══════════════════════════════════════════════╣             │')
                        print                                                                    ( '        │              ║       INGRESE EL AÑO DE INGRESO ACADEMICO    ║             │')
                        print                                                                    ( '        │              ╠══════════════════════════════════════════════╣             │')
                        anio_ingreso                                            =     int (input ( '        │              ║                    '))
                        print                                                                    ( '        │              ╠══════════════════════════════════════════════╣             │')
                        print                                                                    ( '        │              ║       INGRESE EL AÑO DE EGRESO ACADEMICO     ║             │')
                        print                                                                    ( '        │              ╠══════════════════════════════════════════════╣             │')
                        anio_egreso                                             =     int (input ( '        |              ║                    '))
                        
                    except ValueError:
                        
                        Msg_error_try()
                        
                        return False                       
                else:
                
                    Msg_error_Nivel_estudio(grado_academico)
                    
                    return False                   
            else:
                    
                Msg_error_nombre_institucion(nombre_institucion,verificacion_1)   
                
                return False         
            
        elif estudio == 'NO':
            
            estudio            = 'NO'
            nombre_institucion = 'N/A'
            grado_academico    = 'N/A'
            anio_ingreso       = 0
            anio_egreso        = 0
                   
    else:
        
        Msg_error_estudio(estudio)
        
        return False
    
    
    Datos_Academicos = {
                        
                        'DATOS_LABORALES' : 
                            
                            [{ 

                                'ACTIVIDAD_ACADÉMICA'      : estudio,
                                'NOMBRE_DE_INSTITUCION'    : nombre_institucion,
                                'GRADO_ACADEMICO'          : grado_academico,
                                'ANIO_INGRESO'             : anio_ingreso,
                                'ANIO_EGRESO'              : anio_egreso                            

                            }]
                        }
             
    guardado = guardar_datos (Datos_Academicos.items())

    if guardado:
    
        Finalizado = True
    
    else:
        
        Finalizado = False
    
    return Finalizado