# Comenzamos proyecto2
import numpy as np

# Definir un array de 4 dimensiones con valores aleatorios entre 1 y 10
array_4d = np.random.randint(1, 10, size=(2, 3, 4, 5))

# Comprobar que el array tiene 4 dimensiones y mostrar sus detalles
print("Dimensiones del array:", array_4d.ndim)
print("Forma del array:", array_4d.shape)
print("Contenido del array:")
print(array_4d)

# Calcular la suma de los elementos en función de sus últimos 2 ejes
suma_ejes = np.sum(array_4d, axis=(-2, -1))

# Mostrar el resultado de la suma
print("\nSuma de los elementos en función de sus 2 últimos ejes:")
print(suma_ejes)

# Finalizamos proyecto2


