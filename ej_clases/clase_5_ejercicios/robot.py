class Robot():
    energiaMin=10
    energiaMax=100
    def __init__(self,n):
        self.nombre=n
        self.estado= True
        self.pasos=0
        self.energia=self.energiaMax
    # Comandos
    def caminar(self):
        if self.estado:
            self.pasos += 1
            self.energia=self.energia - 5
            if self.energia < self.energiaMin:
                self.recargar()
    def dormir(self):
        if self.estado:
            self.estado=False
            self.energia-=1
            if self.energia < self.energiaMin:
                self.recargar()
    def despertar(self):
        if not(self.estado):
            self.estado=True
            self.energia -= 1
            if self.energia < self.energiaMin:
                self.recargar()
    def recargar(self):
        if self.estado:
            self.energia=self.energiaMax
    #consultas
    def obtenerNombre(self):
        return self.nombre
    def obtenerEstado(self):
        return self.estado
    def obtenerPasos(self):
        return self.pasos
    def obtenerEnergia(self):
        return self.energia
    def tieneMasEnergia(self,e):
        return self.energia > e
    def __str__(self):
        s = self.nombre + ' ' + str(self.estado) + ' ' + str(self.pasos) + ' ' + str(self.energia) 
        return s
    def mayorEnergia(self,r):
        if self.energia > r.obtenerEnergia():
            n = self.energia
        else:
            n = r.obtenerEnergia()
        return n
    def conMasEnergia(self,r):
        if self.energia > r.obtenerEnergia():
            n = self
        else:
            n = r
        return n
    

r1 = Robot('Pepito')
r2 = Robot('Pepita')
for i in range(1, 5):
        if (i % 2 == 0):
            r1.dormir()
        else:

            r1.despertar()

for j in range (i, 5):
        if (j % 2 == 0):
            r2.dormir()
        else:
            r2.despertar()
            r2.caminar()
print(r1.conMasEnergia(r2))


#r2.caminar()
#r2.caminar()
#r2.caminar()
#r2.dormir()
#r1.__str__()
#r2.__str__()
#print(r2)
#print(r1)
#print(r1.mayorEnergia(r2))