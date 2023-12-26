import requests
import pandas as pd

# URL de la API de calidad del aire
api_url = "https://api-ninjas.com/api/airquality"

# DataFrame con los datos demográficos
# Suponiendo que "data" es el DataFrame de datos demográficos ya cargado

# Crear un DataFrame vacío para almacenar los datos de calidad del aire
air_quality_data = pd.DataFrame(columns=["City", "Concentration"])

# Iterar sobre cada fila del DataFrame de datos demográficos
for index, row in data.iterrows():
    city_name = row["City"]  # Nombre de la ciudad
    
    # Hacer la solicitud a la API para obtener los datos de calidad del aire para la ciudad actual
    response = requests.get(api_url, params={"city": city_name})
    
    # Verificar si la solicitud fue exitosa (código 200)
    if response.status_code == 200:
        # Extraer la concentración de la respuesta de la API
        air_quality = response.json().get("concentration")
        
        # Agregar la información al DataFrame de calidad del aire
        air_quality_data = air_quality_data.append({"City": city_name, "Concentration": air_quality}, ignore_index=True)

# Mostrar el DataFrame con la información de calidad del aire por ciudad
print(air_quality_data)# Eliminar columnas especificadas: Race, Count y Number of Veterans
data_cleaned = data.drop(columns=["Race", "Count", "Number of Veterans"])

# Eliminar filas duplicadas
data_cleaned = data_cleaned.drop_duplicates()

# Mostrar las primeras filas del DataFrame limpio
print(data_cleaned.head())
import sqlite3

# Crear una conexión a la base de datos SQLite (si no existe, se creará automáticamente)
conn = sqlite3.connect('datos_demograficos.db')

# Guardar los DataFrames en la base de datos como tablas
data_cleaned.to_sql('datos_demograficos', conn, if_exists='replace')
calidad_aire.to_sql('calidad_aire', conn, if_exists='replace')

# Realizar una consulta para unir ambas tablas y realizar agregaciones
query = '''
    SELECT d.*, c.*
    FROM datos_demograficos AS d
    LEFT JOIN calidad_aire AS c ON d.City = c.city
'''

# Ejecutar la consulta y mostrar las primeras 10 columnas
result = pd.read_sql(query, conn)
print(result.head(10))



