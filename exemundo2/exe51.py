print('10 Primeiros termos de uma PA!')

pri = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a razão: '))
dec = pri + (10 - 1) * razao
for c in range(pri, dec + razao, razao):
    print('{}'.format(c), end=' →')
print('FIM')