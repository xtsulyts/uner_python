def es_primo(numero):
    # Los números menores o iguales a 1 no son primos
    if numero <= 1:
        return False
    # Iterar desde 2 hasta la mitad del número
    for i in range(2, numero // 2 + 1):
        # Si el número es divisible por algún número en este rango, no es primo
        if numero % i == 0:
            return False
    # Si no se encontraron divisores, el número es primo
    return True
es_primo(4
         )