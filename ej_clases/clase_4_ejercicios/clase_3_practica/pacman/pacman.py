class Pacman:

    posicionInicial = [1, 1]

    def __init__(self, mapa):
        self.posicion = Pacman.posicionInicial
        self.mapa = mapa

    def mover(self, posicionDestino):
        if posicionDestino in self.mapa:
            if self.puedeMover(posicionDestino):
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

    #           [2, 1]
    # [1, 2]   [[2, 2]]      [3, 2]
    #           [2, 3]

    def puedeMover(self, posicionDestino):
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

    def obtenerPosicion(self):
        return self.posicion


if __name__ == "__main__":
    pacman1 = Pacman(None)
    print("ACA ESTOY PROBANDO MI CLASE PACMAN")
    print(pacman1.obtenerPosicion())
