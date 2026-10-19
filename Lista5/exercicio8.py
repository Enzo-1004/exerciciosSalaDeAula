idade = int(input('\nDigite sua idade (0 para sair): '))
cont3 = 0
maiorQuantLivros = 0
naoGostamRedacao = 0
somaIdade = 0
contIdade = 0
while idade>0:
    serie = int(input('Informe sua série 1-4: '))
    while serie<1 or serie>4:
        serie = int(input('Informe sua série 1-4: '))
    qtdLivros = int(input('Informe a quantidade de livros/mes: '))
    while qtdLivros<0:
        qtdLivros = int(input('Informe a quantidade de livros/mes: '))
    redacao = input('Gosta de fazer redação S-Sim N-Não: ')
    # while(redacao.upper!='S' and redacao.upper!='N'):
    #     redacao = input('Gosta de fazer redação S-Sim N-Não: ')
    if serie == 1 or serie == 2:
        somaIdade += idade
        contIdade += 1
    if serie == 3:
        cont3+=1
        if redacao in 'N':
            naoGostamRedacao+=1
    if serie == 4 and qtdLivros > maiorQuantLivros:
        maiorQuantLivros = qtdLivros
    idade = int(input('\nDigite sua idade (0 para sair): '))

print("Quantidade de pessoas na terceira série = ",cont3)
print("Maior quantidade de livros lidos por alguém da quarta série = ",maiorQuantLivros)
print("Porcentagem de pessoas na terceira série que não gostam de livros = ",(naoGostamRedacao/cont3)*100, "%")
print("Média de idade dos alunos da primeira e segunda série: ",(somaIdade/contIdade))
