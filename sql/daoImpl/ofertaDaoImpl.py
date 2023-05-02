from datetime import datetime
from logging import Logger, getLogger
from interfaces.dao.ofertaDaoInterface import OfertaDaoInterface
from models.ofertaDto import Oferta
from sql.conexion import conexion_sql

# TODO: Agregar operaciones de puestos, requisitos y ubicaciones a tablas auxiliares.


class OfertaDao(OfertaDaoInterface):
    def __init__(self):
        super().__init__()
        self._log: Logger = getLogger(__class__.__name__)

    def obtener(self, idOferta: int) -> None | Oferta:
        oferta = None

        with conexion_sql() as con:
            cursor = con.cursor()
            cursor.execute(f"SELECT * FROM oferta WHERE ID={idOferta}")

            ofertaRaw = cursor.fetchone()

            if ofertaRaw is None:
                self._log.debug("No hay ningun oferta con ese ID")
            else:
                titulo = str(ofertaRaw[1])
                companyia = str(ofertaRaw[2])
                experiencia = str(ofertaRaw[3])
                salario = int(str(ofertaRaw[4]))
                fecha_publicacion = datetime.strptime(str(ofertaRaw[5]), "%Y-%m-%d")
                puesto_id = int(str(ofertaRaw[6]))
                es_teletrabajo = bool(ofertaRaw[7])

                oferta = Oferta(
                    idOferta,
                    titulo,
                    companyia,
                    experiencia,
                    salario,
                    fecha_publicacion,
                    puesto_id,
                    es_teletrabajo,
                    [],
                    [],
                )
                self._log.debug(str(oferta))

        return oferta

    def actualizar(self, oferta: Oferta):
        with conexion_sql() as con:
            cursor = con.cursor()
            cursor.execute(
                f"""UPDATE ubicacion SET 
                            Titulo='{oferta.titulo}' 
                            Companyia='{oferta.companyia}' 
                            Experiencia='{oferta.experiencia}' 
                            Salario='{oferta.salario}'
                            Fecha_publicacion='{oferta.fecha_publicacion}' 
                            Puesto_id='{oferta.puesto}' 
                            Es_teletrabajo='{oferta.es_teletrabajo}' 
                            WHERE ID={oferta.id}"""
            )
            con.commit()

            if cursor.rowcount is 0:
                self._log.debug("No hay ningun oferta con ese ID")
                return False
            else:
                self._log.debug("Oferta actualizado")

                return True

    def borrar(self, idOferta: int):
        with conexion_sql() as con:
            cursor = con.cursor()
            cursor.execute(f"DELETE FROM oferta WHERE ID={idOferta}")

            con.commit()

            if cursor.rowcount is 0:
                self._log.debug("No hay ningun oferta con ese ID")
                return False
            else:
                self._log.debug("Oferta eliminado")

                return True

    def crear(self, oferta: Oferta):
        with conexion_sql() as con:
            cursor = con.cursor()
            cursor.execute(
                f"""INSERT INTO oferta VALUES (
                '{oferta.titulo}',
                '{oferta.companyia}',
                '{oferta.experiencia}', 
                '{oferta.salario}',
                '{oferta.fecha_publicacion}', 
                '{oferta.puesto}', 
                '{oferta.es_teletrabajo}', 
                """
            )

            con.commit()

            if cursor.rowcount is 0:
                self._log.debug("No se ha podido crear el oferta")
                return False
            else:
                self._log.debug("Oferta creado")

                return True
