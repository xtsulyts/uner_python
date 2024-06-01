""" 4. Dada la siguiente lista: países = [“Argentina,”Brasil”, “Bolivia”,”Paraguay”,”Venezuela”], realizar lo siguiente: 
a. Imprimir la cantidad de elementos que tiene la lista
b. Imprimir el primer y último elemento. 
c. Imprimir el resto. 
d. Permitir que el usuario ingrese un país e imprimir el índice si el país se encuentra en la lista. Si no se encuentra, imprimir un mensaje advirtiendo al usuario. 
e. Permitir al usuario ingresar un número igual o menor a la cantidad de elementos de la lista. Quitar el elemento correspondiente de esa posición. 
f. Imprimir la lista en orden inverso. 
g. Vaciar la lista."""

#En este ej tambien por falta de tiempo no pude soluconar que cambien
#la primer letra del pais ingresado a mayuscula si lo escribe en minuscula
#Y que despues del else vuelva a preguntar el pais hasta que se ingrese correctamente.

print("")
print("#### EJERCICIO 2 ####")
print("")

paises = ["Argentina", "Brasil", "Bolibia", "Paraguay", "Venezuela"]
def ej_4_0():
    print(f"La lista original contiene estos paises: \n {paises}")
    cantidad_elmentos = len(paises)
    print("")
    print(f"a. La cantidad de elementos  de la lista son: {cantidad_elmentos}")
    primer_elemento = paises[0]
    #segundo_elemento = paises[1]
    #tercer_elemento = paises[2]
    #cuerto_elemento = paises[3]
    ultimo_elemento = paises[4]

    print("")
    print(f"b. El primer elemento es {primer_elemento}. \n y el ultimo es {ultimo_elemento}.")
    print("")
    resto = paises[1:4]
    print(f"c. El resto de la lista es : {resto}.")
    print("")

    #coincidencia = paises[0] or paises[1] or paises[2] or paises[3]
    for _ in paises:
        ingresar_pais = input("d. Ingrese un pais: ")
        #ingresar_pais = ingresar_pais.lower()
        if ingresar_pais == paises[0]:
            coincidencia_1 = paises.index(ingresar_pais)
            print(f"La coincidencia es Argentina y su indice es {coincidencia_1}.")
            return
        elif ingresar_pais == paises[1]:
            coincidencia_2 = paises.index(ingresar_pais)
            print(f"La coincidencia es Brasil y su indice es {coincidencia_2}.")
            return
        elif ingresar_pais == paises[2]:
            coincidencia_3 = paises.index(ingresar_pais)
            print(f"La coincidencia es Bolibia y su indice es {coincidencia_3}.")
            return
        elif ingresar_pais == paises[3]:
            coincidencia_4 = paises.index(ingresar_pais)
            print(f"La coincidencia es Paraguay su indice es {coincidencia_4}.")
            return
        elif ingresar_pais == paises[4]:
            coincidencia_5 = paises.index(ingresar_pais)
            print(f"La coincidencia es Venezuela su indice es {coincidencia_5}.")
            return
        else:
            print(f"El pais {ingresar_pais} no esta en la lista.")
            return

ej_4_0()
print("")

def ej_4_1():
    ingreso_indice = int(input("e. Ingrese un numero: "))
    if ingreso_indice <= 4:
        ingreso_indice = ingreso_indice
        ingreso_indice == paises[0] or paises[1] or paises[2] or paises[3] or paises[4]
        ingreso_indice = paises.pop(ingreso_indice)
        #print(ingreso_indice) 
        print(f"El indice ingresado pertenece al pais {ingreso_indice}, sera removido de la lista.")
        print(f"Lista actualizada sin {ingreso_indice} es: \n {paises}")

    
    else:
        print(f"El numero {ingreso_indice} no existe en la lista.") 
        #return input("Ingrese un pais que axistente en la lista: ")

ej_4_1()
print("")

def  ej_4_2():
    lista_reverso = paises[::-1]
    print(f"f. La lista  al reverso quedaria asi: \n {lista_reverso}")
    print("")
    #borrar_lista = paises.clear()
    paises.clear()
    print(f"Vaciar la lista {paises}. ")


ej_4_2()

print("")
print("#### FIN DEL PROGRAMA ####")
print("")



#elif ingreso_indice == paises[0] or paises[1] or paises[2] or paises[3] or paises[4]:
        #ingreso_indice = paises.pop(ingreso_indice)
        #print(ingreso_indice) 
        #print(f"El indice ingresado perenece al pais {ingreso_indice}, sera removido de la lista")
        #print(f"Lista actualizada sin {ingreso_indice} es: \n {paises}")"""