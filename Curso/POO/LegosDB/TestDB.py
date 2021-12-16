import psycopg2
#Conexion con la base de datos
conn = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='Legos'
)

#Se valida conectividad a la base
print(conn)
#Un cursor permite ejecutar sentencias SQL en postgres. Objeto tipo cursor
cursor = conn.cursor()
query = 'SELECT * FROM Legos'
#Ejecuta la setencia SELECT con cursor.execute
cursor.execute(query)
#fetchall permite recuperar todos los registros de la sentencia que se esta ejecutando
registros = cursor.fetchall()
print(registros)

#Se debe cerrar el cursor y la conexión de la db
cursor.close()
conn.close()
