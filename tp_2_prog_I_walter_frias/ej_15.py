#### ESTRUCTURAS DE CONTROL ###
""" 15. Que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”. Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato. """


print("")
print("##### EJERCICIO 10 #####")
print("")


def es_vocal (letra):
    letra = letra
    volcal = "a","e","i","o","u"
    if letra in volcal:
        print(f"La letra que elegiste {letra} es vocal.")

    elif len(letra) != 1:
        print("Solo puedes ingresar una sola letra.")
        es_vocal(letra=input("Ingrese una letra:"))   


    
    else:
        print(f"La letra {letra} no es vocal")   
        es_vocal(letra=input("Ingrese una letra vocal:"))  
        

es_vocal(letra=input("Ingrese una letra:"))   

print("")
print("##### FIN DEL PROGRAMA #####")
print("")