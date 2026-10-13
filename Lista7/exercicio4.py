import random
v1 = [0] * 10
v2 = [0] * 10
for i in range(10):
    v1[i] = random.randint(10, 50)
    v2[i] = random.randint(10, 50)


print(f'Vetor v1: [', end='')
for i in range(10):
    print(f'{v1[i]}  ', end='')

print(f']\nVetor v2: [', end='')
for i in range(10):
    print(f'{v2[i]}  ', end='')

v3 = [0] * 10
print(f']\nVetor v3: [', end='')
for i in range(10):
    v3[i] = v1[i] + v2[i]
    print(f'{v3[i]}  ', end='')
print(f']\n')