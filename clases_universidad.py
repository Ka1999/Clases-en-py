# Enunciado
# Una universidad necesita un sistema para administrar sus estudiantes.
# Cada Estudiante debe almacenar:
# Nombre.
# Carrera.
# Semestre.
# La Universidad debe poder:
# Agregar estudiantes.
# Mostrar todos los estudiantes.
# Buscar un estudiante por su nombre.
# Si el estudiante existe, debe mostrar toda su información.
# Si no existe, debe mostrar un mensaje indicando que no fue encontrado.

class Estudiante:
    def __init__(self, nombre, carrera, semestre):
        self.nombre = nombre
        self.carrera = carrera
        self.semestre = semestre


    def show(self):
        print(f"Nombre del estudiante: {self.nombre}")
        print(f"Carrera del estudiante: {self.carrera}")
        print(f"Semestre del estudiante: {self.semestre}")


class Universidad:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
        for estudiante in self.estudiantes:
            estudiante.show()

    def buscar_estudiante(self, nombre):
        encontrado = False
        for estudiante in self.estudiantes:
            if estudiante.nombre == nombre:
                estudiante.show()
                encontrado = True
                break
        if not encontrado:
            print("El estudiante no existe")

estudiante1 = Estudiante (nombre= "Anasol Quintero González",
                          carrera= "Medicina",
                          semestre=8)
estudiante2 = Estudiante (nombre= "Luna Quintero González",
                          carrera= "Derecho",
                          semestre=6)
estudiante3 = Estudiante (nombre= "Ángel Quintero González",
                          carrera= "Piloto",
                          semestre=4)

universidad = Universidad()
universidad.agregar_estudiante(estudiante1)
universidad.agregar_estudiante(estudiante2)
universidad.agregar_estudiante(estudiante3)

universidad.mostrar_estudiantes()

nombre = input("¿Qué estudiante deseas buscar? ")

universidad.buscar_estudiante(nombre)