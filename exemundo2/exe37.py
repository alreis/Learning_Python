num = int(input('Digite um numero inteiro: '))
print('''\033[1;33;44mEscolha uma das bases para converção:\033[m
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL  é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opçãõ invalida ! Tente novamente.')