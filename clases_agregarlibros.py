# Ejercicio: Agregar un nuevo libro
# Ya tienes una biblioteca con 5 libros.
# Ahora vas a hacer que el usuario pueda agregar un sexto libro.
# Objetivo Al ejecutar el programa, debe preguntar algo como:
# Ingrese el título del libro:
# Ingrese el autor:
# Ingrese el año de publicación:
# Con esos datos debes: Guardar la información en variables.
# Crear un nuevo objeto Libro.
# Agregar ese objeto a la lista libros usando append().
class Libro: 
    def __init__(self,
                 titulo: str,
                 autor: str,
                 anio_publicacion: int):
        self.titulo: str = titulo
        self.autor: str = autor
        self.anio_publicacion: int = anio_publicacion
    

    def show(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.anio_publicacion}")

libros=[]
libro1 = Libro(
    titulo= "La caída",
    autor= "Albert Camus",
    anio_publicacion=1956
)

libro2 = Libro(
    titulo= "Cien años de soledad",
    autor= "Gabriel García Marquéz",
    anio_publicacion=1967
)

libro3 = Libro(
    titulo="Harry Potter y la piedra filosofal",
    autor="J. K. Rowling",
    anio_publicacion=1997
)

libro4 = Libro(
    titulo="La casa de los espíritus",
    autor="Isabel Allende",
    anio_publicacion=1982
)

libro5 = Libro(
    titulo="Frankenstein",
    autor="Mary Shelley",
    anio_publicacion=1818
)

libro6 = Libro(
    titulo = input("Ingrese el título del libro: "),
    autor = input("Ingrese el autor del libro: "),
    anio_publicacion = int(input("Ingrese el año de publicación del libro: "))
)
libros.append(libro1)
libros.append(libro2)
libros.append(libro3)
libros.append(libro4)
libros.append(libro5)
libros.append(libro6)

libro6.show()

for libro in libros:
        libro.show()