
#1-ASIGNAR GLOBAL------------------------------------------------------------------------
print("*" * 75)
print("modulo scope_asignar_2.py")
contador: int =0

def funcion_incrementar():
    global contador 
    contador = contador + 1

def funcion_decrementar():
    global contador 
    contador = contador - 1

funcion_incrementar()
funcion_incrementar()
funcion_decrementar()
print(contador)

#2-ASIGNAR LOCAL------------------------------------------------------------------------

def crear_contador():
    cuenta = 0
    def siguiente():
        nonlocal cuenta
        cuenta += 1
        return cuenta
    return siguiente

c = crear_contador()
print(c(), c(), c())  # 1 2 3