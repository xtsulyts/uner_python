""" 1. Crear un programa que almacene en una lista las materias de esta u otra carrera y que las muestre por pantalla. (La lista debe ser predefinida, no debe ser ingresada por el usuario)"""

#Hola profes, esta vez les debo los comentarios,
#estoy muy a full y tengo que prerarme para el parcial de int_informatica 

print("")
print("#### EJERCICIO 1 ####")
print("")


def mostrar_lista():
    carrera = "Profesoraso de Artes Visuales"
    listado_materias = ["dibujo", "pintura", "escultura", "grabado"]
    mensaje = f"Las materias troncales del {carrera} son:"
    print(f"{mensaje}") 
    for mostrar_materias in listado_materias:
        
        #print(listado_materias)
        print(mostrar_materias)

mostrar_lista()

print("")
print("#### FIN DEL PROGRAMA ####")
print("")