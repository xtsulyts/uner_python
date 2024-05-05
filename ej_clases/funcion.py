def cuanta_atras(x):
    if x == 0:
        print(("despegar"))
    else:
   
        cuanta_atras(x - 1)

cuanta_atras(x = int(input("Ingrese un numero: ")))
