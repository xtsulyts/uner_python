"""A continuación, se presenta el código de un programa que, ante la edad ingresada por el usuario, 
este presenta el equivalente en días, meses y años. Se solicita al alumno que lo refactorice de 
manera tal que:
a. Se elimine la sentencia if / else de la función anio_bisiesto.
b. Las múltiples sentencias if la función dia_mes utilicen la cláusula in en lugar de 
varias cláusulas or.
c. Se agregue una sentencia que valide que la edad ingresada por el usuario es 
numérica.
d. Se agregue una función que encapsule el cálculo del equivalente de la edad en 
días y que tome como parámetros las variables hora_local, anio_comienzo y
anio_fin.
e. Todas las funciones sean transportadas a un archivo auxiliar de funciones 
llamado funciones.py, y este sea importado desde el programa principal"""





from datetime import datetime
import time
from calendar import isleap
# calcular si es un año bisiesto
def anio_bisiesto(anio):
    if isleap(anio): return True
    else: return False
# calcular el numero de dias de cada mes
def calcular_dias_mes(mes, anio_bisiesto): 
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        
        return 31
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return 30
    elif mes == 2 and anio_bisiesto == True:
        return 29
    elif mes == 2 and anio_bisiesto == False:
        return 28
# ingreso de datos del usuario
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")


# seteo inicial de variables
hora_local = time.localtime(time.time())
anios = int(edad)
anio_comienzo = int(hora_local.tm_year) - anios
anio_fin = anio_comienzo + anios
meses = anios * 12 + hora_local.tm_mon
dias = 0
# calcular los dias
for a in range(anio_comienzo, anio_fin):
    if (anio_bisiesto(a)): dias = dias + 366
    else: dias = dias + 365
# agregar los días transcurridos en este año
for m in range(1, hora_local.tm_mon):
 dias = dias + calcular_dias_mes(m, anio_bisiesto(hora_local.tm_year))
# agregar los días transcurridos en este mes
dias = dias + hora_local.tm_mday
print(anio_comienzo)

##########################################################################################
# d. equivalente de la edad en dias
def calcular_edad_en_dias(hora_local, anio_comienzo, anio_fin):
    dias = 0
    
    # Iteramos sobre cada año desde el año de comienzo hasta el año final
    for anio in range(anio_comienzo, anio_fin + 1):
        # Verificamos si el año es bisiesto
        es_bisiesto = anio_bisiesto(hora_local.tm_year)
        
        # Iteramos sobre cada mes del año
        for mes in range(1, 13):
            # Si estamos en el año actual y el mes supera el mes actual, rompemos el ciclo
            if anio == anio_fin and mes > hora_local.tm_mon:
                break
            # Sumamos los días del mes actual
            dias += calcular_dias_mes(mes, es_bisiesto)
    
    return dias
dias_vividos = calcular_edad_en_dias(hora_local, anio_comienzo, anio_fin)
print(f"Has vivido {dias_vividos} días.")
print(anio_comienzo)
print(hora_local)


###########################################################################################



# imprimir la edad del usuario
#print("La edad de %s es %d años o " % (nombre, anios), end="")
#print("%d meses o %d días" % (meses, dias))