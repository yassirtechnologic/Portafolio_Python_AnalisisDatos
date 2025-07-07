import pandas as pd

# Cargar el archivo CSV en un DataFrame
archivo = r"proyecto5.py\Python_AnalisisDatos\COVID_01-01-2021.csv"  # Ruta corregida

try:
    df = pd.read_csv(archivo)
    
    # Mostrar las columnas disponibles en el archivo
    print("Columnas del DataFrame:", df.columns.tolist())
    
    # Asegúrate de que las columnas sean correctas
    columnas = ['Country_Region', 'Province_State', 'Recovered']  # Ajustadas a las columnas reales
    if all(col in df.columns for col in columnas):
        # Filtrar donde 'Recovered' es 0 o está vacío (NaN)
        sin_recuperados = df[(df['Recovered'].isnull()) | (df['Recovered'] == 0)]
        
        # Seleccionar solo las columnas 'Country_Region' y 'Province_State'
        resultado = sin_recuperados[['Country_Region', 'Province_State']]
        
        # Eliminar duplicados si los hay
        resultado = resultado.drop_duplicates()
        
        # Mostrar la lista de provincias y países sin casos recuperados
        print("Provincias y países sin casos recuperados:")
        print(resultado)
    else:
        print(f"El archivo no tiene las columnas esperadas: {columnas}. Verifica los nombres.")
except FileNotFoundError:
    print(f"El archivo {archivo} no se encontró. Asegúrate de que esté en la ruta especificada.")
except Exception as e:
    print(f"Ocurrió un error: {e}")




