"""
Este modulo trabaja con try y con fetch all para traer todos los registros.

"""
import psycopg2
#Conexion con la base de datos
conn = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='Legos')

try:
    with conn:
        #With cierra recurso de cursor, por lo que no es necesario llamar al metodo close()
        with conn.cursor() as curs:
            query = 'SELECT * FROM Legos'
            curs.execute(query)
            regs = curs.fetchall()
            print(regs)
#e guarda error
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conn.close()
