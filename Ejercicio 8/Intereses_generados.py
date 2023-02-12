
def deco_intereses_generados(func):
  def wrapper():
    capital = float(input("Introduce el capital: "))
    tasa_interes = float(input("Introduce la tasa de interés: "))
    tiempo_en_meses = float(input("Introduce el tiempo en meses: "))

    intereses = capital * tasa_interes * tiempo_en_meses / 100 / 12

    print("El importe de los intereses generados es:", intereses)

  return wrapper

@deco_intereses_generados
def intereses_generados():
  pass

intereses_generados()
