# librerias
import os
import json

# modelos
from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino

class Vinoteca:

    __archivoDeDatos = json.load("vinoteca.json")
    __bodegas = []
    __cepas = []
    __vinos = []

    @staticmethod
    def inicializar():
        datos = Vinoteca.__parsearArchivoDeDatos()
        Vinoteca.__convertirJsonAListas(datos)

    @staticmethod
    def obtenerBodegas(orden=None, reverso=False):
        bodegas = Vinoteca.__bodegas[:]
        if isinstance(orden, str):
            if orden == "nombre":
                bodegas.sort(key=lambda bodega: bodega.obtenerNombre(), reverse=reverso)
            elif orden == "vinos":
                bodegas.sort(key=lambda bodega: len(bodega.obtenerVinos()), reverse=reverso)
        return bodegas

    @staticmethod
    def obtenerCepas(orden=None, reverso=False):
        cepas = Vinoteca.__cepas[:]
        if isinstance(orden, str):
            if orden == "nombre":
                cepas.sort(key=lambda cepa: cepa.obtenerNombre(), reverse=reverso)
        return cepas

    @staticmethod
    def obtenerVinos(anio=None, orden=None, reverso=False):
        vinos = Vinoteca.__vinos[:]
        if isinstance(anio, int):
            vinos = [vino for vino in vinos if anio in vino.__partidas]
        if isinstance(orden, str):
            if orden == "nombre":
                vinos.sort(key=lambda vino: vino.obtenerNombre(), reverse=reverso)
            elif orden == "bodega":
                vinos.sort(key=lambda vino: vino.obtenerBodega().obtenerNombre(), reverse=reverso)
            elif orden == "cepas":
                vinos.sort(key=lambda vino: ', '.join(vino.__mapearCepas()), reverse=reverso)
        return vinos

    @staticmethod
    def buscarBodega(id):
        for bodega in Vinoteca.__bodegas:
            if bodega.obtenerId() == id:
                return bodega
        return None

    @staticmethod
    def buscarCepa(id):
        for cepa in Vinoteca.__cepas:
            if cepa.obtenerId() == id:
                return cepa
        return None

    @staticmethod
    def buscarVino(id):
        for vino in Vinoteca.__vinos:
            if vino.obtenerId() == id:
                return vino
        return None

    @staticmethod
    def __parsearArchivoDeDatos():
        try:
            with open(Vinoteca.__archivoDeDatos, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
                return datos
        except FileNotFoundError:
            print(f"El archivo {Vinoteca.__archivoDeDatos} no se encuentra.")
            return None
        except json.JSONDecodeError:
            print(f"Error al decodificar el archivo {Vinoteca.__archivoDeDatos}.")
            return None

    @staticmethod
    def __convertirJsonAListas(datos):
        if datos is not None:
            for bodega_data in datos.get("bodegas", []):
                bodega = Bodega()
                # Aquí asumiendo que Bodega tiene un método para establecer nombre e id
                bodega.__id = bodega_data["id"]
                bodega.__nombre = bodega_data["nombre"]
                Vinoteca.__bodegas.append(bodega)

            for cepa_data in datos.get("cepas", []):
                cepa = Cepa()
                cepa.__id = cepa_data["id"]
                cepa.__nombre = cepa_data["nombre"]
                Vinoteca.__cepas.append(cepa)

            for vino_data in datos.get("vinos", []):
                vino = Vino()
                vino.__id = vino_data["id"]
                vino.__nombre = vino_data["nombre"]
                vino.__partidas = vino_data["partidas"]
                # Asumiendo que Vino tiene un método para obtener la bodega por ID
                vino.__bodega = Vinoteca.buscarBodega(vino_data["bodega"])
                Vinoteca.__vinos.append(vino)


    @classmethod
    def imprimirEstado(cls):
        print("Estado de las listas:")
        print("\nBodegas:")
        for bodega in cls.__bodegas:
            print(bodega)

        print("\nCepas:")
        for cepa in cls.__cepas:
            print(cepa)

        print("\nVinos:")
        for vino in cls.__vinos:
            print(vino)

# Para usarlo:
Vinoteca.inicializar()  # Inicializa y carga los datos
Vinoteca.imprimirEstado()  # Imprime el estado de las listas

