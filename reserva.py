reserva.py

from excepciones import ReservaError

class Reserva:

    def __init__(self, cliente, servicio):

        if cliente is None:
            raise ReservaError("Cliente inválido")

        if servicio is None:
            raise ReservaError("Servicio inválido")

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"