import csv
import generador as gen
import random

pesoClasificacion = 150

def main():
    
    n = int(input("Ingrese la cantidad de atletas a simular: "))
    print(gen.crearDicAtletas(n))
    '''ACA VA COMPLETO EL PROGRAMA CON TODAS LAS FUNCIONES LLAMADAS EN ORDEN, SE INICIAN LAS LISTAS
    DE SER NECESARIO, Y COSO COSO'''
    '''def nombreSolo (dic):
    if leg in legajo:
        return leg
    
    try: 
        print(dic[legajo]['nombreCompleto'])
    except KeyError:
        print("El legajo no existe en el diccionario") ESTO ES UNA IDEA '''
    
if __name__=="__main__":
    main()