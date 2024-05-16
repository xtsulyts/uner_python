#### ESTRUCTURAS DE CONTROL ###
""" 15. Que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”. Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato. """

def es_vocal (letra):
    letra = letra
    volcal = "a","e","i","o","u"
    if letra == volcal:
        print("es vocal")
        return True

    else:
        print("no es")   
        es_vocal(letra=input("Ingrese una letra vocal:"))      

es_vocal(letra=input("Ingrese una letra vocal:"))        