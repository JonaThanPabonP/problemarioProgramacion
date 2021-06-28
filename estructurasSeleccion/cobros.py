'''
Una empresa de préstamos decidió cambiar su esquema de cobros así:
• Si el préstamo es de más de 5000 euros, cobra en tres cuotas
• Si el préstamo es de menos de 1000 euros, cobra en una cuota
• Si el préstamo es entre 2000 y 3000 euros cobra en dos cuotas
• En los demás casos cobra en cinco cuotas
Adicionalmente, si es de menos de 4000 euros cobra el 12% de interés, en caso contrario cobra el 10% de interés.
El programa debe decir en cuántas cuotas debe pagar y de cuánto es cada cuota. Para ello, se calcula el valor total de la deuda con interés y se divide en cuotas iguales.
'''

def cuotas(prestamo):
    if prestamo > 5000:
        return 3
    elif prestamo < 1000:
        return 1
    elif 2000 < prestamo < 3000:
        return 2
    else:
        return 5

def interes(prestamo):
    if prestamo < 4000:
        return 0.12
    else:
        return 0.1

def cobro(prestamo):
    cantCuotas = cuotas(prestamo)
    costoInteres = interes(prestamo)
    precioCuota = prestamo*(1+costoInteres)/cantCuotas
    return f"Debe cancelar {cantCuotas} cuotas de {precioCuota} euros cada una."

print(cobro(float(input("Ingrese el valor del préstamo: "))))
