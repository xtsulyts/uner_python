#9. Pida al usuario que ingrese un texto para luego imprimirlo al revés. Ej: HOLA -> ALOH.

print("")
print("### EJERCICIO NUMERO 9 ###")
print("")

#Defino la variable de entrada.
dato = "Escriba un texto: "
texto = input(dato)
tex_alreves = texto[::-1]
print("")

"""Defino una variable con un string vacio para guardar los caracteres
de la iteracion sobre los datos de la variable texo."""
#texto_alreves = ""


"""El bucle va a iterar por cada uno de los caracteres de la variable texto.
En cada iteracion va a guardar temporalmente cada caracter en la variable caracteres.
Para luego gurdarla en la veriable texto_alreves.
A partir de la segunda iteracion se van a concatenar 
el caracter sigiente con el que ya se guardo en texto_alreves.
Asi hasta terminar el recorrido por todos los caracteres."""

#for caracteres in texto:
    #texto_alreves = caracteres + texto_alreves                        

print("##### El texto al reves se leeria asi #####")
#print(texto_alreves)
print(tex_alreves)


print("")
print("### FIN DEL PROGRAMA ###")
print("")