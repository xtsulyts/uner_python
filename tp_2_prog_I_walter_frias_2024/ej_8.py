##### ESTRUCTURAS DE CONTROL #####

"""8. Pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""


print("")
print("##### EJERCICIO 8 #####")
print("")

def preguntar_edad(edad):#Funcion que recibe la edad expresada en un numero entero.

    if edad > 120 or edad <= 0:#Con if defino los limites de edades aceptadas, mayor de 120 y menores a 0 no seran validas y se llamara de forma recursiva a la funcion para volver a preguntar.
        print("No es una edad valida ingrese una edad valida: ")
        preguntar_edad(int(input("Ingrese su edad: ")))#Llanada recursiva

    elif edad >= 18 and edad <= 120:#Con un elif defino la condicion en el caso que el argumento sea mayor de 18 y menor a 120 para mayor de edad.
        print("Es mayo de edad.")#Si se cumple inprime que es mayor.

    elif edad <= 18 and edad > 0:#Si es mayor que 0 y menor de 18 mostrara que es menor de edad.
         print("Es menor de edad")

       

preguntar_edad(int(input("Ingrese su edad: ")))

print("")
print("##### FIN DEL PROGRAMA #####")
print("")