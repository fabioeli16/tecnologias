class Animal:
    def __init__(self, especie):
        self.especie = especie

    def hacer_sonido(self):
        print("El animal hace un sonido")

    def informacion_animal(self):
        print(f"Soy un animal y mi especie es: {self.especie}")
