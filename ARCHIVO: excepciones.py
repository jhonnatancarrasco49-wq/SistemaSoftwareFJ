# ==============================
# ARCHIVO: excepciones.py
# ==============================

class ClienteError(Exception):
    pass

class ServicioError(Exception):
    pass

class ReservaError(Exception):
    pass


# ==============================
# ARCHIVO: logger_config.py
# ==============================

import logging

logging.basicConfig(
    filename="errores.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def registrar_error(error):
    logging.error(error)


# ==============================
# ARCHIVO: cliente.py
# ==============================

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

    def mostrar_info(self):
        return f"Cliente: {self.__nombre}"


# ==============================
# ARCHIVO: servicio.py
# ==============================

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


class AlquilerEquipo(Servicio):

    def __init__(self, dias):
        super().__init__("Alquiler Equipo")

        if dias <= 0:
            raise ServicioError("Días inválidos")

        self.dias = dias

    def calcular_costo(self):
        return self.dias * 80000

    def descripcion(self):
        return "Servicio de alquiler de equipos"


class AsesoriaEspecializada(Servicio):

    def __init__(self, horas):
        super().__init__("Asesoría")

        if horas <= 0:
            raise ServicioError("Horas inválidas")

        self.horas = horas

    def calcular_costo(self):
        return self.horas * 120000

    def descripcion(self):
        return "Servicio de asesoría especializada"


# ==============================
# ARCHIVO: reserva.py
# ==============================

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

    def cancelar(self):
        self.estado = "Cancelada"

    def mostrar_reserva(self):

        return (
            f"Cliente: {self.cliente.get_nombre()}\n"
            f"Servicio: {self.servicio.descripcion()}\n"
            f"Costo: ${self.servicio.calcular_costo()}\n"
            f"Estado: {self.estado}"
        )


# ==============================
# ARCHIVO: main.py
# ==============================

from cliente import Cliente
from servicio import *
from reserva import Reserva
from logger_config import registrar_error

print("=== SISTEMA SOFTWARE FJ ===")

operaciones = []

# OPERACIÓN 1
try:
    cliente1 = Cliente("Andrea", "123", "andrea@gmail.com")
    operaciones.append("Cliente válido registrado")
except Exception as e:
    registrar_error(e)

# OPERACIÓN 2
try:
    cliente2 = Cliente("", "456", "correo")
except Exception as e:
    registrar_error(e)
    print("Error:", e)

# OPERACIÓN 3
try:
    servicio1 = ReservaSala(2)
    operaciones.append("Reserva sala creada")
except Exception as e:
    registrar_error(e)

# OPERACIÓN 4
try:
    servicio2 = AlquilerEquipo(3)
    operaciones.append("Alquiler creado")
except Exception as e:
    registrar_error(e)

# OPERACIÓN 5
try:
    servicio3 = AsesoriaEspecializada(1)
    operaciones.append("Asesoría creada")
except Exception as e:
    registrar_error(e)

# OPERACIÓN 6
try:
    servicio_error = ReservaSala(-2)
except Exception as e:
    registrar_error(e)
    print("Error:", e)

# OPERACIÓN 7
try:
    reserva1 = Reserva(cliente1, servicio1)
    reserva1.confirmar()

    print("\n--- RESERVA 1 ---")
    print(reserva1.mostrar_reserva())

except Exception as e:
    registrar_error(e)

# OPERACIÓN 8
try:
    reserva2 = Reserva(cliente1, servicio2)
    reserva2.cancelar()

    print("\n--- RESERVA 2 ---")
    print(reserva2.mostrar_reserva())

except Exception as e:
    registrar_error(e)

# OPERACIÓN 9
try:
    reserva3 = Reserva(None, servicio3)
except Exception as e:
    registrar_error(e)
    print("Error:", e)

# OPERACIÓN 10
try:
    reserva4 = Reserva(cliente1, None)
except Exception as e:
    registrar_error(e)
    print("Error:", e)

finally:
    print("\nSistema ejecutado correctamente.")
