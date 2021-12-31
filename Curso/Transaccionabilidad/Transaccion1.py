
import psycopg2 as bd

conn = bd.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='Legos')
try:
    # conn.autocommit tiene un valor bolleano que permitira hacer el autocommit de los valores
    # que se deberan agregar a la base de datos.
    #Si se deja en False, no hara commit. y debera hacerse el commit manual (Linea 14)
    conn.autocommit = False
    curs = conn.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)'
    valores = ('John', 'Ballen', 'jhonn.ballen@gmail.com')
    curs.execute(sentencia,valores)
    print('Termina la transacción')
    #Commit manual
    conn.commit()
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conn.close()
