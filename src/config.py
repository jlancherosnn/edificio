from psycopg2 import connect
 
HOST = 'ec2-54-91-223-99.compute-1.amazonaws.com'
PUERTO = 5432
BD = 'd311rpe8t08qup'
USUARIO = 'hwxgtdgazsitel'
PASS = 'd5cda6a82d6a8f9f86490fb7e6437dbc165ca32115ec6827df619ab52258b042'

def EstablecerConexion():
    try:
        conexion = connect(host=HOST, port=PUERTO, dbname=BD,user=USUARIO, password=PASS)
    except ConnectionError:
        print("Error de conexión")
    return conexion
