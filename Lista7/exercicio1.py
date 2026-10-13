vetor = [0] * 10
for i in range(10):
    vetor[i] = int(input('Digite um número: '))
print('\nNumeros digitados: ')
for i in range(10):
    print(f'{vetor[i]}, ', end='')