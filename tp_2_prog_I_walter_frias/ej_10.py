##### ESTRUCTURAS DE CONTROL #####

"""10. Que el usuario ingrese un número entero positivo y muestre por pantalla lo siguiente:
a. Todos los números impares desde 1 hasta ese número separados por comas.
b. La cuenta atrás desde ese número hasta cero separados por comas.
c. Que indique si es primo o no.
d. Por último, su factorial.
"""

print("")
print("##### EJERCICIO 10 #####")
print("")

def buscar_impares ( numero):
    inicio = 1
    numero = numero
    print(f"A. Los numeros impares desde el 1 al {numero} son: ")
    if numero <= 0:#Con if verifico que el numero ingresado sea valido
        print("El numero ingresado no es valido vuelva a ingresar un numero entero positivo.")
        buscar_impares(inicio = 1, numero = (int(input("Ingrese un numero: "))))#En el caso de no ingresar un numero valido se llama a la funcion de buscar pares de forma recursiva.
    else:
        impares = "" #Si el numero es valido inicializo una variable vacia que almacenara un strig.
    
    for i in range(inicio, numero + 1, 2):#Con el bucle se va a iterar desde el numro  1 hasta el numero ingresado, se indica un salto de 2 para solo guardar solo impares
        #impares += str(i) + "," #Imprimo los numeros impares
        impares += f"{(i)},"

    impares = impares[:-1]#Elimino la ultima coma de la lista
   
    print(impares)
    print("")

    cuenta_atras = "" #Creo una veriable para guardar la cuanta atras
    cuenta_atras = impares[::-1]#Le digo que es igual a impares epezando desde el ultimo caracter.
       
    """for i in range(numero, inicio, -1):
        cuenta_atras += str(i) + ",
    
    cuenta_atras = cuenta_atras[:-1]"""

    print(f"B. La cuanta atras de los numeros impares desde {numero} al {inicio} son: ")#Imprimo la cuenta atras de impares.
    print(f"{cuenta_atras} ")
    print("")

    if numero <= 1:
        return False
    for primo in range(2, numero // 2 + 1):
        if numero % primo == 0:
            print(f"C. El numero {numero} no es primo")
            return False
    print(f"C. El numero {numero} es primo.")
    print("")

    #No puedo saccar el factorial XD
    """if numero == 0:
        return 1
    else:
        recursiva = buscar_impares(numero -1)
        factorial = int(numero) * int(recursiva)
        print(factorial)



    for factorial in range(numero -1):
        factorial = numero  =+ factorial +1
        resutado = numero * factorial"""

    print(f"D. El factorial de {numero} es ")


    
      
       

buscar_impares(numero = (int(input("Ingrese un numero: "))))


print("")
print("##### FIN DEL PROGRAMA #####")
print("")