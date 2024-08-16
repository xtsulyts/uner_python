def listas_diferencia(lista1, lista2):
    # Inicializar las listas para los elementos en común y no comunes
    en_comun = []
    no_comunes = []

    # Encontrar los elementos en común
    for elemento in lista1:
        if elemento in lista2:
            en_comun.append(elemento)

    for elemento in lista2:
        if elemento in lista1 and elemento not in en_comun:
            en_comun.append(elemento)

    # Encontrar los elementos no comunes
    for elemento in lista1:
        if elemento not in lista2:
            no_comunes.append(elemento)

    for elemento in lista2:
        if elemento not in lista1:
            no_comunes.append(elemento)

    # Ordenar las listas según las condiciones
    en_comun.sort(reverse=True)
    no_comunes.sort()

    # Imprimir los resultados
    print(en_comun)
    print(no_comunes)

# Ejemplo de uso
listas_diferencia(['b', 'a', 'c'], ['e', 'b', 'd', 'c'])