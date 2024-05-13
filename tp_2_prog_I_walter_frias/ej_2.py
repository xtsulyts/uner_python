#### FUNCIONES ####

"""2. Que reciba un número entero positivo y una potencia a elevar y que nos devuelva el resultado."""

#Defino la funcion con dos parametros que recibiran el numero solucitado y la potencia a elevar
def date_enter(n, x):
    resultado = n ** x #Elevo el numero a la potencia elegida y guardo el resultado en la variable resultado
    print(f"El resultado es = {resultado}") #Imprimo el resultado de elevar el numero por la potencia

print("")
print("##### EJERCICIO 2 #####")
print("")

date_enter(n = int(input("Ingrese un numero: ")),
           x = (int(input("Ingrese a que potencia lo quiere elevar: "))))

print("")
print("##### FIN DEL PROGRAMA #####")
print("")

