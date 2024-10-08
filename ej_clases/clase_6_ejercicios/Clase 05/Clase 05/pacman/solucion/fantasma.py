class Fantasma:

    posicionInicial = [13, 11]

    def __init__(self, mapa, color):
        self.__posicion = Fantasma.posicionInicial
        self.__mapa = mapa
        self.__color = color

    def mover(self, posicionDestino):
        if posicionDestino in self.__mapa:
            if self.__puedeMover(posicionDestino):
                self.__posicion = posicionDestino
            else:
                print(
                    "El fantasma no se puede mover desde "
                    + str(self.__posicion)
                    + " hacia "
                    + str(posicionDestino)
                )
        else:
            print(
                "La posición de destino " + str(posicionDestino) + " no es navegable!!!"
            )

    def __puedeMover(self, posicionDestino):
        posicionX = self.__posicion[0]
        posicionY = self.__posicion[1]

        posicionDestinoX = posicionDestino[0]
        posicionDestinoY = posicionDestino[1]

        puedeMover = False

        if posicionX == posicionDestinoX and (
            posicionY - 1 == posicionDestinoY or posicionY + 1 == posicionDestinoY
        ):
            puedeMover = True
        elif posicionY == posicionDestinoY and (
            posicionX - 1 == posicionDestinoX or posicionX + 1 == posicionDestinoX
        ):
            puedeMover = True

        return puedeMover

    def establecerPosicion(self, posicion):
        self.__posicion = posicion

    def obtenerPosicion(self):
        return self.__posicion

    def establecerMapa(self, mapa):
        self.__mapa = mapa

    def obtenerMapa(self):
        return self.__mapa

    def establecerColor(self, color):
        self.__color = color

    def obtenerColor(self):
        return self.__color

    def copy(self, fantasma):
        self.__posicion = fantasma.obtenerPosicion()
        self.__mapa = fantasma.obtenerMapa()
        self.__color = fantasma.obtenerColor()

    def clone(self):
        fantasma = Fantasma(self.__mapa, self.__color)
        fantasma.establecerPosicion(self.__posicion)
        return fantasma

    def equals(self, fantasma):
        return (
            self.__posicion == fantasma.obtenerPosicion()
            and self.__mapa == fantasma.obtenerMapa()
            and self.__color == fantasma.obtenerColor()
        )
