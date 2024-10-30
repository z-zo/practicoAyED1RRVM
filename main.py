import generadorAtletas as gen
import output as out

# Constante para la clasificación Panamericano
objetivoClasificacion = 150

# Función I: donde mostramos la lista de atletas en formato de tabla desde el proyecto de fundamentos anterior pero ahora con un diccionario
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
#testear la proxima recursividad para imprimir tabla

#Función II: para encontrar mínimo levantado en todo el torneo
def buscarMinimoLevantamiento(atletas):
    minIntento = float(250)
    atletaMinimo = None #None inicia la variable sin darle un valor cuantificable
    
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
#Mejora para final: incluir una lista de todos los que levantaron el minimo

#Función III: para encontrar el record de levantamiento en todo el torneo
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
#Mejora para final: incluir una lista de todos los que levantaron el maximo ya que se registra solo uno

#Función IV: para encontrar el procentaje de clasificados mayor a 150 kilogramos para el Panamericano
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

#Función V: para consultar el promedio de levantamiento de todos los atletas del torneo
def promedioLevantamiento(atletas):
    acumulador = 0
    cantidadIntentos = 0

    for datos in atletas.values():
        acumulador += sum(datos["intentos"])
        cantidadIntentos += len(datos["intentos"])
    
    promedioTotal = round(acumulador / cantidadIntentos, 2) if cantidadIntentos > 0 else 0
    print(f"\nEl promedio total entre todos los intentos de los participantes fue: {promedioTotal} kg")

# Función VI: de consulta pero ahora con un login y con clave en un documento llamado login.txt
def consultarAtleta(atletas):

    while True:
        consulta = input("¿Desea consultar el legajo de un atleta? (si/no): ").strip().lower()
        if consulta in ["si", "no"]:
            break  # Sale del bucle si la respuesta es "si" o "no"
        else:
            print("Usted a ingresado un valor erroneo. Responda por si o por no.")
    
    if consulta == "si":
        usuario = input("Por favor, Juez, ingrese su nombre de usuario para consulta por atleta con legajo específico: ").strip().lower()
        clave = input("Por favor, ingrese su clave: ")
        
        with open("login.txt", "r") as f:
            validado = False
            for linea in f:
                datos = linea.strip().split(",")
                while True:
                    if datos[0] == usuario and datos[1] == clave:
                        validado = True
                        break
                    else:
                        print("Usuario o clave incorrectos. No se puede realizar la consulta.")
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
        print("Consulta finalizada.")


#Programa Principal
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
    mostrarListaCompleta(atletas)
    out.PodiumRecord(atletas)
    out.podiumPromedio(atletas)
    buscarMinimoLevantamiento(atletas)
    buscarMaximoLevantamiento(atletas)
    porcentajeClasificados(atletas)
    promedioLevantamiento(atletas)
    consultarAtleta(atletas)
    out.exportarInforme(atletas)

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