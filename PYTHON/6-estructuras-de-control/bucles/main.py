#1-DEFINICIONES-----------------------------------------------------
def contador()->None:
    contador: int = 1

    while contador <=10:
        print(contador, end=" ")
        contador += 1
    print("\nFin del bucle while")

def contador_rango()->None:
    for contador in range(1, 11):
        print(contador, end=" ")
    print("\nFin del bucle for")

def recorrer_lista()->None:
    frutas: list[str] = ["Manzana", "Pera", "Uva", "Fresa"]
    for fruta in frutas:
        print(fruta, end=" ")

    for i, fruta in enumerate(frutas, start=1):
        print(f"{i}. {fruta}")

def control_bucle()->None:
    # break: detenerse al encontrar el primer número negativo
    numeros = [4, 8, -2, 7, 1]
    for n in numeros:
        if n < 0:
            print(f"Encontré un negativo: {n}")
            break
        print(n)
    # 4, 8, Encontré un negativo: -2

    # continue: imprimir solo los impares
    for i in range(1, 11):
        if i % 2 == 0:
            continue
        print(i)
    # 1, 3, 5, 7, 9
    
def creador_tablas()->None:
    for tabla in range(1, 4):
        print(f"--- Tabla del {tabla} ---")
        for i in range(1, 11):
            print(f"{tabla} x {i} = {tabla * i}")

def login()->None:
    clave: str = ""

    while clave != "1234":
        clave = input("Digite la clave: ")

    print("Clave correcta, acceso permitido")


#2-EJECUCIONES-----------------------------------------------------
def main():
    contador()
    contador_rango()
    recorrer_lista()
    control_bucle()
    creador_tablas()
    login()



if __name__ == "__main__":
    main()
