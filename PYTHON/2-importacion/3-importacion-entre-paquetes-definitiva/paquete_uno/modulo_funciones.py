#FUNCION 1----------------------------------------------------------------------
"""
    Descripcion:        suma dos numeros enteros.
    Args:               Operadores de la suma
    Returns:            Total resultado.
    Raises (errores):   Ninguno.
"""
def sumador_enteros(
    operador_uno: int,
    operador_dos: int = 1
) -> int:
    resultado_suma: int = operador_uno + operador_dos
    return resultado_suma



#FUNCION 2----------------------------------------------------------------------
"""
    Descripcion:        suma dos numeros enteros.
    Args:               Operadores de la suma
    Returns:            Total resultado.
    Raises (errores):   Ninguno.
"""
def restador_enteros(
        operador_uno: int, 
        operador_dos: int = 1
) -> int:
    resultado_resta: int = operador_uno - operador_dos
    return resultado_resta


#EJECUCIONES-----------------------------------------------------------------------
#ESTO SI SE EJECUTA CUANDO SE IMPORTA
print("*" * 75)
print(f"Resultado multiplicacion desde el modulo paquete_uno.modulo_funciones.py (sin main): {sumador_enteros(1)}")

#ESTO NO SE EJECUTA CUANDO SE IMPORTA
if __name__ == "__main__":
    print(f"Resultado multiplicacion desde el modulo paquete_uno.modulo_funciones.py (con main): {sumador_enteros(10.10)}")