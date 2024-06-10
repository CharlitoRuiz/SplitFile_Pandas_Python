import pandas as pd

# Lee el archivo .rpt
df = pd.read_csv('ultimoIngresoIBC.rpt', header=None)  # Asegúrate de configurar los parámetros adecuadamente

# Especifica el rango de filas que deseas seleccionar
inicio_fila = 1048576  # La primera fila que quieres incluir
fin_fila = 1582538    # La última fila que quieres incluir (incluida)

# Selecciona el rango de filas especificado
filas_seleccionadas = df.iloc[inicio_fila-1:fin_fila]  # Se resta 1 porque el índice de Python comienza en 0

# Guarda las filas seleccionadas en un nuevo archivo
filas_seleccionadas.to_csv('UltimoLoginIBC_29042024.csv',
                            index=False, header=False)  # Ajusta los parámetros según sea necesario
