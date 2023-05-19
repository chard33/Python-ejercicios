class Vehículo:

    def __init__(self, Color, Ruedas, Puertas):
        self.Color = Color
        self.Ruedas = Ruedas
        self.Puertas = Puertas

class Coche(Vehículo):

    def __init__(self, Color, Ruedas, Puertas, Velocidad, Cilindrada):
        super().__init__(Color, Ruedas, Puertas)
        self.Velocidad = Velocidad
        self.Cilindrada = Cilindrada

miCoche = Coche("azul", 4, 4, 150, 1500)

print(f'Mi coche es de color {miCoche.Color}')
print(f'Mi coche tiene {miCoche.Ruedas} llantas')
print(f'Mi coche tiene {miCoche.Puertas} puertas')
print(f'Voy a una velocidad de {miCoche.Velocidad}km/h')
print(f'La cilindrada de mi coche es de {miCoche.Cilindrada}')