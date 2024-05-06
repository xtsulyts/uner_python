##### ESTRUCTURAS DE CONTROL #####

"""11. Que solicite al usuario ingresar una frase. Luego, que imprima la cantidad de vocales que se
encuentran en dicha frase."""

print("")
print("##### EJERCICIO 11 #####")
print("")


letras_seleccionadas = ""
def cantidad_vocales(frase):
    frase = frase
<<<<<<< HEAD
    for imprecion in frase:
        if imprecion in ["a", "e", "i", "o", "u"]:
            #si en la iteracion encuentra una letra de las seleccionadas en la lista cargarla en impresion y guardarla en letras vocales
            letras_vocales =  letras_seleccionadas + imprecion
            print(letras_seleccionadas)
        #if imprecion == vocales:
    #if vocales in frase:
            print(letras_vocales)
            #print(imprecion)
=======
    for i in frase:
        if i in ["a", "e", "i", "o", "u"]:
            #si en la iteracion encuentra una letra de las seleccionadas en la lista cargarla en impresion y guardarla en letras vocales
            letras_vocales =  letras_seleccionadas + i
            contar_vocales = letras_vocales
            numer_letras = letras_vocales.count(letras_vocales)
            #print(letras_vocales, end = ",")
            print(letras_vocales, end = ",")
            print(numer_letras)
            
>>>>>>> 4d56230cd56208c68ab15f8e0623b27cc3859588
cantidad_vocales(frase = input("Ingrese una frase: "))


print("")
print("##### FIN DEL PROGRAMA #####")