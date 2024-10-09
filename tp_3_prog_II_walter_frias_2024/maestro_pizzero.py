from orden import Orden
from pizza import Pizza 
#eth18 primer clase de ethereum


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
        orden = Orden(nro, var)#variedad.establecer_variedad(var) 
        #self.pizzas_por_cocinar.append(variedad)
        self.ordenes_por_cocinar.append(f"Orden: {nro}, Estado: {orden.ESTADO_INICIAL}")  
        self.ordenes_por_cocinar.append(f"Pizzas: {var}")                                                                                   
        #orden.est.ablecer_nro_orden(nro)
        #orden.establecer_pizzas(variedad)
        print(f"imprimo desde Orden: {orden.obtener_nro_orden()}")
        print(f"orden: {nro}, estado: {orden.ESTADO_INICIAL}, pizzas: {var}")
        #print(f"orden: {nro}, estado: {orden.ESTADO_INICIAL}, pizzas:{orden.establecer_pizzas(variedad.establecer_variedad(var))}")
        

# Cocina la primera pizza en la lista de pizzas por cocinar
    def cocinar(self):
    
        
        if self.pizzas_por_cocinar:
            orden_cocinada = self.ordenes_por_cocinar.pop(0)
            self.pizzas_por_cocinar.append(orden_cocinada)
            pizza_cocinada = self.pizzas_por_cocinar.pop(0)
            self.pizza_cocinada.append(pizza_cocinada)
            #print(f"Orden {self.ordenes_por_cocinar[0]}Se ha cocinado: {pizza_cocinada.obtener_variedad()}")
            print(f"Orden:{orden_cocinada}, estado: {Orden.ESTADO_PARA_ENTREGAR} se cocinaron: {pizza_cocinada.obtener_variedad()}")

            
# Se obtiene el nombre del maestro pizzero
    def obtener_nombre (self):
        self.nombre = self.nombre
        return print(self.nombre)   

# Se muestran las pizzas que aún no han sido cocinadas
    def obtener_pizzas_por_cocinar(self):
        print(f"Pizzas por cocinar: {[p.obtener_variedad() for p in self.pizzas_por_cocinar]}")

# Se muestran las pizzas que ya han sido cocinadas y están listas para ser servidas
    def obtener_orden_por_entregar(self):
        return print(self.ordenes_por_cocinar)
    
   
        #print(f"Pizzs por entregar: {[p.obtener_variedad() for p in self.pizzas_por_cocinar]}")