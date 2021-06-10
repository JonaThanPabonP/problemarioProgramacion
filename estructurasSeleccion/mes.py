'''
Pedir un mes(número) y mostrar el nombre del mes.
'''

def mes(num):
    try:
        meses = {1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto", 9:"Septiembre", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"}
        if meses[num] != None:
            return meses[num]
        else:
            return "Número no válido."
    except:
        "Valor ingresado no válido."

print(mes(int(input("Ingrese el número de un mes: "))))