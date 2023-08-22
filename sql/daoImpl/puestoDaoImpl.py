from logging import Logger, getLogger
from interfaces.dao.puestoDaoInterface import PuestoDaoInterface
from models.dto.puestoDto import Puesto
from sql.conexion import conexion_sql


class PuestoDao(PuestoDaoInterface):

    def __init__(self):
        super().__init__()
        self._log: Logger = getLogger(__class__.__name__)

    def obtener(self, idPuesto: int) -> None | Puesto:

        puesto = None

        with conexion_sql() as con:

            cursor = con.cursor()
            cursor.execute(f"SELECT * FROM puesto WHERE ID={idPuesto};")

            puestoRaw = cursor.fetchone()

            if puestoRaw is None:
                self._log.debug("No hay ningun puesto con ese ID")
            else:
                nombre = str(puestoRaw[1])
                puesto = Puesto(idPuesto, nombre)
                self._log.debug(str(puesto))

        return puesto

    def actualizar(self, puesto: Puesto):

        with conexion_sql() as con:

            cursor = con.cursor()
            cursor.execute(
                f"UPDATE puesto SET Nombre='{puesto.nombre}' WHERE ID={puesto.id};")

            con.commit()

            if cursor.rowcount == 0:
                self._log.debug("No hay ningun puesto con ese ID")
                return False
            else:
                self._log.debug("Puesto actualizado")

                return True

    def borrar(self, idPuesto: int):

        with conexion_sql() as con:

            cursor = con.cursor()
            cursor.execute(f"DELETE FROM puesto WHERE ID={idPuesto};")

            con.commit()

            if cursor.rowcount == 0:
                self._log.debug("No hay ningun puesto con ese ID")
                return False
            else:
                self._log.debug("Puesto eliminado")

                return True

    def crear(self, puesto: Puesto):

        with conexion_sql() as con:

            cursor = con.cursor()
            cursor.execute(
                f"INSERT INTO puesto (Nombre) VALUES ('{puesto.nombre}');")

            con.commit()

            if cursor.rowcount == 0:
                self._log.debug("No se ha podido crear el puesto")
                return False
            else:
                self._log.debug("Puesto creado")

                return True
