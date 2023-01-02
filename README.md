# Trabajo de Fin de Grado

TFG que ordena y clasifica los requisitos de ofertas de trabajo relacionadas con la informática en España usando técnicas de web scraping con Selenium.

Basado en https://github.com/csbhakat/DataCollection_Selenium_naukri

## Cambios generales

- Los métodos se obtención de datos se han pasado a la interfaz [OperacionesBusquedaInterface](interfaces/operacionesBusquedaInterface.py).
  
- La gestión del CSV se realiza desde la clase [csvHandler](util/csvHandler.py).

- Para la gestión del driver de Chrome, se usa un módulo basado en Selenium  ([undetectable-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)) que ofrece:
  
    - Protección contra bloqueo de los portales al detectarnos como bots.
  
    - Descarga del último driver de Chrome disponible, y parcheo automático de este.
  
    - Genera un perfil temporal en Google Chrome, que se borra al finalizar la sesión de búsqueda.
  

- La lógica principal del script se desarrolla en el archivo [main](./main.py).
    
    - Las palabras clave se declaran en la variable [keywords](./main.py#L21).  
  
        ```python
        keywords:list=["Big Data","Backend","Spring Boot"]
        ```
   
    - El numero de paginas se declara en la variable [n_paginas](./main.py#L22).
    
        ```python
        n_paginas:int = 10    
        ```

    - En el script original se calculan las URLs de Naukri (Portal laboral indio) desde donde se van a extraer los datos de las ofertas laborales. En este caso, esta parte se gestionará desde cada portal laboral, ya que no todos pueden cambiar de página desde la URL o buscar las palabras clave desde ahí.
  
        Se ha optado por recorrer las palabras clave en un bucle [for](./main.py#L37) e ir recabando la información portal a portal. 

        ```python
        for keyword in keywords:
            portal.buscar(keyword)
        ```
- Uso del modulo logging para reporte de eventos.

- Los portales de empleo genéricos como InfoJobs o Indeed no disponen de unos requisitos claros a la hora de mostrar las ofertas. El formato de los requisitos es libre para cada empresa, por lo que he sacado los requisitos más demandados desde un [portal](https://ticjob.es/) enfocado solo a empleos tecnológicos (que también será analizada) y los he almacenado en el archivo [constantes.py](./util/constantes.py) (+300 requisitos) que se comparara con cada oferta.

## Cambios específicos de cada portal

Para una mejor organización de los casos de cada portal, se ha seguido el patrón de diseño recomendado por Selenium "[Page Object Models](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)". Los cambios realizados al script original específicos de cada portal, se pueden encontrar en la el archivo ".md" en la carpeta de cada uno de ellos. De todas formas, se irán listando a continuación:

- InfoJobs: [InfoJobs.md](./portales/infojobs/InfoJobs.md).
- Indeed: [Indeed.md](./portales/indeed/Indeed.md).
