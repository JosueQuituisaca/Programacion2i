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