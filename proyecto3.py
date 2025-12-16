# Comenzamos proyecto3
import random
from itertools import product

# Generar una lista de vectores aleatorios
def generar_vectores():
    num_vectores = random.randint(2, 5)  # Número aleatorio de vectores entre 2 y 5
    vectores = []
    for _ in range(num_vectores):
        longitud = random.randint(2, 5)  # Longitud aleatoria entre 2 y 5
        vector = [random.randint(1, 10) for _ in range(longitud)]
        vectores.append(vector)
    return vectores

# Función para calcular el producto cartesiano
def producto_cartesiano(vectores):
    resultado = list(product(*vectores))
    print("Vectores generados:")
    for i, v in enumerate(vectores, start=1):
        print(f"Vector {i}: {v}")
    print("\nProducto cartesiano:")
    for combinacion in resultado:
        print(combinacion)

# Generar vectores y calcular el producto cartesiano
vectores_aleatorios = generar_vectores()
producto_cartesiano(vectores_aleatorios)

# Finalizamos proyecto3
