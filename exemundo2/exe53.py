print('\033[33mVerificador de palindromo!\033[m')
frase = input('Insira a frase que sera verificada: ')
frase.strip()
if frase == frase[::-1]:
    print('A frase inserida é um palindromo!')
    print('\033[1;32m{}\033[m'.format(frase[::-1]))
else:
    print('\033[1;31mNão é um palindromo!\033[m')
    print('\033[1;031m{}\033[m'.format(frase[::-1]))