import pandas as pd

# Cargar el archivo Excel en un DataFrame
df = pd.read_excel('ultimoIngresoIBPFabi.xlsx')

# Especifica la columna en la que deseas filtrar los valores nulos
columna_especifica = 'ultimoIngresoBNMiBanco'

# Filtra las filas que tienen valores nulos en la columna específica
filas_nulas = df[df[columna_especifica].isnull()]

# Guarda las filas filtradas en un nuevo archivo Excel
filas_nulas.to_excel('archivo_filtradoG.xlsx', index=False)
