class Estudiante: 
    def __init__(self, nombre):
        self.nombre = nombre

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre


estudiante1 = Estudiante("Flying")
estudiante2 = Estudiante("Zowie")
estudiante3 = Estudiante("Astrobot")
estudiante4 = Estudiante("Astrobot")
estudiante4.cambiar_nombre("Karencita")


print("Hola", Estudiante)