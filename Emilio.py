# Rama Emilio versión 2.1

"""Parte 2:
Pensar en estadisticas se pueden informar a partir de los datos que trabaja el programa

---02-10--- En el ingreso de legajo manejar con (15/22 de P1 - Clase 9) usar excepciones en una función de validar legajos {while true? try? exception}(para que no pongan una letra en el nro de legajo). Modularizar.

Validar los "no repetidos" usando while item in lista

usar diccionarios para relacionar legajos y pesos (???)

Usar la fila "0" para el nombre de las columnas !!OJO!! a partir de ese momento hay que saltear SIEMPRE la primer fila en los readline()

Reemplazar los ingresos con una automatizacion (se ingresa un numero de competidores, se genera legajo (validado), edad (random), y los tres tiros)

se puede hacer una funcion que cree un diccionario a partir de las listas de legajos y nombres completos y edad como un diccionario.

# --------------------------------------------"""
# import random
import MdeBusqueda
objetivoClasificacion = 120

ingresoInt = lambda mensaje: int(input(mensaje))

#función I - determinar rango de validación
def validarRango (inf, sup, mensaje, mensajeError, corte):
    legajo = int(input(mensaje))
    while (legajo<inf or legajo>sup) and legajo !=corte:
        legajo = int(input(mensajeError))
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
            intentos = [random.randint(80, 200) for _ in range(3)]
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
    
    