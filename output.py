import csv

# Función Ib: para mostrar el podio (los tres mejores atletas) ahora con medallas
def podiumPromedio(atletas):
    print("-------------------------------------------------------------------------------------")
    print("\tPODIUM DE MEDALLAS DE ATLETAS PARA MÁXIMO LEVANTAMIENTO PROMEDIO")
    print("-------------------------------------------------------------------------------------")
    print("Legajo | Atleta                | Edad | Int 1(kg)| Int 2(kg)| Int 3(kg)| Promedio(kg)")
    print("-------------------------------------------------------------------------------------")
    
    # Ordena atletas por promedio de levantamiento en orden descendente
    atletasOrdenados = sorted(atletas.items(), key=lambda x: x[1]['promedio'], reverse=True)

    # Itera sobre los tres primeros atletas y asigna medallas en función del podio
    for i, (legajo, datos) in enumerate(atletasOrdenados[:3]):
        nombreCompleto = datos["nombreCompleto"]
        edad = datos["edad"]
        intentos = datos["intentos"]
        promedio = datos["promedio"]

        # Define la medalla basada en la posición en el podio
        if i == 0:
            medalla = "🥇"  # Oro
        elif i == 1:
            medalla = "🥈"  # Plata
        elif i == 2:
            medalla = "🥉"  # Bronce

        # Formato de la salida con medalla y espaciado ajustado para la tabla
        print(f"{legajo:<6} | {nombreCompleto:<19} {medalla} | {edad:<4} | {intentos[0]:<8} | {intentos[1]:<8} | {intentos[2]:<8} | {promedio:<8.2f}")
    
    print("--------------------------------------------------------------------------------------")

# Función IIb: para mostrar el podio (los tres mejores atletas) ahora con medallas segun sus levantamientos maximos
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

# Funcion IIIb: exporta una tabla con los puestos y medalla ademas de todos los datos de cada competidor
def exportarInforme(atletas):
    
    while True:
        exportar = input("Desea exportar el informe del torneo? (si/no)").strip().lower()
        if exportar in ["si", "no"]:
            break
        else:
            print("Responda por si o por no.")
    
    if exportar == "si":
        informe = "informe.csv"
        
        # Ordena atletas por promedio para asignar medallas
        atletasOrdenados = sorted(atletas.items(), key=lambda x: x[1]['promedio'], reverse=True)
        medallas = ["Oro", "Plata", "Bronce"] + ["sin medalla" for i in range(len(atletasOrdenados) - 3)]

        # Crear o abrir el archivo CSV para escritura
        with open(informe, mode='w', newline='') as f:
            writer = csv.writer(f)
            
            # Escribir el encabezado
            writer.writerow(["Legajo", "Nombre Completo", "Edad", "Intento 1 (kg)", "Intento 2 (kg)", "Intento 3 (kg)", "Promedio (kg)", "Medalla", "Variacion de Progreso"])
            
            # Escribir los datos de los atletas con medallas en los primeros 3
            for i, (legajo, datos) in enumerate(atletasOrdenados):
                medalla = medallas[i]
                writer.writerow([legajo, datos["nombreCompleto"], datos["edad"], datos["intentos"][0], datos["intentos"][1], datos["intentos"][2], datos["promedio"], medalla, datos.get("variacion")
                ])
        
        print(f"Informe exportado como '{informe}'.")
    else:
        print("Consulta finalizada.")
