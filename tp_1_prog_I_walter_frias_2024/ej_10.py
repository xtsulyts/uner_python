#10. Escriba un programa que indique si un texto es palíndromo, es decir, 
#se escribe igual al derecho que al revés.
#Por ejemplo: rayar, kayak, somos

print("")
print("### EJERCICIO NUMERO 10 ###")
print("")


dato = input("Introduzca una palabra: ")
dato= dato.lower()
palindromo = dato[::-1]
if palindromo==dato:
    print("Es un palindromo")
else:
    print("No es un palindromo")
    

"""#Defino una funcion y le paso como parametro una variable.
def palindromo(texto):
    texto = texto.lower() #Con la funcion lower() elimino las mayusculas por minusculas del string 
                          #que voy a almacenar.

    primer_indice = 0 #Defino una veriable para el primer caracter del texto en la posicion 0.
    ultimo_indice = len(texto) - 1 #Defino con la funcion len()el ultomo caracter contandolos y restando 1.

#El bucle que recorra el texto del parametro de la funcion.
#Si los indices son diferentes no sera palindroma y retornara False"""

    #while primer_indice < ultimo_indice:
        #if texto[primer_indice] != texto[ultimo_indice]:
            #return False
"""#Si los indices son iguales y mientras el caracter sigiente de indice sea menor al caracter de ultimo_indice.
    #El bucle segira recorriendo sumando 1 a primer indice y restando 1 a ultimo_indice buscando coincidencias.
    #Si el bucle termina el recorrido encontrando == coincidencias de caracteres hasta llegar a la mitad del texto.
    #Entonces retornara True y el texto sera palindromo y se cortara cuando no exista la condicion x > y."""  
        #primer_indice += 1 
        #ultimo_indice -= 1

    #return True

#Ingreso texto por consola
#texto = input("Ingrese un texto: ")

#Ejecuto la funcion palindromo
#print(palindromo(texto))

#Si devuelve True imprimira un mensaje de exito si no es False e imprimira que no es palindroma
#if palindromo(texto):
    #print("Esta palabra se es palindroma!!")
#else:
    #print("Esta palabraa no es palindroma")    


print("")
print("### FIN DEL PROGRAMA ###")
print("")
       
                
    
        




