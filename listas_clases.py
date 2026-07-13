# Una tienda de videojuegos quiere guardar todos los videojuegos registrados.

# Crea una clase llamada Videojuego con los atributos nombre, genero y precio. Luego crea un método mostrar() que imprima la información del videojuego. Después, crea una lista vacía llamada videojuegos, crea tres objetos con la información que tú quieras y agrégalos a la lista utilizando append(). Al final, imprime la lista con print(videojuegos).

class Videojuego:
    def __init__(self, 
                 nombre: str,
                 genero: str,
                 precio: int):
        self.nombre: str = nombre
        self.genero: str = genero
        self.precio: int = precio
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Genero: {self.genero}")
        print(f"Precio: {self.precio}")
videojuegos=[]
videojuego1 = Videojuego(
    nombre="Stardew Valley", 
    genero="Simulación",
    precio=45000
)
videojuego2 = Videojuego(
    nombre="The Last of Us",
    genero="Acción",
    precio=250000
)
videojuego3 = Videojuego(
    nombre="Minecraft",
    genero="Sandbox",
    precio=120000
)

videojuegos.append(videojuego1)
videojuegos.append(videojuego2)
videojuegos.append(videojuego3)

for videojuego in videojuegos:
    videojuego.mostrar()

print(videojuegos)