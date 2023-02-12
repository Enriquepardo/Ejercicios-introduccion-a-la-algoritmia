

def deco_precio_impuestos_incluidos(func):
    def wrapper():
        precio_sin_impuestos = float(input('Introduce el precio sin impuestos: '))
        porcentaje_IVA = float(input('Introduce el porcentaje de IVA: '))
        TII = precio_sin_impuestos + (precio_sin_impuestos * porcentaje_IVA / 100)

        print('El precio con impuestos incluidos es: ', TII)

    return wrapper


@deco_precio_impuestos_incluidos
def precio_con_impuestos_incluidos():
  pass

precio_con_impuestos_incluidos()


