class Contrato :

    def __init__(self, nombre: str, numero: int , fecha: str ):

        self.nombre = nombre
        self.numero = numero
        self.fecha = fecha

contrato = Contrato("Contrato 1", 1, "01-01-2022")
print(contrato)
   