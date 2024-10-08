##### ESTRUCTURAS DE CONTROL #####

"""11. Que solicite al usuario ingresar una frase. Luego, que imprima la cantidad de vocales que se
encuentran en dicha frase."""

print("")
print("##### EJERCICIO 11 #####")
print("")

def contar_vocales_bucle(frase):
    # Convertir la frase a minúsculas para facilitar la comparación
    frase = frase.lower()
    # Inicializar un contador para las vocales
    contador = 0
    # Lista de vocales
    vocales = ['a', 'e', 'i', 'o', 'u']
    
    # Recorrer cada carácter de la frase
    for caracter in frase:
        # Verificar si el carácter es una vocal
        if caracter in vocales:
            contador += 1
    
    return contador

# Solicitar al usuario ingresar una frase
frase_usuario = input("Por favor, ingresa una frase: ")

# Llamar a la función e imprimir el resultado
cantidad_vocales = contar_vocales_bucle(frase_usuario)
print("La cantidad de vocales en la frase es:", cantidad_vocales)