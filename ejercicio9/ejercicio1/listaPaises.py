def main():

    lista = []
    while len(lista) <= 4:

        lista.append(input("Ingresa un pais: "))

    listaSet = set(lista)

    print(sorted(listaSet))

if __name__ == '__main__':
    main()