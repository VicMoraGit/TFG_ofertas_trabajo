from abc import ABC, abstractmethod
from models.requisitoDto import Requisito

class RequisitoDaoInterface(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def obtener_por_nombre(self, nombre:str):
        pass

    @abstractmethod
    def obtener(self, idRequisito:int):
        pass

    @abstractmethod
    def actualizar(self,requisito:Requisito):
        pass

    @abstractmethod
    def borrar(self, idRequisito:int):
        pass

    @abstractmethod
    def crear(self, requisito:Requisito):
        pass
    
