  
# Comenzamos ejercicio_1
import pandas as pd

# Cargar el archivo CSV en un DataFrame
archivo = "proyecto5.py\Python_AnalisisDatos\COVID_01-01-2021.csv"
try:
    # Intentar cargar el archivo CSV
    df = pd.read_csv(archivo)

    # Mostrar información general del DataFrame
    print("Información del DataFrame:")
    print(df.info())

    # Calcular y mostrar la cantidad de datos faltantes por columna
    print("\nCantidad de datos faltantes por columna:")
    print(df.isnull().sum())

    # Mostrar las primeras cinco filas del DataFrame
    print("\nPrimeras cinco filas del DataFrame:")
    print(df.head())

except FileNotFoundError:
    print(f"El archivo '{archivo}' no se encontró. Asegúrate de que el archivo esté en la misma carpeta que este script.")

except pd.errors.EmptyDataError:
    print(f"El archivo '{archivo}' está vacío o no contiene datos válidos.")

except pd.errors.ParserError:
    print(f"Hubo un problema al analizar el archivo '{archivo}'. Verifica que sea un archivo CSV válido.")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

# Finalizamos ejercicio_1
