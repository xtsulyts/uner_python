##### ESTRUCTURAS DE CONTROL #####

"""9. Que el usuario ingrese dos números y muestre cuál de los dos es menor. Considerar el caso
en que ambos números son iguales."""


print("")
print("##### EJERCICIO 8 #####")
print("")

def comparar_numeros(a, b):
    if a < b:
        print(f"El primer numero el {a} es el menor.")
    if b < a:
        print(f"El segundo numero el {b} es el menor.")
    if a == b:
        print("Ambos numeros son iguales ingrese numeros diferentes.")
        comparar_numeros(a=int(input("Ingrese un numero: ")), b=int(input("Ingrese otro numero: ")))


comparar_numeros(a = int(input("Ingrese un numero: ")), b = int(input("Ingrese otro numero: ")))

print("")
print("##### FIN DEL PROGRAMA #####")