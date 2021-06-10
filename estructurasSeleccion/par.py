'''
Escribir un programa que solicite un valor entero al usuario y determine si es par o impar.
'''
def esPar(num):
    try:
        return "Par" if num%2==0 else "Impar"
    except Exception:
        return "Valor de entrada no válido."

print(esPar(int(input("Número: "))))