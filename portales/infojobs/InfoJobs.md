# Portal Infojobs

En primer lugar, se han definido los métodos de la interfaz de búsqueda ([OperacionesBusquedaInterface](interfaces/operacionesBusquedaInterface.py)).

## ✅ Pasos 

1. Abre la página [Infojobs.net](https://www.infojobs.net/) y recorre las posiciones del total de páginas. [Código](./infojobs.py#L30).

2. Se busca la palabra clave en una página [Código](./infojobs.py#L47).


3. Al usar un navegador con un perfil recién creado, suele pedirnos que aceptemos las cookies de la página. [Código](./infojobs.py#L63).
    

4. Cuando la página de resultados ha cargado, en el caso de InfoJobs, es necesario bajar hasta el final de la página para que todas las posiciones se rendericen y aparezcan en el DOM. [Código](./infojobs.py#L80).
   
    
5. Analiza las posiciones de la página de resultados. Extrae el link de cada oferta, lo abre en un driver nuevo, y extrae la información. Por último lo escribe en el CSV y cierra el driver auxiliar. [Código](./infojobs.py#L113).

   

## 📝 Notas

- Se usan expresiones regulares para extraer la experiencia y el salario de las descripciones de las ofertas.

- Después de que el driver clickee sobre algún elemento, se espera 1 segundo a que el navegador lo procese.

- En caso de que una acción cargue una página, se esperan 5 segundos o se espera a la aparición de un elemento concreto.
  


## 🐞 Problemas encontrados

- Cuando se abría una oferta en una nueva pestaña dentro del driver donde están los resultados, después de 10-15 ofertas InfoJobs muestra un captcha. Se ha optado por abrir un nuevo driver en vez de una nueva pestaña.

- Después de buscar varias veces (no hay un número exacto) acaba mostrando un captcha.



    En ese caso la [excepción](./infojobs.py#L43) que salta se controla desde el método buscar. En mi caso, para volver a lanzar el script estoy usando una VPN para cambiar de ip cada vez que aparece y funciona sin problemas.
