# Portal Monster

Hereda de la clase [Portal](https://github.com/VicMoraGit/TFG_ofertas_trabajo/blob/main/portales/portal.py)

## ✅ Pasos 

1. Abre la página [https://www.monster.es/](https://www.monster.es/) y recorre las posiciones de cada pagina. [Código](https://github.com/VicMoraGit/TFG_ofertas_trabajo/blob/main/portales/monster/monster.py#L32).

   
2. Se busca la palabra clave en una página [Código](https://github.com/VicMoraGit/TFG_ofertas_trabajo/blob/main/portales/monster/monster.py#L73).

3. Se analizan las ofertas. En caso de que el titulo de la ultima oferta de la ultima pagina analizada coincida con el titulo de la ultima oferta de la pagina actual, se finaliza la busqueda.  [Código](https://github.com/VicMoraGit/TFG_ofertas_trabajo/blob/main/portales/monster/monster.py#L94).

4. Mientras se analizan todas las ofertas, se van rellenando las estadisticas.
   
   
## 📊 Analisis del portal

- Se muestran 9 ofertas por cada pagina de resultados.
- El salario, la experiencia y los requerimientos hay que extraerlos desde la descripcion de la oferta.
- Este portal no presenta ningun metodo de bloqueo contra bots. Por lo tanto, con una instancia del driver se puede obtener toda la informacion sin bloqueos.
- El rendimiento del script es mas bajo que en los otros portales, ya que las ofertas por pagina son muy pocas (9) y hay que estar navegando a cada pagina y esperar a que cargue.
  
- El formato de la fecha de publicacion de la oferta tambien difiere bastante de unas a otras. Nos podemos encontrar 3 tipos de fechas: 
    - Recien publicado, Hoy,
    - Hace "x" dias
    - Hace "x" horas
    - Hace +30 dias

    Para ello se aplica otro filtro de fechas, y se devuelve en formato DD-MM-YYYY
    
## 🧪 Pruebas

Para comprobar el rendimiento y la robustez del script, se ha hecho la siguiente prueba: 

> Keywords =  Big Data, Desarrollo Web, Backend, Microservicios
> 
> Numero de paginas = 50

Arrojando [este csv](https://github.com/VicMoraGit/TFG_ofertas_trabajo/blob/main/data/CSV/Monster.csv) y las siguientes estadisticas:
 
|   |   |
|---|---|    
|Ofertas analizadas      | 796        
|Ofertas con salario     | 28
|Ofertas con experiencia | 487 
|Tiempo                  | 33.56 mins.

## 📝 Notas

- Se usan expresiones regulares para extraer la experiencia, el salario y los requerimientos de las descripciones de las ofertas.

## 🐞 Problemas encontrados

- Ninguno