import random

def leMatriz():
    matriz = []
    for i in range(4):
        vetor = []
        for j in range(4):
            vetor.append(random.randint(0, 5))
        matriz.append(vetor)
    return matriz

def realizaSoma(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
    return soma


matriz = leMatriz()
print(matriz)
print(realizaSoma(matriz))