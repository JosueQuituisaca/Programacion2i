lineas = ["Hola, mundo\n", "Este es un archivo de prueba\n", "Python es genial\n"]

with open("salida.txt", "w", encoding="utf-8") as archivo:
    archivo.writelines(lineas)


#Aquí se crea o reemplaza un archivo llamado "salida.txt". 
# Primero definimos una lista con varias líneas de texto (cada línea termina con \n para salto de línea). 
# El archivo se abre en modo escritura "w" y luego se escriben todas las líneas al archivo. 
# Esto sirve para guardar texto nuevo.