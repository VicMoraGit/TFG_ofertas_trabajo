import logging
from time import time

from util.csvHandler import csvHandler
import util.stats as stats

from portales.infojobs.infojobs import InfoJobs
from portales.indeed.indeed import Indeed
from portales.portal import Portal

if __name__ == "__main__":
    
    # Configuracion logger
    # logging.basicConfig(level=logging.INFO)
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger("main")
    log.setLevel(logging.DEBUG)

    # Clase encargada del csv
    csvh = csvHandler()
    # Declaracion variables
    portales:list[Portal] = []
    keywords = ["Big Data","Desarrollo Web","Backend","Microservicios"]
    n_paginas = 50
    
    # infoJobs:InfoJobs = InfoJobs(
    #     driver=driver,
    #     n_paginas=n_paginas,
    #     csvHandler=csvh)

    portales.append(Indeed(n_paginas=n_paginas,csvHandler=csvh))

    stats.s_inicio = time()
    for portal in portales:

        portal._iniciar_cronometro()
        
        for keyword in keywords:
                
            log.info(f"Buscando {keyword} en {portal.__class__.__name__}")
            portal.buscar(keyword)
        
        portal.actualizar_estadisticas()

    csvh.cerrar_archivo()
    stats.s_final = time()
    stats.imprime_stats()
    stats.exporta_stats()