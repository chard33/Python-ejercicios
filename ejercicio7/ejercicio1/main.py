import operaciones as oper
def principal():
    print(f'La suma es: {oper.sumar(3,3)}')
    print(f'La resta es: {oper.restar(3,3)}')
    print(f'La multiplicacion es: {oper.multiplicar(3,3)}')
    print(f'La division es: {oper.dividir(3,3)}')

if __name__ == '__main__':
    principal()