"""a. Escribir una función de nombre palabra_no_tiene_letras(palabra,
letras_prohibidas), la cual retorne True si es que los caracteres que componen
una palabra no se encuentran en una lista de caracteres prohibidos."""

"""def palabra_no_tiene_letras(palabra, letras_prohibidas):
    palabra = True
    while palabra in letras_prohibidas:
        
        return True
    print("ok")
    return True

   
palabra_no_tiene_letras(palabra=input("Ingrese una palabra: "), letras_prohibidas = ["a", "b", "c"])"""

def palabra_no_tiene_letras(palabra, letras_prohibidas):
    for letra in palabra:
        if letra in letras_prohibidas:
            return False
    return True

# Definimos la palabra y las letras prohibidas
palabra = "holaz"
letras_prohibidas = ['x', 'y', 'z']

# Llamamos a la función y almacenamos el resultado
resultado = palabra_no_tiene_letras(palabra, letras_prohibidas)

# Imprimimos el resultado
print(resultado)  # Esto imprimirá True


    