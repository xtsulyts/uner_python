"""b. Escribir una función de nombre es_abc(palabra) la cual retorne True siempre y 
cuando las letras que componen dicha palabra estén en orden alfabético, y False 
en caso contrario"""

def es_abc(palabra):
    return list(palabra) == sorted(palabra)

print(es_abc("abc"))
print(es_abc("cba"))


