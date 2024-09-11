
#Función IV - busqueda en lista para identificar si hay duplicados

def busqueda(lista, valorBuscado):
    pos = -1
    i = 0
    while i<len(lista) and pos==-1:
        if lista[i]==valorBuscado:
            pos=i
        i+=1
    return pos