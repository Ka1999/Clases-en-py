# Una universidad quiere llevar el registro de sus estudiantes. Crea una clase llamada Estudiante con los atributos nombre, programa y promedio. Luego crea un método llamado aprobo() que imprima "Aprobó la materia" si el promedio es mayor o igual a 3.0; de lo contrario, debe imprimir "No aprobó la materia". 
# Además, crea un método mostrar() que muestre toda la información del estudiante. Finalmente, crea un objeto con los datos que desees, llama primero al método mostrar() y luego al método aprobo().
class Estudiante:
    def __init__(self,
                 nombre: str,
                 programa: str,
                 promedio: float):
        self.nombre: str = nombre
        self.programa: str = programa
        self.promedio: float = promedio
    def aprobo(self):
        if self.promedio >= 3.0:
            print("Aprobó la materia: ", self.promedio)
        else:
            print("No aprobó la materia: ", self.promedio)
    def mostrar(self):
        print("Nombre de estudiante: ", self.nombre)
        print("Programa: ", self.programa)
        print("Promedio: ", self.promedio)
estudiante1 = Estudiante (nombre= "Anasol Quintero González",
                          programa= "Medicina",
                          promedio= 4.8)
estudiante2 = Estudiante (nombre= "Camila",
                          programa= "Medicina",
                          promedio= 2.8)
estudiante1.mostrar()
estudiante1.aprobo()
estudiante2.mostrar()
estudiante2.aprobo()

        