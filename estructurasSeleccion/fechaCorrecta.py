'''
Solicitar al usuario una fecha (dd:mm:aaaa) y comprobar si es correcta. Para que una fecha sea correcta es necesario:
• El año debe ser mayor que cero.
• El mes debe estar entre 1 y 12.
• Dependiendo del mes que sea, el día debe estar dentro de los límites válidos. Los meses que tienen 31 días son 1, 3, 5, 7, 8, 10 y 12. Los meses de 30 días son 4, 6, 9 y 11. El mes de 28 días es 2, excepto en un año bisiesto que es 29 días.
'''
def bisiesto(anio):
    if (anio%4==0 and anio%100!=0) or anio%400==0:
        return True
    else:
        return False


def valida(date):
    dia = int(date[0])
    mes = int(date[1])
    anio = int(date[2])
    mes31 = [1,3,5,7,8,10,12]
    mes30 = [4,6,9,11]
    mes29 = mes28 = [2]

    if anio>0 and 0<mes<=12 and dia>0:
        if (mes in mes31 and dia<=31) or (mes in mes30 and dia<=30):
            return True
        elif (mes in mes29 and bisiesto(anio) and dia<=29):
            return True
        elif (mes in mes28 and dia<=28):
            return True
        else:
            return False
    else:
        return False


def fechaCorrecta(fecha):
    date = fecha.split(":")
    return "Fecha válida." if valida(date) else "Fecha inválida."
    

print(fechaCorrecta(input("Ingrese una fecha (teniendo en cuenta que el formato es dd:mm:aaaa):")))