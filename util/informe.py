from sql.daoImpl.puestoDaoImpl import PuestoDao
import matplotlib.pyplot as plt
from sql.daoImpl.requisitoDaoImpl import RequisitoDao

from sql.daoImpl.ubicacionDaoImpl import UbicacionDao


class Informe:

    def __init__(self) -> None:
        self._puestoDao = PuestoDao()
        self._ubicacionDao = UbicacionDao()
        self._requisitoDao = RequisitoDao()

    def getInformePPS(self):  # Posiciones Populares ordenadas por salario
        puestos = self._puestoDao.getPuestosInformePPS()
        x = list(range(1, 11))
        height_bars = list(puestos.values())
        labels = list(puestos.keys())

        plt.figure(figsize=(30, 10))
        p = plt.bar(x, height=height_bars, tick_label=labels,
                    width=0.7, color="lightskyblue")
        plt.xlabel("Puestos")
        plt.ylabel("Salario medio")
        plt.title("Puestos mas populares ordenados por salario medio")
        plt.bar_label(p, height_bars)

        plt.show()

    def getInformeUPT(self):  # Ubicaciones populares con datos sobre teletrabajo
        ubicaciones = self._ubicacionDao.getUbicacionesInformeUPT()
        x = list(range(1, 11))
        is_teletrabajo = [ubicacion["Ofertas Teletrabajo"]
                          for ubicacion in ubicaciones]
        not_teletrabajo = [ubicacion["Ofertas totales"] - ubicacion["Ofertas Teletrabajo"]
                           for ubicacion in ubicaciones]
        porcentajes = [ubicacion["Porcentaje teletrabajo"]
                       for ubicacion in ubicaciones]
        provincias_x = [ubicacion["Provincia"] for ubicacion in ubicaciones]

        plt.figure(figsize=(30, 10))
        p1 = plt.bar(x, height=is_teletrabajo,
                     width=0.7, bottom=not_teletrabajo)
        p2 = plt.bar(x, height=not_teletrabajo, tick_label=provincias_x,
                     width=0.7)
        plt.xlabel("Provincias")
        plt.ylabel("Ofertas")
        plt.title("Porcentaje de ofertas con teletrabajo por provincias")
        plt.bar_label(p1, porcentajes)
        plt.legend((p1[0], p2[0]), ('Teletrabajo', 'Presencial'))

        plt.show()

    def getInformeRP(self):  # Requisitos mas populares

        requisitos = self._requisitoDao.getRequisitosInformeRP()
        x = list(range(1, 11))
        height_bars = list(requisitos.values())
        labels = list(requisitos.keys())

        plt.figure(figsize=(30, 10))
        p = plt.bar(x, height=height_bars, tick_label=labels,
                    width=0.7, color="lightskyblue")
        plt.xlabel("Requisitos")
        plt.ylabel("Ofertas que lo requieren")
        plt.title("Requisitos mas demandados")
        plt.bar_label(p, height_bars)

        plt.show()
