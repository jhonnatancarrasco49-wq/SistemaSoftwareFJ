servicio.py
from abc import ABC, abstractmethod
from excepciones import ServicioError

class Servicio(ABC):

    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):

    def __init__(self, horas):
        super().__init__("Reserva Sala")

        if horas <= 0:
            raise ServicioError("Horas inválidas")

        self.horas = horas

    def calcular_costo(self):
        return self.horas * 50000

    def descripcion(self):
        return "Servicio de reserva de sala"