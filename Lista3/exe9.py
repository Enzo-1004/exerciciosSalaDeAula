import random

def gera_numero():
    numero = random.randint(1, 10)
    return numero

def verifica_chute(tentativa):
    global num
    if num == tentativa:
        print('Parabéns, você acertou.')
        return True
    elif num < tentativa:
        print('Errado, tente um número mais baixo.')
        return False
    else:
        print('Errado, tente um número mais alto.')
        return False

def jogar():
    tentativa = int(input('Tente adivinhar o número: '))
    global i
    ganhou = verifica_chute(tentativa)
    if i==2:
        print('Limite de tentativas atingido. Você perdeu.')
    elif ganhou==False and i<2:
        i+=1
        jogar()

num = gera_numero()
i = 0
jogar()