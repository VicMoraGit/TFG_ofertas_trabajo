# Portal Infojobs

En primer lugar, se han definido los metodos de la interfaz de busqueda ([OperacionesBusquedaInterface](interfaces/operacionesBusquedaInterface.py)).

## ✅ Pasos 

1. Abre la pagina [Infojobs.net](https://www.infojobs.net/) y recorre las posiciones del total de paginas. [Codigo](./infojobs.py#L29)

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
   
2. Se busca la palabra clave en una pagina [Codigo](./infojobs.py#L46)

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
3. Al usar un navegador con un perfil recien creado, suele pedirnos que aceptemos las cookies de la pagina. [Codigo](./infojobs.py#L62)
    

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

4. Cuando la pagina de resultados ha cargado, en el caso de InfoJobs, es necesario bajar hasta el final de la pagina para que todas las posiciones se rendericen y aparezcan en el DOM. [Codigo](./infojobs.py#L79)
   
    ```python
    def __scroll_fin_pagina(self):
        
        driver = self._driver
    ```
    
    
    Para esta operacion, se requieren algunos datos internos del DOM. Para ello se usan 3 [scripts](./infojobs.py#L83). en JavaScript que se ejecutan en el navegador.

    - Devuelve la altura del dispositivo donde esta abierto el navegador

        ```javascript
        
        return visualViewport.height;

        ```
    - Devuelve la posicion inferior en pixeles del cuerpo del HTML. 
  
        ```javascript
        
        return document.body.getBoundingClientRect().bottom;

        ```
    - Hace scroll hasta la posicion pasada como argumento, en este caso, la variable [altura_scroll](./infojobs.py#L100).
 
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
5. Analiza las posiciones de la pagina de resultados. Extrae el link de cada oferta, lo abre en un driver nuevo, y extrae la informacion. Por ultimo lo escribe en el csv y cierra el driver auxiliar.

    ```python
    def __analizar_posiciones(self):

        driver = self._driver
        
        # Localizadores 
        posiciones_locator = "div.ij-ContentSearch-list > ul div.sui-AtomCard-link"
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
- 
- Despues de que el driver clickee sobre algun elemento, se espera 1 segundo a que el navegador lo procese.

- En caso de que una accion cargue una pagina, se esperan 5 segundos o se espera a la aparicion de un elemento concreto
  
## 🐞 Problemas encontrados

- Cuando se abria una oferta en una nueva pestaña dentro del driver donde estan los resultados, despues de 10-15 ofertas InfoJobs muestra un captcha. Se ha optado por abrir un nuevo driver en vez de una nueva pestaña

- Despues de buscar varias veces (no hay un numero exacto) acaba mostrando un captcha.

    En ese caso la excepcion que salta se controla desde el metodo buscar. En mi caso, para volver a lanzar el script estoy usando una vpn para cambiar de ip cada vez que aparece y funciona sin problemas

