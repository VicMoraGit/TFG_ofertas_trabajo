from logging import Logger, getLogger
from interfaces.dao.requisitoDaoInterface import RequisitoDaoInterface
from models.requisitoDto import Requisito
from sql.conexion import conexion_sql


class RequisitoDao(RequisitoDaoInterface):
    def __init__(self):
        super().__init__()
        self._log: Logger = getLogger(__class__.__name__)

    def obtener_por_nombre(self, nombre: str):
        requisito = None

        with conexion_sql() as con:
            cursor = con.cursor()
            cursor.execute(f"SELECT * FROM requisito WHERE Nombre={nombre}")

            requisitoRaw = cursor.fetchone()

            if requisitoRaw is None:
                self._log.debug("No hay ningun requisito con ese nombre")
            else:
                id_requisito = int(str(requisitoRaw[0]))
                descripcion = str(requisitoRaw[2])
                enlace = str(requisitoRaw[3])
                categoria = str(requisitoRaw[4])

                requisito = Requisito(
                    id_requisito, nombre, descripcion, enlace, categoria
                )
                self._log.debug(str(requisito))

        return requisito

    def obtener(self, idRequisito: int) -> None | Requisito:
        requisito = None

        with conexion_sql() as con:
            cursor = con.cursor()
            cursor.execute(f"SELECT * FROM requisito WHERE ID={idRequisito}")

            requisitoRaw = cursor.fetchone()

            if requisitoRaw is None:
                self._log.debug("No hay ningun requisito con ese ID")
            else:
                nombre = str(requisitoRaw[1])
                descripcion = str(requisitoRaw[2])
                enlace = str(requisitoRaw[3])
                categoria = str(requisitoRaw[4])

                requisito = Requisito(
                    idRequisito, nombre, descripcion, enlace, categoria
                )
                self._log.debug(str(requisito))

        return requisito

    def actualizar(self, requisito: Requisito):
        with conexion_sql() as con:
            cursor = con.cursor()
            cursor.execute(
                f"""UPDATE ubicacion SET 
                            Nombre='{requisito.nombre}' 
                            Descripcion='{requisito.descripcion}' 
                            Enlace_referencia='{requisito.enlace}' 
                            Categoria='{requisito.categoria}'
                            WHERE ID={requisito.id}"""
            )

            con.commit()

            if cursor.rowcount == 0:
                self._log.debug("No hay ningun requisito con ese ID")
                return False
            else:
                self._log.debug("Requisito actualizado")

                return True

    def borrar(self, idRequisito: int):
        with conexion_sql() as con:
            cursor = con.cursor()
            cursor.execute(f"DELETE FROM requisito WHERE ID={idRequisito}")

            con.commit()

            if cursor.rowcount == 0:
                self._log.debug("No hay ningun requisito con ese ID")
                return False
            else:
                self._log.debug("Requisito eliminado")

                return True

    def crear(self, requisito: Requisito):
        with conexion_sql() as con:
            cursor = con.cursor()
            cursor.execute(
                f"""INSERT INTO requisito VALUES (
                '{requisito.nombre}',
                '{requisito.descripcion}',
                '{requisito.enlace}',
                '{requisito.categoria}')
                """
            )

            con.commit()

            if cursor.rowcount == 0:
                self._log.debug("No se ha podido crear el requisito")
                return False
            else:
                self._log.debug("Requisito creado")

                return True
