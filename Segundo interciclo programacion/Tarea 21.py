#Escribe un programa que use un bucle while para imprimir números desde el 10 hasta el 1.
#Después de que el bucle termine, imprime el mensaje "¡Despegue!".
contador = 10
while contador >= 1:
    print(contador)
    contador -= 1
print("¡Despegue!")
print("\n")
#Escribe un programa que defina una palabra secreta (por ejemplo, puedes usar "python").
#Utiliza un bucle while True para solicitar continuamente al usuario que ingrese una palabra.
#Si la palabra ingresada por el usuario coincide con la palabra secreta, el programa debe imprimir "¡Has adivinado la palabra!" y luego terminar el bucle usando la sentencia break. 
#Si la palabra ingresada no es correcta, el programa debe imprimir "Inténtalo de nuevo." y continuar pidiendo otra palabra.
palabra_secreta = "python"
while True:
    palabra = input("Ingresa una palabra: ")
    if palabra == palabra_secreta:
        print("¡Has adivinado la palabra!")
        break
    else:
        print("Inténtalo de nuevo.")
        continue
print("Fin del juego")
print("\n")
#Escribe un programa que pida al usuario que ingrese texto repetidamente usando un bucle while True.
#Si el usuario ingresa el carácter "#", el programa debe ignorar completamente esa entrada (es decir, no hacer nada con ella y no imprimir nada) y pasar a la siguiente iteración para pedir una nueva entrada. Para esto, utiliza la sentencia continue. 
#Si el usuario ingresa la palabra "listo" (en minúsculas), el programa debe imprimir el mensaje "¡Procesamiento terminado!" y luego finalizar.
#Para cualquier otra entrada de texto que no sea "#" ni "listo", el programa debe imprimir esa misma entrada pero convertida a mayúsculas.
while True:
    texto = input("Ingresa texto: ")
    if texto == "#":
        continue
    elif texto == "listo":
        print("¡Procesamiento terminado!")
        break
    else:
        print(texto.upper())
        continue
print("Fin del programa")
print("\n")
#Define una lista de nombres de amigos. Por ejemplo: invitados = ['Ana', 'Luis', 'Carla', 'Pedro'].
#Utiliza un bucle for para iterar sobre cada nombre en la lista invitados.
#Dentro del bucle, para cada amigo, imprime un saludo personalizado. Por ejemplo, si el nombre es "Ana", debe imprimir "Hola Ana, ¡bienvenida a la fiesta!".
invitados = ['Ana', 'Luis', 'Carla', 'Pedro']
for nombre in invitados:
    print(f"Hola {nombre}, ¡bienvenido a la fiesta!")
print("\n")
#Se proporciona la siguiente lista de números: numeros = [3, 41, 12, 9, 74, 15, 1, 55].
#Escribe un programa que utilice un bucle for para recorrer esta lista y encontrar cuál es el número más grande.
#Antes de comenzar el bucle, inicializa una variable, por ejemplo mayor_hasta_ahora, con un valor muy pequeño (o con el primer elemento de la lista, o con -1 como se sugiere en la presentación si se asume que todos los números serán positivos). 
#Dentro del bucle, compara cada número de la lista con tu variable mayor_hasta_ahora. Si el número actual es mayor, actualiza mayor_hasta_ahora con este número. 
#Al finalizar el bucle, imprime el valor de mayor_hasta_ahora, que será el número más grande encontrado.
numeros = [3, 41, 12, 9, 74, 15, 1, 55]
mayor_hasta_ahora = -1
for numero in numeros:
    if numero > mayor_hasta_ahora:
        mayor_hasta_ahora = numero
print("El número más grande es:", mayor_hasta_ahora)
print("\n")
#Se proporciona la siguiente lista de números: numeros = [2, 5, 8, 11, 14, 17, 20, 23].
#Escribe un programa que utilice un bucle for para contar cuántos de los números en esta lista son pares.
#Inicializa una variable contador a 0 antes del bucle. 
#Dentro del bucle, verifica si cada número es par (puedes usar el operador módulo %: un número es par si numero % 2 == 0).
#Si un número es par, incrementa tu variable contador.
#Al finalizar el bucle, imprime el valor total del contador.
numeros = [2, 5, 8, 11, 14, 17, 20, 23]
contador = 0
for numero in numeros:
    if numero % 2 == 0:
        contador += 1
print(contador)
print("\n")
#Se proporciona la siguiente lista de números: numeros = [10, 20, 30, 40, 50].
#Escribe un programa que utilice un bucle for para calcular la suma de todos los números presentes en la lista.
#Inicializa una variable, por ejemplo suma_total, a 0 antes de comenzar el bucle. 
#Dentro del bucle, acumula la suma de cada número en suma_total. 
#Al finalizar el bucle, imprime el valor de suma_total.
numeros = [10, 20, 30, 40, 50]
suma_total = 0
for numero in numeros:
    suma_total += numero
print(suma_total)
print("\n")
#Se proporciona la siguiente lista de números: numeros = [10, 15, 20, 25, 30].
#Escribe un programa que utilice un bucle for para calcular el promedio de los números en esta lista.
#Para calcular el promedio, necesitarás dos cosas: la suma de todos los números y la cantidad total de números. 
#Puedes usar una variable para la suma (inicializada en 0) y otra para el conteo (inicializada en 0), actualizándolas en cada iteración del bucle. 
#Al finalizar el bucle, calcula el promedio dividiendo la suma total entre la cantidad total de números.
#Imprime el promedio calculado.
numeros = [10, 15, 20, 25, 30]
suma_total = 0
cantidad_total = 0
for numero in numeros:
    suma_total += numero
    cantidad_total += 1
promedio = suma_total / cantidad_total
print("El promedio es:", promedio)
#Filtrando Números Mayores que un Valor (for)
#Se proporciona la siguiente lista de números: numeros = [5, 25, 12, 33, 18, 45, 7].
#Escribe un programa que primero solicite al usuario que ingrese un número umbral (este será el valor con el cual comparar).
#Luego, utiliza un bucle for para iterar sobre la lista numeros.
#Dentro del bucle, si un número de la lista es estrictamente mayor que el número umbral ingresado por el usuario, imprime ese número. 
numeros = [5, 25, 12, 33, 18, 45, 7]
umbral = int(input("Ingresa un número umbral: "))
for numero in numeros:
    if numero > umbral:
        print(numero) 
print("\n")
#Búsqueda de un Valor Específico (for y booleano)
#Se proporciona la siguiente lista de números: numeros = [9, 41, 12, 3, 74, 15].
#Escribe un programa que verifique si el número 3 está presente en esta lista.
#Utiliza una variable booleana, por ejemplo encontrado, e inicialízala en False antes del bucle. 
#Recorre la lista con un bucle for. Si encuentras el número 3, cambia el valor de la variable encontrado a True. Puedes optar por usar break para salir del bucle una vez encontrado, aunque no es estrictamente necesario para este ejercicio.
#Después del bucle, imprime un mensaje que indique si el valor fue encontrado o no, basándote en el estado final de la variable encontrado. Por ejemplo: "El valor 3 fue encontrado: True" o "El valor 3 fue encontrado: False".
numeros = [9, 41, 12, 3, 74, 15]
encontrado = False
for numero in numeros:
    if numero == 3:
        encontrado = True
        break
print(f"El valor 3 fue encontrado: {encontrado}")
print("\n")
#Encontrando el Número Menor (for y None)
#Se proporciona la siguiente lista de números: numeros = [30, 10, 5, 25, 50, 2].
#Escribe un programa que utilice un bucle for para encontrar el número más pequeño en la lista.
#Inicializa una variable, por ejemplo menor_hasta_ahora, con el valor especial None antes de comenzar el bucle. 
#Dentro del bucle, en cada iteración: 
#Si menor_hasta_ahora es None (lo cual será cierto en la primera iteración), asigna el número actual de la lista a menor_hasta_ahora. 
#Si no, compara el número actual de la lista con menor_hasta_ahora. Si el número actual es menor, actualiza menor_hasta_ahora con este número. 
#Para verificar si menor_hasta_ahora es None, utiliza el operador is (ej. if menor_hasta_ahora is None:). 
#Al finalizar el bucle, imprime el valor de menor_hasta_ahora, que será el número más pequeño encontrado.
numeros = [30, 10, 5, 25, 50, 2]
menor_hasta_ahora = None
for numero in numeros:
    if menor_hasta_ahora is None:
        menor_hasta_ahora = numero
    elif numero < menor_hasta_ahora:
        menor_hasta_ahora = numero
print("El número más pequeño es:", menor_hasta_ahora)
#12
n = 5
while n > 0:
    print("Enjabnar")
    print("Enjaguar")
print("Secar")
print("\n")

