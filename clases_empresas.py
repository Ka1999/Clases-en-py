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
    def mostrar_empleado(self):
        for empleado in self.empleados:
            empleado.show()
    def buscar_empleado(self):
        eleccion = input("¿Qué empleado quieres buscar?")
        encontrado = False
        for empleado in self.empleados:
            if empleado.nombre == eleccion:
                empleado.show()
                encontrado = True
                break
            if not encontrado:
                print("No existe")
            
empleado1 = Empleado(nombre= "Karen Vanessa González Alarcón",
                     cargo= "Analista de datos PY",
                     salario=7500000)
empleado2 = Empleado(nombre= "Andrea Correo",
                     cargo= "Cantante",
                     salario=6500000)

empresa = Empresa()
empresa.agregar_empleado(empleado1)
empresa.agregar_empleado(empleado2)

empresa.mostrar_empleado()

empresa.buscar_empleado()

        