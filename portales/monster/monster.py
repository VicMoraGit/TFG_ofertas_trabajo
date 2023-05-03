from time import sleep, time
from logging import Logger, getLogger

# Clases proyecto
from portales.portal import Portal
from util.csvHandler import csvHandler
import util.stats as stats

# Selenium
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options


class Monster(Portal):
    def __init__(self, n_paginas: int, csvHandler: csvHandler):
        super().__init__(n_paginas, csvHandler)

        self._base_url: str = "https://www.monster.es/"
        self._log: Logger = getLogger(__class__.__name__)
        self._titulo_ultima_oferta_pagina = ""
        super().abrir_nav(headless=True)

        # self._log.setLevel(DEBUG)

    def buscar(self, keyword: str):
        self._busqueda_finalizada = False

        self._driver.get(self._base_url)
        self._log.info("Monster.es abierta")

        for i in range(1, self._n_paginas_total + 1):
            self._buscar_keyword(keyword=keyword, n_pagina=i)
            self._analizar_posiciones()
            if self._busqueda_finalizada:
                break

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
        posiciones_locator = 'div[aria-label="Empleos"] > div[tabindex="0"]'

        # Espera que carguen las posiciones. Si no hay posiciones es que se ha llegado a la ultima pagina.
        try:
            WebDriverWait(driver=driver, timeout=10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, posiciones_locator))
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
        titulo = ""

        # Localizadores
        posiciones_locator = 'div[aria-label="Empleos"] > div[tabindex="0"]'
        descripcion_oferta_locator = "BigJobCardId"

        # Presiona ESC ya que a veces aparece un pop up de inicio de sesion que para el script
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)

        # Obtiene las posiciones de esa pagina. Si no hay es que ha llegado a la ultima pagina.
        try:
            posiciones = driver.find_elements(By.CSS_SELECTOR, posiciones_locator)
        except NoSuchElementException:
            self._busqueda_finalizada = True
            return
        self._log.info(f"Analizando ofertas.")

        # Abre cada posicion y extrae la informacion
        for i, posicion in enumerate(posiciones):
            # Se mueve al elemento y espera a que cargue su descripcion para sacar la info
            self._scroll_al_elemento(posicion)
            sleep(0.5)
            posicion.click()

            # Si despues de 10 segundos no ha encontrado la descripcion, ha acabado la busqueda
            try:
                descripcion = WebDriverWait(driver=driver, timeout=10).until(
                    EC.presence_of_element_located((By.ID, descripcion_oferta_locator))
                )
            except:
                self._busqueda_finalizada = True
                return

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

        self._log.info(f"{len(posiciones)} ofertas analizadas.")

        # Escribe todas las ofertas en el csv
        self._csv.escribir_lineas(valores=valores_posiciones)
        self._log.debug("Informacion escrita en el CSV")

        # Actualiza estadisticas
        self._n_ofertas_analizadas += n_ofertas_analizadas
        self._n_ofertas_con_salario += n_ofertas_con_salario
        self._n_ofertas_con_experiencia += n_ofertas_con_experiencia
        self._n_paginas_analizadas += 1

    def _get_title(self, position):
        return position.find_element(
            By.CSS_SELECTOR, 'a[data-test-id="svx-job-title"]'
        ).text.strip()

    def _get_companyname(self, position):
        try:
            empresa = position.find_element(
                By.CSS_SELECTOR, 'h3[data-test-id="svx-job-company"]'
            ).text
        except:
            empresa = "Sin Informacion"

        return empresa

    def _get_experience(self, position):
        return self._filtro.filtrar_experiencia(position.text)

    def _get_salaryexpected(self, position):
        return self._filtro.filtrar_salario(position.text)

    def _get_location(self, position):
        return self._filtro.filtrar_localizacion(
            position.find_element(
                By.CSS_SELECTOR, 'p[data-test-id="svx-job-location"]'
            ).text.strip()
        )

    def _get_skills(self, position):
        return self._filtro.filtrar_skills(position.text)

    def _get_publish_date(self, position):
        return self._filtro.filtrar_fecha(
            position.find_element(
                By.CSS_SELECTOR, 'span[data-test-id="svx-job-date"]'
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
