import undetected_chromedriver as uc
import logging

from util.csvHandler import csvHandler
from portales.infojobs.infojobs import InfoJobsPage

if __name__ == "__main__":
    
    # Configuracion logger
    # logging.basicConfig(level=logging.INFO)
    logging.basicConfig()
    log = logging.getLogger("main")
    log.setLevel(logging.DEBUG)

    # Clase encargada del csv
    csvh = csvHandler()
    # Declaracion variables
    keywords = ["Big Data"]
    n_paginas = 1

    driver:uc.Chrome = uc.Chrome()
    log.debug("Navegador nuevo abierto")

    infoJobs:InfoJobsPage = InfoJobsPage(
        driver=driver,
        n_paginas=n_paginas,
        csvHandler=csvh)

    for keyword in keywords:
        
        log.info(f"Buscando {keyword} en InfoJobs")
        infoJobs.buscar(keyword)
             
    csvh.cerrar_archivo()