#### ESTRUCTURAS DE CONTROL ####

"""13. Que resuelva el siguiente problema: los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo y muestre por pantalla el grupo que le corresponde."""

print("")
print("##### EJERCICIO 13 #####")
print("")


mujeres = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
hombres = ["n","o","p","q","r","s","t","u","v","w","x","y","z"]
femenino = "femenino"
masculino = "masculino"

def cursos(nombre, sexo):
    nombre = nombre
    inicial = nombre[0].lower()

    if sexo.lower() != mujeres or hombres:
        print("Error")
        # return cursos(nombre=input("Ingrese su nobre: "), sexo=input("Ingrese su genero: "))


    elif inicial in mujeres and sexo.lower() == femenino:
        print(f"La alumna {nombre} pertenece al grupo A.")
        
    elif inicial in hombres and sexo.lower() == masculino:
        print(f"El alumno {nombre} pertenece al grupo A.")
        return True

    #elif sexo.lower() != femenino:
    #elif femenino or masculino != sexo.lower():
        #print("Solo puedes elegir entre femenino y masculino, ingresa nuevamente tus datos.")
        #cursos(nombre=input("Ingrese su nobre: "), 
            #sexo=input("Ingrese su genero: "))   
        #return False
    
    else:
        print(f"{nombre} tus datos indican que perteneces al grupo B.")
        

cursos(nombre=input("Ingrese su nobre: "), 
       sexo=input("Ingrese su genero: "))



print("")
print("##### FIN DEL PROGRAMA #####")
