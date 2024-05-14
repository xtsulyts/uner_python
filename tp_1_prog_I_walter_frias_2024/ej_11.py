#11. Programe una aplicación de consola que muestre los primeros 5 
#caracteres de una cadena de texto ingresada por el usuario.

print("")
print("##### EJERCICIO 11 #####")
print("")



#Defino la función que guardara el string.
texto = input("Ingrese una palabra:")

#Defino la variable que guardara los primeros 5 caracteres con un slice.
caracteres = texto[:5]

#Mostramos en pantalla los primeros 5 caracteres.
print("Los primeros 5 carcteres son:", caracteres)


print("")
print("### FIN DEL PROGRAMA ###")
print("")