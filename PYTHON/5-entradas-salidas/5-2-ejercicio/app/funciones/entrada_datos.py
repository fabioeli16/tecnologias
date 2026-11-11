def entrada_numero(mensaje: str)->int:
    while True:
        try:
            numero: int = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: Debes ingresar un número entero válido. Intenta de nuevo.")