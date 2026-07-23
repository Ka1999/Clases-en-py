# Una empresa necesita administrar sus empleados.

# Cada Empleado tiene: nombre, cargo, salario
# La Empresa debe poder:
# Agregar empleados.
# Mostrar todos los empleados.
# Buscar un empleado por su nombre.
# Si lo encuentra, muestra la información.
# Si no lo encuentra, muestra:Empleado no encontrado.

class Empleado:
    def __init__(self,
                 nombre,
                 cargo,
                 salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario 

    def show(self):
        print(f"Nombre: {self.nombre}")
        print(f"Cargo: {self.cargo}")
        print(f"Salario: {self.salario}")


class Empresa:
    def __init__(self):
        self.empleados = []
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
    def mostrar_libros(self):
        for empleado in self.empleados:
            empleado.show()


        