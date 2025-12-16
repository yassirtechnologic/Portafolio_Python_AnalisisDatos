# Comenzamos proyecto1
import numpy as np

nombres = np.array(["Francisco", "Lucia", "Juan", "Paula", "Alba"])
materias = np.array(["html/css", "Javascript", "Base de datos", "Programacion"])
notas = np.array([
    [9, 4, 8, 3],   # Francisco
    [7, 8, 10, 5],  # Lucia
    [10, 8, 6, 8],  # Juan
    [7, 4, 8, 4],   # Paula
    [8, 5, 6, 5]    # Alba
])

# Función para mostrar a los alumnos suspendidos en cada materia
def mostrar_suspenso(nombres, materias, notas):
    for j, materia in enumerate(materias):
        suspendidos = np.sum(notas[:, j] < 5)
        print(f"{materia} se ha suspendido por {suspendidos} alumnos.")

# Función para calcular la nota media de cada alumno
def calcular_media(nombres, notas):
    medias = np.mean(notas, axis=1)
    for i, nombre in enumerate(nombres):
        print(f"{nombre} ha obtenido una nota media de {medias[i]:.2f}.")

# Función para calcular los alumnos que han aprobado el curso
def calcular_aprobados(nombres, notas):
    # Un alumno aprueba si su nota en todas las materias es >= 5
    aprobados = np.all(notas >= 5, axis=1)
    print("Los alumnos que han aprobado el curso son los siguientes:")
    for i, aprobado in enumerate(aprobados):
        if aprobado:
            print(nombres[i])

# Llamamos a las funciones
mostrar_suspenso(nombres, materias, notas)
calcular_media(nombres, notas)
calcular_aprobados(nombres, notas)

# Finalizamos proyecto1
