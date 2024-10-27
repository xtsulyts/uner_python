# librerias
import os
import json

# modelos
# from modelos.bodega import Bodega
# from modelos.cepa import Cepa
# from modelos.vino import Vino


class Vinoteca:

    __archivoDeDatos = "vinoteca.json"
    __bodegas = []
    __cepas = []
    __vinos = []

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
        #Vinoteca.__vinos = data.get("vinos", [])


    def obtenerBodegas(orden=None, reverso=False):
        if isinstance(orden, str):
            if orden == "nombre":
                return 
            elif orden == "vinos":
                pass

    def obtenerCepas(orden=None, reverso=False):
        if isinstance(orden, str):
            if orden == "nombre":
                return Vinoteca.__cepas
            

    def obtenerVinos(anio=None, orden=None, reverso=False):
        if isinstance(anio, int):
            if orden == anio:
              pass
        if isinstance(orden, str):
            if orden == "nombre":
                pass  # completar
            elif orden == "bodega":
                pass  # completar
            elif orden == "cepas":
                pass  # completar
        pass  # completar

    def buscarBodega(id):
        pass  # completar

    def buscarCepa(id):
        pass  # completar

    def buscarVino(id):
        pass  # completar

   
vinoteca_instance = Vinoteca()
vinoteca_instance.inicializar()

        

