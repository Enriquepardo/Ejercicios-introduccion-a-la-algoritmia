

def media_aritmetica_decorator(func):
    def wrapper():
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        num3 = float(input("Introduce el tercer número: "))

        resultado = func(num1, num2, num3)

        print("La media aritmética es:", resultado)

    return wrapper

@media_aritmetica_decorator
def media_aritmetica(num1, num2, num3):
    return (num1 + num2 + num3) / 3

media_aritmetica()
