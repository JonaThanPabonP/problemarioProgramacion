'''
Escribir un programa que solicite un valor entero al usuario y determine si es par o impar.
'''
try:
    print("Par" if int(input("Número: "))%2==0 else "Impar")
except Exception:
    print("Valor de entrada no válido.")