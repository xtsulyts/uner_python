from pizza import Pizza

class Maestro_pizzero :
    def __init__(self, nom):
        self.nombre = nom
        self.pizzas_por_cocinar = []
        self.pizzas_por_entregar = []

    def menu_opcines ():
        opciones = [1,2,3,4]

        while True:
            if opciones == 1:
                print("opcion 1")
            elif opciones == 2:
                print("opcion 2")
            elif opciones == 3:
                print("opcion 3")
            elif opciones == 4:
                break
            else:
                break    

    def establecer_nombre (self, nom):
        self.nombre = nom

    def tomar_pedido (self, var):
        self.var = var.Pizza(input("Ingrese una pizza: "))
        self.pizzas_por_cocinar.append(self.var)
    
    


    def cocinar ():
        pass

    def entregar ():
        pass

    def obtener_nombre ():
        pass

    def obtener_pizzas_por_cocicar ():
        """Pizza[]"""
        pass
    def obtener_pizzas_por_entregar ():
        """Pizza []"""
        pass
pizzero = Maestro_pizzero("pipo")
pizzero.establecer_nombre("hola")
print(pizzero)  
id(pizzero)
pizzero.pizzas_por_entregar
print()
#pizzero.nombre("")
Maestro_pizzero.tomar_pedido(pizzero, "fff")






