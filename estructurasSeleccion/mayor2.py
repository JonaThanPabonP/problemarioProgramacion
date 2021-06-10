'''
Calcula el mayor de n números enteros ingresados por teclado.
'''

def mayor(n):
    lista = [int(input("Número: ")) for i in range(n)]
    return max(lista)

print(mayor(int(input("Ingrese la cantidad de números que quiere agregar: "))))