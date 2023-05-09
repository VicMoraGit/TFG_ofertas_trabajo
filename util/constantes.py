# Filtros español - ingles
from util.enums.categorias_enum import Categoria
from util.enums.subcategorias_enums import SubFramework


FILTRO_HORAS = ["horas", "hora", "hour", "hours"]
FILTRO_DIAS = ["dias", "dia", "day", "days"]
FILTRO_MESES = ["meses", "mes", "month", "months"]
FILTRO_FECHAS = ["nueva", "actualizada", "reciente"]

PALABRAS_RELACIONADAS_ROL = [
    {  # 0
        "practicas": 1,
        "beca": 1,
        "pasante": 1,
        "interno": 1,
        "pasantia": 1,
        "programa": 1,
    },  # No importan los valores en esta lista
    {
        "administrador": 5,
        "administradores": 5,
        "seguridad": 5,
        "gestor": 2,
        "gestores": 2,
        "responsable": 2,
        "responsables": 2,
    },  # 1
    {  # 2
        "analista": 5,
        "analistas": 5,
        "software": 5,
        "programacion": 5,
        "analizador": 5,
        "analizadores": 5,
        "requisitos": 2,
        "aplicaciones": 3,
    },
    {
        "programador": 5,
        "programadores": 5,
        "desarrollador": 5,
        "desarrolladores": 5,
        "backend": 5,
        "web": 2,
        "back-end": 5,
    },  # 3
    {
        "ingeniero": 5,
        "ingenieros": 5,
        "integracion": 5,
        "sistemas": 2,
        "software": 2,
    },  # 4
    {  # 5
        "seo": 5,
        "experto": 5,
        "expertos": 5,
        "optimizador": 5,
        "especialista": 5,
        "motores": 2,
        "busqueda": 3,
        "motor": 2,
        "optimizacion": 5,
    },
    {  # 6
        "programador": 5,
        "programadores": 5,
        "desarrollador": 5,
        "desarrolladores": 5,
        "frontend": 5,
        "web": 2,
        "front-end": 5,
        "frontal": 4,
        "frontales": 4,
    },
    {  # 7
        "especialista": 5,
        "forense": 5,
        "forenses": 5,
        "informatica": 2,
        "analisis": 3,
        "digital": 1,
        "computo": 1,
        "computacion": 1,
    },
    {  # 8
        "ingeniero": 5,
        "ingenieros": 5,
        "seguridad": 5,
        "ciberseguridad": 5,
        "consultor": 5,
        "consultores": 5,
        "asesoramiento": 1,
    },
    {
        "disenador": 5,
        "disenadores": 5,
        "sistemas": 2,
        "embebidos": 4,
        "empotrados": 3,
        "incrustados": 3,
    },  # 9
    {"agente": 5, "servicio": 3, "asistencia": 5, "apoyo": 2, "tecnico": 3},  # 10
    {"probador": 5, "software": 5, "tester": 5, "comprobador": 5, "evaluador": 5},  # 11
    {  # 12
        "ingeniero": 5,
        "ingenieros": 5,
        "vision": 5,
        "computerizada": 4,
        "artificial": 2,
        "especialista": 4,
        "cv": 3,
    },
    {  # 13
        "ingeniero": 5,
        "ingenieros": 5,
        "especialista": 5,
        "seguridad": 4,
        "ciberseguridad": 4,
        "sistemas": 1,
        "embebidos": 1,
        "IoT": 2,
        "internet": 1,
        "cosas": 1,
        "cibernetica": 3,
        "empotrados": 1,
        "incrustados": 1,
    },
    {
        "analista": 5,
        "analizador": 5,
        "analizadores": 5,
        "analistas": 5,
        "calidad": 5,
        "QA": 5,
        "control": 2,
    },  # 14
    {  # 15
        "programador": 5,
        "programadores": 5,
        "desarrollador": 5,
        "desarrolladores": 5,
        "blockchain": 5,
        "cadena": 3,
        "bloques": 2,
        "DLT": 4,
        "ingeniero": 5,
        "ingenieros": 5,
    },
    {  # 16
        "cientifico": 5,
        "datos": 5,
    },
    {
        "analista": 5,
        "analizador": 5,
        "analizadores": 5,
        "analistas": 5,
        "negocios": 5,
        "empresarial": 4,
        "tic": 1,
    },  # 17
    {  # 18
        "ingeniero": 5,
        "ingenieros": 5,
        "arquitectura": 4,
        "empresarial": 4,
        "especialista": 5,
        "gestor": 2,
        "gestores": 2,
    },
    {  # 19
        "programador": 5,
        "programadores": 5,
        "desarrollador": 5,
        "desarrolladores": 5,
        "aplicaciones": 3,
        "apps": 5,
        "moviles": 3,
        "movil": 3,
    },
    {  # 20
        "probador": 5,
        "tester": 5,
        "videojuegos": 5,
        "juegos": 3,
        "digitales": 2,
        "comprobador": 5,
        "evaluador": 5,
    },
    {  # 21
        "ingeniero": 5,
        "ingenieros": 5,
        "nube": 5,
        "sistemas": 2,
        "devops": 4,
        "programador": 5,
        "programadores": 5,
        "desarrollador": 5,
        "desarrolladores": 5,
        "seguridad": 1,
        "infraestructura": 1,
        "arquitecto": 4,
        "arquitectos": 4,
        "redes": 2,
    },
    {  # 22
        "disenador": 5,
        "disenadores": 5,
        "ingeniero": 5,
        "ingenieros": 5,
        "sistemas": 2,
        "inteligentes": 3,
        "ia": 4,
        "ai": 4,
        "inteligencia": 3,
        "artificial": 3,
    },
    {"tecnico": 5, "tic": 2, "informatico": 3, "ti": 2, "oficial": 3},  # 23
    {  # 24
        "analista": 5,
        "analizador": 5,
        "analizadores": 5,
        "analistas": 5,
        "experiencia": 4,
        "usuario": 3,
        "ux": 5,
        "usabilidad": 3,
        "experto": 5,
        "expertos": 5,
    },
    {  # 25
        "programador": 6,
        "programadores": 6,
        "desarrollador": 6,
        "desarrolladores": 6,
        "software": 5,
        "consultor": 6,
        "consultores": 6,
        "ingeniero": 5,
        "ingenieros": 5,
        "aplicaciones": 2,
        "soluciones": 3,
    },
    {"probador": 5, "comprobador": 5, "evaluador": 5, "accesibilidad": 5},  # 26
    {  # 27
        "programador": 5,
        "programadores": 5,
        "desarrollador": 5,
        "desarrolladores": 5,
        "software": 3,
        "ingeniero": 5,
        "ingenieros": 5,
        "sistemas": 3,
        "embebidos": 3,
        "incrustados": 3,
        "empotrados": 3,
    },
    {"tecnico": 5, "redes": 5, "especialista": 5, "mantenimiento": 1},  # 28
    {"consultor": 5, "consultores": 5, "investigacion": 3},  # 29
    {  # 30
        "tester": 5,
        "pruebas": 1,
        "probador": 5,
        "comprobador": 5,
        "evaluador": 5,
        "integracion": 5,
    },
    {
        "arquitecto": 5,
        "arquitectos": 5,
        "sistemas": 5,
        "soluciones": 2,
        "informacion": 1,
    },  # 31
    {  # 32
        "hacker": 5,
        "etico": 5,
        "analista": 5,
        "analizador": 5,
        "analizadores": 5,
        "analistas": 5,
        "vulnerabilidad": 4,
        "vulnerabilidades": 4,
        "pirata": 3,
        "probador": 3,
        "seguridad": 2,
        "tester": 3,
        "evaluador": 3,
        "comprobador": 3,
    },
    {  # 33
        "administrador": 5,
        "administradores": 5,
        "web": 5,
        "webs": 5,
        "maestro": 5,
        "master": 5,
        "webmaster": 5,
    },
    {  # 34
        "arquitecto": 5,
        "arquitectos": 5,
        "blockchain": 5,
        "cadena": 3,
        "bloques": 2,
    },
    {  # 35
        "ingeniero": 5,
        "ingenieros": 5,
        "conocimiento": 5,
        "tecnologias": 3,
        "semanticas": 3,
        "conocimientos": 4,
    },
    {
        "analista": 5,
        "analizadores": 5,
        "ingeniero": 5,
        "ingenieros": 5,
        "datos": 5,
        "analistas": 5,
        "analizador": 5,
    },  # 36
    {  # 37
        "ingeniero": 5,
        "ingenieros": 5,
        "redes": 5,
        "programador": 5,
        "programadores": 5,
        "desarrollador": 5,
        "desarrolladores": 5,
        "configurador": 4,
        "red": 4,
    },
    {  # 38
        "administrador": 5,
        "administradores": 5,
        "base": 5,
        "bases": 5,
        "datos": 4,
        "gestor": 5,
        "gestores": 5,
        "configurador": 4,
        "bd": 3,
        "bbdd": 3,
        "db": 3,
    },
    {  # 39
        "disenador": 5,
        "disenadores": 5,
        "base": 5,
        "bases": 5,
        "datos": 4,
        "arquitecto": 5,
        "arquitectos": 5,
        "bd": 3,
        "bbdd": 3,
        "db": 3,
    },
    {  # 40
        "disenador": 5,
        "disenadores": 5,
        "accesibilidad": 4,
        "iu": 4,
        "ui": 4,
        "interfaces": 3,
        "usuario": 2,
        "usabilidad": 3,
    },
    {"administrador": 5, "administradores": 5, "sistemas": 5},  # 41
    {  # 42
        "desarrollador": 5,
        "desarrolladores": 5,
        "programador": 5,
        "programadores": 5,
        "videojuegos": 5,
        "juegos": 3,
        "digitales": 2,
    },
    {"auditor": 5, "auditores": 5, "informatico": 3, "auditoria": 5},  # 43
    {"tecnico": 5, "seguridad": 5, "especialista": 5},  # 44
    {
        "analista": 5,
        "analistas": 5,
        "sistemas": 5,
        "analizadores": 5,
        "analizador": 5,
    },  # 45
    {  # 46
        "administrador": 5,
        "administradores": 5,
        "responsable": 5,
        "responsables": 5,
        "contenidos": 3,
        "web": 3,
        "redactor": 3,
        "digitales": 3,
    },
    {
        "desarrollador": 5,
        "desarrolladores": 5,
        "sistemas": 5,
        "programadores": 5,
        "programador": 5,
    },  # 47
    {  # 48
        "desarrollador": 5,
        "desarrolladores": 5,
        "base": 5,
        "bases": 5,
        "datos": 4,
        "programador": 5,
        "programadores": 5,
        "bd": 3,
        "bbdd": 3,
        "db": 3,
    },
    {
        "desarrollador": 5,
        "desarrolladores": 5,
        "programador": 5,
        "programadores": 5,
        "web": 5,
        "fullstack": 5,
        "full-stack": 5,
    },  # 49
    {"consultor": 5, "consultores": 5, "integracion": 5, "sistemas": 3},  # 50
    {
        "desarrollador": 5,
        "desarrolladores": 5,
        "programador": 5,
        "programadores": 5,
        "aplicaciones": 4,
        "escritorio": 4,
    },  # 51
]
PROVINCIAS_NORMALIZADAS = {
    "la coruña": "La Coruña",
    "a coruña": "La Coruña",
    "alacant": "Alicante",
    "alicante": "Alicante",
    "albacete": "Albacete",
    "almeria": "Almería",
    "araba": "Álava",
    "alava": "Álava",
    "asturias": "Asturias",
    "avila": "Ávila",
    "badajoz": "Badajoz",
    "barcelona": "Barcelona",
    "bizkaia": "Vizcaya",
    "vizcaya": "Vizcaya",
    "burgos": "Burgos",
    "caceres": "Cáceres",
    "cadiz": "Cádiz",
    "cantabria": "Cantabria",
    "castello": "Castellón",
    "castellón": "Castellón",
    "ceuta": "Ceuta",
    "ciudad Real": "Ciudad Real",
    "cordoba": "Córdoba",
    "cuenca": "Cuenca",
    "gipuzcoa": "Guipúzcoa",
    "gipuzkoa": "Guipúzcoa",
    "guipuzcoa": "Guipúzcoa",
    "girona": "Gerona",
    "gerona": "Gerona",
    "granada": "Granada",
    "guadalajara": "Guadalajara",
    "huelva": "Huelva",
    "huesca": "Huesca",
    "illes balears": "Islas Baleares",
    "islas baleares": "Islas Baleares",
    "jaen": "Jaén",
    "la rioja": "La Rioja",
    "las palmas": "Las Palmas",
    "leon": "León",
    "lerida": "Lérida",
    "lleida": "Lérida",
    "lugo": "Lugo",
    "madrid": "Madrid",
    "mad": "Madrid",
    "malaga": "Málaga",
    "melilla": "Melilla",
    "murcia": "Murcia",
    "navarra": "Navarra",
    "ourense": "Orense",
    "orense": "Orense",
    "palencia": "Palencia",
    "pontevedra": "Pontevedra",
    "santa cruz de tenerife": "Santa Cruz de Tenerife",
    "segovia": "Segovia",
    "sevilla": "Sevilla",
    "soria": "Soria",
    "tarragona": "Tarragona",
    "teruel": "Teruel",
    "toledo": "Toledo",
    "valencia": "Valencia",
    "valladolid": "Valladolid",
    "zamora": "Zamora",
    "zaragoza": "Zaragoza",
    "teletrabajo": "Teletrabajo",
    "tele trabajo": "Teletrabajo",
    "remoto": "Teletrabajo",
}
PROVINCIAS_COMUNIDADES = {
    "Álava": "País Vasco",
    "Albacete": "Castilla-La Mancha",
    "Alicante": "Comunidad Valenciana",
    "Almería": "Andalucía",
    "Asturias": "Principado de Asturias",
    "Ávila": "Castilla y León",
    "Badajoz": "Extremadura",
    "Barcelona": "Cataluña",
    "Burgos": "Castilla y León",
    "Cáceres": "Extremadura",
    "Cádiz": "Andalucía",
    "Cantabria": "Cantabria",
    "Castellón": "Comunidad Valenciana",
    "Ceuta": "Ceuta",
    "Ciudad Real": "Castilla-La Mancha",
    "Córdoba": "Andalucía",
    "La Coruña": "Galicia",
    "Cuenca": "Castilla-La Mancha",
    "Gerona": "Cataluña",
    "Granada": "Andalucía",
    "Guadalajara": "Castilla-La Mancha",
    "Guipúzcoa": "País Vasco",
    "Huelva": "Andalucía",
    "Huesca": "Aragón",
    "Islas Baleares": "Islas Baleares",
    "Jaén": "Andalucía",
    "León": "Castilla y León",
    "Lérida": "Cataluña",
    "Lugo": "Galicia",
    "Madrid": "Comunidad de Madrid",
    "Málaga": "Andalucía",
    "Melilla": "Melilla",
    "Murcia": "Región de Murcia",
    "Navarra": "Navarra",
    "Orense": "Galicia",
    "Palencia": "Castilla y León",
    "Las Palmas": "Islas Canarias",
    "Pontevedra": "Galicia",
    "La Rioja": "La Rioja",
    "Salamanca": "Castilla y León",
    "Segovia": "Castilla y León",
    "Sevilla": "Andalucía",
    "Soria": "Castilla y León",
    "Tarragona": "Cataluña",
    "Santa Cruz de Tenerife": "Islas Canarias",
    "Teruel": "Aragón",
    "Toledo": "Castilla-La Mancha",
    "Valencia": "Comunidad Valenciana",
    "Valladolid": "Castilla y León",
    "Vizcaya": "País Vasco",
    "Zamora": "Castilla y León",
    "Zaragoza": "Aragón",
    "Teletrabajo": "Teletrabajo",
}
ALL_SKILLS = {
    [
        "Aurelia",
        "Framework de JavaScript para aplicaciones de navegador, moviles y de escritorio",
        "https://aurelia.io/docs",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "Emberjs",
        "Framework de JavaScript para aplicaciones de navegador",
        "https://guides.emberjs.com/release/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "Ember",
        "Framework de JavaScript para aplicaciones de navegador",
        "https://guides.emberjs.com/release/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "Nightwatchjs",
        "Framework de JavaScript para realizar tests end-to-end(E2E) en aplicaciones y sitios web.",
        "https://nightwatchjs.org/",
        Categoria.FRAMEWORK,SubFramework.TEST
    ],
    [
        "Nightwatch",
        "Framework de JavaScript para realizar tests end-to-end(E2E) en aplicaciones y sitios web.",
        "https://nightwatchjs.org/",
        Categoria.FRAMEWORK,SubFramework.TEST
    ],
    [
        "FBT",
        "Framework de JavaScript desarrollado por Facebook para internalización de interfaces de usuario",
        "https://facebookincubator.github.io/fbt/",
        Categoria.FRAMEWORK,SubFramework.INTERNACIONALIZACION
    ],
    [
        "Alpinejs",
        "Framework de JavaScript muy ligera para web",
        "https://alpinejs.dev/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "Alpine",
        "Framework de JavaScript muy ligera para web",
        "https://alpinejs.dev/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "Stimulus",
        "Framework de JavaScript sencillo y modesto",
        "https://stimulus.hotwired.dev/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "NativeScript",
        "Framework de JavaScript para aplicaciones nativas en iOS o Android"
        "https://docs.nativescript.org/",
        Categoria.FRAMEWORK,SubFramework.MOVIL
    ],
    [
        "Relay",
        "Libreria de JavaScript para el framework React para gestion de datos en GraphQL",
        "https://relay.dev/docs/",
        Categoria.LIBRERIA,
    ],
    [
        "Cyclejs",
        "Framework para aplicaciones web funcionales",
        "https://cycle.js.org/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "Cycle",
        "Framework para aplicaciones web funcionales",
        "https://cycle.js.org/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "Babylonjs",
        "Motor de juegos en 3D basado en web",
        "https://doc.babylonjs.com/",
        Categoria.FRAMEWORK,SubFramework.GAME
    ],
    [
        "Babylon",
        "Motor de juegos en 3D basado en web",
        "https://doc.babylonjs.com/",
        Categoria.FRAMEWORK,SubFramework.GAME
    ],
    [
        "Flight",
        "Framework minimalista para aplicaciones web por Twitter",
        "https://flightjs.github.io/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "Flightjs",
        "Framework minimalista para aplicaciones web por Twitter",
        "https://flightjs.github.io/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "Onsen UI",
        "Framework de interfaz de usuario para aplicaciones móviles híbridas",
        "https://onsen.io/v2/docs/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "Cylonjs",
        "Framework de robótica y automatización basada en JavaScript",
        "https://cylonjs.com/documentation/",
        Categoria.FRAMEWORK,SubFramework.ROBOTICA
    ],
    [
        "Cylon",
        "Framework de robótica y automatización basada en JavaScript",
        "https://cylonjs.com/documentation/",
        Categoria.FRAMEWORK,SubFramework.ROBOTICA
    ],
    [
        "Jest",
        "Framework de pruebas de JavaScript",
        "https://jestjs.io/docs/en/getting-started",
        Categoria.FRAMEWORK,SubFramework.TEST
    ],
    [
        "Feathers",
        "Framework de aplicaciones web en tiempo real y API RESTful para Node.js",
        "https://docs.feathersjs.com/",
        Categoria.FRAMEWORK,SubFramework.FULLSTACK
    ],
    [
        "Feathersjs",
        "Framework de aplicaciones web en tiempo real y API RESTful para Node.js",
        "https://docs.feathersjs.com/",
        Categoria.FRAMEWORK,SubFramework.FULLSTACK
    ],
    [
        "AVA",
        "Framework de pruebas de JavaScript que se ejecuta en paralelo para una ejecución más rápida",
        "https://github.com/avajs",
        Categoria.FRAMEWORK,SubFramework.TEST
    ],
    [
        "Bootboxjs",
        "biblioteca de JavaScript que proporciona cuadros de diálogo y modales para su uso en aplicaciones web",
        "http://bootboxjs.com/documentation.html",
        Categoria.LIBRERIA,
    ],
    [
        "Bootbox",
        "biblioteca de JavaScript que proporciona cuadros de diálogo y modales para su uso en aplicaciones web",
        "http://bootboxjs.com/documentation.html",
        Categoria.LIBRERIA,
    ],
    [
        "HighchartsJS",
        "biblioteca de gráficos interactivos en JavaScript que permite la creación de visualizaciones de datos sofisticadas y personalizables en aplicaciones web",
        "https://www.highcharts.com/docs/index",
        Categoria.LIBRERIA,
    ],
    [
        "PrimeUI",
        "colección de componentes de interfaz de usuario de código abierto para aplicaciones web, construidos sobre la biblioteca de JavaScript PrimeFaces",
        "https://www.primefaces.org/primeui/",
        Categoria.LIBRERIA,
    ],
    [
        "Highcharts",
        "biblioteca de gráficos interactivos en JavaScript que permite la creación de visualizaciones de datos sofisticadas y personalizables en aplicaciones web",
        "https://www.highcharts.com/docs/index",
        Categoria.LIBRERIA,
    ],
    [
        "Scripty2",
        "biblioteca de animación de JavaScript que permite crear animaciones y efectos visuales dinámicos en páginas web",
        "https://github.com/madrobby/scripty2",
        Categoria.LIBRERIA,
    ],
    [
        "Crafty",
        "Biblioteca de JavaScript para la creación de videojuegos HTML5 y aplicaciones interactivas"
        "https://craftyjs.com/docs/",
        Categoria.LIBRERIA,
    ],
    [
        "Modernizr",
        "Biblioteca de detección de características de HTML, CSS y JavaScript en el navegador del usuario, permitiendo que los desarrolladores adapten el contenido y las características de la aplicación según la compatibilidad con el navegador",
        "https://modernizr.com/docs",
        Categoria.LIBRERIA,
    ],
    [
        "T3",
        "Sistema de gestión de contenidos de código abierto basado en PHP, utilizado para construir sitios web y aplicaciones web empresariales de alta complejidad",
        "https://typo3.org/documentation/",
        Categoria.SOFTWARE,
    ],
    [
        "Typo3",
        "Sistema de gestión de contenidos de código abierto basado en PHP, utilizado para construir sitios web y aplicaciones web empresariales de alta complejidad",
        "https://typo3.org/documentation/",
        Categoria.SOFTWARE,
    ],
    [
        "Cubejs",
        "Herramienta de código abierto que permite la creación de aplicaciones analíticas y de inteligencia empresarial con Node.js y bases de datos analíticas como PostgreSQL, MySQL, y Google BigQuery",
        "https://cube.dev/docs/",
        Categoria.MIDDLEWARE,
    ],
    [
        "Cube",
        "Herramienta de código abierto que permite la creación de aplicaciones analíticas y de inteligencia empresarial con Node.js y bases de datos analíticas como PostgreSQL, MySQL, y Google BigQuery",
        "https://cube.dev/docs/",
        Categoria.MIDDLEWARE,
    ],
    [
        "RequireJS",
        "Biblioteca de JavaScript que permite la carga de módulos de manera asíncrona, mejorando la eficiencia y el rendimiento de las aplicaciones web",
        "https://requirejs.org/docs/start.html",
        Categoria.LIBRERIA,
    ],
    [
        "Zepto",
        "biblioteca de JavaScript para aplicaciones web móviles, similar a jQuery pero de tamaño reducido y mejor rendimiento en dispositivos móviles",
        "https://zeptojs.com/",
        Categoria.LIBRERIA,
    ],
    [
        "Jasmine",
        "Framework de pruebas de JavaScript que se utiliza para realizar pruebas de comportamiento y unitarias en aplicaciones web",
        "https://jasmine.github.io/tutorials/your_first_suite",
        Categoria.FRAMEWORK,SubFramework.TEST
    ],
    [
        "Jasminejs",
        "Framework de pruebas de JavaScript que se utiliza para realizar pruebas de comportamiento y unitarias en aplicaciones web",
        "https://jasmine.github.io/tutorials/your_first_suite",
        Categoria.FRAMEWORK,SubFramework.TEST
    ],
    [
        "QUnit",
        "Framework de pruebas unitarias de JavaScript desarrollado por jQuery, utilizado para realizar pruebas en aplicaciones web",
        "https://qunitjs.com/intro/",
        Categoria.FRAMEWORK,SubFramework.TEST
    ],
    [
        "Mocha",
        "Framework de pruebas de JavaScript que se utiliza para realizar pruebas unitarias, de integración y de extremo a extremo en aplicaciones web y Node.js",
        "https://mochajs.org/#getting-started",
        Categoria.FRAMEWORK,SubFramework.TEST
    ],
    [
        "sketchjs",
        "biblioteca de JavaScript que permite la creación de gráficos vectoriales y animaciones en aplicaciones web utilizando HTML5 canvas",
        "https://github.com/intridea/sketch.js",
        Categoria.LIBRERIA,
    ],
    [
        "Mithril",
        "Framework de JavaScript de código abierto para la creación de aplicaciones web de una sola página (SPA), que utiliza una sintaxis simple y concisa para la creación de componentes y la manipulación del DOM",
        "https://mithril.js.org/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "Enact",
        "Framework de código abierto basado en React para el desarrollo de aplicaciones de TV",
        "https://enactjs.com/docs/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "ZK",
        "Framework de desarrollo de aplicaciones web de código abierto en Java que permite la creación de aplicaciones web en tiempo real con una interfaz de usuario rica y una arquitectura de procesamiento en el lado del servidor",
        "https://www.zkoss.org/documentation/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "Qooxdoo",
        "Framework de código abierto de JavaScript que se utiliza para crear aplicaciones web ricas en características y escalables, utilizando una arquitectura orientada a objetos y una amplia biblioteca de widgets y componentes",
        "https://qooxdoo.org/docs/",
        Categoria.FRAMEWORK,SubFramework.FULLSTACK
    ],
    [
        "Konva",
        "biblioteca de JavaScript de código abierto que se utiliza para crear gráficos vectoriales y animaciones interactivas en aplicaciones web utilizando HTML5 canvas",
        "https://konvajs.org/docs/",
        Categoria.LIBRERIA,
    ],
    [
        "SproutCore",
        "Framework de JavaScript de código abierto que se utiliza para crear aplicaciones web ricas en características, con una interfaz de usuario de alta calidad y una arquitectura de procesamiento en el lado del cliente",
        "https://sproutcore.com/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "Wakanda",
        "plataforma de desarrollo de aplicaciones web de código abierto que permite la creación de aplicaciones web empresariales de alta calidad con una interfaz de usuario rica y una arquitectura de procesamiento en el lado del servidor",
        "https://wakanda.github.io/doc/#/guide?section=introduction",
        Categoria.SOFTWARE,
    ],
    [
        "Webix",
        "Framework de código abierto de JavaScript para la creación de aplicaciones web empresariales con una interfaz de usuario de alta calidad y una amplia biblioteca de widgets y componentes personalizables",
        "https://docs.webix.com/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "Knockout",
        "biblioteca de JavaScript de código abierto que se utiliza para crear interfaces de usuario dinámicas y escalables en aplicaciones web, utilizando el patrón de diseño MVVM para la separación clara de la lógica de la interfaz de usuario y los datos subyacentes",
        "https://knockoutjs.com/documentation/introduction.html",
        Categoria.LIBRERIA,
    ],
    [
        "corMVC",
        "Framework de JavaScript de código abierto para crear aplicaciones web de una sola página utilizando una arquitectura MVC y una sintaxis simple para el enrutamiento y manipulación del DOM",
        "https://github.com/bennadel/CorMVC",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "Lit",
        "biblioteca de JavaScript de código abierto para la creación de componentes web reutilizables y escalables utilizando la sintaxis de plantillas HTML y el enlace de datos bidireccional",
        "https://lit.dev/docs/",
        Categoria.LIBRERIA,
    ],
    [
        "Seemplejs",
        "biblioteca de JavaScript de código abierto para la creación de aplicaciones web escalables y mantenibles. Utiliza el patrón de diseño MVVM y la programación declarativa para la separación clara de la lógica de la interfaz de usuario y los datos subyacentes",
        "https://seemple.js.org/",
        Categoria.LIBRERIA,
    ],
    [
        "Seemple",
        "biblioteca de JavaScript de código abierto para la creación de aplicaciones web escalables y mantenibles. Utiliza el patrón de diseño MVVM y la programación declarativa para la separación clara de la lógica de la interfaz de usuario y los datos subyacentes",
        "https://seemple.js.org/",
        Categoria.LIBRERIA,
    ],
    [
        "Socket.IO",
        "biblioteca de JavaScript que permite la comunicación en tiempo real entre clientes y servidores a través de websockets, con una API fácil de usar para la emisión y recepción de eventos en tiempo real",
        "https://socket.io/docs/v4/index.html",
        Categoria.LIBRERIA,
    ],
    [
        "Meteor",
        "Plataforma de desarrollo web con JavaScript en el cliente y el servidor",
        "https://docs.meteor.com/",
        Categoria.FRAMEWORK,SubFramework.FULLSTACK
    ],
    [
        "Meteorjs",
        "Plataforma de desarrollo web con JavaScript en el cliente y el servidor",
        "https://docs.meteor.com/",
        Categoria.FRAMEWORK,SubFramework.FULLSTACK
    ],
    [
        "ExtJS",
        "Framework JavaScript para la creación de aplicaciones web de alta calidad y ricas en características",
        "https://docs.sencha.com/extjs/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "Ext",
        "Framework JavaScript para la creación de aplicaciones web de alta calidad y ricas en características",
        "https://docs.sencha.com/extjs/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "xstyled",
        "Biblioteca de estilos y temas para React y otras bibliotecas de componentes en JavaScript",
        "https://xstyled.dev/docs",
        Categoria.LIBRERIA,
    ],
    [
        "Opa",
        "Lenguaje de programación web de alto nivel y plataforma de servidor que se utiliza para crear aplicaciones web escalables y seguras con una sintaxis simple y un enfoque en la facilidad de uso",
        "https://opalang.org/",
        Categoria.LENGUAJE,
    ],
    [
        "Vanilla",
        "Framework para javascript multiplataforma y ligero",
        "https://vanilla-js.com/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "Vanillajs",
        "Framework para javascript multiplataforma y ligero",
        "https://vanilla-js.com/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "GWT",
        "conjunto de herramientas de desarrollo de código abierto que permite a los desarrolladores crear y mantener aplicaciones web de alta calidad utilizando Java. GWT compila el código Java en JavaScript optimizado para diferentes navegadores web",
        "http://www.gwtproject.org/",
        Categoria.LIBRERIA,
    ],
    [
        "Ample",
        "biblioteca JavaScript de código abierto que proporciona una plataforma para desarrollar aplicaciones web ricas en funcionalidades",
        "https://www.amplesdk.com/",
        Categoria.LIBRERIA,
    ],
    [
        "MooTools",
        "Conjunto de herramientas JavaScript para desarrollar aplicaciones web interactivas y dinámicas",
        "https://mootools.net/",
        Categoria.FRAMEWORK, SubFramework.FRONTEND
    ],
    [
        "ripplejs",
        "biblioteca de JavaScript que proporciona enrutamiento de URL, bindeos de datos y eventos, y una arquitectura modular para aplicaciones web",
        "https://github.com/ripplejs/ripple",
        Categoria.LIBRERIA,
    ],
    [
        "ripple",
        "biblioteca de JavaScript que proporciona enrutamiento de URL, bindeos de datos y eventos, y una arquitectura modular para aplicaciones web",
        "https://github.com/ripplejs/ripple",
        Categoria.LIBRERIA,
    ],
    [
        "Sailsjs",
        "Framework de aplicaciones web en tiempo real basado en Node.js que proporciona una arquitectura MVC (Modelo Vista Controlador) para la construcción de aplicaciones escalables y fáciles de mantener",
        "https://sailsjs.com/",
        Categoria.FRAMEWORK,SubFramework.BACKEND
    ],
    [
        "Sails",
        "Framework de aplicaciones web en tiempo real basado en Node.js que proporciona una arquitectura MVC (Modelo Vista Controlador) para la construcción de aplicaciones escalables y fáciles de mantener",
        "https://sailsjs.com/",
        Categoria.FRAMEWORK,SubFramework.BACKEND
    ],
    [
        "DHTMLX",
        "Biblioteca para generar XHTML utilizando lenguajes de programación en el lado del servidor, para producir contenido XHTML en tiempo real en lugar de tener archivos HTML estáticos",
        "https://dhtmlx.com/",
        Categoria.LIBRERIA,
    ],
    [
        "Dojo Toolkit",
        "Framework JavaScript de código abierto que proporciona una estructura modular y herramientas para la creación de aplicaciones web complejas y ricas en funcionalidades",
        "https://dojotoolkit.org/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "Echo Framework",
        "Framework para aplicaciones web en Java que proporciona una arquitectura de componentes basada en eventos y un conjunto de herramientas para construir interfaces de usuario dinámicas y responsivas",
        "https://echo.labstack.com/",
        Categoria.FRAMEWORK,SubFramework.BACKEND
    ],
    [
        "Kendo UI",
        "Framework de desarrollo de aplicaciones web que proporciona una amplia variedad de componentes de interfaz de usuario, herramientas de datos y funcionalidades para crear aplicaciones ricas y escalables",
        "https://www.telerik.com/kendo-ui",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "KendoUI",
        "Framework de desarrollo de aplicaciones web que proporciona una amplia variedad de componentes de interfaz de usuario, herramientas de datos y funcionalidades para crear aplicaciones ricas y escalables",
        "https://www.telerik.com/kendo-ui",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "NuclearJS",
        "librería para aplicaciones web que permite gestionar el estado de la aplicación de una manera sencilla y escalable mediante la utilización de un patrón de arquitectura Flux",
        "https://optimizely.github.io/nuclear-js/",
        Categoria.LIBRERIA,
    ],
    [
        "Nuclear",
        "librería para aplicaciones web que permite gestionar el estado de la aplicación de una manera sencilla y escalable mediante la utilización de un patrón de arquitectura Flux",
        "https://optimizely.github.io/nuclear-js/",
        Categoria.LIBRERIA,
    ],
    [
        "Java Web Toolkit",
        "herramienta que permite desarrollar aplicaciones web de manera eficiente utilizando el lenguaje de programación Java",
        "https://www.webtoolkit.eu/jwt",
        Categoria.LIBRERIA,
    ],
    [
        "PureMVC",
        "Framework para desarrollo de aplicaciones basado en el patrón de arquitectura MVC y diseñado para separar la lógica de presentación y la de negocio de una aplicación",
        "http://puremvc.org/",
        Categoria.FRAMEWORK,SubFramework.FULLSTACK
    ],
    [
        "D3",
        "biblioteca de visualización de datos basada en web que permite a los desarrolladores crear gráficos dinámicos y personalizados utilizando HTML, SVG y CSS",
        "https://d3js.org/",
        Categoria.LIBRERIA,
    ],
    [
        "D3js",
        "biblioteca de visualización de datos basada en web que permite a los desarrolladores crear gráficos dinámicos y personalizados utilizando HTML, SVG y CSS",
        "https://d3js.org/",
        Categoria.LIBRERIA,
    ],
    [
        "Handlebarsjs",
        "motor de plantillas para JavaScript que permite generar HTML dinámico al combinar datos con un archivo de plantilla",
        "https://handlebarsjs.com/",
        Categoria.LIBRERIA,
    ],
    [
        "Handlebars",
        "motor de plantillas para JavaScript que permite generar HTML dinámico al combinar datos con un archivo de plantilla",
        "https://handlebarsjs.com/",
        Categoria.LIBRERIA,
    ],
    [
        "Ampersandjs",
        "framework de JavaScript que proporciona una arquitectura modular y escalable para la construcción de aplicaciones web",
        "http://ampersandjs.com/",
        Categoria.FRAMEWORK,SubFramework.FULLSTACK
    ],
    [
        "Ampersand",
        "framework de JavaScript que proporciona una arquitectura modular y escalable para la construcción de aplicaciones web",
        "http://ampersandjs.com/",
        Categoria.FRAMEWORK,SubFramework.FULLSTACK
    
    ],
    [
        "AmplifyJS",
        "Biblioteca JavaScript para simplificar el desarrollo de aplicaciones web y móviles",
        "http://amplifyjs.com/",
        Categoria.LIBRERIA,
    ],
    [
        "Amplify",
        "Biblioteca JavaScript para simplificar el desarrollo de aplicaciones web y móviles",
        "http://amplifyjs.com/",
        Categoria.LIBRERIA,
    ],
    [
        "Heisenbergjs",
        "Biblioteca de UI para la construcción de aplicaciones web basadas en Backbone.js",
        "https://heisenbergjs.org/",
        Categoria.LIBRERIA,
    ],
    [
        "Heisenberg",
        "Biblioteca de UI para la construcción de aplicaciones web basadas en Backbone.js",
        "https://heisenbergjs.org/",
        Categoria.LIBRERIA,
    ],
    [
        "SharepointPlus",
        "Biblioteca de JavaScript para interactuar con la API de SharePoint",
        "https://github.com/Aymkdn/SharepointPlus",
        Categoria.LIBRERIA,
    ],
    [
        "Marionettejs",
        "Biblioteca para construir aplicaciones de Backbone.js más complejas y mantenibles",
        "https://marionettejs.com/",
        Categoria.FRAMEWORK,SubFramework.BACKEND
    ],
    [
        "Marionette",
        "Biblioteca para construir aplicaciones de Backbone.js más complejas y mantenibles",
        "https://marionettejs.com/",
        Categoria.FRAMEWORK,SubFramework.BACKEND
    ],
    [
        "Riot",
        "Biblioteca simple y rápida para construir interfaces de usuario.",
        "https://riot.js.org/",
        Categoria.LIBRERIA,
    ],
    [
        "pagerjs",
        "Biblioteca de enrutamiento de JavaScript para aplicaciones web SPA",
        "https://pagerjs.com/",
        Categoria.LIBRERIA,
    ],
    [
        "CanJS",
        "framework JavaScript para construir aplicaciones web",
        "https://canjs.com/",
        Categoria.LIBRERIA,
    ],
    [
        "Rivetsjs",
        "enlace de datos simplificado para aplicaciones web que no requiere un modelo de vista",
        "https://rivetsjs.com/",
        Categoria.LIBRERIA,
    ],
    [
        "Rivets",
        "enlace de datos simplificado para aplicaciones web que no requiere un modelo de vista",
        "https://rivetsjs.com/",
        Categoria.LIBRERIA,
    ],
    [
        "OpenUI5",
        "framework de interfaz de usuario de código abierto y completo para el desarrollo de aplicaciones empresariales basadas en web",
        "https://openui5.org/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "script.aculo.us",
        "biblioteca de efectos visuales y herramientas de usuario para JavaScript",
        "http://script.aculo.us/",
        Categoria.LIBRERIA,
    ],
    [
        "SmartClient",
        "plataforma de desarrollo de aplicaciones web para construir aplicaciones empresariales ricas en características y escalables",
        "https://www.smartclient.com/",
        Categoria.LIBRERIA,
    ],
    [
        "Backbonejs",
        "framework JavaScript que permite desarrollar aplicaciones web estructuradas",
        "https://backbonejs.org/",
        Categoria.FRAMEWORK,SubFramework.BACKEND
    ],
    [
        "Brick",
        "conjunto de componentes web personalizables y reutilizables que permiten construir interfaces de usuario escalables",
        "https://github.com/mozbrick/brick",
        Categoria.LIBRERIA,
    ],
    [
        "Spine",
        "Framework MVC ligero para JavaScript que se centra en la simplicidad y la facilidad de uso",
        "http://spine.github.io/",
        Categoria.FRAMEWORK,SubFramework.FULLSTACK
    ],
    [
        "UIZE JavaScript Framework",
        "Framework de JavaScript para crear interfaces de usuario de manera rápida y fácil",
        "http://www.uize.com/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "DoneJS",
        "framework de aplicaciones web que se basa en otros frameworks populares, como CanJS, StealJS y DocumentJS, para ofrecer una solución completa para desarrollar aplicaciones web modernas de alta calidad",
        "https://donejs.com/",
        Categoria.FRAMEWORK,SubFramework.FULLSTACK
    ],
    [
        ".NET",
        "Framework desarrollado por Microsoft para la creación de aplicaciones de escritorio y web en Windows",
        "https://dotnet.microsoft.com/",
        Categoria.FRAMEWORK,SubFramework.FULLSTACK
    ],
    [
        "ASP.NET",
        "Framework de Microsoft para el desarrollo de aplicaciones web en .NET",
        "https://dotnet.microsoft.com/apps/aspnet",
        Categoria.FRAMEWORK,SubFramework.FULLSTACK
    ],
    [
        "C#",
        "lenguaje de programación orientado a objetos desarrollado por Microsoft, utilizado en la creación de aplicaciones de escritorio, aplicaciones web y juegos. Es uno de los lenguajes principales para el desarrollo en la plataforma .NET",
        "https://docs.microsoft.com/en-us/dotnet/csharp/",
        Categoria.LENGUAJE,
    ],
    [
        "Entity Framework",
        "Framework desarrollado por Microsoft que permite trabajar con bases de datos relacionales utilizando objetos .NET",
        "https://docs.microsoft.com/en-us/ef/",
        Categoria.FRAMEWORK,SubFramework.BD
    ],
    [
        "VB.NET",
        "lenguaje de programación de propósito general desarrollado por Microsoft para .NET, basado en Visual Basic",
        "https://docs.microsoft.com/en-us/dotnet/visual-basic/",
        Categoria.LENGUAJE,
    ],
    [
        "WCF",
        "Framework de Microsoft para construir y desarrollar aplicaciones distribuidas basadas en servicios web",
        "https://docs.microsoft.com/en-us/dotnet/framework/wcf/",
        Categoria.FRAMEWORK,SubFramework.BACKEND
    ],
    [
        "WPF",
        "Framework de desarrollo de aplicaciones de escritorio para Windows que permite crear interfaces gráficas de usuario interactivas y con alto nivel de personalización",
        "https://docs.microsoft.com/en-us/dotnet/framework/wpf/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "Abap",
        "lenguaje de programación de cuarta generación que se utiliza principalmente para el desarrollo de aplicaciones empresariales en sistemas SAP",
        "https://community.sap.com/topics/abap",
        Categoria.LENGUAJE,
    ],
    [
        "Adobe",
        "Software creativo, como Photoshop, Illustrator, InDesign, Premiere, Acrobat, entre otros",
        "https://helpx.adobe.com/",
        Categoria.SOFTWARE,
    ],
    [
        "Ilustrator",
        "software de diseño gráfico vectorial",
        "https://helpx.adobe.com/illustrator/user-guide.html",
        Categoria.SOFTWARE,
    ],
    [
        "In Design",
        "software de maquetación y diseño de publicaciones",
        "https://helpx.adobe.com/indesign/user-guide.html",
        Categoria.SOFTWARE,
    ],
    [
        "InDesign",
        "software de maquetación y diseño de publicaciones",
        "https://helpx.adobe.com/indesign/user-guide.html",
        Categoria.SOFTWARE,
    ],
    [
        "Premiere",
        "software de edición de vídeo",
        "https://helpx.adobe.com/premiere-pro/user-guide.html",
        Categoria.SOFTWARE,
    ],
    [
        "Photoshop",
        "software de edición y retocado de imágenes",
        "https://helpx.adobe.com/photoshop/user-guide.html",
        Categoria.SOFTWARE,
    ],
    [
        "XD",
        "software de diseño de experiencias de usuario (UX)",
        "https://helpx.adobe.com/xd/user-guide.html",
        Categoria.SOFTWARE,
    ],
    [
        "Ajax",
        "Tecnología para desarrollar aplicaciones web asincrónicas",
        "https://developer.mozilla.org/en-US/docs/Web/Guide/AJAX",
        Categoria.METODOLOGIA,
    ],
    [
        "Angular",
        "Framework de JavaScript para construir aplicaciones web del lado del cliente",
        "https://angular.io/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "ASP",
        "Tecnología de Microsoft para desarrollo web del lado del servidor utilizando C# o VB.NET",
        "https://www.asp.net/",
        Categoria.FRAMEWORK,SubFramework.FULLSTACK
    ],
    [
        "AutoCad",
        "Software de diseño asistido por ordenador para dibujo en 2D y 3D",
        "https://www.autodesk.com/products/autocad/overview",
        Categoria.SOFTWARE,
    ],
    [
        "Bootstrap",
        "Framework front-end para el desarrollo rápido y fácil de sitios web responsivo",
        "https://getbootstrap.com/docs/5.0/getting-started/introduction/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "C",
        " Lenguaje de programación de propósito general y de bajo nivel",
        "https://devdocs.io/c/",
        Categoria.LENGUAJE,
    ],
    [
        "C++",
        "Lenguaje de programación de propósito general y de alto rendimiento",
        "https://devdocs.io/cpp/",
        Categoria.LENGUAJE,
    ],
    [
        "Cobol",
        " Lenguaje de programación orientado a negocios y usado principalmente en aplicaciones empresariales",
        "https://www.ibm.com/docs/en/ibm-zos/2.4.0?topic=programming-about-cobol-language",
        Categoria.LENGUAJE,
    ],
    [
        "Cocoa",
        "Framework para desarrollo de aplicaciones en Mac OS X y iOS",
        "https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaFundamentals/Introduction/Introduction.html",
        Categoria.FRAMEWORK,SubFramework.FULLSTACK
    ],
    [
        "ColdFusion",
        "Lenguaje de programación web",
        "https://helpx.adobe.com/coldfusion/user-guide.html",
        Categoria.LENGUAJE,
    ],
    [
        "CSS",
        "Lenguaje de hojas de estilo para la presentación de páginas web",
        "https://developer.mozilla.org/en-US/docs/Web/CSS",
        Categoria.LENGUAJE,
    ],
    [
        "CSS3",
        "Lenguaje de hojas de estilo para la presentación de páginas web",
        "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3",
        Categoria.LENGUAJE,
    ],
    [
        "Less",
        "Lenguaje de hojas de estilo para la presentación de páginas web",
        "http://lesscss.org/",
        Categoria.LENGUAJE,
    ],
    [
        "Sass",
        "Lenguaje de hojas de estilo para la presentación de páginas web",
        "https://sass-lang.com/documentation",
        Categoria.LENGUAJE,
    ],
    [
        "Delphi",
        "Entorno de desarrollo integrado (IDE) para la programación en Pascal",
        "https://docwiki.embarcadero.com/RADStudio/Alexandria/en/Main_Page",
        Categoria.IDE,
    ],
    [
        "Android",
        "Sistema operativo móvil de código abierto",
        "https://developer.android.com/docs",
        Categoria.OS,
    ],
    [
        "Cordova",
        "Framework para desarrollo de aplicaciones móviles multiplataforma",
        "https://cordova.apache.org/docs/en/latest/",
        Categoria.FRAMEWORK,SubFramework.MOVIL
    ],
    [
        "iOS",
        "Sistema operativo móvil de Apple",
        "https://developer.apple.com/ios/",
        Categoria.OS,
    ],
    [
        "Windows Phone",
        "sistema operativo móvil desarrollado por Microsoft para teléfonos inteligentes, que ahora ha sido descontinuado",
        "https://docs.microsoft.com/en-us/previous-versions/windows/apps/hh202936(v=win.10)",
        Categoria.OS,
    ],
    [
        "Xamarin",
        "Framework de desarrollo de aplicaciones móviles multiplataforma utilizando el lenguaje C# y .NET",
        "https://docs.microsoft.com/en-us/xamarin/",
        Categoria.FRAMEWORK,SubFramework.MOVIL
    ],
    [
        "Go",
        "Lenguaje de programación de código abierto diseñado para crear software simple, eficiente y escalable",
        "https://golang.org/doc/",
        Categoria.LENGUAJE,
    ],
    [
        "HTML",
        "Lenguaje de marcado utilizado para crear páginas web",
        "https://developer.mozilla.org/en-US/docs/Web/HTML",
        Categoria.LENGUAJE,
    ],
    [
        "HTML5",
        "Lenguaje de marcado utilizado para crear páginas web",
        "https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5",
        Categoria.LENGUAJE,
    ],
    [
        "XHTML",
        "Lenguaje de marcado similar a HTML pero con una sintaxis más estricta y compatible con XML",
        "https://www.w3.org/TR/xhtml1/",
        Categoria.LENGUAJE,
    ],
    [
        "Android Studio",
        "Entorno de desarrollo integrado oficial para la plataforma Android",
        "https://developer.android.com/studio",
        Categoria.IDE,
    ],
    [
        "Eclipse",
        "Entorno de desarrollo integrado gratuito y de código abierto para múltiples lenguajes de programación",
        "https://www.eclipse.org/",
        Categoria.IDE,
    ],
    [
        "IntelliJ",
        "Entorno de desarrollo integrado de Java de JetBrains",
        "https://www.jetbrains.com/idea/",
        Categoria.IDE,
    ],
    [
        "Netbeans",
        "Entorno de desarrollo integrado de código abierto para múltiples lenguajes de programación",
        "https://netbeans.apache.org/",
        Categoria.IDE,
    ],
    [
        "Visual Studio Code",
        "Entorno de desarrollo integrado propietario de Microsoft para múltiples lenguajes de programación",
        "https://docs.microsoft.com/en-us/visualstudio/?view=vs-2022",
        Categoria.IDE,
    ],
    [
        "VSCode",
        "Entorno de desarrollo integrado propietario de Microsoft para múltiples lenguajes de programación",
        "https://docs.microsoft.com/en-us/visualstudio/?view=vs-2022",
        Categoria.IDE,
    ],
    [
        "Visual Studio",
        "Entorno de desarrollo integrado propietario de Microsoft para múltiples lenguajes de programación",
        "https://docs.microsoft.com/en-us/visualstudio/?view=vs-2022",
        Categoria.IDE,
    ],
    [
        "XCode",
        "Entorno de desarrollo integrado propietario de Apple para aplicaciones de iOS, macOS, watchOS y tvOS",
        "https://developer.apple.com/xcode/",
        Categoria.IDE,
    ],
    [
        "Zend Studio",
        "Entorno de desarrollo integrado propietario para aplicaciones web y móviles de PHP",
        "https://www.zend.com/products/zend-studio",
        Categoria.IDE,
    ],
    [
        "Ionic",
        "framework para construir aplicaciones móviles híbridas",
        "https://ionicframework.com/docs",
        Categoria.FRAMEWORK,SubFramework.MOVIL
    ],
    [
        "Java",
        "lenguaje de programación orientado a objetos popular y versátil",
        "https://docs.oracle.com/en/java/",
        Categoria.LENGUAJE,
    ],
    [
        "J2EE",
        "conjunto de especificaciones para construir aplicaciones empresariales en Java",
        "https://docs.oracle.com/javaee/7/index.html",
        Categoria.ESPECIFICACION,
    ],
    [
        "JAVA EE",
        "conjunto de especificaciones para construir aplicaciones empresariales en Java",
        "https://docs.oracle.com/javaee/7/index.html",
        Categoria.ESPECIFICACION,
    ],
    [
        "JEE",
        "conjunto de especificaciones para construir aplicaciones empresariales en Java",
        "https://docs.oracle.com/javaee/7/index.html",
        Categoria.ESPECIFICACION,
    ],
    [
        "JAVA SE",
        "conjunto de especificaciones para construir aplicaciones estandares en Java",
        "https://www.oracle.com/java/",
        Categoria.ESPECIFICACION,
    ],
    [
        "EJB",
        "modelo de componente para construir aplicaciones empresariales en Java",
        "https://docs.oracle.com/javaee/7/tutorial/ejb-intro.htm",
        Categoria.ESPECIFICACION,
    ],
    [
        "Grails",
        "framework de desarrollo web para la plataforma Java",
        "https://docs.grails.org/latest/",
        Categoria.FRAMEWORK,SubFramework.BACKEND
    ],
    [
        "J2ME",
        "plataforma Java para dispositivos móviles y embebidos",
        "https://docs.oracle.com/javame/developer/developer.html",
        Categoria.ESPECIFICACION,
    ],
    [
        "JBoss",
        "servidor de aplicaciones Java de código abierto",
        "https://docs.jboss.org/jbossas/docs/Server_Configuration_Guide/beta500/html/index.html",
        Categoria.SERVIDOR,
    ],
    [
        "Tomcat",
        "servidor web y servlet de código abierto para Java",
        "http://tomcat.apache.org/tomcat-9.0-doc/index.html",
        Categoria.SERVIDOR,
    ],
    [
        "JPA",
        "especificación para mapeo objeto-relacional en Java",
        "https://docs.oracle.com/javaee/7/tutorial/persistence-intro.htm",
        Categoria.ESPECIFICACION,
    ],
    [
        "Hibernate",
        "Framework de mapeo objeto-relacional para Java que implementa JPA",
        "https://hibernate.org/orm/documentation/",
        Categoria.FRAMEWORK,SubFramework.BD
    ],
    [
        "JSF",
        "framework para construir interfaces de usuario web en Java",
        "https://docs.oracle.com/javaee/7/javaserver-faces-2-2/vdldocs-facelets/index.html",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "JSP",
        "tecnología para la creación de páginas web dinámicas utilizando Java",
        "https://docs.oracle.com/javaee/5/tutorial/doc/bnagx.html",
        Categoria.LIBRERIA,
    ],
    [
        "Servlets",
        "Componentes de Java para procesamiento de peticiones HTTP en el servidor web",
        "http://www.servlets.com/docs/",
        Categoria.LIBRERIA,
    ],
    [
        "JUnit",
        "Framework para pruebas unitarias en Java",
        "https://junit.org/junit5/docs/current/user-guide/",
        Categoria.FRAMEWORK,SubFramework.TEST
    ],
    [
        "Maven",
        "Herramienta de gestión de proyectos para construir y administrar aplicaciones Java",
        "https://maven.apache.org/guides/",
        Categoria.SOFTWARE,
    ],
    [
        "Spring",
        "Framework de Java para desarrollo de aplicaciones empresariales",
        "https://spring.io/projects/spring-framework",
        Categoria.FRAMEWORK,SubFramework.BACKEND
    ],
    [
        "Springboot",
        "Framework de Java para crear aplicaciones Spring de forma más rápida y sencilla",
        "https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/",
        Categoria.FRAMEWORK,SubFramework.BACKEND
    ],
    [
        "Spring boot",
        "Framework de Java para crear aplicaciones Spring de forma más rápida y sencilla",
        "https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/",
        Categoria.FRAMEWORK,SubFramework.BACKEND
    ],
    [
        "Struts",
        "Framework de Java para el desarrollo de aplicaciones web basadas en el patrón MVC",
        "https://struts.apache.org/getting-started/",
        Categoria.FRAMEWORK,SubFramework.BACKEND
    ],
    [
        "JavaScript",
        "Lenguaje de programación utilizado para el desarrollo de aplicaciones web",
        "https://developer.mozilla.org/en-US/docs/Web/JavaScript",
        Categoria.LENGUAJE,
    ],
    [
        "AngularJS",
        "Framework de JavaScript para construir aplicaciones web del lado del cliente",
        "https://docs.angularjs.org/api",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "Nuxt",
        "Framework de JavaScript para aplicaciones web universales y de renderizado del lado del servidor",
        "https://nuxtjs.org/docs/2.x/get-started/installation",
        Categoria.FRAMEWORK,SubFramework.BACKEND
    ],
    [
        "Next",
        "Framework de React para el desarrollo de aplicaciones web universales y de renderizado del lado del servidor",
        "https://nextjs.org/docs",
        Categoria.FRAMEWORK,SubFramework.BACKEND
    ],
    [
        "NextJS",
        "Framework de React para el desarrollo de aplicaciones web universales y de renderizado del lado del servidor",
        "https://nextjs.org/docs",
        Categoria.FRAMEWORK,SubFramework.BACKEND
    ],
    [
        "NuxtJS",
        "Framework de JavaScript para aplicaciones web universales y de renderizado del lado del servidor",
        "https://nuxtjs.org/docs/2.x/get-started/installation",
        Categoria.FRAMEWORK,SubFramework.BACKEND
    ],
    [
        "Backbone",
        "framework JavaScript que permite desarrollar aplicaciones web estructuradas",
        "https://backbonejs.org/",
        Categoria.FRAMEWORK,SubFramework.BACKEND
    ],
    [
        "Electron",
        "Framework de JavaScript para el desarrollo de aplicaciones de escritorio multiplataforma",
        "https://www.electronjs.org/docs",
        Categoria.FRAMEWORK,SubFramework.FULLSTACK
    ],
    [
        "ElectronJS",
        "Framework de JavaScript para el desarrollo de aplicaciones de escritorio multiplataforma",
        "https://www.electronjs.org/docs",
        Categoria.FRAMEWORK,SubFramework.FULLSTACK
    ],
    [
        "Express",
        "Framework de JavaScript para el desarrollo de aplicaciones web y servicios REST",
        "https://expressjs.com/",
        Categoria.FRAMEWORK,SubFramework.BACKEND
    ],
    [
        "ExpressJS",
        "Framework de JavaScript para el desarrollo de aplicaciones web y servicios REST",
        "https://expressjs.com/",
        Categoria.FRAMEWORK,SubFramework.BACKEND
    ],
    [
        "JQuery",
        "Biblioteca de JavaScript para simplificar la manipulación del DOM y la creación de interacciones en páginas web",
        "https://api.jquery.com/",
        Categoria.LIBRERIA,
    ],
    [
        "JSON",
        "formato de datos liviano y fácil de leer y escribir para intercambio de datos",
        "https://www.json.org/json-en.html",
        Categoria.LENGUAJE,
    ],
    [
        "Nodejs",
        "Entorno en tiempo de ejecucion de JavaScript para construir aplicaciones de red escalables",
        "https://nodejs.org/en/docs/",
        Categoria.EE,
    ],
    [
        "Node",
        "Entorno en tiempo de ejecucion de JavaScript para construir aplicaciones de red escalables",
        "https://nodejs.org/en/docs/",
        Categoria.EE,
    ],
    [
        "ReactJS",
        "Framework de JavaScript para construir interfaces de usuario",
        "https://reactjs.org/docs/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "React",
        "Framwork de JavaScript para construir interfaces de usuario",
        "https://reactjs.org/docs/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "Redux",
        "biblioteca de gestión de estado para aplicaciones de JavaScript",
        "https://redux.js.org/",
        Categoria.LIBRERIA,
    ],
    [
        "ReduxJS",
        "biblioteca de gestión de estado para aplicaciones de JavaScript",
        "https://redux.js.org/",
        Categoria.LIBRERIA,
    ],
    [
        "TypeScript",
        "lenguaje de programación de código abierto que es un superconjunto de JavaScript",
        "https://www.typescriptlang.org/docs/",
        Categoria.LENGUAJE,
    ],
    [
        "Vue",
        "Framework de JavaScript para construir interfaces de usuario",
        "https://vuejs.org/v2/guide/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "VueJS",
        "Framework de JavaScript para construir interfaces de usuario",
        "https://vuejs.org/v2/guide/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "JMeter",
        "herramienta de prueba de carga y rendimiento de aplicaciones",
        "https://jmeter.apache.org/usermanual/",
        Categoria.SOFTWARE,
    ],
    [
        "Kotlin",
        "lenguaje de programación de código abierto que se ejecuta en la Máquina Virtual de Java (JVM)",
        "https://kotlinlang.org/docs/home.html",
        Categoria.LENGUAJE,
    ],
    [
        "Dart",
        "lenguaje de programación de código abierto desarrollado por Google",
        "https://dart.dev/guides",
        Categoria.LENGUAJE,
    ],
    [
        "Flutter",
        "Framework multiplataforma de código abierto basado en el lenguaje de programación Dart",
        "https://flutter.dev/docs",
        Categoria.FRAMEWORK,SubFramework.MOVIL
    ],
    [
        "MS SQL",
        "sistema de gestión de bases de datos relacionales desarrollado por Microsoft",
        "https://docs.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver15",
        Categoria.SGBD,
    ],
    [
        "MySQL",
        "sistema de gestión de bases de datos relacionales de código abierto",
        "https://dev.mysql.com/doc/",
        Categoria.SGBD,
    ],
    [
        "NUnit",
        "Framework de pruebas unitarias para el lenguaje de programación .NET",
        "https://nunit.org/docs/",
        Categoria.FRAMEWORK,SubFramework.TEST
    ],
    [
        "Objective-C",
        "lenguaje de programación utilizado principalmente para el desarrollo de aplicaciones para el sistema operativo iOS",
        "https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Introduction/introObjectiveC.html",
        Categoria.LENGUAJE,
    ],
    [
        "Oracle Forms",
        "lenguaje de programación y un entorno de desarrollo integrado para la creación de aplicaciones empresariales",
        "https://docs.oracle.com/en/middleware/developer-tools/forms/",
        Categoria.LENGUAJE,
    ],
    [
        "Perl",
        "lenguaje de programación de propósito general",
        "https://perldoc.perl.org/",
        Categoria.LENGUAJE,
    ],
    [
        "PHP",
        "lenguaje de programación utilizado principalmente para el desarrollo web del lado del servidor",
        "https://www.php.net/docs.php",
        Categoria.LENGUAJE,
    ],
    [
        "CakePHP",
        "Framework de código abierto para el desarrollo de aplicaciones web PHP",
        "https://book.cakephp.org/4/en/index.html",
        Categoria.FRAMEWORK,SubFramework.BACKEND
    ],
    [
        "CodeIgniter",
        "framework de aplicaciones web de código abierto basado en el patrón de diseño MVC (Modelo-Vista-Controlador) para PHP",
        "https://codeigniter.com/user_guide/index.html",
        Categoria.FRAMEWORK,SubFramework.BACKEND
    ],
    [
        "Laravel",
        "framework de aplicaciones web de código abierto basado en PHP con una sintaxis elegante y expresiva",
        "https://laravel.com/docs/8.x",
        Categoria.FRAMEWORK,SubFramework.BACKEND
    ],
    [
        "Symfony",
        "framework de aplicaciones web de código abierto basado en PHP, con una arquitectura flexible y modular",
        "https://symfony.com/doc/current/index.html",
        Categoria.FRAMEWORK,SubFramework.BACKEND
    ],
    [
        "YII",
        "framework de aplicaciones web de código abierto basado en PHP, que permite desarrollar aplicaciones de alta escalabilidad y rendimiento",
        "https://www.yiiframework.com/doc/guide/2.0/en",
        Categoria.FRAMEWORK,SubFramework.BACKEND
    ],
    [
        "Zend",
        "framework de aplicaciones web de código abierto basado en PHP, que ofrece una arquitectura modular y escalable para aplicaciones empresariales",
        "https://docs.zendframework.com/",
        Categoria.FRAMEWORK,SubFramework.BACKEND
    ],
    [
        "PL1",
        "lenguaje de programación de alto nivel, enfocado en aplicaciones empresariales y científicas",
        "https://www.ibm.com/support/pages/enterprise-pli-zos-documentation-library",
        Categoria.LENGUAJE,
    ],
    [
        "PowerBuilder",
        "herramienta de desarrollo de aplicaciones empresariales, que permite crear aplicaciones de escritorio y móviles",
        "https://docs.appeon.com",
        Categoria.SOFTWARE,
    ],
    [
        "Protractor",
        "Framework de prueba de extremo a extremo para aplicaciones Angular y AngularJS",
        "https://www.protractortest.org/#/api",
        Categoria.FRAMEWORK,SubFramework.TEST
    ],
    [
        "Python",
        "lenguaje de programación de alto nivel, con una sintaxis simple y fácil de aprender",
        "https://docs.python.org/3/",
        Categoria.LENGUAJE,
    ],
    [
        "PyCharm",
        "un entorno de desarrollo integrado (IDE) para el lenguaje de programación Python",
        "https://www.jetbrains.com/pycharm/",
        Categoria.IDE,
    ],
    [
        "Django",
        "Framework de desarrollo web en Python",
        "https://docs.djangoproject.com/en/3.2/",
        Categoria.FRAMEWORK,SubFramework.BACKEND
    ],
    [
        "R",
        "lenguaje de programación y un entorno de desarrollo para estadísticas y análisis de datos",
        "https://www.r-project.org/help.html",
        Categoria.LENGUAJE,
    ],
    [
        "React Native",
        "Framework para desarrollo de aplicaciones móviles nativas en JavaScript",
        "https://reactnative.dev/docs/getting-started",
        Categoria.FRAMEWORK,SubFramework.MOVIL
    ],
    [
        "REST",
        "Representational State Transfer, estilo de arquitectura para sistemas web que utiliza HTTP y URIs",
        "https://restfulapi.net/",
        Categoria.ESPECIFICACION,
    ],
    [
        "Ruby",
        "Lenguaje de programación dinámico, orientado a objetos y de propósito general",
        "https://www.ruby-lang.org/en/documentation/",
        Categoria.LENGUAJE,
    ],
    [
        "Ruby on rails",
        "Framework de desarrollo web basado en el lenguaje de programación Ruby",
        "https://guides.rubyonrails.org/",
        Categoria.FRAMEWORK,SubFramework.BACKEND
    ],
    [
        "Scala",
        "Lenguaje de programación multiparadigma que combina la programación orientada a objetos y la programación funcional",
        "https://docs.scala-lang.org/",
        Categoria.LENGUAJE,
    ],
    [
        "Shell",
        "Interprete de comandos que permite interactuar con el sistema operativo mediante comandos",
        "https://www.gnu.org/software/bash/manual/bash.html",
        Categoria.CLI,
    ],
    [
        "Sketch",
        "biblioteca de JavaScript que permite la creación de gráficos vectoriales y animaciones en aplicaciones web utilizando HTML5 canvas",
        "https://www.sketch.com/docs/",
        Categoria.LIBRERIA,
    ],
    [
        "SQL",
        "Lenguaje de programación para gestionar bases de datos relacionales",
        "https://docs.microsoft.com/en-us/sql/?view=sql-server-ver15",
        Categoria.LENGUAJE,
    ],
    [
        "SQLite",
        "Sistema de gestión de bases de datos relacional y embebido",
        "https://www.sqlite.org/docs.html",
        Categoria.SGBD,
    ],
    [
        "Swift",
        "Lenguaje de programación de propósito general desarrollado por Apple para el desarrollo de aplicaciones en sus sistemas operativos",
        "https://swift.org/documentation/",
        Categoria.LENGUAJE,
    ],
    [
        "Tensorflow",
        "Biblioteca de código abierto de aprendizaje automático desarrollada por Google",
        "https://www.tensorflow.org/api_docs",
        Categoria.LIBRERIA,
    ],
    [
        "UML",
        "Lenguaje de modelado de software",
        "http://www.uml.org/",
        Categoria.LENGUAJE,
    ],
    [
        "VBA",
        "Lenguaje de programación de macros utilizado en Microsoft Office",
        "https://docs.microsoft.com/en-us/office/vba/library-reference/concepts/getting-started-with-vba-in-office",
        Categoria.LENGUAJE,
    ],
    [
        "Visual Basic",
        " Lenguaje de programación de Microsoft para el desarrollo de aplicaciones Windows",
        "https://docs.microsoft.com/en-us/dotnet/visual-basic/getting-started/",
        Categoria.LENGUAJE,
    ],
    [
        "WinDev",
        "Herramienta de desarrollo RAD para aplicaciones de escritorio y web",
        "https://windev.com/windev",
        Categoria.IDE,
    ],
    [
        "WebDev",
        "Herramienta de desarrollo RAD para aplicaciones de escritorio y web",
        "https://windev.com/webdev",
        Categoria.IDE,
    ],
    [
        "XML",
        "Lenguaje de marcado utilizado para el intercambio de datos en la web",
        "https://www.w3.org/XML/",
        Categoria.LENGUAJE,
    ],
    [
        "XSL",
        "Lenguaje de transformación de documentos XML",
        "https://www.w3.org/TR/xsl/",
        Categoria.LENGUAJE,
    ],
    [
        "XSLT",
        "Lenguaje de transformación de documentos XML",
        "https://www.w3.org/TR/xslt/",
        Categoria.LENGUAJE,
    ],
    [
        "Active Directory",
        "Servicio de directorio de Microsoft utilizado para gestionar recursos en una red",
        "https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview",
        Categoria.SOFTWARE,
    ],
    [
        "Apache",
        "Servidor web de código abierto",
        "https://httpd.apache.org/docs/",
        Categoria.SERVIDOR,
    ],
    [
        "Citrix",
        "Software de virtualización de aplicaciones y escritorios",
        "https://docs.citrix.com/en-us/citrix-virtual-apps-desktops/",
        Categoria.SOFTWARE,
    ],
    [
        "Cucumber",
        "framework de pruebas de aceptación basado en lenguaje natural",
        "https://cucumber.io/docs/cucumber/",
        Categoria.FRAMEWORK,SubFramework.TEST
    ],
    [
        "SGBD",
        "sistemas de gestión de bases de datos",
        "https://docs.microsoft.com/en-us/sql/?view=sql-server-ver15",
        Categoria.SGBD,
    ],
    [
        "Access",
        "sistema de gestión de bases de datos de Microsoft",
        "https://docs.microsoft.com/en-us/office/client-developer/access/",
        Categoria.SGBD,
    ],
    [
        "DB2",
        "sistema de gestión de bases de datos relacional de IBM",
        "https://www.ibm.com/es-es/db2",
        Categoria.SGBD,
    ],
    [
        "DynamoDB",
        "base de datos NoSQL totalmente administrada de Amazon Web Services",
        "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html",
        Categoria.SGBD,
    ],
    [
        "Informix",
        "sistema de gestión de bases de datos relacional de IBM",
        "https://www.ibm.com/es-es/products/informix",
        Categoria.SGBD,
    ],
    [
        "MongoDB",
        "base de datos NoSQL de código abierto",
        "https://docs.mongodb.com/",
        Categoria.SGBD,
    ],
    [
        "OracleDB",
        "sistema de gestión de bases de datos relacional de Oracle",
        "https://docs.oracle.com/en/database/oracle/oracle-database/",
        Categoria.SGBD,
    ],
    [
        "Postgre",
        "sistema de gestión de bases de datos relacional de código abierto",
        "https://www.postgresql.org/docs/",
        Categoria.SGBD,
    ],
    [
        "PostgreSQL",
        "sistema de gestión de bases de datos relacional de código abierto",
        "https://www.postgresql.org/docs/",
        Categoria.SGBD,
    ],
    [
        "Redis",
        "base de datos en memoria de código abierto",
        "https://redis.io/documentation",
        Categoria.SGBD,
    ],
    [
        "SQL Server",
        "Sistema de gestión de bases de datos relacional de Microsoft",
        "https://docs.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver15",
        Categoria.SGBD,
    ],
    [
        "IBM Notes",
        "Aplicación de software colaborativo de IBM",
        "https://help.hcltechsw.com/",
        Categoria.SOFTWARE,
    ],
    [
        "IIS",
        "Servidor web de Microsoft para sistemas operativos Windows",
        "https://docs.microsoft.com/en-us/iis/",
        Categoria.SERVIDOR,
    ],
    [
        "Linux",
        "Sistema operativo libre y de código abierto",
        "https://www.linux.org/docs/",
        Categoria.OS,
    ],
    [
        "Debian",
        "Distribución de Linux conocida por su estabilidad y seguridad",
        "https://www.debian.org/doc/",
        Categoria.OS,
    ],
    [
        "Kali Linux",
        "Distribución de Linux especializada en pruebas de penetración y seguridad",
        "https://docs.kali.org/",
        Categoria.OS,
    ],
    [
        "Red Hat",
        "Distribución de Linux empresarial de código abierto",
        "https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/",
        Categoria.OS,
    ],
    [
        "Ubuntu",
        "Distribución de Linux fácil de usar y popular",
        "https://ubuntu.com/server/docs",
        Categoria.OS,
    ],
    [
        "Mac OS",
        "Sistema operativo exclusivo de los dispositivos Mac de Apple",
        "https://developer.apple.com/macos/",
        Categoria.OS,
    ],
    [
        "MacOS",
        "Sistema operativo exclusivo de los dispositivos Mac de Apple",
        "https://developer.apple.com/macos/",
        Categoria.OS,
    ],
    [
        "tvOS",
        "sistema operativo de Apple para Apple TV",
        "https://developer.apple.com/tvos/",
        Categoria.OS,
    ],
    [
        "tv OS",
        "sistema operativo de Apple para Apple TV",
        "https://developer.apple.com/tvos/",
        Categoria.OS,
    ],
    [
        "MQ Series",
        "software de mensajería de IBM",
        "https://www.ibm.com/docs/en/ibm-mq",
        Categoria.SOFTWARE,
    ],
    [
        "Tibco",
        "software de integración empresarial y de análisis de datos",
        "https://docs.tibco.com",
        Categoria.SOFTWARE,
    ],
    [
        "Tuxedo",
        "Middleware de Oracle para aplicaciones distribuidas",
        Categoria.MIDDLEWARE,
        "https://www.oracle.com/middleware/technologies/tuxedo.html",
    ],
    [
        "MS Exchange Server",
        "Servidor de correo electrónico y colaboración de Microsoft",
        "https://docs.microsoft.com/en-us/exchange/",
        Categoria.SOFTWARE,
    ],
    [
        "MS Office",
        "suite de aplicaciones de ofimática de Microsoft",
        "https://support.microsoft.com/en-us/office",
        Categoria.SOFTWARE,
    ],
    [
        "Nagios",
        "sistema de monitorización de redes y servicios",
        "https://assets.nagios.com/downloads/nagioscore/docs/nagioscore/",
        Categoria.SOFTWARE,
    ],
    [
        "Novell",
        "Software de redes",
        "https://www.novell.com/documentation/",
        Categoria.SOFTWARE,
    ],
    [
        "Oracle",
        "Software de bases de datos y aplicaciones empresariales",
        "https://docs.oracle.com/en/",
        Categoria.SOFTWARE,
    ],
    [
        "Oracle Service Bus",
        "middleware de Oracle para integración de servicios",
        "https://docs.oracle.com/en/middleware/fusion-middleware/12.2.1.4/osb/index.html",
        Categoria.MIDDLEWARE,
    ],
    [
        "Avaya",
        "Software que ofrece soluciones de comunicaciones empresariales",
        "https://support.avaya.com/",
        Categoria.SOFTWARE,
    ],
    [
        "Cisco",
        "Software que desarrolla y vende equipos de red y telecomunicaciones",
        "https://www.cisco.com/c/en/us/support/index.html",
        Categoria.SOFTWARE,
    ],
    [
        "Juniper",
        "Software para redes de alta velocidad",
        "https://www.juniper.net/documentation/",
        Categoria.SOFTWARE,
    ],
    [
        "SOAP",
        "protocolo para intercambio de datos en la web",
        "https://www.w3schools.com/xml/xml_soap.asp",
        Categoria.ESPECIFICACION,
    ],
    [
        "TCP/IP",
        "protocolo de comunicación utilizado en internet y redes privadas",
        "https://tools.ietf.org/html/rfc1180",
        Categoria.ESPECIFICACION,
    ],
    [
        "CheckPoint",
        "Software que proporciona soluciones de seguridad de redes",
        "https://www.checkpoint.com/es/products/capsule-docs/",
        Categoria.SOFTWARE,
    ],
    [
        "F5 Network",
        "Software que ofrece servicios de entrega de aplicaciones y seguridad de redes",
        "https://docs.cloud.f5.com/docs/",
        Categoria.SOFTWARE,
    ],
    [
        "Fortinet",
        "Software que proporciona soluciones de seguridad de red y ciberseguridad",
        "https://docs.fortinet.com/document/fortigate/6.0.0/cookbook/286785/introduction-to-fortinet-security",
        Categoria.SOFTWARE,
    ],
    [
        "Imperva",
        "Software en soluciones de seguridad de datos y aplicaciones en la nube",
        "https://docs.imperva.com/",
        Categoria.SOFTWARE,
    ],
    [
        "McAfee",
        "Software de seguridad informática que ofrece soluciones de antivirus, firewall y seguridad de redes para proteger a los usuarios contra virus, malware, spam y otras amenazas en línea",
        "https://www.mcafee.com/enterprise/en-us/products.html",
        Categoria.SOFTWARE,
    ],
    [
        "Selenium",
        "Libreria de automatización de pruebas de software que permite simular la interacción de un usuario con una aplicación web",
        "https://www.selenium.dev/documentation/en/",
        Categoria.LIBRERIA,
    ],
    [
        "SharePoint",
        "plataforma de colaboración empresarial de Microsoft que permite crear y gestionar sitios web para compartir información y documentos",
        "https://docs.microsoft.com/en-us/sharepoint/dev/",
        Categoria.SOFTWARE,
    ],
    [
        "Amazon Web Service",
        "plataforma de servicios en la nube de Amazon que ofrece una amplia gama de servicios de infraestructura, plataforma y software como servicio",
        "https://aws.amazon.com/documentation/",
        Categoria.SOFTWARE,
    ],
    [
        "AWS",
        "plataforma de servicios en la nube de Amazon que ofrece una amplia gama de servicios de infraestructura, plataforma y software como servicio",
        "https://aws.amazon.com/documentation/",
        Categoria.SOFTWARE,
    ],
    [
        "Google Cloud Platform",
        " plataforma de servicios en la nube de Google que ofrece servicios de infraestructura, plataforma y software como servicio",
        "https://cloud.google.com/docs",
        Categoria.SOFTWARE,
    ],
    [
        "GCP",
        " plataforma de servicios en la nube de Google que ofrece servicios de infraestructura, plataforma y software como servicio",
        "https://cloud.google.com/docs",
        Categoria.SOFTWARE,
    ],
    [
        "IBM Bluemix",
        "plataforma de servicios en la nube de IBM que permite a los desarrolladores crear, ejecutar y gestionar aplicaciones en la nube",
        "https://www.ibm.com/cloud/bluemix",
        Categoria.SOFTWARE,
    ],
    [
        "Bluemix",
        "plataforma de servicios en la nube de IBM que permite a los desarrolladores crear, ejecutar y gestionar aplicaciones en la nube",
        "https://www.ibm.com/cloud/bluemix",
        Categoria.SOFTWARE,
    ],
    [
        "Microsoft Azure",
        "plataforma de servicios en la nube de Microsoft que ofrece servicios de infraestructura, plataforma y software como servicio",
        "https://docs.microsoft.com/en-us/azure/",
        Categoria.SOFTWARE,
    ],
    [
        "Azure",
        "plataforma de servicios en la nube de Microsoft que ofrece servicios de infraestructura, plataforma y software como servicio",
        "https://docs.microsoft.com/en-us/azure/",
        Categoria.SOFTWARE,
    ],
    [
        "Tivoli",
        "suite de software de gestión de sistemas de IBM que incluye herramientas para la monitorización, la automatización, la gestión de la configuración y la seguridad de sistemas y redes",
        "https://www.ibm.com/docs/en/tivoli-monitoring",
        Categoria.SOFTWARE,
    ],
    [
        "AIX",
        "Sistema operativo de IBM",
        "https://www.ibm.com/docs/en/aix/7.1?topic=aix-pdfs",
        Categoria.OS,
    ],
    [
        "Solaris",
        "Sistema operativo de Oracle",
        "https://www.oracle.com/solaris/solaris11/",
        Categoria.OS,
    ],
    [
        "CVS",
        "Sistema de control de versiones",
        "https://www.nongnu.org/cvs/",
        Categoria.VCS,
    ],
    [
        "GIT",
        "Sistema de control de versiones distribuido",
        "https://git-scm.com/documentation",
        Categoria.VCS,
    ],
    [
        "Jenkins",
        "Herramienta de integración continua",
        "https://www.jenkins.io/doc/",
        Categoria.SOFTWARE,
    ],
    [
        "Mercurial",
        "Sistema de control de versiones distribuido",
        "https://www.mercurial-scm.org/",
        Categoria.VCS,
    ],
    [
        "TFS",
        "Herramienta de gestión de proyectos y control de versiones de Microsoft",
        "https://docs.microsoft.com/en-us/azure/devops/server/?view=azure-devops",
        Categoria.VCS,
    ],
    [
        "Azure devOps",
        "Herramienta de gestión de proyectos y control de versiones de Microsoft",
        "https://docs.microsoft.com/en-us/azure/devops/server/?view=azure-devops",
        Categoria.VCS,
    ],
    [
        "SVN",
        "Sistema de control de versiones centralizado",
        "https://subversion.apache.org/docs/",
        Categoria.VCS,
    ],
    [
        "Svelte",
        "Framework de JavaScript",
        "https://svelte.dev/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "SvelteJS",
        "Framework de JavaScript",
        "https://svelte.dev/",
        Categoria.FRAMEWORK,SubFramework.FRONTEND
    ],
    [
        "Docker",
        "Plataforma para crear, implementar y ejecutar aplicaciones en contenedores",
        "https://docs.docker.com/",
        Categoria.SOFTWARE,
    ],
    [
        "Hyper-V",
        "Tecnología de virtualización de Microsoft",
        "https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/",
        Categoria.SOFTWARE,
    ],
    [
        "Kubernetes",
        "Plataforma de orquestación de contenedores",
        "https://kubernetes.io/docs/",
        Categoria.SOFTWARE,
    ],
    [
        "VMware",
        "Plataforma de virtualización",
        "https://docs.vmware.com/en/VMware-vSphere/index.html",
        Categoria.SOFTWARE,
    ],
    [
        "WebLogic",
        "Plataforma de servidor de aplicaciones Java EE de Oracle",
        "https://docs.oracle.com/en/middleware/standalone/weblogic-server/index.html",
        Categoria.SERVIDOR,
    ],
    [
        "WebSphere",
        "Plataforma de servidor de aplicaciones Java EE de IBM"
        "https://www.ibm.com/docs/en/was-nd",
        Categoria.SERVIDOR,
    ],
    [
        "Windows",
        "Sistema operativo de Microsoft para computadoras personales",
        "https://docs.microsoft.com/en-us/windows/",
        Categoria.OS,
    ],
    [
        "Windows Server",
        "Sistema operativo de Microsoft para servidores",
        "https://docs.microsoft.com/en-us/windows-server/",
        Categoria.OS,
    ],
    [
        "Windows Server 2016",
        "Sistema operativo de Microsoft para servidores",
        "https://docs.microsoft.com/en-us/windows-server/",
        Categoria.OS,
    ],
    [
        "Windows Server 2019",
        "Sistema operativo de Microsoft para servidores",
        "https://docs.microsoft.com/en-us/windows-server/",
        Categoria.OS,
    ],
    [
        "Windows Server 2022",
        "Sistema operativo de Microsoft para servidores",
        "https://docs.microsoft.com/en-us/windows-server/",
        Categoria.OS,
    ],
    [
        "Z/OS",
        "Sistema operativo de mainframe de IBM",
        "https://www.ibm.com/docs/en/zos/2.4.0?topic=overview-introducing-zos-24",
        Categoria.OS,
    ],
    [
        "OS/400",
        "Sistema operativo de mainframe de IBM utilizado en los servidores IBM iSeries y AS/400",
        "https://www.ibm.com/docs/en/i/7.4?topic=overview-os-400-operating-system",
        Categoria.OS,
    ],
    [
        "Alhambra",
        "Librería para el diseño y trabajo con algoritmos DNA",
        "https://github.com/DNA-and-Natural-Algorithms-Group/alhambra",
        Categoria.LIBRERIA,
    ],
    [
        "Cassandra",
        "base de datos distribuida NoSQL de código abierto diseñada para manejar grandes cantidades de datos en múltiples servidores, proporcionando alta disponibilidad y sin un único punto de falla",
        "https://cassandra.apache.org/doc/latest/",
        Categoria.SGBD,
    ],
    [
        "Hadoop",
        "framework de software de código abierto para almacenar y procesar grandes conjuntos de datos en un clúster distribuido",
        "https://hadoop.apache.org/docs/current/",
        Categoria.FRAMEWORK,SubFramework.CD
    ],
    [
        "Spark",
        "motor de análisis de datos rápido y de código abierto para procesamiento de datos distribuido",
        "https://spark.apache.org/docs/latest/",
        Categoria.FRAMEWORK,SubFramework.CD
    ],
    [
        "Storm",
        "sistema de procesamiento de flujo de datos en tiempo real y distribuido",
        "https://storm.apache.org/releases/2.2.0/index.html",
        Categoria.FRAMEWORK,SubFramework.CD
    ],
    [
        "HyperLedger fabric",
        "plataforma de blockchain de código abierto que permite la creación de aplicaciones empresariales basadas en blockchain",
        "https://hyperledger-fabric.readthedocs.io/en/release-2.3/",
        Categoria.FRAMEWORK,SubFramework.BLOCKCHAIN
    ],
    [
        "Cognos",
        "herramienta de inteligencia empresarial utilizada para generar informes, análisis y paneles",
        "https://www.ibm.com/docs/en/cognos-analytics/11.1.0?topic=services-cognos-analytics-documentation",
        Categoria.SOFTWARE,
    ],
    [
        "MS Power BI",
        "herramienta de inteligencia empresarial utilizada para visualizar y analizar datos",
        "https://docs.microsoft.com/en-us/power-bi/",
        Categoria.SOFTWARE,
    ],
    [
        "Oracle BI",
        "plataforma de inteligencia empresarial utilizada para la creación de informes, análisis y paneles",
        "https://docs.oracle.com/en/business-intelligence/index.html",
        Categoria.SOFTWARE,
    ],
    [
        "Qlik Sense",
        "herramienta de visualización de datos utilizada para analizar y compartir información en tiempo real",
        "https://www.qlik.com/us/products/qlik-sense",
        Categoria.SOFTWARE,
    ],
    [
        "QlikView",
        "herramienta de inteligencia empresarial utilizada para la creación de informes y análisis de datos",
        "https://help.qlik.com/en-US/qlikview",
        Categoria.SOFTWARE,
    ],
    [
        "Alfresco",
        "sistema de gestión de contenidos empresariales de código abierto",
        "https://docs.alfresco.com/6.2/concepts/welcome-introduction.html",
        Categoria.SOFTWARE,
    ],
    [
        "Drupal",
        "sistema de gestión de contenidos (CMS) gratuito y de código abierto para crear sitios web y aplicaciones web",
        "https://www.drupal.org/docs",
        Categoria.SOFTWARE,
    ],
    [
        "Joomla",
        "CMS gratuito y de código abierto para crear sitios web y aplicaciones web",
        "https://docs.joomla.org/Main_Page",
        Categoria.SOFTWARE,
    ],
    [
        "Liferay",
        "plataforma de portal web y CMS empresarial de código abierto",
        "https://learn.liferay.com/",
        Categoria.SOFTWARE,
    ],
    [
        "Magento",
        "CMS gratuito y de código abierto enfocado en la creación de tiendas en línea y comercio electrónico",
        "https://devdocs.magento.com/",
        Categoria.SOFTWARE,
    ],
    [
        "WordPress",
        "CMS gratuito y de código abierto muy popular para crear sitios web, blogs y aplicaciones web",
        "https://wordpress.org/support/",
        Categoria.SOFTWARE,
    ],
    [
        "CRM",
        "conjunto de prácticas, estrategias y tecnologías para administrar y analizar las interacciones con los clientes y potenciales clientes",
        "https://docs.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/developer-guide",
        Categoria.SOFTWARE,
    ],
    [
        "Documentum",
        "sistema de gestión de contenido empresarial (ECM) propiedad de EMC Corporation",
        "https://www.ibm.com/docs/es/datacap/9.1.4?topic=actions-documentum",
        Categoria.SOFTWARE,
    ],
    [
        "Odoo",
        "sistema de planificación de recursos empresariales (ERP) gratuito y de código abierto para empresas",
        "https://www.odoo.com/documentation/user/",
        Categoria.SOFTWARE,
    ],
    [
        "SSIS",
        "herramienta de integración de datos de Microsoft SQL Server",
        "https://docs.microsoft.com/en-us/sql/integration-services/",
        Categoria.SOFTWARE,
    ],
    [
        "JD Edwards",
        "paquete de software de gestión empresarial propiedad de Oracle Corporation utilizado principalmente por empresas de manufactura",
        "https://docs.oracle.com/en/applications/jd-edwards/index.html",
        Categoria.SOFTWARE,
    ],
    [
        "JIRA",
        "Herramienta de seguimiento de proyectos y problemas utilizada para la gestión ágil de proyectos de software",
        "https://confluence.atlassian.com/jirasoftware",
        Categoria.SOFTWARE,
    ],
    [
        "Agile",
        "Metodología ágil de desarrollo de software que se enfoca en la colaboración del equipo de desarrollo y la entrega iterativa y continua de software",
        "https://www.agilealliance.org/agile101/",
        Categoria.ESPECIFICACION,
    ],
    [
        "Scrum",
        "Metodología ágil de desarrollo de software que se enfoca en la colaboración del equipo de desarrollo y la entrega iterativa y continua de software",
        "https://www.scrum.org/resources/what-is-scrum",
        Categoria.ESPECIFICACION,
    ],
    [
        "MS Dynamics",
        "Solución de software empresarial que permite la gestión de finanzas, inventarios, ventas, compras y recursos humanos",
        "https://docs.microsoft.com/en-us/dynamics365/",
        Categoria.SOFTWARE,
    ],
    [
        "Navision",
        "Solución de software empresarial que permite la gestión de finanzas, inventarios, ventas, compras y recursos humanos",
        "https://docs.microsoft.com/en-us/dynamics-nav/",
        Categoria.SOFTWARE,
    ],
    [
        "Oracle E-Business Suite",
        "Suite de aplicaciones empresariales de Oracle que cubre áreas como finanzas, cadena de suministro, recursos humanos y ventas",
        "https://docs.oracle.com/cd/E18727_01/index.htm",
        Categoria.SOFTWARE,
    ],
    [
        "PeopleSoft",
        "Solución de software empresarial que cubre áreas como recursos humanos, finanzas, cadena de suministro y gestión de proyectos",
        "https://docs.oracle.com/cd/E66686_01/pt853pbh1/eng/pt/tcdg.htm",
        Categoria.SOFTWARE,
    ],
    [
        "SAGE",
        "Software de contabilidad y gestión empresarial utilizado por pequeñas y medianas empresas",
        "https://www.sage.com/en-us/products/",
        Categoria.SOFTWARE,
    ],
    [
        "Salesforce",
        "Plataforma de gestión de relaciones con clientes (CRM) basada en la nube que permite la gestión de ventas, marketing y servicio al cliente",
        "https://developer.salesforce.com/docs/",
        Categoria.SOFTWARE,
    ],
    [
        "SAP",
        "Suite de aplicaciones empresariales que cubre áreas como finanzas, gestión de cadena de suministro, recursos humanos y análisis de negocio",
        "https://help.sap.com/viewer/index",
        Categoria.SOFTWARE,
    ],
    [
        "SAS",
        "Herramientas de análisis de datos utilizadas para la minería de datos, el modelado estadístico y la visualización de datos",
        "https://documentation.sas.com/",
        Categoria.SOFTWARE,
    ],
    [
        "JMP",
        "Herramientas de análisis de datos utilizadas para la minería de datos, el modelado estadístico y la visualización de datos",
        "https://www.jmp.com/es_es/support/jmp-documentation.html",
        Categoria.SOFTWARE,
    ],
    [
        "SCADA",
        "Sistema de control y adquisición de datos utilizado en la automatización industrial",
        "https://rapidscada.org/product/documentation/",
        Categoria.SOFTWARE,
    ],
    [
        "Siebel",
        "Plataforma de gestión de relaciones con clientes (CRM) utilizada para la gestión de ventas, marketing y servicio al cliente",
        "https://www.oracle.com/es/cx/siebel/",
        Categoria.SOFTWARE,
    ],
    [
        "Tableau",
        "Software de análisis y visualización de datos utilizado para la creación de informes y paneles de control interactivos",
        "https://www.tableau.com/learn/get-started",
        Categoria.SOFTWARE,
    ],
}
