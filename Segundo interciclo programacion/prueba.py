documento = open('mbox.txt')
for linea in documento:
    if linea.startswith('from:'):
        print(linea)