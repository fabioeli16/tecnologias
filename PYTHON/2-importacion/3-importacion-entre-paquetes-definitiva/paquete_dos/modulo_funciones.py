
#VARIABLES-----------------------------------------------------------------------
resultado_suma: int = 0
resultado_resta: int= 0
resultado_multiplicacion: int= 0

#FUNCIONES-----------------------------------------------------------------------
def sumador_enteros(operador_uno: int, operador_dos: int) -> int:
    global resultado_suma
    resultado_suma = operador_uno + operador_dos
    return None



def restador_enteros(operador_uno: int, operador_dos: int) -> int:
    global resultado_resta
    resultado_resta = operador_uno - operador_dos
    return None


def multiplicador_entero(operador_uno: int = 1, operador_dos: int = 1) -> int:
    global resultado_multiplicacion
    resultado_multiplicacion = operador_uno * operador_dos
    return None



