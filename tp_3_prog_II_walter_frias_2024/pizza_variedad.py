class Pizza_variedad :
    def __init__(self, nom_var, pre : float):
        self.nombre_var = nom_var
        self.pre = pre
    
    def establecer_nombre_variedad (self, nom_var : str):
        var = input("Ingrese el nombre de la pizza: ")
        self.nombre_var = nom_var
        nom_var = var
    
    def establecer_precio (self, pre : int):
        self.pre = pre
    
    def obtener_nombre (self):
        return self.nombre_var
    
    def obtener_precio (self):
        return self.pre