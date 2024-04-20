import pandas as pd

# Lee el archivo .rpt
with open('UltimoLoginIBP.rpt', 'r') as f:
    lines = f.readlines()

# Define el tamaño de cada trozo
tamanio_trozo = 1000000

# Divide el contenido en trozos de tamaño definido
trozos = [lines[i:i+tamanio_trozo] for i in range(0, len(lines), tamanio_trozo)]

# Crea un nuevo DataFrame para cada trozo y lo guarda en una pestaña de un archivo Excel
with pd.ExcelWriter('archivo_dividido.xlsx') as writer:
    for i, trozo in enumerate(trozos):
        df = pd.DataFrame(trozo, columns=['Linea'])
        df.to_excel(writer, sheet_name=f'Trozo_{i+1}', index=False)

