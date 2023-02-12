import functools

def area_triangulo(func):
    def wrapper(base, altura):
        return 0.5 * func(base, altura)
    return wrapper

@area_triangulo
def area_triangulo_base_altura(base, altura):
    return base * altura

@area_triangulo
def area_triangulo_lados(lado1, lado2):
    return lado1 * lado2 / 2

base = float(input("Ingrese la medida de la base: "))
altura = float(input("Ingrese la medida de la altura: "))

area1 = area_triangulo_base_altura(base, altura)
print("El área del triángulo es", area1)

lado1 = float(input("Ingrese la medida de uno de los lados: "))
lado2 = float(input("Ingrese la medida del otro lado: "))

area2 = area_triangulo_lados(lado1, lado2)
print("El área del triángulo es", area2)

