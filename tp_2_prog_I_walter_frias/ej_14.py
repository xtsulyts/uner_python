#### ESTRUCTURAS DE CONTROL ####
""" 14. Que pida un año y que escriba si es bisiesto o no. Les recordamos que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. Algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto. """

def bisiento(año):
    multiplo_1 = 4
    multiplo_2 = 400
    multiplo_3 = 100
    año = año
    if año % multiplo_1  == 0 and año % multiplo_2 == 0:
        print("bisiesto")

    elif año % 100 == 0:
        print("no es")

    else:
        print("no")
        

bisiento(año=int(input("Ingrese un año te dire si es bisiesto:")))    