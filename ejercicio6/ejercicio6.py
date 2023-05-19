class Vehículo:

    Color = "azul"
    Ruedas = 4
    Puertas = 2

class Coche(Vehículo):

    Velocidad = 140
    Cilindrada = 4

miCoche = Coche()

print(f'Mi coche es de color {miCoche.Color}')
print(f'Mi coche tiene {miCoche.Ruedas} llantas')
print(f'Mi coche tiene {miCoche.Puertas} puertas')
print(f'Voy a una velocidad de {miCoche.Velocidad}km/h')
print(f'La cilindrada de mi coche es de {miCoche.Cilindrada}')