vel = int(input('Digite a velocidade do carro: '))

if vel > 80:
    print('Você foi multado !\nA multa vai custar {} reais'.format((vel-80)*7))

else:
    print('Continue na velociade permitida !')