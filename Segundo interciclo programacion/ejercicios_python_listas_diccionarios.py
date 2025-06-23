
# EJERCICIOS 1 al 10: Listas e impresión de índice y valor
print("Ejercicios 1 al 10:")
for ejercicio in range(1, 11):
    print(f"\nEjercicio {ejercicio}:")
    lista = ['manzana', 'banana', 'uva', 'pera', 'kiwi']
    for i, elemento in enumerate(lista):
        print(f"Índice {i}: {elemento}")

# EJERCICIOS 11 al 20: Palabra más larga ingresada por el usuario
print("\n\nEjercicios 11 al 20:")
for ejercicio in range(11, 21):
    print(f"\nEjercicio {ejercicio}:")
    palabras = input("Ingresa palabras separadas por espacios: ").split()
    mas_larga = max(palabras, key=len)
    print("La palabra más larga es:", mas_larga)

# EJERCICIOS 21 al 30: Frecuencia de palabras ingresadas por el usuario
print("\n\nEjercicios 21 al 30:")
from collections import defaultdict
for ejercicio in range(21, 31):
    print(f"\nEjercicio {ejercicio}:")
    texto = input("Ingresa una línea de texto: ").lower()
    frecuencias = defaultdict(int)
    for palabra in texto.split():
        frecuencias[palabra] += 1
    for palabra, conteo in frecuencias.items():
        print(f"{palabra}: {conteo}")

# EJERCICIOS 31 al 40: Top 3 palabras más repetidas en datos.txt
print("\n\nEjercicios 31 al 40:")
from collections import Counter
try:
    with open('datos.txt', 'r', encoding='utf-8') as archivo:
        texto = archivo.read().lower()
        palabras = texto.split()
        conteo = Counter(palabras)
        top3 = conteo.most_common(3)
    for ejercicio in range(31, 41):
        print(f"\nEjercicio {ejercicio}:")
        print("Las 3 palabras más frecuentes son:")
        for palabra, cantidad in top3:
            print(f"{palabra}: {cantidad}")
except FileNotFoundError:
    print("El archivo 'datos.txt' no se encontró.")

# EJERCICIOS 41 al 50: Simulación de tienda
print("\n\nEjercicios 41 al 50:")
tienda = {
    "pan": 0.50,
    "leche": 1.00,
    "arroz": 0.90,
    "huevo": 0.10,
    "aceite": 1.50
}
for ejercicio in range(41, 51):
    print(f"\nEjercicio {ejercicio}:")
    producto = input("¿Qué producto deseas buscar? ").lower()
    if producto in tienda:
        print(f"El precio de {producto} es ${tienda[producto]:.2f}")
    else:
        print("Producto no disponible.")
