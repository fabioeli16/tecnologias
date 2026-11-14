
def describir_temperatura()->None:
    temperatura: int = 30
    if (temperatura > 25):
        print("Hace calor",end="...\n")
    else:
        print("Hace frio",end="...\n")

def par_impar()->None:
    numero: int= 10

    if (numero % 2 == 0):
        print("El numero es par")
    else:
        print("El numero es impar")

def calificador()->None:
    calificacion: int = 8

    if (calificacion >= 9):
        print("Excelente")
    elif (calificacion >= 7):
        print("Aprobado")
    elif ( calificacion >= 6):
        print("Suficiente")
    else:
        print("Reprobado")

#OPERADOTR TERNARIO--------------------------------------------------------
def reconocer_edad()->None:
    edad: int = 17
    estado: str = "Mayor de edad" if (edad >= 18) else "Menor de edad"
    print(estado)

def elegir_opcion()->None:
    opcion = input("Digita (1, 2, 3): ")

    match opcion:
        case "1":
            print("Ver saldo")
        case "2":
            print("Depositar")
        case "3":
            print("Salir")
        case _:            # _ captura cualquier otro valor
            print("Opción no válida")


def main():
    describir_temperatura()
    par_impar()
    calificador()
    reconocer_edad()
    elegir_opcion()



if __name__ == "__main__":
    main()
