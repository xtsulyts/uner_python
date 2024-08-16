def listas_diferencia(lista1, lista2):
    # Encontrar los elementos en común entre ambas listas
    en_comun = sorted(set(lista1) & set(lista2), reverse=True)
    
    # Encontrar los elementos no comunes entre ambas listas
    no_comunes = sorted(set(lista1) ^ set(lista2))
    
    # Imprimir los resultados
    print(en_comun)
    print(no_comunes)

# Ejemplo de uso
listas_diferencia(['b', 'a', 'c'], ['e', 'b', 'd', 'c'])