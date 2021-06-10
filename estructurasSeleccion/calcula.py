'''
Pedir al usuario un valor. Si el valor es positivo, pedir un segundo valor y calcular la suma, resta y producto de
ambos. Mostrar los resultados por pantalla.
'''


def calcula(num1):
    if num1>=0:
        num2 = int(input("Número: "))
        suma = num1 + num2
        resta = num1 - num2
        mult = num1 * num2

        return f"Suma: {suma}", f"Resta: {resta}", f"Producto: {mult}"
    else:
        return "Ingrese un número positivo"


print(calcula(int(input("Número: "))))