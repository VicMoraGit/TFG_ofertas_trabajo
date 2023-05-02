import re
from logging import Logger, getLogger
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

# Modulos externos
from unidecode import (
    unidecode,
)  # util para no tener en cuenta acentos y caracteres no-Ascii

from util.constantes import (
    ALL_SKILLS,
    FILTRO_HORAS,
    FILTRO_DIAS,
    FILTRO_MESES,
    FILTRO_FECHAS,
    PROVINCIAS,
)

log: Logger = getLogger("FiltroOfertas")
# log.setLevel(DEBUG)


class FiltroOfertas:
    def filtrar_fecha(self, texto: str):
        formato_fecha = "%Y-%m-%d"
        fecha_string = "Sin informacion"
        texto_lowercase = unidecode(texto.lower())

        # Si contiene digitos, se comprueban diferentes situaciones para obtener la fecha
        digitos = self._filtrar_digitos(texto)

        if digitos is not None:
            # Horas

            if any(
                x in texto_lowercase for x in FILTRO_HORAS
            ):  # la fecha contiene palabras relacionadas con "hora". Indeed
                fecha_string = date.today().strftime(formato_fecha)

            # Dias
            elif any(
                x in texto_lowercase for x in FILTRO_DIAS
            ):  # la fecha contiene palabras relacionadas con "dias". Indeed
                hoy = date.today()
                fecha_oferta = hoy - relativedelta(days=int(digitos.strip()))
                fecha_string = fecha_oferta.strftime(formato_fecha)

            # Meses
            elif any(
                x in texto_lowercase for x in FILTRO_MESES
            ):  # la fecha contiene palabras relacionadas con "meses". Indeed
                hoy = date.today()
                fecha_oferta = hoy - relativedelta(months=int(digitos.strip()))
                fecha_string = fecha_oferta.strftime(formato_fecha)

            elif (
                "/" in texto_lowercase
            ):  # fecha en formato DD/MM/YY. se eliminan posibles palabras. Tecnoempleo
                for palabra in FILTRO_FECHAS:
                    texto_lowercase = texto_lowercase.replace(palabra, "")
                fecha_string = datetime.strptime(texto_lowercase, "%d/%m/%Y").strftime(
                    formato_fecha
                )

        # Si no contiene digitos, se habra publicado hoy. ej. "Recien publicado", "Hoy".
        else:
            palabras_publicacion_hoy = ["recien", "hoy", "today", "now", "just"]
            if any(x in texto_lowercase for x in palabras_publicacion_hoy):
                fecha_string = date.today().strftime(formato_fecha)

        return fecha_string

    def filtrar_salario(self, texto: str):
        salario = "Sin informacion"

        # Extrae el salario de un texto, teniendo en cuenta numero de digitos, puntos, espacios y simbolo €
        #  regexr.com/75m25

        try:
            p = re.compile(r"£(\d|\.|\,){3,}(\s|)|(\d|\.|\,){3,}(\s|)€")
            s = p.search(texto)
            if s is not None:
                # Hay ofertas donde el salario publicado es un rango, por lo tanto se devuelve solo el primer valor
                # coincida con la expresion regular. ej: 30.000 - 35.000 € devolvera 35.000€ por el '€'

                salario = s.group()
                log.debug("Hay informacion sobre el salario")

        except:
            log.debug("No tiene informacion sobre salario")

        return salario

    def filtrar_experiencia(self, texto: str):
        experiencia = "Sin informacion"
        texto_lowercase = unidecode(texto.lower())
        try:
            # Filtra la experiencia de la descripcion en ingles https://regexr.com/75m3i o español https://regexr.com/75m4v.
            re_esp = re.compile(
                r"(experiencia\s)*(\+*)\d(\+*)+\s*(anos de experiencia|anos|ano)(?!.*(mercado|sector))"
            )
            re_eng = re.compile(
                r"(|required\s)(experience\s)*(\+*)\d(\+*)+\s*(years of experience|years|year)(?!.*(market|sector))"
            )

            # Busqueda de coincidencias
            s_esp = re_esp.search(texto_lowercase)
            s_eng = re_eng.search(texto_lowercase)

            # En caso de contener experiencia, extrae los años
            if s_esp is not None:
                años = self._filtrar_digitos(s_esp.group())
                if años is not None:
                    experiencia = años
                    log.debug("Si requiere experiencia")

            elif s_eng is not None:
                años = self._filtrar_digitos(s_eng.group())
                if años is not None:
                    experiencia = años
                    log.debug("Si requiere experiencia")

        except:
            log.debug("No tiene informacion sobre experiencia")

        return experiencia

    def _filtrar_digitos(self, texto: str):
        # Filtra solo los años
        re_digitos = re.compile(r"\d+")
        s_digitos = re_digitos.search(texto)

        if s_digitos is not None:
            return s_digitos.group()

        return None

    def filtrar_skills(self, texto: str):
        skills_oferta = []
        texto_lowercase = unidecode(texto.lower())
        # Se compara si alguna skill esta presente en la descripcion de la oferta

        for skill in ALL_SKILLS:
            # La expresion regular se asegura de que la skill coincida con una palabra completa
            p = re.compile(rf"\b{re.escape(skill.lower())}\b")
            s = p.search(texto_lowercase)
            if s is not None:
                skills_oferta.append(skill)

        if len(skills_oferta) == 0:
            log.debug("No se encontraron skils")

        return skills_oferta

    def filtrar_localizacion(self, texto: str):
        localizacion = "Sin informacion"
        texto_lowercase = unidecode(texto.lower())

        for provincia in PROVINCIAS.keys():
            if provincia in texto_lowercase:
                localizacion = PROVINCIAS[provincia]
                break

        return localizacion
