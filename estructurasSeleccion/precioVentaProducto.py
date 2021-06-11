'''
El dueño de una papelería desea un programa que le indique el precio de venta de un artículo dado. El precio se calcula de acuerdo con la siguiente fórmula: PVP = precio_coste + ganancia. Donde la ganancia será:
• El 15% si el precio de coste es inferior Bs. 3.
• 50 céntimos si el precio de coste está entre Bs. 3 y Bs. 6.
• El 25% si el precio de coste supera los Bs. 6.
'''

def precioVenta(precio_coste):
    ganancia = 0
    if precio_coste<3:
        ganancia = precio_coste*0.15
    elif 3<=precio_coste<=6:
        ganancia = 0.50
    else:
        ganancia = precio_coste*0.25
    return f"El precio de la venta del producto es de {precio_coste + ganancia} Bs."

print(precioVenta(float(input("Ingrese el costo del producto: "))))