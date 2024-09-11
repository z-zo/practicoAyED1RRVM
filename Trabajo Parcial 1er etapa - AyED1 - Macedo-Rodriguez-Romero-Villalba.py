# Enunciado TP1, Algoritmos y Estructura de Datos turno Noche Grupo 1
# [Macedo, Rodriguez, Romero Quirino y Villalba]

# OBJETIVO DEL PROYECTO: 
#Nuestro objetivo es desarrollar un programa que se pueda utilizar en una competencia deportiva de levantamiento de pesas que lo puedan usar [personas reales].

#ALCANCE: 

#Desarrolle un programa que simule una competencia de levantamiento, con tres intentos de levantamiento olímpico de la técnica de Peso Muerto por cada atleta.
#El programa permite el ingreso del número de legajo de los atletas entre 1000 a 9999 y también permite el registro de la edad de los atletas que son validados como mayores a 18 años para poder participar. 
#La condición de fin es ingresar la variable de finalización (-1).
#Se generarán tres intentos aleatorios de levantamientos en Kg para cada atleta, si el promedio entre esos 3 levantamientos supera un objetivo llamado objetivo Clasificación con un valor definido de 120 kilogramos; el atleta clasifica a los futuros panamericanos en Santiago de Chile 2025.
#Se desarrollara una función de busqueda en un modulo que será llamado desde el código principal.

#A continuacion el programa solicitará el ingreso por medio de usuario y contraseña de un juez para acceder a la información de:

#• Una lista con [legajos], [edades] y una matriz con los tres levantamientos relacionados al legajo.
#• Porcentaje de atletas clasificados a los panamericanos superando los 120kgs promedio entre los tres intentos.
#• El intento de levantamiento máximo récord de todo el torneo con su legajo/s del participante/s correspondiente/s.
#• Permitir al juez(usuario) una búsqueda por legajo particular, recibiendo su información aislada

#--------------------------------------------

#Programa de clasificación Olímpico de Levantamiento de Pesas UADE 2024 ->

import random
import MdeBusqueda
objetivoClasificacion = 120

ingresoInt = lambda mensaje: int(input(mensaje))

#función I - determinar rango de validación
def validarRango (inf, sup, mensaje, mensajeError, corte):
    legajo = ingresoInt(mensaje)
    while (legajo<inf or legajo>sup) and legajo !=corte:
        legajo = ingresoInt(mensajeError)
    return legajo

#función II - Validación ingresos de variables para legajo y edades de atletas con rangos
def ingresarLegajos(legajos,edades):
    legajo = validarRango(1000,9999,"Bienvenido al Programa de clasificación Olímpico de Levantamiento de Pesas UADE 2024, por favor, Ingrese legajo (entre 1000 y 9999) o para finalizar presione -1: ","Error, Re-ingrese el número de legajo (entre 1000 y 9999) o -1 para finalizar: ",-1)
    while legajo !=-1:
        pos= MdeBusqueda.busqueda (legajos, legajo)
        if pos==-1:
            edad = int(input("Ingrese la edad del atleta (debe ser igual o mayor a 18 años): "))
            if edad <18 or edad>100:
                print("Error, edad invalida, vuelva a ingresar legajo o -1 para finalizar: ")
            else:
                legajos.append(legajo)
                edades.append(edad)
        else:
            print("Error, legajo duplicado")
        legajo = validarRango(1000,10000,"Ingrese legajo (entre 1000 y 9999): ","Error, Re-ingrese el número de legajo (entre 1000 y 9999) o -1 para finalizar: ",-1)

#Función III - Carga de levantamientos de atletas al azar (3 intentos)
def cargaLevantamiento (liLeg, liLev):
    for i in range(len(liLeg)):
            intentos = [random.randint(80, 200) for _ in range(3)]#requerimiento comprension 
            liLev.append(intentos)

#Función IV - Tabla de clasificación
def mostrarLista(legajos, edades, levantamiento1, levantamiento2, levantamiento3):
    print("---------------------------------------------------------------------------------")
    print("\tTABLA DE RESULTADOS DE LA COMPETENCIA DE LEVANTAMIENTO UADE 2024")
    print("---------------------------------------------------------------------------------")
    print("\nLegajo | Edad | Intento 1 | Intento 2 | Intento 3 | Promedio ")
    print("---------------------------------------------------------------------------------")
    for i in range(len(legajos)):
        promedio = round((levantamiento1[i] + levantamiento2[i] + levantamiento3[i]) / 3)
        print("%6d | %4d | %3d kg    | %3d kg    | %3d kg    | %3d kg" % (legajos[i], edades[i], levantamiento1[i], levantamiento2[i], levantamiento3[i], promedio))
        print("---------------------------------------------------------------------------------")

#Función V - Porcentaje atletas clasificados al panamericano del total de participantes
def calcularPorcentajeClasificados(legajos, levantamiento1, levantamiento2, levantamiento3):
    clasificados = 0
    total = len(legajos)  # Total de atletas

    for i in range(total):
        promedio = (levantamiento1[i] + levantamiento2[i] + levantamiento3[i]) / 3
        if promedio > objetivoClasificacion:
            clasificados += 1

    if total > 0:
        porcentajeClasificados = (clasificados * 100) / total
    else:
        porcentajeClasificados = 0

    return porcentajeClasificados

# Función VI mostrar levantamientoPesoMaximo
def levantamientoRecord(legajos, levantamiento1, levantamiento2, levantamiento3):
    record = 0
    legRec = 0

    for i in range(len(legajos)):
        # Comprobar si el levantamiento de la primera lista es el récord
        if levantamiento1[i] > record:
            record = levantamiento1[i]
            legRec = legajos[i]

        # Comprobar si el levantamiento de la segunda lista es el récord
        if levantamiento2[i] > record:
            record = levantamiento2[i]
            legRec = legajos[i]

        # Comprobar si el levantamiento de la tercera lista es el récord
        if levantamiento3[i] > record:
            record = levantamiento3[i]
            legRec = legajos[i]
    print("---------------------------------------------------------------------------------------------------------")
    return print("El levantamiento record fue del competidor con el legajo", legRec, ", con un peso de ", record,"Kg")

#función VII - Consulta para jueces sobre el un legajo y su Peso Mínimo
def encontrarMinimo(levantamiento1, levantamiento2, levantamiento3, legajos, legajoBuscado):
    minimo = 201  # Usamos un valor inicial alto como 201, que no se confunda con levantamientos reales
    encontrado = 0  # Variable para indicar si se encontró el legajo buscado (0 no encontrado, 1 encontrado)

    i = 0
    while i < len(legajos):
        if legajos[i] == legajoBuscado:
            lev1 = levantamiento1[i]
            lev2 = levantamiento2[i]
            lev3 = levantamiento3[i]

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

            encontrado = 1  # Indicamos que se encontró el legajo buscado
        i += 1

    # Si no se encontró el legajo buscado, retornamos el valor inicial 201
    if encontrado == 0:
        minimo = 201

    return minimo

#Programa Principal
def main():
    legajos=[]
    edades=[]
    ingresarLegajos(legajos,edades)
    levantamientos =[]

    cargaLevantamiento(legajos, levantamientos)

    print (levantamientos)

    mostrarLista(legajos, edades, levantamiento1, levantamiento2, levantamiento3)
    porcentajeClasificados = calcularPorcentajeClasificados(legajos, levantamiento1, levantamiento2, levantamiento3)
    print('El porcentaje de atletas clasificados al panamericano es: ',porcentajeClasificados,'%, felicidades a al/los participante(s) que gana(n) un ticket a la competencia internacional en Santiago de Chile 2025')
    levantamientoRecord(legajos, levantamiento1, levantamiento2, levantamiento3)

    legajoBuscar = int(input("Juez de levantamiento, por favor, Ingrese el legajo del atleta para consultar el intento con su levantamiento mínimo: "))
    minimoLevantamientos = encontrarMinimo(levantamiento1, levantamiento2, levantamiento3, legajos, legajoBuscar)

    # Mientras no se haya encontrado el mínimo de levantamientos (minimoLevantamientos != 201), seguir pidiendo el legajo.
    while minimoLevantamientos == 201:
        print("No se encontraron levantamientos para el legajo", legajoBuscar)
        legajoBuscar = int(input("Por favor, Re-Ingrese nuevamente el legajo para consultar el intento con su levantamiento mínimo: "))
        minimoLevantamientos = encontrarMinimo(levantamiento1, levantamiento2, levantamiento3, legajos, legajoBuscar)

    # Cuando se encuentre el mínimo de levantamientos, imprimir el resultado.
    print("El intento con su levantamiento mínimo para el atleta con legajo", legajoBuscar, "es:", minimoLevantamientos, "Kg")
    print("--------------------------------------------------------------------------------")
    print("Gracias por usar nuestra mas reciente versión del sistema de Puntos del comite olímpico de la UADE")
    print("Para dar comentarios en la mejora del programa por parte de Entrenadores, Jueces u organizadores del programa,")
    print("no dude en escribirnos en comiteolimpico@uade.edu.ar")

    print("--------------------------------------------------------------------------------")
    print(" SISTEMA DE RESULTADOS DE LA COMPETENCIA DE LEVANTAMIENTO UADE 2024 (c) VERSION 1.0 ")
    print("--------------------------------------------------------------------------------")
    print(" Todos los derechos reservados - Escuela del Sur")
#main
if __name__=="__main__":
    main()