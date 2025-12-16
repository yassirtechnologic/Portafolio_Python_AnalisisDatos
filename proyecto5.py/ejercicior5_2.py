import pandas as pd

# Cargar el archivo CSV en un DataFrame
archivo = r"proyecto5.py\Python_AnalisisDatos\COVID_01-01-2021.csv"

try:
    df = pd.read_csv(archivo)
    
    # Mostrar las columnas disponibles en el archivo
    print("Columnas del DataFrame:", df.columns.tolist())
    
    # Asegurarte de usar las columnas correctas
    columnas = ['Country_Region', 'Confirmed', 'Deaths', 'Recovered', 'Active']
    if all(col in df.columns for col in columnas):
        # Agrupar los datos por país y calcular los totales
        totales_pais = df.groupby('Country_Region')[['Confirmed', 'Deaths', 'Recovered', 'Active']].sum()
        
        # Mostrar los totales
        print("Totales por país:")
        print(totales_pais)
    else:
        print(f"El archivo no tiene las columnas esperadas: {columnas}. Verifica los nombres.")
except FileNotFoundError:
    print(f"El archivo {archivo} no se encontró. Asegúrate de que esté en la ruta especificada.")
except Exception as e:
    print(f"Ocurrió un error: {e}")








