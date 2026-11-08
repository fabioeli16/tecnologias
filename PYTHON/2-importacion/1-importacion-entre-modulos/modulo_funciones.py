
#VARIABLES-----------------------------------------------------------------------
resultado_suma: int = 0
resultado_resta: int= 0

#FUNCIONES-----------------------------------------------------------------------
def sumador_enteros(
    operador_uno: int,
    operador_dos: int = 1
) -> int:
    """
    suma dos numeros enteros.
    Args:
        Operadores de la suma
    Returns:
        Total calculado con impuesto.
    Raises:
        Ninguno.
    """

    global resultado_suma
    resultado_suma = operador_uno + operador_dos
    return resultado_suma



def restador_enteros(operador_uno: int, operador_dos: int = 1) -> int:
    global resultado_resta
    resultado_resta = operador_uno - operador_dos
    return resultado_resta


#print(sumador_enteros(5, 3))
#print(f"Resultado resta: {restador_enteros(5)}")