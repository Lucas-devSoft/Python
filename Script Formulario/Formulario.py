from Funciones import *
from datetime import date

while True:
    
    cont = 0
    i = 0 
     
    try:

        limpiar_consola()
        
        print                                                                                                                                         ( '       ┌─────────────────────────────────────────────────────────────┐')
        print                                                                                                                                         ( '       │           FORMULARIO CON SALIDA JSON EN PYTHON              │')
        print                                                                                                                                         ( '       ├────────────────────────────────────┬────────────────────────┤')
        cantidad_integrantes                                                                                                        =     int(  input ( '       │ Cuantas personas viven en su Hogar │       '))
    
        while i < cantidad_integrantes:

            i += 1

            limpiar_consola()
            
            print                                                                                                                                     ( '       ┌───────────────────────┬─────────────────────────────────────┐')
            print                                                                                                                                     (f'       │    DATOS PERSONALES   │   Integrante Familiar N° {i} de {cantidad_integrantes}.    │')
            print                                                                                                                                     ( '       ├───────────────────────┴────────────┬────────────────────────┤')
            nombre                                                                                                                  =            input( '       │                  Ingrese su Nombre │       ').capitalize()
                            
            if nombre.isalpha() and len(nombre) >= 4:                
                    
                print                                                                                                                                 ( '       ├────────────────────────────────────┼────────────────────────┤')
                apellido                                                                                                            =            input( '       │                Ingrese su Apellido │       ').capitalize()

                if apellido.isalpha() and len(apellido) >= 4:
                
                    print                                                                                                                             ( '       ├────────────────────────────────────┼────────────────────────┤')
                    Jefe                                                                                                            =            input( '       │          Es Jefe/a de Hogar? si/no │       ').lower()

                    if Jefe == 'si' or Jefe == 'no':
                        
                        print                                                                                                                         ( '       ├──────────────┬──────────────┬──────┴──────────┬─────────────┤')
                        print                                                                                                                         ( '       │  Casad@ (C)  │  Solter@ (S) │  Divorciad@ (D) │  Viud@ (V)  │')
                        print                                                                                                                         ( '       ├──────────────┴──────────────┴──────┬──────────┴─────────────┤')
                        estado                                                                                                      =            input( '       │                       Estado civil │       ').upper()
                
                        if estado == 'C' or estado == 'S' or estado == 'D' or estado == 'V':
                    
                            match estado:
                                
                                case 'C':
                                    estado = 'Casado'
                                case 'S':
                                    estado = 'Soltero'
                                case 'D':
                                    estado = 'Divorciado'
                                case 'V':
                                    estado = 'Viudo'
                                                                            
                            print                                                                                                                     ( '       ├────────────────────────────────────┴────────────────────────┤')
                            print                                                                                                                     ( '       │                 Ingrese su Fecha de Nacimiento              │')
                            print                                                                                                                     ( '       ├────────────────────────────────────┬────────────────────────┤')
                            Fecha_Nacimiento                                                                                        = date ( int(input( '       │                     (1 - 9999) Año │       ')),
                                                                                                                                             int(input( '       │                      (01 - 12) Mes │       ')),
                                                                                                                                             int(input( '       │                      (01 - 31) Dia │       ')))
                            fecha_actual = date.today()
                            Edad = fecha_actual.year - Fecha_Nacimiento.year

                            print                                                                                                                     ( '       ├────────────────────────────────────┼────────────────────────┤')
                            Nacionalidad                                                                                            =            input( '       │            Ingrese su Nacionalidad │       ').capitalize()

                            if Nacionalidad.isalpha() and len(Nacionalidad) >= 5:

                                print                                                                                                                 ( '       ├───────────────────┬────────────────────┬────────────────────┤')
                                print                                                                                                                 ( '       │    Femenino (F)   │    Masculino (M)   │     Otros (O)      │')
                                print                                                                                                                 ( '       ├───────────────────┴────────────────┬───┴────────────────────┤')
                                Genero                                                                                              =            input( '       │                 Ingrese su Genero  │       ').upper()
                                
                                if Genero == 'F' or Genero == 'M' or Genero == 'O':
                                    
                                    match Genero:
                                        
                                        case 'F':
                                            Genero = 'Femenino'
                                        case 'M': 
                                            Genero = 'Masculino'
                                        case 'O':
                                            Genero = 'Otros'
                                    
                                    limpiar_consola()
                                    
                                    print                                                                                                             ( '       ┌───────────────────────┬─────────────────────────────────────┐')
                                    print                                                                                                             (f'       │    DATOS LABORALES    │  Integrante Familiar N° {i} de {cantidad_integrantes}.     │')
                                    print                                                                                                             ( '       ├───────────────────────┴────────────┬────────────────────────┤')                               
                                    trabajo                                                                                         =            input( '       │   Ingrese si esta trabajando si/no │       ').lower()

                                    if trabajo == 'si' or trabajo == 'no':
                                        
                                        if trabajo == 'si':
                                            
                                            print                                                                                                     ( '       ├────────────────────────────────────┼────────────────────────┤')
                                            nombre_empresa                                                                          =            input( '       │     Ingrese Nombre de la empresa   │       ')
                                            
                                            if nombre_empresa.isascii() and len(nombre_empresa) > 5:
                                        
                                                print                                                                                                 ( '       ├────────────────────────┬───────────┴────────┬───────────────┤')
                                                print                                                                                                 ( '       │  Jornada Completa (JC) │ Media Jornada (MJ) │ Freelancer (F)│')
                                                print                                                                                                 ( '       ├────────────────────────┴───────────┬────────┴───────────────┤')
                                                Jornada_laboral                                                                     =            input( '       │       Ingrese su Jornada Laboral   │       ').upper()
                                                
                                                if Jornada_laboral == 'JC' or Jornada_laboral == 'MJ' or Jornada_laboral == 'F':
                                                    
                                                    match Jornada_laboral:
                                                        
                                                        case 'JC':
                                                            Jornada_laboral = 'Jornada Completa'
                                                            
                                                        case 'MJ':
                                                            Jornada_laboral = 'Media Jornada'
                                                            
                                                        case 'F':
                                                            Jornada_laboral = 'Freelancer'

                                                    print                                                                                             ( '       ├────────────────────────────────────┼────────────────────────┤')
                                                    sueldo                                                                          =      float(input( '       │     Ingrese su salario en brutos   │       '))
                                                
                                                else:
                                                    
                                                    Jornada_error_msg(Jornada_laboral)                                                                                    
                                            else:
                                                
                                                Empresa_error_msg(nombre_empresa)
                                                                                                                        
                                        elif trabajo == 'no':
                                            
                                            nombre_empresa  = None
                                            Jornada_laboral = None                                           
                                            sueldo          = None
                                    
                                    else:
                                        
                                        Trabajo_error_msg(trabajo)
     
                                    limpiar_consola()
                                                    
                                    print                                                                                                             ( '       ┌───────────────────────┬─────────────────────────────────────┐')
                                    print                                                                                                             (f'       │    DATOS ACADEMICOS   │  Integrante Familiar N° {i} de {cantidad_integrantes}.     │')
                                    print                                                                                                             ( '       ├───────────────────────┴────────────┬────────────────────────┤')         
                                    graduacion                                                                                      =            input( '       │        Es graduado Academico si/no │       ').lower()

                                    if graduacion == 'si' or graduacion == 'no':

                                        if graduacion == 'si':
                                             
                                            print                                                                                                     ( '       ├──────────────┬─────────────┬───────┴─────────┬──────────────┤')                                   
                                            print                                                                                                     ( '       │ Bachillerato | Técnicatura | Tecnicatura sup.│  Universidad |')
                                            print                                                                                                     ( '       │      (B)     |     (T)     |       (TS)      |       (U)    |')
                                            print                                                                                                     ( '       ├──────────────┴─────┼───────┴──────────┼──────┴──────────────┘')
                                            print                                                                                                     ( '       │   Profesorado (P)  │    Maestria (M)  │                      ')
                                            print                                                                                                     ( '       ├────────────────────┴──────────────┬───┘                      ')                                                                                            
                                            nivel_graduacion                                                                        =            input( '       │    Ingrese su nivel de graduacion │       ').upper()  
                                                
                                            if nivel_graduacion == 'B' or nivel_graduacion == ' T' or nivel_graduacion == 'TS' or nivel_graduacion == 'U' or nivel_graduacion == 'P' or nivel_graduacion == 'M':

                                                match nivel_graduacion:

                                                    case 'B':
                                                        nivel_graduacion  = 'Secundaria Bachiller'
                                                    case 'T': 
                                                        nivel_graduacion  = 'Secundaria Técnica'
                                                    case 'TS':
                                                        nivel_graduacion  = 'Técnicatura Superior'
                                                    case 'U':
                                                        nivel_graduacion  = 'Universidad'
                                                    case 'P':
                                                        nivel_graduacion  = 'Profesorado'
                                                    case 'M':
                                                        nivel_graduacion  = 'Maestria'
                                                                                    
                                                print                                                                                                ( '       ├────────────────────────────────────┼─────────────────────────┤')
                                                nombre_institucion_graduado                                                         =           input( '       │ Nombre institucion donde se graduo │       ').capitalize()     
                                    
                                                if nombre_institucion_graduado.isascii() and len(nombre_institucion_graduado) > 5: 
                                                            
                                                    print                                                                                            ( '       ├────────────────────────────────────┼─────────────────────────┤')
                                                    anio_ingreso                                                                    =     int (input ( '       │      Ingrese el año de su ingreso  │       '))
                                                    print                                                                                            ( '       ├────────────────────────────────────┼─────────────────────────┤')
                                                    anio_egreso                                                                     =     int (input ( '       │       Ingrese el año de su egreso  │       '))
                                                            
                                                else:
                                                    
                                                    Institucion_error_msg(nombre_institucion_graduado)             
                                            else:
                                                
                                                Nivel_graduacion_error_msg(nivel_graduacion)  
                                                                            
                                        elif graduacion == 'no':
                                            
                                            nivel_graduacion            = None
                                            nombre_institucion_graduado = None
                                            anio_ingreso                = None
                                            anio_egreso                 = None
                                    
                                    else:
                                        
                                        Graduacion_error_msg(graduacion)  
                                                   
                                    print                                                                                                            ( '       ├────────────────────────────────────┼─────────────────────────┤')
                                    estudia                                                                                         =          input ( '       │  Continua con sus estudios? si/no  │       ').lower()
                                            
                                    if estudia == 'si' or estudia == 'no':
                                            
                                        if estudia == 'si':
                                        
                                            print                                                                                                    ( '       ├────────────────────┬───────────────┬───────────┬─────────────┤')                                   
                                            print                                                                                                    ( '       │  Secundaria Adulto |  Secundaria   │ Terciario | Universidad |')
                                            print                                                                                                    ( '       |  Bachiller (SAB)   |  Tecnica (ST) |   (T)     |     (U)     |')
                                            print                                                                                                    ( '       ├────────────────────┴───────────────┴────┬──────┴─────────────┤')   
                                            academia_actual                                                                         =           input( '       │   Ingrese el grado academico que cursa  │       ').upper() 
                                            
                                            if academia_actual == 'SAB' or academia_actual == 'ST' or academia_actual == 'T' or academia_actual == 'U':
                                                
                                                match academia_actual:
                                                
                                                    case 'SAB':
                                                        academia_actual = 'Secundario de Adultos'
                                                    case 'ST':
                                                        academia_actual = 'Secundaria tecnica'
                                                    case 'T':
                                                        academia_actual = 'Terciario' 
                                                    case 'U':
                                                        academia_actual = 'Universidad'
                                                        
                                                print                                                                                                ( '       ├────────────────────────────────────┬─────────────────────────┤')
                                                nombre_institucion                                                                  =          input ( '       │          Nombre de la institucion  │       ').capitalize()                                                                                  
                                        
                                                if nombre_institucion.isascii() and len(nombre_institucion) > 5: 
                                                        
                                                    print                                                                                            ( '       ├────────────────────────────────────┼─────────────────────────┤')
                                                    ingreso                                                                         =     int (input ( '       │      Ingrese el año de su ingreso  │       '))
                                                    print                                                                                            ( '       ├────────────────────────────────────┼─────────────────────────┤')
                                                    egreso                                                                          =     int (input ( '       │       Ingrese el año de su egreso  │       '))                                                                                                      
                                                    print                                                                                            ( '       └────────────────────────────────────┴─────────────────────────┘')
                                                
                                                else:
                                            
                                                    Institucion_error_msg(nombre_institucion) 
                                                
                                            else:
                                                
                                                Academia_error_msg(academia_actual)
                        
                                        elif estudia == 'no':
                                            
                                            academia_actual     = None
                                            nombre_institucion  = None
                                            ingreso             = None
                                            egreso              = None  
                                                        
                                    else:
                                                
                                        Estudios_error_msg(estudia)                                                                                                                          
                                                                           
                                else:
                                    
                                    Genero_error_msg(Genero)     
                            else:
                                
                                Nacionalidad_error_msg(Nacionalidad)  
                                
                            Datos_ingresados = {
                        
                                    'IDENTIFICADOR_INGRESO'     : [{
                                                                    
                                                                    'IDENTIFICADOR_INTEGRANTE'    :i,
                                                                    'IDENTIFICADOR_FAMILIA'       :cont
                                                                    
                                                                    }],

                                    'DATOS_PERSONALES'          : [{ 
                                                            
                                                                    'NOMBRE'                      : nombre,
                                                                    'APELLIDO'                    : apellido,
                                                                    'ES_JEFE/A_DE_HOGAR'          : Jefe,
                                                                    'GENERO'                      : Genero,
                                                                    'FECHA_DE_NACIMIENTO'         : Fecha_Nacimiento,
                                                                    'EDAD'                        : Edad,
                                                                    'ESTADO_CIVIL'                : estado,
                                                                    'NACIONALIDAD'                : Nacionalidad
                                                                }],
                                    'DATOS_LABORALES'           : [{ 

                                                                    'NOMBRE_DE_EMPRESA'           :nombre_empresa,
                                                                    'JORNADA_LABORAL'             :Jornada_laboral,
                                                                    'HABERES_BRUTOS'              :sueldo                             
                                                                    }],
                                    
                                    'DATOS_ACADEMICOS'          : [{
                                        
                                                                    'ES_GRADUADO_ACADEMICO'       : graduacion,
                                                                    'GRADO_DE_GRADUACION'         : nivel_graduacion,                                                                                          
                                                                    'NOMBRE_INSTITUCION'          : nombre_institucion_graduado,
                                                                    'ANIO_INGRESO'                : anio_ingreso,
                                                                    'ANIO_EGRESO'                 : anio_egreso,
                                                                    'ESTA_ESTUDIANDO'             : estudia,
                                                                    'CURSO_ACTUAL'                : academia_actual,
                                                                    'NOMBRE_DE_LA_ACADEMIA'       : nombre_institucion,
                                                                    'INGRESO_ACADEMIA'            : ingreso,
                                                                    'EGRESO_ACADEMIA'             : egreso
                                                                        
                                                                }]
                                                    }
                            guardar_datos (Datos_ingresados.items())                            
                            
                            print()
                            print                                                                                                                    ( '       ┌──────────────────────────────────────────────┬──────────────┐')
                            preguntar                                                                                                   = input      ( '       |    Quiere agregar a una nueva familia? si/no │   ')
                            print                                                                                                                    ( '       └──────────────────────────────────────────────┴──────────────┘')   
                            
                            while preguntar == 'si':
                                
                                cont += 1
                                
                                print                                                                                                                ( '       ┌─────────────────────────────────────────────────────────────┐')
                                print                                                                                                                ( '       │           FORMULARIO CON SALIDA JSON EN PYTHON              │')
                                print                                                                                                                ( '       ├────────────────────────────────────┬────────────────────────┤')
                                cantidad_integrantes                                                                                =    int(  input ( '       │ Cuantas personas viven en su Hogar │       '))
                            
                            else: 
                                
                                while preguntar == 'no':
                                
                                    break
                                                                  
                        else:
                            
                            Estado_error_msg(estado)       
                    else:
                        
                        Jefe_error_msg(Jefe)                      
                else:
                        
                    Apellido_error_msg(apellido)                                          
            else:
                
                Nombre_error_msg(nombre) 
        
        break
    
    except ValueError or NameError:
        
        print( '       └────────────────────────────────────┴────────────────────────┘')
        print()
        print( '       ┌─────────────────────────────────────────────────────────────┐')
        print( '       │   ERROR,SE INGRESO UN DATO INVALIDO O EL CAMPO ES VACIO.    │')
        input( '       └─────────────────────────────────────────────────────────────┘')

        limpiar_consola()
        
        
   