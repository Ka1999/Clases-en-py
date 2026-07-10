# Crea una clase llamada Empleado que tenga los atributos nombre, cargo y salario. Luego crea un método llamado aumentar_salario(valor) que sume el valor recibido al salario del empleado, y un método mostrar() que imprima el nombre, el cargo y el salario actualizado. Finalmente, crea un objeto llamado empleado1 con el nombre "Karen", el cargo "Desarrolladora Python" y un salario de 3.500.000. Después aumenta el salario en 500.000 y muestra la información final del empleado.
class Empleado: 
    def __init__(self,
                 nombre: str,
                 cargo: str,
                 salario: int):
        self.nombre: str = nombre
        self.cargo: str = cargo
        self.salario: int = salario
    def aumentar_salario(self, valor):
        self.salario += valor
    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Cargo: ", self.cargo)
        print("Salario: ", self.salario)
empleado1 = Empleado(nombre="Karen Vanessa González Alarcón",
                     cargo="Desarrolladora de Python",
                     salario=7000000)
empleado1.aumentar_salario(500000)
empleado1.mostrar()


