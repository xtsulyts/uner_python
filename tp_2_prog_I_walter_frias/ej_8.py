##### ESTRUCTURAS DE CONTROL #####

"""8. Pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""


print("")
print("##### EJERCICIO 8 #####")
print("")

def preguntar_edad(edad):
    if edad >= 18:
        print("Es mayo de edad.")
    else:
        print("Es menor de edad")

preguntar_edad(int(input("Ingrese su edad: ")))

print("")
print("##### FIN DEL PROGRAMA #####")