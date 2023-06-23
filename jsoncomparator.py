import json

# Ruta de los archivos JSON en Google Drive
ruta_archivo1 = 'archivo1.json'
ruta_archivo2 = 'archivo2.json'

# Carga los datos de los archivos JSON
with open(ruta_archivo1, 'r') as file:
    data1 = json.load(file)

with open(ruta_archivo2, 'r') as file:
    data2 = json.load(file)

# Compara los archivos JSON
diferencias = {}

for key in data1:
    if key not in data2:
        diferencias[key] = {'valor_original': data1[key], 'valor_modificado': None}
    elif data1[key] != data2[key]:
        diferencias[key] = {'valor_original': data1[key], 'valor_modificado': data2[key]}

for key in data2:
    if key not in data1:
        diferencias[key] = {'valor_original': None, 'valor_modificado': data2[key]}

# Guarda las diferencias en un archivo txt en Google Drive
ruta_archivo_diferencias = 'Ruta para guardar el archivo con las diferencias.'

with open(ruta_archivo_diferencias, 'w') as file:
    for key, values in diferencias.items():
        file.write(f'Diferencia en la clave "{key}":\n')
        file.write(f'Valor original: {values["valor_original"]}\n')
        file.write(f'Valor modificado: {values["valor_modificado"]}\n')
        file.write('---\n')

print("Diferencias guardadas exitosamente en el archivo txt.")
