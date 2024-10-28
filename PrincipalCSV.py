import generadorAtletas as gen
import csv
import os

# la constante en 150 kilogramos para dividir los clasificados y calcular porcentaje de clasificados del total
objetivoClasificacion = 150

# Función para guardar los datos de los atletas en un archivo CSV
def guardarEnCSV(atletas):
    # Definir el nombre del archivo CSV
    archivocsv = "atletas.csv"
    
    # Crear o abrir el archivo CSV para escritura
    with open(archivocsv, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Escribir el encabezado
        writer.writerow(["Legajo", "Nombre Completo", "Edad", "Intento 1 (kg)", "Intento 2 (kg)", "Intento 3 (kg)", "Promedio (kg)"])
        
        # Escribir los datos de los atletas
        for legajo, datos in atletas.items():
            writer.writerow([legajo, datos["nombreCompleto"], datos["edad"]] + datos["intentos"] + [datos["promedio"]])
    
    print(f"Datos de los atletas guardados en '{archivocsv}'.")

# Función que utilizamos para leer datos en nuestro archivo CSV
def leerDesdeCSV(archivocsv):
    atletas = {}
    if not os.path.exists(archivocsv):
        print(f"El archivo '{archivocsv}' no existe.")
        return atletas
    
    with open(archivocsv, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            legajo = row["Legajo"]
            nombreCompleto = row["Nombre Completo"]
            edad = int(row["Edad"])
            intentos = [int(row["Intento 1 (kg)"]), int(row["Intento 2 (kg)"]), int(row["Intento 3 (kg)"])]
            promedio = round(sum(intentos) / len(intentos), 2)
            atletas[legajo] = {
                "nombreCompleto": nombreCompleto,
                "edad": edad,
                "intentos": intentos,
                "promedio": promedio
            }
    return atletas

# Función donde mostramos la lista de atletas en formato de tabla desde el proyecto de fundamentos anterior pero ahora con un diccionario
def mostrarListaCompleta(atletas):
    print("-------------------------------------------------------------------------------------")
    print("\tTABLA DE RESULTADOS DE LA COMPETENCIA DE LEVANTAMIENTO UADE 2024")
    print("-------------------------------------------------------------------------------------")
    print("Legajo | Atleta                | Edad | Int 1(kg)| Int 2(kg)| Int 3(kg)| Promedio(kg)")
    print("-------------------------------------------------------------------------------------")
    for legajo, datos in atletas.items():
        nombreCompleto = datos["nombreCompleto"]
        edad = datos["edad"]
        intentos = datos["intentos"]
        promedio = datos["promedio"]
        print(f"{legajo:<6} | {nombreCompleto:<21} | {edad:<4} | {intentos[0]:<8} | {intentos[1]:<8} | {intentos[2]:<8} | {promedio:<8.2f}")
    print("--------------------------------------------------------------------------------------")

# Función para mostrar el podio (los tres mejores atletas) ahora con medallas
def podiumPromedio(atletas):
    print("-------------------------------------------------------------------------------------")
    print("\tPODIUM DE MEDALLAS DE ATLETAS PARA MÁXIMO LEVANTAMIENTO PROMEDIO")
    print("-------------------------------------------------------------------------------------")
    print("Legajo | Atleta                | Edad | Int 1(kg)| Int 2(kg)| Int 3(kg)| Promedio(kg)")
    print("-------------------------------------------------------------------------------------")
    
    # Ordena atletas por promedio de levantamiento en orden descendente
    atletasOrdenados = sorted(atletas.items(), key=lambda x: x[1]['promedio'], reverse=True)

    # Itera sobre los tres primeros atletas y asigna medallas en función del podio
    for index, (legajo, datos) in enumerate(atletasOrdenados[:3]):
        nombreCompleto = datos["nombreCompleto"]
        edad = datos["edad"]
        intentos = datos["intentos"]
        promedio = datos["promedio"]

        # Define la medalla basada en la posición en el podio
        if index == 0:
            medalla = "🥇"  # Oro
        elif index == 1:
            medalla = "🥈"  # Plata
        elif index == 2:
            medalla = "🥉"  # Bronce

        # Formato de la salida con medalla y espaciado ajustado para la tabla
        print(f"{legajo:<6} | {nombreCompleto:<19} {medalla} | {edad:<4} | {intentos[0]:<8} | {intentos[1]:<8} | {intentos[2]:<8} | {promedio:<8.2f}")
    
    print("--------------------------------------------------------------------------------------")

def PodiumRecord(atletas):
    # Ordenar a los atletas por el levantamiento máximo en un solo intento
    atletasOrdenados = sorted(
        atletas.items(),
        key=lambda x: max(x[1]["intentos"]),
        reverse=True
    )

    # Seleccionar a los tres primeros para el podium
    podium = atletasOrdenados[:3]

    # Mostrar el podium basado en el levantamiento máximo
    print("-------------------------------------------------------------------------------------")
    print("        PODIUM DE MEDALLAS DE ATLETAS CON RECORD DE LEVANTAMIENTO EN UN INTENTO ")
    print("-------------------------------------------------------------------------------------")
    print("Legajo | Atleta                | Edad | Int 1(kg)| Int 2(kg)| Int 3(kg)| Lev. Máximo(kg)")
    print("-------------------------------------------------------------------------------------")
    for i, (legajo, atleta) in enumerate(podium):
        medalla = "🥇" if i == 0 else "🥈" if i == 1 else "🥉"
        intentos = atleta["intentos"]
        max_levantamiento = max(intentos)
        print(f"{legajo:<7}| {atleta['nombreCompleto']:<20} {medalla} | {atleta['edad']:<5}| {intentos[0]:<10}| {intentos[1]:<10}| {intentos[2]:<10}| {max_levantamiento:<10}")
    print("-------------------------------------------------------------------------------------")

#función para encontrar mínimo levantado en todo el torneo
def buscarMinimoLevantamiento(atletas):
    minIntento = float(250)
    atletaMinimo = None
    
    for legajo, datos in atletas.items():
        intentoMinimoActual = min(datos["intentos"])
        if intentoMinimoActual < minIntento:
            minIntento = intentoMinimoActual
            atletaMinimo = (legajo, datos)
    
    if atletaMinimo:
        legajo, datos = atletaMinimo
        print("\nAtleta con el levantamiento mínimo:")
        print(f"Legajo: {legajo}")
        print(f"Nombre: {datos['nombreCompleto']}")
        print(f"Edad: {datos['edad']}")
        print(f"Intentos (kg): {datos['intentos']}")
        print(f"Levantamiento mínimo (kg): {minIntento}")

#función para encontrar el record de levantamiento en todo el torneo
def buscarMaximoLevantamiento(atletas):
    maxIntento = float(0)
    atletaMaximo = None
    
    for legajo, datos in atletas.items():
        intentoMaximoActual = max(datos["intentos"])
        if intentoMaximoActual > maxIntento:
            maxIntento = intentoMaximoActual
            atletaMaximo = (legajo, datos)
    
    if atletaMaximo:
        legajo, datos = atletaMaximo
        print("\nAtleta con el levantamiento máximo: ")
        print(f"Legajo: {legajo}")
        print(f"Nombre: {datos['nombreCompleto']}")
        print(f"Edad: {datos['edad']}")
        print(f"Intentos (kg): {datos['intentos']}")
        print(f"Levantamiento máximo (kg): {maxIntento}")

#función para encontrar el procentaje de clasificados mayor a 150 kilogramos para el Panamericano
def porcentajeClasificados(atletas):
    totalAtletas = len(atletas)
    cantidadClasificados = 0
    
    for datos in atletas.values():
        if datos["promedio"] > objetivoClasificacion:#fijado en 150 al inicio
            cantidadClasificados += 1
    
    if cantidadClasificados > 0:
        porcentaje = round((cantidadClasificados*100)/totalAtletas, 1)
        print(f"\nEl porcentaje de clasificados mayores a {objetivoClasificacion} kilogramos para los siguientes Panamericanos es: {porcentaje} %")
    else:
        print(f"\nNo hay atletas clasificados a los siguientes Panamericanos con un promedio mayor a {objetivoClasificacion} kilogramos, porcentaje 0")

#función para consultar el promedio de levantamiento de todos los atletas del torneo
def promedioLevantamiento(atletas):
    sumador = 0
    cantidadIntentos = 0

    for datos in atletas.values():
        sumador += sum(datos["intentos"])
        cantidadIntentos += len(datos["intentos"])
    
    promedioTotal = round(sumador / cantidadIntentos, 2) if cantidadIntentos > 0 else 0
    print(f"\nEl promedio total entre todos los intentos de los participantes fue: {promedioTotal} kg")

# Función de consulta pero ahora con un login y con clave en un documento llamado login.txt
def consultarAtleta(atletas):
    consulta = input("¿Desea consultar el legajo de un atleta? (si/no): ").strip().lower()
    
    if consulta == "si":
        usuario = input("Por favor, Juez, ingrese su nombre de usuario para consulta por atleta con legajo específico: ")
        clave = input("Por favor, ingrese su clave: ")
        
        with open("login.txt", "r") as file:
            validado = False
            for linea in file:
                datos = linea.strip().split(",")
                if datos[0] == usuario and datos[1] == clave:
                    validado = True
                    break
        
        if validado:
            legajoConsulta = input("Juez, ingrese el legajo de 4 dígitos del atleta que desea consultar: ").strip()
            legajoConsulta = str(legajoConsulta)
            atleta = atletas.get(legajoConsulta)
            
            if atleta:
                print("\nInformación del atleta de consulta para Juez de la Competencia UADE 2024:")
                print(f"Nombre: {atleta['nombreCompleto']}")
                print(f"Edad: {atleta['edad']}")
                print(f"Intentos: {atleta['intentos']}")
                print(f"Promedio de levantamiento: {atleta['promedio']:.2f} kg")
            else:
                print("Legajo no encontrado.")
        else:
            print("Usuario o clave incorrectos. No se puede realizar la consulta.")
            print("Gracias por participar en el torneo Levantamiento UADE 2024")
    elif consulta == "no":
        print("Consulta finalizada.")
    else:
        print("Por favor, ingrese 'si' o 'no'.")

#programa principal
def main():
    while True:
        try:
            n = int(input("Bienvenido al Programa de clasificación Olímpico de Levantamiento de Pesas UADE 2024\nIngrese la cantidad de atletas a simular,\nPara finalizar; presione 0 o cualquier número negativo: "))
            if n <= 0:
                print("Usted ha finalizado el programa, Gracias por participar en el torneo Levantamiento UADE 2024")
                return
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    atletas = gen.crearDicAtletas(n)
    guardarEnCSV(atletas)  # Guardamos los datos en un CSV
    podiumPromedio(atletas)
    PodiumRecord(atletas)
    buscarMinimoLevantamiento(atletas)
    buscarMaximoLevantamiento(atletas)
    porcentajeClasificados(atletas)
    promedioLevantamiento(atletas)
    # Cargar atletas desde CSV
    print("\nCargando datos desde CSV...listo!!!")
    atletasDesdeCSV = leerDesdeCSV("atletas.csv")
    # Opcional: Puedes mostrar los atletas leídos desde el CSV
    mostrarListaCompleta(atletasDesdeCSV)
    # Consultar información de un atleta
    consultarAtleta(atletasDesdeCSV)

    print("--------------------------------------------------------------------------------------------------------------")
    print("Gracias por usar nuestra mas reciente versión del sistema de Puntos del comite olímpico de la UADE")
    print("Para dar comentarios en la mejora del programa por parte de Entrenadores, Jueces u organizadores del programa,")
    print("\t No dude en escribirnos en comiteolimpico@uade.edu.ar")
    print("--------------------------------------------------------------------------------------------------------------")
    
    print("--------------------------------------------------------------------------------------------------------------")
    print("\t SISTEMA DE RESULTADOS DE LA COMPETENCIA DE LEVANTAMIENTO UADE 2024 (c) VERSION 3.0 ")
    print("--------------------------------------------------------------------------------------------------------------")
    print("\t Todos los derechos reservados - Escuela del Sur™ - Programación 1 ")
    print("--------------------------------------------------------------------------------------------------------------")

#llamada de main
if __name__ == "__main__":
    main()
