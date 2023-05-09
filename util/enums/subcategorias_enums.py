from enum import Enum


class SubFramework(Enum):
    FRONTEND = "Front-end"
    BACKEND = "Back-end"
    FULLSTACK = "Full-stack"
    INTERNACIONALIZACION = "Internacionalización"
    MOVIL = "Móvil"
    BD = "Base de datos"
    TEST = "Testing"
    CD = "Ciencia de datos"
    GAME = "Videojuegos"
    ROBOTICA = "Robótica"
    BLOCKCHAIN = "Cadena de bloques"


class SubLibreria(Enum):
    GESTION_DATOS = "Gestión de datos"
    UI = "Interfaz de usuario"
    AI = "Inteligencia Artificial"
    ACCESS = "Accesibilidad"
    DEPENDENCIAS = "Dependencias"
    DOM = "Manipulacion DOM"
    IO = "Comunicacion C/S"
    ESTADO = "Gestión de estado"
    API = "Contenedor de API"
    TEST = "Testing"


class SubSoftware(Enum):
    CMS = "Sistema de gestor de contenidos"
    DISENYO = "Diseño"
    BUILD = "Construcción de proyectos"
    TEST = "Testing"
    NEGOCIOS = "Negocios"
    LDAP = "Acceso a directorio"
    VIRTUAL = "Virtualización"
    CONT = "Orquestación y contenedores"
    MENSAJERIA = "Comunicación y mensajería"
    OFFICE = "Ofimática"
    RENDIMIENTO = "Rendimiento y monitorización"
    RED = "Redes"
    SEG = "Seguridad"
    ECM = "Gestión documental empresarial"
    SUITE = "Suite de servicios en la nube"
    CICD = "Integración continua y entrega continua"
    ERP = "Sistema de planificación de recursos empresariales"
    SEGUIMIENTO = "Seguimiento de proyectos e incidencias"
    CRM = "Gestión de relaciones con clientes"


class SubNoAplica(Enum):
    NO_APLICA = "No aplica"


class SubOS(Enum):
    LINUX = "GNU/Linux"
    WIN = "Windows"
    BSD = "BSD (Berkeley Software Distribution)"
    UNIX = "UNIX"


class SubServidor(Enum):
    WEB = "Web"


class SubSGBD(Enum):
    SQL = ("Base de datos relacional",)
    NO_SQL = "Base de datos no relacional"


class SubVCS(Enum):
    DIST = ("Distribuido",)
    CENT = "Centralizado"
