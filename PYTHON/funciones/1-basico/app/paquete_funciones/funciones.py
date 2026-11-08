

#FUNCION 1--------------------------------------------------------------------
def saludar(nombre: str="Desconocido") -> None:
    print(f"Holaaaa {nombre}, otra vez por aqui jaja que crazy")
    return None

#FUNCION 2--------------------------------------------------------------------
#
def sumador_varios_numeros(*numeros)-> float:
    resultado: int= 0

    #Valida que tenga valores
    if not numeros or len(numeros) == 0:
        print("No se enviaron numeros")
        return None

    #Valida que tenga solo numeros (Usando expresion generadora)
    if any(isinstance(x, str) for x in numeros):
        print("La tupla contiene al menos un string")
        return None

    for numero in numeros:
        resultado += numero
    return resultado


#FUNCION 3--------------------------------------------------------------------
def obtener_datos() -> tuple[str,int]:
    nombre: str = "Eli"
    edad: int = 29

    #Esto retorna una tupla
    #return nombre, edad

    #Retornar la tupla explicitamente
    return (nombre, edad)




#FUNCION 3--------------------------------------------------------------------
#SOBRE SCOPE
mi_variable_global: int = 25
def manipular_variable_global(nuevo_valor:int=0)-> None:
    global mi_variable_global
    mi_variable_global = nuevo_valor
    return None