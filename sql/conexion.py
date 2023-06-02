from contextlib import contextmanager
from logging import Logger, getLogger
import traceback
from mysql.connector import connect
from sys import argv
log: Logger = getLogger("MySQL")


@contextmanager
def conexion_sql():

    if is_docker():
        host = 'host.docker.internal'
    else:
        host = "localhost"

    user = "tfgUser"
    pwd = "tfgUser"
    db = "tfg"

    conn = connect(host=host, user=user, password=pwd, database=db)

    try:
        yield conn
    except:
        log.warning(traceback.format_exc())
        conn.rollback()
        conn.close()


def is_docker():

    try:
        return argv[1] in ['-d', '--docker']

    except:
        return False
