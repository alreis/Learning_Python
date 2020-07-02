ano = int(input('Digite um ano: '))
if (ano % 4 != 0 + ano % 400 != 0 + ano % 100 == 0):
    print('{} não é um ano Bissexto !'.format(ano))
else:
    print('{} é um ano Bissexto !'.format(ano))