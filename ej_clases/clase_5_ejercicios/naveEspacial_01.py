class NaveEspacial():
    # Atributos de clase
    maxDeposito = 1000
    parsec = 100
    # Método de inicialización
    def __init__(self, o, c):
    # Atributos de instancia
        """ 
        si comb > maxDeposito, combustible=maxDeposito. 
        Requiere que o igual a 
        'V', 'R' o 'A'
        """
        self.color=o
        if c > self.maxDeposito:
            self.combustible = self.maxDeposito
        else:
            self.combustible = c
    # Comandos
    def establecerColor(self,o):
        self.color = o
    def establecerCombustible(self,c):
        if c > self.maxDeposito:
            self.combustible = self.maxDeposito
        else:
            self.combustible = c
    def llenarDeposito(self):
        self.combustible = self.maxDeposito
    # Consultas
    def obtenerColor(self):
        return self.color
    def obtenerCombustible(self):
        return self.combustible
    def obtenerAutonomia(self):
        return self.combustible / self.parsec
    def __eq__(self, otro):
        if (isinstance(otro, NaveEspacial)):
            equiv = self.color == otro.color and self.combustible == otro.combustible
        else: 
            equiv = False
        return equiv 
    def __str__(self):
        cadena = self.color + ' ' + str(self.combustible)
        return cadena 
    def mayar_energia (self, r):
        if self.energia > r.obtenerEnergia():
            n = self.energia
        else:
            n = r.obtenerEnergia()
        return n
    def con_mas_energia (self, r):
        if self.energia > r.obtenerEnergia():
            n = self
        else:
            n = r
        return n