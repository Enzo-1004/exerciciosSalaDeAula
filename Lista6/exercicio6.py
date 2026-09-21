tamanhoTime = int(input('Informe a quantidade de jogadores por time: '))
forca1 = 0
forca2 = 0
for i in range(2):
    print('\nEquipe ', i+1)
    for j in range(tamanhoTime):
        print('Jogador ', j+1)
        altura = float(input('Informe a altura: '))
        while altura<= 0:
            altura = float(input('Informe a altura: '))
        idade = int(input('Informe a idade: '))
        while idade<=0:
            idade = int(input('Informe a idade: '))
        sexo = input('Informe sexo f-feminino m-masculino: ')
        while sexo!='f' and sexo!='m':
            sexo = input('Informe sexo f-feminino m-masculino: ')
            
        modificador = 1
        if idade >= 50:
            modificador = 0.7
        elif sexo == 'f':
            modificador = 0.9

        if i == 0:
            forca1 += 10*altura*modificador
        else:
            forca2 += 10*altura*modificador

print('\nResultado: ')
if forca1 == forca2:
    print('Empate!')
elif forca1 > forca2:
    print('Equipe 1 ganhou!')
else:
    print('Equipe 2 ganhou!')

