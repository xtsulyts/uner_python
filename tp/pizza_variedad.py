# pizza_variedad.py

class PizzaVariedad:
    def __init__(self, nomVar: str, pre: float):
        if pre <= 0:
            raise ValueError("El precio debe ser mayor a 0.0")
        self.nombreVariedad = nomVar
        self.precio = pre
    
    def __str__(self):
        return f"{self.nombreVariedad}: {self.precio}€"
