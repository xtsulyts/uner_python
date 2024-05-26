""" 1. Crear un programa que almacene en una lista las materias de esta u otra carrera y que las muestre por pantalla. (La lista debe ser predefinida, no debe ser ingresada por el usuario)"""

print("")
print("#### EJERCICIO 1 ####")
print("")


def mostrar_lista():
    carrera = "Profesoraso de Artes Visuales"
    listado_materias = ["dibujo", "pintura", "escultura", "grabado"]
    mensaje = f"Las marias troncales del {carrera} son:"
    print(f"{mensaje}")
    cantidad = 1 
    for mostrar_materias in listado_materias:
        
        #print(listado_materias)
        print(mostrar_materias)

mostrar_lista()

print("")
print("#### FIN DEL PROGRAMA ####")
print("")