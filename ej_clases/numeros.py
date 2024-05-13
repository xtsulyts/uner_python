# Pedir al usuario que ingrese un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Validar que el número sea positivo
if numero <= 0:
    print("El número ingresado no es válido. Debe ser un entero positivo.")
else:
    # Inicializar una cadena vacía para almacenar los números impares
    impares = ""

    # Iterar desde 1 hasta el número ingresado, con un paso de 2 para obtener solo impares
    for i in range(1, numero + 1, 2):
        # Agregar el número impar a la cadena, separado por comas
        impares += str(i) + ", "

    # Eliminar la última coma y espacio de la cadena
    impares = impares[:-2]

    # Imprimir los números impares separados por comas
    print("Números impares hasta", numero, ":", impares)

    # Inicializar una cadena vacía para almacenar la cuenta regresiva
    cuenta_regresiva = ""

    # Iterar desde el número ingresado hasta 0 (excluyendo 0), con un paso de -1 para la cuenta regresiva
    for i in range(numero, 0, -1):
        # Agregar el número a la cadena de cuenta regresiva, separado por comas
        cuenta_regresiva += str(i) + ", "

    # Eliminar la última coma y espacio de la cadena
    cuenta_regresiva = cuenta_regresiva[:-2]

    # Imprimir la cuenta regresiva separada por comas
    print("Cuenta regresiva desde", numero, "hasta 0:", cuenta_regresiva)