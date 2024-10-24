# orden.py
from pizza import Pizza

class Orden:
    ESTADO_INICIAL = 1
    ESTADO_PARA_ENTREGAR = 2
    ESTADO_ENTREGADA = 3
    total_ordenes = 0

    def __init__(self, nro: int, pizzas=None):
        if pizzas is None:
            pizzas = []
        self.nroOrden = nro
        self.pizzas = pizzas
        self.estadoOrden = Orden.ESTADO_INICIAL
        Orden.total_ordenes += 1

    def agregar_pizza(self, pizza: Pizza):
        self.pizzas.append(pizza)

    def cambiar_estado(self, nuevo_estado: int):
        if nuevo_estado in [Orden.ESTADO_INICIAL, Orden.ESTADO_PARA_ENTREGAR, Orden.ESTADO_ENTREGADA]:
            self.estadoOrden = nuevo_estado
        else:
            raise ValueError("Estado de la orden no válido")

    def calcular_total(self):
        return sum(pizza.variedad.precio for pizza in self.pizzas)

    def __str__(self):
        estado_orden = {1: "Inicial", 2: "Para Entregar", 3: "Entregada"}
        pizzas_str = "\n".join(str(pizza) for pizza in self.pizzas)
        return f"Orden N°{self.nroOrden} - Estado: {estado_orden[self.estadoOrden]}\nPizzas:\n{pizzas_str}\nTotal: {self.calcular_total()}€"

    @staticmethod
    def obtener_total_ordenes():
        return Orden.total_ordenes
