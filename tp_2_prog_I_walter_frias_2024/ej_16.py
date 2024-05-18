#### ESTRUCTURAS DE CONTROL ####
""" Inprimir patron """


print("")
print("##### EJERCICIO 16 #####")
print("")

#defino la funcion que imprimira el patron, el argumento segun el enunciado es 5
def imprimir_patron(numero_inicial): 
    for i in range(numero_inicial, 0, -1):#Con el primer for imprimo desde 5 a o en una linea
        for patron in range(i, 0, -1):#En un for anidado itero la variable patron desde i hasta 0 restando 1.
            print(patron, end = "")#Imprimo los numeros separados por un espacio.
        print()#Con este print por cada iteracion hago un salto de linea.


imprimir_patron(5)