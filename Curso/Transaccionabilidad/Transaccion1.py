
import psycopg2 as bd

conn = bd.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='Legos')
try:
    #Si el valor se deja en True, el commit hacia la base se hara automaticamente.
    conn.autocommit = True
    curs = conn.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)'
    valores = ('Andres', 'Ballen', 'andres.ballen038@gmail.com')
    curs.execute(sentencia,valores)
    print('Termina la transacción')
    # conn.commit()
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conn.close()
