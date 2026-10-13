vetor = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(1, 10, 1):
    if i % 2 == 0:
        vetor[i] = 1
    else:
        vetor[i] = 0

for i in range(10):
    print(f'{vetor[i]}, ', end='')