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
from selenium.common.exceptions import TimeoutException, NoSuchElementException

import undetected_chromedriver as uc

class InfoJobsPage(obi):

    def __init__(self, driver:uc.Chrome, n_paginas:int, csvHandler: csvHandler):
        self._base_url:str ="https://www.infojobs.net/"
        self._driver:uc.Chrome = driver
        self._log:Logger = getLogger("InfoJobs")
        # self._log.setLevel(DEBUG)
        self._n_paginas = n_paginas
        self._csv = csvHandler;
    
    def buscar(self, keyword:str):
        driver = self._driver

        # Abre la pagina de InfoJobs
        driver.delete_all_cookies()
        driver.get(self._base_url)
        self._log.info("Infojobs.net abierta")
        
        for i in range(1, self._n_paginas+1):
            try:
                self.__buscar_keyword(keyword=keyword, n_pagina=i)
                self.__scroll_fin_pagina()
                self.__analizar_posiciones()
            except (TimeoutException,NoSuchElementException):
                self._log.error("Captcha en pantalla, busqueda en InfoJobs interrumpida")
                return

    def __buscar_keyword(self,keyword:str, n_pagina:int):
        
        ruta_busqueda = "jobsearch/search-results/list.xhtml"
        parametro_keyword="keyword=" + keyword
        parametro_pagina="page=" + str(n_pagina)
        
        driver = self._driver
        driver.get(f"{self._base_url}{ruta_busqueda}?{parametro_pagina}&{parametro_keyword}")
        
        # Espera que cargue la pagina
        sleep(5)

        # Comprueba si hay cookies
        self.__gestionar_cookies()


    def __gestionar_cookies(self):
        driver = self._driver
        
        # Localizadores
        aceptar_cookies_boton_locator = '[data-testid="TcfAccept"]'

        try:    
            # Acepta las cookies
            driver.find_element(By.CSS_SELECTOR,aceptar_cookies_boton_locator).click()
            sleep(1)
            self._log.debug("Cookies aceptadas")

        except:

            # No hay pop up de cookies
            self._log.debug("No hay cookies")

    def __scroll_fin_pagina(self):
        
        driver = self._driver

        # Scripts JavaScript
        altura_viewport_script = "return visualViewport.height;"
        posicion_inferior_script = "return document.body.getBoundingClientRect().bottom;"
        scroll_script = "window.scrollTo(0, arguments[0]);"

        # Declaracion variables
        altura_scroll = 0
        altura_vp = driver.execute_script(altura_viewport_script)
        
        posicion_inferior_anterior = 0
        posicion_inferior_actual  = driver.execute_script(posicion_inferior_script) 
        
        # Scroll hacia abajo hasta el final de la pagina
        while posicion_inferior_anterior != posicion_inferior_actual:

            self._log.debug("Deslizando")
            #Hace scroll
            altura_scroll += altura_vp
            driver.execute_script(scroll_script, altura_scroll)
            
            # Se espera 1 seg a que las posiciones se rendericen en el DOM
            sleep(1)

            # Obtiene el final de la pagina y comprueba si es igual que la
            # ultima iteracion
            posicion_inferior_anterior = posicion_inferior_actual
            posicion_inferior_actual  = driver.execute_script(posicion_inferior_script) 

      
    def __analizar_posiciones(self):

        driver = self._driver
        
        # Localizadores 
        posiciones_locator = "div.ij-ContentSearch-list > ul div.sui-AtomCard-link"
        resumen_posicion_locator = ".panel-canvas.panel-rounded"
        descripcion_posicion_locator = "prefijoDescripcion1"

        # Obtiene las posiciones de esa pagina
        posiciones = driver.find_elements(By.CSS_SELECTOR, posiciones_locator)
        self._log.info(f"Analizando {len(posiciones)} ofertas.")

        # Abre cada posicion y extrae la informacion
        for i,posicion in enumerate(posiciones):
            
            #Carga la oferta en un nuevo driver
            link_posicion = self.__get_link(posicion)
            
            driverAux = uc.Chrome()    
            driverAux.get(link_posicion)
            self._log.debug("Oferta abierta")

            #Espera a que aparezca el elemento que resume la oferta
            resumen_oferta = WebDriverWait(driver=driverAux,timeout=10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,resumen_posicion_locator)))
            self._log.debug("Resumen de la oferta visible")
            descripcion = driver.find_element(By.ID,descripcion_posicion_locator)

            # Extrae la informacion
            informacion_posicion={}
            titulo=self.__get_title(resumen_oferta)
            ubicacion=self.__get_location(resumen_oferta)
            compañia=self.__get_companyname(resumen_oferta)
            experiencia=self.__get_experience(resumen_oferta)
            salario=self.__get_salaryexpected(resumen_oferta)
            skills=self.__get_skills(descripcion)
            self._log.debug("Informacion extraida.")

            # Rellena el diccionario
            informacion_posicion['titulo']=titulo
            informacion_posicion['compañia']=compañia
            informacion_posicion['experiencia']=experiencia
            informacion_posicion['salario']=salario
            informacion_posicion['ubicacion']=ubicacion
            informacion_posicion['skills']=skills
            
            self._csv.escribir_linea(valores=informacion_posicion.values())
            self._log.debug("Informacion escrita en csv")

            driverAux.close()
            self._log.debug("Driver auxiliar cerrado")
            self._log.info(f"Oferta analizada {i+1}/{len(posiciones)}")


    def __get_link(self, position:WebElement):

        link_posicion_locator = "h2.ij-OfferCardContent-description-title > a"    
        return position.find_element(By.CSS_SELECTOR, link_posicion_locator).get_attribute("href")

    def __get_title(self, position:WebElement):
        
        titulo_posicion_locator = "prefijoPuesto"
        return position.find_element(By.ID, titulo_posicion_locator).text
 

    def __get_companyname(self, position:WebElement):
        
        compañia_locator = '.link[data-track="Company Detail Clicked"]'
        nombre_compañia_raw = position.find_element(By.CSS_SELECTOR, compañia_locator).get_attribute("title")  
        nombre_compañia_limpio = nombre_compañia_raw.replace("Ofertas de trabajo en ","").replace(" ofertas de empleo profesionales","")

        return nombre_compañia_limpio

    
    def __get_experience(self, position:WebElement):
        
        descripcion_resumen_locator = 'div.inner + div '
        descripcion = position.find_element(By.CSS_SELECTOR, descripcion_resumen_locator).text
        
        try:
            p = re.compile("no requerida|(\d+\s*((experiencia)|(de \3)|(años \4)|años|año))")
            s = p.search(descripcion)

            if s is not None:
                experience = s.group()
                if s == "no requerida":
                    self._log.debug("No requiere experiencia")
                else: 
                    self._log.debug("Si requiere experiencia")    
                return experience

        except:
            self._log.debug("No tiene informacion sobre experiencia")          
        
        return "Sin informacion"

    def __get_salaryexpected(self, position:WebElement):
        
        descripcion_resumen_locator = 'div.inner +div '
        descripcion = position.find_element(By.CSS_SELECTOR, descripcion_resumen_locator).text
        
        try:
            p = re.compile("\d.+€")
            
            s = p.search(descripcion)

            if s is not None:
                self._log.debug("Hay informacion sobre el salario")    
                salario = s.group()
                return salario

        except:
            self._log.debug("No tiene informacion sobre salario")
            
        
        return "Sin informacion"

    def __get_location(self, position:WebElement):
        
        poblacion_posicion_locator = 'prefijoPoblacion'
        provincia_posicon_locator = 'prefijoProvincia'
        
        poblacion = position.find_element(By.ID, poblacion_posicion_locator).text
        provincia = position.find_element(By.ID, provincia_posicon_locator).text

        return poblacion+provincia
    
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