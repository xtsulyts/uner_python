# funcion que calcula los valores de verdad para los 4 enunciados
def procesar_sentencias(a, b, c):
    print('\na=' + str(b) + ', b=' + str(b) + ', c=' + str(c))

    # modificar sentencia_reducida para el punto i.
    sentencia = (a or b) or (b and c)
    sentencia_reducida = a or b
    print('i. ' + str(sentencia) + ' | ' + str(sentencia_reducida))

    # modificar sentencia_reducida para el punto ii.
    sentencia = b and c or False
    sentencia_reducida = b and c
    print('ii. ' + str(sentencia) + ' | ' + str(sentencia_reducida))

    # modificar sentencia_reducida para el punto iii.
    sentencia = a and b or c or (b and a)
    sentencia_reducida = a and b or c or (b and a) # TODO: a completar por los alumnos.
    print('iii. ' + str(sentencia) + ' | ' + str(sentencia_reducida))

    # modificar sentencia_reducida para el punto iv.
    sentencia = a == True or b == False
    sentencia_reducida = a == True or b == False # TODO: a completar por los alumnos.
    print('iv. ' + str(sentencia) + ' | ' + str(sentencia_reducida))

a=True
b=False
c=False
procesar_sentencias(a, b, c)

a=False
b=True
c=False
procesar_sentencias(a, b, c)

a=False
b=False
c=True
procesar_sentencias(a, b, c)

a=True
b=True
c=False
procesar_sentencias(a, b, c)

a=False
b=True
c=True
procesar_sentencias(a, b, c)

a=True
b=False
c=True
procesar_sentencias(a, b, c)

a=True
b=True
c=True
procesar_sentencias(a, b, c)

a=False
b=False
c=False
procesar_sentencias(a, b, c)