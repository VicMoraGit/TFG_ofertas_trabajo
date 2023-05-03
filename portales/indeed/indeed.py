# Modulos python
from logging import Logger, getLogger, DEBUG
from time import sleep
from traceback import format_exc

# Clases proyecto
from portales.portal import Portal
from sql.daoImpl.puestoDaoImpl import PuestoDao
from util.azure_translator import Traductor
from util.csvHandler import csvHandler
import util.stats as stats
from exceptions.DescripcionNoEmbebida import DescripcionNoEmbebida

# Selenium
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class Indeed(Portal):
    def __init__(self, n_paginas: int, csvHandler: csvHandler, dominio_pais="es"):
        super().__init__(n_paginas, csvHandler)
        self.dominio_pais = dominio_pais
        self._base_url: str = f"https://{dominio_pais}.indeed.com/"
        self._log: Logger = getLogger(__class__.__name__)
        self._titulo_ultima_oferta_pagina = ""
        self._busqueda_finalizada = False
        self.puestoDao = PuestoDao()
        # self._log.setLevel(DEBUG)

    def buscar(self, keyword: str):
        # Reseteo de variables en cada busqueda
        self._busqueda_finalizada = False
        self._n_paginas_analizadas = 0

        while not self._busqueda_finalizada:
            for i in range(self._n_paginas_analizadas, self._n_paginas_total):
                # Para cada pagina un driver nuevo
                super().abrir_nav()
                self._driver.get(self._base_url)
                self._log.info(f"Indeed.com {self.dominio_pais.upper()} abierta")

                try:
                    self._buscar_keyword(keyword=keyword, n_pagina=i)
                    self._analizar_posiciones()
                    self._driver.quit()

                    if self._busqueda_finalizada:
                        break

                except (DescripcionNoEmbebida, WebDriverException):
                    self._log.error(format_exc())
                    self._driver.quit()
                    break

                if i == self._n_paginas_total - 1:
                    self._busqueda_finalizada = True

    def actualizar_estadisticas(self):
        super().actualizar_estadisticas()
        stats.datos_portales.append(self.asdict())

    def _buscar_keyword(self, keyword: str, n_pagina: int):
        ruta_busqueda = "jobs"
        parametro_keyword = "q=" + keyword
        parametro_pagina = "start=" + str(n_pagina) + "0"

        driver = self._driver
        driver.get(
            f"{self._base_url}{ruta_busqueda}?{parametro_pagina}&{parametro_keyword}"
        )
        self._log.info(f"Analizando pagina {str(n_pagina+1)}")

        # Localizadores
        posiciones_locator = "#mosaic-provider-jobcards > ul > li div.cardOutline"

        # Espera que carguen las posiciones
        WebDriverWait(driver=driver, timeout=10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, posiciones_locator))
        )

    def _scroll_al_elemento(self, posicion):
        driver = self._driver
        driver.execute_script("arguments[0].scrollIntoView(true);", posicion)

    def _analizar_posiciones(self):
        driver = self._driver
        valores_posiciones = []

        n_ofertas_analizadas = 0
        n_ofertas_con_salario = 0
        n_ofertas_con_experiencia = 0
        titulo = ""

        # Localizadores
        posiciones_locator = "#mosaic-provider-jobcards > ul > li div.cardOutline"
        descripcion_oferta_locator = "div.jobsearch-JobComponent"

        # Presiona ESC ya que a veces aparece un pop up de inicio de sesion que para el script
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)

        # Obtiene las posiciones de esa pagina
        posiciones = driver.find_elements(By.CSS_SELECTOR, posiciones_locator)
        self._log.info(f"Analizando ofertas.")

        # Abre cada posicion y extrae la informacion
        for i, posicion in enumerate(posiciones):
            # Se mueve al elemento y espera a que cargue su descripcion para sacar la info
            self._scroll_al_elemento(posicion)
            sleep(0.5)
            posicion.click()

            if len(driver.window_handles) > 1:
                raise DescripcionNoEmbebida("Descripcion no embebida")

            # Si despues de dos segundos no ha encontrado la descripcion, ha saltado un captcha
            descripcion = WebDriverWait(driver=driver, timeout=10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, descripcion_oferta_locator)
                )
            )

            # Extrae la informacion de la oferta visible
            informacion_posicion = {}
            titulo = self._get_title(posicion)
            ubicacion = self._get_location(posicion)
            compañia = self._get_companyname(posicion)
            fecha = self._get_publish_date(posicion)
            experiencia = self._get_experience(descripcion)
            salario = self._get_salaryexpected(descripcion)
            skills = self._get_skills(descripcion)

            self._log.debug("Informacion extraida.")

            # Rellena el diccionario
            if not titulo == "":
                informacion_posicion["titulo"] = titulo
                informacion_posicion["compañia"] = compañia
                informacion_posicion["experiencia"] = experiencia
                informacion_posicion["salario"] = salario
                informacion_posicion["ubicacion"] = ubicacion
                informacion_posicion["fecha"] = fecha
                informacion_posicion["skills"] = skills

                # Escribe en csv
                valores_posiciones.append(informacion_posicion.values())

                # Actualiza estadisticas
                n_ofertas_analizadas += 1
                if salario != "Sin informacion":
                    n_ofertas_con_salario += 1
                if experiencia != "Sin informacion":
                    n_ofertas_con_experiencia += 1

                self._log.debug("Estadisticas actualizadas")

            self._log.debug(f"Oferta analizada {i+1}/{len(posiciones)}")

        # Comprueba si esta es la ultima pagina de la palabra clave.
        # Si es la ultima, finaliza la busqueda y no añade las ultimas
        # posiciones ni estadisticas.

        if titulo == self._titulo_ultima_oferta_pagina:
            self._busqueda_finalizada = True
            return
        else:
            self._titulo_ultima_oferta_pagina = titulo

        self._log.info(f"{len(posiciones)} ofertas analizadas.")

        # Escribe todas las ofertas en el csv
        self._csv.escribir_lineas(valores=valores_posiciones)
        self._log.debug("Informacion escrita en el CSV")

        # Actualiza estadisticas
        self._n_ofertas_analizadas += n_ofertas_analizadas
        self._n_ofertas_con_salario += n_ofertas_con_salario
        self._n_ofertas_con_experiencia += n_ofertas_con_experiencia
        self._n_paginas_analizadas += 1

    def _get_title(self, position: WebElement):
        td = Traductor()

        try:
            title = position.find_element(By.CSS_SELECTOR, ".jobTitle").text
            dominio_idioma = td.detectar_idioma(title)

            if dominio_idioma != "es":
                title = td.traducir(dominio_idioma, "es", title)

            indice_puesto = self._filtro.filtrar_posicion(title)
            print("Titulo oferta ", title)
            title = self.puestoDao.obtener(indice_puesto)
            print(title)

        except:
            self._log.error(format_exc())
            title = ""

        return title

    def _get_companyname(self, position: WebElement):
        try:
            company = position.find_element(By.CSS_SELECTOR, ".companyName").text

        except:
            company = ""
        return company

    def _get_experience(self, position: WebElement):
        return self._filtro.filtrar_experiencia(position.text)

    def _get_salaryexpected(self, position: WebElement):
        return self._filtro.filtrar_salario(position.text)

    def _get_location(self, position: WebElement):
        posicion = position.find_element(By.CSS_SELECTOR, ".companyLocation")
        try:
            location = self._filtro.filtrar_localizacion(posicion.text)

        except:
            location = ""
        return location

    def _get_skills(self, position: WebElement):
        return self._filtro.filtrar_skills(position.text)

    def _get_publish_date(self, position: WebElement):
        try:
            publish_date = position.find_element(By.CSS_SELECTOR, "span.date").text
        except:
            publish_date = ""

        return self._filtro.filtrar_fecha(publish_date)

    def asdict(self):
        dict_super = super().asdict()
        dict_super["nombre"] = __class__.__name__

        return dict_super
