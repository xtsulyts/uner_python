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

#### HOLA PROFES EN ESTE EJERCICIO TUVE UN PREBLEMA QUE NO LO PUDE RESOLVER ####
#### SI INGRESO UN NUMERO MAYOR A 10 LA LISTA SE ME DESORDENA, INTENTE PASAR LOS NUMEROS ####
#### INTENTE PASAR A STR Y ME DEVOLVIA LA CUANTA ATRAS ASI EJ 23,24,25 COMO 52,42,32 ####
#### LO ENTREGO ASI NO LO PUDE RESOLVER ####
numero = int(input("Ingrese un numero: "))
print("")
def buscar_impares ( numero):
    inicio = 1
    numero = numero
    # Impares
    print(f"A. Los numeros impares desde el 1 al {numero} son: ")
    if numero <= 0:#Con if verifico que el numero ingresado sea valido
        print("El numero ingresado no es valido vuelva a ingresar un numero entero positivo.")
        buscar_impares(inicio = 1, numero = (int(input("Ingrese un numero: "))))#En el caso de no ingresar un numero valido se llama a la funcion de buscar pares de forma recursiva.
    else:
        impares = [] #Si el numero es valido inicializo una variable vacia que almacenara un strig.
    
    for i in range(inicio, numero + 1, 2):#Con el bucle se va a iterar desde el numro  1 hasta el numero ingresado, se indica un salto de 2 para solo guardar solo impares
        #impares += str(i) + "," #Imprimo los numeros impares
        impares +=f"{i}"
    impares = impares
    print(f"{impares}")
    print("")

    #Cuenta atras
    cuenta_atras = [] #Creo una veriable para guardar la cuanta atras en una lista
    cuenta_atras += impares
    imprecion_cuenta_atras = cuenta_atras[::-1] #Le digo que es igual a impares epezando desde el ultimo caracter.
    print(f"B. La cuanta atras de los numeros impares desde {numero} al {inicio} son: ")#Imprimo la cuenta atras de impares.
    print(f"{imprecion_cuenta_atras} ")
    print("")

    #Numero primo
    if numero <= 1:
        return False
    for primo in range(2, numero // 2 + 1):
        if numero % primo == 0:
            print(f"C. El numero {numero} no es primo")
            return False
    print(f"C. El numero {numero} es primo.")
    print("")

    # Factorial
def sacar_factoria(numero):
    if numero == 0 or numero ==1:
        return 1
    else:
        return numero *  sacar_factoria(numero - 1)
    print()

buscar_impares(numero)#(numero = (int(input("Ingrese un numero: "))))
factorial = sacar_factoria(numero)
print("")
print(f"D. El factorial de {numero} es = {factorial}")
print("")
print("##### FIN DEL PROGRAMA #####")
print("")