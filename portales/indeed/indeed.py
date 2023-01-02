#Modulos python
from logging import Logger, getLogger, DEBUG
import re
from time import sleep
from util.constantes import ALL_SKILLS

#Clases proyecto
from interfaces.operacionesBusquedaInterface import OperacionesBusquedaInterface as obi
from util.csvHandler import csvHandler

#Selenium
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import undetected_chromedriver as uc

class IndeedPage(obi):

    def __init__(self, driver:uc.Chrome, n_paginas:int, csvHandler: csvHandler):
        self._base_url:str ="https://es.indeed.com/"
        self._driver:uc.Chrome = driver
        self._log:Logger = getLogger("Indeed")
        # self._log.setLevel(DEBUG)
        self._n_paginas = n_paginas
        self._csv = csvHandler;

    def buscar(self, keyword:str):
        driver = self._driver

        # Abre la pagina de Indeed
        driver.delete_all_cookies()
        driver.get(self._base_url)
        self._log.info("Indeed.com abierta")
        
        for i in range(1, self._n_paginas+1):
            self.__buscar_keyword(keyword=keyword, n_pagina=i)
            self.__analizar_posiciones()

    def __buscar_keyword(self,keyword:str, n_pagina:int):
        
        ruta_busqueda = "jobs"
        parametro_keyword="q=" + keyword
        parametro_pagina="start=" +str(n_pagina) +"0"
        
        driver = self._driver
        driver.get(f"{self._base_url}{ruta_busqueda}?{parametro_pagina}&{parametro_keyword}")
        
        # Espera que cargue la pagina
        sleep(5)     
    
    def __analizar_posiciones(self):
        
        driver = self._driver

        # Localizadores 
        posiciones_locator = '#mosaic-provider-jobcards > ul > li'
        descripcion_oferta_locator = 'jobDescriptionText'
        
        # Guarda el id de la pestaña de resultados
        ch = driver.current_window_handle

        # Obtiene las posiciones de esa pagina
        posiciones = driver.find_elements(By.CSS_SELECTOR,posiciones_locator)
        self._log.info(f"Analizando {len(posiciones)} ofertas.")
        
        # Abre cada posicion y extrae la informacion
        for i,posicion in enumerate(posiciones):

            # Extrae la informacion
            informacion_posicion={}
            titulo=self.__get_title(posicion)
            ubicacion=self.__get_location(posicion)
            compañia=self.__get_companyname(posicion)
            link_posicion = self.__get_link(posicion)
            
            # Si el link esta vacio, pasa a la siguiente posicion.
            # Si no, abre la oferta en una nueva pestaña y extrae el salario y la experiencia
            if link_posicion == "":
                continue
            driver.tab_new(link_posicion)           
            driver.switch_to.window(driver.window_handles[1])
            self._log.debug("Oferta abierta")

            #Espera a que la descripcion de la oferta aparezca
            descripcion = WebDriverWait(driver=driver,timeout=10).until(
                EC.presence_of_element_located((By.ID,descripcion_oferta_locator)))
            self._log.debug("Resumen de la oferta visible")
            
            #Extrae mas informacion
            experiencia=self.__get_experience(descripcion)
            salario=self.__get_salaryexpected(descripcion)
            skills=self.__get_skills(descripcion)
            self._log.debug("Informacion extraida.")
            
            # Rellena el diccionario
            if not titulo=="":
                informacion_posicion['titulo']=titulo
                informacion_posicion['compañia']=compañia
                informacion_posicion['experiencia']=experiencia
                informacion_posicion['salario']=salario
                informacion_posicion['ubicacion']=ubicacion
                informacion_posicion['skills']=skills

                #Write to csv file
                self._csv.escribir_linea(valores=informacion_posicion.values())
                self._log.debug("Informacion escrita en csv")

            #Cierra la oferta y devuelve el control a la pestaña de resultados                
            driver.close()
            driver.switch_to.window(ch)
            self._log.debug("Pestaña cerrada")
            self._log.info(f"Oferta analizada {i+1}/{len(posiciones)}")

    
    
    def __get_link(self, position:WebElement):

        try:
            link= position.find_element(By.CSS_SELECTOR,'.jobTitle > a').get_attribute("href")
        except:
            link=""
        return link

    def __get_title(self, position:WebElement):
        
        try:
            title=position.find_element(By.CSS_SELECTOR,'.jobTitle').text
        except:
            title=""

        return title


    def __get_companyname(self, position:WebElement):
        
        try:
            company=position.find_element(By.CSS_SELECTOR,'.companyName').text
        
        except:
            company=""
        return company 

    def __get_experience(self, position:WebElement):
        
        try:
            # Filtra la experiencia de la descripcion
            re_general = re.compile("(experiencia.* )*\d+.*((experiencia)|(de \3)|(años \4))")
            
            # Filtra solo los años 
            re_años = re.compile("\d+ (años)")
            
            s = re_general.search(position.text)
            if s is not None:
                s2 =re_años.search(s.group())
                if s2 is not None:
                    experience = s2.group()
                    self._log.debug("Si requiere experiencia")    

                    return experience
        except:
            self._log.debug("No tiene informacion sobre experiencia")

        return "Sin informacion"

    def __get_salaryexpected(self, position:WebElement):
        
        try:
            p = re.compile("(\d|\.|\,){3,}.+€")
            s = p.search(position.text)
            if s is not None:
                salary = s.group()
                self._log.debug("Hay informacion sobre el salario")    
                return salary
        except:
            self._log.debug("No tiene informacion sobre salario")

        return "Sin informacion"


    def __get_location(self, position:WebElement):
        
        try:
            location=position.find_element(By.CSS_SELECTOR,'.companyLocation').text
            
        except:
            location=""
        return location

    def __get_skills(self, position:WebElement):

        skills_oferta = []
        descripcion_texto = position.text

        # Se compara si alguna skill esta presente en la descripcion de la oferta
                
        for skill in ALL_SKILLS:
            p = re.compile(rf"\b{re.escape(skill.lower())}\b")
            s = p.search(descripcion_texto.lower())
            if s is not None:
                skills_oferta.append(skill)
        
        return skills_oferta