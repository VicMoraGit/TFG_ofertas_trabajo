from abc import ABC, abstractmethod
from models.puestoDto import Puesto

class PuestoDaoInterface(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def obtener(self, idPuesto:int) ->  None|Puesto:
        pass

    @abstractmethod
    def actualizar(self,puesto:Puesto) -> bool:
        pass

    @abstractmethod
    def borrar(self, idPuesto:int) -> bool:
        pass

    @abstractmethod
    def crear(self, puesto:Puesto) -> bool:
        pass
    
