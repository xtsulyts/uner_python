#EJERCICIO1) Escribir un programa Python que calcule el índice de masa corporal de una persona (IMC). 
# < 16 | Criterio de ingreso en hospital
# De 16 a 17 | Infrapeso
# De 17 a 18 | Bajo peso
# De 18 a 25 | Peso normal (saludable)
# De 25 a 30 | Sobrepeso (obesidad de grado I)
# De 30 a 35 | Sobrepeso crónico (obesidad de grado II)
# De 35 a 40 | Obesidad premórbida (obesidad de grado III)
# > 40 | Obesidad mórbida (obesidad de grado IV)
# EJERCICIO 2) Para convertir entre las diferent

print("")
print("")
def calcular_imc (peso, altura):
    imc = peso / (altura **2)
    return imc

peso = 0
altura = 0

peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en m: "))

imc = calcular_imc(peso, altura)
if imc < 16:
    print("Criterio de ingreso en hospital")
elif imc < 17:
    print("Infrapeso")
elif imc < 18:
    print("Bajo peso")
elif imc < 25:
    print("Peso normal (saludable)")
elif imc < 30:
    print("Sobrepeso (obesidad de grado I)")
elif imc < 35:
    print("Sobrepeso crónico (obesidad de grado II)")
elif imc < 40:
    print("Obesidad pre-morbida (obesidad de grado III)")
else:
    print("Obesidad morbida (obesidad de grado IV)")    


print("Tu IMC es: ", imc)  

print("")
