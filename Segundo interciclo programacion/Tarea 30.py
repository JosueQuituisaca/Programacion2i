palabra_buscar = "python"
contador = 0

with open("archivo.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        contador += linea.lower().count(palabra_buscar)

print(f"La palabra '{palabra_buscar}' aparece {contador} veces.")

#Este código busca cuántas veces aparece la palabra "python" en el archivo "archivo.txt". 
# Lee el archivo línea por línea, convierte cada línea a minúsculas para ignorar mayúsculas y cuenta 
# las veces que aparece la palabra. Al final muestra el total.

