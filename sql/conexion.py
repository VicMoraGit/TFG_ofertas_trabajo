from contextlib import contextmanager
from mysql.connector import connect

@contextmanager
def conexion_sql():

    host="localhost"
    user="tfgUser"
    pwd="tfgUser"
    db="tfg"

    conn = connect(host=host, user=user, password=pwd, database=db)
    
    try:
        yield conn
    except:
        conn.close()
        