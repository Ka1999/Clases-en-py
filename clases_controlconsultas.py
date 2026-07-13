# Crea una clase llamada Mascota con los atributos nombre, especie, edad y consultas_pendientes.

# Luego crea un método llamado atender_consulta(cantidad) que verifique si la mascota tiene suficientes consultas pendientes. Si las tiene, debe descontar la cantidad indicada de consultas_pendientes y mostrar un mensaje informando que la consulta fue registrada con éxito. Si intenta registrar más consultas de las que tiene pendientes, debe mostrar un mensaje indicando que no es posible realizar la operación.

# Además, crea un método llamado mostrar() que imprima toda la información de la mascota.

class Mascota:
    def __init__(self, 
                 nombre: str,
                 especie: str,
                 edad: int,
                 consultas_pendientes: int):
        self.nombre: str = nombre
        self.especie: str = especie
        self.edad: int = edad
        self.consultas_pendientes: int = consultas_pendientes
    def atender_consulta(self, 
                         cantidad: int):
        if self.consultas_pendientes >= cantidad:
            self.consultas_pendientes -= cantidad
            print(f"La consulta para {self.nombre} fue registrada con éxito")
        else:
            print("No es posible realizar el registro")
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad}")
        print(f"Consultas pendientes: {self.consultas_pendientes}")

mascota1 = Mascota (nombre = "Mijo",
                    especie= "Perro",
                    edad= 5,
                    consultas_pendientes= 5)

mascota1.mostrar()
mascota1.atender_consulta(2)
mascota1.mostrar()
mascota1.atender_consulta(5)
mascota1.mostrar()     
        