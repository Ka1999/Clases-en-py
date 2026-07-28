# Ejercicio: Tienda y Productos

# En este ejercicio practicarás nuevamente la composición entre clases. Crearás una clase llamada Producto, que tendrá los atributos nombre, precio y cantidad, además de un método show() para mostrar la información de cada producto.

# Después crearás una clase llamada Tienda, la cual almacenará una lista de objetos Producto. La tienda deberá permitir 
# agregar productos, 
# mostrar todos los productos registrados, 
# buscar un producto por su nombre y 
# actualizar la cantidad de un producto cuando sea necesario. Para buscar y actualizar utilizarás un recorrido con un for, una variable encontrado y la estructura que ya has practicado en los ejercicios anteriores.

# Al finalizar, crea tres productos, agrégalos a una tienda, muestra todos los productos, busca uno de ellos, actualiza la cantidad de un producto y vuelve a mostrar la lista para verificar que el cambio se realizó correctamente.

class Producto:
    def __init__(self, 
                 nombre,
                 precio,
                 cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    def show(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Cantidad: {self.cantidad}")

class Tienda:
    def __init__(self):
        self.producto = []
    def agregar_producto(self, elemento):
        self.producto.append(elemento)
    def mostrar_productos(self):
        for elemento in self.producto:
            elemento.show()
    def buscar_producto(self, elemento):
        eleccion = input("¿Qué producto quieres buscar?")
        encontrado = False
        for producto in self.producto:
            if producto.nombre == eleccion:
                elemento.show()
                encontrado = True
                break
            if not encontrado:
                print("Producto no existe")
    def actualizar_producto(self, elemento, nuevo_cambio):
        eleccion = input("¿Qué producto quieres actualizar?")
        encontrado = False
        for producto in self.producto:
            if producto.nombre == eleccion:
                nuevo_cambio = int(input("¿Cuál es la nueva duración? "))
                elemento.show()
                encontrado = True
                break
            if not encontrado:
                print("Producto no existe")

