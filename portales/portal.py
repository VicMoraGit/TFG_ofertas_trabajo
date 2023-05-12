# Clases proyecto
from time import time
from util.csvHandler import csvHandler
from util.filtro import FiltroOfertas
import util.stats as stats

from interfaces.operacionesBusquedaInterface import OperacionesBusquedaInterface as obi

# Selenium
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc

# DRIVER_VERSION = "112.0.5615.49"
DRIVER_VERSION = 112


class Portal(obi):
    def __init__(self, n_paginas: int, csvHandler: csvHandler):
        self._n_paginas_total = n_paginas
        self._csv = csvHandler
        self._filtro = FiltroOfertas()

        # Estadisticas Ofertas
        self._n_ofertas_analizadas = 0
        self._n_paginas_analizadas = 0
        self._n_ofertas_con_salario = 0
        self._n_ofertas_con_experiencia = 0

        # Estadisticas Rendimiento
        self._es_bloqueado = False
        self._ruta_captura_captcha = ""
        self._t_total = 0

    def abrir_nav(self, headless=False):
        options = Options()
        # options.add_experimental_option("useAutomationExtension",False)
        # options.add_experimental_option("excludeSwitches",["enable-automation"])
        if headless:
            options.add_argument("--headless")

        self._driver = uc.Chrome(
            options=options,
            version_main=DRIVER_VERSION,
        )
        """
        s = Service(ChromeDriverManager(version=DRIVER_VERSION).install())

        self._driver = WebDriver(service=s, options=options)
        """
    def buscar(self, keyword: str):
        pass

    def _buscar_keyword(self, keyword: str, n_pagina: int):
        pass

    def _analizar_posiciones(self):
        pass

    def _iniciar_cronometro(self):
        self._s_inicio = time()

    def _get_link(self, position: WebElement):
        pass

    def _get_title(self, position: WebElement):
        pass

    def _get_companyname(self, position: WebElement):
        pass

    def _get_experience(self, position: WebElement):
        pass

    def _get_salaryexpected(self, position: WebElement):
        pass

    def _get_location(self, position: WebElement):
        pass

    def _get_skills(self, position: WebElement):
        pass

    def _get_publish_date(self, position: WebElement):
        pass

    def actualizar_estadisticas(self):
        stats.n_ofertas_analizadas += self._n_ofertas_analizadas
        stats.n_ofertas_con_salario += self._n_ofertas_con_salario
        stats.n_ofertas_con_experiencia += self._n_ofertas_con_experiencia

        # Calcula el tiempo final
        s_final = time()
        self._t_total = round((s_final - self._s_inicio) / 60, 2)

    def asdict(self):
        return {
            "ofertas_analizadas": str(self._n_ofertas_analizadas),
            "ofertas_con_salario": str(self._n_ofertas_con_salario),
            "ofertas_con_experiencia": str(self._n_ofertas_con_experiencia),
            "es_bloqueado": self._es_bloqueado,
            "tiempo_total": self._t_total,
        }
