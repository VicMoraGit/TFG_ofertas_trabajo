# Portal Tecnoempleo

Hereda de la clase [Portal](https://github.com/VicMoraGit/TFG_ofertas_trabajo/blob/main/portales/portal.py)

## ✅ Pasos 

1. Abre la página [https://www.tecnoempleo.com/](https://www.tecnoempleo.com/) y recorre las posiciones de cada pagina. [Código](https://github.com/VicMoraGit/TFG_ofertas_trabajo/blob/main/portales/tecnoempleo/tecnoempleo.py#L30).

   
2. Se busca la palabra clave en una página [Código](https://github.com/VicMoraGit/TFG_ofertas_trabajo/blob/main/portales/tecnoempleo/tecnoempleo.py#L45).


3. Se analizan las ofertas. En caso de que el titulo de la ultima oferta de la ultima pagina analizada coincida con el titulo de la ultima oferta de la pagina actual, se finaliza la busqueda.  [Código](https://github.com/VicMoraGit/TFG_ofertas_trabajo/blob/main/portales/tecnoempleo/tecnoempleo.py#L63).

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

Arrojando [este csv](https://github.com/VicMoraGit/TFG_ofertas_trabajo/blob/main/data/CSV/Tecnoempleo.csv) y las siguientes estadisticas:
 
|   |   |
|---|---|    
|Ofertas analizadas      | 896        
|Ofertas con salario     | 334
|Ofertas con experiencia | 850 
|Tiempo                  | 15.59 mins.

## 📝 Notas

- Se usan expresiones regulares para extraer la experiencia, el salario y los requerimientos de las descripciones de las ofertas.

## 🐞 Problemas encontrados

- Ninguno
