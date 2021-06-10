'''
Dada la fecha de hoy, calcular la fecha del día siguiente. Suponer que el año no es bisiesto.
'''
from datetime import datetime,timedelta

def fecha():
    today = datetime.today()
    tomorrow = today + timedelta(days = 1)
    return tomorrow.strftime("%Y/%m/%d")

print(fecha())