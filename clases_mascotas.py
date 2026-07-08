#Ejercicio 1
#Crea una clase llamada Mascota. En el método __init__ define los atributos nombre, edad y peso. Luego crea un método llamado mostrar_informacion() que muestre esos tres atributos utilizando self. Después crea tres objetos llamados Luna, Max y Toby con los datos que prefieras y, al final, llama el método mostrar_informacion() para cada uno de ellos.

class Mascota:
    def __init__(self, 
                nombre:str, 
                edad:int,
                peso:int):
        self.nombre: str = nombre
        self.edad: int = edad
        self.peso: int = peso
    
    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Peso:", self.peso)

mascota = Mascota(nombre = "Luna",
                   edad= 5,
                   peso= 7)

mascota2 = Mascota(nombre = "Max",
                   edad= 10,
                   peso= 2)

mascota3 = Mascota(nombre = "Luna",
                   edad= 5,
                   peso= 7)

mascota.mostrar_informacion()
mascota2.mostrar_informacion()
mascota3.mostrar_informacion()

