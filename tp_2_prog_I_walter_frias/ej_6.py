##### ESTRUCTURAS DE CONTROL ####

"""6. Que pida al usuario una palabra y la muestre por pantalla 10 veces."""

print("")
print("##### EJERCICIO 6 #####")
print("")

#Funcion que recibe una variable que almacene un string como parametro.
def contador(palabra):
    for mostrar in range(10): #El for recorrera 10 veces guardando en la variable mortrar la palabra que se ingrese como argumeto cuando se llame a la funcion.
        mostrar = palabra
        print(f"{mostrar}")

contador(palabra = input("Ingrese una palabra: "))#Llamada a funcion.

print("")
print("##### FIN DEL PROGRAMA #####")