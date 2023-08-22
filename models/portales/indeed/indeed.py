# Modulos python
from logging import Logger, getLogger, DEBUG
from time import sleep
from traceback import format_exc
from models.ofertaDto import Oferta

# Clases proyecto
from portales.portal import Portal
from util.azure_translator import Traductor
from util.csvHandler import csvHandler
import util.stats as stats
from exceptions.DescripcionNoEmbebida import DescripcionNoEmbebida

# DAOs
from sql.daoImpl.ofertaDaoImpl import OfertaDao

# Selenium
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException

# TODO:
# [x]: Comprobar teletrabajo
# [x]: Multiples localizaciones


class Indeed(Portal):
    def __init__(self, n_paginas: int, csvHandler: csvHandler, dominio_pais="es"):
        super().__init__(n_paginas, csvHandler)
        self.dominio_pais = dominio_pais
        self._base_url: str = f"https://{dominio_pais}.indeed.com/"
        self._log: Logger = getLogger(__class__.__name__)
        self._titulo_ultima_oferta_pagina = ""
        self._busqueda_finalizada = False

        # DAOs

        self.ofertaDao = OfertaDao()
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
                self._log.info(
                    f"Indeed.com {self.dominio_pais.upper()} abierta")

                try:
                    self._buscar_keyword(keyword=keyword, n_pagina=i)
                    if self._busqueda_finalizada:
                        self.close()

                        break
                    self._analizar_posiciones()
                    self._log.info("Quiting browser")
                    self._driver.close()

                except (DescripcionNoEmbebida, WebDriverException):
                    self._driver.save_screenshot("error.png")
                    self._log.error(format_exc())
                    self._busqueda_finalizada = True
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
        parametro_mas_recientes = 'sort=date'
        driver = self._driver
        driver.get(
            f"{self._base_url}{ruta_busqueda}?{parametro_pagina}&{parametro_keyword}&{parametro_mas_recientes}"
        )
        self._log.info(f"Analizando pagina {str(n_pagina+1)}")

        # Localizadores
        posiciones_locator = "#mosaic-provider-jobcards > ul > li div.cardOutline"

        # Espera que carguen las posiciones. Si no hay posiciones es que se ha llegado a la ultima pagina.
        try:
            WebDriverWait(driver=driver, timeout=10).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, posiciones_locator))
            )
        except TimeoutException:
            self._busqueda_finalizada = True
            return

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

            # Si despues de 10 segundos no ha encontrado la descripcion, ha saltado un captcha
            descripcion = WebDriverWait(driver=driver, timeout=10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, descripcion_oferta_locator)
                )
            )
            # Extrae la informacion de la oferta visible
            oferta: Oferta = Oferta()
            oferta.titulo = self._get_title(posicion)

            # Rellena el diccionario
            if not oferta.titulo == "":
                oferta.ubicaciones = self._get_locations(posicion, descripcion)
                oferta.es_teletrabajo = self._is_teletrabajo(
                    oferta.ubicaciones)
                oferta.companyia = self._get_companyname(posicion)
                oferta.fecha_publicacion = self._get_publish_date(posicion)
                oferta.experiencia = self._get_experience(descripcion)
                oferta.salario = self._get_salaryexpected(descripcion)
                oferta.puesto = self._get_position(posicion)
                oferta.requisitos = self._get_skills(descripcion)

                self._log.debug("Informacion extraida.")

                # Inserta la oferta en las posiciones para el csv
                valores_posiciones.append(oferta.to_csv())

                # Inserta la oferta en BD
                self.ofertaDao.crear(oferta)

                # Actualiza estadisticas
                n_ofertas_analizadas += 1
                if oferta.salario != "NULL":
                    n_ofertas_con_salario += 1
                if oferta.experiencia != "NULL":
                    n_ofertas_con_experiencia += 1
                self._log.debug("Estadisticas actualizadas")

            self._log.debug(f"Oferta analizada {i+1}/{len(posiciones)}")

        # Comprueba si esta es la ultima pagina de la palabra clave.
        # Si es la ultima, finaliza la busqueda y no añade las ultimas
        # posiciones ni estadisticas.

        # Escribe en CSV
        self._csv.escribir_lineas(valores_posiciones)

        self._log.info(f"{len(posiciones)} ofertas analizadas.")

        # Actualiza estadisticas
        self._n_ofertas_analizadas += n_ofertas_analizadas
        self._n_ofertas_con_salario += n_ofertas_con_salario
        self._n_ofertas_con_experiencia += n_ofertas_con_experiencia
        self._n_paginas_analizadas += 1

        if titulo == self._titulo_ultima_oferta_pagina:
            return
        else:
            self._titulo_ultima_oferta_pagina = titulo

    def _get_title(self, position: WebElement):
        try:
            title = position.find_element(By.CSS_SELECTOR, ".jobTitle").text
        except:
            self._log.error(format_exc())
            title = ""

        return title

    def _is_teletrabajo(self, ubicaciones: list[int]):
        """
        53 es el ID de teletrabajo
        """
        if 53 in ubicaciones:
            return True
        return False

    def _get_position(self, position: WebElement) -> int:
        td = Traductor()
        indice_puesto = 0
        try:
            title = position.find_element(By.CSS_SELECTOR, ".jobTitle").text
            dominio_idioma = td.detectar_idioma(title)

            if dominio_idioma != "es":
                title = td.traducir(dominio_idioma, "es", title)
            indice_puesto = self._filtro.filtrar_posicion(title)

        except:
            self._log.error(format_exc())

        return indice_puesto

    def _get_companyname(self, position: WebElement):
        try:
            company = position.find_element(
                By.CSS_SELECTOR, ".companyName").text

        except:
            company = ""
        return company

    def _get_experience(self, position: WebElement):
        return self._filtro.filtrar_experiencia(position.text)

    def _get_salaryexpected(self, position: WebElement) -> (str | int):
        return self._filtro.filtrar_salario(position.text)

    def _get_locations(self, position: WebElement, descripcion: WebElement) -> list:
        """
        Extrae la localizacion de su CSS y de la descripcion del anuncio en caso de que existiesen
        ubicaciones extra.
        """

        posicion = position.find_element(By.CSS_SELECTOR, ".companyLocation")
        try:
            locations = self._filtro.filtrar_localizacion(
                posicion.text + descripcion.text
            )

        except:
            locations = []
        return list(locations)

    def _get_skills(self, position: WebElement):
        return self._filtro.filtrar_skills(position.text)

    def _get_publish_date(self, position: WebElement):
        try:
            publish_date = position.find_element(
                By.CSS_SELECTOR, "span.date").text
        except:
            publish_date = ""

        return self._filtro.filtrar_fecha(publish_date)

    def asdict(self):
        dict_super = super().asdict()
        dict_super["nombre"] = __class__.__name__

        return dict_super
