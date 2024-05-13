##### FUNCIONES #####


"""3. Que nos calcule el total de una factura tras aplicarle el IVA. La función debe recibir la
cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca
la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%."""

print("")
print("##### EJERCICIO 3 #####")
print("")

#Defino una funcion que reciba como parametro el importe de la factura y el impuesto que se la aplicara
def calacular_iva(fc, impuesto):
     fc = fc
     impuesto = impuesto
     if impuesto <= 0 : #Si el impuesto es igual o menor a 0 se sumara el IVA 21% automaticamente y mostrata el valor en pantalla.
          fc = fc / 100 * 21 + fc
          print("El porcentaje de impuestos es incorrecto, se aplico IVA 21%")
          print(f"El valor final de la factura mas impuestos es: {fc}")

     elif impuesto > 0: #Si el impuesto es mayor a 0 se aplicara el impuesto que se ingrese por consola y se mostara en pantalla el resultado.
          fc = fc / 100 * impuesto + fc
          print(f"El valor final de la factura mas impuestos es: {fc}")

     """if impuesto == str:
               print("El impuesto solo acepta numeros enteros")
               calacular_iva(fc = int(input("Ingrese el monto de su factura: ")), impuesto = int(input("Ingrese el % de inspuestos:")))"""
          



calacular_iva(fc = float(input("Ingrese el monto de su factura: ")), impuesto = float(input("Ingrese el % de inspuestos:")))

print("")
print("##### FIN DEL PROGRAMA #####")