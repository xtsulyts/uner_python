# crea una funcion que permita al usuario ingresar un pais y su capital a una lista vacia llamada paises_capitales

paises_capitales = []
paises = []
capitales = []      

for i in range(5):
    inpais =(input("Ingrese el nombre del pais: "))
    incapital =input("Ingrese la capital del pais: ")
    paises_capitales.append([inpais,incapital])

print(f"La lista de paises y capitales es: \n{paises_capitales}")      

