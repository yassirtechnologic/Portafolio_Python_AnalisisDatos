import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Archivos CSV
files = [
    r"proyecto5.py/Python_AnalisisDatos/COVID_01-01-2021.csv",
    r"proyecto5.py/Python_AnalisisDatos/COVID_01-02-2021.csv",
    r"proyecto5.py/Python_AnalisisDatos/COVID_01-03-2021.csv"
]

# Cargar y combinar los datasets
dataframes = [pd.read_csv(file) for file in files]
data = pd.concat(dataframes, ignore_index=True)

# Renombrar columnas para claridad
data.rename(columns={
    'Last_Update': 'Fecha',
    'Province_State': 'Provincia',
    'Confirmed': 'Confirmados',
    'Recovered': 'Recuperados'
}, inplace=True)

# Convertir 'Fecha' a datetime
data['Fecha'] = pd.to_datetime(data['Fecha'], errors='coerce')

# Filtrar datos del primer trimestre 2021
data = data[(data['Fecha'] >= '2021-01-01') & (data['Fecha'] <= '2021-03-31')]

# Agrupar por provincia y fecha
grouped = data.groupby(['Provincia', 'Fecha']).sum().reset_index()

# Configuración del gráfico
date_format = mdates.DateFormatter("%d-%b")

# Generar gráficos separados por provincia
for provincia in grouped['Provincia'].unique():
    plt.figure(figsize=(10, 6))
    subset = grouped[grouped['Provincia'] == provincia]
    plt.plot(subset['Fecha'], subset['Confirmados'], label='Confirmados', color='red')
    plt.plot(subset['Fecha'], subset['Recuperados'], label='Recuperados', color='green')

    plt.title(f'Evolución de COVID-19 en {provincia} - Primer Trimestre 2021')
    plt.xlabel('Fecha')
    plt.ylabel('Número de Casos')
    plt.gca().xaxis.set_major_formatter(date_format)
    plt.xticks(rotation=45)
    plt.legend(title='Categorías')
    plt.tight_layout()
    plt.show()






