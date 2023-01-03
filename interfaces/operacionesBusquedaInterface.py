from abc import ABC, abstractmethod

#Clases proyecto

from util.csvHandler import csvHandler


#Selenium
from selenium.webdriver.remote.webelement import WebElement
import undetected_chromedriver as uc


class OperacionesBusquedaInterface(ABC):

    def __init__(self, driver:uc.Chrome, n_paginas:int, csvHandler: csvHandler):
        self._driver:uc.Chrome = driver
        self._n_paginas = n_paginas
        self._csv = csvHandler;

    @abstractmethod
    def buscar(self, keyword:str):
        pass
    
    @abstractmethod
    def __buscar_keyword(self, keyword:str, n_pagina:int):
        pass

    @abstractmethod
    def __analizar_posiciones(self):
        pass

    @abstractmethod
    def __get_link(self, position:WebElement):
        pass

    @abstractmethod
    def __get_title(self, position:WebElement):
        pass

    @abstractmethod
    def __get_companyname(self, position:WebElement):
        pass  
    
    @abstractmethod
    def __get_experience(self, position:WebElement):
        pass

    @abstractmethod
    def __get_salaryexpected(self, position:WebElement):
        pass

    @abstractmethod
    def __get_location(self, position:WebElement):
        pass
    @abstractmethod
    def __get_skills(self, position:WebElement):
        pass