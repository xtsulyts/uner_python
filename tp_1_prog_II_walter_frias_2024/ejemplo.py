import time
import calendar

def calcular_dias_y_meses(hora_local, anio_comienzo, anio_fin):
    anios = anio_fin - anio_comienzo
    meses = anios * 12 + hora_local.tm_mon
    dias = 0

    # Cálculo de los días
    for anio in range(anio_comienzo , anio_fin):
        if calendar.isleap(anio):
            dias += 366
        else:
            dias += 365

    # Devolver el resultado
    return dias, meses

# Ejemplo de uso:
hora_local = time.localtime(time.time())  # Hora local actual
edad = 40  
anio_comienzo = int(hora_local.tm_year) - edad
anio_fin = anio_comienzo + edad

dias, meses = calcular_dias_y_meses(hora_local, anio_comienzo, anio_fin)
print(f"Desde el año {anio_comienzo} hasta el año {anio_fin} ({edad} años) hay un total de {dias} días.")
print(f"En total, se han vivido {meses} meses.")