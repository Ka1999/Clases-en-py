# Ejercicio: Crea una clase llamada Libro que tenga los atributos titulo y autor. Luego crea un método llamado mostrar() que imprima primero el título y después el autor. Finalmente, crea un objeto con el título "Harry Potter" y el autor "J. K. Rowling", y llama al método mostrar() para visualizar la información del libro. No ejecutes el programa hasta terminarlo y escríbelo completamente por tu cuenta.

class Libro:
    def __init__(self, 
                 titulo:str, 
                 autor:str):
        self.titulo: str = titulo
        self.autor: str = autor
    def mostrar(self):
        print("Titulo: ", self.titulo)
        print("Autor: ", self.autor)

libro1 = Libro("Harry Potter", "J. K. Rowling")
libro1.mostrar()

    
        