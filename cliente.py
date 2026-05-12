cliente.py

from excepciones import ClienteError

class Cliente:

    def __init__(self, nombre, documento, correo):

        if not nombre:
            raise ClienteError("Nombre inválido")

        if "@" not in correo:
            raise ClienteError("Correo inválido")

        self.__nombre = nombre
        self.__documento = documento
        self.__correo = correo

    def get_nombre(self):
        return self.__nombre