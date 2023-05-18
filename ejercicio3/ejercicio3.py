# Ejercicio 3

peso = float(input("Cual es tu peso en Kilogramos: "))

altura = float(input("Cual es tu estatura en Metros: "))

imc = round(peso / pow(altura, 2), 2)

print(f'Tu índice de masa corporal es: {imc}')
