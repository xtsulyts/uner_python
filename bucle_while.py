import random

numero_secreto = random.randint(1, 100)
intentos = 0
adivinado = False

print("Adivina el número secreto (entre 1 y 100):")

while not adivinado:
    intento = int(input("Intento: "))
    intentos += 1

    if intento == numero_secreto:
        print("¡Felicidades! Adivinaste el número en", intentos, "intentos.")
        adivinado = True
    elif intento < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")


