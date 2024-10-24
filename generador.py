import random
from faker import Faker

fk = Faker()

# Función para generar un número de legajo sin repeticiones+

def generarleg(legajos):
    while True:
        try:
            legajo = random.randint(1000, 9999)
            if legajo not in legajos:
                break
        except ValueError:
            print(f"Error: legajo existente")
            continue
    return legajo

# Función para crear un diccionario con los datos de los atletas
def crearDicAtletas(n):
    atletas = {}
    for a in range(n):
        legajo = generarleg(atletas.keys())
        edad = random.randint(18, 65)
        nombre_completo = fk.name()  # Integrar faker
        intentos = [random.randint(50, 200) for i in range(3)]  # Levantamientos entre 50kg y 200kg
        
        atletas[legajo] = {
            "nombreCompleto": nombre_completo,
            "edad": edad,
            "intentos": intentos,
            "promedio": round(sum(intentos) / 3, 2)
        }
    return atletas

dic = crearDicAtletas(5)

