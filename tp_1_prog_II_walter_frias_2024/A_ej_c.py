"""c. Escriba un procedimiento procesar_palabras(entrada) que acepte una 
secuencia de palabras separadas por coma, las ordene y las imprima. 
Suponiendo que la entrada provista al programa es la siguiente:
te,felicito,que,bien,actuas
La salida esperada es:
actuas,bien,felicito,que,te"""

def procesar_palabras(entrada):
    entrada = entrada.split(",")
    entrada.sort()
    print(entrada)
procesar_palabras("te,felicito,que,bien,actuas")

