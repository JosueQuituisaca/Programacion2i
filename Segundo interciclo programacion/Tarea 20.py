conteo=0
suma=0
print('antes',conteo,suma)
for valor in [9,41,12,3,74,15]:
    conteo=conteo+1
    suma=suma+valor
    print(conteo,suma,valor)
print('Despues',conteo,suma,suma/conteo)