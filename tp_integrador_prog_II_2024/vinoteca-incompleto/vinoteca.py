# librerias
import os
import json
#import modelos.entidad_vineria import EntidadVineria

# modelos
from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino


class Vinoteca:

    __archivoDeDatos = "vinoteca.json"
    # __bodegas = Bodega("nombre",[])
    # __cepas = Cepa("nombre",[])
    # __vinos = []

    def inicializar(datos):
        datos = Vinoteca.__parsearArchivoDeDatos()
        Vinoteca.__convertirJsonAListas(datos)
        print("========================================")
        print("======BODEGAS======")
        print(Vinoteca.__bodegas)
        print("========================================")
        print("======CEPAS======")
        print(Vinoteca.__cepas)
        print("========================================")
        print("======VINOS======")
        print(Vinoteca.__vinos)

    def __parsearArchivoDeDatos():
        try:
            with open(Vinoteca.__archivoDeDatos, "r", encoding="utf-8") as archivo: # Paso 1: Abrir el archivo con un bloque 'with'
                datos = json.load(archivo)# Paso 2: Cargar el contenido del archivo como diccionario usando json.load()
                #print("Datos cargados del archivo:", datos)
            return datos  # Retorna el diccionario cargado del archivo JSON
        except FileNotFoundError:
            print(f"El archivo {Vinoteca.__archivoDeDatos} no fue encontrado.")
            return None

    def __convertirJsonAListas(data):
        # Llama a __parsearArchivoDeDatos para obtener los datos
        #data = Vinoteca.__parsearArchivoDeDatos()

        # Llenar las listas privadas con los datos del diccionario
        Vinoteca.__bodegas = data.get("bodegas", [])
        Vinoteca.__cepas = data.get("cepas", [])
        Vinoteca.__vinos = data.get("vinos", [])


    # def obtenerBodegas(orden=None, reverso=False):
    #     if isinstance(orden, str):
    #         if orden == "nombre":
    #             ver_bodega = Vinoteca.__bodegas[1][2]
    #             print(ver_bodega)
    
    def obtenerBodegas(self):
        print("===BODEGAS===")
        for diccionario in Vinoteca.__bodegas:
            print("nombre", diccionario["nombre"][:], "id", diccionario["id"][:])
       

    def obtenerCepas(self):
        print("===CEPAS===")
        for diccionario in Vinoteca.__cepas:
            print("nombre", diccionario["nombre"][:],
                  "id", diccionario["id"][:], 
                  "partidas", diccionario["partidas"][:])


   

    # def obtenerCepas(orden=None, reverso=False):
    #     if isinstance(orden, str):
    #         if orden == "nombre":
    #             return Vinoteca.__cepas
            
    def obtenerVinos(self):
        print("====VINOS===")
        for diccionario in Vinoteca.__vinos:
            print("nombre", diccionario["nombre"][:], "id", diccionario["id"][:])

    # def obtenerVinos(anio=None, orden=None, reverso=False):
    #     if isinstance(anio, int):
    #         if orden == anio:
    #           pass
    #     if isinstance(orden, str):
    #         if orden == "nombre":
    #             pass  # completar
    #         elif orden == "bodega":
    #             pass  # completar
    #         elif orden == "cepas":
    #             pass  # completar
    #     pass  # completar

    def buscarBodega(id):
        pass  # completar

    def buscarCepa(id):
        pass  # completar

    def buscarVino(id):
        pass  # completar

   
vinoteca_instance = Vinoteca()
vinoteca_instance.inicializar()
vinoteca_instance.obtenerBodegas()
vinoteca_instance.obtenerCepas()
vinoteca_instance.obtenerVinos()

        

