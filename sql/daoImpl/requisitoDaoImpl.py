from logging import Logger, getLogger
from interfaces.dao.requisitoDaoInterface import RequisitoDaoInterface
from models.dto.requisitoDto import Requisito
from sql.conexion import conexion_sql


class RequisitoDao(RequisitoDaoInterface):
    def __init__(self):
        super().__init__()
        self._log: Logger = getLogger(__class__.__name__)

    def getRequisitosInformeRP(self):

        # Devuelve los requisitos mas populares
        with conexion_sql() as con:
            cursor = con.cursor()
            cursor.execute(
                f"""SELECT  r.Nombre, COUNT(r.Nombre) FROM tfg.requisito r 
                    INNER JOIN tfg.requisitos_oferta ro ON r.ID=ro.id_requisito 
                    INNER JOIN tfg.oferta o ON o.ID = ro.id_oferta 
                    WHERE r.Categoria  != "Soft Skill"
                    GROUP BY r.Nombre ORDER BY COUNT(r.Nombre) DESC LIMIT 10;
                    """)

            requisitosRaw = cursor.fetchall()

            requisitos = {}
            for requisito in requisitosRaw:
                requisitos[str(requisito[0]).replace(
                    " ", "\n")] = int(str(requisito[1]))

            return dict(sorted(requisitos.items(), key=lambda item: item[1], reverse=True))

    def obtener_por_nombre(self, nombre: str):
        requisito = None

        with conexion_sql() as con:
            cursor = con.cursor()
            cursor.execute(f"SELECT * FROM requisito WHERE Nombre={nombre};")

            requisitoRaw = cursor.fetchone()

            if requisitoRaw is None:
                self._log.debug("No hay ningun requisito con ese nombre")
            else:
                id_requisito = int(str(requisitoRaw[0]))
                descripcion = str(requisitoRaw[2])
                enlace = str(requisitoRaw[3])
                categoria = str(requisitoRaw[4])
                subcategoria = str(requisitoRaw[5])

                requisito = Requisito(
                    id_requisito, nombre, descripcion, enlace, categoria, subcategoria
                )
                self._log.debug(str(requisito))

        return requisito

    def obtener(self, idRequisito: int) -> None | Requisito:
        requisito = None

        with conexion_sql() as con:
            cursor = con.cursor()
            cursor.execute(f"SELECT * FROM requisito WHERE ID={idRequisito};")

            requisitoRaw = cursor.fetchone()

            if requisitoRaw is None:
                self._log.debug("No hay ningun requisito con ese ID")
            else:
                nombre = str(requisitoRaw[1])
                descripcion = str(requisitoRaw[2])
                enlace = str(requisitoRaw[3])
                categoria = str(requisitoRaw[4])
                subcategoria = str(requisitoRaw[5])

                requisito = Requisito(
                    idRequisito, nombre, descripcion, enlace, categoria, subcategoria
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
                            Subcategoria='{requisito.subcategoria}'
                            WHERE ID={requisito.id};"""
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
            cursor.execute(f"DELETE FROM requisito WHERE ID={idRequisito};")

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
                f"""INSERT INTO requisito (Nombre, Descripcion, Enlace_referencia, Categoria, Subcategoria) VALUES (
                '{requisito.nombre}',
                '{requisito.descripcion}',
                '{requisito.enlace}',
                '{requisito.categoria}',
                '{requisito.subcategoria}');
                """
            )

            con.commit()

            if cursor.rowcount == 0:
                self._log.debug("No se ha podido crear el requisito")
                return False
            else:
                self._log.debug("Requisito creado")

                return True
