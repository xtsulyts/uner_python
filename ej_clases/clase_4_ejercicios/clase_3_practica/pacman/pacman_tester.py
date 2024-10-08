from pacman_mapa import mapa
from pacman import Pacman


class PacmanTester:

    def run(self):
        pacman1 = Pacman(mapa)
        print("Pacman1 está en: " + str(pacman1.obtenerPosicion()))
        pacman1.mover([1, 2])
        print("Pacman1 está en: " + str(pacman1.obtenerPosicion()))
        pacman1.mover([2, 2])
        print("Pacman1 está en: " + str(pacman1.obtenerPosicion()))
        pacman1.mover([1, 8])
        print("Pacman1 está en: " + str(pacman1.obtenerPosicion()))
        pacman1.mover([1, 3])
        pacman1.mover([1, 4])
        pacman1.mover([1, 5])
        pacman1.mover([1, 6])
        pacman1.mover([1, 7])
        pacman1.mover([1, 8])
        print("Pacman1 está en: " + str(pacman1.obtenerPosicion()))


if __name__ == "__main__":
    pacmanTester = PacmanTester()
    pacmanTester.run()
