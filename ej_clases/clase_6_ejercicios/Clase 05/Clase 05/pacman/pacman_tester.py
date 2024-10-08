from pacman_mapa import mapa
from pacman import Pacman


class PacmanTester:

    def run(self):
        pacman1 = Pacman(mapa)
        # print("Pacman1 está en: " + str(pacman1.obtenerPosicion()))
        pacman1.mover([1, 2])
        # print("Pacman1 está en: " + str(pacman1.obtenerPosicion()))
        pacman1.mover([2, 2])
        # print("Pacman1 está en: " + str(pacman1.obtenerPosicion()))
        pacman1.mover([1, 8])
        # print("Pacman1 está en: " + str(pacman1.obtenerPosicion()))
        pacman1.mover([1, 3])
        pacman1.mover([1, 4])
        pacman1.mover([1, 5])
        pacman1.mover([1, 6])
        pacman1.mover([1, 7])
        pacman1.mover([1, 8])
        print("Pacman1 está en: " + str(pacman1.obtenerPosicion()))

        # copy
        # pacman2 = Pacman(mapa)
        # print("Pacman2 está en: " + str(pacman2.obtenerPosicion()))
        # pacman1.copy(pacman2)
        # print("Pacman1 está en: " + str(pacman1.obtenerPosicion()))
        # print("Pacman2 está en: " + str(pacman2.obtenerPosicion()))

        # clone
        # pacman2 = pacman1.clone()
        # # pacman2 = pacman1
        # print("Pacman1 está en: " + str(pacman1.obtenerPosicion()))
        # print("Pacman2 está en: " + str(pacman2.obtenerPosicion()))
        # print(pacman1 == pacman2)
        # print(id(pacman1))
        # print(id(pacman2))
        
        # clone / equals
        pacman2 = pacman1.clone()
        print("Pacman1 está en: " + str(pacman1.obtenerPosicion()))
        print("Pacman2 está en: " + str(pacman2.obtenerPosicion()))
        print(pacman1.equals(pacman2))
        print(id(pacman1))
        print(id(pacman2))

if __name__ == "__main__":
    pacmanTester = PacmanTester()
    pacmanTester.run()
