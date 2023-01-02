# Trabajo de Fin de Grado

TFG que ordena y clasifica los requisitos de ofertas de trabajo relacionadas con la informatica en España usando tecnicas de web scraping con Selenium

Basado en https://github.com/csbhakat/DataCollection_Selenium_naukri

## Cambios generales

- Los metodos se obtencion de datos se han pasado a  la interfaz [OperacionesBusquedaInterface](interfaces/operacionesBusquedaInterface.py).
  
- La gestion del csv se realiza desde la clase [csvHandler](util/csvHandler.py).

- Para la gestion del driver de Chrome, se usa un modulo basado en selenium  ([undetectable-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)) que ofrece:
  
    - Proteccion contra bloqueo de los portales al detectarnos como bots.
  
    - Descarga del ultimo driver de Chrome disponible, y parcheo automatico de este.
  
    - Genera un perfil temporal en Google Chrome, que se borra al finalizar la sesion de busqueda.
  

- La logica principal del script se desarrolla en el archivo [main](./main.py).
    
    - Las palabras clave se declaran en la variable [keywords](./main.py#L18).  
  
        ```python
        keywords:list=["Big Data","Backend","Spring Boot"]
        ```
   
    - El numero de paginas se declara en la variable [n_paginas](./main.py#L19).
    
        ```python
        n_paginas:int = 10    
        ```

    - En el script original se calculan las urls de Naukri (Portal laboral indio) desde donde se van a extraer los datos de las ofertas laborales. En este caso, esta parte se gestionara desde cada portal laboral, ya que no todos pueden cambiar de pagina desde la url o buscar las palabras clave desde ahi.
  
        Se ha optado por recorrer las palabras clave en un bucle [for](./main.py#L29) e ir recabando la informacion portal a portal. 

        ```python
        for keyword in keywords:
            portal.buscar(keyword)
        ```
- Uso del modulo logging para reporte de eventos.

- Los portales de empleo genericos como InfoJobs o Indeed no disponen de unos requisitos claros a la hora de mostrar las ofertas. El formato de los requisitos es libre para cada empresa, por lo que he sacado los requisitos mas demandados desde un [portal](https://ticjob.es/) enfocado solo a empleos tecnologicos (que tambien sera analizada) y los he almacenado en el archivo [constantes.py](./util/constantes.py) (+300 requisitos) que se comparara con cada oferta.

## Cambios especificos de cada portal

Para una mejor organizacion de los casos de cada portal, se ha seguido el patron de diseño recomendado por Selenium "[Page Object Models](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)". Los cambios realizados al script original especificos de cada portal, se pueden encontrar en la el archivo ".md" en la carpeta de cada uno de ellos. De todas formas, se iran listando a continuacion:

- InfoJobs: [InfoJobs.md](./portales/infojobs/InfoJobs.md).
- Indeed: [Indeed.md](./portales/indeed/Indeed.md).

