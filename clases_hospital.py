# Ejercicio: Hospital y Pacientes
# Enunciado
# Un hospital necesita administrar la información de sus pacientes.
# Crearás una clase llamada Paciente, que tendrá los atributos nombre, edad y diagnostico, además de un método show() para mostrar la información de cada paciente.

# Después crearás una clase llamada Hospital, la cual almacenará una lista de objetos Paciente. El hospital deberá permitir agregar pacientes, mostrar todos los pacientes registrados, buscar un paciente por su nombre, actualizar el diagnóstico de un paciente y eliminar un paciente de la lista. 
# Al finalizar, crea tres pacientes, agrégalos al hospital, muestra todos los pacientes, busca uno, actualiza su diagnóstico, elimina un paciente y vuelve a mostrar la lista para verificar que los cambios se realizaron correctamente.

class Paciente:
    def __init__(self,
                 nombre,
                 edad,
                 diagnostico):
        self.nombre = nombre
        self.edad = edad
        self.diagnostico = diagnostico

    def show(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Diágnostico: {self.diagnostico}")


class Hospital:
    def __init__(self):
        self.pacientes = []

    def agregar_paciente(self, elemento):
        self.pacientes.append(elemento)

    def mostrar_pacientes(self):
        for i in self.pacientes:
            i.show()

    def buscar_paciente(self):
        eleccion = input("¿Qué paciente buscas? ")
        encontrado = False

        for paciente in self.pacientes:
            if paciente.nombre == eleccion:
                paciente.show()
                encontrado = True
                break
        if not encontrado:
            print("No existe")

    def actualizar_paciente(self):
        eleccion = input("¿Qué paciente quieres actualizar? ") 
        encontrado = False  

        for paciente in self.pacientes:
            if paciente.nombre == eleccion:
                nuevo_cambio = input("¿Cuál es el nuevo diágnostico?") 
                paciente.diagnostico = nuevo_cambio
                print("Diágnostico actualizado.")
                encontrado = True
                break
        if not encontrado:
            print("No existe")
                       
    def eliminar_paciente(self):
        eleccion = input("¿Qué paciente quieres eliminar? ") 
        encontrado = False  

        for paciente in self.pacientes:
            if paciente.nombre == eleccion:
                self.pacientes.remove(paciente)
                encontrado = True
                break
        if not encontrado:
            print("No existe")


paciente1 = Paciente (nombre = "Nicolas",
                      edad = 28,
                      diagnostico = "Varicela")
paciente2 = Paciente (nombre = "Mariam",
                      edad = 48,
                      diagnostico = "Covid")
paciente3 = Paciente (nombre = "Jacob",
                      edad = 34,
                      diagnostico = "Contusión")

hospital = Hospital()

hospital.agregar_paciente(paciente1)
hospital.agregar_paciente(paciente2)
hospital.agregar_paciente(paciente3)

hospital.actualizar_paciente(paciente1)
hospital.eliminar_paciente(paciente1)
hospital.actualizar_paciente(paciente3)
        