from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from logger_config import registrar_error

print("===================================")
print(" SISTEMA SOFTWARE FJ ")
print("===================================")

# LISTA DE OPERACIONES
operaciones = []

# ===================================
# OPERACIÓN 1 - CLIENTE VÁLIDO
# ===================================

try:

    cliente1 = Cliente(
        "Andrea",
        "123456",
        "andrea@gmail.com"
    )

    operaciones.append("Cliente válido registrado")

    print("\nCliente registrado correctamente")

except Exception as e:

    registrar_error(e)

    print("Error:", e)

# ===================================
# OPERACIÓN 2 - CLIENTE INVÁLIDO
# ===================================

try:

    cliente2 = Cliente(
        "",
        "789456",
        "correo"
    )

except Exception as e:

    registrar_error(e)

    print("\nError cliente:", e)

# ===================================
# OPERACIÓN 3 - SERVICIO SALA
# ===================================

try:

    servicio1 = ReservaSala(2)

    operaciones.append("Reserva de sala creada")

    print("\nServicio de sala creado")

except Exception as e:

    registrar_error(e)

    print("Error:", e)

# ===================================
# OPERACIÓN 4 - ALQUILER EQUIPO
# ===================================

try:

    servicio2 = AlquilerEquipo(3)

    operaciones.append("Alquiler de equipo creado")

    print("\nServicio alquiler creado")

except Exception as e:

    registrar_error(e)

    print("Error:", e)

# ===================================
# OPERACIÓN 5 - ASESORÍA
# ===================================

try:

    servicio3 = AsesoriaEspecializada(1)

    operaciones.append("Asesoría creada")

    print("\nServicio asesoría creado")

except Exception as e:

    registrar_error(e)

    print("Error:", e)

# ===================================
# OPERACIÓN 6 - SERVICIO INVÁLIDO
# ===================================

try:

    servicio_error = ReservaSala(-2)

except Exception as e:

    registrar_error(e)

    print("\nError servicio:", e)

# ===================================
# OPERACIÓN 7 - RESERVA EXITOSA
# ===================================

try:

    reserva1 = Reserva(cliente1, servicio1)

    reserva1.confirmar()

    print("\n========== RESERVA 1 ==========")

    print(reserva1.mostrar_reserva())

except Exception as e:

    registrar_error(e)

    print("Error:", e)

# ===================================
# OPERACIÓN 8 - RESERVA CANCELADA
# ===================================

try:

    reserva2 = Reserva(cliente1, servicio2)

    reserva2.cancelar()

    print("\n========== RESERVA 2 ==========")

    print(reserva2.mostrar_reserva())

except Exception as e:

    registrar_error(e)

    print("Error:", e)

# ===================================
# OPERACIÓN 9 - RESERVA SIN CLIENTE
# ===================================

try:

    reserva3 = Reserva(None, servicio3)

except Exception as e:

    registrar_error(e)

    print("\nError reserva:", e)

# ===================================
# OPERACIÓN 10 - RESERVA SIN SERVICIO
# ===================================

try:

    reserva4 = Reserva(cliente1, None)

except Exception as e:

    registrar_error(e)

    print("\nError reserva:", e)

# ===================================
# MOSTRAR OPERACIONES
# ===================================

print("\n===================================")
print(" OPERACIONES REALIZADAS ")
print("===================================")

for operacion in operaciones:
    print("-", operacion)

# ===================================
# FINALIZAR SISTEMA
# ===================================

print("\nSistema ejecutado correctamente.")