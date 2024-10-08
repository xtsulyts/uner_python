class NaveEspacial :
    max_deposito =1000
    parsec = 100
    def __init__(self,co, comb):
        self.estado_alertas = False

        self.color=co
        if(comb>self.max_deposito):
            self.combustible = self.max_deposito
        else:
            self.combustible = comb

    def establecerEstadoAlertas(self, habilitar):
        self.estado_alertas = habilitar

    def obtenerCombustible(self):
        return self.combustible

    def agregarCombustible(self, comb):
        if self.combustible + comb > self.max_deposito:
            if self.estado_alertas:
                print("!De los " + str(comb) + "litros, solo se pudieron cargar " + str(self.max_deposito - self.combustible) + "litros")
            self.combustible = self.max_deposito
        else:
            if  self.estado_alertas:

              print("Se cargaron" + str(comb) + "litros")


nave_espacial1 = NaveEspacial('R', 988888)
nave_espacial1.establecerEstadoAlertas(False)
nave_espacial1.combustible += 1
print(nave_espacial1.obtenerCombustible())