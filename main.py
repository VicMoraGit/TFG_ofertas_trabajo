import undetected_chromedriver as uc
import logging
from portales.infojobs.infojobs import InfoJobsPage

if __name__ == "__main__":
    
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger()

    keywords = ["Big Data"]
    n_paginas = 10

    driver:uc.Chrome = uc.Chrome()
    log.info("Navegador nuevo abierto")

    infoJobs:InfoJobsPage = InfoJobsPage(driver=driver)

    for keyword in keywords:
        infoJobs.buscar(keyword)
        pass