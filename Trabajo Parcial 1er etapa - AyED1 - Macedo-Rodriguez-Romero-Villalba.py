# Enunciado TP1
# [Macedo,Rodriguez, Romero Quirino y Villalba] 
# SISTEMA DE RESULTADOS DE LA COMPETENCIA DE LEVANTAMIENTO UADE 2024 (c) VERSION 2.0 

#Alcance general: Aumnetar las variables de ingresos del programa de levantamiento UADE 2023 VERSIÓN 1

#Objetivos:
#• Poder ingresar nombres de atletas como cadena de carácteres al programa para lograr una experiencia de usuario mas personalizado
#• Manejar multiples listas y matrices, junto con la funicon lambda, slicing.
#• pedir una consulta de levantamiento minimo para los juezes por el nombre

# Desarrolle un programa que simule una competencia de levantamiento,
# con tres intentos de levantamiento olímpico de clean & jerk por cada atleta.
# El programa debe permitir el ingreso del número de legajo entre 1000 a 9999 y
# el registro de la edad mayor a 18 años y menor de 100 que deben ser validados 
# para poder participar, como también su nombre+espacio+apellido.
# la condición de fin del programa es ingresar la variable de finalización (-1).

# Se deben generar tres intentos de levantamientos en Kg aleatorios para cada atleta,
# Si el promedio entre esos 3 levantamientos supera un objetivo llamado objetivo Clasificación
# con un valor definido de 120 kilogramos, el atleta será clasificado en el torneo para los panamericanos.
# Al finalizar con -1 este programa olímpico informará:

#   1 • Tabla con legajos, edades, nombres+apellido e intentos con datos al azar (random) del 1er levantamiento, 2do levantamiento, 3er levantamiento y el promedio entre las tres.
#   2 • Porcentaje de atletas clasificados superando los 120 kg promedio para el ir a los panamericanos.
#   3 • Crear una función en un módulo propio (programación modular) ligado al código principal
#   4 • Permitir ingresos de legajos con una función lambda
#   5 • Lograr incluir en la función cargaLevantamiento listas por comprensión y uso de slicing
#   6 • Manejo de Datos estructurados (Listas y matrices).
#   6 • EL intento de levantamiento máximo record de todo el torneo con su legajo de participante correspondiente.
#   7 • Permitir al juez/usuario la consulta de un nombe+apellido (cadena de carácteres) informando su intento de peso mínimo de levantamiento.

#--------------------------------------------


#Programa de clasificación Olímpico de Levantamiento de Pesas UADE 2024 ->

from random import randint
from MdeBusqueda import busqueda

objetivoClasificacion = 120

ingresoInt = lambda mensaje: int(input(mensaje))

#función I - determinar rango de validación
def validarRango (inf, sup, mensaje, mensajeError, corte):
    legajo = ingresoInt(mensaje)
    while (legajo<inf or legajo>sup) and legajo !=corte:
        legajo = ingresoInt(mensajeError)
    return legajo

#función II - Validación ingresos de variables para legajo y edades de atletas con rangos
def ingresarAtleta(legajos,edades, nombres):
    legajo = validarRango(1000,9999,"Bienvenido al Programa de clasificación Olímpico de Levantamiento de Pesas UADE 2024, por favor, Ingrese legajo (entre 1000 y 9999): para finalizar presione -1: ","Error, Re-ingrese el número de legajo (entre 1000 y 9999) o -1 para finalizar: ",-1)
    while legajo !=-1:
        pos= busqueda (legajos, legajo)
        if pos==-1:
            edad = int(input("Ingrese la edad del atleta (debe ser igual o mayor a 18 años): "))
            nombre = input("Ingrese el nombe+apellido del atleta: ").lower()
            if edad <18 or edad>100 or not nombre.isalpha():
                print("Error, vuelva a ingresar los datos del atleta correctamente: ")
    
            else:
                legajos.append(legajo)
                edades.append(edad)
                nombres.append(nombre)
        else:
            print("Error, legajo duplicado")
        legajo = validarRango(1000,10000,"Ingrese legajo (entre 1000 y 9999): ","Error, Re-ingrese el número de legajo (entre 1000 y 9999) o -1 para finalizar: ",-1)
    
#Función III - Carga de levantamientos de atletas al azar (3 intentos)
def cargaLevantamiento (liLeg, liLev):
    for i in range(len(liLeg)):
            intentos = [0]*3
            
            for j in range(len(intentos)):
                intentos[j:j+1] = [randint(80,200)]
            liLev.append(intentos)

#Función V - Tabla de clasificación
def mostrarLista(legajos, edades, nombres, liLev):
    print("---------------------------------------------------------------------------------")
    print("\tTABLA DE RESULTADOS DE LA COMPETENCIA DE LEVANTAMIENTO UADE 2024")
    print("---------------------------------------------------------------------------------")
    print("\nLegajo | Edad | nombe+apellido | Intento 1 | Intento 2 | Intento 3 | Promedio ")
    print("---------------------------------------------------------------------------------")
    for i in range(len(legajos)):
        promedio = round((liLev[i][0] + liLev[i][1] + liLev[i][2]) / 3)
        print("%6d | %4d | %10s | %3d kg    | %3d kg    | %3d kg    | %3d kg" % (legajos[i], edades[i], nombres[i].title(), liLev[i][0], liLev[i][1], liLev[i][2], promedio))
        print("---------------------------------------------------------------------------------")

#Función VI - Porcentaje atletas clasificados al panamericano del total de participantes
def calcularPorcentajeClasificados(legajos, liLev):
    clasificados = 0
    total = len(legajos)  # Total de atletas

    for i in range(total):
        promedio = (liLev[i][0] + liLev[i][1] + liLev[i][2]) / 3
        if promedio > objetivoClasificacion:
            clasificados += 1

    if total > 0:
        porcentajeClasificados = (clasificados * 100) / total
    else:
        porcentajeClasificados = 0

    return porcentajeClasificados

# Función VII mostrar levantamientoPesoMaximo
def levantamientoRecord(legajos, liLev):
    record = 0
    legRec = 0

    for i in range(len(legajos)):
        # Comprobar si el levantamiento de la primera lista es el récord
        if liLev[i][0] > record:
            record = liLev[i][0]
            legRec = legajos[i]

        # Comprobar si el levantamiento de la segunda lista es el récord
        if liLev[i][1] > record:
            record = liLev[i][1]
            legRec = legajos[i]

        # Comprobar si el levantamiento de la tercera lista es el récord
        if liLev[i][2] > record:
            record = liLev[i][2]
            legRec = legajos[i]
    print("---------------------------------------------------------------------------------------------------------")
    return print("El levantamiento record fue del competidor con el legajo", legRec, ", con un peso de ", record,"Kg")

#función VIII - Consulta para jueces sobre el un legajo y su Peso Mínimo
def encontrarMinimo(liLev, nombres, nombreBuscado):
    minimo = 201  # Usamos un valor inicial alto como 201, que no se confunda con levantamientos reales
    encontrado = 0  # Variable para indicar si se encontró el nombre buscado (0 no encontrado, 1 encontrado)

    if nombreBuscado in nombres:
            i = nombres.index(nombreBuscado)

            lev1 = liLev[i][0]
            lev2 = liLev[i][1]
            lev3 = liLev[i][2]

            # Encontrar el mínimo entre los 3 levantamientos
            if lev1 < lev2 and lev1 < lev3:
                minActual = lev1
            elif lev2 < lev3:
                minActual = lev2
            else:
                minActual = lev3

            # Actualizar el mínimo global si es necesario
            if minActual < minimo:
                minimo = minActual

            encontrado = 1  # Indicamos que se encontró el nombre buscado

    # Si no se encontró el nombre buscado, retornamos el valor inicial 201
    if encontrado == 0:
        minimo = 201
        if nombreBuscado == "-1":
            minimo=-1

    return minimo

#Programa Principal
def main():
    legajos=[]
    edades=[]
    nombres=[]
    ingresarAtleta(legajos,edades,nombres)
    liLev = []
    
    if len(legajos) != 0:
        for i in range(len(legajos)):
            cargaLevantamiento(legajos, liLev)
        mostrarLista(legajos, edades,nombres,liLev)
        porcentajeClasificados = calcularPorcentajeClasificados(legajos, liLev)
        print('El porcentaje de atletas clasificados al panamericano es: ',porcentajeClasificados,'%, felicidades a al/los participante(s) que gana(n) un ticket a la competencia internacional en Santiago de Chile 2025')
        levantamientoRecord(legajos, liLev)

        
        nombreBuscar = input("Juez de levantamiento, por favor, Ingrese el nombe+apellido del atleta para consultar el intento con su levantamiento mínimo: ").lower()
        minimoLevantamientos = encontrarMinimo(liLev, nombres, nombreBuscar)

        # Mientras no se haya encontrado el mínimo de levantamientos (minimoLevantamientos != 201), seguir pidiendo el legajo.
        while minimoLevantamientos == 201 :
            print("No se encontraron levantamientos para el atleta", nombreBuscar)
            nombreBuscar =input("Por favor, Re-Ingrese nuevamente el nombe+apellido para consultar el intento con su levantamiento mínimo: ")
            minimoLevantamientos = encontrarMinimo(liLev, nombres, nombreBuscar)

        # Cuando se encuentre el mínimo de levantamientos, imprimir el resultado.
        if(minimoLevantamientos != -1):
            print("El intento con su levantamiento mínimo para el atleta con nombe+apellido ", nombreBuscar, "es:", minimoLevantamientos, "Kg")
            print("--------------------------------------------------------------------------------")

    print("PROGRAMA FINALIZADO")
    print("Gracias por usar nuestra mas reciente versión del sistema de Puntos del comite olímpico de la UADE")
    print("Para dar comentarios en la mejora del programa por parte de Entrenadores, Jueces u organizadores del programa,")
    print("no dude en escribirnos en comiteolimpico@uade.edu.ar")

    print("--------------------------------------------------------------------------------")
    print(" SISTEMA DE RESULTADOS DE LA COMPETENCIA DE LEVANTAMIENTO UADE 2024 (c) VERSION 2.0 ")
    print("--------------------------------------------------------------------------------")
    print(" Todos los derechos reservados - Escuela del Sur")
#main
if __name__=="__main__":
    main()
    
#Siguiente Alcance: Crear un programa que logré ingresar nombres y registros de atletas con sus respectivas marcas informando un podium final de 3er, 2do y 1 lugar