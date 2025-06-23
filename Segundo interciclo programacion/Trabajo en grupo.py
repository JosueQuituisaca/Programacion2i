#•	Juego del número secreto
import random
def juego_numero_secreto():
    numero_secreto = random.randint(1, 100)
    num = int(input("Dame un número: "))
    while num != numero_secreto:
        if num < numero_secreto:
            print("El número es mayor")
        else:
            print("El número es menor")
        num = int(input("Dame un número: "))
    print("¡Felicidades! ¡Ganaste!")
juego_numero_secreto()  
print("\n")

def menu_matematico():
    print("Bienvenido al Menú Matemático Interactivo")
    nombre_usuario = input("Por favor, ingresa tu nombre: ")
    print(f"Hola {nombre_usuario}, ¡bienvenido!")

    while True:
        print("\nElige una operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Salir")
        opcion = input("Ingresa el número de la operación que deseas realizar: ")
        if opcion == '4':
            print("Gracias por usar el Menú Matemático Interactivo. ¡Hasta luego!")
            break
        elif opcion in ['1', '2', '3']:
            try:
                numero1 = float(input("Ingresa el primer número: "))
                numero2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Por favor, ingresa números válidos.")
                continue
            if opcion == '1':
                resultado = numero1 + numero2
                print(f"El resultado de sumar {numero1} y {numero2} es: {resultado}")
            elif opcion == '2':
                resultado = numero1 - numero2
                print(f"El resultado de restar {numero1} y {numero2} es: {resultado}")
            elif opcion == '3':
                resultado = numero1 * numero2
                print(f"El resultado de multiplicar {numero1} y {numero2} es: {resultado}")
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 4.")
menu_matematico()