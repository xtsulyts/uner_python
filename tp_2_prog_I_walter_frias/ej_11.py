##### ESTRUCTURAS DE CONTROL #####

"""11. Que solicite al usuario ingresar una frase. Luego, que imprima la cantidad de vocales que se
encuentran en dicha frase."""

print("")
print("##### EJERCICIO 11 #####")
print("")

contar = ""
letras_seleccionadas = ""
def cantidad_vocales(frase):
    letras_seleccionadas = ""
    frase = frase
    for i in frase:
        if i in ["a", "e", "i", "o", "u"]: #si en la iteracion encuentra una letra de las seleccionadas en la lista cargarla en impresion y guardarla en letras vocales
            letras_vocales =  letras_seleccionadas + i
            #contardor = letras_seleccionadas + i
            numer_letras = letras_vocales.count(letras_vocales + letras_seleccionadas)
            #c = contardor.count(contardor)
            print(letras_vocales, end = ",")
            print(numer_letras)
            
cantidad_vocales(frase = input("Ingrese una frase: "))
print(letras_seleccionadas)


print("")
print("##### FIN DEL PROGRAMA #####")