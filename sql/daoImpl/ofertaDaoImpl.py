from datetime import datetime
from logging import Logger, getLogger
from interfaces.dao.ofertaDaoInterface import OfertaDaoInterface
from models.ofertaDto import Oferta
from sql.conexion import conexion_sql
from sql.daoImpl.ubicacionDaoImpl import UbicacionDao

# TODO: Operaciones CRUD de tablas auxiliares
# [x] - Tabla requisitos_oferta
#   [x] - Insertar
#   [x] - Obtener
#   [x] - Eliminar
# [x] - Tabla ubicacion_oferta
#   [x] - Insertar
#   [x] - Obtener
#   [x] - Eliminar


class OfertaDao(OfertaDaoInterface):
    def __init__(self):
        super().__init__()
        self._log: Logger = getLogger(__class__.__name__)
        self.ubicacionDao = UbicacionDao()

    def obtener(self, idOferta: int) -> None | Oferta:
        oferta = None

        with conexion_sql() as con:
            cursor = con.cursor()
            cursor.execute(f"SELECT * FROM oferta WHERE ID={idOferta};")

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

                requisitos = []
                cursor.execute(f"SELECT * FROM requisitos_oferta WHERE ID={idOferta};")
                requisitosRaw = cursor.fetchall()

                if requisitosRaw is not None:
                    for requisito in requisitosRaw:
                        requisitos.append(requisito[1])

                ubicaciones = []
                cursor.execute(f"SELECT * FROM ubicaciones_oferta WHERE ID={idOferta};")
                ubicacionesRaw = cursor.fetchall()

                if ubicacionesRaw is not None:
                    for ubicacion in ubicacionesRaw:
                        ubicaciones.append(ubicacion[1])

                oferta = Oferta(
                    idOferta,
                    titulo,
                    companyia,
                    experiencia,
                    salario,
                    fecha_publicacion,
                    puesto_id,
                    es_teletrabajo,
                    ubicaciones,
                    requisitos,
                )
                self._log.debug(str(oferta))

        return oferta

    def borrar(self, idOferta: int):
        with conexion_sql() as con:
            cursor = con.cursor()

            cursor.execute(f"DELETE FROM requisitos_oferta WHERE id_oferta={idOferta};")
            cursor.execute(
                f"DELETE FROM ubicaciones_oferta WHERE id_oferta={idOferta};"
            )
            cursor.execute(f"DELETE FROM oferta WHERE ID={idOferta};")

            con.commit()

            if cursor.rowcount == 0:
                self._log.debug("No hay ninguna oferta con ese ID")
                return False
            else:
                self._log.debug("Oferta eliminada")

                return True

    def crear(self, oferta: Oferta):
        with conexion_sql() as con:
            cursor = con.cursor()
            cursor.execute(
                f"""INSERT INTO oferta (Titulo, Companyia, Experiencia, Salario, Fecha_publicacion, Puesto_id, Es_teletrabajo) VALUES (
                '{oferta.titulo}',
                '{oferta.companyia}',
                {oferta.experiencia}, 
                {oferta.salario},
                '{oferta.fecha_publicacion}',
                {oferta.puesto}, 
                {oferta.es_teletrabajo}
                );
                """
            )

            if cursor.rowcount == 0:
                self._log.debug("No se ha podido crear la oferta")
                return False
            else:
                cursor.execute(f"SELECT last_insert_id();")
                id_oferta = int(str(cursor.fetchone()[0]))

                for id_requisito in oferta.requisitos:
                    cursor.execute(
                        f"INSERT INTO requisitos_oferta (id_oferta, id_requisito) VALUES({id_oferta},{id_requisito});"
                    )

                for id_ubicacion in oferta.ubicaciones:
                    cursor.execute(
                        f"INSERT INTO ubicaciones_oferta (id_oferta, id_ubicacion) VALUES({id_oferta},{id_ubicacion});"
                    )

                con.commit()
                self._log.debug("Oferta creada")

                return True
