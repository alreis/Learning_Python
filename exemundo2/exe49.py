num = int(input('Digite um numero para saber sua tabuada: '))
for c in range(1, 10+1):
    print('{} x {} = {}'.format(num, c, num*c))