from pizza import Pizza

class Mozo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pizzas = [] # a) Se inicializa la lista de pizzas como vacía.

    def establecer_nombre(self, nombre):
        self.nombre = nombre

# b) Se toman 1 o 2 pizzas de la lista de pizzas por entregar.
    def tomar_pizzas(self, pizzas_por_entregar): 
        if pizzas_por_entregar:
            max_pizzas = min(2, len(pizzas_por_entregar)) # El mozo puede llevar 1 o 2 pizzas como máximo.
            self.pizzas = pizzas_por_entregar[:max_pizzas]
            print(f"{self.nombre} ha tomado las pizzas: {[pizza.obtener_variedad() for pizza in self.pizzas]}")
            del pizzas_por_entregar[:max_pizzas] # Se eliminan las pizzas tomadas de la lista de pizzas por entregar.
        else:
            print(f"No hay pizzas para que {self.nombre} las tome.")

    # c) Se sirven las pizzas a los clientes.

    def servir_pizzas(self):
        if self.pizzas:
            print(f"{self.nombre} ha servido las pizzas: {[pizza.obtener_variedad() for pizza in self.pizzas]}")
            self.pizzas = []
        else:
            print(f"{self.nombre} no tiene pizzas para servir.") # Limpiamos la lista de pizzas después de servir.

    # d) Se verifica si el mozo está libre para seguir entregando pizzas.  

    def obtener_estado_libre(self):
        return len(self.pizzas) == 0  # Está libre si no tiene pizzas en las manos

    def obtener_nombre(self):
        return self.nombre

    def obtener_pizzas(self):
        return self.pizzas