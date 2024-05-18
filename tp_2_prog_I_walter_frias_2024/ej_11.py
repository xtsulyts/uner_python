##### ESTRUCTURAS DE CONTROL #####

"""11. Que solicite al usuario ingresar una frase. Luego, que imprima la cantidad de vocales que se
encuentran en dicha frase."""

print("")
print("##### EJERCICIO 11 #####")
print("")

def cantidad_vocales(frase):#Defino una funcion que con una variable como parametro que recibe un str
    #letras_selecionadas = [] #Inicializo una lista vacia para almacenar las letras seleccionadas
    frase = frase.lower() #Le digo que pase a minusculas en el caso de que ingrese una frase con mayusculas
    vocales = "aeiou"#Defino una funcion que almacena un str con las letras vocales
    contador = 0 #Inicio un contador en cero
    
    for l in frase: #Con for itero por los caracteres de la frase ingresada
        if l in vocales:#Si l tiene coincidencias con alguna de las vocales la toma
            #letras_selecionadas.append(l)# Con append guardo en letras seleccionadas las coincidencias que encientre l
            contador += 1 #Por cada cioncidencia el contador sumara 1:
            #print(f"Las letras vocales son {letras_selecionadas}")
    return contador

cantidad_vocales = cantidad_vocales(frase = input("Ingrese una frase: "))
print("")
print(f"El numero de vocales en tu frase son : {cantidad_vocales}")
#print(f"Las vocales de la frase {frase} son : {letras_selecionadas}")




"""letras_seleccionadas = ""
def cantidad_vocales(frase):
    letras_seleccionadas = ""
    
    frase = frase
    for i in frase:
        if i in ["a", "e", "i", "o", "u"]: #si en la iteracion encuentra una letra de las seleccionadas en la lista cargarla en impresion y guardarla en letras vocales
            letras_vocales =  letras_seleccionadas + i
            #contardor = letras_seleccionadas + i
            #numer_letras = letras_vocales.count(letras_vocales + letras_seleccionadas)
            #c = contardor.count(contardor)
            #c = letras_vocales.count(letras_vocales)
            letras_vocales = letras_vocales [::-1]
            #print(letras_vocales, end = ",")
            print(f"{letras_seleccionadas}")
        
    contador = 0
    for i in frase:
        if i in ["a", "e", "i", "o", "u"]: #si en la iteracion encuentra una letra de las seleccionadas en la lista cargarla en impresion y guardarla en letras vocales
            letras_vocales =  letras_seleccionadas + i
            contador =+ 1
            #contardor = letras_seleccionadas + i
            numer_letras = letras_vocales.count(letras_vocales + letras_seleccionadas)
            #c = contardor.count(contardor)
        print(f"{contador}")
        #print(c)            
cantidad_vocales(frase = input("Ingrese una frase: "))
print(letras_seleccionadas)"""

print("")
print("##### FIN DEL PROGRAMA #####")