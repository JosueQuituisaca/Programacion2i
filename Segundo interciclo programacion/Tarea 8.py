#1. Crear una función que imprima un mensaje.Escribe una función llamada saludo() que imprima '¡Hola, mundo!'.
def saludo():
    print("¡Hola, mundo!")
saludo()
print("\n")
#2. Función con un argumento.Crea una función llamada saludar(nombre) que imprima 'Hola, <nombre>'.
def saludar(nombre):
    print("Hola, " + nombre)
saludar("Josue")
print("\n")
#3. Suma de dos números.Define una función sumar(a, b) que retorne la suma de ambos números.
def sumar(a, b):
    return a + b
print(sumar(1, 2))
print("\n")
#4. Calcular el salario .Escribe la función computepay(horas, tarifa) para calcular el pago con horas extra.
def computepay(horas, tarifa):
    if horas > 40:
        horas_extras = horas - 40
        pago = (40 * tarifa) + (horas_extras * (tarifa * 1.5))
    else:
        pago = horas * tarifa
    return pago
horas = float(input("Ingrese las horas trabajadas: "))
tarifa = float(input("Ingrese la tarifa por hora: "))
pago = computepay(horas, tarifa)
print("El pago es: ", pago)
print("\n")
#5. Función para determinar el mayor carácter.Escribe una función mayor_caracter(cadena) que retorne el carácter mayor en una cadena.
def mayor_caracter(cadena):
    mayor = cadena[0]
    for i in range(1, len(cadena)):
        if cadena[i] > mayor:
            mayor = cadena[i]
    return mayor
print(mayor_caracter("hola mundo"))
print("\n")
#6. Conversión de tipo.crea una función convertir_a_flotante(valor) que intente convertir una cadena a float
def convertir_a_flotante(valor):
    try:
        return float(valor)
    except ValueError:

        return None 
valor = input("Ingrese un valor: ")
resultado = convertir_a_flotante(valor)
if resultado is not None:
    print(f"El valor {valor} se convirtió en {resultado} como float.")
else:
    print(f"El valor {valor} no se pudo convertir a float.")
print("\n")
#7. Función que retorna un saludo en diferentes idiomas.Escribe saludo_idioma(lang) que retorne 'Hola' si es 'es', 'Bonjour' si es 'fr', y 'Hello' por defecto
def saludo_idioma(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'
print(saludo_idioma('es'))
print(saludo_idioma('fr'))
print(saludo_idioma('en'))
print("\n")
#8. Comprobar si un número es par.Crea una función es_par(numero) que retorne True si el número es par.
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
print(es_par(10))
print("\n")
#9. Concatenar cadenas.Crea una función concatenar(cad1, cad2) que retorne la concatenación de ambas cadenas
def concatenar(cad1, cad2):
    return cad1 + cad2 
print(concatenar("hola", "mundo"))
print("\n")
#10. Calcular promedio.Define una función promedio(lista) que calcule el promedio de una lista de números.
def promedio(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    promedio = suma / len(lista)
    return promedio
print(promedio([1,2,3,4,5,6,7,8,9,10]))
print("\n")
#11. Contar vocales.Escribe contar_vocales(cadena) que retorne cuántas vocales hay en la cadena.
def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador += 1
    return contador
print(contar_vocales("hola mundo"))
print("\n")
#12. Revertir cadena.Define una función invertir(cadena) que devuelva la cadena al revés.
def invertir(cadena):
    return cadena[::-1]
print(invertir("hola mundo"))
print("\n")

#13. Tabla de multiplicar.Crea una función tabla(numero) que imprima la tabla de multiplicar del número del 1 al 10.
def tabla(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
tabla(5)
print("\n")

#14. Función sin parámetros.Crea una función llamada mensaje() que imprima tres líneas de texto distintas.
def mensaje():
    print("Esta es la primera línea.")
    print("Aquí va la segunda línea.")
    print("Y esta es la tercera línea.")
mensaje()
print("\n")

#15. Función que retorne el número más pequeño.Define menor_valor(lista) que retorne el número más pequeño de una lista.
def menor_valor(lista):
    menor = lista[0]
    for numero in lista:
        if numero < menor:
            menor = numero
    return menor
print(menor_valor([5, 3, 9, 1, 7]))
print("\n")

#16. Calcular factorial.Crea una función factorial(n) que calcule el factorial de un número.
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
print(factorial(5))
print("\n")

#17. Determinar si un número es primo.Escribe una función es_primo(numero) que retorne True si es primo, False si no.
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True
print(es_primo(7))
print(es_primo(10))
print("\n")

#18. Repetir una cadena n veces.Crea una función repetir(cadena, n) que retorne la cadena repetida n veces.
def repetir(cadena, n):
    return cadena * n
print(repetir("hola", 3))
print("\n")

#19. Función con múltiples parámetros.Define una función descripcion(nombre, edad, ciudad) que imprima una frase con esos datos.
def descripcion(nombre, edad, ciudad):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}.")
descripcion("Ana", 25, "Madrid")
print("\n")

#20. Verificar palíndromo.Escribe es_palindromo(cadena) que retorne True si la cadena es un palíndromo.
def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")
    return cadena == cadena[::-1]
print(es_palindromo("Anita lava la tina"))
print(es_palindromo("hola"))
print("\n")
