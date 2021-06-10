'''
Determinar en que estado está el agua en función de su temperatura. Si es negativa el estado será sólido, si es menor que 100 será líquido y si es mayor que 100 será gas. Pedir al usuario el valor de la temperatura.
'''


def estadoAgua(temperatura):
    try:
        if temperatura > 0 and temperatura < 100:
            return "Líquido"
        elif temperatura>=100:
            return "Gas"
        else:
            return "Sólido"
    except:
        "Valor ingresado no válido."

print(estadoAgua(int(input("Ingrese la tempratura del agua: "))))