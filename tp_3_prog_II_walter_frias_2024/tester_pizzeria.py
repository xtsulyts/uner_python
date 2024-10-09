
from maestro_pizzero import Maestro_pizzero
from mozo import Mozo
from pizza import Pizza
from pizza_variedad import Pizza_variedad

class TesterPizzeria:
    @staticmethod
    def main():
        # a) Se crean los objetos de tipo MaestroPizzero y Mozo
        pizzero = Maestro_pizzero("PIPO")
        mozo1 = Mozo('Alfredo')
        mozo2 = Mozo('Alfredo')
        variedad_1 = Pizza_variedad("muzza", 10000)
        pizza = Pizza
        

# A continuación, se muestra el menú de opciones
        while True:
            print("\nMenu:")
            print(" 1. Tomar pedido Pizzero.")
            print(" 2. Ver pizzas por cocinar.")
            print(" 3. Cocinar pizzas.")
            #print(" 4. Ver pizzas por entregar.")
            #print(" 5. Entregar pizzas con mozo1.")
            #print(" 6. Entregar pizzas con mozo2.")
            #print(" 7. Salir.")

            # Validación de la entrada para evitar que un valor no numérico cause un error
            try:
                opcion = int(input("Ingrese una opción: "))
            except ValueError:
                print("Entrada no válida. Por favor ingrese un número.")
                continue  # Regresa al inicio del loop para pedir la opción de nuevo

            if opcion == 1:
                pizzero.tomar_pedido(1)

            elif opcion == 2:
                pizzero.obtener_orden_por_entregar()

            elif opcion == 3:
                pizzero.cocinar()

            elif opcion == 4:
                variedad_1.obtener_precio()

            elif opcion == 5:
                variedad_1.obtener_nombre()

            elif opcion == 6:
                pizza.obtener_variedad("")

            elif opcion == 7:
                variedad_1.establecer_nombre_variedad("")

            elif opcion == 8:
                pizza.obtener_variedad()

            elif opcion == 9:
                print("Saliendo del programa...")
                break

            else:
                print("Opción no válida, por favor elija una opción del 1 al 7.")

if __name__ == '__main__':
    testerPizzeria = TesterPizzeria()
    TesterPizzeria.main()