import logging
from time import time

from util.csvHandler import csvHandler
import util.stats as stats
from portales.infojobs.infojobs import InfoJobs
from portales.indeed.indeed import Indeed

if __name__ == "__main__":
    
    # Configuracion logger
    # logging.basicConfig(level=logging.INFO)
    logging.basicConfig(level=logging.INFO)
    
    log = logging.getLogger("main")
    log.setLevel(logging.DEBUG)

    # Clase encargada del csv
    csvh = csvHandler()
    # Declaracion variables
    keywords = ["Big Data"]
    n_paginas = 30
    
    # infoJobs:InfoJobs = InfoJobs(
    #     driver=driver,
    #     n_paginas=n_paginas,
    #     csvHandler=csvh)

    indeed:Indeed = Indeed(
        n_paginas=n_paginas,
        csvHandler=csvh)

    stats.s_inicio = time()

    for keyword in keywords:

        #log.info(f"Buscando {keyword} en InfoJobs")
        #infoJobs.buscar(keyword)

        log.info(f"Buscando {keyword} en Indeed")
        indeed.buscar(keyword)
        

    csvh.cerrar_archivo()
    stats.s_final = time()
    stats.imprime_stats()
    stats.exporta_stats()