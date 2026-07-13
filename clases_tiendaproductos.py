# Una tienda quiere administrar sus productos. Crea una clase llamada Producto con los atributos nombre, precio y stock (cantidad disponible). 
# Luego crea un método llamado vender(cantidad) que verifique si hay suficiente stock para realizar la venta. 
# Si lo hay, debe descontar la cantidad vendida del stock e imprimir un mensaje indicando que la venta fue exitosa. Si no hay suficiente stock, debe imprimir un mensaje informando que no es posible realizar la venta. Además, crea un método mostrar() que imprima toda la información del producto. 
# Finalmente, crea un producto con los datos que desees, muestra su información, realiza una venta de algunas unidades, vuelve a mostrar la información y luego intenta vender una cantidad mayor al stock disponible.

class Producto:
    def __init__(self,
                 nombre:str,
                 precio:float,
                 stock:int):
        self.nombre:str = nombre
        self.precio:float = precio
        self.stock:int = stock
    def vender(self, cantidad):
        if  self.stock >= cantidad :
            self.stock -= cantidad        
            print("Venta realizada con éxito")
        else:
            print("No hay suficiente stock")
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Stock: {self.stock}")
producto1 = Producto(nombre="Shampoo", 
                     precio=45000, 
                     stock=5)
producto1.mostrar()
print("----------------")
producto1.vender(3)
print("----------------")
producto1.mostrar()
print("----------------")
producto1.vender(10)  
print("----------------")
producto1.mostrar()
        