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

def buscar_impares (inicio, numero):
    print("Los numeros impares son:")
    inicio = inicio
    numero = numero
    for impares in range(inicio, numero + 1, 2):
        c = impares -1
        print(impares, end=",")
        print(c)
    
        

    """for i in range(numero, impares):
        i = i -1
        print(i, end=",")"""

buscar_impares(inicio = 1, numero = (int(input("Ingrese un numero: "))))


print("")
print("##### FIN DEL PROGRAMA #####")
print("")