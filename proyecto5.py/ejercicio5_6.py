import pandas as pd
import matplotlib.pyplot as plt

# Archivos CSV
files = [
    "proyecto5.py/Python_AnalisisDatos/COVID_01-01-2021.csv",
    "proyecto5.py/Python_AnalisisDatos/COVID_01-02-2021.csv",
    "proyecto5.py/Python_AnalisisDatos/COVID_01-03-2021.csv"
]

# Lista para almacenar los DataFrames
dataframes = []

# Procesar y corregir fechas manualmente
for file in files:
    print(f"Procesando archivo: {file}")
    df = pd.read_csv(file)

    # Corregir fechas manualmente si están vacías o incorrectas
    if "COVID_01-02-2021" in file:
        df['Last_Update'] = '2021-02-01'
    elif "COVID_01-03-2021" in file:
        df['Last_Update'] = '2021-03-01'

    df['Last_Update'] = pd.to_datetime(df['Last_Update'], errors='coerce')
    df['Mes'] = df['Last_Update'].dt.month_name(locale='en')  # Añadir nombre del mes
    dataframes.append(df)

# Combinar todos los datos
data = pd.concat(dataframes, ignore_index=True)

# Agrupar por mes
resumen = data.groupby('Mes')[['Confirmed', 'Deaths', 'Recovered']].sum()

# Ordenar los meses
meses_orden = ['January', 'February', 'March']
resumen = resumen.reindex(meses_orden, fill_value=0)

# Graficar
resumen.plot(kind='bar', figsize=(10, 6), width=0.8)
plt.title('Evolución COVID-19 - Primer Trimestre 2021')
plt.xlabel('Meses')
plt.ylabel('Número de Casos')
plt.xticks(rotation=0)
plt.legend(title='Categorías')
plt.tight_layout()
plt.show()



















