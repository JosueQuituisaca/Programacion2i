import csv

with open("datos.csv", newline='', encoding="utf-8") as archivo_csv:
    lector = csv.reader(archivo_csv)
    for fila in lector:
        print(f"Nombre: {fila[0]}, Edad: {fila[1]}, Ciudad: {fila[2]}")

#Este código lee un archivo "datos.csv" donde los datos están separados por comas. 
# Usa la librería csv para separar cada línea en columnas (como nombre, edad, ciudad). 
# Luego imprime cada dato con una etiqueta clara para que sea fácil entender la información.