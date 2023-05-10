from datetime import date
from dataclasses import dataclass

from models.puestoDto import Puesto
from models.requisitoDto import Requisito
from models.ubicacionDto import Ubicacion

@dataclass
class Oferta:
    _id:int
    _titulo:str
    _companyia:str
    _experiencia:str
    _salario:int
    _fecha_publicacion:date
    _puesto:Puesto
    _es_teletrabajo:bool
    _ubicacion:list[Ubicacion]
    _requisitos:list[Requisito]


    @property
    def id(self):
        return self._id

    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self,titulo:str):
        self._titulo = titulo

    @property
    def companyia(self):
        return self._companyia
    
    @companyia.setter
    def companyia(self,companyia:str):
        self._companyia = companyia

    @property
    def experiencia(self):
        return self._experiencia
    
    @experiencia.setter
    def experiencia(self,experiencia:str):
        self._experiencia = experiencia

    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self,salario:int):
        self._salario = salario

    @property
    def fecha_publicacion(self):
        return self._fecha_publicacion
    
    @fecha_publicacion.setter
    def fecha_publicacion(self,fecha_publicacion:date):
        self._fecha_publicacion = fecha_publicacion

    @property
    def puesto(self):
        return self._puesto
    
    @puesto.setter
    def puesto(self,puesto:Puesto):
        self._puesto = puesto

    @property
    def es_teletrabajo(self):
        return self._es_teletrabajo
    
    @es_teletrabajo.setter
    def es_teletrabajo(self,es_teletrabajo:bool):
        self._es_teletrabajo = es_teletrabajo

    @property
    def ubicacion(self):
        return self._ubicacion
    
    @ubicacion.setter
    def ubicacion(self,ubicacion:list[Ubicacion]):
        self._ubicacion = ubicacion

    @property
    def requisitos(self):
        return self._requisitos
    
    @requisitos.setter
    def requisitos(self,requisitos:list[Requisito]):
        self._requisitos = requisitos

    