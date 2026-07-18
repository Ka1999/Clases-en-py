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

libros.append(libro1)
libros.append(libro2)
libros.append(libro3)

titulo = input("Escribe que titulo quieres eliminar: ")

for libro in libros:
    if libro.titulo == titulo:
        libros.remove(libro)
        print(f"{titulo}, ha sido eliminado")
        break

for libro in libros:
    libro.show()