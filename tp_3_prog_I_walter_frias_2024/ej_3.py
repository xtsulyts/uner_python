""" 3. Dada la siguiente lista de frutas [“banana”, “manzana”, “pera”], permitir al usuario ingresar 3
frutas más para agregarlas al final de lista. Luego, mostrar por pantalla la lista completa y
debajo la misma lista pero sólo con las frutas que añadió el usuario.
 """

print("")
print("#### EJERCICIO 3 ####")
print("")

def agregar_a_lista():
    i = 0
    lista = ["banana", "manzana", "pera"]
    lista_nueva = []
    print(f"Lista de frutas: \n {lista}")
    
    while i < 3:
        ingreso = input("Ingrese el nombre de una fruta a la lista: ")
        ingreso = ingreso.lower()
        existente = ingreso in lista or lista_nueva
        if existente == True:
            print(f"La fruta {ingreso} ya existe ingrese otra:")
        else:
            lista.append(ingreso)
            lista_nueva.append(ingreso)
            i += 1
    print(f"Esta es la lista completa: \n {list(lista)} \n Estos son los elementos que se agragaron a la lista original: \n {list(lista_nueva)}")
    #matriz = list(lista), list(lista_nueva)
    #for x in matriz:
       # print(x)
    #print()
            
agregar_a_lista()

print("")
print("#### FIN DEL PROGRAMA ####")
print("")
