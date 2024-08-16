"""e. Escribir un procedimiento numeros_par_impar(entrada) que, dada una lisa de 
números, eleve cada elemento impar en ella al cuadrado y los mueva a otra lista 
e imprima ambas. La lista de números la ingresa el usuario en forma de números 
separados por coma.
Suponiendo que el usuario ingresa la siguiente lista:
1,2,3,4,5,6,7,8,9
Entonces, la salida del programa debería ser:
2,4,6,8
1,9,25,49,81"""

def numeros_par_impar():
    entrada = []
    numeros_impares = []
    numeros_pares = []
    numeros_impares_cuadrado = []
    cantidad_ingresos = 0

    while cantidad_ingresos <= 10:
        ingreso_datos = int(input("Ingrese un numero: "))
        entrada.append(ingreso_datos)
        cantidad_ingresos += 1
        print(f"Cantidad de intento: { cantidad_ingresos}")
        if cantidad_ingresos == 10:
            
            break
  
        print(cantidad_ingresos)
        print(entrada)
        if ingreso_datos % 2 == 0:
            numeros_pares.append(ingreso_datos)
            #print(f"Cantidad de intento: { cantidad_ingresos}")
            #print(f"Los numeros pares son: {numeros_pares}")
        else:
            numeros_impares.append(ingreso_datos)
            elevados = ingreso_datos ** 2
            numeros_impares_cuadrado.append(elevados)
            #print(f"Los numeros impares son: {numeros_impares}")
    print(f"Los numeros pares son: {numeros_pares}")
    print(f"Los numeros impares son: {numeros_impares}")
    print(f"Los numeros impares elevados al cuadrado son: {numeros_impares_cuadrado}")
    print("Fin del programa")


  

        

numeros_par_impar()

