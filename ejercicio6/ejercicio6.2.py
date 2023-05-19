class Alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f'Nombre alumno: {self.nombre}')
        print(f'Nota alumno: {self.nota}')

    def resultado(self):
        return "Aprobado" if self.nota >= 6 else "Reprobado"

alumno = Alumno("Carlos", 8.5)

alumno.imprimir()

print(alumno.resultado())