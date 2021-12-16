"""
Este modulo inserta de a un registro.

"""
import psycopg2
#Conexion con la base de datos
conn = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='Legos')
try:
    with conn:
        #With cierra recurso de cursor, por lo que no es necesario llamar al metodo close()
        with conn.cursor() as curs:
            #Los campos y valores se almacenan por parte para luego trabajarlos con el cursor
            insertar = 'INSERT INTO Legos (id, Franquicia, Codigo, Producto, Cantidad, precio, ubicacion)' \
                       'VALUES(%s, %s, %s, %s, %s, %s, %s) '
            valores = ((11, 'DC', 'WM880', 'Jocker_1', '50', 10000, 'Caja 16'),)
            curs.executemany(insertar,valores)
            registros_insertados = curs.rowcount
            print(f'Registros afectados: {registros_insertados}')
           #Commit guarda cambios en la base de datos


#e guarda error
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conn.close()