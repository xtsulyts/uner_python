class Area(Personal):
    def __init__(self, nombre, apellido, edad, departamento):
        super().__init__(nombre, apellido, edad)
        self.departamento = departamento
    
    def dar_alta_empleado(self, empleado):
        print(f"Empleado {empleado.nombre} {empleado.apellido} dado de alta en el departamento {self.departamento}")

# Ejemplo de uso
empleado1 = Personal("Juan", "Perez", 30)
empleado2 = Personal("Maria", "Gomez", 25)

area_ventas = Area("Carlos", "Gutierrez", 40, "Ventas")
area_ventas.dar_alta_empleado(empleado1)
area_ventas.dar_alta_empleado(empleado2)