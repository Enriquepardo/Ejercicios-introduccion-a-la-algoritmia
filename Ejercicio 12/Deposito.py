
def verificar_saldo(func):
    def wrapper(self, cantidad):
        if self.saldo - cantidad < 0 and self.descubierto_autorizado == 0:
            print("No se puede retirar esa cantidad, saldo insuficiente")
        elif self.saldo - cantidad < -self.descubierto_autorizado:
            print("No se puede retirar esa cantidad, descubierto autorizado insuficiente")
        else:
            func(self, cantidad)
    return wrapper
def preguntar_retirar_dinero():
    respuesta = input("Desea retirar dinero? (S/N): ")
    if respuesta == "S":
        dinero_a_retirar = float(input("Ingrese el dinero a retirar: "))
        cuenta.retirar(dinero_a_retirar)
        preguntar_retirar_dinero()
    elif respuesta == "N":
        print("Gracias por utilizar nuestros servicios")
    else:
        print("Ingrese una respuesta valida")
        preguntar_retirar_dinero()
class Cuenta:
    def __init__(self, saldo, descubierto_autorizado=0):
        self.saldo = saldo
        self.descubierto_autorizado = descubierto_autorizado

    @verificar_saldo
    def retirar(self, cantidad):
        self.saldo -= cantidad
        print(f"Se ha retirado {cantidad} del saldo, su nuevo saldo es: {self.saldo}")
    

    

saldo_cuenta = float(input("Ingrese el saldo de la cuenta: "))
cuenta = Cuenta(saldo_cuenta)
preguntar_retirar_dinero()
