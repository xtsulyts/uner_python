

from pizza_variedad import Pizza_variedad

class Pizza:

    ESTADO_POR_COCINAR = 1
    ESTADO_COCINADA = 2
    ESTADO_ENTREGADA = 3

    def __init__(self, var: str):
        self.__variedad = var
        self.estado = 1


    def establecer_variedad(self, var: str):
       
        var = Pizza_variedad(nom_var=input("Ingrese la variedad: "), pre=int(input("Igrese el precio: ")))
        self.__variedad = var
        pizza = Pizza(1, var)
        self.__variedad = var
        print(pizza)                                

    def establecer_estado_interno (self, estado: int):
        self.estado = estado

    def obtener_variedad(self):
        return self.__variedad
    
    def  ontener_estado_interno (self):
        return self.estado
    def __repr__(self):
        return self.__variedad




