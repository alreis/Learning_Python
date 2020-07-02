'''Programa para financiamento'''
val = float(input('Digite o valor da casa : '))
sal = float(input('Digite seu salario : '))
anos = int(input('Em quantos anos vai financiar ? '))

if val / (anos*12) > sal * 0.30:
    print('\33[1;31mFinanciamento não aprovado !\33[m')
else:
    print('\33[1;32mFinanciamento aprovado !\33[m')
