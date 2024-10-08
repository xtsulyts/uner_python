class Persona:

    def __init__(self, nom, ape, dni):
        self.__nombre = nom
        self.__apellido = ape
        self.__dni = dni

    def establecerNombre(self, nom):
        self.__nombre = nom

    def establecerApellido(self, ape):
        self.__apellido = ape

    def establecerDni(self, dni):
        self.__dni = dni

    def obtenerNombre(self):
        return self.__nombre

    def obtenerApellido(self):
        return self.__apellido

    def obtenerDni(self):
        return self.__dni

    def copy(self, persona2):
        self.__nombre = persona2.obtenerNombre()
        self.__apellido = persona2.obtenerApellido()
        self.__dni = persona2.obtenerDni()

    def clone(self):
        persona2 = Persona(self.__nombre, self.__apellido, self.__dni)
        return persona2

    def equals(self, persona2):
        return (
            self.__nombre == persona2.obtenerNombre()
            and self.__apellido == persona2.obtenerApellido()
            and self.__dni == persona2.obtenerDni()
        )
    
    def __eq__(self, persona2):
        return self.__dni == persona2.obtenerDni()

nico = Persona('Nicolas', 'Gonzalez', '39263616')
nico2 = Persona('Nicolas', 'Gonzalez', '39263616')
print(id(nico))
print(id(nico2))
print(nico == nico2)
print(nico.equals(nico2))
