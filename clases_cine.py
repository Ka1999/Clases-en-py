# Un cine necesita llevar el control de las sillas disponibles para una función.
# Crea una clase llamada SalaCine con los atributos nombre_pelicula, hora y sillas_disponibles.
# Luego crea un método llamado reservar(cantidad) que verifique si hay suficientes sillas para realizar la reserva. Si las hay, debe descontar la cantidad de sillas reservadas y mostrar un mensaje indicando que la reserva fue exitosa. Si no hay suficientes sillas, debe informar que no es posible realizar la reserva.
# Además, crea un método llamado mostrar() que imprima el nombre de la película, la hora de la función y la cantidad de sillas disponibles.
# Finalmente:
# Crea una sala para la película "Lilo & Stitch" a las 7:00 p. m. con 30 sillas disponibles.
# Muestra la información.
# Reserva 8 sillas.
# Vuelve a mostrar la información.
# Intenta reservar 25 sillas.
# Muestra nuevamente la información.
class SalaCine:
    def __init__(self, 
                 nombre_pelicula: str, 
                 hora: str, 
                 sillas_disponibles: int):
        self.nombre_pelicula: str = nombre_pelicula
        self.hora: str = hora
        self.sillas_disponibles: int = sillas_disponibles
    def reservar(self, cantidad):
        if self.sillas_disponibles >= cantidad:
            self.sillas_disponibles -= cantidad
            print(f"La reserva para la película {self.nombre_pelicula}, fue exitosa")
        else:
            print(f"La reserva para la película {self.nombre_pelicula} no fue exitosa")
    def mostrar(self):
        print(f"Película: {self.nombre_pelicula}")
        print(f"Hora: {self.hora}")
        print(f"Sillas disponibles: {self.sillas_disponibles}")

pelicula1 = SalaCine(nombre_pelicula= "Lilo y Stitch",
                     hora= "19:00",
                     sillas_disponibles= 30)

pelicula1.mostrar()
pelicula1.reservar(8)
print("_________________________")
pelicula1.mostrar()        
pelicula1.reservar(25)
pelicula1.mostrar()
        