


""" Ejercicio de practica, herencia de clase, super class"""


class Personal:
    def __init__(self, nombre: object, apellido: object, dni: object, email: object) -> object:
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.email = email


class Area(Personal):
    def __init__(self, nombre, apellido, dni, email, sector):

        super().__init__(nombre, apellido, dni, email)

        self.employable = None
        self.area = None
        self.sector = sector
        sector = []

    def alta_sector(self, area):
        self.area = []
        for area in area:
            area.append(input("Aggregate area: "))

    def alta_employable(self, employable):
        self.employable = employable
        # empleado = (input("Agregar empledo: "))
        print(
            f"Sa cargado al empleado:{employable.nombre} {employable.apellido}\n DNI: {employable.dni}\n email:{employable.email}\n Al puesto de: {self.sector}")

    def calculatorenunciates(self, asistecncias, ausencias):
        self.asistencias = asistecncias
        self.ausencias = ausencias
        if asistecncias > 26:
            print("El emplado podria darse de baja: ")

    def baja_empleado(self, faltas, empleado):
        self.empleado = empleado
        self.faltas = faltas
        self.baja = False
        while faltas > 3:
            self.baja = True
            print(f"El employable {empleado.nombre} se a dado de baja")

        print("El empaneled falto tres veces en el mes")

    def asignar_sector(self):
        pass


class Sueldo(Area):
    def __init__(self, nombre, apellido, dni, email, sector_1, sector_2, sector_3, categoria_a, categoria_b,
                 categoria_c):
        super().__init__(nombre, apellido, dni, email, sector_1, sector_2, sector_3)
        self.categoria_a = categoria_a
        self.categoria_a = categoria_b
        self.categoria_a = categoria_c


#Objeto Persona
maria = Personal(input("ingrese Nombre: "),
                 input("Ingrese apellido: "),
                 int(input("Ingrese nro de dni:")),
                 input("Ingress el email: "))

#Objeto caja
caja = Area("", "", "", "", input("Ingrese area: "))
caja.alta_employable(maria)
"""walter = Personal(input("ingrese Nombre: "),
                  input("Ingrese apellido: "),
                  int(input("Ingrese nro de dni:")),
                  input("Ingrese el email: "))
cocina = Area("", "", "", "", input("Ingrese area: "))
cocina.alta_empleado(walter)"""





