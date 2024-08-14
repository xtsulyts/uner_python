"""b. Escribir una función de nombre es_abc(palabra) la cual retorne True siempre y 
cuando las letras que componen dicha palabra estén en orden alfabético, y False 
en caso contrario"""

def es_abc(palabra):
    return list(palabra) == sorted(palabra)

palabra = "ljodooacn"

resultado = palabra

resultado = es_abc(palabra)

