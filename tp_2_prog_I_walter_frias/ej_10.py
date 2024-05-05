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

def buscar_impares (numero):
    print("Los numeros impares son:")
    numero = numero
    for impares in range(numero):
        impares = impares + 1
        numeros_pares = impares % 3
        imprecion = numeros_pares
        if imprecion == 0:
            print(impares, end = ",")

buscar_impares(numero =(int(input("Ingrese un numero: "))))