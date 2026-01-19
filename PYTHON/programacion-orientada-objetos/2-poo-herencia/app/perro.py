from app.animal import Animal


class Perro(Animal):
    def __init__(self, especie, raza):
        super().__init__(especie)   # Llama al constructor de Animal
        self.raza = raza

    def hacer_sonido(self):
        print("Guau guau")

    def informacion_perro(self):
        print(f"Soy un {self.especie}, y mi raza es {self.raza}")
