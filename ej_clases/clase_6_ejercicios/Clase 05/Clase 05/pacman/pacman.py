class Pacman:

    posicionInicial = [1, 1]

    def __init__(self, mapa):
        self.__posicion = Pacman.posicionInicial
        self.__mapa = mapa

    def mover(self, posicionDestino):
        if posicionDestino in self.__mapa:
            if self.puedeMover(posicionDestino):
                self.__posicion = posicionDestino
            else:
                print(
                    "El pacman no se puede mover desde "
                    + str(self.__posicion)
                    + " hacia "
                    + str(posicionDestino)
                )
        else:
            print(
                "La posición de destino " + str(posicionDestino) + " no es navegable!!!"
            )

    #           [2, 1]
    # [1, 2]   [[2, 2]]      [3, 2]
    #           [2, 3]

    def puedeMover(self, posicionDestino):
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
        if isinstance(posicion, list):
            if len(posicion) == 2:
                self.__posicion = posicion

    def obtenerPosicion(self):
        return self.__posicion

    def establecerMapa(self, mapa):
        self.__mapa = mapa

    def obtenerMapa(self):
        return self.__mapa

    def copy(self, pacman2):
        self.__posicion = pacman2.obtenerPosicion()
        self.__mapa = pacman2.obtenerMapa()

    def clone(self):
        pacman2 = Pacman(self.__mapa)
        pacman2.establecerPosicion(self.__posicion)
        return pacman2

    def equals(self, pacman2):
        return (
            self.__posicion == pacman2.obtenerPosicion()
            and self.__mapa == pacman2.obtenerMapa()
        )
