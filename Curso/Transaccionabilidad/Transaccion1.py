
import psycopg2 as bd

conn = bd.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='Legos')
try:
    with conn:
        with conn.cursor() as curs:
            #Si el valor se deja en True, el commit hacia la base se hara automaticamente.
            conn.autocommit = False
            curs = conn.cursor()
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)'
            valores = ('Cosme', 'Fulanito', 'joselito@gmail.com')
            curs.execute(sentencia, valores)

            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Pepe', 'Pelaez', 'pepepepa@rebelde.com', 11)
            curs.execute(sentencia, valores)

            #Esta linea permite el commit para hacer el push hacia la base de datos.
            #conn.commit() //Se gestiona automatico con el with.


except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conn.close()
#Se movio esta linea hasta el final, por que la transacción se ejecuta hasta el final.
print('Termina la transacción, se hizo commit')
