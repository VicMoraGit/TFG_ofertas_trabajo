from time import sleep, time
from logging import Logger, getLogger
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
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options


class Tecnoempleo(Portal):
    def __init__(self, n_paginas: int, csvHandler: csvHandler):
        super().__init__(n_paginas, csvHandler)

        self._base_url: str = "https://www.tecnoempleo.com/"
        self._log: Logger = getLogger(__class__.__name__)
        self._titulo_ultima_oferta_pagina = ""
        super().abrir_nav(headless=False)

        # self._log.setLevel(DEBUG)
        self.ofertaDao = OfertaDao()

    def buscar(self, keyword: str):
        self._busqueda_finalizada = False

        self._driver.get(self._base_url)
        self._log.info("Tecnoempleo.com abierta")

        for i in range(1, self._n_paginas_total + 1):
            self._buscar_keyword(keyword=keyword, n_pagina=i)
            self._analizar_posiciones()
            if self._busqueda_finalizada:
                break

    def _buscar_keyword(self, keyword: str, n_pagina: int):
        ruta_busqueda = "ofertas-trabajo"
        parametro_keyword = "te=" + keyword
        parametro_pagina = "pagina=" + str(n_pagina)

        driver = self._driver
        driver.get(
            f"{self._base_url}{ruta_busqueda}/?{parametro_keyword}&{parametro_pagina}"
        )
        self._log.info(f"Analizando pagina {str(n_pagina)}")

        # Localizadores
        posiciones_locator = "div.bg-white.col-12.col-sm-12.col-md-12.col-lg-9 > div.p-2.border-bottom.py-3.bg-white"

        # Espera que carguen las posiciones
        WebDriverWait(driver=driver, timeout=10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, posiciones_locator))
        )

    def _analizar_posiciones(self):
        driver = self._driver
        valores_posiciones = []

        n_ofertas_analizadas = 0
        n_ofertas_con_salario = 0
        n_ofertas_con_experiencia = 0
        titulo = ""
        ch = driver.current_window_handle
        # Localizadores
        posiciones_locator = "div.bg-white.col-12.col-sm-12.col-md-12.col-lg-9 > div.p-2.border-bottom.py-3.bg-white"
        descripcion_oferta_locator = "section > div.container > div.row.col-border"

        # Obtiene las posiciones de esa pagina
        posiciones = driver.find_elements(By.CSS_SELECTOR, posiciones_locator)
        self._log.info(f"Analizando ofertas.")

        # Abre cada posicion y extrae la informacion
        for i, posicion in enumerate(posiciones):
            # Abre cada posicion en una pestaña nueva para extraer la info
            link = self._get_link(posicion)

            driver.switch_to.new_window("tab")
            driver.get(link)
            try:
                descripcion = WebDriverWait(driver=driver, timeout=10).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, descripcion_oferta_locator)
                    )
                )
            except:
                driver.close()
                driver.switch_to.window(ch)
                continue

            # Extrae la informacion de la oferta visible
            oferta: Oferta = Oferta()
            oferta.titulo = self._get_title(descripcion)

            # Rellena el diccionario
            if not oferta.titulo == "":
                oferta.ubicaciones = self._get_locations(descripcion)
                oferta.es_teletrabajo = self._is_teletrabajo(oferta.ubicaciones)
                oferta.companyia = self._get_companyname(descripcion)
                oferta.fecha_publicacion = self._get_publish_date(descripcion)
                oferta.experiencia = self._get_experience(descripcion)
                oferta.salario = self._get_salaryexpected(descripcion)
                oferta.puesto = self._get_position(descripcion)
                oferta.requisitos = self._get_skills(descripcion)

                self._log.debug("Informacion extraida.")

                # Inserta la oferta en BD

                self.ofertaDao.crear(oferta)

                # Actualiza estadisticas
                n_ofertas_analizadas += 1
                if oferta.salario is not None:
                    n_ofertas_con_salario += 1
                if oferta.experiencia is not None:
                    n_ofertas_con_experiencia += 1

                self._log.debug("Estadisticas actualizadas")

            self._log.debug(f"Oferta analizada {i+1}/{len(posiciones)}")

            # Cierra y devuelve el control a la pestaña de resultados
            driver.close()
            driver.switch_to.window(ch)

        # Comprueba si esta es la ultima pagina de la palabra clave.
        # Si es la ultima, finaliza la busqueda y no añade las ultimas
        # posiciones ni estadisticas.

        if titulo == self._titulo_ultima_oferta_pagina:
            self._busqueda_finalizada = True
            return
        else:
            self._titulo_ultima_oferta_pagina = titulo

        self._log.info(f"{len(posiciones)} ofertas analizadas.")

        # Actualiza estadisticas
        self._n_ofertas_analizadas += n_ofertas_analizadas
        self._n_ofertas_con_salario += n_ofertas_con_salario
        self._n_ofertas_con_experiencia += n_ofertas_con_experiencia
        self._n_paginas_analizadas += 1

    def _get_link(self, position: WebElement):
        return position.find_element(By.CSS_SELECTOR, "h3 > a").get_attribute("href")

    def _get_title(self, position):
        return position.find_element(
            By.CSS_SELECTOR, 'h1[itemprop="title"]'
        ).text.strip()

    def _get_companyname(self, position):
        try:
            empresa = position.find_element(
                By.CSS_SELECTOR, 'span[itemprop="name"]'
            ).text
        except:
            empresa = None

        return empresa

    def _get_experience(self, position):
        return self._filtro.filtrar_experiencia(
            self._extraer_caracteristica(position, "Experiencia")
        )

    def _get_salaryexpected(self, position):
        return self._filtro.filtrar_salario(
            self._extraer_caracteristica(position, "Salario")
        )

    def _is_teletrabajo(self, ubicaciones: list[int]):
        """
        53 es el ID de teletrabajo
        """
        if 53 in ubicaciones:
            return True
        return False

    def _get_locations(self, descripcion: WebElement):
        """
        Extrae la localizacion de su CSS y de la descripcion del anuncio en caso de que existiesen
        ubicaciones extra.
        """
        try:
            locations = self._filtro.filtrar_localizacion(descripcion.text)

        except:
            locations = []
        return locations

    def _get_position(self, position: WebElement):
        td = Traductor()
        indice_puesto = 0
        try:
            title = position.find_element(By.CSS_SELECTOR, 'h1[itemprop="title"]').text
            dominio_idioma = td.detectar_idioma(title)

            if dominio_idioma != "es":
                title = td.traducir(dominio_idioma, "es", title)
            indice_puesto = self._filtro.filtrar_posicion(title)

        except:
            self._log.error(format_exc())

        return indice_puesto

    def _get_skills(self, position: WebElement):
        return self._filtro.filtrar_skills(position.text)

    def _get_publish_date(self, position):
        return self._filtro.filtrar_fecha(
            position.find_element(By.CSS_SELECTOR, "span.ml-4").text
        )

    def _extraer_caracteristica(self, position: WebElement, nombre_caracteristica):
        valor = None

        # Localizadores
        caracteristicas_locator = "ul > li"
        nombre_caracteristica_locator = "span.d-inline-block.px-2"
        valor_caracteristica_locator = "span.float-end"

        # Se elimina la ultima caracteristica porque son la skills y tienen otra maquetacion
        caracteristicas = position.find_elements(
            By.CSS_SELECTOR, caracteristicas_locator
        )[:-1]

        for caracteristica in caracteristicas:
            nombre_caracteristica_lista = caracteristica.find_element(
                By.CSS_SELECTOR, nombre_caracteristica_locator
            ).text

            if nombre_caracteristica_lista == nombre_caracteristica:
                valor = caracteristica.find_element(
                    By.CSS_SELECTOR, valor_caracteristica_locator
                ).text
                break
        return valor

    def actualizar_estadisticas(self):
        super().actualizar_estadisticas()
        stats.datos_portales.append(self.asdict())

    def asdict(self):
        dict_super = super().asdict()
        dict_super["nombre"] = __class__.__name__

        return dict_super
