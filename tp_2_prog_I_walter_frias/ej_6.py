##### ESTRUCTURAS DE CONTROL ####

"""6. Que pida al usuario una palabra y la muestre por pantalla 10 veces."""

print("")
print("##### EJERCICIO 6 #####")
print("")
def contador(palabra):
    for mostrar in range(10):
        mostrar = palabra
        print(f"{mostrar}")

contador(palabra = input("Ingrese una palabra: "))

print("")
print("##### FIN DEL PROGRAMA #####")