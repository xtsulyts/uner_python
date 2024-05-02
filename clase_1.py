

class Restaurante:
    def __init__(self, horario):
        self.horario = horario
        
    def open_restaurante(self, apertura):
        self.apertura = apertura
        return self.apertura 
    
class Personal:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def marcar_ingreso(self, hora_inicio):
        self.hora_inicio = hora_inicio
        print(f"Horari de ingreso es, {hora_inicio}")
    def marcar_salida(self, hora_salida):
        return hora_salida

        
class Areas(Personal):
    def __init__(self, nombre, apellido, dni, departamento):
        super().__init__(nombre, apellido, dni )
        self.departamento= departamento


    def alta_personal(self, empleado):
        self.empleado = empleado
        print(f"Se dio de alta al empleado: {empleado.nombre}, {empleado.apellido}, {empleado.dni}, {self.departamento}")

    def baja_personal(self, baja):
        self.baja = baja        

empleado_1 = Personal("Walter", "Frias", 30435677)
empleada_1 = Personal("Fernanda", "Fernandez", 37886423)

gerencia = Areas("", "", 30435677, "gerencia")
gerencia.alta_personal(empleado_1)
gerencia.marcar_ingreso("10am")











