###### FUNCIONES #####

""" 1. Que al pasarle una cadena <nombre> nos muestre por pantalla el saludo ¡Hola <nombre>!."""


#Defino la funcion paso como parametro una variable que almacenara un string
def saludo(nombre):
    print("")
    print("##### EJERCICIO 1 #####")
    print("")
    print(f"¡Hola {nombre}!")

#Llamo a la funcion y paso con un input el parametro
saludo(input("Escriba su nombre: "))
print("")
print("##### FIN DEL PROGRAMA #####")
print("")