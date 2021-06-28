'''
Calcular el salario neto de un trabajador de una empresa cuyo trabajo se paga por horas. Introducir por teclado el número de horas y el precio de la hora. El cálculo se realiza del siguiente modo:
    • Las primeras 35 horas de cada semana se pagan a la tarifa normal (suponer 4 semanas al mes).
    • Las horas extras se pagan un 50% más que las normales.
    • Los impuestos a deducir a los trabajadores varían en función de su sueldo mensual (considerando las horas extras trabajadas):
        • Si el sueldo es menor de € 600, libre de impuestos.
        • Si el sueldo está entre € 600 y € 1000, los impuestos son el 20%.
        • Si el sueldo es mayor de € 1000, el 30%.
'''

def costoHora(cantHoras):
    if cantHoras > 35*4:
        return 35*4 + (cantHoras-35*4)*1.5
    else:
        return cantHoras

def impuestos(sueldoMensual):
    if 600 <= sueldoMensual <= 1000:
        return sueldoMensual*0.2
    elif sueldoMensual > 1000:
        return sueldoMensual*0.3

def salarioTrabajador(cantHoras, precioHora):
    sueldo = precioHora*costoHora(cantHoras)
    return sueldo-impuestos(sueldo)

print(salarioTrabajador(int(input("Ingrese la cantidad de horas trabajadas: ")),float(input("Ingrese el precio de cada hora: "))))