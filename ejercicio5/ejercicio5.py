# Ejercicio 5

añoBisiesto = int(input("Ingrese el año a consultar: "))

print(f'El año {añoBisiesto} es bisiesto' if añoBisiesto % 4 == 0 and añoBisiesto % 100 != 0 or añoBisiesto % 400 == 0 else f'El año {añoBisiesto} no es bisiesto')
