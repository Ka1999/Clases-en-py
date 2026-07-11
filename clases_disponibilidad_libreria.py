# Una biblioteca necesita administrar los préstamos de libros. Crea una clase llamada Libro con los atributos titulo, autor y disponible (este último debe indicar si el libro está disponible con un valor True o False). 
# Luego crea un método llamado prestar() que verifique si el libro está disponible. Si lo está, debe imprimir "Libro prestado con éxito" y cambiar el valor de disponible a False. Si no está disponible, debe imprimir "El libro no está disponible". También crea un método mostrar() que imprima toda la información del libro. Finalmente, crea un libro, muestra su información, intenta prestarlo dos veces seguidas y observa qué sucede.
class Libro:
    def __init__(self,
                 titulo: str,
                 autor: str,
                 disponible: bool):
        self.titulo: str = titulo
        self.autor: str = autor
        self.disponible: bool = disponible
    def prestar(self):
        if self.disponible:
            print(f"{self.titulo} fue prestado con éxito.")
            self.disponible = False
        else:
            print(self.titulo, "El libro no está disponible")
    def mostrar(self):
        print("Titulo: ", self.titulo)
        print("Autor: ", self.autor)
        print("Disponibilidad: ", self.disponible)

        if self.disponible:
            print("Disponibilidad: Disponible")
        else:
            print("Disponibilidad: No disponible")
libro1 = Libro ("Harry Potter", "J. K. Rowling",True)
libro1.mostrar()
libro1.prestar()
libro1.mostrar()
libro1.prestar()
