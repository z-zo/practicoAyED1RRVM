import random
"""
Documentación multilínea sobre programación modular generadorAtletas

•Según el número de atletas que el usario presione al incio del programa
•Devuelve al archivo Principal un diccionario con claves y valores para cada uno de los atletas
•También crea un archivo csv llammado atletas.csv
        
        atletas[str(legajo)] = {
            "nombreCompleto": nombreCompleto,
            "edad": edad,
            "intentos": intentos,
            "promedio": round(sum(intentos) / 3, 2)
        }
    print("Diccionario de atletas generado:", atletas)
"""
from faker import Faker #libreria conectada por nino de python3 pip -m con nombres al azar
fk = Faker()

# Función para generar un número de legajo sin duplicados
def generarleg(legajos):
    while True:
        legajo = random.randint(1000, 9999)
        if legajo not in legajos: #busqueda de fundamentos cambiada a busqueda not in para evitar duplicados
            return legajo

# Función para crear un diccionario con los datos de los atletas
def crearDicAtletas(n):
    atletas = {}
    for _ in range(n):
        legajo = generarleg(atletas.keys())
        edad = random.randint(18, 25)
        nombreCompleto = fk.name()  # Genera nombres aleatorios
        intentos = [random.randint(50, 250) for _ in range(3)]  # 3 Intentos de levantamiento en kg / lista por comprensión
        #creación diccionario clave:valor 
        atletas[str(legajo)] = {
            "nombreCompleto": nombreCompleto,
            "edad": edad,
            "intentos": intentos,
            "promedio": round(sum(intentos) / 3, 2)
        }
    #print("Diccionario de atletas generado:", atletas)
    return atletas
