def fatorial(a):
    if a == 1:
        return 1
    else:
        return a * fatorial(a-1)

a = int(input('Digite um número: '))
print(f'O fatorial de {a} é {fatorial(a)}')