def main():

    texto = [f'Hola, {input("Ingresa tu nombre: ")}!']
    archivo = escritura("archivo.txt", texto)


def escritura(fichero, texto):

    archivo = open(fichero, "w")

    for linea in texto:
        archivo.write(f'{linea}\n')

    archivo.close()

    print("Archivo creado")

if __name__ == "__main__":
    main()

