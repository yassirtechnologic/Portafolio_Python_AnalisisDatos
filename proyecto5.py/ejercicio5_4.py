# Comenzamos ejercicio_4
import pandas as pd

# Cargar el archivo CSV en un DataFrame
archivo = r"proyecto5.py\Python_AnalisisDatos\COVID_01-01-2021.csv"  # Ruta corregida
try:
    df = pd.read_csv(archivo)

    # Mostrar las columnas del archivo para verificar
    print("Columnas disponibles en el archivo:", df.columns.tolist())

    # Asegúrate de que las columnas sean correctas
    columnas = ['Country_Region', 'Confirmed', 'Deaths', 'Recovered', 'Active']  # Ajustadas a las columnas reales
    if all(col in df.columns for col in columnas):
        # Agrupar los datos por país y calcular totales
        totales_pais = df.groupby('Country_Region')[['Confirmed', 'Deaths', 'Recovered', 'Active']].sum()

        # Ordenar por casos confirmados en orden descendente
        top_10_paises = totales_pais.sort_values(by='Confirmed', ascending=False).head(10)

        # Mostrar los 10 países con más casos confirmados
        print("Top 10 países con más casos confirmados:")
        print(top_10_paises)
    else:
        print(f"El archivo no tiene las columnas esperadas: {columnas}. Verifica el nombre de las columnas.")
except FileNotFoundError:
    print(f"El archivo '{archivo}' no se encontró. Asegúrate de que el archivo esté en la misma carpeta que este script.")
except pd.errors.EmptyDataError:
    print(f"El archivo '{archivo}' está vacío o no contiene datos válidos.")
except pd.errors.ParserError:
    print(f"Hubo un problema al analizar el archivo '{archivo}'. Verifica que sea un archivo CSV válido.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

# Finalizamos ejercicio_4

