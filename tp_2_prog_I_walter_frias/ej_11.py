##### ESTRUCTURAS DE CONTROL #####

"""11. Que solicite al usuario ingresar una frase. Luego, que imprima la cantidad de vocales que se
encuentran en dicha frase."""

print("")
print("##### EJERCICIO 8 #####")
print("")


letras_seleccionadas = ""
def cantidad_vocales(frase):
    frase = frase
    for imprecion in frase:
        if imprecion in ["a", "e", "i", "o", "u"]:
            #si en la iteracion encuentra una letra de las seleccionadas en la lista cargarla en impresion y guardarla en letras vocales
            letras_vocales =  letras_seleccionadas + imprecion
            print(letras_seleccionadas)
        #if imprecion == vocales:
    #if vocales in frase:
            print(letras_vocales)
            #print(imprecion)
cantidad_vocales(frase = input("Ingrese una frase: "))


print("")
print("##### FIN DEL PROGRAMA #####")