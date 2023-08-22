from logging import Logger, getLogger
from interfaces.dao.puestoDaoInterface import PuestoDaoInterface
from models.dto.puestoDto import Puesto
from sql.conexion import conexion_sql


class PuestoDao(PuestoDaoInterface):

    def __init__(self):
        super().__init__()
        self._log: Logger = getLogger(__class__.__name__)

    def getPuestosInformePPS(self):
        # Devuelve los puestos con salario que mas se repiten, junto al salario medio de esos puestos
        with conexion_sql() as con:
            cursor = con.cursor()
            cursor.execute(
                f"SELECT AVG(o.Salario), p.Nombre  FROM oferta o  INNER JOIN puesto p ON p.ID = o.Puesto_id WHERE o.Puesto_id!=99 GROUP BY o.Puesto_id ORDER BY COUNT(o.Salario) DESC LIMIT 10;")

            puestosRaw = cursor.fetchall()

            puestos = {}
            for puesto in puestosRaw:
                puestos[str(puesto[1]).replace(" ", "\n")] = round(
                    float(str(puesto[0])), 2)

            return dict(sorted(puestos.items(), key=lambda item: item[1], reverse=True))

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
