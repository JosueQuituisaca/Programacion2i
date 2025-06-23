# Ejercicio 1
frutas = ["manzana", "banana", "naranja", "uva", "sandía"]
for i in range(len(frutas)):
    print(f"{i}: {frutas[i]}")

# Ejercicio 2
animales = ["gato", "perro", "conejo", "tigre", "león"]
for i, animal in enumerate(animales):
    print(f"{i}: {animal}")

# Ejercicio 3
numeros = [1, 2, 3, 4, 5]
for i, num in enumerate(numeros):
    print(f"Índice {i}: {num}")

# Ejercicio 4
colores = ["rojo", "verde", "azul", "amarillo", "morado"]
for i in range(len(colores)):
    print(f"{i}: {colores[i]}")

# Ejercicio 5
paises = ["Ecuador", "Colombia", "Perú", "Chile", "Argentina"]
for i, pais in enumerate(paises):
    print(f"{i}: {pais}")

# Ejercicio 6
materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for i, materia in enumerate(materias):
    print(f"{i}: {materia}")

# Ejercicio 7
autos = ["Toyota", "Nissan", "Chevrolet", "Kia", "Hyundai"]
for i, auto in enumerate(autos):
    print(f"{i}: {auto}")

# Ejercicio 8
numeros_pares = [2, 4, 6, 8, 10]
for i in range(len(numeros_pares)):
    print(f"Índice {i}: {numeros_pares[i]}")

# Ejercicio 9
palabras = ["sol", "luz", "pan", "mar", "voz"]
for palabra in palabras:
    print(f"{palabra} tiene {len(palabra)} letras")

# Ejercicio 10
elementos = [10, "casa", 3.14, True, [1, 2, 3]]
for i, e in enumerate(elementos):
    print(f"{i}: {e}")


# Ejercicio 11
palabras = input("Escribe 3 palabras separadas por espacio: ").split()
print("La palabra más larga es:", max(palabras, key=len))

# Ejercicio 12
palabras = []
while True:
    palabra = input("Escribe una palabra ('fin' para terminar): ")
    if palabra == "fin":
        break
    palabras.append(palabra)
print("La palabra más larga es:", max(palabras, key=len))

# Ejercicio 13
frutas = [input("Fruta: ") for _ in range(5)]
print("Fruta más larga:", max(frutas, key=len))

# Ejercicio 14
palabras = input("Palabras favoritas (separadas por espacio): ").split()
print("Palabra más larga:", max(palabras, key=len))

# Ejercicio 15
amigos = input("Nombres de amigos (espacio entre cada uno): ").split()
print("Nombre más largo:", max(amigos, key=len))

# Ejercicio 16
palabras = input("Palabras sobre tecnología: ").split()
print("Más larga:", max(palabras, key=len))

# Ejercicio 17
animales = [input("Animal: ") for _ in range(5)]
print("Animal más largo:", max(animales, key=len))

# Ejercicio 18
cosas = input("Escribe cosas de la casa: ").split()
print("Más largo:", max(cosas, key=len))

# Ejercicio 19
colores = [input("Color: ") for _ in range(5)]
print("Color más largo:", max(colores, key=len))

# Ejercicio 20
palabras = input("Palabras relacionadas con Python: ").split()
print("Más larga:", max(palabras, key=len))


# Ejercicio 21
texto = input("Ingresa una línea de texto: ").lower().split()
frecuencia = {}
for palabra in texto:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
print(frecuencia)

# Ejercicio 22
for palabra in sorted(frecuencia):
    print(f"{palabra}: {frecuencia[palabra]}")

# Ejercicio 23
print("Texto en minúsculas:")
print(" ".join(palabra.lower() for palabra in texto))

# Ejercicio 24
palabras_comunes = ["el", "la", "y", "de", "a"]
frecuencia_filtrada = {k: v for k, v in frecuencia.items() if k not in palabras_comunes}
print(frecuencia_filtrada)

# Ejercicio 25
texto = input("Otra línea de texto: ").split()
contador = {}
for palabra in texto:
    contador[palabra] = contador.get(palabra, 0) + 1
print(contador)

# Ejercicio 26
for palabra, cantidad in contador.items():
    if cantidad > 1:
        print(f"{palabra}: {cantidad}")

# Ejercicio 27
palabras = input("Texto: ").lower().split()
frecuencia = {}
for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
print(frecuencia)

# Ejercicio 28
linea = input("Texto (no puede estar vacío): ").strip()
if linea:
    print("Correcto")
else:
    print("Cadena vacía")

# Ejercicio 29
from collections import Counter
texto = input("Frase: ").lower().split()
cuenta = Counter(texto)
for palabra, cant in cuenta.most_common():
    print(f"{palabra}: {cant}")

# Ejercicio 30
total = sum(frecuencia.values())
porcentaje = {k: (v / total) * 100 for k, v in frecuencia.items()}
print(porcentaje)


# Ejercicio 31
with open("datos.txt", "r") as archivo:
    palabras = archivo.read().split()
    print("Palabras:", len(palabras))

# Ejercicio 32
from collections import Counter
with open("datos.txt", "r") as archivo:
    palabras = archivo.read().lower().split()
    contar = Counter(palabras)
    print("Top 3 palabras:", contar.most_common(3))

# Ejercicio 33
palabras_largas = [p for p in palabras if len(p) > 4]
print(palabras_largas)

# Ejercicio 34
vocales = ["a", "e", "i", "o", "u"]
con_vocal = [p for p in palabras if p[0] in vocales]
print(con_vocal)

# Ejercicio 35
print("Veces que aparece 'python':", palabras.count("python"))

# Ejercicio 36
import matplotlib.pyplot as plt
palabras, valores = zip(*contar.most_common(3))
plt.bar(palabras, valores)
plt.title("Top 3 Palabras")
plt.show()

# Ejercicio 37
print("Palabras únicas:", len(set(palabras)))

# Ejercicio 38
with open("frecuencias.txt", "w") as salida:
    for palabra, cantidad in contar.items():
        salida.write(f"{palabra}: {cantidad}\n")

# Ejercicio 39
import string
limpio = [p.strip(string.punctuation) for p in palabras]
print(limpio[:10])

# Ejercicio 40
nombre_archivo = input("Nombre del archivo: ")
with open(nombre_archivo, "r") as f:
    contenido = f.read()
    print(contenido)


# Ejercicio 41
productos = {"pan": 0.5, "leche": 1.0, "huevo": 0.2, "arroz": 0.8, "aceite": 2.5}
print(productos)

# Ejercicio 42
p = input("Producto: ")
print(f"Precio de {p} es ${productos.get(p, 'no disponible')}")

# Ejercicio 43
for producto in productos:
    print(f"{producto}: ${productos[producto]}")

# Ejercicio 44
p = input("Producto: ")
cant = int(input("Cantidad: "))
if p in productos:
    print("Total: $", productos[p] * cant)
else:
    print("Producto no encontrado.")

# Ejercicio 45
p = input("Producto a actualizar: ")
nuevo = float(input("Nuevo precio: "))
productos[p] = nuevo
print(productos)

# Ejercicio 46
p = input("Producto a eliminar: ")
if p in productos:
    del productos[p]
print(productos)

# Ejercicio 47
caro = max(productos, key=productos.get)
print("Producto más caro:", caro)

# Ejercicio 48
barato = min(productos, key=productos.get)
print("Producto más barato:", barato)

# Ejercicio 49
total = sum(productos.values())
print("Total si compras 1 de cada uno: $", total)

# Ejercicio 50
with open("inventario.txt", "w") as f:
    for prod, precio in productos.items():
        f.write(f"{prod}: {precio}\n")
