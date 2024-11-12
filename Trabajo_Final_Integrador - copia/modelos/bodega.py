import json

from modelos.entidadvineria import EntidadVineria

class Bodega(EntidadVineria):
    def __init__(self, id, nombre):
        # self.id = id
        # self.nombre = nombre
        # self.cepas = []
        # self.vinos = []

        super().__init__(id, nombre) 
     

    # Consultas: Se recuperan todos los vinos de la vinoteca y se filtran aquellos que pertenecen a la bodega.
    # def obtenerVinos(self): 
    #     from vinoteca import Vinoteca 
    #     todos_vinos = Vinoteca.obtener_vinos() 
    #     if todos_vinos is not None: 
    #         vinos_bodega = [vino for vino in todos_vinos if self.id in vino.obtenerCepasIds()] 
    #         return vinos_bodega
    #     return []
    

    def obtenerVinos(self):
        from vinoteca import Vinoteca
        todos_vinos = Vinoteca.obtenerVinos()
        if todos_vinos is not None:
            return todos_vinos
        return None
        print(f"Todos los vinos: {todos_vinos}")
        if todos_vinos is not None: 
            vinos_bodega = [vino for vino in todos_vinos if vino.obtenerBodega() and vino.obtenerBodega().obtenerId() == self.id]
            self.vinos = vinos_bodega 
            print(f"Vinos de la bodega {self.nombre}: {vinos_bodega}")
            return vinos_bodega 
        return []

    # Se obtienen todos los vinos de la vinoteca y se filtran de acuerdo con las cepas.
    # def obtenerCepas(self):
    #     vinos_bodega = self.obtenerVinos()
    #     print(f"Vinos de la bodega {self.nombre} para obtener cepas: {vinos_bodega}")
    #     cepas_bodega = {cepa.obtenerId() for vino in vinos_bodega for cepa in vino.obtenerCepas()}
    #     self.cepas = list(cepas_bodega)
    #     print(f"Cepas de la bodega {self.nombre}: {cepas_bodega}")
    #     return list(cepas_bodega)

    def obtenerCepas(self):
        from vinoteca import Vinoteca
        return Vinoteca.obtener_cepas()

    def __repr__(self):
        return json.dumps(self.convertirAJSON())

    # La bodega representa un diccionario JSON básico.
    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "vinos": self.obtenerVinos(),
        }

    # En este caso, se convierte a la bodega en un diccionario JSON completo.
    def convertirAJSONFull(self):
        return self.convertirAJSON()
        # return {
        #     "id": self.obtenerId(),
        #     "nombre": self.obtenerNombre(),
        #     "cepas": self.__mapearCepas(),
        #     "vinos": self.__mapearVinos(),
        # }

    # Métodos privados para mapear cepas y vinos
    # def __mapearCepas(self):
    #     cepas = self.obtenerCepas()
    #     cepasMapa = map(lambda a: a.nombre, cepas)
    #     return list(cepasMapa)
    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        return [cepa.obtenerNombre() for cepa in cepas]


    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        vinosMapa = map(
            lambda a: a.obtenerNombre()
            + " ("
            + a.obtenerBodega().obtenerNombre()
            + ")",
            vinos,
        )
        return list(vinosMapa)

    