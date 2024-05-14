#6. Programe una aplicación de consola que pregunte el precio total de la cuenta, 
#luego  pregunte cuántos comensales hay. 
#A continuación deberá dividir la cuenta total por el número de comensales y 
#mostrar cuánto debe pagar cada persona.

print("")
print("### EJERCICIO NUMERO 6 ###")
print("")

#Defino veriables de entrada e 
dato_1 = "Cual es el precio total de la cuenta: "
cuenta = int(input(dato_1)) 
dato_2 = "Cuantos comensales son?: "
comensales = int(input(dato_2))

#Divido las variables para saber el resultado e imprimo cuanto debe pagar cada comensal.
cuanta_comensal = cuenta / comensales
print(("Cada comensal debe pagar:"), cuanta_comensal)

print("")
print("### FIN DEL PROGRAMA ###")
print("")
