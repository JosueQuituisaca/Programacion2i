#crear un menú de ARCHVOS 1.CREAR ARCHIVO 2. NUEVO Y QUE YO PUEDA PONER EL NOMBRE .3.ESCRIBIR EN EL ARCHIVO 4.ELIMINAR

def crear_archivo(nombre):    
    with open(nombre, 'w') as archivo:        
        archivo.write("")  
        print(f"Archivo '{nombre}' creado.")
def nuevo_archivo():
    nombre = input("Ingrese el nombre del nuevo archivo: ")
    crear_archivo(nombre)
    print(f"Archivo '{nombre}' creado.")
def escribir_en_archivo(nombre):
    contenido = input("Ingrese el contenido a escribir en el archivo: ")
    with open(nombre, 'a') as archivo:        
        archivo.write(contenido + "\n")      
        print(f"Contenido escrito en el archivo '{nombre}'.")
def eliminar_archivo(nombre):
    import os
    os.remove(nombre)
    print(f"Archivo '{nombre}' eliminado.")
def mostrar_menu():
    print("\nMenú de Archivos:")
    print("1. Crear archivo")
    print("2. Nuevo archivo")
    print("3. Escribir en archivo")
    print("4. Eliminar archivo")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion
def menu():
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            nombre = input("Ingrese el nombre del archivo a crear: ")
            crear_archivo(nombre)
        elif opcion == '2':
            nuevo_archivo()
        elif opcion == '3':
            nombre = input("Ingrese el nombre del archivo en el que desea escribir: ")
            escribir_en_archivo(nombre)
        elif opcion == '4':
            nombre = input("Ingrese el nombre del archivo a eliminar: ")
            eliminar_archivo(nombre)
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
    menu()