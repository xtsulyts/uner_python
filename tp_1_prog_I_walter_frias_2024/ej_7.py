#7. Pida al usuario un número x de días y luego mostrar por pantalla cuántas horas, 
#minutos y segundos son esos números de días.

print("")
print("### EJERCICIO NUMERO 7 ###")
print("")

#Variable de entrada de datos.
dato = "Escriba una cantidad X de dias: "
nro_dias = int(input(dato)) 
print("")
print("### En cantidad de horas ###")

#Guardo la cantidad de horas de un dia en una variable.
#Imprimo el resultado de multiplicar el dato de entrada con la variable.
#Para los dos datos siguientes minutos y segundos se uso el mismo criterio.
horas_x_dia = 24
horas_totales = nro_dias * horas_x_dia
print(("### Son:"), horas_totales, "###")
print("")

print("### En cantidad de minutos ###")
minutos_x_hora = 60
minutos_totales = horas_totales * minutos_x_hora
print(("## Son:"), minutos_totales, "###")
print("")

print(("### En cantidad de segundos ####"))
segundos_x_hora = 60
segundos_totales = minutos_totales * segundos_x_hora
print(("### Son:"), segundos_totales, "###")

print("")
print("### FIN DEL PROGRAMA ###")
print("")







