class Libro:
    def __init__(self, 
                 titulo:str, 
                 autor:str,
                 anio_publicacion:int):
        self.titulo: str = titulo
        self.autor: str = autor
        self.anio_publicacion: int = anio_publicacion
    def show (self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año: {self.anio_publicacion}")

class Biblioteca:
    def __init__(self):
        self.libros = [] 
    def agregar_libro(self, libro):
        self.libros.append(libro)
    def mostrar_libros(self):
        for libro in self.libros:
            libro.show()
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

biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

biblioteca.mostrar_libros()
    
        