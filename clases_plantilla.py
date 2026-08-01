# Una veterinaria necesita administrar las mascotas que atiende.

# Crearás una clase llamada Mascota, con los atributos nombre, especie y edad. Además, tendrá un método show() para mostrar la información de cada mascota.

# Después crearás una clase llamada Veterinaria, que almacenará una lista de objetos Mascota. La veterinaria deberá permitir agregar mascotas, mostrar todas las mascotas, buscar una mascota por su nombre, actualizar la edad de una mascota y eliminar una mascota.

# Al finalizar, crea tres mascotas, agrégalas a la veterinaria, muestra todas, busca una, actualiza la edad de una mascota, elimina una mascota y vuelve a mostrar la lista.

class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def show(self):
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad}")


class Veterinaria:
    def __init__(self):
        self.mascotas = []

    def agregar_mascota(self, elemento):
        self.mascotas.append(elemento)

    def mostrar_mascotas(self):
        for i in self.mascotas:
            i.show()

    def buscar_mascota(self):
        eleccion = input("¿Cuál es el nombre de la mascota? ")
        encontrado = False

        for i in self.mascotas:
            if i.nombre == eleccion:
                encontrado = True
                i.show()
                break
        if not encontrado:
            print("Mascota no encontrada")

    def actualizar_mascota(self):
        eleccion = input("¿Cuál es el nombre de la mascota que quieres cambiar? ")
        encontrado = False

        for i in self.mascotas:
            if i.nombre == eleccion:
                nuevo_cambio = input("¿Cuál es la edad que quieres actualizar?: ")
                i.edad == nuevo_cambio
                encontrado = True
                print("Cambio realizado")
                break
        if not encontrado:
            print("Mascota no encontrada")       

    def eliminar_mascota(self):
        eleccion = input("¿Cuál es el nombre de la mascota que quieres cambiar? ")
        encontrado = False