import csv
from sys import exit
from datetime import date
from os import getcwd, path
from logging import Logger, getLogger, DEBUG


class csvHandler:
    def __init__(self) -> None:
        self._log: Logger = getLogger(__class__.__name__)
        # self._log.setLevel(DEBUG)
        self._ruta = self.__obtener_ruta_archivo()
        self._archivo = self.__obtener_archivo()
        self._writer = self.__obtener_writer()

        self.__escribir_cabecera()

    def escribir_lineas(self, valores):
        self._writer.writerows(valores)
        self._log.debug("Lineas escritas en csv")

    def __obtener_ruta_archivo(self):
        # Devuelve ruta de un csv con la fecha de hoy en el nombre
        dateTimeObj = date.today()
        nombre_archivo = "Analisis_" + str(dateTimeObj) + ".csv"

        ruta = path.join(getcwd(), "data", "CSV", nombre_archivo)
        self._log.debug("Ruta creada")

        return ruta

    def __obtener_archivo(self):
        try:
            archivo = open(self._ruta, "w", encoding="UTF-8", newline="")
            self._log.debug("Archivo creado/abierto")
            return archivo
        except Exception as e:
            self._log.critical("Error al crear el archivo", exc_info=True)
            exit(str(e))

    def __obtener_writer(self):
        writer = csv.writer(self._archivo)
        self._log.debug("Writer devuelto")

        return writer

    def cerrar_archivo(self):
        self._archivo.close()
        self._log.debug("Archivo cerrado")

    def __escribir_cabecera(self):
        self._writer.writerow(
            [
                "Titulo",
                "Compañia",
                "Experiencia",
                "Salario",
                "Ubicacion",
                "Fecha",
                "Requisitos",
            ]
        )
        self._log.debug("Cabecera declarada")
