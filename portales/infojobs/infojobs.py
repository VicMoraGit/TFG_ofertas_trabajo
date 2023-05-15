# Modulos python
from logging import Logger, getLogger, DEBUG
from os import path
import re
from time import sleep, time

# from util.constantes import ALL_SKILLS

# Clases proyecto
# from util.csvHandler import csvHandler
# from portales.portal import Portal
# import util.stats as stats

# Selenium
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver

"""
class InfoJobs(Portal):

    def __init__(self, n_paginas:int, csvHandler: csvHandler):
        super().__init__(n_paginas,csvHandler)
        
        self._base_url:str ="https://www.infojobs.net/"
        self._log:Logger = getLogger(__class__.__name__)
        # self._log.setLevel(DEBUG)
        self._driver = WebDriver("chromedriver.exe")

    def buscar(self, keyword:str):
        driver = self._driver

        # Comienza a contar
        s_inicio = time()

        # Abre la pagina de InfoJobs
        driver.delete_all_cookies()
        driver.get(self._base_url)
        self._log.info("Infojobs.net abierta")
        
        for i in range(1, self._n_paginas_total+1):
            
            try:

                self._buscar_keyword(keyword=keyword, n_pagina=i)
                self._scroll_fin_pagina()
                self._analizar_posiciones()
            
            except (TimeoutException,NoSuchElementException):
                
                self._ruta_captura_captcha = path.join("data","capturasError","error"+__class__.__name__+".png")
                self._driver.save_screenshot(self._ruta_captura_captcha)

                self._es_bloqueado = True     
                self._log.error("Captcha en pantalla, busqueda en InfoJobs interrumpida")

                break
            
        # Calcula el tiempo final
        s_final = time()
        self._t_total = round((s_final - s_inicio) / 60, 2)

        # Se actualizan las estadisticas con los datos del portal
        stats.n_ofertas_analizadas += self._n_ofertas_analizadas
        stats.n_ofertas_con_salario += self._n_ofertas_con_salario
        stats.n_ofertas_con_experiencia += self._n_ofertas_con_experiencia
        stats.datos_portales.append(self.asdict())

    def _buscar_keyword(self,keyword:str, n_pagina:int):
        
        ruta_busqueda = "jobsearch/search-results/list.xhtml"
        parametro_keyword="keyword=" + keyword
        parametro_pagina="page=" + str(n_pagina)
        
        driver = self._driver
        driver.get(f"{self._base_url}{ruta_busqueda}?{parametro_pagina}&{parametro_keyword}")
        
        # Espera que cargue la pagina
        sleep(5)

        # Comprueba si hay cookies
        self._gestionar_cookies()


    def _gestionar_cookies(self):
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

    def _scroll_fin_pagina(self):
        
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

      
    def _analizar_posiciones(self):

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
            link_posicion = self._get_link(posicion)
            
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
            titulo=self._get_title(resumen_oferta)
            ubicacion=self._get_location(resumen_oferta)
            compañia=self._get_companyname(resumen_oferta)
            experiencia=self._get_experience(resumen_oferta)
            salario=self._get_salaryexpected(resumen_oferta)
            skills=self._get_skills(descripcion)
            self._log.debug("Informacion extraida.")

            # Rellena el diccionario
            informacion_posicion['titulo']=titulo
            informacion_posicion['compañia']=compañia
            informacion_posicion['experiencia']=experiencia
            informacion_posicion['salario']=salario
            informacion_posicion['ubicacion']=ubicacion
            informacion_posicion['skills']=skills
            
            # Escribe en csv
            self._csv.escribir_linea(valores=informacion_posicion.values())
            self._log.debug("Informacion escrita en csv")

            # Actualiza estadisticas
            self._n_ofertas_analizadas+=1
            if salario != "Sin informacion":
                self._n_ofertas_con_salario+=1
            if experiencia != "Sin informacion":
                self._n_ofertas_con_experiencia+=1

            self._log.debug("Estadisticas actualizadas")

            driverAux.close()
            self._log.debug("Driver auxiliar cerrado")
            self._log.info(f"Oferta analizada {i+1}/{len(posiciones)}")

        # Actualiza estadisticas
        self._n_paginas_analizadas += 1

    def _get_link(self, position:WebElement):

        link_posicion_locator = "h2.ij-OfferCardContent-description-title > a"    
        return position.find_element(By.CSS_SELECTOR, link_posicion_locator).get_attribute("href")

    def _get_title(self, position:WebElement):
        
        titulo_posicion_locator = "prefijoPuesto"
        return position.find_element(By.ID, titulo_posicion_locator).text
 

    def _get_companyname(self, position:WebElement):
        
        compañia_locator = '.link[data-track="Company Detail Clicked"]'
        nombre_compañia_raw = position.find_element(By.CSS_SELECTOR, compañia_locator).get_attribute("title")  
        nombre_compañia_limpio = nombre_compañia_raw.replace("Ofertas de trabajo en ","").replace(" ofertas de empleo profesionales","")

        return nombre_compañia_limpio

    
    def _get_experience(self, position:WebElement):
        
        descripcion_resumen_locator = 'div.inner + div '
        descripcion = position.find_element(By.CSS_SELECTOR, descripcion_resumen_locator).text
        
        try:
            p = re.compile("no requerida|(\d+\s*(años|año|(años de experiencia))(?!.*(mercado|sector)))")
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

    def _get_salaryexpected(self, position:WebElement):
        
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

    def _get_location(self, position:WebElement):
        
        poblacion_posicion_locator = 'prefijoPoblacion'
        provincia_posicon_locator = 'prefijoProvincia'
        
        poblacion = position.find_element(By.ID, poblacion_posicion_locator).text
        provincia = position.find_element(By.ID, provincia_posicon_locator).text

        return poblacion+provincia
    
    def _get_skills(self, position:WebElement):

        skills_oferta = []
        descripcion_texto = position.text

        # Se compara si alguna skill esta presente en la descripcion de la oferta
                
        for skill in ALL_SKILLS:
            p = re.compile(rf"\b{re.escape(skill.lower())}\b")
            s = p.search(descripcion_texto.lower())
            if s is not None:
                skills_oferta.append(skill)
        
        return skills_oferta

    def asdict(self):

        dict_super =  super().asdict()
        dict_super["nombre"] = __class__.__name__
        
        if self._es_bloqueado:
            dict_super["ruta_captura_error"] = self._ruta_captura_captcha;
        
        return dict_super

"""
driver = WebDriver("chromedriver.exe")

driver.get("https://developer.infojobs.net/test-console/execute.xhtml")


for i in range(1, 21):
    input_url = driver.find_element(By.ID, "apiuri")
    boton_enviar = driver.find_element(By.ID, "send-button")

    input_url.clear()
    input_url.send_keys(
        "https://api.infojobs.net/api/7/offer?q=Big%20Data&page=" + str(i)
    )
    boton_enviar.click()