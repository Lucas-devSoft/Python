import mysql.connector

def conectar_BD(guardar):

    global conexion

    try : 

        conexion = mysql.connector.connect(

                                    host='localhost',
                                    port= 3306,
                                    user='root',
                                    password='',
                                    db='calculadora_history'

                                )
        
        if guardar == 'S' :
        
            if conexion.is_connected():

                estado  = 'Conectado'
                cursor  = conexion.cursor()
                info_BD = cursor.execute('SELECT database();')
                info_BD = cursor.fetchone()
                info_server = conexion.get_server_info()

                print                                       ( '├─────────────────┬─────────────────────────────┬───────────────────────────┤')
                print                                       ( '│     Estado      │        Base de Datos        |          Server           │')
                print                                       ( '├─────────────────┼─────────────────────────────┼───────────────────────────┤')
                print                                       (f'│   {estado}     │   {info_BD}  |   {info_server}   │')
                print                                       ( '├─────────────────┴─────────────────────────────┴───────────────────────────┤')
                
        elif guardar == 'N':
            
            estado      = 'Desconectado'
            info_BD     = 'N/A'
            info_server = 'N/A'

            print                                           ( '├─────────────────┬─────────────────────────────┬───────────────────────────┤')
            print                                           ( '│     Estado      │        Base de Datos        |          Server           │')
            print                                           ( '├─────────────────┼─────────────────────────────┼───────────────────────────┤')
            print                                           (f'│   {estado}  │              {info_BD}            |           {info_server}             │')
            print                                           ( '├─────────────┴───────────────────────────────────┴─────────────────────────┤')
            
        
    except: 

        estado      = 'Sin Conexion'
        info_BD     = 'N/A'
        info_server = 'N/A'

        print                                               ( '├─────────────────┬─────────────────────────────┬───────────────────────────┤')
        print                                               ( '│     Estado      │        Base de Datos        |          Server           │')
        print                                               ( '├─────────────────┼─────────────────────────────┼───────────────────────────┤')
        print                                               (f'│   {estado}  │              {info_BD}            |           {info_server}             │')
        print                                               ( '├─────────────────┴─────────────────────────────┴───────────────────────────┤')
    
def guardado_datos(nombre,opcion,Operaciones,numero1,numero2,resultado):
    
    try:
        
        if conexion.is_connected():

            if numero2 == 0:
                
                datos = conexion.cursor()
                sentencia2 = f"INSERT INTO historial (Nombre,Opcion,Valor_1,Operaciones,Resultados) VALUES ('{nombre}','{opcion}','{numero1}','{Operaciones}','{resultado}')" 
                datos.execute(sentencia2)
                conexion.commit()
                
            else:
                
                datos = conexion.cursor()
                #sentencia1 = "Truncate historial" Resetea el auntoincremento del ID, pero borra todos los datos de la tabla.
                sentencia1 = f"INSERT INTO historial (Nombre,Opcion,Valor_1,Operaciones,Valor_2,Resultados) VALUES ('{nombre}','{opcion}','{numero1}','{Operaciones}','{numero2}','{resultado}')"
                #datos.execute(sentencia1) 
                datos.execute(sentencia1)
                conexion.commit()

            conexion.close()
            datos.close()
    
        
    except NameError:
        
        print ('│      Las operaciones no se guardaran sin conexion a la Base de Datos      |')
        
def error_guardado(guardar):
    
    while guardar != 'S' and guardar != 'N':
        
        print (' La Opcion esperada es < S >  o < N > ')
        input ('  Para continuar sin guardar sus operaciones  ')
        break