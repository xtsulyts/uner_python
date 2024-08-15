#Se tiene los siguientes datos del nivel del rio (en metros) en el puerto de concordia, para los últimos 5 días hábiles de la semana.
# 5/6/2023 altura de rio 1.66
# 6/6/2023 altura de rio 1.88
# 7/6/2023 altura de rio 1.58
# 8/6/2023 altura de rio 2.08
# 9/6/2023 altura de rio 1.49

#Escribir un programa Python para permitir ingresar los datos por consola de los 5 días y guardarlos en una lista llamada altura_rio_puerto_concordia[]. 

#a. Mostrar la altura mínima semanal y en qué día de la semana ocurrió. 
#b .Mostrar la altura máxima semanal y en que día de la semana ocurrió. 
#c .Calcular el promedio del nivel en la semana.

# Definir los días de la semana



altura_rio_puerto_concordia = []


for i in range(5):
    dia = input(f"Ingrese la fecha para el día {i+1} (formato DD/MM/AAAA): ")
    altura = float(input(f"Ingrese la altura del río para el día {dia}: "))
    altura_rio_puerto_concordia.append((dia, altura))

altura_minima = altura_rio_puerto_concordia[0]
for registro in altura_rio_puerto_concordia:
    if registro[1] < altura_minima[1]:
        altura_minima = registro

dia_minima, valor_minima = altura_minima
print(f"Altura mínima semanal: {valor_minima} m el día {dia_minima}")


altura_maxima = altura_rio_puerto_concordia[0]
for registro in altura_rio_puerto_concordia:
    if registro[1] > altura_maxima[1]:
        altura_maxima = registro

dia_maxima, valor_maxima = altura_maxima
print(f"Altura máxima semanal: {valor_maxima} m el día {dia_maxima}")


suma_alturas = 0
for registro in altura_rio_puerto_concordia:
    suma_alturas += registro[1]

promedio_altura = suma_alturas / len(altura_rio_puerto_concordia)
print(f"Promedio del nivel del río en la semana: {promedio_altura:.2f} m")

print(f"Lista completa altura de rio puerto concordia: {altura_rio_puerto_concordia}")