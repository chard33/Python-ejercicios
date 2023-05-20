import pickle
def main():

    miVehiculo = Vehiculo("Azul", 2, 4)

    guardar(miVehiculo)

    print(cargar())

class Vehiculo:

    def __init__(self, color, puertas, llantas):
        self.color = color
        self.puertas = puertas
        self.llantas = llantas

    def __str__(self):
        return f'Clase: {self.__class__}\nColor: {self.color}\nPuertas: {self.puertas}\nLlantas: {self.llantas}'

def guardar(miVehiculo):

    partida = open("datosPartida", "wb")

    pickle.dump(miVehiculo, partida)

    partida.close()

def cargar():

    partida = open("datosPartida", "rb")

    datos = pickle.load(partida)

    partida.close()

    return datos

if __name__ == "__main__":
    main()
