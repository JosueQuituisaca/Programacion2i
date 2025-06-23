man_a= open('mbox.txt')
for linea in man_a:
    linea = linea.rstrip()
    if not linea.startswith('from:'):
        continue
    print(linea)
