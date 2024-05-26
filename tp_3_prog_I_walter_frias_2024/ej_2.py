""" 2. Pedir al usuario que ingrese 5 números para luego almacenarlos en una lista y ordenarlos.
Imprimir por pantalla el resultado.
"""



print("")
print("#### EJERCICIO 2 ####")
print("")


def ordenar_numeros():
    numeros = []
    i = 0
    while i < 5:
        numero_ingresado = float(input("Ingrese un numero: "))
        numero_repetido = numero_ingresado in numeros
        if numero_repetido:
            print(f"El numero {numero_ingresado} ya existe ingresa otro.")
        else:
            numeros.append(numero_ingresado)
            #i = i + 1
            i += 1
    numeros.sort()
    primer_numero = numeros[0]
    ultimo_numero = numeros[4]
    print(f"Los numeros que elegiste se ordenaron de {primer_numero} a {ultimo_numero} y son : \n {numeros}")
    #print(primer_numero)
    #print(ultimo_numero)
ordenar_numeros()

"""def ordenar_numeros():
    numeros = []
    for _ in range(5):

        n = float(input("Ingrese un numero: "))
        if n_repetido := n in numeros:
            print(f"El numero {n_repetido} ya existe ingresa otro.")
        else:
            numeros.append(n)
    numeros.sort()
    print(numeros)

ordenar_numeros()"""

print("")
print("#### FIN DEL PROGRAMA ####")
print("")
