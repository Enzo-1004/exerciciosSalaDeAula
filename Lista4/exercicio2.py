def fatorial(num):
    for i in range(num-1, 1, -1):
        num*=i
    return num

def somatorio(numero):
    somatorio = 0
    if numero == 1 or numero ==0:
        return 1
    else:
        for i in range(numero, 0, -1):
            somatorio += 1/fatorial(i)
        return somatorio

numero = int(input('Digite um número: '))
print('Somatório = ',somatorio(numero))