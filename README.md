# practicoProgra1RRVM
Trabajo practico algoritmos y estructura de datos I. Alumnos: Romero, Rodriguez, Villalba, Macedo

Alcance General:

Mejorar las funcionalidades del programa de levantamiento UADE 2023 (Versión 1), reduciendo las variables de ingreso a una, optimizando la automatización de datos y utilizando diccionarios para una mejor organización y manejo de la información

Características:
Automatización de Ingresos: Automatizar el ingreso de datos como legajos, nombre, edad y los tres intentos de levantamientos, validando los legajos y asegurando que sean únicos.

Validaciones: Utilizar excepciones para validar correctamente los legajos (evitando letras) y asegurar que no se repitan los números de legajo mediante un ciclo while true.

Diccionarios: Crear una función que transforme las listas de legajos, nombres completos y edades en un diccionario donde el legajo sea la clave, y el valor una sub diccionario que contenga el nombre completo y la edad como claves a sus valores.

Manejo Avanzado de Datos: Trabajar con listas, matrices, y diccionarios, junto con funciones lambda, slicing, y manejo de excepciones.
Consultas Personalizadas: Habilitar consultas sobre el desempeño de un atleta a partir de su n° de legajo, orientadas a los jueces.

Estadísticas: Incorporar la generación de estadísticas adicionales a partir de los datos de los levantamientos.

El programa recibirá del usuario la cantidad de atletas a simular y devolvera: 

1. Tabla de Resultados de Atletas:
Contenido: Legajo, Edad, Nombre Completo, 1er Intento, 2do Intento, 3er Intento, Promedio de Levantamientos.
2. Atletas Clasificados para los Panamericanos:
Contenido: Legajo, Nombre Completo, Promedio de Levantamientos (solo atletas que superaron 120 kg de promedio).
3. Estadísticas del Torneo:
Contenido: Estadísticas globales del torneo, como el número total de competidores, porcentaje de clasificados, levantamiento máximo, etc.
4. Consultas de Jueces:
Contenido: Resultado de una consulta de un juez, mostrando los intentos de levantamiento de un atleta específico (nombre+apellido).
5. Evolución de Levantamientos por Atleta:

Contenido: Para cada atleta, se mostrarán los tres intentos de levantamiento junto con la variación entre ellos (diferencia entre levantamientos) y su progreso. Esto sirve para identificar si un atleta mejora en los intentos posteriores o si su rendimiento decae.



Descripción del Programa:
Se deberá desarrollar un programa que simule una competencia de levantamiento olímpico (modalidad clean & jerk), con las siguientes características:

Ingreso Automatizado de Atletas:
El ingreso de datos será automatizado: 
el usuario ingresará el número de competidores, y el programa generará automáticamente el legajo (validado y único), edad (aleatoria), y los tres intentos de levantamiento.
Los legajos se generarán utilizando una función que valide que no contengan letras, utilizando un ciclo while true y el manejo de excepciones con try y exception. Los legajos no deben repetirse, por lo que se validará que el número no esté en la lista de legajos ya ingresados utilizando un ciclo while item in lista.

Función de Creación de Diccionario:
Crear una función que tome las listas de legajos, nombres completos y edades, y genere un diccionario donde el legajo sea la clave. El valor asociado a cada legajo será otro diccionario, con dos claves: "edad" para almacenar la edad del atleta, y "nombreCompleto" para almacenar el nombre completo. Este formato permitirá un manejo más organizado y accesible de la información.

Datos de los Atletas:
Para participar, se ingresarán automáticamente el número de legajo (entre 1000 y 9999), la edad (aleatoria entre 18 y 100 años), y el nombre completo en formato "Nombre Apellido".
La finalización del programa se indicará ingresando la variable -1.

Registro de Levantamientos:
Para cada atleta, se generarán tres levantamientos en kilogramos de forma aleatoria.
Si el promedio de los tres levantamientos supera un objetivo de 120 kg, el atleta será clasificado para los Juegos Panamericanos.

Uso de Diccionarios:
Los legajos estarán relacionados con los levantamientos y otros datos de los atletas utilizando diccionarios para un manejo más estructurado de la información.

Manejo de Archivos:
El programa debe utilizar la fila "0" para los nombres de las columnas. Desde ese punto, siempre se debe saltar la primera fila cuando se lean los datos (readline()).

Funcionalidades Clave:

Generación de Tabla de Resultados:
Mostrar una tabla con los legajos, edades, nombres+apellidos, los tres intentos de levantamiento, y el promedio entre los tres intentos.

Clasificación:
Indicar el porcentaje de atletas que superan los 120 kg de promedio y que, por lo tanto, clasifican para los Panamericanos.

Estadísticas:
Generar estadísticas adicionales a partir de los datos recolectados, como el promedio general de levantamientos, el número de intentos fallidos, y el peso total levantado por todos los atletas.
Programación Modular:
Crear una función específica en un módulo independiente, vinculada al código principal.

Uso de Funciones Lambda:
Permitir el ingreso de legajos utilizando una función lambda.

Listas por Comprensión y Slicing:
Implementar el uso de listas por comprensión y slicing en la función encargada de registrar los levantamientos (cargaLevantamiento).

Manejo de Datos Estructurados:
Gestionar listas, matrices y diccionarios para almacenar la información de los atletas y sus intentos.

Función de Creación de Diccionario:
Crear una función que tome las listas de legajos, nombres completos y edades, y genere un diccionario donde el legajo sea la clave, y el valor sea una lista con el nombre completo del atleta y su edad.

Récord del Torneo:
Determinar el intento de levantamiento máximo registrado en todo el torneo, junto con el legajo del atleta correspondiente.

Consultas para Jueces:
Habilitar una consulta para que el juez/usuario pueda ingresar un nombre+apellido y recibir información sobre el intento de levantamiento mínimo de dicho atleta.

