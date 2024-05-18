##### ESTRUCTURAS DE CONTROL #####

"""9. Que el usuario ingrese dos números y muestre cuál de los dos es menor. Considerar el caso
en que ambos números son iguales."""


print("")
print("##### EJERCICIO 9 #####")
print("")

def comparar_numeros(a, b):#Funcion que recibe dos numeros como parametro.
    if a < b:#Con if le digo al programa que que compare los numeros, si el primer numero a es menor que b imprimira que es menor.
        print(f"El primer numero {a} es el menor.")
    elif b < a:#Si el segundo numero b es es menor que a mostara en pantalla que b es menor.
        print(f"El segundo numero {b} es el menor.")
    elif a == b:
        print("Ambos numeros son iguales ingrese numeros diferentes.")#Si ambos numeros son iguales se mostrara un mensaje para que vuelva a ingresar los numeros.
        comparar_numeros(a=int(input("Ingrese un numero: ")), b=int(input("Ingrese otro numero: ")))#Llamada recursiva a la funcion para ingresar conrectamente los numeros.


comparar_numeros(a = int(input("Ingrese un numero: ")), b = int(input("Ingrese otro numero: ")))

print("")
print("##### FIN DEL PROGRAMA #####")