from abc import ABC, abstractmethod
from models.dto.ubicacionDto import Ubicacion


class UbicacionDaoInterface(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def obtener(self, idUbicacion: int):
        pass

    @abstractmethod
    def actualizar(self, ubicacion: Ubicacion):
        pass

    @abstractmethod
    def borrar(self, idUbicacion: int):
        pass

    @abstractmethod
    def crear(self, ubicacion: Ubicacion):
        pass
