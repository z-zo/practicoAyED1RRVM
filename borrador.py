# Importamos el módulo generador con las funciones necesarias
import generadorAtletas as gen

# la constante en 120 kilogramos para dividir los clasificados y calcular porcentaje de clasificados del total
objetivoClasificacion = 150

# Función donde mostramos la lista de atletas en formato de tabla
def mostrarListaCompleta(atletas):
    print("-------------------------------------------------------------------------------------")
    print("\tTABLA DE RESULTADOS DE LA COMPETENCIA DE LEVANTAMIENTO UADE 2024")
    print("-------------------------------------------------------------------------------------")
    print("Legajo | Atleta                | Edad | Int 1(kg)| Int 2(kg)| Int 3(kg)| Promedio(kg)")
    print("-------------------------------------------------------------------------------------")
    # Iteramos sobre cada atleta en el diccionario y mostramos los datos
    for legajo, datos in atletas.items():
        nombreCompleto = datos["nombreCompleto"]
        edad = datos["edad"]
        intentos = datos["intentos"]
        promedio = datos["promedio"]
        # Imprimimos la información del atleta en el formato f string
        print(f"{legajo:<6} | {nombreCompleto:<21} | {edad:<4} | {intentos[0]:<8} | {intentos[1]:<8} | {intentos[2]:<8} | {promedio:<8.2f}")
    print("--------------------------------------------------------------------------------------")

# Función para mostrar el podio (los tres mejores atletas)
def mostrarListaPodio(atletas):
    print("-------------------------------------------------------------------------------------")
    print("\tPODIUM DE MEDALLAS DE ATLETAS CON MAS ALTO LEVANTAMIENTO UADE 2024")
    print("-------------------------------------------------------------------------------------")
    print("Legajo | Atleta                | Edad | Int 1(kg)| Int 2(kg)| Int 3(kg)| Promedio(kg)")
    print("-------------------------------------------------------------------------------------")
    
    # Ordenar los atletas por su promedio (de mayor a menor)
    atletasOrdenados = sorted(atletas.items(), key=lambda x: x[1]['promedio'], reverse=True)

    # Limitar la visualización a los primeros 3 atletas
    for index, (legajo, datos) in enumerate(atletasOrdenados[:3]):  # Slicing para los primeros 3 atletas
        nombreCompleto = datos["nombreCompleto"]
        edad = datos["edad"]
        intentos = datos["intentos"]
        promedio = datos["promedio"]

        # Determinar el símbolo del semáforo según el lugar
        if index == 0:  # Primer lugar
            semaforo = "🟡"  # Círculo amarillo
        elif index == 1:  # Segundo lugar
            semaforo = "⚪"  # Círculo plomo
        else:  # Tercer lugar
            semaforo = "🟠"  # Círculo naranja

        # Formatear los intentos con el semáforo en lugar del asterisco
        intentosSemaforizados = [
            f"{intento} {semaforo}" if intento == max(intentos) else intento
            for intento in intentos
        ]

        print(f"{legajo:<6} | {nombreCompleto:<21} | {edad:<4} | {intentosSemaforizados[0]:<8} | {intentosSemaforizados[1]:<8} | {intentosSemaforizados[2]:<8} | {promedio:<8.2f}")
    
    print("--------------------------------------------------------------------------------------")


# Función para encontrar el atleta con el levantamiento mínimo en kilogramos
def buscarMinimoLevantamiento(atletas):
    minIntento = float(200)
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

# Función para encontrar el atleta con el levantamiento máximo en kilogramos
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
        print("\nAtleta con el levantamiento máximo:")
        print(f"Legajo: {legajo}")
        print(f"Nombre: {datos['nombreCompleto']}")
        print(f"Edad: {datos['edad']}")
        print(f"Intentos (kg): {datos['intentos']}")
        print(f"Levantamiento máximo (kg): {maxIntento}")

# Función para calcular el promedio de clasificados mayores a 120 kgs(testeado y funcionando)
def porcentajeClasificados(atletas):
    totalAtletas = len(atletas)
    cantidadClasificados = 0
    
    for datos in atletas.values():
        if datos["promedio"] > objetivoClasificacion:
            cantidadClasificados += 1
    
    if cantidadClasificados > 0:
        porcentaje = round((cantidadClasificados*100)/totalAtletas,1)
        print(f"\nEl porcentaje de clasificados mayores a {objetivoClasificacion} kilogramos para los siguientes Panamericanos es: {porcentaje} %")
    else:
        print(f"\nNo hay atletas clasificados a los siguientes Panamericanos con un promedio mayor a {objetivoClasificacion} kilogramos, porcentaje 0")

# Función para calcular el promedio total de todos los intentos de los atletas del torneo
def promedioLevantamiento(atletas):
    sumador = 0
    cantidadIntentos = 0

    # Función lambda para calcular el promedio
    calcularPromedio = lambda intentos: round(sum(intentos) / len(intentos), 2) if len(intentos) > 0 else 0

    for datos in atletas.values():
        sumador += sum(datos["intentos"])
        cantidadIntentos += len(datos["intentos"])
    
    promedioTotal = round(sumador / cantidadIntentos, 2) if cantidadIntentos > 0 else 0
    print(f"\nEl promedio total entre todos los intentos de los participantes fue: {promedioTotal} kg")


# Función para consultar un atleta específico después de iniciar sesión
def consultarAtleta(atletas):
    usuario = input("Ingrese su nombre de usuario: ")
    clave = input("Ingrese su clave: ")
    
    # Leer archivo de login para validar usuario y clave
    with open("login.txt", "r") as file:
        validado = False
        for linea in file:
            datos = linea.strip().split(",")
            if datos[0] == usuario and datos[1] == clave:
                validado = True
                break
    
    if validado:
        legajoConsulta = input("Ingrese el legajo del atleta que desea consultar: ").strip()
        # Convertimos el legajo ingresado a cadena (string) y buscamos en el diccionario
        legajoConsulta = str(legajoConsulta) # Aseguramos que es una cadena
        atleta = atletas.get(legajoConsulta)
        
        if atleta:  # Verifica si el atleta existe en el diccionario
            print("\nInformación del atleta:")
            print(f"Nombre: {atleta['nombreCompleto']}")
            print(f"Edad: {atleta['edad']}")
            print(f"Intentos: {atleta['intentos']}")
            print(f"Promedio de levantamiento: {atleta['promedio']:.2f} kg")
            print("Gracias por participar en el torneo.")
        else:
            print("Legajo no encontrado.")
    else:
        print("Usuario o clave incorrectos. No se puede realizar la consulta.")


# Programa principal
def main():
    while True:
        try:
            n = int(input("Bienvenido al Programa de clasificación Olímpico de Levantamiento de Pesas UADE 2024\nIngrese la cantidad de atletas a simular,\nPara finalizar; presione 0 o cualquier número negativo: "))
            if n <= 0:
                print("El número de ingreso de atletas debe ser mayor a 0. Usted ha finalizado el programa.")
                return  # Termina el programa si el número es 0 o negativo
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    # Generamos el diccionario de atletas usando la función generador de nino con faker
    atletas = gen.crearDicAtletas(n)
    # Mostramos la lista de atletas con la tabla de Emilio
    mostrarListaCompleta(atletas)
    # Mostramos la lista de los 3 mejores atletas
    mostrarListaPodio(atletas)
    # Buscamos y mostramos el levantamiento mínimo entre todos los intentos de los atletas
    buscarMinimoLevantamiento(atletas)
    # Buscamos y mostramos el levantamiento máximo entre todos los intentos de los atletas
    buscarMaximoLevantamiento(atletas)
    # Calculamos y mostramos el porcentaje de atletas clasificados mayores a 120 kilogramos del total de participantes
    porcentajeClasificados(atletas)
    # Calculamos y mostramos el promedio de todos los levantamientos de todos los atletas del torneo de halterofilia
    promedioLevantamiento(atletas)
    
    consulta = input("Juez del Torneo, ¿Desea consultar las estadísticas de un atleta en específico? (si/no): ").strip().lower()
    if consulta == "si":
        consultarAtleta(atletas)
    else:
        print("Gracias por participar en el torneo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
