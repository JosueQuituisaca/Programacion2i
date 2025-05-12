#Contar dígitos de un número entero (ej: 456 → 3).
print("Ingrese un número entero: ")
num = int(input())
cont = 0
while num > 0:
    num = num // 10
    cont += 1
print(f"El número tiene {cont} dígitos")
