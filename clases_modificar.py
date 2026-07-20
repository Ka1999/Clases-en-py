# Crea una clase llamada Pelicula con los atributos: titulo director duracion
# Agrega un método show() para mostrar toda la información.
# Luego:
# Crea 3 películas. Guárdalas en una lista llamada peliculas. Pide al usuario el título de una película. Si la película existe, pregunta por la nueva duración.
# Cambia la duración de esa película.
# Muestra el mensaje:Duración actualizada.Finalmente, muestra todas las películas para comprobar que el cambio sí se hizo.

class Pelicula:
    def __init__(self, 
                 titulo: str,
                 director: str,
                 duracion: int):
        self.titulo: str = titulo
        self.director: str = director
        self.duracion: int = duracion


    def show(self):
        print(f"TITULO: {self.titulo}")
        print(f"DIRECTOR: {self.director}")
        print(f"DURACIÓN: {self.duracion}")

    def cambiar_duracion(self, nueva_duracion):
        self.duracion = nueva_duracion

peliculas =[]

pelicula1 = Pelicula(
    titulo= "Interestelar",
    director= "Christopher Nolan",
    duracion= 169
)

pelicula2 = Pelicula(
    titulo= "Toy Story",
    director= "John Lasseter",
    duracion= 81
)

pelicula3 = Pelicula(
    titulo= "Titanic",
    director= "James Cameron",
    duracion= 194
)
        
peliculas.append(pelicula1)
peliculas.append(pelicula2)
peliculas.append(pelicula3)

eleccion = input("¿Qué pelicula quieres cambiar?")

encontrado = False

for i in peliculas:
    if i.titulo == eleccion:
        nueva_duracion = int(input("¿Cuál es la nueva duración? "))
        i.cambiar_duracion(nueva_duracion)
        encontrado = True
        break

if not encontrado:
        print("No existe esa pelicula")

for pelicula in peliculas:
    pelicula.show()
    