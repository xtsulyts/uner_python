import time
from calendar import isleap
list
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

hora_local = time.localtime(time.time())
anios = int(edad)
anio_comienzo = int(hora_local.tm_year) - anios
anio_fin = anio_comienzo + anios
meses = anios * 12 + hora_local.tm_mon
dias = 0

def equivalente_en_dias(hora_local, anio_comienzo, anio_fin):
    hora_local = time.localtime(time.time())
    bisiesto = 0
    for a_bisiesto in range(anio_comienzo, anio_fin):
        if isleap(a_bisiesto): bisiesto = bisiesto + 1
    return (bisiesto * 366) + ((anio_fin - anio_comienzo) * 365) 
    
#print(bisiesto)
#print(f"La hora lola es: {hora_local}")
  

dias = equivalente_en_dias(hora_local, anio_comienzo, anio_fin) + hora_local.tm_mday

print(f"En {edad} años trascurrieron {dias} dias!!")
print(f"El año  de inicio es: {anio_comienzo} y el año actual es {anio_fin}")
