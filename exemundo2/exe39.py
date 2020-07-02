ano = int(input('Qual o seu ano de nascimento ? '))

if 2019 - ano == 18:
    print('Esta na hora de se alistar !')

elif 2019 - ano < 18:
    print('Falta(m) {} ano(s) para você se alistar !'.format(18 - (2019 - ano)))

else:
    print('Você deveria ter se alistado a {} ano(s) atras !'.format((18 - (2019 - ano))*(-1)))
