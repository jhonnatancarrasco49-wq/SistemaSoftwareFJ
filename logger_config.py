logger_config.py

import logging

logging.basicConfig(
    filename="errores.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def registrar_error(error):
    logging.error(error)