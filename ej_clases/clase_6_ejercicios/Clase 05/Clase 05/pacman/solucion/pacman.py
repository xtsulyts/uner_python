class Pacman:

    posicionInicial = [1, 1]

    def __init__(self, mapa):
        self.__posicion = Pacman.posicionInicial
        self.__mapa = mapa

    def mover(self, posicionDestino):
        if posicionDestino in self.mapa:
            if self.__puedeMover(posicionDestino):
                self.posicion = posicionDestino
            else:
                print(
                    "El pacman no se puede mover desde "
                    + str(self.posicion)
                    + " hacia "
                    + str(posicionDestino)
                )
        else:
            print(
                "La posición de destino " + str(posicionDestino) + " no es navegable!!!"
            )

    def __puedeMover(self, posicionDestino):
        posicionX = self.posicion[0]
        posicionY = self.posicion[1]

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

    def copy(self, pacman):
        self.__posicion = pacman.obtenerPosicion()
        self.__mapa = pacman.obtenerMapa()

    def clone(self):
        fantasma = Pacman(self.__mapa)
        fantasma.establecerPosicion(self.__posicion)
        return fantasma

    def equals(self, pacman):
        return (
            self.__posicion == pacman.obtenerPosicion()
            and self.__mapa == pacman.obtenerMapa()
        )
