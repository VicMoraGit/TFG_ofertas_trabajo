from abc import abstractmethod

#Selenium
from selenium.webdriver.remote.webelement import WebElement

class OperacionesBusquedaInterface():
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