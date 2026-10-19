def fatorial(n):
    for i in range(n-1, 1, -1):
        n*=i

    return n

def combinacao(n, k):
    if k==n:
        return 1
    else:
        return fatorial(n)/(fatorial(k)*fatorial(n-k))


n=-2
k=-1
while n<k:
    n = int(input('Qual é o número total de pessoas?: '))
    while n<1:
        n = int(input('Qual é o número total de pessoas?: '))
    k = int(input('Quantas pessoas terá cada time?: '))
    while k<1:
        k = int(input('Quantas pessoas terá cada time?: '))


print(f'Existem {combinacao(n, k)} combinações de times diferentes que podem ser feitas.')