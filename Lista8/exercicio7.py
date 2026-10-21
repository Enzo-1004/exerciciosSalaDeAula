print('Olá digite a equação afim que descreve a trajetória do tiro. Formato: y = ax + b')
a = int(input('Digite o valor de (a): '))
b = int(input('Digite o valor de (b): '))
matriz = []

for i in range(5):
    matriz.append([0]*5)

quantTiros=0
for i in range(5):
    for j in range(5):
        tiro = (a*j) + b
        if tiro == i:
            matriz[i][j]=1
            quantTiros+=1

for i in range(4, -1, -1):
    print(matriz[i])

if(quantTiros>10):
    print(f'O agente não conseguiu desviar dos {quantTiros} tiros')
else:
    print(f'O agente conseguiu desviar dos {quantTiros} tiros')

