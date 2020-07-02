val1 = float(input('Insira o primeiro valor : '))
val2 = float(input('Insira o segundo valor : '))

if val1 > val2:
    print('{} é o maior valor !'.format(val1))

elif val2 > val1:
    print('{} é o maior valor !'.format(val2))

else:
    print('{} e {} são iguais !'.format(val1, val2))