'''
Un año es bisiesto si es divisible por 4 y no es por 100, o si es divisible por 400. Escribe un programa que lea un año y devuelva si es bisiesto o no.
'''

def bisiesto(anio):
    return True if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0 else False
        
print(bisiesto(int(input("Ingrese un año: "))))