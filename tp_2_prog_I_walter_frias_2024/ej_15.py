#### ESTRUCTURAS DE CONTROL ###
""" 15. Que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”. Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato. """


print("")
print("##### EJERCICIO 10 #####")
print("")

#Defino la funcion para comprobar si la letra ingresada es vocal o no.
def es_vocal (letra):
    letra = letra.lower()#Con lower() paso a minusculas en caso de que se ingrese una letra mayuscula
    volcal = "a","e","i","o","u" #Varieble para comprobar si en la frase hay alguna coincidencia
    if letra in volcal:#Itero el argumento ingresado en la variable vocales buscando coincidencias y las guardo en letra.
        print(f"La letra que elegiste {letra} es vocal.")#Imprimo el resultado

    elif len(letra) > 1:#Si se cumple que letra sea mayor a un caracter, se envia un mensaje y se llama a la funcion de forma recursiva.
        print("Solo puedes ingresar una sola letra.")
        es_vocal(letra=input("Ingrese una letra:"))   


    
    else:#En el caso de que no se cupla niguna de las condiciones anteriores devolvera que no es vocal.
        print(f"La letra {letra} no es vocal")   
        es_vocal(letra=input("Ingrese una letra vocal:"))  
        

es_vocal(letra=input("Ingrese una letra:"))   

print("")
print("##### FIN DEL PROGRAMA #####")
print("")