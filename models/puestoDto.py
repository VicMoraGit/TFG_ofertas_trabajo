from dataclasses import dataclass

@dataclass
class Puesto:

    _id:int
    _nombre:str
	
    @property
    def id(self):
        return self._id
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self,nombre:str):
        self._nombre = nombre

    def __str__(self) -> str:
        return f"Puesto {self._id}: {self._nombre}"
    