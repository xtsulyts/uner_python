
from maestro_pizzero import Maestro_pizzero
from mozo import Mozo
from pizza import Pizza
from pizza_variedad import Pizza_variedad
from orden import Orden
class TesterPizzeria:
    @staticmethod
    def main():
        # a) Se crean los objetos de tipo MaestroPizzero y Mozo
        pizzero = Maestro_pizzero("PIPO")
        mozo1 = Mozo('Alfredo')
        mozo2 = Mozo('Alfredo')
        variedad_1 = Pizza_variedad("muzza", 5000)
        pizza_1 = Pizza(variedad_1)
        print(variedad_1.obtener_precio())
        #print(pizza_1.obtener_variedad().obtener_nombre())
        variedad_2 =Pizza_variedad("napo",  7000)
      
 
        

# A continuación, se muestra el menú de opciones
        while True:
            print("\nMenu:")
            print(" 1. Crear una orden. ")
            print(" 2. Agregar pizzas a la orden.")
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
                n_orden = int(input("Ingrese nro de orden"))
                if n_orden == 1:
                    #pizza_1 = Pizza(variedad_1)
                    orden = Orden(n_orden, pizza_1)
                    print(orden.obtener_pizzas().obtener_variedad())



            elif opcion == 2:
              while True:
                  print("Opciones de piizza.")
                  print("1. muzzaz, precio $5000")
                  print("2. nappo, precio $7000")
                  opciones = int(input("elija una opcion: "))
                  if opciones == 1:
                      pizza_1 = Pizza(variedad_1)
                      print(pizza_1.obtener_variedad().obtener_nombre())


                  elif opciones == 2:
                       pizza_2 = Pizza(variedad_2)
                       print(pizza_2.obtener_variedad().obtener_nombre())
                  
                  elif opciones == 9:
                      break
                 

               

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