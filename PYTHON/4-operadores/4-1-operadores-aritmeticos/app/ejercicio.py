from typing import Final



#1-DEFINIR VARIABLES----------------------------------------------------
SEGUNDOS_POR_HORA: Final[int] = 3600
SEGUNDOS_POR_MINUTO: Final[int] = 60



def convertir_segundos_a_horas(segundos: int) -> float:
    """
    Convierte segundos a horas.
    :param segundos: Cantidad de segundos a convertir.
    :return: Cantidad de horas.
    """
    horas: int = segundos // SEGUNDOS_POR_HORA
    return horas

def convertir_segundos_a_minutos(segundos: int) -> float:
    """
    Convierte segundos a minutos.
    :param segundos: Cantidad de segundos a convertir.
    :return: Cantidad de minutos.
    """
    minutos:int = (segundos % SEGUNDOS_POR_HORA) // SEGUNDOS_POR_MINUTO     
    return minutos

def convertir_segundos_a_tiempo(segundos: int) -> str:
    """
    Convierte segundos a horas, minutos y segundos.
    :param segundos: Cantidad de segundos a convertir.
    :return: Cadena con el tiempo en formato "HH:MM:SS".
    """
    horas = convertir_segundos_a_horas(segundos)
    minutos = convertir_segundos_a_minutos(segundos)
    segundos_restantes: int = segundos % SEGUNDOS_POR_MINUTO
    return f"{horas:02d}:{minutos:02d}:{segundos_restantes:02d}"