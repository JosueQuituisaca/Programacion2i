#Leer archivos línea por línea hasta fin de archivo.
f = open("archivo.txt", "r")
linea = f.readline()
while linea != "":
    print(linea, end="")
    linea = f.readline()
f.close()
print("fin del programa")



