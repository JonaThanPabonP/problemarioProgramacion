'''
En una empresa cada empleado debe teclear un código identificador de 3 cifras en la entrada. Escribir un programa que muestre por pantalla la categoría del empleado teniendo en cuenta que:
    • Si el código es divisible por 2, por 3 y por 5, la categoría del empleado es “Director general”.
    • Si el código es divisible por 3 y por 5 pero no por 2, la categoría del empleado es “Directivo”.
    • Si el código es divisible por 2, pero no por 3 ni por 5, la categoría del empleado es “Staff”.
    • Si el código no es divisible por 2, ni por 3 ni por 5, la categoría del empleado es “Seguridad”.
Recuerde que: Un numero X es divisible por otro Y; si X mod Y = 0.
'''



def categoriaEmpleado(codigo):
    if codigo%2==0 and codigo%3==0 and codigo%5==0:
        return "Director general"
    elif codigo%3==0 and codigo%5==0:
        return "Directivo"
    elif codigo%2==0:
        return "Staff"
    else:
        return "Seguridad"

print(categoriaEmpleado(int(input("Ingrese su código identificador: "))))