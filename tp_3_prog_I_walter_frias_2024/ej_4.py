""" 4. Dada la siguiente lista: países = [“Argentina,”Brasil”, “Bolivia”,”Paraguay”,”Venezuela”], realizar lo siguiente: 
a. Imprimir la cantidad de elementos que tiene la lista
b. Imprimir el primer y último elemento. 
c. Imprimir el resto. 
d. Permitir que el usuario ingrese un país e imprimir el índice si el país se encuentra en la lista. Si no se encuentra, imprimir un mensaje advirtiendo al usuario. 
e. Permitir al usuario ingresar un número igual o menor a la cantidad de elementos de la lista. Quitar el elemento correspondiente de esa posición. 
f. Imprimir la lista en orden inverso. 
g. Vaciar la lista."""

print("")
print("#### EJERCICIO 2 ####")
print("")

paises = ["Argentina", "Brasil", "Bolibia", "Paraguay", "Venezuela"]
def ej_4():
    cantidad_elmentos = len(paises)
    print(f"a. La cantidad de elementos  de la lista:{cantidad_elmentos}")
    primer_elemento = paises[0]
    #segundo_elemento = paises[1]
    #tercer_elemento = paises[2]
    #cuerto_elemento = paises[3]
    ultimo_elemento = paises[4]
    print(f"b. El primer elemento es {primer_elemento}. \n y el ultimo es {ultimo_elemento}.")
    resto = paises[1:3]
    print(f"c. El resto de la lista es : {resto}.")

    
    #coincidencia = paises[0] or paises[1] or paises[2] or paises[3]
    for _ in paises:
        ingresar_pais = input("Ingrese un pais: ")
        ingresar_pais = ingresar_pais
        if ingresar_pais == paises[0]:
            coincidencia_1 = paises.index(ingresar_pais)
            print(f"d. la coincidencia es Argentina y su indice es {coincidencia_1}.")
            """if coincidencia_1 == paises[0]:
                ingreso_indice = int(input("Ingrese un numero:"))
                ingreso_indice == 0
                paises = paises.pop(0)
                print(paises)"""
            return
        elif ingresar_pais == paises[1]:
            coincidencia_2 = paises.index(ingresar_pais)
            print(f"d. la coincidencia es Brasil y su indice es {coincidencia_2}.")
        elif ingresar_pais == paises[2]:
            coincidencia_3 = paises.index(ingresar_pais)
            print(f"d. la coincidencia es Bolibia y su indice es {coincidencia_3}.")
            return
        elif ingresar_pais == paises[3]:
            coincidencia_4 = paises.index(ingresar_pais)
            print(f"d. la coincidencia es Paraguay su indice es {coincidencia_4}.")
            return
        elif ingresar_pais == paises[3]:
            coincidencia_5 = paises.index(ingresar_pais)
            print(f"d. la coincidencia es Venezuela su indice es {coincidencia_5}.")
            return
        else:
            print(f"El pais {ingresar_pais} no esta en la lista.")
            return

ej_4()

print("")
print("#### FIN DEL PROGRAMA ####")
print("")
