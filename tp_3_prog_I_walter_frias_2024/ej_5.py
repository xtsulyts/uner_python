""" 5. Escriba un programa Python que solicite al usuario el ingreso de números enteros. Cuando el
usuario ingrese la palabra “fin” el programa deberá concluir con la carga de datos. Cada uno
de los números ingresados por el usuario deberá ser almacenado en una lista. A
continuación, realice las siguientes tareas:
a. Determinar el máximo.
b. Obtener segundo valor máximo. Es decir el que le sigue al máximo.
c. Determinar el mínimo.
d. Calcular la multiplicación de todos los números de la lista.
e. Contar los valores pares e impares.
f. Remover los elementos repetidos."""


print("")
print("#### EJERCICIO 5 ####")
print("")

lista_a = []
print("Ingrese numeros enteros y 'fin' para concluir con la catga de datos.")

while True:
    entrada = input("Ingrese un numero entero o 'fin' para terminar: ")
    if entrada.lower() == 'fin':
        break
    if entrada.isdigit():
        lista_a.append(int(entrada))
    else:
        print("Solo podes ingresar numeros enteros.")

maximo = max(lista_a) if lista_a else None
print("Maximo:", maximo)

segundo_maximo = None
if len(lista_a) > 1:
    numeros_unicos = set(lista_a)
    numeros_unicos.remove(maximo)
    segundo_maximo = max(numeros_unicos)
    print("Segundo maximo:", segundo_maximo)
   
minimo = min(lista_a) if lista_a else None
print("Minimo:", minimo)

producto = 1
for num in lista_a:
    producto *= num
print("Producto de todos los numeros:", producto)


pares = sum(1 for num in lista_a if num % 2 == 0)
impares = len(lista_a) - pares
print("Cantidad de numeros pares:", pares)

numeros_sin_repetidos = list(set(lista_a))
print("Lista sin elementos repetidos:", numeros_sin_repetidos)

print("")
print("#### FIN DEL PROGRAMA ####")
print("")




