import pandas as pd

# Lee el archivo CSV
df = pd.read_excel('01062024.xlsx')

# Definir el tamaño del trozo
tamano_trozo = 999

# Guardar los segmentos de líneas en archivos separados
for i in range(0, len(df), tamano_trozo):
    # Selecciona el trozo de líneas correctas
    trozo = df.iloc[i:i + tamano_trozo].copy()
    print(f'Filas de {i} a {i + tamano_trozo} para el archivo {i // tamano_trozo + 1}')
    print(trozo.head())  # Imprime las primeras filas del trozo para verificar
    nombre_archivo = f'ClientesAEliminar01062024_{i // tamano_trozo + 1}.csv'  # Nombre del archivo de salida
    trozo.to_csv(nombre_archivo, index=False)  # Guarda el trozo en el archivo con extensión .csv
    print(f'Se ha guardado el segmento {i // tamano_trozo + 1} en {nombre_archivo}')
