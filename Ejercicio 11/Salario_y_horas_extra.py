

salario_bruto = float(input('Ingrese el salario bruto: '))
horas_extra = int(input('Ingrese las horas extra: '))


def aumento_salario_extra(func):
    def wrapper(salario_bruto, horas_extra):
        tarifa_hora = salario_bruto / (35 * 52)
        if horas_extra <= 8:
            return 0
        else:
            salario_extra = func(tarifa_hora, horas_extra)
            return salario_extra
    return wrapper

@aumento_salario_extra
def calcular_salario_extra(tarifa_hora, horas_extra):
    if horas_extra <= 36:
        return (horas_extra - 8) * tarifa_hora
    elif horas_extra <= 43:
        return (36 - 8) * tarifa_hora + (horas_extra - 36) * tarifa_hora * 1.25
    else:
        return (36 - 8) * tarifa_hora + (43 - 36) * tarifa_hora * 1.25 + (horas_extra - 43) * tarifa_hora * 1.5



print(calcular_salario_extra(salario_bruto, horas_extra))
