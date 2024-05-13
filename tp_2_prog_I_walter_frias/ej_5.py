##### FUNCIONES #####


"""5. Que dado tres números ingresados por el usuario nos devuelva el promedio."""


print("")
print("##### EJERCICIO 5 #####")
print("")

#Funcion que recive tres agumentos para sacar un promedio.
def calcula_promedio(a, b, c):
     a = a
     b = b
     c = c
     promedio = (a + b + c) / 3 #En esta variable se guardara el promedio de los tres numeros solicitados.
     print(f"El promedio es : {promedio}")

#Llamad a la funcion ingresando los argumentos solicitados.
calcula_promedio(a = float(input("Ingrese el peimer el primer numero: ")),
                 b = float(input("Ingrese el segundo numero: ")),
                 c = float(input("Ingrese el tercer numero: ")))
print("")
print("##### FIN DEL PROGRAMA #####")