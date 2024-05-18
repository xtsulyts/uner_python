#### ESTRUCTURAS DE CONTROL ####
""" 14. Que pida un año y que escriba si es bisiesto o no. Les recordamos que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. Algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto. """

print("")
print("##### EJERCICIO 13 #####")
print("")


# Defino ls funcion que comprobara si el anio ingresado es bisiesto o no
def bisiento(año):
    #Las variables contienen el int para comprobar los multiplos
    multiplo_1 = 4
    multiplo_2 = 400
    multiplo_3 = 100
    año = año
    #Compruebo los multiplos dados para comprobar si en anio es bisiesto.
    if (año % multiplo_1  == 0 and año % multiplo_3 != 0) or (año % multiplo_2 == 0):
        print(f"El año {año} es bisiesto.")
    #Si ninguna condicion se cumple el anio no es bisiesto.
    else:
        print(f"El año {año} no es bisiesto.")

bisiento(año=int(input("Ingrese un año te dire si es bisiesto:"))) 

print("")
print("##### FIN DEL PROGRAMA #####")