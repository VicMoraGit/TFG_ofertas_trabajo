# Portal Indeed

En primer lugar, se han definido los metodos de la interfaz de busqueda ([OperacionesBusquedaInterface](interfaces/operacionesBusquedaInterface.py)).

## ✅ Pasos 

1. Abre la pagina [es.indeed.com](https://es.indeed.com/) y recorre las posiciones del total de paginas. [Codigo](./indeed.py#L29)

    ```python
    def buscar(self, keyword:str):
        driver = self._driver

        # Abre la pagina de Indeed
        driver.delete_all_cookies()
        driver.get(self._base_url)
        self._log.info("Indeed.com abierta")
        
        for i in range(1, self._n_paginas+1):
            self.__buscar_keyword(keyword=keyword, n_pagina=i)
            self.__analizar_posiciones()

    ```
   
2. Se busca la palabra clave en una pagina [Codigo](./indeed.py#L41)

    ```python
    def __buscar_keyword(self,keyword:str, n_pagina:int):
        
        ruta_busqueda = "jobs"
        parametro_keyword="q=" + keyword
        parametro_pagina="start=" +str(n_pagina) +"0"
        
        driver = self._driver
        driver.get(f"{self._base_url}{ruta_busqueda}?{parametro_pagina}&{parametro_keyword}")
        
        # Espera que cargue la pagina
        sleep(5)    
    ```
3. Se analizan las ofertas. Se extrae la informacion que se muestra en la pagina de resultado, y se abre la oferta en una pestaña nueva para sacar la experiencia y el salario tambien. [Codigo](./indeed.py#L53)
   ```python
   def __analizar_posiciones(self):
        
        driver = self._driver

        # Localizadores 
        posiciones_locator = '#mosaic-provider-jobcards > ul > li'
        descripcion_oferta_locator = 'jobDescriptionText'
        
        # Guarda el id de la pestaña de resultados
        ch = driver.current_window_handle

        # Obtiene las posiciones de esa pagina
        posiciones = driver.find_elements(By.CSS_SELECTOR,posiciones_locator)
        
        # Abre cada posicion y extrae la informacion
        for i,posicion in enumerate(posiciones):

            # Extrae la informacion
            informacion_posicion={}
            titulo=self.__get_title(posicion)
            ubicacion=self.__get_location(posicion)
            compañia=self.__get_companyname(posicion)
            link_posicion = self.__get_link(posicion)
            
            # Si el link esta vacio, pasa a la siguiente posicion.
            # Si no, abre la oferta en una nueva pestaña y extrae el salario y la experiencia
            if link_posicion == "":
                continue
            driver.tab_new(link_posicion)           
            driver.switch_to.window(driver.window_handles[1])

            #Espera a que la descripcion de la oferta aparezca
            descripcion = WebDriverWait(driver=driver,timeout=10).until(
                EC.presence_of_element_located((By.ID,descripcion_oferta_locator)))
            
            #Extrae mas informacion
            experiencia=self.__get_experience(descripcion)
            salario=self.__get_salaryexpected(descripcion)
            
            # Rellena el diccionario
            if not titulo=="":
                informacion_posicion['titulo']=titulo
                informacion_posicion['compañia']=compañia
                informacion_posicion['experiencia']=experiencia
                informacion_posicion['salario']=salario
                informacion_posicion['ubicacion']=ubicacion
   
                #Write to csv file
                self._csv.escribir_linea(valores=informacion_posicion.values())

            #Cierra la oferta y devuelve el control a la pestaña de resultados                
            driver.close()
            driver.switch_to.window(ch)
   ```

## 📝 Notas

- Se usan expresiones regulares para extraer la experiencia y el salario de las descripciones de las ofertas

- En caso de que una accion cargue una pagina, se esperan 5 segundos o se espera a la aparicion de un elemento concreto

- Al contrario que en InfoJobs, Indeed no ha mostrado ningun metodo contra bots, por lo que las ofertas se han abierto en el mismo driver sin encontrar ningun problema
  
## 🐞 Problemas encontrados

- A veces el script devuelve ofertas que no contienen ningun link, es por eso que se [comprueba si el link esta vacio](./indeed.py#L80) antes de abrir la oferta en una pestaña. Puede ser por que haya presencia de publicidad, y detecte esa publicidad como una oferta.