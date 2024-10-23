# Rama Emilio versión 2.1.1

import csv
import random
#from faker import Faker instalar la libreria de faker en python
from random import randint
import MdeBusqueda

fk = Faker()

objetivoClasificacion = 120

# Función para generar un número de legajo sin repeticiones
def generarleg(legajos):
    while True:
        try:
            legajo = random.randint(1000, 9999)
            if legajo not in legajos:
                return legajo
        except ValueError:
            continue

# Función para crear un diccionario con los datos de los atletas
def crearDicAtletas(n, legajos, edades, nombres, levantamientos):
    atletas = {}
    for a in range(n):
        legajo = generarleg(legajos)
        edad = random.randint(18, 65)
        nombre_completo = fk.name()  # Integrar Faker para nombres reales
        intentos = [random.randint(50, 200) for i in range(3)]  # Levantamientos entre 50kg y 200kg
        
        legajos.append(legajo)
        edades.append(edad)
        nombres.append(nombre_completo)
        levantamientos.append(intentos)

        atletas[legajo] = {
            "nombreCompleto": nombre_completo,
            "edad": edad,
            "intentos": intentos,
            "promedio": round(sum(intentos) / 3, 2)
        }
    return atletas

# Función I - Determinar rango de validación con manejo de excepciones
def validarRango(inf, sup, mensaje, mensajeError, corte):
    while True:
        try:
            legajo = int(input(mensaje))
            if (legajo >= inf and legajo <= sup) or legajo == corte:
                return legajo
            else:
                print(mensajeError)
        except ValueError:
            print("Error: debe ingresar un número válido.")

# Función II - Validación de ingresos para legajos y edades de atletas con rangos
def ingresarLegajos(legajos, edades):
    legajo = validarRango(1000, 9999, "Bienvenido al Programa de clasificación Olímpico de Levantamiento de Pesas UADE 2024, por favor, Ingrese legajo (entre 1000 y 9999) o para finalizar presione -1: ", "Error, Re-ingrese el número de legajo (entre 1000 y 9999) o -1 para finalizar: ", -1)
    while legajo != -1:
        pos = MdeBusqueda.busqueda(legajos, legajo)
        if pos == -1:
            try:
                edad = int(input("Ingrese la edad del atleta (debe ser igual o mayor a 18 años): "))
                if edad < 18 or edad > 100:
                    print("Error, edad inválida. Vuelva a ingresar el legajo o -1 para finalizar.")
                else:
                    legajos.append(legajo)
                    edades.append(edad)
            except ValueError:
                print("Error: Ingrese una edad válida.")
        else:
            print("Error, legajo duplicado")
        legajo = validarRango(1000, 9999, "Ingrese legajo (entre 1000 y 9999): ", "Error, Re-ingrese el número de legajo (entre 1000 y 9999) o -1 para finalizar: ", -1)

# Función III - Carga de levantamientos de atletas al azar (3 intentos)
def cargaLevantamiento(legajos, levantamientos):
    for _ in range(len(legajos)):
        intentos = [randint(80, 200) for _ in range(3)]
        levantamientos.append(intentos)

# Función IV - Mostrar tabla de clasificación con nombres
def mostrarLista(legajos, nombres, edades, levantamientos):
    print("---------------------------------------------------------------------------------")
    print("\tTABLA DE RESULTADOS DE LA COMPETENCIA DE LEVANTAMIENTO UADE 2024")
    print("---------------------------------------------------------------------------------")
    print("\nLegajo | Nombre Completo         | Edad | Intento 1 | Intento 2 | Intento 3 | Promedio ")
    print("---------------------------------------------------------------------------------")
    for i in range(len(legajos)):
        intentos = levantamientos[i]
        promedio = round(sum(intentos) / 3)
        print(f"{legajos[i]:6d} | {nombres[i]:<24} | {edades[i]:4d} | {intentos[0]:3d} kg    | {intentos[1]:3d} kg    | {intentos[2]:3d} kg    | {promedio:3d} kg")
        print("---------------------------------------------------------------------------------")

# Función V - Calcular porcentaje de atletas clasificados
def calcularPorcentajeClasificados(legajos, levantamientos):
    clasificados = 0
    total = len(legajos)

    for intentos in levantamientos:
        promedio = sum(intentos) / 3
        if promedio > objetivoClasificacion:
            clasificados += 1

    if total > 0:
        porcentajeClasificados = (clasificados * 100) / total
    else:
        porcentajeClasificados = 0

    return porcentajeClasificados

# Función VI - Mostrar levantamiento récord
def levantamientoRecord(legajos, levantamientos):
    record = 0
    legRec = 0

    for i in range(len(legajos)):
        for intento in levantamientos[i]:
            if intento > record:
                record = intento
                legRec = legajos[i]

    print("---------------------------------------------------------------------------------------------------------")
    print(f"El levantamiento record fue del competidor con el legajo {legRec}, con un peso de {record} Kg")
    print("---------------------------------------------------------------------------------------------------------")

# Función VII - Consulta para jueces sobre un legajo y su peso mínimo
def encontrarMinimo(levantamientos, legajos, legajoBuscado):
    minimo = 201
    encontrado = False

    for i in range(len(legajos)):
        if legajos[i] == legajoBuscado:
            minActual = min(levantamientos[i])
            if minActual < minimo:
                minimo = minActual
            encontrado = True

    if not encontrado:
        minimo = 201

    return minimo

# Programa principal
def main():
    legajos = []
    edades = []
    nombres = []
    levantamientos = []

    # Ingreso de datos automáticamente
    crearDicAtletas(3, legajos, edades, nombres, levantamientos)

    # Mostrar lista de resultados
    mostrarLista(legajos, nombres, edades, levantamientos)

    # Calcular porcentaje de clasificados
    porcentajeClasificados = calcularPorcentajeClasificados(legajos, levantamientos)
    print(f'El porcentaje de atletas clasificados al panamericano es: {porcentajeClasificados:.2f}%. Felicidades a los ganadores.')

    # Mostrar levantamiento récord
    levantamientoRecord(legajos, levantamientos)

    # Consulta de levantamiento mínimo para un legajo
    legajoBuscar = validarRango(1000, 9999, "Juez de levantamiento, por favor, Ingrese el legajo del atleta para consultar el intento con su levantamiento mínimo: ", "Error, Re-ingrese el legajo correctamente: ", -1)
    minimoLevantamientos = encontrarMinimo(levantamientos, legajos, legajoBuscar)

    while minimoLevantamientos == 201:
        print(f"No se encontraron levantamientos para el legajo {legajoBuscar}")
        legajoBuscar = validarRango(1000, 9999, "Por favor, Re-Ingrese nuevamente el legajo para consultar el intento con su levantamiento mínimo: ", "Error, Re-ingrese el legajo correctamente: ", -1)
        minimoLevantamientos = encontrarMinimo(levantamientos, legajos, legajoBuscar)

    print(f"El intento con su levantamiento mínimo para el atleta con legajo {legajoBuscar} es: {minimoLevantamientos} Kg")

    # Mensaje de despedida
    print("--------------------------------------------------------------------------------")
    print("Gracias por usar nuestra más reciente versión del sistema de Puntos del comité olímpico de la UADE")
    print("Para dar comentarios en la mejora del programa por parte de Entrenadores, Jueces u organizadores del programa,")
    print("no dude en escribirnos en comiteolimpico@uade.edu.ar")
    print("--------------------------------------------------------------------------------")
    print("SISTEMA DE RESULTADOS DE LA COMPETENCIA DE LEVANTAMIENTO UADE 2024 (c) VERSION 1.0")
    print("--------------------------------------------------------------------------------")
    print("Todos los derechos reservados - Escuela del Sur")

if __name__ == "__main__":
    main()

