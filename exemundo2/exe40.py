not1 = float(input('Insira a primeira nota : '))
not2 = float(input('Insira a segunda nota : '))
media = (not1 + not2)/2

if media < 5.0:
    print('Aluno \33[1;31mReprovado\33[m !')

elif media >= 5.0 and media < 7.0:
    print('Aluno em \33[1;33mRecuperação\33[m !')

else:
    print('Aluno \33[1;32mAprovado\33[m !')
