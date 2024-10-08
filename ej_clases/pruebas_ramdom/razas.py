#defino una clase abstracta raza con parametros y comportamientos
class Raza:
    def __init__(self, color, region, cantidad, costumbres, genero):
      self.color = color
      self.region = region
      self.cantidad = cantidad
      self.constumbres = costumbres
      self.genero = genero

    def ejercitarse ( ejercicio):
        #if ejercicio == "ejercitadose":
            #print("La entidad se esta ejercitando")vibre como si lo tuvieras y lo tendras
        if isinstance(ejercicio, int) >=1 :
             print("La entidad se esta ejercitando")

        else:
            "La entidad no esta haciendo ejercicio"    
    def alimentarse():
        pass
    def reproducirse():
        pass
    def ataque():
        pass
    def defensa():
        pass
    def moverse():
        pass
class Grises(Raza):
       
    def __init__(self, color, region, cantidad, costumbres, genero, alimentacion):
        super().__init__(color, region, cantidad, costumbres, genero)
        self.alimentacion = alimentacion
        
class Azules(Raza):
    def __init__(self, color, region, cantidad, costumbres, genero, descanso):
        super().__init__(color, region, cantidad, costumbres, genero)
        super().ejercitarse(10)
        self.descanso = descanso

    def caminar (self, avanzar, detenerse):
        #avanzar = False
        #detenerse = True

        if avanzar >= 1:
            print("La entidad se esta moviendo")
        elif detenerse <= 1:
            print("La entidad esta detenida")
        else:
            print("La entidad esta detenida") 
    
    
    def saltar (self, avanzar, restroceder):
        if avanzar <= 0:
            print("La entidad esta avanzando saltando")
        elif restroceder >0:
            print("la entidad salto hacia atras")    
        
 
        

print(Grises.__bases__)
print(Raza.__subclasses__())

entidad_azul = Azules("azul", "espacio", 100, "extraterrestres", "ermafrodita", 50)
entidad_azul.caminar(0,1)
print(entidad_azul.color, entidad_azul.region, entidad_azul.cantidad, entidad_azul.constumbres, entidad_azul.genero, entidad_azul.descanso)
entidad_azul.saltar(0,2)
entidad_azul.ejercitarse("ejercitandose", 4)



