# Crea una clase llamada Producto con los atributos nombre, precio y cantidad. Agrega un método llamado show() que muestre toda la información del producto. Luego crea tres productos, guárdalos en una lista llamada productos y pide al usuario el nombre del producto que desea buscar. Si el producto existe, muestra toda su información usando show(). Si no existe, muestra el mensaje "Producto no encontrado"
class Producto:
    def __init__(self,
                 nombre: str,
                 precio: str,
                 cantidad: int):
        self.nombre: str = nombre
        self.precio: str = precio
        self.cantidad: int = cantidad
    
    def show(self):
        print(f"Nombre del producto: {self.nombre}")
        print(f"Precio del producto: {self.precio}")
        print(f"Cantidad del producto: {self.cantidad}")

productos = []

producto1 = Producto(nombre="Gel de rizos",
                     precio= 45000,
                     cantidad= 5
)
producto2 = Producto(nombre="Difusor",
                     precio= 15000,
                     cantidad= 2
)
producto3 = Producto(nombre="Crema de peinar de rizos",
                     precio= 25000,
                     cantidad= 25
)

productos.append(producto1)
productos.append(producto2)
productos.append(producto3)     

eleccion = input("Elige un producto: ")
encontrado = False

for elemento in productos:
    if elemento.nombre == eleccion:
        elemento.show()
        encontrado = True
if not encontrado:
        print("No existe el producto")
