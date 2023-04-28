from abc import ABC, abstractmethod

#Selenium
from selenium.webdriver.remote.webelement import WebElement

class OperacionesBusquedaInterface(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def buscar(self, keyword:str):
        pass
    
    @abstractmethod
    def _buscar_keyword(self, keyword:str, n_pagina:int):
        pass

    @abstractmethod
    def _analizar_posiciones(self):
        pass

    @abstractmethod
    def _get_link(self, position:WebElement):
        pass

    @abstractmethod
    def _get_title(self, position:WebElement):
        pass

    @abstractmethod
    def _get_companyname(self, position:WebElement):
        pass  
    
    @abstractmethod
    def _get_experience(self, position:WebElement):
        pass

    @abstractmethod
    def _get_salaryexpected(self, position:WebElement):
        pass

    @abstractmethod
    def _get_location(self, position:WebElement):
        pass
    @abstractmethod
    def _get_skills(self, position:WebElement):
        pass