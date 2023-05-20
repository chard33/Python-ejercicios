from functools import reduce
def main():

    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    print(aplicacion(lista))

def aplicacion(lista):

    lista = filter(lambda x: x % 2, lista)
    return reduce(lambda x, y: x + y, lista)

if __name__ == '__main__':
    main()