from app.config.settings import DEBUG, get_settings
import requests

edad: int = 20


def main():
    # Comparadores------------------------------------------------------------------------
    print(edad == 18)   # False
    print(edad != 18)   # True
    print(edad >= 18)   # True
    print(edad < 13)    # False

    # Comparaciones encadenadas (muy propias de Python)
    print(18 <= edad <= 25)   # True, equivale a: edad >= 18 and edad <= 25

    # También funcionan con texto (orden alfabético, distingue mayúsculas)
    print("ana" == "Ana")     # False
    print("ana" < "beto")     # True

    # Uso dentro de un if
    if edad >= 18:
        print("Mayor de edad")
    else:
        print("Menor de edad")

    #Errores comunes-----------------------------------------------------------------------
    # 1. Confundir = (asignar) con == (comparar)
    x = 5        # asigna
    x == 5       # compara -> True

    # 2. Comparar floats con ==
    print(0.1 + 0.2 == 0.3)            # False (por la precisión decimal)
    import math
    print(math.isclose(0.1 + 0.2, 0.3))  # True: esta es la forma correcta

    # 3. Comparar texto con número
    print("5" == 5)        # False: son tipos distintos
    print(int("5") == 5)   # True

    

if __name__ == "__main__":
    main()
