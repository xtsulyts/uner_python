#8. Escriba un programa que permita al usuario ingresar la base y altura de un triángulo 
#para luego imprimir por pantalla la superficie total.

print("")
print("### EJERCICIO NUMERO 8 ###")
print("")

print("### BASE Y ALTURA PARA CALCULAR ###")
print("########### SUPERFICIE ############")
print("######## DE UN TRIANGULO ##########")
print("")

#Defino las variables para almnacenar los datos necesarios para el calculo solicutado.
dato_1 = "Ingrese en numeros la base del triangulo: "
base_triangulo = int(input(dato_1))
dato_2 = "Ingrese la altura del triangulo: "
altura_triangulo = int(input(dato_2))
superficie_total = base_triangulo * altura_triangulo / 2

#Imprimo la respuesta.
print(("La superficie total es:"), superficie_total)

print("")
print("### FIN DEL PROGRAMA ###")
print("")