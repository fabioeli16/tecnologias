
#VARIABLES ------------------------------------------------------
x = 10        # entero
y = "hola"    # string
z = 3.14      # float
print (x,y,z)



#USAR HINTS ------------------------------------------------------
edad: int = 25
nombre: str = "Eli"
precio: float = 19.99
activo: bool = True
#PERO NO ES RESTRICTIVO
edad = "Fabio"
print (edad,nombre,precio,activo)


#HINTS + LISTAS + DICCIONARIOS ------------------------------------
numeros: list[int] = [1, 2, 3]
usuario: dict[str, str] = {"nombre": "Eli"}
numeros.append("Hola")

print(numeros)


#HINTS Y FUNCIONES ------------------------------------------------------
def suma(a: int, b: int) -> int:
    return a + b



