import pandas as pd

# Define la ruta al archivo Excel original y la ruta del nuevo archivo Excel
ruta_archivo_original = '27052024/BorrarJose.xlsx'
ruta_archivo_nuevo = '27052024/BorrarJose_Filtrado.xlsx'

# Lee el archivo Excel original
df = pd.read_excel(ruta_archivo_original, header=None)  # 'header=None' asume que no hay encabezados

# Selecciona la columna por índice (por ejemplo, la primera columna es el índice 0)
indice_columna_especifica = 4
columna_especifica = df.iloc[:, [indice_columna_especifica]]

# Guarda la columna seleccionada en un nuevo archivo Excel
columna_especifica.to_excel(ruta_archivo_nuevo, index=False, header=False)  # 'header=False' asume que no quieres encabezado

print(f'Se ha guardado la columna especifica en {ruta_archivo_nuevo}')