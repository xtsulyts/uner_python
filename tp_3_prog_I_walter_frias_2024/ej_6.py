""" 6. Programe una aplicación de consola Python que brinde al usuario la posibilidad de a partir de una lista vacía: 
a. Agregar un elemento al final. 
b. Agregar un elemento al principio. 
c. Quitar un elemento al final. 
d. Quitar un elemento al principio"""


print("")
print("#### EJERCICIO 2 ####")
print("")

def ej_6():
    lista_vacia = []
    a = "a" #Agregar un elemento al final. 
    b = "b" #Agregar un elemento al principio. 
    c = "c" #Quitar un elemento al final. 
    d = "d" #Quitar un elemento al principio.
    salir = "salir"
    print("Opcion A, agregar un elemento al final de la lista. ")
    print("Opcion B, Agregar un elemento al principio de la lista.")
    print("Opcio C, Quitar un elemento al final de la lista.")
    print("Opcion D, Quitar un elemento al principio de la lista.")
    print("Para salir del programa ingrese la palabra salir")
    
    while True:
        opcion = input("Seleccione una opción: ")
        
        if opcion == a:
            elemento = input("Ingrese el elemento a agregar al final: ")
            lista_vacia.append(elemento)
            print(f"Elemento '{elemento}' agregado al final.")
            print(lista_vacia)
        
        elif opcion == b:
            elemento = input("Ingrese el elemento a agregar al principio: ")
            lista_vacia.insert(0, elemento)
            print(f"Elemento '{elemento}' agregado al principio.")
            print(lista_vacia)
        
        
        elif opcion == c:
            if lista_vacia:
                elemento = lista_vacia.pop()
                print(f"Elemento '{elemento}' quitado del final.")
                print(lista_vacia)

        elif opcion == d:
            if lista_vacia:
                elemento = lista_vacia.pop(0)
                print(lista_vacia)
            else:
                print("La lista está vacía, no se puede quitar un elemento.")
        
        #elif opcion == "4":
            #print("Lista actual:", lista)
        
        elif opcion == salir:
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")
        
        print() 
ej_6()

print("")
print("#### FIN DEL PROGRAMA ####")
print("")