""" 7. Escriba un programa Python que cuente con dos listas, la primera de ellas almacenará strings
con tareas pendientes y la segunda almacenará strings con tareas terminadas. Permita al
usuario:
a. Agregar nuevas tareas pendientes.
b. Marcar las tareas pendientes como terminadas. Al hacer esto, la tarea deberá pasar
de la lista de pendientes a la de terminadas.
Nota: posterior a cada operación deberá mostrar por pantalla el estado actual de ambas
listas."""


# Creamos dos listas vacías para almacenar las tareas pendientes y las tareas terminadas
tareas_pendientes = []
tareas_terminadas = []

# Función para mostrar el estado actual de ambas listas
def mostrar_estado():
    print("Tareas Pendientes:", tareas_pendientes)
    print("Tareas Terminadas:", tareas_terminadas)

# Función para agregar nuevas tareas pendientes
def agregar_tarea():
    nueva_tarea = input("Ingrese la nueva tarea pendiente: ")
    tareas_pendientes.append(nueva_tarea)
    print("Se ha agregado la tarea correctamente.")
    mostrar_estado()

# Función para marcar tareas pendientes como terminadas
def marcar_como_terminada():
    if not tareas_pendientes:
        print("No hay tareas pendientes para marcar como terminadas.")
        return
    tarea_terminada = tareas_pendientes.pop(0)  # Sacamos la primera tarea de la lista de pendientes
    tareas_terminadas.append(tarea_terminada)
    print("Se ha marcado la tarea como terminada.")
    mostrar_estado()

# Función principal del programa
def main():
    while True:
        print("\nMenú:")
        print("1. Agregar nueva tarea pendiente")
        print("2. Marcar tarea pendiente como terminada")
        print("3. Mostrar estado actual de las listas")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            marcar_como_terminada()
        elif opcion == "3":
            mostrar_estado()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
main()

