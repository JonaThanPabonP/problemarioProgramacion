'''
Solicitar al usuario la inicial del día de la semana y mostrar el nombre del día completo. La letra inicial puede ser mayúscula o minúscula. Usar la x para el miércoles.
'''

def diaSemana(inicial):
    dias = {"l":"Lunes","m":"Martes","x":"Miércoles","j":"Jueves","v":"Viernes","s":"Sábado","d":"Domingo"}
    if inicial.lower() in dias.keys():
        return dias[inicial.lower()]
    else:
        return "Valor no válido. Intentelo nuevamente."

print(diaSemana(input("Ingrese la inicial de un día de la semana: ")))