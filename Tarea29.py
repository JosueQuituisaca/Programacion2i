#Sumar números ingresados por el usuario hasta que ingrese 0.
total = 0
numero = 1  
while numero != 0:
    numero = int(input("Ingresa un número (0 para terminar): "))
    if numero != 0:  
        total += numero
print(f"La suma total es: {total}")

#Adivinar un número aleatorio entre 1 y 100 (pistas: "mayor" o "menor").

import random
aleatorio = random.randint(1,100)
print(aleatorio)
print("Adivina el número")
num = int(input("Dame un número: "))
while num != aleatorio:
    if num < aleatorio:
        print("El número es mayor")
    else:
        print("El número es menor")
    num = int(input("Dame un número: "))
print("felicidades has adivinado el número")

#Validar contraseña (repetir hasta que coincida con una guardada).

contraseña= input("ingrese contraseña: ")
while contraseña != "jaqd2006":
    print("contraseña incorrecta")
    contraseña= input("ingrese contraseña: ")
print("contraseña correcta")

#Simular un cajero automático (menú: retirar, depositar, salir).
saldo = 100  
activo = True  

print("Bienvenido al Cajero Automático")
print("Saldo inicial:", saldo)

while activo:
    print("\nMenú:")
    print("1. Retirar dinero")
    print("2. Depositar dinero")
    print("3. Consultar saldo")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == "1":
        monto = float(input("Ingrese el monto a retirar: "))
        if monto > saldo:
            print("Saldo insuficiente")
        else:
            saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: {saldo}")
    
    elif opcion == "2":
        monto = float(input("Ingrese el monto a depositar: "))
        saldo += monto
        print(f"Depósito exitoso. Nuevo saldo: {saldo}")
    
    elif opcion == "3":
        print(f"Su saldo actual es: {saldo}")
    
    elif opcion == "4":
        print("Gracias por usar el cajero. ¡Hasta luego!")
        activo = False  # Salimos del bucle
    
    else:
        print("Opción inválida. Intente nuevamente.")

#Calcular la raíz cuadrada por aproximación (método babilónico).

def raiz_babilonica(n, aproximacion_inicial=1.0, iteraciones=10):
    x = aproximacion_inicial
    for i in range(iteraciones):
        x = (x + n / x) / 2
        print(f"Iteración {i+1}: {x}")
    return x 
n = float(input("Ingrese un número: "))
raiz = raiz_babilonica(n)
print(f"La raíz cuadrada de {n} es aproximadamente {raiz}")

#Contar dígitos de un número entero (ej: 456 → 3).

print("Ingrese un número entero: ")
num = int(input())
cont = 0
while num > 0:
    num = num // 10
    cont += 1
print(f"El número tiene {cont} dígitos")

#Generar la secuencia de Fibonacci hasta un límite.
limite = int(input("Ingrese el límite de la secuencia de Fibonacci: "))
a, b = 0, 1
while a < limite:
    print(a, end=" ")
    a, b = b, a + b
print()
print("Secuencia de Fibonacci hasta el límite:", limite)

#Encontrar números primos en un rango dado. 
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
inicio = int(input("Ingrese el número de inicio del rango: "))
fin = int(input("Ingrese el número de fin del rango: "))
print("Números primos en el rango",inicio, "a",fin, ":")
for numero in range(inicio,fin + 1):
    if es_primo(numero):
        print(numero)
print("rango final")

#Simular un temporizador (contar regresivamente desde n).
print("Programa para contar regresivamente desde n")
n=int(input("ingrese el numero: "))
print("Contando regresivamente desde n")
while n>=0:
    print(n)
    n=n-1
print("Fin")

#Leer archivos línea por línea hasta fin de archivo.

#MIENTRAS - WHILE
#visulisar los 5 primeros numeros con mientras = while

contador = 0
while contador <= 100:
    print("numero", contador)
    contador = contador + 1
print("fin del programa")