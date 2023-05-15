from contextlib import contextmanager
from logging import Logger, getLogger
import traceback
from mysql.connector import connect

log:Logger = getLogger("MySQL")

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
        log.warning(traceback.format_exc())
        conn.rollback()
        conn.close()
        