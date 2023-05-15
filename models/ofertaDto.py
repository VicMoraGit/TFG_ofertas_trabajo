from datetime import date
from dataclasses import dataclass

from models.puestoDto import Puesto


@dataclass
class Oferta:
    _id:int = 0
    _titulo:str = None
    _companyia:str = None
    _experiencia:str = None
    _salario:int = 0
    _fecha_publicacion:str = None
    _puesto:Puesto = None
    _es_teletrabajo:bool = None
    _ubicaciones:list[int] = None
    _requisitos:list[int] = None


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
    def fecha_publicacion(self,fecha_publicacion:str):
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
    def ubicaciones(self):
        return self._ubicaciones
    
    @ubicaciones.setter
    def ubicaciones(self,ubicaciones:list[int]):
        self._ubicaciones = ubicaciones

    @property
    def requisitos(self):
        return self._requisitos
    
    @requisitos.setter
    def requisitos(self,requisitos:list[int]):
        self._requisitos = requisitos

    