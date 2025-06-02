#1.	Crear una función multiplicar(x, y) que retorne el producto de dos números.
def multiplicar(x, y):
    return x * y
resultado = multiplicar(3, 4)
print(resultado)  
#2.	Crear una función es_par(numero) que retorne True si el número es par.
def es_par(numero): 
    return numero % 2 == 0 
resultado = es_par(4)
print(resultado)
#3.	Crear una función presentarse(nombre, edad) y que imprima un mensaje con tus datos. 
def presentarse(nombre, edad):
    print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")
presentarse('Josue', 18)

