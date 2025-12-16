# Comenzamos proyecto4
import numpy as np
import pandas as pd

# Generar una lista de números enteros aleatorios entre 0 y 20 y convertirlo en una serie
lista_numeros = np.random.randint(0, 21, 10).tolist()
serie_A = pd.Series(lista_numeros, name="serieA")
print("Contenido de la serie A:")
print(serie_A)

# Generar un array de 10 números enteros aleatorios entre 0 y 20 y convertirlo en una serie
array_numeros = np.random.randint(0, 21, 10)
serie_B = pd.Series(array_numeros, name="serieB")
print("\nContenido de la serie B:")
print(serie_B)

# Función para comprobar posiciones de múltiplos de 3 en una serie
def encontrar_posicion_multiplo_3(serie):
    indices = serie[serie % 3 == 0].index
    print("\nPosiciones de los números múltiplos de 3 en la serie:")
    print(list(indices))

# Invocar la función con serie A
encontrar_posicion_multiplo_3(serie_A)

# Función para encontrar elementos comunes entre las 2 series
def encontrar_comunes(serie1, serie2):
    comunes = serie1[serie1.isin(serie2)]
    print("\nElementos comunes entre las series:")
    print(comunes)

# Invocar la función con serie A y serie B
encontrar_comunes(serie_A, serie_B)

# Función para encontrar elementos de la primera serie que no están en la segunda
def encontrar_no_comunes(serie1, serie2):
    no_comunes = serie1[~serie1.isin(serie2)]
    print("\nElementos de la primera serie que no están en la segunda:")
    print(no_comunes)

# Invocar la función con serie A y serie B
encontrar_no_comunes(serie_A, serie_B)

# Generar un DataFrame que compare serie A y serie B
df = pd.DataFrame({'serieA': serie_A, 'serieB': serie_B})
df.index.name = 'indice'
print("\nDataFrame comparando serieA y serieB:")
print(df)

# Generar una serie con valores aleatorios y crear un DataFrame de 7 x 7
serie_C = pd.Series(np.random.randint(1, 11, 49), name="serieC")
dataframe_c = pd.DataFrame(serie_C.values.reshape(7, 7))
print("\nDataFrame de 7 filas y 7 columnas generado a partir de serieC:")
print(dataframe_c)

# Finalizamos proyecto4




