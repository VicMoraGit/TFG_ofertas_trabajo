# Portal Indeed

Hereda de la clase [Portal](https://github.com/VicMoraGit/TFG_ofertas_trabajo/blob/main/portales/portal.py)

## ✅ Pasos 

1. Abre la página [es.indeed.com](https://es.indeed.com/) y recorre las posiciones del total de páginas. [Código](https://github.com/VicMoraGit/TFG_ofertas_trabajo/blob/main/portales/indeed/indeed.py#31).

    Se usan dos variables de control, en caso de que haya algun error si la busqueda no esta finalizada, se vuelve a buscar a partir de la ultima pagina finalizada.

    ```python
    
        self._busqueda_finalizada = False
        self._n_paginas_analizadas = 0

    ```
   
2. Se busca la palabra clave en una página [Código](https://github.com/VicMoraGit/TFG_ofertas_trabajo/blob/main/portales/indeed/indeed.py#L66).

3. Se analizan las ofertas. En caso de que el titulo de la ultima oferta de la ultima pagina analizada coincida con el titulo de la ultima oferta de la pagina actual, se finaliza la busqueda.  [Código](https://github.com/VicMoraGit/TFG_ofertas_trabajo/blob/main/portales/indeed/indeed.py#L87).

4. Mientras se analizan todas las ofertas, se van rellenando las estadisticas.

## 📊 Analisis del portal

- Se muestran 15 ofertas por cada pagina de resultados.
- La localizacion de la oferta no esta "regulada" por el propio portal, por lo tanto se presentan diferentes problemas:

    | Problema               | Ejemplo                  
    | ---                    | ---                      
    | Diferente formato      | Palma de Mallorca, Palma, palma
    | Idioma                 | Alicante, Alacant
    | Codigos postales       | 28045 Madrid
    | Teletrabajo in "?"     | Teletrabajo in 28020 Madrid
    | Municipio              | San-Sebastian, Marbella, Tres Cantos
    La solucion aportada es la siguiente: 
    
    - Se ha generado un filtro de provincias españolas validas y sus posibles variantes (idioma, formatos)
    - Si existe la palabra teletrabajo o remoto, se marca exclusivamente como "Teletrabajo"
  

- El formato de la fecha de publicacion de la oferta tambien difiere bastante de unas a otras. Nos podemos encontrar 3 tipos de fechas: 
    - Recien publicado, Hoy,
    - Hace "x" dias
    - Hace "x" horas
    - Hace +30 dias

    Para ello se aplica otro filtro de fechas, y se devuelve en formato DD-MM-YYYY
- Indeed muestra los datos de salarios, experiencia y requerimientos dentro de las descripciones de las ofertas. Para acceder a esas descripciones, hay que clickar sobre las ofertas de la pagina de resultados. Detalles a tener en cuenta:
  - El tamaño de la ventana del driver tiene que ser lo suficientemente amplio como para permitir que las descripciones se muestren embebidas dentro de la pagina de resultados.
  - Si se abren muchas descripciones de esta manera, nos detecta como bot y se abren en una ventana nueva. Para ello se usa un [nuevo driver](https://github.com/VicMoraGit/TFG_ofertas_trabajo/blob/main/portales/indeed/indeed.py#L42) por pagina de resultados.
  - Nos interesa obtener la descripcion embebida en la pagina de resultados para ahorrar tiempo.

## 🧪 Pruebas

Para comprobar el rendimiento y la robustez del script, se ha hecho la siguiente prueba: 

> Keywords =  Big Data, Desarrollo Web, Backend, Microservicios
> 
> Numero de paginas = 50

Arrojando [este csv](https://github.com/VicMoraGit/TFG_ofertas_trabajo/blob/main/data/CSV/Indeed.csv) y las siguientes estadisticas:
 
|   |   |
|---|---|    
|Ofertas analizadas      | 2280        
|Ofertas con salario     | 418
|Ofertas con experiencia | 276 
|Tiempo                  | 95.42 mins.

## 📝 Notas

- Se usan expresiones regulares para extraer la experiencia, el salario y los requerimientos de las descripciones de las ofertas.

- Algunas skills tienen caracteres que se usan para definir reglas en las expresiones regulares, por lo que se han escapado con [re.escape()](https://github.com/VicMoraGit/TFG_ofertas_trabajo/blob/main/portales/indeed/indeed.py#L198)

## 🐞 Problemas encontrados

- A veces el script devuelve ofertas que no contienen ningún link, es por eso que se [comprueba si el link esta vacío](https://github.com/VicMoraGit/TFG_ofertas_trabajo/blob/main/portales/indeed/indeed.py#L80) antes de abrir la oferta en una pestaña. Puede ser porque haya presencia de publicidad, y detecte esa publicidad como una oferta.

