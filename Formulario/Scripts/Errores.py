"""

       MENSAJES DE ERROR PARA LOS DATOS PERSONALES

"""

def Msg_error_Nombre(nombre,verificacion_1,verificacion_2):

    while not (len(nombre) >= 3 and verificacion_1) or verificacion_2:
        
        print                                                                                                   ( '        │              ╠══════════════════════════════════════════════╣             │') 
        print                                                                                                   ( '        │              ║ EL FORMATO ES INVALIDO O EL CAMPO ESTA VACIO ║             |')
        
        break
    
def Msg_error_Apellido(apellido,verificacion_1,verificacion_2):
    
    while not (len(apellido) >= 3 and verificacion_1) or verificacion_2:
        
        print                                                                                                   ( '        │              ╠══════════════════════════════════════════════╣             │') 
        print                                                                                                   ( '        │              ║ EL FORMATO ES INVALIDO O EL CAMPO ESTA VACIO ║             |')
        
        break  
    
def Msg_error_Jefe(Jefe):
    
    while not (Jefe == 'SI' and Jefe == 'NO'):

        print                                                                                                   ( '        │              ╠══════════════════════════════════════════════╣             │') 
        print                                                                                                   ( '        │              ║  RESPUESTA INVALIDA O EL CAMPO ESTA VACIO.   ║             |')
        
        break   

        
def Msg_error_Estado(estado):
    
    while not (estado == 'S' and estado == 'C' and estado == 'D' and estado == 'V') or estado == '':
        
        print                                                                                                   ( '        │              ╠══════════════════════════════════════════════╣             │') 
        print                                                                                                   ( '        │              ║   RESPUESTA INVALIDA O EL CAMPO ESTA VACIO.  ║             |')
        
        break
         
def Msg_error_Nacionalidad(Nacionalidad,verificacion_1,verificacion_2):

    while not (len(Nacionalidad) >= 5 and verificacion_1) or verificacion_2:

        print                                                                                                   ( '        │              ╠══════════════════════════════════════════════╣             │') 
        print                                                                                                   ( '        │              ║ EL FORMATO ES INVALIDO O EL CAMPO ESTA VACIO ║             |')
        
        break
    
def Msg_error_Ciudad(ciudad,verificacion_1,verificacion_2):
    
    while not (len(ciudad) >= 5 and verificacion_1) or verificacion_2:
        
        print                                                                                                   ( '        │              ╠══════════════════════════════════════════════╣             │') 
        print                                                                                                   ( '        │              ║ EL FORMATO ES INVALIDO O EL CAMPO ESTA VACIO ║             |')
        
        break
            
def Msg_error_Localidad(localidad,verificacion_1,verificacion_2):

    while not (len(localidad) >= 5 and verificacion_1) or verificacion_2:
        
        print                                                                                                   ( '        │              ╠══════════════════════════════════════════════╣             │') 
        print                                                                                                   ( '        │              ║ EL FORMATO ES INVALIDO O EL CAMPO ESTA VACIO ║             |')
        
        break

        
def Msg_error_Codigo(codigo_postal):
    
    while not len(codigo_postal) == 4 :
        
        print                                                                                                   ( '        │              ╠══════════════════════════════════════════════╣             │') 
        print                                                                                                   ( '        │              ║ EN EL CODIGO SE REQUIERE 4 DIGITOS NUMERICOS ║             |')
        
        break
    
def Msg_error_Genero(Genero):
    
    while not (Genero == 'M' or Genero == 'F' or Genero == 'O'):
        
        print                                                                                                   ( '        │              ╠══════════════════════════════════════════════╣             │') 
        print                                                                                                   ( '        │              ║   GENERO INVALIDO O EL CAMPO ESTA VACIO.     ║             |')
        
        break
    
"""

       MENSAJES DE ERROR PARA LOS EXCEPCIONES

"""

def Msg_error_nacimiento():
    
    print                                                                                                       ( '        │              ╠══════════════════════════════╩═══════════════╣             │') 
    print                                                                                                       ( '        │              ║  RESPUESTA INVALIDA SE ESPERA VALOR NUMERICO ║             |')

     
def Msg_error_try():
                           
    print                                                                                                       ( '        │              ╠══════════════════════════════════════════════╣             │') 
    print                                                                                                       ( '        │              ║  RESPUESTA INVALIDA SE ESPERA VALOR NUMERICO ║             |')
    

"""

       MENSAJES DE ERROR PARA LOS DATOS LABORALES

"""

def Msg_error_Trabajo(trabajo):

    while trabajo != 'SI' and trabajo != 'NO':

        print                                                                                                   ( '        │              ╠══════════════════════════════════════════════╣             │') 
        print                                                                                                   ( '        │              ║  RESPUESTA INVALIDA O EL CAMPO ESTA VACIO.   ║             |')
        
        break
        
def Msg_error_nombre_Empresa(nombre_empresa,verificacion_1,verificacion_2):
    
    while not (len(nombre_empresa) > 5 and verificacion_1) or verificacion_2:
        
        print                                                                                                   ( '        │              ╠══════════════════════════════════════════════╣             │') 
        print                                                                                                   ( '        │              ║  RESPUESTA INVALIDA O EL CAMPO ESTA VACIO.   ║             |')
        
        break
    
def Msg_error_cuit_empresa(cuit_empresa,verificacion_1,verificacion_2):
    
    while not (len(cuit_empresa) == 15 and verificacion_1 ) and verificacion_2:
        
        print                                                                                                   ( '        │              ╠══════════════════════════════════════════════╣             │') 
        print                                                                                                   ( '        │              ║  RESPUESTA INVALIDA O EL CAMPO ESTA VACIO.   ║             |')

        break
    
def Msg_error_Jornada_laboral(Jornada_laboral):

    while not (Jornada_laboral == 'C' or Jornada_laboral == 'M' or Jornada_laboral == 'F' ) or Jornada_laboral == '':
        
        print                                                                                                   ( '        │              ╠══════════════════════════════════════════════╣             │') 
        print                                                                                                   ( '        │              ║  RESPUESTA INVALIDA O EL CAMPO ESTA VACIO.   ║             |')
        
        break

def Msg_error_sector(sector,verificacion_1,verificacion_2):
    
    while not (len (sector) > 5 and verificacion_1) and verificacion_2:
    
        print                                                                                                   ( '        │              ╠══════════════════════════════════════════════╣             │') 
        print                                                                                                   ( '        │              ║  RESPUESTA INVALIDA O EL CAMPO ESTA VACIO.   ║             |')

        break
    
"""

        MENSAJES DE ERRORES PARA LOS DATOS ACADEMICOS

"""

def Msg_error_estudio(estudio):

    while not (estudio == 'SI' or estudio == 'NO'):

        print                                                                                                   ( '        │              ╠══════════════════════════════════════════════╣             │') 
        print                                                                                                   ( '        │              ║  RESPUESTA INVALIDA O EL CAMPO ESTA VACIO.   ║             |')

        break
    
def Msg_error_nombre_institucion(nombre_institucion,verificacion_1):
    
    while not (len(nombre_institucion) > 5 and verificacion_1):
        
        print                                                                                                   ( '        │              ╠══════════════════════════════════════════════╣             │') 
        print                                                                                                   ( '        │              ║  RESPUESTA INVALIDA O EL CAMPO ESTA VACIO.   ║             |')

        break


def Msg_error_Nivel_estudio(grado_academico):
    
    while not (grado_academico == 'S' or grado_academico == 'T' or grado_academico == 'F' or grado_academico == 'P'):
        
        print                                                                                                   ( '        │              ╠══════════════════════════════════════════════╣             │') 
        print                                                                                                   ( '        │              ║  RESPUESTA INVALIDA O EL CAMPO ESTA VACIO.   ║             |')

        break
    
"""

    ERROR DEL RESETEO DEL FORMULARIO

"""

def Msg_error_reseteo(resetear):
    
    while not (resetear == 'L' or resetear == 'S'):
        
        print                                                                                                   ( '        │              ╠══════════════════════════════════════════════╣             │') 
        print                                                                                                   ( '        │              ║  RESPUESTA INVALIDA O EL CAMPO ESTA VACIO.   ║             |')

        break
