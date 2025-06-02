while True:
    line = input('> ingrese un caracter ')
    if line[0]=='#':
        continue
    if line == 'terminado':
        break
    print(line)
print('terminado') 
print('\n')

for i in [5,4,3,2,1]:
    print(i)
print('Blastoff')