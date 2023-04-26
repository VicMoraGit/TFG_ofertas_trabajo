from abc import ABC, abstractmethod
from models.puestoDto import Puesto

class puestoDaoInterface(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def obtener(self, idPuesto:int):
        pass

    @abstractmethod
    def actualizar(self,puesto:Puesto):
        pass

    @abstractmethod
    def borrar(self, idPuesto:int):
        pass

    @abstractmethod
    def crear(self, puesto:Puesto):
        pass
    
