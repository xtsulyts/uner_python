class Mozo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.pizzas = []

    def servirPizzas(self):
        if len(self.pizzas) > 0:
            self.pizzas = []
            print("Pizzas servidas!")
        else:
            print("Este mozo no tiene pizzas para servir!")