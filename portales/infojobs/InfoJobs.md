# Portal Infojobs

En primer lugar, se han definido los métodos de la interfaz de búsqueda ([OperacionesBusquedaInterface](interfaces/operacionesBusquedaInterface.py)).

## ✅ Pasos 

1. Abre la página [Infojobs.net](https://www.infojobs.net/) y recorre las posiciones del total de páginas. [Código](./infojobs.py#L30).

    ```python
    def buscar(self, keyword:str):
        driver = self._driver

        # Abre la pagina de InfoJobs
        driver.delete_all_cookies()
        driver.get(self._base_url)
        self._log.info("Infojobs.net abierta")
        
        for i in range(1, self._n_paginas+1):
            try:
                self.__buscar_keyword(keyword=keyword, n_pagina=i)
                self.__scroll_fin_pagina()
                self.__analizar_posiciones()
            except (TimeoutException,NoSuchElementException):
                return
    ```
   
2. Se busca la palabra clave en una página [Código](./infojobs.py#L47).

    ```python
    def __buscar_keyword(self,keyword:str, n_pagina:int):
        
        ruta_busqueda = "jobsearch/search-results/list.xhtml"
        parametro_keyword="keyword=" + keyword
        parametro_pagina="page=" + str(n_pagina)
        
        driver = self._driver
        driver.get(f"{self._base_url}{ruta_busqueda}?{parametro_pagina}&{parametro_keyword}")
        
        # Espera que cargue la pagina
        sleep(5)

        # Comprueba si hay cookies
        self.__gestionar_cookies()
    ```
3. Al usar un navegador con un perfil recién creado, suele pedirnos que aceptemos las cookies de la página. [Código](./infojobs.py#L63).
    

   ```python
    def __gestionar_cookies(self):
        driver = self._driver
        
        # Localizadores
        aceptar_cookies_boton_locator = '[data-testid="TcfAccept"]'

        try:    
            # Acepta las cookies
            driver.find_element(By.CSS_SELECTOR,aceptar_cookies_boton_locator).click()         
            sleep(1)
        except:
            # No hay pop up de cookies
            pass
    ```

4. Cuando la página de resultados ha cargado, en el caso de InfoJobs, es necesario bajar hasta el final de la página para que todas las posiciones se rendericen y aparezcan en el DOM. [Código](./infojobs.py#L80).
   
    ```python
    def __scroll_fin_pagina(self):
        
        driver = self._driver
    ```
    
    
    Para esta operación, se requieren algunos datos internos del DOM. Para ello se usan 3 [scripts](./infojobs.py#L84). En JavaScript que se ejecutan en el navegador.

    - Devuelve la altura del dispositivo donde está abierto el navegador.

        ```javascript
        
        return visualViewport.height;

        ```
    - Devuelve la posición inferior en píxeles del cuerpo del HTML. 
  
        ```javascript
        
        return document.body.getBoundingClientRect().bottom;

        ```
    - Hace scroll hasta la posición pasada como argumento, en este caso, la variable [altura_scroll](./infojobs.py#L101).
 
        ```javascript
        
        window.scrollTo(0, arguments[0]);

        ```

    Se va bajando hasta el final poco a poco para que las posiciones se vayan renderizando, ya que si se baja directamente hasta el final del body, no carga ninguna.

    ```python

        # Declaracion variables
        altura_scroll = 0
        altura_vp = driver.execute_script(altura_viewport_script)
        
        posicion_bottom_anterior = 0
        posicion_bottom_actual  = driver.execute_script(posicion_bottom_script) 
        
        # Scroll hacia abajo hasta el final de la pagina
        while posicion_inferior_anterior != posicion_inferior_actual:

            #Hace scroll
            altura_scroll += altura_vp
            driver.execute_script(scroll_script, altura_scroll)
            
            # Se espera 1 seg a que las posiciones se rendericen en el DOM
            sleep(1)

            # Obtiene el final de la pagina y comprueba si es igual que la
            # ultima iteracion
            posicion_inferior_anterior = posicion_inferior_actual
            posicion_inferior_actual  = driver.execute_script(posicion_inferior_script) 
    ```
5. Analiza las posiciones de la página de resultados. Extrae el link de cada oferta, lo abre en un driver nuevo, y extrae la información. Por último lo escribe en el CSV y cierra el driver auxiliar. [Código](./infojobs.py#L113).

    ```python
    def __analizar_posiciones(self):

        driver = self._driver
        
        # Localizadores 
        posiciones_locator = "div.ij-ContentSearch-list  ul div.sui-AtomCard-link"
        resumen_posicion_locator = ".panel-canvas.panel-rounded"

        # Obtiene las posiciones de esa pagina
        posiciones = driver.find_elements(By.CSS_SELECTOR, posiciones_locator)
        self._log.info(f"Analizando {len(posiciones)} ofertas.")

        # Abre cada posicion y extrae la informacion
        for i,posicion in enumerate(posiciones):
            
            #Carga la oferta en un nuevo driver
            link_posicion = self.__get_link(posicion)
            
            driverAux = uc.Chrome()    
            driverAux.get(link_posicion)

            #Espera a que aparezca el elemento que resume la oferta
            resumen_oferta = WebDriverWait(driver=driverAux,timeout=10).until(


                EC.presence_of_element_located((By.CSS_SELECTOR,resumen_posicion_locator)))
            
            # Extrae la informacion
            informacion_posicion={}
            titulo=self.__get_title(resumen_oferta)
            ubicacion=self.__get_location(resumen_oferta)
            compañia=self.__get_companyname(resumen_oferta)
            experiencia=self.__get_experience(resumen_oferta)
            salario=self.__get_salaryexpected(resumen_oferta)

            # Rellena el diccionario
            informacion_posicion['titulo']=titulo
            informacion_posicion['compañia']=compañia
            informacion_posicion['experiencia']=experiencia
            informacion_posicion['salario']=salario
            informacion_posicion['ubicacion']=ubicacion
            
            self._csv.escribir_linea(valores=informacion_posicion.values())

            driverAux.close()
    ```

## 📝 Notas

- Se usan expresiones regulares para extraer la experiencia y el salario de las descripciones de las ofertas.

- Después de que el driver clickee sobre algún elemento, se espera 1 segundo a que el navegador lo procese.

- En caso de que una acción cargue una página, se esperan 5 segundos o se espera a la aparición de un elemento concreto.
  


## 🐞 Problemas encontrados

- Cuando se abría una oferta en una nueva pestaña dentro del driver donde están los resultados, después de 10-15 ofertas InfoJobs muestra un captcha. Se ha optado por abrir un nuevo driver en vez de una nueva pestaña.

- Después de buscar varias veces (no hay un número exacto) acaba mostrando un captcha.



    En ese caso la [excepción](./infojobs.py#L43) que salta se controla desde el método buscar. En mi caso, para volver a lanzar el script estoy usando una VPN para cambiar de ip cada vez que aparece y funciona sin problemas.
