main.py

from cliente import Cliente
from servicio import ReservaSala
from reserva import Reserva
from logger_config import registrar_error

print("=== SISTEMA SOFTWARE FJ ===")

try:
    cliente1 = Cliente("Andrea", "123", "andrea@gmail.com")

    servicio1 = ReservaSala(2)

    reserva1 = Reserva(cliente1, servicio1)

    reserva1.confirmar()

    print("Reserva realizada correctamente")

except Exception as e:
    registrar_error(e)
    print("Error:", e)