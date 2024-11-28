#8 función apertura y lectura de archivo csv e informar campeones max Promedio 
def diccionario(filename):
    try:
        with open(filename,"rt") as fp:
            
            atletas ={}
            
            for linea in fp:
                valores = linea.strip().split(",")
                if len(valores)<7:
                    continue
            
                legajo=valores[0]
                nombreCompleto=valores[1]
                edad=int(valores[2])
                intentos=list(map(int, valores[3:6]))
                promedio=float(valores[6])
                
                atletas[legajo] ={
                    "nombreCompleto": nombreCompleto,
                    "edad": edad,
                    "intentos":intentos,
                    "promedio":promedio
                }
    except IOError:
        print("¡Error en la apertura del archivo!")
    return atletas

def campeones(atletas):
    
    atletasOrdenados = sorted(
        atletas.items(),
        key=lambda x: x[1]["promedio"],
        reverse=True
    )[:3]
    for legajo, datos in atletasOrdenados:
        print(f"{legajo} - {datos['nombreCompleto']} - Promedio: {datos['promedio']} kg")

    """atletasCampeones = [
        {
            "legajo": legajo,
            "nombreCompleto": datos['nombreCompleto'],
            "edad": datos["edad"],
            "intentos": datos["intentos"],
            "promedio": datos["promedio"]
        }
        for legajo, datos in atletasOrdenados
    ]"""

    return atletasOrdenados