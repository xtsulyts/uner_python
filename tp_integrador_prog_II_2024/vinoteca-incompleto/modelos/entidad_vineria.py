
class EntidadVineria:
    def __init__(self, id:str, nombre:str):
        self.id=id
        self.nombre=nombre
    
    def esteblecerNombre(self, nombre:str):
        self.nombre=nombre

    def obtenerId(self):
        return self.id
    
    def obtenerNombre(self):
        return self.nombre
    def __eq__(self, id):
        pass