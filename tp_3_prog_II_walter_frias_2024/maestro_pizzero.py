from orden import Orden
from pizza import Pizza 

# Se inicializan el nombre del maestro pizzero y dos listas donde se van a almacenar  las pizzas aún no cocinadas 
class Maestro_pizzero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ordenes_por_cocinar = []
        self.pizzas_por_cocinar = []
        self.pizza_cocinada = []

# Se establece el nombre del maestro pizzero
    def establecer_nombre (self, nom):
        self.nom = nom

# Se toma el pedido del cliente y se ingresa la variedad de pizza
    def tomar_pedido(self, orden):
        nro = int(input ("Igrese el numero de orden: "))
        var = input("Ingrese la variedad de pizza: ") 
        variedad = Pizza(var) 
        orden = Orden(nro,variedad.establecer_variedad(var)) 
        self.pizzas_por_cocinar.append(variedad)
        self.ordenes_por_cocinar.append(nro)                                                                                        
        #orden.establecer_nro_orden(nro)
        #orden.establecer_pizzas(variedad)
        print(f"Pizzas por cocinar: {[p.obtener_variedad() for p in self.pizzas_por_cocinar]}")

# Cocina la primera pizza en la lista de pizzas por cocinar
    def cocinar(self):
    
        
        if self.pizzas_por_cocinar:
            pizza_cocinada = self.pizzas_por_cocinar.pop(0)
            self.pizza_cocinada.append(pizza_cocinada)
            print(f"Se ha cocinado: {pizza_cocinada.obtener_variedad()}")
            
# Se obtiene el nombre del maestro pizzero
    def obtener_nombre (self):
        self.nombre = self.nombre
        return print(self.nombre)   

# Se muestran las pizzas que aún no han sido cocinadas
    def obtener_pizzas_por_cocinar(self):
        print(f"Pizzas por cocinar: {[p.obtener_variedad() for p in self.pizzas_por_cocinar]}")

# Se muestran las pizzas que ya han sido cocinadas y están listas para ser servidas
    def obtener_pizzas_por_entregar(self):
        print(f"Pizzas por entregar: {[p.obtener_variedad() for p in self.pizzas_por_cocinar]}")