def obtener_un_solo_caracter(caracter):
    caracter = caracter
    while True:
        #entrada = input("Ingresa un solo caracter: ")
        if len(caracter) == 1:
            return caracter
        else:
            print("Entrada inválida. Por favor, ingresa solo un caracter.")

# Llamar a la función
caracter = obtener_un_solo_caracter(input("Ingresa un solo caracter: "))