print("")
print("##### EJERCICIO 12 #####")
print("")
print("##### DD / MM / AAAA #####")
print("")

#Defino las variables de entrada de datos.
dia = int(input("Ingrese el dia del mes: "))
mes = int(input("Ingrese un mes del año: "))
año = int(input("Ingrese un año: "))
print("")

#Defino una funcion comprobar los parametros de entrada.

def ej_12(dia, mes, año):

#Con el condicional if defino las reglas que deben cumplir los campos.
  if dia <= 31:
   return False
  print("### No puede haber mas de 31 dias en un mes!!! ###")

  if mes <= 12:
   return False
  print("### No puede haber mas de 12 meses en un año!!! ###")

  if año <= 2024:
   return False
  print("### No el año a elegir no puede ser menor a 2024 !!! ###")

#Llamo a la funcion ej_12 para imprimir los mensajes de alerta.
ej_12(dia, mes, año)
print("")
print("## Dia:", dia,",", "Mes:", mes,"y Año:", año,"","##" )

print("")
print("##### FIN DEL PROGRAMA #####")
print("")