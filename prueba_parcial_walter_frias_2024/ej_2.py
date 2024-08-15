#EJERCICIO 2) Para convertir entre las diferentes escalas de temperaturas Celsius (ºC), Fahrenheit(ºF) se realizan los siguientes cálculos: 
#De ºC a ºF: se multiplica por 1,8 y se suma 32. 
#De ºF a ºC: se resta 32 y se divide entre 1,8.

#Escribir un programa Python con dos funciones para permitir la conversión de escalas: 

print("")
print("")
def convertir_celsius_fharenhait(c):
    c = float(input("Introduce la temperatura en °C: "))
    f = (c * 1.8) + 32
    print("La temperatura en °F es: ", f)       

def convertir_fharenhait_celsius(f):
    f = float(input("Introduce la temperatura en °F: "))
    c = (f - 32) / 1.8
    print("La temperatura en °C es:" , c)

#conversion_53c = convertir_celsius_fharenhait(c = 53)
#print(f"La conversión de 53°C a °F es: {conversion_53c}")
#conversion_77f = convertir_fharenhait_celsius(f = 77)
#print(f"La conversión de 77°F a °C es: {conversion_77f}")
convertir_celsius_fharenhait(c=float)
convertir_fharenhait_celsius(f=float)


