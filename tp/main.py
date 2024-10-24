# main.py
from pizza_variedad import PizzaVariedad
from pizza import Pizza
from orden import Orden

# Listas globales para almacenar variedades de pizza y órdenes
variedades = []
ordenes = []
contador_ordenes = 1

def mostrar_variedades():
    """Mostrar la lista de variedades de pizza disponibles."""
    if not variedades:
        print("No hay variedades de pizza disponibles.")
        return
    print("Variedades de pizza disponibles:")
    for i, var in enumerate(variedades, 1):
        print(f"{i}. {var}")

def crear_variedad():
    """Permite al usuario crear una nueva variedad de pizza."""
    nombre = input("Ingrese el nombre de la nueva variedad de pizza: ")
    try:
        precio = float(input("Ingrese el precio de la pizza: "))
        nueva_variedad = PizzaVariedad(nombre, precio)
        variedades.append(nueva_variedad)
        print(f"Variedad {nombre} creada exitosamente.\n")
    except ValueError:
        print("Error: El precio debe ser un número válido.")

def crear_orden():
    """Permite crear una nueva orden vacía."""
    global contador_ordenes
    nueva_orden = Orden(contador_ordenes)
    ordenes.append(nueva_orden)
    print(f"Orden #{contador_ordenes} creada exitosamente.\n")
    contador_ordenes += 1

def agregar_pizza_a_orden():
    """Permite al usuario agregar una pizza a una orden."""
    if not ordenes:
        print("No hay órdenes disponibles. Cree una orden primero.\n")
        return
    if not variedades:
        print("No hay variedades de pizza disponibles. Cree una variedad primero.\n")
        return

    # Seleccionar orden
    print("Seleccione el número de la orden:")
    for i, orden in enumerate(ordenes, 1):
        print(f"{i}. Orden #{orden.nroOrden}")
    try:
        nro_orden = int(input("Ingrese el número de la orden: ")) - 1
        if nro_orden < 0 or nro_orden >= len(ordenes):
            print("Número de orden no válido.")
            return
    except ValueError:
        print("Debe ingresar un número válido.")
        return

    # Seleccionar variedad de pizza
    mostrar_variedades()
    try:
        nro_variedad = int(input("Seleccione el número de la variedad de pizza: ")) - 1
        if nro_variedad < 0 or nro_variedad >= len(variedades):
            print("Número de variedad no válido.")
            return
    except ValueError:
        print("Debe ingresar un número válido.")
        return

    # Crear la pizza y agregarla a la orden
    pizza = Pizza(variedades[nro_variedad])
    ordenes[nro_orden].agregar_pizza(pizza)
    print(f"Pizza de {variedades[nro_variedad].nombreVariedad} agregada a la Orden #{ordenes[nro_orden].nroOrden}.\n")

def ver_ordenes():
    """Muestra la lista de órdenes con sus pizzas."""
    if not ordenes:
        print("No hay órdenes creadas.")
        return
    for orden in ordenes:
        print(orden)

def menu():
    """Menú principal del programa."""
    while True:
        print("------ Menú Principal ------")
        print("1. Crear una nueva variedad de pizza")
        print("2. Crear una nueva orden")
        print("3. Agregar una pizza a una orden")
        print("4. Ver lista de órdenes")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_variedad()
        elif opcion == "2":
            crear_orden()
        elif opcion == "3":
            agregar_pizza_a_orden()
        elif opcion == "4":
            ver_ordenes()
        elif opcion == "5":
            print("¡Gracias por usar el sistema de órdenes de pizza!")
            break
        else:
            print("Opción no válida, intente de nuevo.\n")

if __name__ == "__main__":
    menu()
