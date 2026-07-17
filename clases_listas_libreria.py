# Una biblioteca tiene registrados varios libros.
# Crea una clase llamada Libro con los atributos titulo, autor y anio_publicacion. 
# Luego crea un método mostrar() que imprima la información del libro.
# Después:
# Crea una lista vacía llamada libros.
# Crea cuatro libros (los datos los eliges tú).
# Agrega los cuatro libros a la lista usando append().
# Recorre la lista con un for.
# Dentro del for, utiliza un if para buscar el libro cuyo título sea "Frankenstein".
# Cuando lo encuentre, llama al método mostrar() para mostrar únicamente ese libro.
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
libros.append(libro1)
libros.append(libro2)
libros.append(libro3)
libros.append(libro4)
libros.append(libro5)

for libro in libros:
    if libro.titulo == "Frankenstein":
        libro.show()
    
        
        