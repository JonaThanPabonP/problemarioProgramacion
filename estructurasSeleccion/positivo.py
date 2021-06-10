'''
Escribir un programa que solicite un valor entero al usuario y determine si es positivo o negativo.
'''

def esPositivo(num):
    try:
        return "Positivo" if num>=0 else "Negativo"
    except Exception:
        return "Valor de entrada no válido."

print(esPositivo(int(input("Número: "))))