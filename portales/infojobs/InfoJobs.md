# Portal Infojobs

En primer lugar, se han definido los metodos de la interfaz de busqueda ([OperacionesBusquedaInterface](interfaces/operacionesBusquedaInterface.py)).

## Pasos 

1. Abre la pagina [Infojobs.net](https://www.infojobs.net/). [Codigo](./infojobs.py#L20)

    ```python
    def buscar(self, keyword:str):
        driver = self._driver

        # Abre la pagina de InfoJobs
        driver.get(self._base_url)
        ...
    ```
   
2. En el caso de infojobs, las busquedas de las palabras claves no se pueden hacer directamente desde la url (en forma de parametro) por lo que requiere de una busqueda manual usando Selenium. [Codigo](./infojobs.py#L29)

    ```python
    def __buscar_keyword(self,keyword:str):
        driver = self._driver

        # Localizadores
        input_busqueda_locator = "palabra"
        boton_busqueda_locator = "searchOffers"
        
        # Espera hasta que el campo de busqueda este visible
        # y obtiene los elementos
        input_busqueda = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, input_busqueda_locator)))
        boton_busqueda = driver.find_element(By.ID, boton_busqueda_locator)
        
        # Inserta la palabra clave en el campo
        input_busqueda.clear()
        input_busqueda.send_keys(keyword)

        # Comprueba si el pop-up de las cookies permite clickar el boton
        self.__gestionar_cookies()

        # Click boton busqueda
        boton_busqueda.click()
    ```
3. Al usar un navegador con un perfil recien creado, suele pedirnos que aceptemos las cookies de la pagina. [Codigo](./infojobs.py#L53)
   ```python
    def __gestionar_cookies(self):
        driver = self._driver
        
        # Localizadores
        panel_cookies_locator = "cmpContainer"
        aceptar_cookies_boton_locator = '[data-testid="TcfAccept"]'

        try:    
            # Acepta las cookies
            driver.find_element(By.ID, panel_cookies_locator)
            driver.find_element(By.CSS_SELECTOR,aceptar_cookies_boton_locator).click()         

        except:
            # No hay pop up de cookies
            pass
    ```