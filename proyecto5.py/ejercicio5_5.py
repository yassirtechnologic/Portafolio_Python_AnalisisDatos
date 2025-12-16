# Comenzamos ejercicio5
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV en un DataFrame
archivo = r"proyecto5.py\Python_AnalisisDatos\COVID_01-01-2021.csv"  # Ruta corregida
try:
    df = pd.read_csv(archivo)

    # Mostrar columnas disponibles (para verificar)
    print("Columnas disponibles en el archivo:", df.columns.tolist())

    # Asegúrate de que las columnas sean correctas
    columnas = ['Country_Region', 'Confirmed', 'Deaths', 'Recovered', 'Active']  # Nombres ajustados
    if all(col in df.columns for col in columnas):
        # Agrupar los datos por país y calcular totales
        totales_pais = df.groupby('Country_Region')[['Confirmed', 'Deaths', 'Recovered', 'Active']].sum()

        # Filtrar países con menos de 150 fallecidos
        filtrados = totales_pais[totales_pais['Deaths'] < 150]

        # Crear el gráfico de barras
        filtrados[['Confirmed', 'Deaths', 'Recovered']].plot(kind='bar', figsize=(12, 6))
        plt.title('Casos confirmados, fallecidos y recuperados (fallecidos < 150)')
        plt.xlabel('Países')
        plt.ylabel('Cantidad')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # Mostrar el gráfico
        plt.show()
    else:
        print(f"El archivo no tiene las columnas esperadas: {columnas}. Verifica los nombres de las columnas en el archivo.")
except FileNotFoundError:
    print(f"El archivo '{archivo}' no se encontró. Asegúrate de que el archivo esté en la ruta especificada.")
except pd.errors.EmptyDataError:
    print(f"El archivo '{archivo}' está vacío o no contiene datos válidos.")
except pd.errors.ParserError:
    print(f"Hubo un problema al analizar el archivo '{archivo}'. Verifica que sea un archivo CSV válido.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

# Finalizamos ejercicio5
