from naveEspacial_01 import *
class VideoJuego():

    def main(self):
        naveA = NaveEspacial('R',750)	
        naveB = NaveEspacial('R',1000)
        if (naveA.obtenerAutonomia() > naveB.obtenerAutonomia()):
            print('Nave A')
        else:
            print('Nave B')
        #print(naveB.__str__())
        #print(naveA==naveB)

if __name__ == '__main__':
    videoJ = VideoJuego()
    videoJ.main()