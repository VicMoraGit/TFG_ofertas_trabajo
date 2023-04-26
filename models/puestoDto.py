from dataclasses import dataclass

@dataclass
class PuestoDto:

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

    