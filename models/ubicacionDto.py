from dataclasses import dataclass

@dataclass
class UbicacionDto:

    _id:int
    _provincia:str
    _comunidad:str

	
    @property
    def id(self):
        return self._id
    
    @property
    def provincia(self):
        return self._provincia
    
    @provincia.setter
    def provincia(self,provincia:str):
        self._provincia = provincia
    
    @property
    def comunidad(self):
        return self._comunidad

    @comunidad.setter
    def comunidad(self,comunidad:str):
        self._comunidad = comunidad
    
    