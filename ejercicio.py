
promedios = []
bestPro = []
failPro =[]
canPro = 0
ProFinal = 0

while True:
    canPro = int(input('Promedio: '))
    if canPro == 0:
        break;
    promedios.append(canPro)
    if canPro > 9:
        bestPro.append(canPro)
    if canPro < 4:
        failPro.append(canPro)
    ProFinal += canPro

promedios.sort(reverse=True)
final= ProFinal / len(promedios)

print(f'Promedios {promedios}')
print(f'Mejor Promedio :{bestPro}')
print(f'Peor Promedio :{failPro}')
print(f'Promedio Grupal : {final}')

for n in promedios:
    print(f'-----{n}')






