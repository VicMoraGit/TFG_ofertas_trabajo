from logging import Logger, getLogger
from traceback import format_exc
from config import api_key_azure
from uuid import uuid4
from requests import post


class Traductor():

    def __init__(self) -> None:
        self._endpoint = "https://api.cognitive.microsofttranslator.com"
        self._location = "westeurope"
        self._log: Logger = getLogger(__class__.__name__)

    def traducir(self, dominio_from: str, dominio_to: str, texto: str) -> str:
        ruta = "/translate"
        url = self._endpoint + ruta

        params = {
            'api-version': '3.0',
            'from': dominio_from,
            'to': dominio_to
        }

        headers = {
            'Ocp-Apim-Subscription-Key': api_key_azure,
            'Ocp-Apim-Subscription-Region': self._location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid4())
        }

        body = [{
            'text': texto
        }]
        try:

            request = post(url, params=params, headers=headers, json=body)
            json = request.json()
            print(json)

            return json[0]["translations"][0]["text"]
        
        except:

            self._log.error(format_exc())
            return None

    def detectar_idioma(self, texto: str) -> str:
        ruta = "/detect"
        url = self._endpoint + ruta

        params = {
            'api-version': '3.0',
        }

        headers = {
            'Ocp-Apim-Subscription-Key': api_key_azure,
            'Ocp-Apim-Subscription-Region': self._location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid4())
        }

        body = [{
            'text': texto
        }]
        try:

            request = post(url, params=params, headers=headers, json=body)
            json = request.json()
            print(json)
            return json[0]["language"]
        
        except:

            self._log.error(format_exc())
            return None
