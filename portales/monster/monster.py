from time import sleep, time
from logging import DEBUG, Logger, getLogger
from traceback import format_exc
from models.ofertaDto import Oferta

# Clases proyecto
from portales.portal import Portal
from sql.daoImpl.ofertaDaoImpl import OfertaDao
from util.azure_translator import Traductor
from util.csvHandler import csvHandler
import util.stats as stats

# Selenium
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Monster(Portal):
    def __init__(self, n_paginas: int, csvHandler: csvHandler):
        super().__init__(n_paginas, csvHandler)

        self._base_url: str = "https://www.monster.es/"
        self._log: Logger = getLogger(__class__.__name__)
        self._titulo_ultima_oferta_pagina = ""
        # self._log.setLevel(DEBUG)
        self.ofertaDao = OfertaDao()

    def buscar(self, keyword: str):
        self._busqueda_finalizada = False
        super().abrir_nav()
        self._driver.get(self._base_url)
        self._log.info("Monster.es abierta")

        for i in range(1, self._n_paginas_total + 1):

            self._buscar_keyword(keyword=keyword, n_pagina=i)

            if self._busqueda_finalizada:
                break

            self._analizar_posiciones()

    def _buscar_keyword(self, keyword: str, n_pagina: int):
        ruta_busqueda = "trabajo/buscar"
        parametro_keyword = "q=" + keyword
        parametro_pagina = "page=" + str(n_pagina)

        driver = self._driver
        driver.get(
            f"{self._base_url}{ruta_busqueda}?{parametro_keyword}&{parametro_pagina}&geo=0&where=españa"
        )
        self._log.info(f"Analizando pagina {str(n_pagina)}")

        # Localizadores
        posiciones_locator = "#JobCardGrid > ul > li"

        # Espera que carguen las posiciones. Si no hay posiciones es que se ha llegado a la ultima pagina.
        try:
            WebDriverWait(driver=driver, timeout=10).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, posiciones_locator))
            )
        except TimeoutException:
            self._busqueda_finalizada = True
            return

    def _analizar_posiciones(self):
        driver = self._driver
        valores_posiciones = []

        n_ofertas_analizadas = 0
        n_ofertas_con_salario = 0
        n_ofertas_con_experiencia = 0

        # Localizadores
        posiciones_locator = "#JobCardGrid > ul > li"
        descripcion_oferta_locator = "BigJobCardId"

        posiciones = driver.find_elements(
            By.CSS_SELECTOR, posiciones_locator)

        self._log.info(f"Analizando ofertas.")

        # Abre cada posicion y extrae la informacion
        for i, posicion in enumerate(posiciones):

            # Si despues de 10 segundos no ha encontrado la descripcion o hay error al hacer scroll, ha acabado la busqueda
            try:
                # Se mueve al elemento y espera a que cargue su descripcion para sacar la info

                self._scroll_al_elemento(posicion)
                sleep(0.5)
                posicion.click()
                descripcion = WebDriverWait(driver=driver, timeout=10).until(
                    EC.visibility_of_element_located(
                        (By.ID, descripcion_oferta_locator))
                )
            except:
                break

            # Extrae la informacion de la oferta visible
            oferta: Oferta = Oferta()
            oferta.titulo = self._get_title(descripcion)

            # Rellena el diccionario
            if not oferta.titulo == "":
                oferta.ubicaciones = self._get_locations(descripcion)
                oferta.es_teletrabajo = self._is_teletrabajo(
                    oferta.ubicaciones)
                oferta.companyia = self._get_companyname(descripcion)
                oferta.fecha_publicacion = self._get_publish_date(descripcion)
                oferta.experiencia = self._get_experience(descripcion)
                oferta.salario = self._get_salaryexpected(descripcion)
                oferta.puesto = self._get_position(descripcion)
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

        # Escribe en CSV
        self._csv.escribir_lineas(valores_posiciones)

        self._log.info(f"{len(posiciones)} ofertas analizadas.")

        # Actualiza estadisticas
        self._n_ofertas_analizadas += n_ofertas_analizadas
        self._n_ofertas_con_salario += n_ofertas_con_salario
        self._n_ofertas_con_experiencia += n_ofertas_con_experiencia
        self._n_paginas_analizadas += 1

    def _get_title(self, position):
        return position.find_element(By.CSS_SELECTOR, "h2.JobViewTitle").text.strip()

    def _get_companyname(self, position) -> str:
        try:
            empresa = position.find_element(
                By.CSS_SELECTOR, 'a[class^="company-name"] > h2'
            ).text
        except:
            empresa = ""

        return empresa

    def _get_experience(self, position):
        return self._filtro.filtrar_experiencia(position.text)

    def _get_salaryexpected(self, position):
        return self._filtro.filtrar_salario(position.text)

    def _is_teletrabajo(self, ubicaciones: list[int]):
        """
        53 es el ID de teletrabajo
        """
        if 53 in ubicaciones:
            return True
        return False

    def _get_position(self, position: WebElement):
        td = Traductor()
        indice_puesto = 0
        try:
            title = self._get_title(position)
            dominio_idioma = td.detectar_idioma(title)

            if dominio_idioma != "es":
                title = td.traducir(dominio_idioma, "es", title)
            indice_puesto = self._filtro.filtrar_posicion(title)

        except:
            self._log.error(format_exc())

        return indice_puesto

    def _get_locations(self, descripcion: WebElement) -> list:
        """
        Extrae la localizacion de su CSS y de la descripcion del anuncio en caso de que existiesen
        ubicaciones extra.
        """

        try:
            locations = self._filtro.filtrar_localizacion(descripcion.text)

        except:
            locations = []
        return list(locations)

    def _get_skills(self, position):
        return self._filtro.filtrar_skills(position.text)

    def _get_publish_date(self, position):
        return self._filtro.filtrar_fecha(
            position.find_element(
                By.CSS_SELECTOR, '[data-test-id="svx-jobview-posted"]'
            ).text
        )

    def _scroll_al_elemento(self, posicion):
        driver = self._driver
        driver.execute_script("arguments[0].scrollIntoView(true);", posicion)

    def actualizar_estadisticas(self):
        super().actualizar_estadisticas()
        stats.datos_portales.append(self.asdict())

    def asdict(self):
        dict_super = super().asdict()
        dict_super["nombre"] = __class__.__name__

        return dict_super
