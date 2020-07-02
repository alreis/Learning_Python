print('\033[1;34mCalculador de volume de esferas.\033[m')
r = int(input('Insira o raio da esfera: '))
print('O volume da esfera com raio = \033[1;31m{}\033[m é: \033[1;33m{:.3f}\033[m'.format(r, (4/3.0)*3.14159*r**3))