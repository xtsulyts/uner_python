#### FUNCIONES ####
#2. Que reciba un número entero positivo y una potencia a elevar y que nos devuelva el resultado.

def date_enter(n, x):
    resultado = n ** x
    print(f"El resultado es = {resultado}")

print("")
print("##### EJERCICIO 2 #####")
print("")

date_enter(n = int(input("Ingrese un numero: ")),
           x = (int(input("Ingrese a que potencia lo quiere elevar: "))))

print("")
print("##### FIN DEL PROGRAMA #####")

