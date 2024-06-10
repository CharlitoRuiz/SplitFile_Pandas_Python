import pandas as pd
import numpy as np

# Lee el archivo Excel -el excel debe estar en la raiz-
df = pd.read_csv('01062024.csv')

# Divide el DataFrame en trozos de n líneas
trozos = np.array_split(df, len(df) // 999)

#Guarda los segmentos de lineas en archivos separados
for i, trozo in enumerate(trozos):
    nombre_archivo = f'ClientesAEliminar01062024_{i + 1}.csv'  # Nombre del archivo de salida
    trozo.to_csv(nombre_archivo, index=False)     # Guarda el trozo en el archivo con extension .csv en este caso
    print(f'Se ha guardado el segmento {i + 1} en {nombre_archivo}')