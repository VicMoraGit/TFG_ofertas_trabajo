from logging import Logger, getLogger
from interfaces.operacionesBusquedaInterface import OperacionesBusquedaInterface as obi
from time import sleep
#Selenium
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import undetected_chromedriver as uc

class InfoJobsPage(obi):

    def __init__(self, driver:uc.Chrome):
        self._base_url:str ="https://www.infojobs.net/"
        self._driver:uc.Chrome = driver
        self._log:Logger = getLogger("InfoJobs")
    
    
    def buscar(self, keyword:str):
        driver = self._driver

        # Abre la pagina de InfoJobs
        driver.get(self._base_url)
        self._log.info("Infojobs.net abierta")

        self.__buscar_keyword(keyword=keyword)
        
    def __buscar_keyword(self,keyword:str):
        driver = self._driver

        # Localizadores
        input_busqueda_locator = "palabra"
        boton_busqueda_locator = "searchOffers"
        
        # Espera hasta que el campo de busqueda este visible
        # y obtiene los elementos
        input_busqueda = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, input_busqueda_locator)))
        boton_busqueda = driver.find_element(By.ID, boton_busqueda_locator)
        
        # Inserta la palabra clave en el campo
        input_busqueda.clear()
        input_busqueda.send_keys(keyword)

        # Comprueba si el pop-up de las cookies permite clickar el boton
        self.__gestionar_cookies()

        # Click boton busqueda
        boton_busqueda.click()
        self._log.info("Buscando ofertas...")

    def __gestionar_cookies(self):
        driver = self._driver
        # Localizadores
        panel_cookies_locator = "cmpContainer"
        aceptar_cookies_boton_locator = '[data-testid="TcfAccept"]'

        try:    
            # Acepta las cookies
            driver.find_element(By.ID, panel_cookies_locator)
            driver.find_element(By.CSS_SELECTOR,aceptar_cookies_boton_locator).click()
            
            self._log.info("Cookies aceptadas")

        except:
            # No hay pop up de cookies
            self._log.info("No hay cookies")
        
        

    def __get_link(self, position:WebElement):
        pass

    def __get_title(self, position:WebElement):
        pass

    def __get_companyname(self, position:WebElement):
        pass  
    
    def __get_experience(self, position:WebElement):
        pass

    def __get_salaryexpected(self, position:WebElement):
        pass

    def __get_location(self, position:WebElement):
        pass