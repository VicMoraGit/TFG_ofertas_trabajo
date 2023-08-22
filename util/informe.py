from sql.daoImpl.puestoDaoImpl import PuestoDao
import matplotlib.pyplot as plt


class Informe:

    def __init__(self) -> None:
        self._puestoDao = PuestoDao()

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
