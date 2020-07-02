import random

print('\33[1;32m==\33[m'*20)
print('\33[1;32mJOKENPÔ\33[m'.rjust(33))
print('\33[1;32m==\33[m'*20)

print('** Pedra, Papel ou tesoura ! **')
jogo = ['PEDRA', 'PAPEL', 'TESOURA']
x = random.choice(jogo)

jogada = str(input('Qual a sua jogada ? '))

if 'PAPEL' in jogada.upper() and 'PAPEL' in x or 'PEDRA' in jogada.upper() and 'PEDRA' in x or\
        'TESOURA' in jogada.upper() and 'TESOURA' in x:
    print('Jogada do Computador: {}'.format(x))
    print('\33[7mEmpate !\33[m')

elif 'PAPEL' in jogada.upper() and 'TESOURA' in x or 'TESOURA' in jogada.upper() and 'PEDRA' in x or\
        'PEDRA' in jogada.upper() and 'PAPEL' in x:
    print('Jogada do Computador: {}'.format(x))
    print('\33[1;31mVocê Perdeu !\33[m')

else:
    print('Jogada do Computador: {}'.format(x))
    print('\33[1;34mVocê Ganhou !\33[m')