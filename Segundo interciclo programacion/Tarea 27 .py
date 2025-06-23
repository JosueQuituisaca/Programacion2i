# Leer el archivo archivo.txt
with open("archivo.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())

#Este código abre el archivo llamado "archivo.txt" para leer su contenido. 
# Usa un ciclo para recorrer línea por línea el
# archivo y con strip() elimina espacios o saltos de línea extras para que el texto se vea limpio. 
# Después, muestra cada línea en pantalla. El archivo se cierra solo cuando termina de leer.

#El encoding le dice a Python cómo leer o guardar los caracteres en un archivo, 
# especialmente las letras con acentos o símbolos. 
# Usar encoding="utf-8" evita errores y asegura que los caracteres especiales se manejen bien al leer o escribir archivos.

#(as) sirve para darle un nombre al archivo abierto y usarlo dentro del bloque de código.