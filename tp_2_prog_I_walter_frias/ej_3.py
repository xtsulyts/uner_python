##### FUNCIONES #####


"""3. Que nos calcule el total de una factura tras aplicarle el IVA. La función debe recibir la
cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca
la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%."""

print("")
print("##### EJERCICIO 3 #####")
print("")
def calacular_iva(c, i):
     i = 21
     total_fc = c / 100 * i + c
     print(f"El valor final de la factura es: {total_fc}")

calacular_iva(c = int(input("Ingrese el monto de su factura sin iva: ")), i = 21)

print("")
print("##### FIN DEL PROGRAMA #####")