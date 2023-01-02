import csv;
from sys import exit
from datetime import date
from os import getcwd, path
from logging import Logger, getLogger, DEBUG

class csvHandler:
    def __init__(self) -> None:

        self._log:Logger = getLogger("csv") 
        # self._log.setLevel(DEBUG)       
        self._ruta = self.__obtener_ruta_archivo()
        self._archivo = self.__obtener_archivo()
        self._writer = self.__obtener_writer()

        self.__escribir_cabecera()

    
    def escribir_linea(self, valores):
        self._writer.writerow(valores)
        self._log.debug("Linea escrita en csv")

    def __obtener_ruta_archivo(self):

        # Devuelve ruta de un csv con la fecha de hoy en el nombre
        dateTimeObj = date.today()
        nombre_archivo = "Analisis_"+str(dateTimeObj)+".csv"

        ruta = path.join(getcwd(),nombre_archivo)
        self._log.debug("Ruta creada")
        
        return ruta

    def __obtener_archivo(self):
        
        try:
            archivo =  open(self._ruta, 'w', encoding="UTF-8", newline="")
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
        self.escribir_linea(['Titulo', 'Compañia', 'Experiencia', 'Salario', 'Ubicacion'])
        self._log.debug("Cabecera declarada")

