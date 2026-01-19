from app.perro import Perro

def main():
    mi_perro = Perro("Firulais", "Labrador")
    mi_perro.informacion_animal()
    mi_perro.informacion_perro()
    mi_perro.hacer_sonido()


if __name__ == "__main__":
    main()
