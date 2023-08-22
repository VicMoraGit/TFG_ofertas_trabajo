import logging
import traceback
from time import time

from pyvirtualdisplay.display import Display

from util.csvHandler import csvHandler
import util.stats as stats
from util.gui.menu import Menu

from portales.indeed.indeed import Indeed
from portales.monster.monster import Monster
from portales.tecnoempleo.tecnoempleo import Tecnoempleo

from portales.portal import Portal


def quitScript(menu: Menu):

    menu.showExitMenu()
    exit()


def showMenu(menu: Menu):

    menu.showMenu()
    match menu.resultado:
        case 1:
            pass
        case 2:
            menu.showInformesMenu()
            match menu.informe:

                case 1:
                    pass

                case 2:
                    pass

                case 3:
                    pass

                case 4:
                    pass

                case _:
                    quitScript(menu)

            quitScript(menu)

        case _:
            quitScript(menu)


if __name__ == "__main__":
    # Configuracion logger
    # logging.basicConfig(level=logging.INFO)

    menu = Menu()
    showMenu(menu)

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger("main")
    log.setLevel(logging.DEBUG)

    # Clase encargada del csv
    csvh = csvHandler()
    # Declaracion variables
    portales: list[Portal] = []
    keywords = ["DevOps",  "Programador", "Desarrollador", "Analista", "Frontend", "Inteligencia artificial", "Backend",
                "Fullstack", "Ciencia de datos", "Ciberseguridad", "IoT", "Redes", "Bases de datos", "Mineria de Datos", "Robotica", "Desarrollo de videojuegos"
                ]
    n_paginas = 100

    with Display() as disp:

        portales.append(Monster(n_paginas=n_paginas, csvHandler=csvh))
        portales.append(Tecnoempleo(n_paginas=n_paginas, csvHandler=csvh))
        portales.append(Indeed(n_paginas=n_paginas,
                        csvHandler=csvh, dominio_pais="es"))
        # portales.append(Indeed(n_paginas=n_paginas, csvHandler=csvh, dominio_pais="uk"))
        # portales.append(Indeed(n_paginas=n_paginas,csvHandler=csvh,dominio_pais="fr"))

        stats.s_inicio = time()

        for portal in portales:
            portal._iniciar_cronometro()

            for keyword in keywords:
                try:
                    log.info(
                        f"Buscando {keyword} en {portal.__class__.__name__}")
                    portal.buscar(keyword)
                except:
                    log.info(traceback.format_exc())
                    continue
                finally:
                    portal.close()

            portal.actualizar_estadisticas()

        csvh.cerrar_archivo()
        stats.s_final = time()
        stats.imprime_stats()
        stats.exporta_stats()
