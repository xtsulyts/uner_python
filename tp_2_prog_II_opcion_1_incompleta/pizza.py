# pizza.py
from pizza_variedad import PizzaVariedad

class Pizza:
    ESTADO_POR_COCINAR = 1
    ESTADO_COCINADA = 2
    ESTADO_ENTREGADA = 3

    def __init__(self, var: PizzaVariedad):
        self.variedad = var
        self.estado = Pizza.ESTADO_POR_COCINAR

    def cambiar_estado(self, nuevo_estado: int):
        if nuevo_estado in [Pizza.ESTADO_POR_COCINAR, Pizza.ESTADO_COCINADA, Pizza.ESTADO_ENTREGADA]:
            self.estado = nuevo_estado
        else:
            raise ValueError("Estado no válido")

    def __str__(self):
        estado_pizza = {1: "Por Cocinar", 2: "Cocinada", 3: "Entregada"}
        return f"Pizza de {self.variedad.nombreVariedad} - Estado: {estado_pizza[self.estado]} - Precio: {self.variedad.precio}€"
