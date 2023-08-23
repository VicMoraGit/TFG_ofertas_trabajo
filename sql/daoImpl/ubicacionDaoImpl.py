from logging import Logger, getLogger
import traceback

from interfaces.dao.ubicacionDaoInterface import UbicacionDaoInterface
from models.dto.ubicacionDto import Ubicacion
from sql.conexion import conexion_sql


class UbicacionDao(UbicacionDaoInterface):
    def __init__(self):
        super().__init__()
        self._log: Logger = getLogger(__class__.__name__)

    def getUbicacionesInformeUPT(self):
        #Devuelve informacion sobre las ubicaciones de las ofertas y el teletrabajo en ellas
        with conexion_sql() as con:
            cursor = con.cursor()
            cursor.execute(
                f"""SELECT COUNT(o.Titulo), u.Provincia, 
                    COUNT(CASE WHEN o.Es_teletrabajo=TRUE THEN 1 END)
                    FROM tfg.oferta o 
                    INNER JOIN tfg.ubicaciones_oferta uo ON uo.id_oferta = o.ID
                    INNER JOIN tfg.ubicacion u ON uo.id_ubicacion = u.ID WHERE u.Provincia != 'Teletrabajo' 
                    GROUP BY u.Provincia ORDER BY COUNT(o.Titulo) DESC LIMIT 10;
                """)

            ubicacionesRaw = cursor.fetchall()
            ubicaciones = []
            for ubicacion in ubicacionesRaw:
                ubicaciones.append(
                    {
                        "Provincia": ubicacion[1],
                        "Ofertas totales": ubicacion[0],
                        "Ofertas Teletrabajo": ubicacion[2],
                        "Porcentaje teletrabajo": str(
                            round(
                                int(str(ubicacion[2]))
                                * 100/int(str(ubicacion[0])), 2)
                        ) + "%"
                    }
                )

            return sorted(ubicaciones, key=lambda item: item["Ofertas totales"], reverse=True)

    def obtener(self, idUbicacion: int):
        ubicacion = None

        with conexion_sql() as con:
            cursor = con.cursor()
            cursor.execute(
                f"SELECT * FROM ubicacion WHERE ID={idUbicacion};",
            )

            ubicacionRaw = cursor.fetchone()

            if ubicacionRaw is None:
                self._log.debug("No hay ninguna ubicacion con ese ID")
            else:
                provincia = str(ubicacionRaw[1])
                comunidad = str(ubicacionRaw[2])
                ubicacion = Ubicacion(idUbicacion, provincia, comunidad)
                self._log.debug(str(ubicacion))

        return ubicacion

    def actualizar(self, ubicacion: Ubicacion):
        with conexion_sql() as con:
            cursor = con.cursor()
            cursor.execute(
                f"""UPDATE ubicacion SET 
                            Provincia='{ubicacion.provincia}',
                            Comunidad='{ubicacion.comunidad}' 
                            WHERE ID={ubicacion.id};"""
            )

            con.commit()

            if cursor.rowcount == 0:
                self._log.debug("No hay ningun ubicacion con ese ID")
                return False
            else:
                self._log.debug("Ubicacion actualizado")

                return True

    def borrar(self, idUbicacion: int):
        with conexion_sql() as con:
            cursor = con.cursor()
            cursor.execute(
                f"DELETE FROM ubicacion WHERE ID={idUbicacion};",
            )

            con.commit()

            if cursor.rowcount == 0:
                self._log.debug("No hay ningun ubicacion con ese ID")
                return False
            else:
                self._log.debug("Ubicacion actualizado")

                return True

    def crear(self, ubicacion: Ubicacion):
        try:
            with conexion_sql() as con:
                cursor = con.cursor()

                cursor.execute(
                    f"INSERT INTO ubicacion (Provincia, Comunidad) VALUES('{ubicacion.provincia}','{ubicacion.comunidad}');")
                con.commit()
                if cursor.rowcount == 0:
                    self._log.debug("No se ha podido crear la ubicacion")
                    return False
                else:
                    self._log.debug("Ubicacion actualizado")

                    return True
        except:
            self._log.error(traceback.format_exc())
