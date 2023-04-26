from dataclasses import dataclass

@dataclass
class Requisito:

    _id:int
    _nombre:str
    _descripcion:str
    _enlace:str
    _categoria:str

	
    @property
    def id(self):
        return self._id
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self,nombre:str):
        self._nombre = nombre
    
    @property
    def descripcion(self):
        return self._descripcion
    
    @descripcion.setter
    def descripcion(self,descripcion:str):
        self._descripcion = descripcion
    
    @property
    def enlace(self):
        return self._enlace
    
    @enlace.setter
    def enlace(self,enlace:str):
        self._enlace = enlace
    
    @property
    def categoria(self):
        return self._categoria
    
    @categoria.setter
    def categoria(self,categoria:str):
        self._categoria = categoria
    
    