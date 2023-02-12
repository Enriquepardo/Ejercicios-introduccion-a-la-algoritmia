import functools

def media_ponderada_decorator(func):
    def wrapper():
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        num3 = float(input("Introduce el tercer número: "))
        coef1 = float(input("Introduce el primer coeficiente de ponderación: "))
        coef2 = float(input("Introduce el segundo coeficiente de ponderación: "))
        coef3 = float(input("Introduce el tercer coeficiente de ponderación: "))

        resultado = func(num1, num2, num3, coef1, coef2, coef3)

        print("La media ponderada es:", resultado)

    return wrapper

@media_ponderada_decorator
def media_ponderada(num1, num2, num3, coef1, coef2, coef3):
    return (num1 * coef1 + num2 * coef2 + num3 * coef3) / (coef1 + coef2 + coef3)

media_ponderada()
