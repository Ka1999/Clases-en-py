# Crea una clase llamada Mascota con los atributos nombre, especie y edad, y un método llamado show() que muestre toda la información de la mascota. 
# Luego crea tres objetos de tipo Mascota, guárdalos en una lista llamada mascotas y pide al usuario que escriba el nombre de la mascota que desea eliminar. Recorre la lista para buscar la mascota por su nombre y, si la encuentras, elimínala de la lista y muestra el mensaje "Mascota eliminada.". Finalmente, recorre nuevamente la lista e imprime todas las mascotas que quedaron utilizando el método show().

class Mascota:
    def __init__(self,
                 nombre: str,
                 especie: str,
                 edad: int):
        self.nombre: str = nombre
        self.especie: str = especie
        self.edad: int = edad

    def show(self):
        print(f"Nombre de la mascota {self.nombre}")
        print(f"Especie de la mascota {self.especie}")
        print(f"Edad de la mascota {self.edad}")

mascotas=[]
mascota1 = Mascota(nombre="Mija",
                   especie="Perro",
                   edad=4) 

mascota2 = Mascota(nombre="Mishi",
                   especie="Gato",
                   edad=2) 
mascota3 = Mascota(nombre="Coco",
                   especie="Loro",
                   edad=6)  
   
mascotas.append(mascota1)
mascotas.append(mascota2)
mascotas.append(mascota3)

nombre = input("Pon el nombre de la mascota que quieres eliminar: ")

for animal in mascotas:
    if animal.nombre == nombre:
        mascotas.remove(animal)
        print(f"{nombre} fue eliminado")
        break

for i in mascotas:
    i.show()