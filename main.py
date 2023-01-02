import undetected_chromedriver as uc
import logging
from time import time

from util.csvHandler import csvHandler
from portales.infojobs.infojobs import InfoJobsPage
from portales.indeed.indeed import IndeedPage

if __name__ == "__main__":
    
    # Configuracion logger
    # logging.basicConfig(level=logging.INFO)
    logging.basicConfig(level=logging.INFO)
    
    log = logging.getLogger("main")
    log.setLevel(logging.DEBUG)

    # Clase encargada del csv
    csvh = csvHandler()
    # Declaracion variables
    keywords = ["Desarrollador web"]
    n_paginas = 1

    driver:uc.Chrome = uc.Chrome()
    log.debug("Navegador nuevo abierto")

    infoJobs:InfoJobsPage = InfoJobsPage(
        driver=driver,
        n_paginas=n_paginas,
        csvHandler=csvh)

    indeed:IndeedPage = IndeedPage(
        driver=driver,
        n_paginas=n_paginas,
        csvHandler=csvh)
    start = time()
    for keyword in keywords:
        log.info(f"Buscando {keyword} en InfoJobs")
        #infoJobs.buscar(keyword)
        log.info(f"Buscando {keyword} en Indeed")
        indeed.buscar(keyword)
             
    csvh.cerrar_archivo()
    log.info('Tiempo para recoger los datos: {} mins'.format(round((time() - start) / 60, 2)))