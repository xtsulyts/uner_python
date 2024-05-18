#### ESTRUCTURAS DE CONTRL ####

""" 17. Que muestre todos los números primos entre 0 y 100 e imprima cuántos números primos hay."""

print("")
print("##### EJERCICIO 17 #####")
print("")

#Defino una funcion que calcula el numero primo de un numero.
def primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
#Defino una funcion que llamara a la funcion primo para comprobar los numeros primos en un rango de 100   
def primos_hasta_100():
    primos = [] #Inicio una variable que con una lista vacia para almacenar los numeros primos.
    for numero in range(101):
        if primo(numero):
            primos.append(numero)#Con append() agrego los resultados en primos
    return primos

# Ejemplo de uso:
primos = primos_hasta_100()
cantidad_primos = len(primos)#Con le cuanto la cantidad de numeros primos.

print("Números primos entre 0 y 100 son:")
print(primos)
print("")
print(f"Cantidad total de números primos entre 0 y 100: {cantidad_primos}")

print("")
print("##### FIN DEL PROGRAMA #####")
print("")
