#1.	Crear una función multiplicar(x, y) que retorne el producto de dos números.
def multiplicar(x, y):
    resultado=x * y
    return resultado
print('multiplicacion es', multiplicar(4,8))  
#2.	Crear una función es_par(numero) que retorne True si el número es par y false si es impar.
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
numero = int(input("Ingrese un número: "))
if es_par(numero):
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

#3.	Crear una función presentarse(nombre, edad) y que imprima un mensaje con tus datos. 
def presentarse(nombre, edad):
    print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
presentarse(nombre, edad)
