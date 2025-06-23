nueva_linea = "Nueva línea agregada.\n"

with open("salida.txt", "a", encoding="utf-8") as archivo:
    archivo.write(nueva_linea)

# Este código abre el archivo "salida.txt" en modo añadir ("a"), 
# que permite escribir al final sin borrar el contenido anterior. 
# Se define una línea nueva y se agrega al archivo. Esto es útil para guardar 
# información extra sin perder lo que ya está guardado.


