# Crea una clase llamada CuentaBancaria. En el método __init__ define los atributos titular y saldo. Luego crea un método llamado consignar(valor) que aumente el saldo de la cuenta con el valor recibido. Después crea otro método llamado mostrar_informacion() que muestre el nombre del titular y el saldo actual. Finalmente, crea un objeto, realiza una consignación y muestra la información de la cuenta.

class CuentaBancaria:
    def __init__(self,
                 titular: str,
                 saldo: int):
        self.titular:str = titular
        self.saldo:int = saldo
    def consignar(self, valor):
        self.saldo += valor
    def mostrar_informacion(self):
        print("Titular: ", self.titular)
        print("Saldo: ", self.saldo)

cliente1 = CuentaBancaria(titular= "Luna Quintero",
                        saldo= 50000)
cliente1.consignar(200)
cliente1.mostrar_informacion()