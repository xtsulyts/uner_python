#### FUNCIONES ####

"""4. Que dada la base y altura de un triángulo nos calcule su área."""



print("")
print("##### EJERCICIO 4 #####")
print("")

#Defino una funcion para calcular el area, se pasan como parametros dos variables que guardaran la base y altura
def area_triangulo(b, a):
    b = b
    a = a
    area = b * a / 2 #Defino una variable para almacenar el resultado de la formula que calculara la base del triangulo.
    print(f"El area del triangulo es: {area}") #Imprimo en pantalla el resultado de la formula.

#Llamo a la funcion ingresando los argumantos solucitados.
area_triangulo(b = float(input("Ingrese la base del triangulo: ")),
               a = float(input("Ingrese la altura del triangulo: ")))

print("")
print("##### FIN DEL PROGRAMA #####")
print("")