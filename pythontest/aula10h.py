print('\33[1;35m-=\33[m'*20)
print('\33[1;32mAnalisador de Triângulos\33[m')
print('\33[1;35m-=\33[m'*20)
com1 = float(input('\33[0;37mDigite o comprimento de um lado do triângulo:\33[m '))
com2 = float(input('\33[0;33mDigite o compriment do segundo lado do triângulo:\33[m '))
com3 = float(input('\33[0;34mDigite o comprimento do terceiro lado do triângulo:\33[m '))

if com1 > com2 + com3 or com2 > com1 + com3 or com3 > com1 + com2:
    print('\33[1;31mEsses comprimentos não podem formar um triângulo !\33[m')

else:
    print('\33[0;36mEsses comprimento podem formar um triângulo !\33[m')