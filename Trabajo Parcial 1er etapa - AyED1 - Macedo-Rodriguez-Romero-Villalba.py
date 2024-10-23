# Rama Guillermo version 2.2l


"""Parte 2:
Pensar en estadisticas se pueden informar a partir de los datos que trabaja el programa

---02-10--- En el ingreso de legajo manejar con (15/22 de P1 - Clase 9) usar excepciones en una función de validar legajos {while true? try? exception}(para que no pongan una letra en el nro de legajo). Modularizar.

Validar los "no repetidos" usando while item in lista

usar diccionarios para relacionar legajos y pesos (???)

Usar la fila "0" para el nombre de las columnas !!OJO!! a partir de ese momento hay que saltear SIEMPRE la primer fila en los readline()

Reemplazar los ingresos con una automatizacion (se ingresa un numero de competidores, se genera legajo (validado), edad (random), y los tres tiros)

se puede hacer una funcion que cree un diccionario a partir de las listas de legajos y nombres completos y edad como un diccionario.

# --------------------------------------------"""


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