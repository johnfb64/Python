"""
Este modulo trabaja con fetch one para traer solo de a un registro

"""
class ConsultaUnidad:

    import psycopg2 as db

    conn = db.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='Legos')
    try:
        cur = conn.cursor()
        sentencia = "INSERT INTO usuarios () VALUES(%s)"



    #e guarda error
    except Exception as e:
        print(f'Ocurrio un error: {e}')
    finally:
        conn.close()
