dis = float(input('Insira a distância da viagem em Km: '))

if (dis <= 200):
    print('O preço da passagem é: {:.2f} reais'.format(dis*0.50))

else:
    print('O preço da passagem é: {:.2f} reais'.format(dis*0.45))