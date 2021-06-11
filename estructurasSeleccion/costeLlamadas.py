'''
Escribir un programa que permita determinar la cantidad total a pagar por una llamada telefónica de N minutos (introducido por el usuario), teniendo en cuenta lo siguiente:
• Las llamadas de 5 minutos o menos tienen un coste de 10 BsF.
• Cada minuto adicional a partir de los 5 primeros cuesta 2 BsF.
'''

def costeLlamadas(N):
    total = 10
    extra = 2
    if N<=5:
        return f"Costo de la llamada: {total} BsF"
    elif N > 5:
        total = total + (N-5)*extra
        return f"Costo de la llamada: {total} BsF"
    else:
        return "Ingrese una cantidad entera positiva."


print(costeLlamadas(int(input("Ingrese la cantidad de minutos que tardó la llamada: "))))