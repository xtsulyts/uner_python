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

numeros = []
print("Ingrese números enteros uno por uno. Cuando haya terminado, escriba 'fin'.")

while True:
    entrada = input("Ingrese un número entero o 'fin' para terminar: ")
    if entrada.lower() == 'fin':
        break
    if entrada.isdigit():
        numeros.append(int(entrada))
    else:
        print("Por favor, ingrese un número entero válido.")

# Paso 2: Determinar el máximo
maximo = max(numeros) if numeros else None

# Paso 3: Obtener el segundo máximo
segundo_maximo = None
if len(numeros) > 1:
    numeros_unicos = set(numeros)
    numeros_unicos.remove(maximo)
    segundo_maximo = max(numeros_unicos)

# Paso 4: Determinar el mínimo
minimo = min(numeros) if numeros else None

# Paso 5: Calcular la multiplicación de todos los números
producto = 1
for num in numeros:
    producto *= num

# Paso 6: Contar los valores pares e impares
pares = sum(1 for num in numeros if num % 2 == 0)
impares = len(numeros) - pares

# Paso 7: Remover los elementos repetidos
numeros_sin_repetidos = list(set(numeros))

# Mostrar resultados
print("Resultados:")
print("Máximo:", maximo)
print("Segundo máximo:", segundo_maximo)
print("Mínimo:", minimo)
print("Producto de todos los números:", producto)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Lista sin elementos repetidos:", numeros_sin_repetidos)

print("")
print("#### FIN DEL PROGRAMA ####")
print("")




