import logging
from time import time

from util.csvHandler import csvHandler
import util.stats as stats

from portales.tecnoempleo.tecnoempleo import Tecnoempleo
#from portales.infojobs.infojobs import InfoJobs
from portales.indeed.indeed import Indeed
from portales.monster.monster import Monster

from portales.portal import Portal

# Visualizacion de datos
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter 


raw_csv_file=open("data/CSV/Tecnoempleo.csv", 'r', encoding="UTF-8", newline="")

df=pd.read_csv(raw_csv_file)

df.drop(df[df['Experiencia'] == "Sin informacion"].index, inplace = True)

años_experiencia=df['Experiencia']

print(años_experiencia)
Counter = Counter(años_experiencia) 
most_occur = Counter.most_common(10) 


fig = plt.figure(figsize = (10, 10)) 
experiencia = pd.DataFrame(Counter.most_common(6) ,
                             columns=['experiencia', 'count'])
print(experiencia)
# creating the bar plot 
plt.bar(experiencia['experiencia'], experiencia['count'], color ='maroon',  
        width = 0.4) 
  
plt.xlabel("Años") 
plt.ylabel("Cantidad") 
plt.title("Experiencia media Tecnoempleo") 
plt.savefig('TecnoempleoExperiencia.png')


if __name__ == "__main__":
    
    # Configuracion logger
    # logging.basicConfig(level=logging.INFO)
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger("main")
    log.setLevel(logging.DEBUG)

    # Clase encargada del csv
    csvh = csvHandler()
    # Declaracion variables
    portales:list[Portal] = []
    keywords = ["Big Data", "Desarrollo Web", "Backend", "Microservicios"]
    n_paginas = 50
    
    # infoJobs:InfoJobs = InfoJobs(
    #     driver=driver,
    #     n_paginas=n_paginas,
    #     csvHandler=csvh)

    portales.append(Indeed(n_paginas=n_paginas,csvHandler=csvh))
    portales.append(Tecnoempleo(n_paginas=n_paginas,csvHandler=csvh))
    portales.append(Monster(n_paginas=n_paginas,csvHandler=csvh))

    stats.s_inicio = time()
    for portal in portales:

        portal._iniciar_cronometro()
        
        for keyword in keywords:
                
            log.info(f"Buscando {keyword} en {portal.__class__.__name__}")
            portal.buscar(keyword)
        
        portal.actualizar_estadisticas()

    csvh.cerrar_archivo()
    stats.s_final = time()
    stats.imprime_stats()
    stats.exporta_stats()