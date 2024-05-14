#5. Escriba un programa que pida al usuario que ingrese 3 números. 
#Sume los dos primeros y luego multiplique este total por el tercero. 
#Mostrar la respuesta en pantalla de la siguiente forma: “La respuesta es XX”.

print("")
print("### EJERCICIO NUMERO 5 ###")
print("")


#Defino las variables de entrada de los dos primeros datos
dato_1 = "Ingrese el primer numero: "
primer_numero = int(input(dato_1))
dato_2 = "Ingrese el segundo numero se sumara al primero: "
segundo_numero = int(input(dato_2))
resultado_1 = primer_numero + segundo_numero

#Imprimo el resultado de la suma en pantalla.
print(("El resultado de la suma es:"), resultado_1)

#Defino la variable del numero x el que se va a multiplicar el primer resultado.
dato_3 = "Ingrese el tercer numero se multiplicara con el resultado de la suma: "
tercer_numero =  int(input(dato_3))
resultado_2 = resultado_1 * tercer_numero

#Imprimo la respuesta final en pantalla.
print(("La respuesta es:"), resultado_2)

print("")
print("### FIN DEL PROGRAMA ###")
print("")
