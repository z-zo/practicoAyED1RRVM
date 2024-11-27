import generadorAtletas as gen
import os

#0 Constante para la clasificación Panamericano
objetivoClasificacion = 150

#1 Función para mostrar el podio (los tres mejores atletas) ahora con medallas
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

#2 Función de record de levantamiento
def PodiumRecord(atletas):
    # Ordenar a los atletas por el levantamiento máximo en un solo intento
    atletasOrdenados = sorted(
        atletas.items(),
        key=lambda x: max(x[1]["intentos"]), #ordenando la lista de mayor a menor, comienza en 1 por que el 0 es el titulo de la tabla
        reverse=True 
    )
    #SLICING Seleccionar a los tres primeros para el podium
    podium = atletasOrdenados[:3] #Corta posición 0, 1 y 2

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

#3 Función para encontrar mínimo levantado en todo el torneo
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

#4 Función para encontrar el record de levantamiento en todo el torneo
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

#5 Función para encontrar el procentaje de clasificados mayor a 150 kilogramos para el Panamericano
def porcentajeClasificados(atletas):
    totalAtletas = len(atletas)
    cantidadClasificados = 0
    #ATENCIÓN CREAR UN BLOQUE PROTEGIDO RY EXCEPT PARA LISTA IS ES DIVISION POR 0 TRY EXCEPT
    for datos in atletas.values():
        if datos["promedio"] > objetivoClasificacion:#fijado en 150 al inicio
            cantidadClasificados += 1
    
    if cantidadClasificados > 0:
        porcentaje = round((cantidadClasificados*100)/totalAtletas, 1)
        print(f"\nEl porcentaje de clasificados mayores a {objetivoClasificacion} kilogramos para los siguientes Panamericanos es: {porcentaje} %")
    else:
        print(f"\nNo hay atletas clasificados a los siguientes Panamericanos con un promedio mayor a {objetivoClasificacion} kilogramos, porcentaje 0")

#6 Función para consultar el promedio de levantamiento de todos los atletas del torneo
def promedioLevantamiento(atletas):
    sumador = 0
    cantidadIntentos = 0

    for datos in atletas.values():
        sumador += sum(datos["intentos"])
        cantidadIntentos += len(datos["intentos"])
    
    promedioTotal = round(sumador / cantidadIntentos, 2) if cantidadIntentos > 0 else 0
    print(f"\nEl promedio total entre todos los intentos de los participantes fue: {promedioTotal} kg")

#7 Función donde mostramos la lista de atletas en formato de tabla desde el proyecto de fundamentos anterior pero ahora con un diccionario
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

#8 función apertura y lectura de archivo csv e informar campeones max Promedio 
def abrircsvpromedio(filename):
    campeones=[]
    try:
        with open(filename,"rt") as fp:
            
            atletasauxiliar ={}
            
            for linea in fp:
                valores = linea.strip().split(",")
                if len(valores)<7:
                    continue
            
                legajo=valores[0]
                nombreCompleto=valores[1]
                edad=int(valores[2])
                intentos=list(map(int, valores[3:6]))
                promedio=float(valores[6])
                
                atletasauxiliar[legajo] ={
                    "nombreCompleto": nombreCompleto,
                    "edad": edad,
                    "intentos":intentos,
                    "promedio":promedio
                }
            atletasOrdenados = sorted(
                atletasauxiliar.items(),
                key=lambda x: x[1]["promedio"],
                reverse=True
            )[:3]
            
            for legajos, datos in atletasOrdenados:
                campeones.append({
                    "legajo": legajo,
                    "nombreCompleto": datos['nombreCompleto'],
                    "edad":datos["edad"],
                    "intentos":datos["intentos"],
                    "promedio":datos["promedio"]
                })
                
    except IOError:
        print("¡Error en la apertura del archivo!")
    return campeones
        
        
#9 Función de consulta pero ahora con un login y con clave en un documento llamado login.txt
def consultarAtleta(atletas):
    consulta = input("¿Estimado Juez(a), Desea consultar con legajo entre 1000 y 9999)\nEl perfil completo de levantamiento de un(a) atleta de la competencia? (si/no): ").strip().lower()
    
    if consulta == "si":
        usuario = input("Por favor, Juez(a), ingrese su nombre de usuario(a) en la plataforma: ")
        clave = input("Por favor, ingrese la clave: ")
        
        with open("login.txt", "r") as file:
            validado = False
            for linea in file:
                datos = linea.strip().split(",")
                if datos[0] == usuario and datos[1] == clave:
                    validado = True
                    break
        
        if validado: #str para hacer match entre llave del diccionario y el ingreso del juez en valor entero 4 dígitos
            legajoConsulta = str(input("Juez, ingrese el legajo de 4 dígitos del atleta que desea consultar: ").strip())
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

#10 programa principal
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
    #primera parte del UX/UI
    podiumPromedio(atletas)
    PodiumRecord(atletas)
    buscarMinimoLevantamiento(atletas)
    buscarMaximoLevantamiento(atletas)
    porcentajeClasificados(atletas)
    promedioLevantamiento(atletas)
    mostrarListaCompleta(atletas)
    
    filename = "atletas.csv"
    campeones = abrircsvpromedio(filename)
    print("\nCampeones con los promedios más altos:")
    for atleta in campeones:
        print(f"{atleta['legajo']} - {atleta['nombreCompleto']} - Promedio: {atleta['promedio']:.2f} kg")

    #segunda parte del UX/UI
    consultarAtleta(atletas)

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
