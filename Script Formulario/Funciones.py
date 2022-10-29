import json

def limpiar_consola():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')        


def guardar_datos(Datos_ingresados):
    
    with open('Datos_Registrados.json','a',encoding='utf8') as file:
        for recorrer in Datos_ingresados:
            json.dump(recorrer,file,indent=4,default=str,ensure_ascii=False)


def Nombre_error_msg(nombre):

    while not (nombre.isalpha() and len(nombre) > 4) or nombre == '':

        print( '       └────────────────────────────────────┴────────────────────────┘')
        print()
        print( '       ┌─────────────────────────────────────────────────────────────┐')
        print( '       │  ERROR,SE INGRESO UN NOMBRE INVALIDO O EL CAMPO ES VACIO.   │')
        input( '       └─────────────────────────────────────────────────────────────┘')
        break

def Apellido_error_msg(apellido):
    
    while not (apellido.isalpha() and len(apellido) > 4 ) or apellido == '':
        
        print( '       └────────────────────────────────────┴────────────────────────┘')
        print()
        print( '       ┌─────────────────────────────────────────────────────────────┐')
        print( '       │ ERROR,SE INGRESO UN APELLIDO INVALIDO O EL CAMPO ES VACIO.  │')
        input( '       └─────────────────────────────────────────────────────────────┘')
        break

def Jefe_error_msg(Jefe):
    
    while Jefe != 'si' or Jefe != 'no' and Jefe == '':

        print( '       └────────────────────────────────────┴────────────────────────┘')
        print()
        print( '       ┌─────────────────────────────────────────────────────────────┐')
        print( '       │ ERROR,SE INGRESO UNA RESPUESTA INVALIDA O EL CAMPO ES VACIO │')
        input( '       └─────────────────────────────────────────────────────────────┘')
        
        limpiar_consola()
        
        break
        
def Estado_error_msg(estado):
    
    while estado != 'C' or estado != 'S' or estado != 'D' or estado != 'V' and estado == '':
        
        print( '       └────────────────────────────────────┴────────────────────────┘')
        print()
        print( '       ┌─────────────────────────────────────────────────────────────┐')
        print( '       │ ERROR,SE INGRESO UNA RESPUESTA INVALIDA O EL CAMPO ES VACIO │')
        input( '       └─────────────────────────────────────────────────────────────┘')
        
        limpiar_consola()
        
        break

def Nacionalidad_error_msg(Nacionalidad):

    while not (Nacionalidad.isalpha() and len(Nacionalidad) >= 5 and Nacionalidad == ''):

        print( '       └────────────────────────────────────┴────────────────────────┘')
        print()
        print( '       ┌─────────────────────────────────────────────────────────────┐')
        print( '       │ ERROR, SE DETECTO UNA NACIONALIDAD INVALIDA O CAMPO VACIO.  │')
        input( '       └─────────────────────────────────────────────────────────────┘')
        
        limpiar_consola()
        
        break

def Genero_error_msg(Genero):
    
    while Genero != 'F' or Genero != 'M' or Genero != 'O' and Genero == '':
        
        print( '       └────────────────────────────────────┴────────────────────────┘')
        print()
        print( '       ┌─────────────────────────────────────────────────────────────┐')
        print( '       │  ERROR, SE DETECTO UNA RESPUESTA INVALIDA O CAMPO VACIO.    │')
        input( '       └─────────────────────────────────────────────────────────────┘')
        
        limpiar_consola()
        
        break
    

def Trabajo_error_msg(trabajo):

    while not (trabajo == 'si' or trabajo == 'no') and trabajo == '':

        print( '       └────────────────────────────────────┴────────────────────────┘')
        print()
        print( '       ┌─────────────────────────────────────────────────────────────┐')
        print( '       │  ERROR, SE DETECTO UNA RESPUESTA INVALIDA O CAMPO VACIO.    │')
        input( '       └─────────────────────────────────────────────────────────────┘')
        
        limpiar_consola()
        
        break

def Empresa_error_msg(nombre_empresa):
    
    while not (nombre_empresa.isacci() and len(nombre_empresa) > 5):
        
        print( '       └────────────────────────────────────┴────────────────────────┘')
        print()
        print( '       ┌─────────────────────────────────────────────────────────────┐')
        print( '       │   ERROR, SE DETECTO UN NOMBRE INVALIDO O CAMPO VACIO.       │')
        input( '       └─────────────────────────────────────────────────────────────┘')      
        
        limpiar_consola()
        
        break

def Jornada_error_msg(Jornada_laboral):

    while Jornada_laboral != 'JC' or Jornada_laboral != 'MJ' or Jornada_laboral != 'F' and Jornada_laboral == '':
        
        print( '       └────────────────────────────────────┴────────────────────────┘')
        print()
        print( '       ┌─────────────────────────────────────────────────────────────┐')
        print( '       │    ERROR, SE DETECTO UNA RESPUESTA INVALIDA O VACIA.        │')
        input( '       └─────────────────────────────────────────────────────────────┘')      
        
        limpiar_consola()
        
        break

def Graduacion_error_msg(graduacion):

    while not (graduacion != 'si' or graduacion != 'no') and graduacion == '':

        print( '       └────────────────────────────────────┴────────────────────────┘')
        print()
        print( '       ┌─────────────────────────────────────────────────────────────┐')
        print( '       │  ERROR, SE DETECTO UNA RESPUESTA INVALIDA O CAMPO VACIO.    │')
        input( '       └─────────────────────────────────────────────────────────────┘')
        
        limpiar_consola()
        
        break

def Estudios_error_msg(estudia):
    
    while not (estudia != 'si' or estudia != 'no') and estudia == '':

        print( '       └────────────────────────────────────┴────────────────────────┘')
        print()
        print( '       ┌─────────────────────────────────────────────────────────────┐')
        print( '       │  ERROR, SE DETECTO UNA RESPUESTA INVALIDA O CAMPO VACIO.    │')
        input( '       └─────────────────────────────────────────────────────────────┘')
        
        limpiar_consola()
        
        break

def Academia_error_msg(academia_actual):
    
    while academia_actual != 'SAB' or academia_actual != 'ST' or academia_actual != 'T' or academia_actual != 'U':
        
        print( '       └────────────────────────────────────┴────────────────────────┘')
        print()
        print( '       ┌─────────────────────────────────────────────────────────────┐')
        print( '       │  ERROR, SE DETECTO UNA RESPUESTA INVALIDA O CAMPO VACIO.    │')
        input( '       └─────────────────────────────────────────────────────────────┘')
        
        limpiar_consola()
        
        break


def Nivel_graduacion_error_msg(nivel_graduacion):
    
    while nivel_graduacion  != 'SB' or nivel_graduacion   != 'ST' or nivel_graduacion   != 'TS' or nivel_graduacion   != 'U' or nivel_graduacion   != 'P' or nivel_graduacion  != 'M':
        
        print( '       └────────────────────────────────────┴────────────────────────┘')
        print()
        print( '       ┌─────────────────────────────────────────────────────────────┐')
        print( '       │  ERROR, SE DETECTO UNA RESPUESTA INVALIDA O CAMPO VACIO.    │')
        input( '       └─────────────────────────────────────────────────────────────┘')
        
        limpiar_consola()
        
        break

def Institucion_error_msg(nombre_institucion_graduado):
    
    while not (nombre_institucion_graduado.isascii() and len(nombre_institucion_graduado) > 5) :
        
        print( '       └────────────────────────────────────┴────────────────────────┘')
        print()
        print( '       ┌─────────────────────────────────────────────────────────────┐')
        print( '       │   ERROR, SE DETECTO UN NOMBRE INVALIDO O CAMPO VACIO.       │')
        input( '       └─────────────────────────────────────────────────────────────┘')      
        
        limpiar_consola()
        
        break




