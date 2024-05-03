#### FUNCIONES ####

"""4. Que dada la base y altura de un triángulo nos calcule su área."""



print("")
print("##### EJERCICIO 4 #####")
print("")

def area_triangulo(b, a):
    b = b
    a = a
    area = b * a / 2
    print(f"El area del triangulo es: {area}")

area_triangulo(b = int(input("Ingrese la base del triangulo: ")),
               a = int(input("Ingrese la altura del triangulo: ")))

print("")
print("##### FIN DEL PROGRAMA #####")