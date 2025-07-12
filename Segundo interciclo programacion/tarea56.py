#menu archivo
import os

with open("archivo1.txt", "w") as f:
    f.write("Este es el archivo 1.\n")
print("Se creó 'archivo1.txt'.")
with open("archivo2.txt", "w") as f:
    f.write("Este es el archivo 2.\n")

print("Se creó 'archivo2.txt'.")
print("\nEscribe lo que quieras guardar en 'archivo1.txt'.")
print("Escribe 'salir' para terminar.\n")

while True:
    texto = input("Escribe: ")
    if texto.lower() == "salir":
        break
    with open("archivo1.txt", "a") as f:
        f.write(texto + "\n")
    print("Texto guardado.")
if os.path.exists("archivo2.txt"):
    os.remove("archivo2.txt")
    print("\nSe eliminó 'archivo2.txt'.")
else:
    print("\nEl archivo2.txt no existe.")

print("Programa finalizado.")
