
mensaje: str =  None
numero: int =   0

def funcion_mensaje(texto: str)->None:

    print(f"Este es el mensaje recibido: {texto}")

def funcion_asignar_valor(valor: int)->None:
    global numero
    numero = valor


print("Se ejecuto 'modulo_uno.py'")


if __name__ == "__main__":
    print("Se ejecuto 'modulo_uno.py' como main")
