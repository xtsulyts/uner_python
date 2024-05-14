#13. Programe una aplicación de consola que solicite al usuario su nombre, después su apellido
#y a continuación su año de nacimiento. 
#Con esos datos deberá generar una sugerencia de usuario y contraseña.
#Por ejemplo: nombre: Martín, apellido: Francisconi, Año nacimiento:1985 -> Usuario: mfrancisconi, Contraseña: mf.1985.

print("")
print("### EJERCICIO NUMERO 13 ###")
print("")

#Defino la veriables para guardar los datos solicitados.
nombre = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")
anio_nacimiento = int(input("Ingrese su anio de nacimineto:"))
print("")

#Imprimo en pantalla lo que solicita el ejercicio.
print("Nombre:", nombre)
print("Apellido:", apellido)

#Los strig para completar las sugerencias los guardo en variables.
#Con el slice selecciono las dos primeros caracteres de nombre y apellido 
#y los concateno.
usuario = nombre.lower()[:1] + apellido.lower()
contrasenia = nombre.lower()[:1] + apellido.lower()[:1] + "."

#Elimino las mayusculas para usuario y contrasenia.
#usuario_final = usuario.lower()
#contrasenia_final = contrasenia.lower()[:1]

print("Usuario:", (usuario))
print(("Contrasenia:"), contrasenia + str(anio_nacimiento))

#Concateno un stirg a los datos ingresados para dar las sugerencias
#que pide el ejercicio.

print("")
print("### FIN DEL PROGRAMA ###")
print("")