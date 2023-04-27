from abc import ABC, abstractmethod
from models.ofertaDto import Oferta

class OfertaDaoInterface(ABC):
    def __init__(self):
        super().__init__()
    
    
    @abstractmethod
    def actualizar(self,oferta:Oferta):
        pass

    @abstractmethod
    def borrar(self, idOferta:int):
        pass

    @abstractmethod
    def crear(self, oferta:Oferta):
        pass
    