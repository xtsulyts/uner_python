#### ESTRUCTURAS DE CONTROL ####

""" 12. Pedir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro
mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día
ingresado no es ninguno de esos, imprimir otro mensaje."""

print("")
print("##### EJERCICIO 12 #####")
print("")

lunes = "lunes"
martes = "martes"
miercoles = "miercoles"
jueves = "jueves"
viernes = "viernes"
sabado = "sabado"
domingo = "domingo"

def dia_semana (dia):
    print(f"Elegiste el dia {dia}!!!")
    if dia.lower() == lunes:
        print(f"Hoy es {lunes} empieza una nueva semana!")

    elif dia.lower() == martes:
        print(f"Es {martes} un dia de muchas actividades, laburo a la mañana, taewoondo con Lola y a la noche Programacion I, hay que arrancar organizado")

    elif dia.lower() == miercoles:
        print(f"Los {miercoles} a la mañana tengo ingles, a la tarde Introducción a la un formatica y a la noche practica docente.")   

    elif dia.lower() == jueves:
        print(f"EL {jueves} es el unico dia libre que tengo, es como mi franco!")

    elif dia.lower() == viernes:
        print(f"Los {viernes} son dias agitados! se viene el fin de semana, se cursa Programacion a la noche y se termina en algun bar.")

    elif dia.lower() == sabado:
        print(f"Llego {sabado}!!! jeje hay que seguir estudiando.")

    elif dia.lower() == domingo:
        print(f"Los {domingo}s son dias ideales para relajar, hacer alguna actividad al aire libre.")

    else:
        print(f"{dia} no es un dia de la semana, intenta otra vez!")
        dia_semana(dia=input("Hola, ingresa un dia de la semana: "))

dia_semana(dia=input("Hola, ingresa un dia de la semana: "))

print("")
print("##### FIN DEL PROGRAMA #####")
