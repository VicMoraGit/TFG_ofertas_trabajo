# Portal Tecnoempleo

Hereda de la clase [Portal](../portal.py)

## ✅ Pasos 

1. Abre la página [https://www.tecnoempleo.com/](https://www.tecnoempleo.com/) y recorre las posiciones de cada pagina. [Código](./tecnoempleo.py#L32).

   
2. Se busca la palabra clave en una página [Código](./tecnoempleo.py#L73).

    ```python
    def __buscar_keyword(self,keyword:str, n_pagina:int):
        
        ruta_busqueda = "ofertas-trabajo"
        parametro_keyword="te=" + keyword
        parametro_pagina="pagina=" +str(n_pagina)
        
        driver = self._driver
        driver.get(f"{self._base_url}{ruta_busqueda}/?{parametro_keyword}&{parametro_pagina}")
        
        # Localizadores
        posiciones_locator = 'div.bg-white.col-12.col-sm-12.col-md-12.col-lg-9 > div.p-2.border-bottom.py-3.bg-white'
        
        # Espera que carguen las posiciones
        WebDriverWait(driver=driver,timeout=10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, posiciones_locator))) 
    ```
3. Se analizan las ofertas. En caso de que el titulo de la ultima oferta de la ultima pagina analizada coincida con el titulo de la ultima oferta de la pagina actual, se finaliza la busqueda.  [Código](./tecnoempleo.py#L94).

4. Mientras se analizan todas las ofertas, se van rellenando las estadisticas.

## 📊 Analisis del portal

- Se muestran 30 ofertas por cada pagina de resultados.
- Toda la informacion de la oferta menos los requirimientos esta regulada. Por tanto, se puede extraer directamente desde el atributo de la oferta, sin tener que analizar la descripcion con expresiones regulares.
- La fecha se pasa al formato DD-MM-YYYY, si la oferta se ha actualizado recientemente, se añade "actualizada" a la fecha, por lo que hay que analizar la fecha y presentarla en el formato correcto.
- Este portal no presenta ningun metodo de bloqueo contra bots. Por lo tanto, con una instancia del driver se puede obtener toda la informacion sin bloqueos.
  
- Si se quiere extraer la experiencia, es necesario entrar dentro de la oferta, ya que en la pagina de resultados no esta esa informacion.
  
## 🧪 Pruebas

Para comprobar el rendimiento y la robustez del script, se ha hecho la siguiente prueba: 

> Keywords =  Big Data, Desarrollo Web, Backend, Microservicios
> 
> Numero de paginas = 50

Arrojando [este csv](../../data/CSV/Tecnoempleo.csv) y las siguientes estadisticas:
 
|   |   |
|---|---|    
|Ofertas analizadas      | 896        
|Ofertas con salario     | 334
|Ofertas con experiencia | 850 
|Tiempo                  | 15.59 mins.

## 📝 Notas

- Se usan expresiones regulares para extraer la experiencia, el salario y los requerimientos de las descripciones de las ofertas.

- Algunas skills tienen caracteres que se usan para definir reglas en las expresiones regulares, por lo que se han escapado con [re.escape()](./tecnoempleo.py#L198)

## 🐞 Problemas encontrados

- A veces el script devuelve ofertas que no contienen ningún link, es por eso que se [comprueba si el link esta vacío](./tecnoempleo.py#L80) antes de abrir la oferta en una pestaña. Puede ser porque haya presencia de publicidad, y detecte esa publicidad como una oferta.

